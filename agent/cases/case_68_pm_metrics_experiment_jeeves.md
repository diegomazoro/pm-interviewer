*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 68 — Jeeves: Was the Higher Cashback Worth It? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Jeeves. Three months ago you raised cashback on card spend from 1% to 1.5% for all customers in Mexico, as a promotion. Since then, monthly card spend in Mexico has grown 25%. The marketing team wants to make the higher cashback permanent and roll it out to every country. Your CFO asks whether it actually paid off. How would you evaluate it?"

**Objective (private reference, reveal only if asked directly):** Determine the incremental effect of the cashback increase and whether it's profitable.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What was monthly spend before and after?" | About $100M a month before, $125M a month during the promotion. | On request |
| 2 | "What does Jeeves earn on card spend?" | About 1.8% of spend (interchange). | On request |
| 3 | "Was there a control group?" | Yes -- by accident, about 10% of customers weren't enrolled due to a configuration error and stayed at 1%. | On request -- key fact |
| 4 | "What happened in the control group?" | Reveal Exhibit 1 once asked about the control group or a comparison. | On request |
| 5 | "Did anything else drive growth in those months?" | New customer signups were strong, and the period included the end-of-year season, when business spending is usually higher. | On request |
| 6 | "Did customers change how they spend?" | Reveal Exhibit 2 once asked about spend behavior or patterns. | On request |

**Guardrail reminder:** Do not mention incrementality, seasonality, or the control group unless asked -- the candidate should question the 25% on their own.

---

## C. Exhibits / data

**Exhibit 1 — Spend Growth, Promotion vs. Not Enrolled (same 3 months)**

| Group | Spend growth vs. prior 3 months |
|---|---|
| Customers at 1.5% cashback | +25% |
| Customers who stayed at 1% (control) | +16% |

**Exhibit 2 — Spend Patterns at 1.5%**

| Metric | Value |
|---|---|
| Share of extra spend that was previously paid by bank transfer (e.g. suppliers that accept cards with a fee) | 40% |
| Share of customers who said they'd move spend back if cashback returns to 1% | 55% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Separate incremental growth from what would have happened anyway (seasonality, new customers).
2. Use the control group to estimate the true effect.
3. Compute profit: extra interchange vs. extra cashback cost.
4. Decide whether to keep it, change it, or roll it out.

**Quantitative reasoning a strong candidate shows:**
- Incremental effect: about 25% - 16% = 9 points of growth from the promotion (roughly $9M a month on a $100M base).
- Without the promotion, spend would have been about $116M; with it, $125M.
- Revenue: interchange on the extra $9M = 1.8% x $9M = $162K a month.
- Cost: with the promotion, cashback is 1.5% x $125M = $1.875M a month; without it, 1% x $116M = $1.16M -> extra cost about $715K a month.
- Net: $162K - $715K = about -$550K a month.

**Correct core insight:** Most of the 25% would have happened anyway (the control grew 16%). The promotion's real effect is about 9 points, and paying extra cashback on all spend (not just the extra) costs about four times what the extra spend earns. Rolling it out everywhere would multiply the loss. Some of the extra spend is also customers paying suppliers by card with fees just to earn cashback, which may not last.

**A strong final recommendation includes:**
- Don't make 1.5% permanent for everyone; don't roll it out to other countries.
- Consider targeted incentives: higher cashback only on incremental spend above a customer's baseline, or on specific categories Jeeves wants to win.
- Run proper tests with a planned control group in future.
- Metrics: incremental spend vs. control, net margin (interchange minus rewards), customer retention.

**Scoring anchors:**
- 5/5 insight generation: uses the control group, computes incremental revenue vs. total extra cost, recognizes seasonality, and recommends targeted incentives.
- 3/5: uses the control group but doesn't compute profit, or computes cost without the control.
- 1/5: recommends rolling it out because spend grew 25%.
