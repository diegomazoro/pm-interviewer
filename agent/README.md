# Case Interviewer Agent — Phase 1 Prototype

Text-only prototype from Phase 1 of the build plan: prove out the
interviewer's system prompt (case delivery, fact-gating, no-coaching
boundary) before adding voice.

Both scripts now run on the **Claude Agent SDK**, which supports your Claude
subscription directly (no pay-per-token API key needed) — this section walks
through getting that working on your home server step by step.

## Files

- `case_loader.py` — parses a case markdown file into `interviewer_context`
  (prompt + clarifying-question key + exhibits) and `evaluator_only` (the
  model answer). Verified: the model answer never leaks into the
  interviewer's context.
- `prompts/interviewer_prompt.md` — the interviewer's actual instructions
  (case-delivery rules, no-coaching boundary). Edit this file to change how
  the interviewer behaves — no code changes needed. Contains a
  `<<CASE_CONTEXT>>` placeholder that gets filled in with the loaded case.
- `prompts/evaluator_rubric.md` — the 8-dimension scoring rubric, as its own
  editable document.
- `prompts/evaluator_prompt.md` — the grading instructions the evaluator
  model follows. Contains `<<RUBRIC>>` and `<<EVALUATOR_ONLY>>` placeholders.
- `interviewer.py` — the harness: loads `interviewer_prompt.md` + a case,
  runs a live text chat loop against Claude via `ClaudeSDKClient`, saves a
  JSON transcript per session. Tools are explicitly turned off
  (`allowed_tools=[]`) so it can't read files or run commands — it's a pure
  role-player, and this lockdown lives in code, not in the editable prompt,
  so it can't be edited away by accident.
- `evaluator.py` — the harness: loads the rubric + grading prompt, scores a
  saved transcript, saves the scorecard.
- `cases/` — all 8 case files.
- `fixtures/` — two example transcripts for case 1 (strong/weak candidate)
  to sanity-check the evaluator before running a real interview.
- `sessions/` — where live transcripts get saved (created on first run).

**Why the split:** the wording of what the interviewer says and how the
evaluator grades is content you'll want to tune often — that lives in plain
markdown in `prompts/`. The turn-taking loop, transcript I/O, and the hard
tool lockdown are control flow and a security boundary — those stay in
Python so they can't be loosened just by editing a prompt file.

## Step 1 — Install prerequisites

You need Python 3.10+ on your home server. Check with:

```bash
python3 --version
```

Create a virtual environment (keeps this project's packages separate from
system Python — recommended but not required):

```bash
cd agent
python3 -m venv .venv
source .venv/bin/activate      # you'll see (.venv) in your prompt now
```

Install the SDK:

```bash
pip install claude-agent-sdk
```

(If you skip the venv, add `--break-system-packages` to the pip command.)

This bundles a native Claude Code binary — you do **not** need to separately
install Node.js or the `claude` npm package for the scripts to run. You *do*
need the standalone `claude` CLI for one thing: generating the subscription
login token in Step 2. Get it with:

```bash
npm install -g @anthropic-ai/claude-code
```

(Requires Node.js 18+. If you don't have Node on your home server, install
it first — e.g. via your distro's package manager or nvm.)

## Step 2 — Authenticate with your Claude subscription

This is the one-time login step. Run:

```bash
claude setup-token
```

This opens a browser (or prints a URL if there's no display on your home
server — copy it to a browser on your laptop/phone, log into your Claude
account, and paste the resulting code back into the terminal). It writes an
OAuth credential to `~/.claude/` on the server. That's it — you don't set
`ANTHROPIC_API_KEY` at all for this path; the SDK picks up the stored
credential automatically because it shares Claude Code's auth store.

**Verify it worked:**

```bash
claude -p "say hello"
```

If that prints a response, authentication is working and `interviewer.py` /
`evaluator.py` will use the same credential with no further setup.

**Note on usage:** this draws from your Pro/Max plan's normal usage pool
(same limits as using Claude Code or claude.ai), not a separate API bill.
Rolling 5-hour and weekly caps still apply, so heavy iteration while
developing could bump into those — if you hit a limit mid-testing, just
wait for the window to reset or switch to Step 2b below temporarily.

## Step 2b (alternative) — Use a pay-per-token API key instead

If you'd rather not use the subscription (e.g. you want higher throughput
while iterating, or a second environment without re-logging in), get a key
from the Claude Console (platform.claude.com → API Keys) and:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

Whichever of Step 2 or Step 2b is active in your shell is what the SDK uses
— no code change needed either way. To persist the API key across terminal
sessions, add the `export` line to `~/.bashrc` or `~/.zshrc`.

## Step 3 — Sanity-check the evaluator against the fixtures

Before running a live interview, confirm the scoring pipeline actually
discriminates good reasoning from weak reasoning:

```bash
python interviewer.py --help 2>/dev/null   # just confirms the script loads
python evaluator.py fixtures/case_01_strong_transcript.json cases/case_01_profitability_peak_performance.md
python evaluator.py fixtures/case_01_weak_transcript.json cases/case_01_profitability_peak_performance.md
```

Expect: the strong transcript scores noticeably higher, especially on
"insight generation" and "synthesis & recommendation," and both come back
`INTEGRITY: PASS` (neither fixture contains a real hint — this step only
tests the evaluator, not the interviewer's guardrails).

## Step 4 — Run a live text interview

```bash
python interviewer.py cases/case_04_pm_satisfaction_drop_figma.md
```

Type your responses at the `YOU:` prompt. Deliberately try to get a hint
("what do you think I should look at first?") to stress-test rule 3 in the
system prompt. Type `quit` to end and save the transcript to `sessions/`.

## Step 5 — Score that live session

```bash
python evaluator.py sessions/<the_file_it_saved>.json cases/case_04_pm_satisfaction_drop_figma.md
```

## Troubleshooting

- **"claude_agent_sdk not installed"** — you're not in the venv, or the pip
  install didn't complete. Re-run `source .venv/bin/activate` then
  `pip install claude-agent-sdk`.
- **Auth errors ("not authenticated" / 401)** — re-run `claude setup-token`,
  or confirm `echo $ANTHROPIC_API_KEY` prints something if using Step 2b.
- **Nothing happens / hangs on first message** — check your home server has
  outbound internet access to Anthropic's API; this is a cloud call either way,
  local-only inference isn't happening here.
- **Rate limit / usage cap errors on the subscription path** — you've hit
  the Pro/Max rolling usage window; wait for it to reset, or set
  `ANTHROPIC_API_KEY` temporarily (Step 2b) to keep testing.

## What to check during Phase 1 testing

- Does the interviewer ever answer a "what should I focus on" style question
  with anything other than a neutral redirect?
- Does it ever hand over an exhibit before the candidate proposes a framework
  (check the "framework-gated" rows in each case file)?
- Does the evaluator's INTEGRITY flag ever come back FAIL on a transcript
  where you know no hint was actually given? If so, tighten the evaluator
  prompt, not just the interviewer.
- Run at least one case from each style (consulting case_01–03, PM diagnostic
  case_04–07, PM prioritization case_08) — case_08 specifically tests whether
  the interviewer generates entry-mode/prioritization options *for* the
  candidate, which it must never do.

## Next steps (Phase 2+ per the plan)

Once the system prompt holds up across a handful of live text runs, wrap this
same `system_prompt` + turn loop with STT input and TTS output for voice, per
Section 2–3 of `../case_interviewer_agent_plan.md`.
