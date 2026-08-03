*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 10 — OpenAI: Safeguards for an Agent That Acts on a User's Behalf (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at OpenAI. ChatGPT's agent mode can already browse the web and take actions on a user's behalf -- filling out forms, adding items to a cart, submitting information -- and its capabilities are expanding to include actions with real-world consequences, like completing a purchase or booking a reservation. Your team needs to decide how the product should handle these higher-stakes actions. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Design an approach to authorizing consequential agent actions that balances user trust and safety against friction, with a clear v1 scope and concrete success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who's the primary user for agent mode today?" | Not fully decided -- early usage skews toward tech-savvy power users automating multi-step tasks (travel booking, shopping, research) rather than mainstream casual users. | On request |
| 2 | "What's the business motivation for expanding into consequential actions?" | It's viewed as a major differentiator and engagement/subscription driver, and a natural extension of agent mode beyond read-only tasks. | On request -- important scoping context |
| 3 | "What safeguards exist today?" | Today the agent generally pauses and asks the user to manually complete any step involving payment or submitting personal information; it doesn't yet distinguish low-risk from high-risk actions beyond that blanket rule. | On request |
| 4 | "Can the agent reliably tell reversible from irreversible actions?" | Not reliably -- e.g., adding an item to a cart is reversible, submitting a non-refundable booking is not, but this distinction isn't consistently modeled today. | On request |
| 5 | "What do competitors do here?" | Reveal Exhibit 2 (competitive landscape note) if asked. | On request |
| 6 | "Is there any pilot data on how this works today?" | Reveal Exhibit 1 (early pilot data) once the candidate asks for data/evidence, or once they've proposed an initial direction. | On request or framework-gated |
| 7 | "What happens if the agent takes a wrong or unwanted action?" | Open design question -- there's no rollback/undo mechanism today; a mistaken purchase or booking is handled through normal customer support, not a product-level safeguard. | On request |
| 8 | "Are there account-security concerns, e.g. the agent using saved payment info?" | Yes -- agent actions today use the same saved payment/account info a user would use manually, with no separate lower-trust sandbox for agent-initiated actions. | On request |

**Guardrail reminder:** Do not tell the candidate which confirmation mechanism, risk-tiering approach, or starting user segment to pick, and do not confirm whether any specific idea (e.g., a blanket confirmation screen) is "the" right direction -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in an early test, adding a confirmation screen before every consequential action reduced completed agent tasks by 35%, but among the users who did see the confirmation screen, about 80% approved it in under 2 seconds without appearing to read the details."

---

## C. Exhibits / data

**Exhibit 1 — Early Pilot Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| % of agent sessions including at least one "consequential" action (payment, form submission, irreversible send) | 18% |
| % of those actions where the user had already given very specific instructions (e.g., "book the 6pm flight under $300") | 64% |
| Avg. time spent on the confirmation screen before approving | 1.8 seconds |
| % of support contacts related to the agent taking an unwanted action | 2.3% |
| % drop in completed agent tasks after adding a confirmation screen before every consequential action | 35% |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

At least two competing AI assistants have shipped "review before you click" style previews rather than a blocking confirmation for every step, and generally scope early consequential-action support to a pre-approved allow-list of sites/services rather than the open web.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** narrows to a specific starting segment and
action type rather than "all consequential actions for all users" --
e.g., starting with power users who already give highly specific
instructions (exhibit 1, question 1 confirms this is 64% of cases),
and a bounded action type like completing a purchase from a pre-approved
list of merchants, rather than the open web.

**Product taste:** goes beyond "add a confirmation screen" -- e.g.,
proposes risk-tiered handling where fully-specified, low-ambiguity
actions get a lightweight preview while ambiguous or irreversible
actions get a fuller review step, or proposes surfacing what the agent
is about to do in plain language rather than a generic Yes/No dialog.
Shows conviction in one direction rather than listing options with no pick.

**Prioritization & tradeoffs:** explicitly scopes v1 -- e.g., launch
consequential actions only for a narrow set of pre-vetted merchants/
services with reversible outcomes (cart checkout with a cancellation
window), deferring irreversible or ambiguous actions (non-refundable
bookings, one-off form submissions to arbitrary sites) to a later phase.

**Business judgment & metrics:** ties the recommendation to the stated
motivation (differentiation, subscription engagement) and proposes
concrete metrics -- e.g., completion rate of consequential tasks, rate of
user-reported "unwanted action" incidents, and confirmation-approval
read time as a proxy for whether users are actually engaging with
safety prompts -- rather than a vague goal like "make it safer."

**Composure under the follow-up:** the scripted twist (confirmation
fatigue -- fast, unread approvals, and a 35% drop in completed tasks)
directly challenges a naive "confirm everything" answer. A strong
candidate adapts -- e.g., proposes risk-based confirmation only for
ambiguous/irreversible actions, batches confirmations, or makes the
default action reversible so most flows skip confirmation entirely --
rather than dismissing the data or abandoning their framework.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the confirmation-fatigue tension (e.g., risk-tiered or reversible-by-default
  actions) even before the twist is revealed, and defends the choice.
- 3/5: candidate proposes a reasonable but generic confirmation flow and
  adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("add a safety check") with
  no segmentation, no metrics, and struggles to respond to the twist.
