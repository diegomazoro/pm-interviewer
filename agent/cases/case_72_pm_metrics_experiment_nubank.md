*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 72 — Nubank: Credit Limit Increases That Look Great (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Nubank's credit card team. Three months ago, you ran a test that automatically raised credit limits for a random group of customers. Customers who got the increase spent 30% more on their cards than the control group, and early delinquency barely changed. The growth team wants to roll it out to all eligible customers. Your Head of Credit asks you to evaluate whether that's the right decision. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Evaluate whether the limit increase is profitable once delayed credit losses are considered, and decide whether to roll out.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How was delinquency measured?" | Share of customers 90+ days late on payments, measured three months after the increase. | On request |
| 2 | "What were the numbers?" | Reveal Exhibit 1 once asked for the test results. | On request |
| 3 | "How long does it usually take for credit losses to show up?" | Most defaults on new credit appear between 6 and 12 months later. | On request -- key fact |
| 4 | "Has a similar test been run before?" | Reveal Exhibit 2 once asked about past tests, earlier cohorts, or longer-term data. | On request |
| 5 | "Who was eligible?" | Customers with at least 6 months on time, across all risk levels. | On request |
| 6 | "How does Nubank earn on card spend?" | Interchange of about 1% on spend, plus interest when customers carry a balance. | On request |
| 7 | "Do results differ by customer risk level?" | Reveal Exhibit 2 once asked for a breakdown by risk level (if not already shown). | On request |

**Guardrail reminder:** Do not mention the delay in losses or the earlier cohort unless asked -- the candidate should question whether three months is enough on their own.

---

## C. Exhibits / data

**Exhibit 1 — Test Results at 3 Months**

| Metric | Control | Limit increase |
|---|---|---|
| Card spend per customer | baseline | +30% |
| Revenue per customer (interchange + interest) | baseline | +22% |
| 90+ days delinquency | 2.0% | 2.1% |

**Exhibit 2 — Earlier Pilot Cohort, 12 Months After a Similar Increase**

| Risk level | Revenue change | 90+ days delinquency: control vs. increase | Net profit change |
|---|---|---|---|
| Low risk | +18% | 1.0% vs. 1.2% | positive |
| Medium risk | +25% | 3.0% vs. 4.8% | about zero |
| High risk | +33% | 6.0% vs. 11.5% | strongly negative |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Question the time horizon: are three months enough for credit outcomes?
2. Look for longer-term evidence.
3. Segment by risk level.
4. Decide on a targeted rollout with monitoring.

**Correct core insight:** Three months is too early -- credit losses mostly show up after 6 to 12 months, so the flat delinquency at 3 months is misleading. The earlier cohort shows that at 12 months, the increase is profitable for low-risk customers, roughly break-even for medium risk, and strongly loss-making for high risk (delinquency nearly doubles). Rolling out to all eligible customers would mix profitable and losing segments.

**Quantitative reasoning a strong candidate shows:**
- High risk: delinquency 6.0% to 11.5% -- almost double, outweighing the +33% revenue.
- Low risk: small increase in delinquency (1.0% to 1.2%) vs. +18% revenue -- profitable.

**A strong final recommendation includes:**
- Roll out to low-risk customers only; hold medium risk pending more data; don't roll out to high risk.
- Evaluate credit products on vintage curves (outcomes by month since the change), not 3-month snapshots.
- Primary metric: risk-adjusted profit per customer at 12 months; guardrail: delinquency by cohort.

**Scoring anchors:**
- 5/5 insight generation: questions the time horizon, uses the earlier cohort, segments by risk, and recommends a targeted rollout with vintage monitoring.
- 3/5: suspects losses lag but doesn't use the data to segment.
- 1/5: recommends a full rollout because spend is up and delinquency looks flat.
