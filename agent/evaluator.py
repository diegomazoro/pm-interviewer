"""
Phase 3 prototype: post-interview scoring pass.

Takes a saved transcript (from interviewer.py) plus the case's
evaluator-only section (model answer / scoring anchors) and produces a
structured scorecard.

The rubric and grading instructions live in prompts/evaluator_rubric.md and
prompts/evaluator_prompt.md, not in this file -- edit those markdown files
to change scoring criteria or grading behavior without touching code. This
file is just the harness: it assembles the prompt, calls the model, and
saves the scorecard.

Uses the Claude Agent SDK's single-shot `query()` function -- same auth
rules as interviewer.py (API key OR your Claude subscription via
`claude setup-token`, no code change needed either way).

Usage:
    python evaluator.py sessions/case_01_..._<timestamp>.json cases/case_01_profitability_peak_performance.md
"""
import asyncio
import json
import sys
from pathlib import Path

from case_loader import load_case

PROMPTS_DIR = Path(__file__).parent / "prompts"


def build_system_prompt(evaluator_only: str, guardrail_reminder: str = "", case_type: str = "diagnostic") -> str:
    # product_sense cases are graded on a different rubric (business
    # judgment, user-centricity, product taste, prioritization, composure
    # under follow-ups) than diagnostic cases (structuring, quant reasoning,
    # insight generation, etc.) -- see prompts/product_sense_rubric.md.
    rubric_name = "product_sense_rubric.md" if case_type == "product_sense" else "evaluator_rubric.md"
    rubric = (PROMPTS_DIR / rubric_name).read_text(encoding="utf-8")
    template = (PROMPTS_DIR / "evaluator_prompt.md").read_text(encoding="utf-8")
    if not guardrail_reminder:
        guardrail_reminder = "(No case-specific guardrail was found for this case -- rely on the general integrity check only.)"
    return (
        template
        .replace("<<RUBRIC>>", rubric)
        .replace("<<EVALUATOR_ONLY>>", evaluator_only)
        .replace("<<GUARDRAIL_REMINDER>>", guardrail_reminder)
    )


def format_transcript(transcript) -> str:
    lines = []
    for turn in transcript:
        speaker = "INTERVIEWER" if turn["role"] == "interviewer" else "CANDIDATE"
        lines.append(f"{speaker}: {turn['text']}")
    return "\n".join(lines)


async def evaluate(session_path: str, case_path: str):
    try:
        from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
    except ImportError:
        print("The 'claude_agent_sdk' package isn't installed. Run:")
        print("  pip install claude-agent-sdk --break-system-packages")
        sys.exit(1)

    case = load_case(case_path)
    session = json.loads(Path(session_path).read_text())
    transcript_text = format_transcript(session["transcript"])

    system_prompt = build_system_prompt(case.evaluator_only, case.guardrail_reminder, case.case_type)

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=[],  # no file/bash/web access -- pure text grading
    )

    scorecard = ""
    async for message in query(prompt=f"TRANSCRIPT:\n{transcript_text}", options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    scorecard += block.text

    print(scorecard)
    out_path = Path(session_path).with_suffix(".scorecard.txt")
    out_path.write_text(scorecard)
    print(f"\nSaved scorecard to {out_path}")
    return scorecard


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python evaluator.py <session_transcript.json> <case_file.md>")
        sys.exit(1)
    asyncio.run(evaluate(sys.argv[1], sys.argv[2]))
