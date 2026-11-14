*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 66 — Jeeves: Card Spend Falling in Mexico (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Jeeves, a corporate card and spend-management platform for startups and SMBs. In Mexico, card spend per active customer has dropped 20% over the last two months, even though the number of customers keeps growing. Other countries look stable. Your Head of Product wants to know why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the drop in card spend per active customer in Mexico and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is 'spend per active customer' calculated?" | Total card spend in the month divided by companies with at least one card transaction that month. | On request |
| 2 | "Did the customer mix change -- smaller companies joining?" | The mix of new customers by size is similar to before. | On request -- rules out mix |
| 3 | "Did fees, rewards, or pricing change?" | No changes to fees or rewards. | On request |
| 4 | "Did anything change in risk or credit?" | Two months ago, a new risk model was introduced in Mexico to set credit limits. | On request -- key fact |
| 5 | "What happened to declines?" | Reveal Exhibit 1 once asked about declined transactions or card failures. | On request |
| 6 | "Which customers are affected?" | Reveal Exhibit 2 once asked for a breakdown by customer type or tenure. | On request |
| 7 | "What do customers say?" | Reveal Exhibit 3 once asked about customer feedback or support tickets. | On request |
| 8 | "Did the new model reduce losses?" | Credit losses in Mexico are slightly lower, but they were already low before the change. | On request |

**Guardrail reminder:** Do not connect the new risk model, credit limits, and declines for the candidate -- let them find it.

---

## C. Exhibits / data

**Exhibit 1 — Declined Transactions in Mexico**

| Metric | Before | Last 2 months |
|---|---|---|
| Share of card transactions declined | 3% | 11% |
| Of declines, share due to "credit limit reached" | 30% | 72% |

**Exhibit 2 — Spend per Active Customer by Tenure**

| Customer tenure | Change in spend per customer | Average credit limit change |
|---|---|---|
| Joined in the last 12 months | -34% | -45% |
| Customers for more than 12 months | -2% | -5% |

**Exhibit 3 — Support Ticket Themes**

- "Our card got declined paying for software, again."
- "We had to switch back to our bank's card for ads spend."
- "Why did our limit go down when we always pay on time?"

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the metric; rule out customer mix and pricing.
2. Look for what changed (new risk model) and check declines.
3. Segment by customer tenure.
4. Weigh risk vs. growth and recommend fixes.

**Correct core insight:** The new risk model cut credit limits, especially for newer customers (-45%). Their cards now hit limits and get declined (declines from 3% to 11%, mostly "limit reached"), so they move spend to other cards -- spend per customer for newer customers fell 34%. Credit losses barely improved, because they were already low. The model is costing a lot of spend (and future relationships) to avoid little risk.

**A strong final recommendation includes:**
- Recalibrate the model for newer customers, using payment history and cash balances; consider gradual limit increases for customers who pay on time.
- Reach out to affected customers before they move permanently to another card.
- Product fixes: alerts before limits are reached, easy requests for limit increases.
- Metrics: decline rate, limit-related declines, spend per customer by tenure, credit losses as guardrail.

**Scoring anchors:**
- 5/5 insight generation: connects the risk model to lower limits, declines, and the tenure split; weighs small loss reduction against big spend loss; recommends recalibration and product fixes.
- 3/5: finds declines rose but doesn't connect to tenure or weigh the tradeoff.
- 1/5: assumes competitors or customer mix without checking declines.
