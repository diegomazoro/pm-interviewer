*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 9 — Anthropic: Designing Longer-Running Autonomous Tasks (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Anthropic. Claude can already write code, browse, and take actions on a user's behalf through tool use, but today it mostly works in short bursts with a human checking in frequently. Your team is exploring giving Claude the ability to work on multi-step tasks over much longer stretches of time -- for example, managing a multi-day project end-to-end -- with less constant supervision. How would you approach designing this?"

**Objective (private reference, reveal only if asked directly):** Design an approach to longer-running, more autonomous task execution, with a clear view of who it's for, what the MVP looks like, how autonomy is bounded, and how success is measured.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who is the target user for this -- developers, enterprises, or general consumers?" | Not decided yet -- that's part of what the candidate should reason through. All three currently use Claude in some form, but usage patterns differ a lot: developers use it inside their own tooling, enterprises route it through internal workflows, consumer users use the chat app directly. | On request |
| 2 | "What counts as a 'task' here -- can you give an example?" | Examples under discussion: triaging and responding to a backlog of support tickets over several days, researching and drafting a multi-section report, or managing a recurring data-cleanup job. Nothing is finalized. | On request |
| 3 | "What safeguards exist today?" | Today, Claude generally pauses for explicit confirmation before higher-risk actions (e.g. sending an email, making a purchase, deleting data), and sessions are short enough that a human is naturally still "in the loop." | On request |
| 4 | "What's the business motivation here?" | Longer-running autonomous work is where competitors are investing heavily, and enterprise customers have specifically asked for it to replace multi-step manual workflows; it's seen as a meaningful growth area, not just a research curiosity. | On request -- important scoping context |
| 5 | "What's technically possible right now vs. still a research problem?" | Longer context windows and more reliable multi-step tool use already exist; what's unsolved is *reliably* noticing when something has gone wrong mid-task without a human watching every step. | On request |
| 6 | "Are there any internal usage or research signals so far?" | Reveal Exhibit 1 (early pilot data) once the candidate asks for data or evidence, or once they've proposed an initial direction. | On request or framework-gated |
| 7 | "What do competitors offer here?" | Reveal Exhibit 2 (competitive landscape note) if asked specifically about the competitive picture. | On request |
| 8 | "What would happen if the task goes wrong partway through?" | That's an open design question -- there's no current mechanism for a long-running task to detect and safely pause itself mid-way if something looks off; this is one of the harder unsolved parts. | On request |

**Guardrail reminder:** Do not tell the candidate which user segment, checkpoint design, or autonomy model to pick, and do not confirm whether "checkpoints" or any other specific mechanism is the right direction -- these are exactly the kinds of decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in an early internal pilot, tasks that paused for a check-in had a 90% satisfaction rate when the check-in happened once, but users started ignoring or auto-approving the check-in prompt without reading it once it appeared more than twice in the same task."

---

## C. Exhibits / data

**Exhibit 1 — Early Pilot Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| Avg. task length in pilot (multi-step, low supervision) | 6 hours of elapsed task time |
| % of pilot tasks completed without any human correction needed | 61% |
| % of pilot tasks where a human had to step in to correct a mistake | 24% |
| % of pilot tasks abandoned/timed out | 15% |
| Most common failure mode reported | Task "drifted" from the original goal over many steps without noticing |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

At least two competing AI labs have shipped early versions of longer-running agent products, generally aimed at developer/enterprise workflows first rather than general consumers, and generally marketed with heavy caveats about needing human review of the final output.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** picks a specific starting segment rather than
"everyone" -- e.g., enterprise workflow teams already running Claude on
recurring internal processes, since exhibit 1 shows real signal there and
question 4 confirms enterprise demand exists today. Explicitly scopes what
"long-running" means for a first version (e.g., hours, not days, to start).

**Product taste:** goes beyond "just add a confirmation step" -- e.g.,
proposes a check-in mechanism that adapts based on task risk level rather
than firing on a fixed schedule, or a way for the agent to summarize
what it's done so far so a human can spot drift without reading every
step. Shows conviction in a specific direction rather than listing five
options with no pick.

**Prioritization & tradeoffs:** explicitly states an MVP boundary -- e.g.,
launch with a single supported task type and a hard time-boxed limit
before requiring human sign-off, deferring fully open-ended multi-day
autonomy. Explicitly says what's out of scope for v1.

**Business judgment & metrics:** ties the recommendation back to the
stated business motivation (enterprise demand, competitive pressure) and
proposes concrete metrics -- e.g., task-completion rate without
correction, plus a guardrail metric like rate of undetected task drift or
rate of human overrides -- rather than a vague goal like "make it more
autonomous."

**Composure under the follow-up:** the scripted twist (check-in fatigue
after repeated prompts) directly challenges a naive "just add more
check-ins" answer. A strong candidate adapts -- e.g., proposes adaptive or
risk-based check-in frequency instead of a fixed cadence, or a passive
progress summary instead of an interruptive prompt -- rather than
dismissing the data or abandoning their framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design directly anticipates or elegantly
  resolves the check-in-fatigue tension (e.g., adaptive/risk-based
  check-ins) even before the twist is revealed, and defends the choice.
- 3/5: candidate proposes a reasonable but generic solution (fixed
  periodic check-ins) and adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("add more safety checks")
  with no segmentation, no metrics, and struggles to respond to the twist.
