*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 40 — Mercado Libre: Lowering the Free Shipping Threshold (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Mercado Libre Mexico. Your team ran an A/B test that lowered the free-shipping threshold from 299 pesos to 199 pesos. In the test group, orders went up 12%. The growth team wants to roll it out to everyone right away. Your director asks you whether that's the right call. How would you evaluate the result?"

**Objective (private reference, reveal only if asked directly):** Evaluate whether the lower threshold creates value once costs and customer behavior are considered, and recommend a decision.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What was the goal of lowering the threshold?" | To grow purchases and attract new buyers, especially for low-priced items. | On request |
| 2 | "How long did the test run and how big was it?" | Four weeks; users were randomly split, with about 100,000 orders a week in the control group. | On request |
| 3 | "What happened to total sales value, not just orders?" | Reveal Exhibit 1 once asked about GMV, order value, or revenue. | On request |
| 4 | "Who pays for free shipping?" | Mercado Libre subsidizes it: about 85 pesos per free-shipped order on average. | On request |
| 5 | "What does Mercado Libre earn per sale?" | About 15% of the order value. | On request |
| 6 | "Did new buyers or repeat purchases change?" | Reveal Exhibit 2 once asked about new buyers, retention, or longer-term effects. | On request |
| 7 | "Did people split orders?" | Some did -- part of the order growth came from buyers placing two smaller orders instead of one larger one. | Reveal only if asked specifically about order splitting |

**Guardrail reminder:** Do not point the candidate to shipping costs, order value, or splitting -- they should ask about the economics on their own. Don't say whether to roll out.

---

## C. Exhibits / data

**Exhibit 1 — Weekly Results (per group)**

| Metric | Control (299 threshold) | Test (199 threshold) |
|---|---|---|
| Orders | 100,000 | 112,000 |
| Average order value | 420 pesos | 385 pesos |
| GMV | 42.0M pesos | 43.1M pesos |
| Share of orders shipped free | 55% | 78% |

**Exhibit 2 — Buyer Effects**

| Metric | Control | Test |
|---|---|---|
| New buyers per week | 8,000 | 8,640 |
| 60-day repeat purchase rate of new buyers | 34% | 36% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Go beyond orders: GMV, revenue, and shipping cost.
2. Compute the net economic effect.
3. Consider long-term value: new buyers and repeat behavior.
4. Decide, possibly with a targeted version.

**Quantitative reasoning a strong candidate shows:**
- GMV: 43.1M vs. 42.0M = +2.6%, far below the +12% order growth (lower order value, some splitting).
- Revenue gain: 1.1M x 15% = about 0.17M pesos a week.
- Shipping cost: control 55,000 free orders x 85 = 4.68M; test 87,360 x 85 = 7.43M -> +2.75M pesos a week.
- Net: about -2.6M pesos a week before long-term effects.
- New buyers: +640 a week, with slightly better repeat rate. Each would need to be worth roughly 4,000 pesos of future profit to break even -- unlikely for most.

**Correct core insight:** Orders up 12% looks great, but most of it is smaller orders and splitting; GMV only grows 2.6%, and the extra shipping subsidy costs about 16x the extra revenue. The only real upside is new buyers, so a targeted version -- the lower threshold only for first purchases or new buyers, or only in specific categories -- could capture that benefit without subsidizing every existing customer.

**A strong final recommendation includes:**
- Don't roll out to everyone.
- Test a targeted version (new buyers only, or low-ticket categories where competition is fierce).
- Primary metric: contribution profit per user (or GMV net of shipping cost), with new buyer growth and repeat rate as secondary.
- Watch for order splitting as a guardrail.

**Scoring anchors:**
- 5/5 insight generation: computes GMV, revenue, and shipping cost, shows the net loss, weighs new-buyer value, and proposes a targeted test.
- 3/5: notices lower order value or higher cost, but doesn't quantify the net effect.
- 1/5: recommends rolling out because orders went up 12%.
