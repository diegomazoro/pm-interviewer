*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 70 — Nubank: Approved Loans That Never Get Disbursed (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Nubank Mexico, working on personal loans. Loan applications are growing, and approval rates are stable. But the share of approved customers who actually complete the process and receive their money has fallen from 70% to 52% over the last six weeks. Your director wants to know why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose why fewer approved loans are being disbursed and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What steps happen between approval and receiving the money?" | After approval, the customer reviews the offer, confirms their identity with a government ID number check, signs the contract in the app, and the money is sent to their account. | On request |
| 2 | "Did interest rates or loan offers change?" | No changes to rates, amounts, or terms. | On request -- rules out offer changes |
| 3 | "Where in the process do people drop off?" | Reveal Exhibit 1 once asked about the funnel or drop-off by step. | On request |
| 4 | "Did anything change in the identity step?" | Six weeks ago, a new regulation required checking each customer's ID number directly with a government service in real time. | On request -- key fact |
| 5 | "Is the drop different by time, device, or customer type?" | Reveal Exhibit 2 once asked for a breakdown by time of day, device, or segment. | On request |
| 6 | "What do customers say?" | Reveal Exhibit 3 once asked about complaints or feedback. | On request |
| 7 | "Do customers who drop off come back later?" | About 20% of those who fail the identity step try again within 7 days; the rest don't. | On request |

**Guardrail reminder:** Do not connect the regulation, the government service, and time of day for the candidate -- let them find the pattern in the exhibits.

---

## C. Exhibits / data

**Exhibit 1 — Completion by Step (approved customers)**

| Step | Before | Last 6 weeks |
|---|---|---|
| Reviewed offer | 95% | 95% |
| Passed identity check | 90% | 66% |
| Signed contract | 74% | 54% |
| Money received | 70% | 52% |

**Exhibit 2 — Identity Check Success Rate by Time of Day (last 6 weeks)**

| Time of day | Success rate | Share of attempts |
|---|---|---|
| 12am - 9am | 92% | 15% |
| 9am - 3pm | 51% | 50% |
| 3pm - 12am | 79% | 35% |

**Exhibit 3 — Customer Complaints**

- "It keeps saying 'try again later' at the ID step."
- "Waited for the screen to load and it timed out."
- "I gave up and got a loan from another app."

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Map the steps after approval and find where drop-off increased.
2. Rule out offer changes; look at what changed in the failing step.
3. Segment by time of day, device, and customer type.
4. Recommend short-term and long-term fixes.

**Correct core insight:** The drop happens at the identity check (90% to 66% pass). The new regulation requires a real-time check against a government service, and that service fails or times out under load -- the success rate is 51% during peak hours (9am-3pm), when half of attempts happen, vs. 92% overnight. Customers see "try again later," most never return, and some take a loan elsewhere. It's an infrastructure and experience problem, not a customer-quality problem.

**Quantitative reasoning a strong candidate shows:**
- Weighted success: 0.15 x 92% + 0.50 x 51% + 0.35 x 79% = 13.8 + 25.5 + 27.7 = 67% -- consistent with the 66% overall.

**A strong final recommendation includes:**
- Don't make customers retry manually: queue the check, retry automatically in the background, and notify the customer when it passes.
- Save progress so customers don't restart the process.
- Work with the government service on capacity; monitor its availability.
- Check whether the regulation allows a temporary alternative check during outages.
- Metrics: identity-check success rate by hour, approval-to-disbursement rate, abandoned approved loans.

**Scoring anchors:**
- 5/5 insight generation: finds the identity-check drop, connects it to the regulation and peak-hour failures, quantifies, and recommends asynchronous retries.
- 3/5: finds the failing step but not the time-of-day pattern or cause.
- 1/5: blames interest rates or competitors without looking at the funnel.
