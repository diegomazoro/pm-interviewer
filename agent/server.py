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
- POST /v1/chat/completions  -- OpenAI-compatible endpoint. Point an
  ElevenLabs Agent's "custom LLM" at this URL (one Agent per case; pass
  which case via the `case_id` query param, e.g.
  https://your-host/v1/chat/completions?case_id=case_04_pm_satisfaction_drop_figma).
  ElevenLabs sends the running conversation on every turn; this endpoint
  rebuilds the case-specific system prompt, calls Claude, returns the
  reply, and writes the running transcript to sessions/ on every call (the
  incoming message list IS the full transcript so far, so this is
  stateless -- no server-side session memory required).
- POST /evaluate  -- given a case_id + session_id (or a transcript
  directly), scores a saved transcript the same way evaluator.py does and
  returns the scorecard as JSON.
- GET  /health  -- for the hosting platform's health checks.

Run locally for testing:
    export ANTHROPIC_API_KEY=sk-ant-...
    uvicorn server:app --reload --port 8000

Deploy: see README.md for Render/Fly.io/Railway steps.
"""
import hashlib
import json
import os
import time
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: Optional[str] = None
    messages: List[ChatMessage]
    stream: Optional[bool] = False


def openai_messages_to_transcript(messages: List[ChatMessage]) -> list:
    """Map OpenAI-style roles to our {role: interviewer/candidate, text} shape,
    dropping any system messages (our own system prompt is authoritative,
    not whatever the voice platform's dashboard might also send)."""
    transcript = []
    for m in messages:
        if m.role == "system":
            continue
        role = "interviewer" if m.role == "assistant" else "candidate"
        transcript.append({"role": role, "text": m.content})
    return transcript


def transcript_to_anthropic_messages(messages: List[ChatMessage]) -> list:
    out = []
    for m in messages:
        if m.role == "system":
            continue
        anth_role = "assistant" if m.role == "assistant" else "user"
        out.append({"role": anth_role, "content": m.content})
    if not out:
        # First turn of a brand new call -- same trigger the CLI uses to
        # get the model to open with the case prompt.
        out.append({"role": "user", "content": "[SESSION START -- please begin the interview.]"})
    return out


@app.post("/v1/chat/completions")
def chat_completions(
    req: ChatCompletionRequest,
    case_id: str = Query(..., description="Which case file to run, e.g. case_04_pm_satisfaction_drop_figma"),
    session_id: Optional[str] = Query(None, description="Optional session id, for naming the saved transcript file"),
):
    case = load_case(str(case_path_for(case_id)))
    system_prompt = build_interviewer_prompt(case)
    anthropic_messages = transcript_to_anthropic_messages(req.messages)

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
    # We can't rely on the voice platform passing a stable session_id on
    # every turn (unverified without a live account -- see VOICE_SETUP.md).
    # So: if one IS given, use it. Otherwise, derive a stable key from
    # case_id + the first message in the history, since the platform is
    # expected to resend the whole growing conversation each turn (that's
    # the point of the OpenAI chat-completions format) -- the first
    # message stays constant across a single call, so this naturally
    # groups every turn of one conversation into the same file without
    # needing any platform-specific session field. Only the very first
    # turn (empty history, nothing to hash yet) falls back to a fresh id.
    if session_id:
        sid = session_id
    elif req.messages:
        first = req.messages[0].content
        sid = hashlib.sha1(f"{case_id}|{first}".encode()).hexdigest()[:12]
    else:
        sid = uuid.uuid4().hex[:12]
    transcript = openai_messages_to_transcript(req.messages)
    transcript.append({"role": "interviewer", "text": reply_text})
    session_path = SESSIONS_DIR / f"{case_id}_{sid}.json"
    session_path.write_text(json.dumps({"case_id": case_id, "transcript": transcript}, indent=2))

    return {
        "id": f"chatcmpl-{sid}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": MODEL,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": reply_text},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": resp.usage.input_tokens,
            "completion_tokens": resp.usage.output_tokens,
            "total_tokens": resp.usage.input_tokens + resp.usage.output_tokens,
        },
    }


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

    system_prompt = build_evaluator_prompt(case.evaluator_only, case.guardrail_reminder)
    transcript_text = format_transcript(transcript)

    client = get_anthropic_client()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1200,
        system=system_prompt,
        messages=[{"role": "user", "content": f"TRANSCRIPT:\n{transcript_text}"}],
    )
    scorecard = "".join(block.text for block in resp.content if block.type == "text")
    return {"case_id": req.case_id, "scorecard": scorecard}


@app.get("/health")
def health():
    return {"status": "ok"}
