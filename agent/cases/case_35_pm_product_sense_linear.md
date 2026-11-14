*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 35 — Linear: Will This Project Ship on Time? (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Linear. Engineering leaders constantly get asked 'Will this project ship on time?' and they usually answer with a gut feeling, then get surprised when deadlines slip. Linear has a lot of data about how work actually moves. How would you design a product that helps teams know -- and communicate -- whether a project is on track?"

**Objective (private reference, reveal only if asked directly):** Design an approach that helps teams predict and communicate project delivery, with a clear target user, MVP, tradeoffs, and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who asks 'will it ship on time'?" | Usually executives, product leads, and other teams that depend on the project. | On request |
| 2 | "Who answers it today?" | Engineering managers and project leads, usually by reading through issues and asking engineers. | On request |
| 3 | "What data does Linear have about projects?" | Issues, estimates (if the team uses them), status changes, cycle history, who's assigned, and project target dates. | On request |
| 4 | "How often do projects slip today?" | Reveal Exhibit 1 once asked for data on delays. | On request |
| 5 | "Do teams estimate their work?" | About 45% of teams use estimates; the rest don't, and many engineers dislike estimating. | On request |
| 6 | "What do engineering managers say they need?" | Reveal Exhibit 2 once asked about research or user needs. | On request |
| 7 | "Why does this matter for Linear's business?" | Engineering leaders are the buyers. Helping them answer leadership's questions is a key reason to choose Linear over competitors. | On request |

**Guardrail reminder:** Do not tell the candidate whether to target managers, executives, or engineers, or whether to rely on estimates, forecasts, or status updates -- they need to choose.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a pilot where projects showed an automatic predicted ship date visible to the whole company, teams started inflating their estimates to keep the prediction 'green,' and after two months the predictions were less accurate than before the pilot."

---

## C. Exhibits / data

**Exhibit 1 — Project Delivery (last 12 months, projects with a target date)**

| Metric | Value |
|---|---|
| Projects delivered by their target date | 38% |
| Projects that slipped more than 2 weeks | 41% |
| Median point at which a slip was first communicated | after 80% of the planned time had passed |
| Projects where scope grew more than 30% after start | 52% |

**Exhibit 2 — Interviews with 30 Engineering Managers**

- "I usually find out a project is late when it's already too late to do anything."
- "Scope creep is the real killer, not slow engineers."
- "I spend Friday afternoons writing status updates nobody reads carefully."
- "If a tool judges my team, they'll game it."

---

## D. Model answer / "what good looks like"

**Strong problem framing:** picks the engineering manager or project lead as the user, with the goal of spotting risk early and communicating it -- not "predict dates perfectly." Uses Exhibit 1 to see that slips are communicated late (80% of the way in) and that scope growth is common.

**Product taste:** strong ideas include early-warning signals (scope growth, work not started, blocked issues) instead of a single predicted date; scope change tracking against the original plan; auto-drafted status updates that the lead edits; a range ("likely between X and Y") rather than a precise date. An ambitious option: "what-if" planning that shows what to cut to hit the date.

**Prioritization & tradeoffs:** MVP such as a project health view for leads with scope-change and risk signals plus an auto-drafted weekly update, leaving out company-wide predicted dates and estimate-dependent forecasting for v1. Discusses visibility vs. gaming.

**Business judgment & metrics:** ties to engineering leaders as buyers. Metrics: how early slips are communicated (as % of planned time), share of projects on time, time spent writing updates. Guardrails: estimate inflation, team sentiment.

**Composure under the follow-up:** the twist shows that public, automatic predictions create pressure to game inputs. A strong candidate adapts: keep forecasts private to the team lead first, rely on signals that are harder to game (scope changes, progress), show ranges, and treat the lead as the owner who communicates. A weak candidate drops prediction entirely or ignores gaming.

**Scoring anchors:**
- 5/5: specific user, focus on early risk detection over precise dates, clear MVP, metrics on early communication, strong adaptation to gaming.
- 3/5: reasonable forecast feature but generic user or metrics only on accuracy.
- 1/5: "AI predicts the ship date" with no thought about inputs, gaming, or who acts on it.
