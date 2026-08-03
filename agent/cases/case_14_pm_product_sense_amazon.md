*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 14 — Amazon: Proactive Replenishment of Household Essentials via Alexa (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager on the Alexa devices team at Amazon. Customers can already say 'Alexa, reorder paper towels' to repurchase something they've bought before, but usage of this is low -- most people simply forget to reorder essentials until they've already run out. Your team wants to help customers replenish household essentials -- things like paper towels, detergent, coffee -- before they run out, using Alexa. How would you approach designing this?"

**Objective (private reference, reveal only if asked directly):** Design a proactive replenishment approach for household essentials via Alexa, with a clear starting segment, a scoped trigger/notification mechanism, and metrics that account for prediction accuracy.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who should we target first -- single-person households, families, existing Subscribe & Save users?" | Not decided -- that's part of what the candidate should reason through. Single-person households tend to have the most regular, predictable consumption patterns; multi-person households buy the same categories but with much more variable timing. | On request |
| 2 | "What's the business motivation here?" | Increasing repeat-purchase frequency and Subscribe & Save enrollment for everyday essentials, and strengthening Alexa's role as a daily-use habit rather than an occasional voice-search tool. | On request -- important scoping context |
| 3 | "What exists today?" | Customers can manually say a reorder command referencing a past purchase; there's no proactive prompt today, and awareness of the manual reorder command itself is low. | On request |
| 4 | "How would Alexa know when something is about to run out?" | Based on past purchase cadence for that item/category on the account -- e.g., if paper towels were bought roughly every 5 weeks historically, predict the next run-out around that interval. This is inherently a prediction, not a certainty. | On request |
| 5 | "Does this need order-level accuracy, or can it just be a helpful reminder?" | Open question for the candidate to weigh -- not decided whether this should auto-order, suggest-and-confirm, or just remind. | On request |
| 6 | "What do competitors or other smart-home/retail products do here?" | Reveal Exhibit 2 (competitive note) if asked. | On request |
| 7 | "Is there any data on how accurate purchase-cadence prediction is today?" | Reveal Exhibit 1 (pilot data) once the candidate asks for evidence, or once they propose an initial direction. | On request or framework-gated |
| 8 | "Does this require the customer to opt in, or would it be on by default?" | Open question -- not decided; relevant to how the candidate designs around prediction errors and trust. | On request |

**Guardrail reminder:** Do not tell the candidate which household segment, trigger mechanism (auto-order vs. suggest vs. remind), or notification design to pick, and do not confirm whether proactive voice prompts or any other specific idea is "the" right direction -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in an early test, proactive low-supply prompts based on past purchase cadence were accurate within plus-or-minus 3 days for single-person households, but for multi-person households, predicted run-out timing was off by 10 or more days on average, and 45% of users in that group who received an inaccurate prompt disabled proactive notifications entirely afterward."

---

## C. Exhibits / data

**Exhibit 1 — Prediction Pilot Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| Prediction accuracy window, single-person households | within +/- 3 days |
| Prediction accuracy window, multi-person households | off by 10+ days on average |
| % of multi-person-household users who disabled proactive notifications after one inaccurate prompt | 45% |
| % increase in reorder rate among users who received an accurate prompt | 28% |
| Awareness rate of the existing manual voice-reorder command, all users | 19% |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

Some retail and smart-home products offer sensor-based or manual-tap replenishment triggers (a physical button, or a connected dispenser) rather than relying purely on predicted purchase cadence, trading extra hardware/setup for higher accuracy.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** picks a specific starting segment rather than
"all households" -- e.g., single-person households, since exhibit 1
shows prediction is far more reliable there, deferring the noisier
multi-person case. Explicitly separates "predicting run-out timing"
from "getting customers to notice and act on the prompt," since both
matter to the stated goal.

**Product taste:** goes beyond "just send a reminder when the model
predicts run-out" -- e.g., proposes a suggest-and-confirm flow rather
than auto-ordering, with a low-friction one-tap or one-word voice
confirm, or proposes surfacing prediction confidence so low-confidence
predictions become a gentle nudge rather than a confident claim. Shows
conviction in a specific direction rather than listing options with no
pick.

**Prioritization & tradeoffs:** explicitly scopes v1 -- e.g., launch
proactive prompts only for single-person households and only for a
handful of high-frequency, low-variability categories (coffee, paper
towels) before expanding to multi-person households or a wider catalog.

**Business judgment & metrics:** ties the recommendation to the stated
motivation (repeat-purchase frequency, Subscribe & Save enrollment,
daily-use habit) and proposes concrete metrics -- e.g., reorder rate
lift among users who receive an accurate prompt, plus a guardrail
metric like the opt-out/notification-disable rate driven by inaccurate
prompts -- rather than a vague goal like "help people reorder more."

**Composure under the follow-up:** the scripted twist (prediction
accuracy collapses for multi-person households, driving a high
disable rate) directly challenges a naive "predict and notify everyone
the same way" answer. A strong candidate adapts -- e.g., restricts
proactive prompting to segments/categories where confidence is high,
lowers the confidence threshold or softens prompt language for
uncertain cases, or shifts multi-person households to a different,
lower-commitment mechanism (an easy on-demand check rather than a
proactive claim) -- rather than dismissing the data or abandoning their
framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the prediction-accuracy tension (e.g., confidence-gated prompting or
  segment-specific mechanisms) even before the twist is revealed, and
  defends the choice.
- 3/5: candidate proposes a reasonable but generic "notify everyone"
  solution and adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("remind people to
  reorder") with no segmentation, no metrics, and struggles to respond
  to the twist.
