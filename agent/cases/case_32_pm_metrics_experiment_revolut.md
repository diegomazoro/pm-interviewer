*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 32 — Revolut: Did the Selfie Check Reduce Fraud? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Revolut's fraud team. Two months ago you launched a selfie check for every transfer above €1,000. The fraud dashboard shows fraud losses on those protected transfers are down 64%, and the team wants to celebrate and extend the selfie check to other products. Your Head of Risk asks you to evaluate whether the change actually worked. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Assess the true impact of the selfie check on total fraud and on legitimate customers, and recommend what to do next.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What does the 64% measure exactly?" | Fraud losses on transfers above €1,000, compared with the two months before launch. | On request |
| 2 | "What happened to total fraud losses across all transfers?" | Reveal Exhibit 1 once asked about total fraud or fraud in other transfer sizes. | On request |
| 3 | "Did the pattern of transfers change after launch?" | Reveal Exhibit 2 once asked about transfer sizes, distribution, or fraudster behavior. | On request |
| 4 | "How did legitimate customers react to the selfie check?" | Reveal Exhibit 3 once asked about customer friction, abandonment, or complaints. | On request |
| 5 | "Was there a control group?" | No -- it was launched to everyone at the same time. | On request |
| 6 | "Did anything else change in fraud prevention during this period?" | No other major changes. | On request |
| 7 | "What does a fraud attack typically look like here?" | Mostly account takeover and scams where the victim is tricked into sending money. Fraudsters often adapt to rules within weeks. | On request |

**Guardrail reminder:** Do not mention displacement, the €900-999 band, or friction unless the candidate asks for that data -- the core skill is questioning the headline metric on their own.

---

## C. Exhibits / data

**Exhibit 1 — Monthly Fraud Losses by Transfer Size**

| Transfer size | Before launch | After launch |
|---|---|---|
| Above €1,000 | €7.0M | €2.5M |
| €900-999 | €0.8M | €3.5M |
| €500-899 | €1.2M | €1.3M |
| Below €500 | €1.0M | €1.2M |
| Total | €10.0M | €8.5M |

**Exhibit 2 — Number of Transfers in the €900-999 Range**

| Period | Transfers per month |
|---|---|
| Before launch | 410,000 |
| After launch | 690,000 |

**Exhibit 3 — Legitimate Customer Experience on Transfers Above €1,000**

| Metric | Value |
|---|---|
| Legitimate transfers abandoned at the selfie step | 11% |
| Of those, completed later (same or different method) | 40% |
| Complaints about transfers, month over month | +35% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Check the scope of the metric: protected transfers only, vs. total fraud.
2. Look for displacement: fraudsters moving to unprotected transfers.
3. Measure the cost to legitimate customers.
4. Decide what to change and how to measure it properly.

**Correct core insight:** Fraud didn't drop 64% -- it mostly moved. Losses above €1,000 fell by €4.5M, but losses just under the threshold (€900-999) rose by €2.7M, and transfers in that band jumped from 410K to 690K a month: fraudsters are splitting or sizing transfers to dodge the check. Total fraud fell only 15% (€10.0M to €8.5M). Meanwhile, 11% of legitimate large transfers were abandoned at the selfie step, and complaints rose 35%. A fixed threshold invites gaming; extending it to other products would repeat the problem.

**Quantitative reasoning a strong candidate shows:**
- Total reduction: (10.0 - 8.5) / 10.0 = 15%, not 64%.
- Displacement: €900-999 losses up €2.7M -- 60% of the €4.5M "saved" above €1,000.
- Friction: 11% abandoned, 60% of those never completed = about 6.6% of legitimate large transfers lost.

**A strong final recommendation includes:**
- Don't extend the selfie check as-is; report total fraud as the headline metric.
- Move to risk-based checks (trigger on risk signals like new payee, new device, unusual pattern) rather than a fixed amount, so fraudsters can't size around it.
- Measure total fraud losses, legitimate completion rate, and complaints together; use a holdout for future changes.

**Scoring anchors:**
- 5/5 insight generation: finds the displacement, computes the real total reduction, quantifies legitimate friction, and recommends risk-based checks.
- 3/5: asks about total fraud and sees a smaller reduction, but misses displacement or friction.
- 1/5: accepts the 64% and supports extending the check.
