# Voice setup — deploying the backend and wiring up ElevenLabs

This covers Phase 2: turning the text-only prototype into a live voice
practice tool with a landing page and a "start practicing" button.

## 1. Get a standard Anthropic API key

Since other people will use this (not just personal practice), use a
pay-per-token API key rather than subscription auth:

1. Go to the Claude Console (platform.claude.com) → API Keys → create a key.
2. Keep it handy for Step 2 — you'll set it as an environment variable on
   whatever host runs `server.py`, never in the code itself.

## 2. Deploy `agent/server.py` to a public host

Any of Render, Fly.io, or Railway works the same way in broad strokes.
Render is the simplest to talk through:

1. Push this `agent/` folder to a git repo (GitHub/GitLab) — Render deploys
   from a repo, not a local folder.
2. In Render: New → Web Service → connect the repo, root directory `agent/`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn server:app --host 0.0.0.0 --port $PORT` (already
   saved as `Procfile` too, which Render and Railway both auto-detect).
5. Add an environment variable: `ANTHROPIC_API_KEY` = the key from Step 1.
6. Deploy. Render gives you a public URL like
   `https://case-interviewer.onrender.com`.

**Verify it's live** before touching ElevenLabs:
```
curl https://your-app.onrender.com/health
```
Should return `{"status":"ok"}`. Then test a full turn (note: the response
is now Server-Sent Events, per ElevenLabs' custom-LLM protocol, not a
single JSON object — add `-N` so curl doesn't buffer it):
```
curl -N -X POST "https://your-app.onrender.com/v1/chat/completions?case_id=case_04_pm_satisfaction_drop_figma" \
  -H "Content-Type: application/json" \
  -d '{"messages": []}'
```
Should print a few `data: {...}` lines ending in `data: [DONE]`, where the
first chunk's `choices[0].delta.content` is the interviewer's opening line.

## 3. Create ONE ElevenLabs Agent for the whole case library

Since the goal is a large, growing case library (not just 8 cases), this
does **not** use one Agent per case — that doesn't scale. Instead, a single
Agent serves every case, and which case runs is chosen per conversation.

ElevenLabs' Conversational AI product (now called "Agents" in their docs)
supports a **custom LLM** mode: it handles STT/TTS/turn-taking, and calls
your server for the actual reply on each turn. `server.py` resolves which
case to run from three possible sources, in this order:

1. a `?case_id=` query param (handy for manual testing, not used by the widget),
2. `elevenlabs_extra_body.case_id` in the request body (ElevenLabs' Python/JS
   SDK supports passing an arbitrary `extra_body` dict per conversation —
   **this is documented for their SDK, not confirmed for the plain HTML
   widget**, so treat it as a bonus path if you later move off the widget),
3. a system message containing the text `CASE_ID: <id>` — **this is the
   path built for the widget specifically**, using a mechanism ElevenLabs'
   docs do confirm for it (see setup below).

**Setup:**

1. In the ElevenLabs dashboard, create one new Agent (e.g. "Case Interview Practice").
   **Turn off "default personality"** if the Agent creation flow enables it —
   this was a real bug we hit: with it on, the Agent behaved with a generic
   built-in persona layered on top of (or instead of) whatever `server.py`
   sends as the system prompt, producing responses that directly
   contradicted `interviewer_prompt.md` (e.g. refusing to share case data
   at all, the opposite of Rule 1). Our backend already fully controls the
   interviewer's behavior — this toggle should be off so nothing else is
   influencing tone or instructions.
2. Under the Agent's **System prompt** field, enter just these two lines:
   ```
   CASE_ID: {{case_id}}
   SESSION_ID: {{session_id}}
   ```
   (these are markers for our backend to read back, not a real prompt — the
   actual interviewer instructions come from `agent/prompts/interviewer_prompt.md`
   inside `server.py`, which fully overrides whatever ElevenLabs sends as
   system content). `session_id` is generated client-side by `web/session.html`
   before the call starts, so the browser already knows the exact id to
   request later for scoring — no manual copy-pasting, and no dependence on
   capturing ElevenLabs' own internal conversation id (which this server
   never sees during the call anyway).
3. Under the Agent's LLM settings, switch to **custom LLM** and set the
   server URL to your deployed backend, no query param needed:
   `https://your-app.onrender.com/v1/chat/completions`
4. Set the Agent's **First message** field to:
   `{{first_message}}`
   Do **not** leave this blank. ElevenLabs' own dashboard hint says "if
   empty, the agent will wait for the user to start the conversation" —
   meaning it will NOT call your custom LLM automatically at call start,
   it just sits there silently. Since the candidate doesn't know the case
   yet, that would stall every call. Instead, ElevenLabs speaks this field
   itself via its own TTS, before your backend is ever called — the
   `{{first_message}}` template variable is filled in per-conversation by
   the widget's `dynamic-variables` attribute (see Step 4 below), which
   `web/config.js` sets to each case's exact opening line. Your custom LLM
   only gets called starting from the candidate's first reply onward.
5. Pick a voice under Voice settings.
6. Make sure the Agent is public with authentication disabled (Advanced
   tab) — required for the plain embed widget used below.
7. Copy the one Agent ID (shown in the dashboard).

## 4. Frontend: landing page + practice page — already built

The `web/` folder (sibling to `agent/`) has this done: `index.html` (landing
page), `practice.html` (case picker, reads the list from `config.js`), and
`session.html` (embeds the ElevenLabs widget, setting its `dynamic-variables`
attribute to `{"case_id": "...", "first_message": "..."}` for whichever case
was picked — this fills in both the `{{case_id}}` in the Agent's system
prompt AND the `{{first_message}}` in the Agent's First message field from
Step 3). Each case's opening line lives in `config.js` as that case's
`firstMessage` field, already filled in with the exact case-prompt text plus
a short welcome sentence — no per-case setup left to do there. You only need
to edit the top of `web/config.js`:

1. Set `backendUrl` to your deployed server's URL from Step 2.
2. Set `agentId` (one shared value, not per-case) to the Agent ID from Step 3.7.

If you add a new case to the library later, add a matching entry (with its
own `firstMessage`) to `config.js`'s `cases` array — nothing else changes.

Until both are filled in, `session.html` shows a "setup incomplete" notice
instead of the widget, so it's obvious what's left to configure.

**Test locally** before deploying the static files anywhere:
```
cd web && python3 -m http.server 8080
```
Then open `http://localhost:8080` in a browser. Any static host works for
real deployment (Netlify, Vercel, GitHub Pages, or even served by the same
box running `server.py`).

**Fixed:** `session.html` generates a random session id client-side before
the call starts and passes it to the Agent via the `SESSION_ID: {{session_id}}`
marker (Step 3.2), so the "Session ID" field is now pre-filled automatically
— no manual copying from `agent/sessions/` needed. (You can still edit it by
hand if you ever need to.) Requires the Agent's system prompt to actually
have both marker lines from Step 3.2 — if the field is empty after a call,
double check that.

## 5. After the call: scoring

`server.py` already writes a transcript to `sessions/<case_id>_<session>.json`
on every turn, so once a call ends you have a complete record. To surface a
score:

- Simplest: a "get my results" button on your practice page that calls your
  own backend's `/evaluate` endpoint with `{"case_id": ..., "session_id": ...}`
  (you'll need the widget to expose or you to capture ElevenLabs'
  conversation ID to use as `session_id` — check their widget/SDK events for
  a call-start or call-end callback that provides this).
- More automated: ElevenLabs supports post-call webhooks that fire when a
  conversation ends and can include the full transcript — wiring that to
  call your `/evaluate` endpoint automatically is a reasonable next step
  once the basic flow is working, but isn't built yet.

## What's built vs. what you still need to configure

**Built and tested (this repo):** `server.py`'s two endpoints, verified
end-to-end with a mocked Claude response — case loading, system prompt
assembly, transcript saving, and evaluation all work.

**Not yet done, needs your hands-on setup:** actually deploying to a host,
creating the ElevenLabs account/agents, confirming the exact first-message
behavior in their current dashboard, and building the actual landing/practice
HTML pages. None of that can be verified without a live ElevenLabs account
and a deployed URL, so budget some trial-and-error on the ElevenLabs
dashboard specifics — their UI details are the one part of this plan I
couldn't test directly.
