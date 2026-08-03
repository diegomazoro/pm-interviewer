"""
Phase 1 prototype: text-only case interviewer.

Runs a turn-by-turn chat loop with the candidate (stdin/stdout for now --
voice gets layered on top of this same system prompt + loop in Phase 2).

The interviewer's instructions live in prompts/interviewer_prompt.md, not in
this file -- edit that markdown file to change wording/rules without
touching code. This file is just the harness: it loads the prompt, loads a
case, runs the loop, saves the transcript, and hard-disables tool access.

Uses the Claude Agent SDK (claude_agent_sdk), which supports two auth modes
with NO code change required -- whichever is configured in your shell wins:

  1. API key: export ANTHROPIC_API_KEY=sk-ant-...
  2. Your Claude Pro/Max subscription: run `claude setup-token` once (see
     README.md), then just don't set ANTHROPIC_API_KEY at all.

Tools are explicitly disabled (allowed_tools=[]) -- this is a pure
conversational role-player, it should never read/write files or run
commands mid-interview.

Usage:
    python interviewer.py cases/case_01_profitability_peak_performance.md
"""
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from case_loader import load_case

PROMPTS_DIR = Path(__file__).parent / "prompts"


def build_system_prompt(case) -> str:
    # product_sense cases (open-ended design/improvement prompts) use a
    # different interviewer ruleset than diagnostic/root-cause cases -- see
    # prompts/interviewer_prompt_product_sense.md for why (the standard
    # "how would you measure success" / "what would you cut" follow-ups and
    # the scripted mid-interview "twist" are specific to that format).
    template_name = (
        "interviewer_prompt_product_sense.md"
        if getattr(case, "case_type", "diagnostic") == "product_sense"
        else "interviewer_prompt.md"
    )
    template = (PROMPTS_DIR / template_name).read_text(encoding="utf-8")
    return template.replace("<<CASE_CONTEXT>>", case.interviewer_context)


async def run_interview(case_path: str, session_out_dir: str = "sessions"):
    try:
        from claude_agent_sdk import (
            ClaudeSDKClient,
            ClaudeAgentOptions,
            AssistantMessage,
            TextBlock,
        )
    except ImportError:
        print("The 'claude_agent_sdk' package isn't installed. Run:")
        print("  pip install claude-agent-sdk --break-system-packages")
        sys.exit(1)

    case = load_case(case_path)
    system_prompt = build_system_prompt(case)
    transcript = []

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=[],  # no file/bash/web access -- pure conversation
    )

    print(f"=== Starting interview: {case.title} ===")
    print("(Type your responses. Type 'quit' to end and save the transcript.)\n")

    async with ClaudeSDKClient(options=options) as client:
        await client.query("[SESSION START -- please begin the interview.]")
        while True:
            interviewer_text = ""
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            interviewer_text += block.text
            print(f"INTERVIEWER: {interviewer_text}\n")
            transcript.append({"role": "interviewer", "text": interviewer_text})

            candidate_text = input("YOU: ").strip()
            if candidate_text.lower() in {"quit", "exit"}:
                break
            transcript.append({"role": "candidate", "text": candidate_text})
            await client.query(candidate_text)

    Path(session_out_dir).mkdir(exist_ok=True)
    out_path = Path(session_out_dir) / f"{case.case_id}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    out_path.write_text(json.dumps({"case_id": case.case_id, "transcript": transcript}, indent=2))
    print(f"\nSaved transcript to {out_path}")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python interviewer.py <path_to_case_file.md>")
        sys.exit(1)
    asyncio.run(run_interview(sys.argv[1]))
