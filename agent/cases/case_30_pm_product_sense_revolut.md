*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 30 — Revolut: Helping Young Adults Build a Saving Habit (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Revolut. A large share of your customers are between 18 and 25. Many of them use Revolut every day for spending, but very few of them save regularly -- most end each month with close to nothing left. How would you design a product experience that helps young adults build a real saving habit?"

**Objective (private reference, reveal only if asked directly):** Design an approach that helps 18-25 year olds save consistently, with a clear target user, MVP, tradeoffs, and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Which markets?" | Focus on Europe, where most of these customers are. | On request |
| 2 | "Who are these users, more specifically?" | Mostly students and people in their first jobs. Income is low and often irregular -- part-time work, freelance gigs, or money from family. | On request |
| 3 | "What saving tools exist in the app today?" | Savings "vaults" where users can move money manually, with optional round-ups of card payments to the nearest euro. | On request |
| 4 | "How are the existing tools used?" | Reveal Exhibit 1 once asked for usage data. | On request |
| 5 | "Why don't they save, according to research?" | Reveal Exhibit 2 once asked about user research or reasons. | On request |
| 6 | "What does Revolut gain if they save more?" | Customers who keep balances in savings are much more likely to make Revolut their main bank as they get older, and savings balances earn Revolut interest margin. | On request -- business context |
| 7 | "Are there regulatory constraints?" | Products can't be misleading about returns, and Revolut must avoid pushing customers into financial difficulty. | On request |

**Guardrail reminder:** Do not tell the candidate which sub-segment to target or whether to use automation, gamification, goals, or social features -- they need to choose and justify.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a pilot that turned on automatic weekly savings transfers by default for young users, average savings went up a lot, but 18% of participants then had a card payment declined because the transfer had emptied their main balance -- and complaints from that group were the highest of any feature this year."

---

## C. Exhibits / data

**Exhibit 1 — Saving Tool Usage, Customers Aged 18-25**

| Metric | Value |
|---|---|
| Have ever opened a savings vault | 41% |
| Moved money into a vault in the last 30 days | 11% |
| Use round-ups | 9% |
| Median vault balance among those with a balance | €60 |
| Share who withdraw everything from a vault within 2 weeks of saving | 47% |

**Exhibit 2 — Research Themes (interviews and survey of 2,000 young customers)**

- "I'll save when I earn more." (most common)
- "I don't know how much I can afford to put away -- my income changes month to month."
- "I saved for a trip, then needed the money for rent."
- 71% said they'd like to have an emergency buffer of at least one month's rent.

---

## D. Model answer / "what good looks like"

**Strong problem framing:** picks a specific segment -- e.g. young people in first jobs with irregular income -- and a specific goal, like building a small emergency buffer, rather than "saving more." Uses Exhibit 1 to see that the issue isn't access to tools (41% opened a vault) but sticking with it (47% withdraw within two weeks).

**Product taste:** strong ideas adapt to irregular income: save a percentage of each incoming payment rather than a fixed amount; "safe-to-save" amounts calculated from upcoming bills; an emergency buffer goal with clear progress; making withdrawals deliberate but not blocked; celebrating streaks. An ambitious option: a smart buffer that automatically moves money back to the main account if a payment would otherwise fail.

**Prioritization & tradeoffs:** MVP such as "save X% of every incoming payment" toward an emergency buffer goal, leaving out social features or investment products for v1. Discusses automation vs. user control.

**Business judgment & metrics:** ties to Revolut becoming the main bank over time. Metrics: share of young users saving at least monthly for 3+ months, median buffer size, share keeping savings for 60+ days. Guardrails: declined payments, overdraft-like situations, complaints.

**Composure under the follow-up:** the twist shows automation that ignores cash flow hurts users. A strong candidate adapts: trigger saving on incoming money rather than on a schedule, keep a minimum balance, auto-return money before a payment fails, or make the default opt-in. A weak candidate drops automation entirely or ignores the harm.

**Scoring anchors:**
- 5/5: specific segment, insight that habit (not access) is the problem, cash-flow-aware MVP, habit and harm metrics, thoughtful adaptation.
- 3/5: reasonable features (goals, gamification) but generic segment or vague metrics.
- 1/5: generic "add a savings goal" or "financial education," no adaptation after the twist.
