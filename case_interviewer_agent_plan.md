# Voice Case-Interviewer Agent — Build Plan & Evaluation Criteria

## 1. Concept

A voice-only agent that runs a consulting-style case interview live with a candidate: presents the case prompt, answers clarifying questions with only the facts it's given (no hints or steering toward insights), and afterward scores the conversation against a fixed rubric.

## 2. Recommended architecture

**Voice stack: STT + LLM + TTS pipeline (not a speech-to-speech realtime API), for this use case specifically.**

Reasoning: realtime speech-to-speech APIs (OpenAI Realtime, ElevenLabs Conversational AI) are lower latency and feel more natural, but they reason and speak in one pass, which makes it harder to enforce "never leak a hint" and to keep a clean, auditable transcript for scoring. A pipeline gives you:
- A dedicated **text LLM turn** where you can enforce strict system-prompt rules (case facts only, no coaching) before anything is spoken.
- A clean **transcript** to feed into the scoring step afterward.
- Easier debugging/iteration on the "brain" independent of voice quality.

Once the interview logic is solid, you can swap in a realtime voice API later for lower latency without changing the case logic or rubric.

Components:
1. **Voice orchestration (STT + TTS + turn-taking)**: **ElevenLabs Conversational AI ("Agents")**, used in its **custom-LLM mode** rather than Hyponema. Considered Hyponema (an all-in-one voice-agent builder) and ruled it out: it's private-beta/waitlist-only, and its whole design is "describe the job, our model reasons for you" — using it would mean re-implementing the interviewer's guardrails inside a third-party agent-definition system we can't fully control or audit. ElevenLabs' custom-LLM mode instead lets ElevenLabs own the hard parts (streaming STT, streaming TTS, turn-taking, interruption/barge-in handling, browser WebSocket plumbing) while calling out to **our own server** for the actual reply on every turn — so the interviewer logic and guardrails built in Phase 1 don't change at all, voice is just a layer wrapped around them.
2. **Interviewer LLM**: Claude, called from a small backend service (see Phase 2 below) using a **standard Anthropic API key** (pay-per-token), not subscription auth — because this is now meant for other people to use, not just personal practice, and Anthropic's usage policy doesn't allow reselling/sharing subscription-based rate limits to other users of a third-party product. Holds the case file in its system prompt exactly as before, with the same guardrails from `agent/prompts/interviewer_prompt.md`. Only reveals data when asked the right question; refuses insight/strategy questions with a neutral deflection.
3. **Backend server**: a thin FastAPI wrapper (`agent/server.py`) exposing an OpenAI-chat-completions-compatible endpoint. ElevenLabs sends the running conversation to this endpoint each turn; it loads the case via `case_loader.py`, builds the system prompt from `interviewer_prompt.md`, calls Claude, and returns the reply text. The same endpoint's request history doubles as the transcript, saved in the same shape `interviewer.py` already produces, so `evaluator.py` needs no changes.
4. **Frontend**: a landing page explaining the service, plus a second page that embeds ElevenLabs' web widget/JS SDK. Clicking "start practicing" opens the voice session immediately; the agent's first turn (short welcome + reading the case prompt verbatim) fires the same way it does in the Phase 1 CLI version.
5. **Evaluator (separate pass, after the interview ends)**: same backend, same Claude API key, single-shot call — takes the saved transcript + case's answer key, scores against the rubric in Section 4.

**Deployment**: the backend needs a public URL for ElevenLabs to call, so it runs on a simple managed host (Render, Fly.io, or Railway) rather than your personal machine or a home server — there's still no local model doing inference, the LLM call always goes to Anthropic's cloud, so the hosting choice is purely about "does ElevenLabs' cloud have a URL to reach," not about compute.

## 3. Build plan (phased)

**Phase 0 — Case content — done, extended**
- 8 case files written: 3 consulting-style (`case_01`–`case_03`) and 5 PM-style (`case_04`–`case_08`, covering satisfaction drop, retention drop, support bottleneck, fraud increase, and roadmap prioritization). Each has a case prompt, a gated clarifying-question answer key, exhibits, and a model answer with scoring anchors, kept in `agent/cases/`. Brand pivoted to **Loudcase**, positioned PM-first for practicing case interviews at top tech companies (see `web/index.html`); the 3 consulting cases stay on disk but are excluded from the public case picker in `web/config.js`.
- Added a second case type, **product sense** (`case_09`–`case_14`: Anthropic, OpenAI, Google, Meta, Netflix, Amazon), based on real research into how this interview format actually works and is graded (Lenny's Newsletter / Exponent guides — see task history). Product sense is an open-ended design/improvement format ("design a feature for X"), fundamentally different from the diagnostic/root-cause cases, so it required real code changes, not just new content:
  - `case_loader.py` now parses an optional `**Case type:**` line (defaults to `diagnostic` for backward compatibility with `case_01`–`08`).
  - `interviewer.py` / `evaluator.py` / `server.py` branch on `case.case_type` to select between `interviewer_prompt.md` / `interviewer_prompt_product_sense.md` and `evaluator_rubric.md` / `product_sense_rubric.md`.
  - New rubric (`product_sense_rubric.md`): 5 dimensions (problem framing & segmentation, product taste, prioritization & tradeoffs, business judgment & metrics, communication & composure under follow-ups), total /25 — deliberately different from the diagnostic rubric's /40, since real PM interview loops score these rounds differently too.
  - New interviewer behavior (`interviewer_prompt_product_sense.md`): allows two standard, content-neutral follow-ups ("how would you measure success," "what would you cut") that a real interviewer always asks regardless of the answer's content, plus a scripted "solution-gated" follow-up twist (a complicating data point) delivered once, only after the candidate proposes a concrete solution — modeled on the real Meta-style metric-conflict follow-up pattern found in research.
  - `evaluator_prompt.md`'s scorecard format instruction was generalized from a hardcoded `/40` to read the max from whichever rubric is injected, since two rubrics with different totals now exist.

**Phase 1 — Core pipeline (text-only prototype) — done**
- `agent/interviewer.py` and `agent/evaluator.py` are built on the Claude Agent SDK, with the actual prompt wording split out into editable markdown (`agent/prompts/interviewer_prompt.md`, `evaluator_rubric.md`, `evaluator_prompt.md`) so content can be tuned without touching code. `agent/case_loader.py` guarantees the model answer never leaks into the interviewer's context (verified programmatically across all 8 cases). Two fixture transcripts (strong/weak candidate) let the evaluator be sanity-checked before running a live interview.
- Not yet done: an actual live dry-run conversation (needs your Claude subscription authenticated on whatever machine you run it on — see `agent/README.md`), and stress-testing the no-coaching boundary against adversarial questions.

**Phase 2 — Add voice — in progress**
- Vendor decision made: ElevenLabs Conversational AI (custom-LLM mode), not Hyponema — see Section 2 for reasoning.
- Built and tested: `agent/server.py` (FastAPI wrapper around `case_loader.py` / `interviewer_prompt.md` / Claude, using a standard Anthropic API key; `/v1/chat/completions` and `/evaluate` both verified end-to-end with a mocked Claude client, including a fix so multi-turn transcripts accumulate into one session file even without a platform-supplied session id).
- Built: `web/` static frontend — landing page, case picker, and a session page embedding the ElevenLabs widget, driven by a single `config.js` you fill in once the backend and ElevenLabs agents exist.
- Backend deployed to Railway and verified live (`https://pm-interviewer-production.up.railway.app`) — confirmed end-to-end against the real Claude API (not a mock), correctly returns a case's opening line. `web/config.js`'s `backendUrl` is set.
- Redesigned for scale: rather than one ElevenLabs Agent per case (doesn't scale to a large library), `server.py` now resolves `case_id` from a query param, `elevenlabs_extra_body`, or a `CASE_ID: {{case_id}}` system-message marker filled in by the widget's `dynamic-variables` attribute — confirmed against ElevenLabs' current docs. Also switched responses to SSE streaming, matching their documented custom-LLM protocol (the prior plain-JSON response likely wouldn't have worked against a real Agent). One shared Agent now serves the whole case library.
- Fixed a real gap found mid-setup: the ElevenLabs dashboard's own hint text says an empty "First message" field makes the agent wait silently for the user, rather than auto-calling the custom LLM at call start — which would stall every call, since the candidate doesn't know the case yet. Fix: each case's exact opening line now lives in `config.js` as a `firstMessage` field, passed to the Agent's `{{first_message}}` template via the widget's `dynamic-variables` attribute, so ElevenLabs speaks it directly via its own TTS; the custom LLM is only called from the candidate's first reply onward. This also required a fix in `server.py`: the stable-session-id hash now keys off the candidate's first reply instead of the first message in history, since the first message is now a fixed per-case string (identical across every candidate doing that case) rather than model-generated — hashing the old way would have collided different candidates' sessions on the same case into one file.
- Still to do: actually create that one ElevenLabs Agent (system prompt = the `CASE_ID: {{case_id}}` marker, custom LLM pointed at the Railway URL, First message = `{{first_message}}`) and fill its ID into `config.js`, verify this behavior against a live account, and automate scorecard retrieval (currently a manual session-id entry — see `agent/VOICE_SETUP.md`).

**Phase 3 — Scoring pass — done (text-only)**
- Evaluator prompt and rubric built as described above. Once Phase 2 adds voice, no changes needed here — it scores a transcript regardless of how the transcript was produced.

**Phase 4 — Polish — not started**
- Session recording/transcript storage, a simple UI to start a case and view past scorecards, tuning latency and voice naturalness.

**Phase 5 — Verification — partially done**
- Fixture-based evaluator sanity check exists (Phase 1). Still to do: run live interviews per case (including a "textbook good" and a "clueless" run) and confirm the scorecard differentiates them correctly; confirm the interviewer never leaks hints under adversarial questioning, across both the consulting and PM case styles.

## 4. Evaluation criteria (rubric)

Score each dimension 1–5 (1 = poor, 5 = excellent). Total /40 (8 dimensions × 5 points each), plus qualitative feedback per dimension.

1. **Problem structuring** — Did the candidate lay out a clear, MECE framework before diving into analysis? Was the structure tailored to the specific case rather than a generic template?

2. **Clarifying questions** — Did they ask relevant, well-targeted questions early (objective, scope, constraints) rather than guessing or skipping this step?

3. **Quantitative reasoning** — Are calculations correct? Are estimates reasonable, sanity-checked, and is math done efficiently out loud?

4. **Business/commercial sense** — Do the ideas and conclusions reflect real-world commercial judgment (market dynamics, feasibility, risk) rather than purely academic logic?

5. **Insight generation** — Did they draw non-obvious, correct insights from the data/exhibits provided, rather than just restating numbers?

6. **Synthesis & recommendation** — Is there a clear, top-down final recommendation, with a "so what," supported by the strongest 2–3 reasons, delivered proactively (not just when asked)?

7. **Communication** — Clear, structured, confident verbal communication; signposting ("First, I'll look at... second..."); appropriate pacing; listens to and correctly uses information given.

8. **Composure & adaptability** — How they handle ambiguity, pushback, or being told they're wrong; do they adjust their approach without falling apart or getting defensive?

Optional pass/fail flags (not scored numerically, but noted): candidate never received unearned hints from the interviewer (integrity of the test itself); candidate stayed within time budget if one was set.

## 5. Guardrails for the interviewer agent (system prompt rules)

- Only reveal facts/exhibits when specifically asked for them (or at the point the case script says to reveal proactively, e.g., handing over an exhibit after framework is presented).
- Never suggest which branch of a framework to explore, never say "good idea" or "not quite" about approach — stay neutral ("Sure, here's that data" / "What would you like to know next?").
- If asked directly for help ("what do you think I should focus on?"), redirect neutrally: "This is your call to make."
- Keep a hidden running log of exactly what was revealed and when, for the evaluator.
