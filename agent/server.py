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
import json
import logging
import os
import re
import time
import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

logger = logging.getLogger("uvicorn.error")

from case_loader import load_case
from interviewer import build_system_prompt as build_interviewer_prompt
from evaluator import build_system_prompt as build_evaluator_prompt, format_transcript

BASE_DIR = Path(__file__).parent
CASES_DIR = BASE_DIR / "cases"
SESSIONS_DIR = BASE_DIR / "sessions"
SESSIONS_DIR.mkdir(exist_ok=True)

MODEL = "claude-sonnet-5"

app = FastAPI(title="Case Interviewer Voice Backend")

# Permissive for development. Restrict allow_origins to your actual
# frontend domain before going live with real users.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    resp = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=system_prompt,
        messages=anthropic_messages,
    )
    reply_text = "".join(block.text for block in resp.content if block.type == "text")

    # Save the running transcript (incoming history + this new reply) so
    # /evaluate can score it later, same shape interviewer.py produces.
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
    transcript = openai_messages_to_transcript(messages)
    transcript.append({"role": "interviewer", "text": reply_text})
    session_path = SESSIONS_DIR / f"{resolved_case_id}_{sid}.json"
    session_path.write_text(json.dumps({"case_id": resolved_case_id, "transcript": transcript}, indent=2))

    # ElevenLabs' custom-LLM protocol expects SSE-streamed chunks (see
    # VOICE_SETUP.md) -- we wrap the one full reply (our Claude call above
    # isn't itself streamed yet) in that chunk framing so it's a valid
    # response either way, whether or not the caller actually reads it
    # incrementally.
    def event_stream():
        yield sse_chunk({
            "id": f"chatcmpl-{sid}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": MODEL,
            "choices": [{"index": 0, "delta": {"role": "assistant", "content": reply_text}, "finish_reason": None}],
        })
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

class EvaluateRequest(BaseModel):
    case_id: str
    session_id: Optional[str] = None
    transcript: Optional[list] = None  # [{role, text}, ...] -- alternative to session_id


@app.post("/evaluate")
def evaluate(req: EvaluateRequest):
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

    return {"case_id": req.case_id, "scorecard": scorecard}


@app.get("/health")
def health():
    return {"status": "ok"}
