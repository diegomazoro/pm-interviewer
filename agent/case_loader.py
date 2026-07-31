"""
Parses a case markdown file (as produced for this project) into the pieces
the interviewer and evaluator need, keeping them cleanly separated:

- interviewer_context: everything the INTERVIEWER is allowed to see
  (prompt, clarifying-question key, exhibits). This is what goes into the
  interviewer's system prompt.
- evaluator_only: the "Model answer / what good looks like" section.
  This must NEVER be included in the interviewer's system prompt -- it's
  reserved for the post-interview scoring pass only.
- guardrail_reminder: the case-specific "**Guardrail reminder:** ..." line
  from Section B. This is meta-instruction about interviewer behavior, not
  a spoiler of case facts, so it's safe to give to BOTH the interviewer
  (it's already part of interviewer_context) AND the evaluator, so the
  evaluator can check the transcript against this case's specific
  no-coaching rule instead of relying only on a generic integrity check.

Case files are expected to have top-level headers:
  # Case File N -- <Title>
  ## A. Case prompt ...
  ## B. Clarifying-question answer key
  ## C. Exhibits / data
  ## D. Model answer / "what good looks like"

Everything before "## D." is interviewer_context. Everything from "## D."
onward is evaluator_only. The guardrail reminder is pulled out separately
via a regex match on the "**Guardrail reminder:**" line found in Section B.
"""
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Case:
    case_id: str
    title: str
    interviewer_context: str
    evaluator_only: str
    guardrail_reminder: str
    raw_text: str


def load_case(path: str) -> Case:
    text = Path(path).read_text(encoding="utf-8")

    title_match = re.search(r"^#\s*(Case File.*)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else Path(path).stem

    split_match = re.search(r"^##\s*D\.\s*Model answer", text, re.MULTILINE)
    if not split_match:
        raise ValueError(
            f"Could not find '## D. Model answer' section in {path}; "
            "cannot safely separate interviewer-facing content from the answer key."
        )

    interviewer_context = text[: split_match.start()].strip()
    evaluator_only = text[split_match.start():].strip()

    guardrail_match = re.search(r"^\*\*Guardrail reminder:\*\*\s*(.+)$", text, re.MULTILINE)
    guardrail_reminder = guardrail_match.group(1).strip() if guardrail_match else ""

    case_id = Path(path).stem
    return Case(
        case_id=case_id,
        title=title,
        interviewer_context=interviewer_context,
        evaluator_only=evaluator_only,
        guardrail_reminder=guardrail_reminder,
        raw_text=text,
    )


def list_cases(cases_dir: str = "cases"):
    return sorted(Path(cases_dir).glob("case_*.md"))


if __name__ == "__main__":
    import sys
    p = sys.argv[1] if len(sys.argv) > 1 else "cases/case_01_profitability_peak_performance.md"
    c = load_case(p)
    print(f"Loaded: {c.title}")
    print(f"Interviewer context length: {len(c.interviewer_context)} chars")
    print(f"Evaluator-only length: {len(c.evaluator_only)} chars")
    print(f"Guardrail reminder: {c.guardrail_reminder!r}")
    assert "Model answer" not in c.interviewer_context, "LEAK: model answer present in interviewer context!"
    assert c.guardrail_reminder, "No guardrail reminder found -- check the case file format."
    print("OK: no leakage of model answer into interviewer context, guardrail reminder found.")
