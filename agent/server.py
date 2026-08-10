"""
Phase 2: voice backend.

A thin FastAPI wrapper around the same interviewer/evaluator logic used by
the Phase 1 CLI (interviewer.py, evaluator.py, case_loader.py) -- nothing
about the case-gating rules or guardrails changes here, this file only adds
an HTTP surface so a voice platform (ElevenLabs Conversational AI, in
"custom LLM" mode) can call it turn by turn.

Auth: uses a standard Anthropic API key (ANTHROPIC_API_KEY), NOT the Claude
Agent SDK / subscription auth used by the CLI prototype -- because this
server is meant to be used by other people, and Anthropic's usage policy
doesn't allow reselling or sharing subscription-based rate limits to other
users of a third-party product. Get a key from the Claude Console
(platform.claude.com -> API Keys).

Endpoints:
- POST /v1/chat/completions  -- OpenAI-compatible endpoint, ONE ElevenLabs
  Agent for ALL cases (scales to a large case library without creating an
  agent per case). Which case runs is resolved, in priority order, from:
    1. the `case_id` query param (handy for manual/curl testing), or
    2. `elevenlabs_extra_body.case_id` in the request body -- ElevenLabs
       lets you pass an arbitrary `extra_body` dict per conversation via
       their client SDK/widget at call-start time, and forwards it to the
       custom LLM under this field. This is how one Agent can serve many
       cases: your frontend picks the case and passes its id as
       extra_body when starting the voice session, instead of the case
       being baked into the Agent's dashboard config.
  Responds in Server-Sent Events (SSE) format, per ElevenLabs' documented
  custom-LLM protocol (they expect streaming chunks, not a single JSON
  blob, even though our underlying Claude call here is non-streaming --
  we just wrap the one full reply in the expected SSE chunk framing).
  Also writes the running transcript to sessions/ on every call (the
  incoming message list IS the full transcript so far, so this is
  stateless -- no server-side session memory required).
- POST /evaluate  -- given a case_id + session_id (or a transcript
  directly), scores a saved transcript the same way evaluator.py does and
  returns the scorecard as JSON.
- GET  /health  -- for the hosting platform's health checks.

Run locally for testing:
    export ANTHROPIC_API_KEY=sk-ant-...
    uvicorn server:app --reload --port 8000

Deploy: see VOICE_SETUP.md for Render/Fly.io/Railway steps.
"""
import hashlib
import hmac
import json
import logging
import os
import re
import time
import uuid
from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

logger = logging.getLogger("uvicorn.error")

import auth
import billing
from case_loader import load_case
from interviewer import build_system_prompt as build_interviewer_prompt
from evaluator import build_system_prompt as build_evaluator_prompt, format_transcript

BASE_DIR = Path(__file__).parent
CASES_DIR = BASE_DIR / "cases"
# Same DATA_DIR convention as auth.py (see there for why) -- keeps saved
# transcripts on the same persistent volume as users.db, instead of the
# ephemeral container disk.
DATA_DIR = Path(os.environ.get("DATA_DIR", BASE_DIR))
SESSIONS_DIR = DATA_DIR / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

MODEL = "claude-sonnet-5"

app = FastAPI(title="Case Interviewer Voice Backend")

auth.init_db()

# Permissive for development. Restrict allow_origins to your actual
# frontend domain before going live with real users.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def require_user(authorization: Optional[str] = Header(None)) -> dict:
    """FastAPI dependency: pulls the logged-in user off the Authorization
    header, or raises 401. Used on endpoints the browser calls directly
    (like /evaluate) -- NOT on /v1/chat/completions, since that's called
    server-to-server by ElevenLabs and never carries the browser's JWT."""
    try:
        return auth.user_from_bearer_header(authorization)
    except auth.AuthError as exc:
        raise HTTPException(status_code=401, detail=str(exc))


def require_admin(x_admin_secret: Optional[str] = Header(None)) -> None:
    """Guards the /admin/* routes with a separate shared secret (ADMIN_SECRET
    env var) -- deliberately not the same mechanism as user JWTs, since this
    is you looking at the raw database, not a logged-in user action.
    Fails closed: if ADMIN_SECRET isn't set on the server at all, admin
    routes are unreachable rather than silently open."""
    configured = os.environ.get("ADMIN_SECRET")
    if not configured:
        raise HTTPException(status_code=503, detail="Admin access is not configured on this server.")
    if not x_admin_secret or not hmac.compare_digest(x_admin_secret, configured):
        raise HTTPException(status_code=401, detail="Invalid or missing admin secret.")


def get_anthropic_client():
    try:
        from anthropic import Anthropic
    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="The 'anthropic' package isn't installed. Run: pip install anthropic",
        )
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="ANTHROPIC_API_KEY is not set on the server.",
        )
    return Anthropic(api_key=api_key)


def case_path_for(case_id: str) -> Path:
    p = CASES_DIR / f"{case_id}.md"
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"Unknown case_id: {case_id}")
    return p


# ---- Auth ----

class SignupRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/auth/signup")
def signup(req: SignupRequest):
    try:
        user = auth.create_user(req.email, req.password)
    except auth.AuthError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    conn = auth._get_conn()
    row = conn.execute("SELECT id FROM users WHERE email = ?", (user["email"],)).fetchone()
    conn.close()
    token = auth.issue_token(row["id"], user["email"])
    return {"token": token, "email": user["email"]}


@app.post("/auth/login")
def login(req: LoginRequest):
    try:
        user = auth.verify_login(req.email, req.password)
    except auth.AuthError as exc:
        raise HTTPException(status_code=401, detail=str(exc))
    token = auth.issue_token(user["id"], user["email"])
    return {"token": token, "email": user["email"]}


# ---- OpenAI-compatible chat completions ----
#
# NOTE: this endpoint deliberately does NOT use a strict Pydantic request
# model. Every real call from ElevenLabs was failing with 422 Unprocessable
# Content -- FastAPI's automatic validation rejecting the body before our
# code ever ran, most likely because a message's `content` isn't always a
# plain string in whatever ElevenLabs actually sends (some chat-completions
# style APIs send content as a list of parts, e.g.
# [{"type": "text", "text": "..."}], not a bare string). Rather than guess
# again, we parse the raw JSON ourselves, normalize defensively, and log the
# raw body so any future mismatch is visible in Railway's logs instead of
# silently 422ing.

def normalize_content(content) -> str:
    """Coerce whatever shape `content` arrives in into a plain string."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict):
                parts.append(part.get("text") or part.get("content") or "")
        return "".join(parts)
    return str(content)


def normalize_messages(raw_messages) -> list:
    """Turn whatever `messages` looks like into our plain {role, content}
    dict shape, tolerating missing/odd fields instead of raising."""
    normalized = []
    if not isinstance(raw_messages, list):
        return normalized
    for m in raw_messages:
        if not isinstance(m, dict):
            continue
        role = m.get("role") or "user"
        content = normalize_content(m.get("content"))
        normalized.append({"role": role, "content": content})
    return normalized


def sse_chunk(payload: dict) -> str:
    return f"data: {json.dumps(payload)}\n\n"


CASE_ID_MARKER_RE = re.compile(r"CASE_ID:\s*(\S+)")
SESSION_ID_MARKER_RE = re.compile(r"SESSION_ID:\s*(\S+)")


def _marker_from_system_message(messages: list, pattern: "re.Pattern") -> Optional[str]:
    """Shared helper: the Agent's own system-prompt field (set in the
    ElevenLabs dashboard) carries one-line markers like `CASE_ID: {{case_id}}`
    and `SESSION_ID: {{session_id}}`, with the widget's dynamic-variables
    attribute filling in the {{...}} per conversation. ElevenLabs sends the
    resulting text as a system message to this endpoint -- we just read the
    values back out of it. `messages` here is our normalized list of plain
    {role, content} dicts."""
    for m in messages:
        if m["role"] == "system":
            match = pattern.search(m["content"])
            if match:
                return match.group(1)
    return None


def case_id_from_system_message(messages: list) -> Optional[str]:
    return _marker_from_system_message(messages, CASE_ID_MARKER_RE)


def session_id_from_system_message(messages: list) -> Optional[str]:
    """The frontend (web/session.html) generates a random session id
    client-side BEFORE the call starts and passes it through the same
    marker mechanism as case_id. This is the reliable way to correlate a
    saved transcript file with the browser's "Get my scorecard" button --
    capturing ElevenLabs' own internal conversation id after the fact
    wouldn't work, since it's never part of the custom-LLM request body,
    so this server would have no way to know it during the call."""
    return _marker_from_system_message(messages, SESSION_ID_MARKER_RE)


def openai_messages_to_transcript(messages: list) -> list:
    """Map OpenAI-style roles to our {role: interviewer/candidate, text} shape,
    dropping any system messages (our own system prompt is authoritative,
    not whatever the voice platform's dashboard might also send)."""
    transcript = []
    for m in messages:
        if m["role"] == "system":
            continue
        role = "interviewer" if m["role"] == "assistant" else "candidate"
        transcript.append({"role": role, "text": m["content"]})
    return transcript


def transcript_to_anthropic_messages(messages: list) -> list:
    out = []
    for m in messages:
        if m["role"] == "system":
            continue
        anth_role = "assistant" if m["role"] == "assistant" else "user"
        out.append({"role": anth_role, "content": m["content"]})
    if not out:
        # First turn of a brand new call -- same trigger the CLI uses to
        # get the model to open with the case prompt.
        out.append({"role": "user", "content": "[SESSION START -- please begin the interview.]"})
    return out


@app.post("/v1/chat/completions")
async def chat_completions(
    request: Request,
    case_id: Optional[str] = Query(None, description="Which case file to run -- e.g. case_04_pm_satisfaction_drop_figma. Optional if elevenlabs_extra_body.case_id is provided instead."),
    session_id: Optional[str] = Query(None, description="Optional session id, for naming the saved transcript file"),
):
    try:
        body = await request.json()
    except Exception as exc:
        raw = await request.body()
        logger.error("chat_completions: failed to parse JSON body: %s -- raw: %r", exc, raw[:2000])
        raise HTTPException(status_code=400, detail=f"Invalid JSON body: {exc}")

    if not isinstance(body, dict):
        logger.error("chat_completions: body was not a JSON object: %r", body)
        raise HTTPException(status_code=400, detail="Request body must be a JSON object.")

    # Log every incoming payload's shape (not the full transcript text, to
    # keep logs readable) so a future mismatch is visible instead of a bare
    # 422/500 -- this is what a debugging session on this exact endpoint
    # needed and didn't have.
    raw_messages = body.get("messages")
    logger.info(
        "chat_completions: received %d raw message(s), keys=%s",
        len(raw_messages) if isinstance(raw_messages, list) else -1,
        list(body.keys()),
    )

    messages = normalize_messages(raw_messages)
    elevenlabs_extra_body = body.get("elevenlabs_extra_body") or {}

    resolved_case_id = (
        case_id
        or elevenlabs_extra_body.get("case_id")
        or case_id_from_system_message(messages)
    )
    if not resolved_case_id:
        raise HTTPException(
            status_code=400,
            detail="No case_id given -- pass it as a ?case_id= query param, as "
                    "elevenlabs_extra_body.case_id, or via a system message "
                    "containing 'CASE_ID: <id>' (see VOICE_SETUP.md).",
        )

    case = load_case(str(case_path_for(resolved_case_id)))
    system_prompt = build_interviewer_prompt(case)
    anthropic_messages = transcript_to_anthropic_messages(messages)
    client = get_anthropic_client()

    # sid only depends on `messages` (not on the reply), so it's safe to
    # resolve before the Claude call.
    #
    # Priority for naming the file:
    #   1. ?session_id= query param (manual/curl testing)
    #   2. SESSION_ID: <id> marker in a system message -- this is what
    #      web/session.html actually uses: it generates a random id
    #      client-side before the call starts and threads it through via
    #      the widget's dynamic-variables, so the browser already knows
    #      the exact id to ask for later (no manual copy-pasting, and no
    #      dependence on capturing ElevenLabs' own internal conversation id,
    #      which never reaches this server during the call anyway).
    #   3. A hash of case_id + the first CANDIDATE (user-role) message, as a
    #      fallback for callers that don't send the marker at all -- stable
    #      across turns of one call (the platform resends the whole growing
    #      history each turn) without needing any explicit session field.
    #      Hashed off the first USER message rather than messages[0], since
    #      messages[0] is now a fixed per-case opening line spoken directly
    #      by ElevenLabs (see firstMessage in config.js) -- identical for
    #      every candidate on that case, so hashing it would collide
    #      different people's sessions into one file.
    if session_id:
        sid = session_id
    else:
        sid = session_id_from_system_message(messages)
        if not sid:
            first_user_msg = next((m["content"] for m in messages if m["role"] == "user"), None)
            if first_user_msg:
                sid = hashlib.sha1(f"{resolved_case_id}|{first_user_msg}".encode()).hexdigest()[:12]
            else:
                # No user turn yet at all (e.g. a manual curl test with empty
                # messages) -- nothing stable to key off, so use a fresh id.
                sid = uuid.uuid4().hex[:12]

    # Actually stream tokens to ElevenLabs as Claude generates them, instead
    # of blocking on the full response and sending it as one chunk. This
    # used to wait for messages.create() to finish completely before
    # returning anything -- fine for short exchanges, but each turn resends
    # the WHOLE growing transcript, so Claude's response time (and thus
    # time-to-first-byte for ElevenLabs) crept up as a call went on. Once
    # that exceeded ElevenLabs' per-turn response timeout, it dropped the
    # whole conversation and the widget reset to its idle "Start interview"
    # state -- exactly the symptom reported ("varies, but always after a
    # while" + hard reset, not a graceful end). Real streaming keeps
    # time-to-first-token low regardless of how long the reply itself takes.
    def event_stream():
        reply_chunks = []
        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=500,
                system=system_prompt,
                messages=anthropic_messages,
            ) as stream:
                for text in stream.text_stream:
                    reply_chunks.append(text)
                    yield sse_chunk({
                        "id": f"chatcmpl-{sid}",
                        "object": "chat.completion.chunk",
                        "created": int(time.time()),
                        "model": MODEL,
                        "choices": [{"index": 0, "delta": {"role": "assistant", "content": text}, "finish_reason": None}],
                    })
        except Exception as exc:
            # A transient Claude API error (rate limit, timeout, etc.)
            # mid-stream -- have the interviewer say *something* instead of
            # the connection just dying, which is what caused the hard
            # reset before.
            logger.error("chat_completions: error while streaming Claude response: %s", exc)
            if not reply_chunks:
                fallback = "Sorry, could you repeat that?"
                reply_chunks.append(fallback)
                yield sse_chunk({
                    "id": f"chatcmpl-{sid}",
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": MODEL,
                    "choices": [{"index": 0, "delta": {"role": "assistant", "content": fallback}, "finish_reason": None}],
                })

        reply_text = "".join(reply_chunks)

        # Save the running transcript (incoming history + this new reply)
        # now that the full reply is known, so /evaluate can score it later,
        # same shape interviewer.py produces.
        transcript = openai_messages_to_transcript(messages)
        transcript.append({"role": "interviewer", "text": reply_text})
        session_path = SESSIONS_DIR / f"{resolved_case_id}_{sid}.json"
        session_path.write_text(json.dumps({"case_id": resolved_case_id, "transcript": transcript}, indent=2))

        yield sse_chunk({
            "id": f"chatcmpl-{sid}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": MODEL,
            "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
        })
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


# ---- Evaluation ----

SCORE_LINE_RE = re.compile(r"TOTAL:?\s*\d+\s*/\s*\d+", re.IGNORECASE)


def extract_score_summary(scorecard: str) -> Optional[str]:
    """Pulls just the 'TOTAL: X/Y' line out of a full scorecard -- this is
    what free-plan users see instead of the full rubric breakdown."""
    match = SCORE_LINE_RE.search(scorecard)
    return match.group(0) if match else None


class EvaluateRequest(BaseModel):
    case_id: str
    session_id: Optional[str] = None
    transcript: Optional[list] = None  # [{role, text}, ...] -- alternative to session_id


@app.post("/evaluate")
def evaluate(req: EvaluateRequest, user: dict = Depends(require_user)):
    # Free-plan usage gate. Checked BEFORE the (paid, per-call) Claude
    # request below so a free user who's used up their 5 doesn't cost us
    # an evaluator call just to get turned away. Premium is unlimited.
    status = auth.get_billing_status(user["id"])
    if not status["is_premium"] and status["interviews_used"] >= auth.FREE_INTERVIEW_LIMIT:
        raise HTTPException(
            status_code=402,
            detail=f"You've used all {auth.FREE_INTERVIEW_LIMIT} free scored interviews on the "
                    "Free plan. Upgrade to Premium for unlimited interviews, detailed feedback, "
                    "and your full score history.",
        )

    case = load_case(str(case_path_for(req.case_id)))

    if req.transcript is not None:
        transcript = req.transcript
    elif req.session_id is not None:
        session_path = SESSIONS_DIR / f"{req.case_id}_{req.session_id}.json"
        if not session_path.exists():
            raise HTTPException(status_code=404, detail=f"No saved session at {session_path.name}")
        transcript = json.loads(session_path.read_text())["transcript"]
    else:
        raise HTTPException(status_code=400, detail="Provide either session_id or transcript.")

    system_prompt = build_evaluator_prompt(case.evaluator_only, case.guardrail_reminder, case.case_type)
    transcript_text = format_transcript(transcript)

    client = get_anthropic_client()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": f"TRANSCRIPT:\n{transcript_text}"}],
    )
    scorecard = "".join(block.text for block in resp.content if block.type == "text")

    # Debug instrumentation: a live test produced an empty scorecard string
    # with a 200 status, which shouldn't happen -- log exactly what Claude's
    # response looked like so we can see why (stop_reason, block types,
    # token usage) instead of guessing blind again.
    logger.info(
        "evaluate: stop_reason=%s, content_block_types=%s, scorecard_len=%d, "
        "input_tokens=%s, output_tokens=%s, transcript_len=%d",
        getattr(resp, "stop_reason", None),
        [getattr(b, "type", None) for b in resp.content],
        len(scorecard),
        getattr(resp.usage, "input_tokens", None) if hasattr(resp, "usage") else None,
        getattr(resp.usage, "output_tokens", None) if hasattr(resp, "usage") else None,
        len(transcript_text),
    )

    if not scorecard.strip():
        logger.error("evaluate: empty scorecard. Full response object: %r", resp)
        raise HTTPException(
            status_code=502,
            detail="The evaluator model returned an empty response -- check Railway logs "
                    "for the 'evaluate: empty scorecard' entry for details.",
        )

    score_summary = extract_score_summary(scorecard)

    # Always store the FULL scorecard in history, for every user -- if a
    # free user upgrades later, their earlier interviews already have
    # full feedback available rather than just the score they originally
    # saw. This call also increments the user's usage counter.
    auth.record_interview(
        user_id=user["id"],
        case_id=req.case_id,
        session_id=req.session_id or "adhoc",
        score_summary=score_summary,
        scorecard=scorecard,
    )

    if status["is_premium"]:
        return {"case_id": req.case_id, "scorecard": scorecard, "is_premium": True}

    # Free plan: score only, no detailed rubric breakdown.
    preview = score_summary or "Your score is being calculated."
    remaining = auth.FREE_INTERVIEW_LIMIT - status["interviews_used"] - 1
    upsell = (
        f"\n\n---\nDetailed feedback is a Premium feature. "
        f"You have {max(remaining, 0)} free scored interview(s) left. "
        f"Upgrade for unlimited interviews, detailed feedback, and full history."
    )
    return {"case_id": req.case_id, "scorecard": preview + upsell, "is_premium": False}


# ---- Billing (Stripe) ----

class CreateCheckoutRequest(BaseModel):
    success_url: str
    cancel_url: str


@app.post("/billing/create-checkout-session")
def create_checkout_session(req: CreateCheckoutRequest, user: dict = Depends(require_user)):
    try:
        url = billing.create_checkout_session(user["id"], user["email"], req.success_url, req.cancel_url)
    except billing.BillingError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"url": url}


@app.post("/billing/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    try:
        event = billing.verify_webhook(payload, sig_header)
    except billing.BillingError as exc:
        logger.error("billing webhook: %s", exc)
        raise HTTPException(status_code=400, detail=str(exc))

    if event["type"] == "checkout.session.completed":
        user_id = billing.user_id_from_checkout_event(event)
        if user_id:
            auth.set_premium(user_id)
            logger.info("billing: marked user_id=%s as premium", user_id)
        else:
            logger.error("billing: checkout.session.completed with no user id in event: %r", event)

    return {"received": True}


@app.get("/billing/status")
def billing_status(user: dict = Depends(require_user)):
    try:
        return auth.get_billing_status(user["id"])
    except auth.AuthError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


# ---- History (Premium) ----

@app.get("/history")
def history(user: dict = Depends(require_user)):
    status = auth.get_billing_status(user["id"])
    if not status["is_premium"]:
        raise HTTPException(
            status_code=403,
            detail="Interview history is a Premium feature. Upgrade to see your past scores and feedback.",
        )
    return {"interviews": auth.get_history(user["id"])}


# ---- Admin (you only, via ADMIN_SECRET -- see require_admin) ----

@app.get("/admin/users")
def admin_list_users(_: None = Depends(require_admin)):
    conn = auth._get_conn()
    rows = conn.execute(
        "SELECT id, email, is_premium, interviews_used, created_at FROM users ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return {"users": [dict(r) for r in rows]}


@app.get("/admin/interview-history")
def admin_interview_history(_: None = Depends(require_admin)):
    conn = auth._get_conn()
    rows = conn.execute(
        "SELECT ih.id, u.email, ih.case_id, ih.session_id, ih.score_summary, ih.created_at "
        "FROM interview_history ih JOIN users u ON u.id = ih.user_id "
        "ORDER BY ih.created_at DESC"
    ).fetchall()
    conn.close()
    return {"history": [dict(r) for r in rows]}


@app.get("/health")
def health():
    return {"status": "ok"}
