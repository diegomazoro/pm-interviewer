*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 20 — Stripe: Reading a Checkout A/B Test (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Stripe Checkout, the hosted payment page merchants send their customers to. Your team redesigned the page to show express payment options, like saved cards and wallets, at the top before the regular card form. You ran a two-week A/B test, and the experiment dashboard says conversion went up 4.2% in the new version. Your director wants to know: should we roll it out to 100% of traffic? How would you approach this decision?"

**Objective (private reference, reveal only if asked directly):** Decide whether the test result is trustworthy and large enough to justify shipping, and define what would make it a confident decision.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is 'conversion' defined?" | Completed payments divided by checkout sessions started. | On request |
| 2 | "What was the goal of the redesign, and what's the primary metric?" | The goal was more completed payments for merchants. Conversion as defined above was the pre-registered primary metric. | On request |
| 3 | "How was traffic split, and how many sessions were in each group?" | Planned split was 50/50, randomized per checkout session. Reveal Exhibit 1 once asked for the sample sizes or the raw numbers. | On request |
| 4 | "Is the result statistically significant?" | The dashboard reports the 4.2% lift as statistically significant. | On request |
| 5 | "Were there any bugs, incidents, or rollout issues during the test?" | Engineering mentioned that the new page had loading problems on some older Android browsers, and that the team added a fallback during the test. | On request |
| 6 | "What does the fallback do?" | When the new page failed to load, the session was served the old page instead -- and the experiment logged those sessions under the old-page (control) group. | Reveal only if asked specifically what the fallback does or how those sessions were counted |
| 7 | "Can I see results by device, browser, or segment?" | Reveal Exhibit 2 once asked for any segment breakdown. | On request |
| 8 | "How did the effect change over time?" | Reveal Exhibit 3 once asked about the trend over time or week by week. | On request |
| 9 | "Did you track guardrail metrics -- speed, errors, fraud, refunds?" | Reveal Exhibit 4 once asked about guardrails or any secondary metric. | On request |
| 10 | "How much is a percentage point of conversion worth?" | Across all merchants on Checkout, one percentage point of conversion is roughly $3B a year in additional payment volume. | On request |

**Guardrail reminder:** Do not point the candidate toward the sample split, the fallback, the device breakdown, or the week-by-week trend, and do not confirm or deny whether the 4.2% is real -- the core skill being tested is whether they question the result on their own and ask for the data that would validate it.

---

## C. Exhibits / data

**Exhibit 1 — Overall Test Results**

| Group | Sessions | Completed payments | Conversion |
|---|---|---|---|
| Control (old page) | 1,120,000 | 694,000 | 62.0% |
| Treatment (new page) | 1,000,000 | 646,000 | 64.6% |

**Exhibit 2 — Results by Browser Segment**

| Segment | Group | Sessions | Conversion |
|---|---|---|---|
| Modern browsers | Control | 1,000,000 | 64.0% |
| Modern browsers | Treatment | 1,000,000 | 64.6% |
| Older Android browsers | Control | 120,000 | 45.0% |
| Older Android browsers | Treatment | 0 | -- |

**Exhibit 3 — Week-by-Week Conversion (modern browsers only)**

| Week | Control | Treatment |
|---|---|---|
| Week 1 | 64.0% | 65.2% |
| Week 2 | 64.0% | 64.0% |

**Exhibit 4 — Guardrail Metrics**

| Metric | Control | Treatment |
|---|---|---|
| Page load time (75th percentile) | 1.1 s | 1.4 s |
| Payment error rate | 1.8% | 1.7% |
| Dispute rate (early read) | 0.31% | 0.30% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Confirm the metric definition and the decision being made (ship or not, and how confident we need to be).
2. Check trustworthiness before interpreting: sample ratio, instrumentation, bugs, novelty effects.
3. Compare like-for-like segments to estimate the true effect.
4. Check guardrails, then decide -- with a plan for what to do next.

**Correct core insight:** The 4.2% is not trustworthy. The planned 50/50 split came out about 53/47 (1,120,000 vs 1,000,000 sessions) -- a sample ratio mismatch that, at this scale, can't be chance. The cause is the fallback: older Android sessions that failed on the new page were logged as control, so every older Android session (all 120,000, which convert at only 45%) ended up in control, dragging it down. Comparing like with like (modern browsers only) the lift is 64.6% vs 64.0% -- about 0.6 percentage points, or about 0.9% relative, not 4.2%. And Exhibit 3 shows even that may be a novelty effect: +1.2 points in week 1 and zero in week 2. Exhibit 4 adds a real cost: the page is about 300 ms slower, and the new page doesn't work at all for older Android users.

**Quantitative reasoning a strong candidate shows:**
- Spots the split: 1,120,000 / 2,120,000 = about 52.8% in control instead of 50%.
- Recomputes the like-for-like lift: 64.6 - 64.0 = 0.6 points, about 0.9% relative.
- Notes the week-2 effect is zero, so the steady-state effect may be close to nothing.
- Optionally sizes the stakes: 0.6 points x $3B per point = about $1.8B of payment volume a year if real -- worth getting right, not worth shipping on a broken test.

**A strong final recommendation includes:**
- Don't ship to 100% on this result; the headline number is driven by an assignment bug.
- Fix older Android support (or exclude it from both groups by design), fix how fallback sessions are assigned, and re-run for long enough to see past the novelty period (e.g. 3-4 weeks).
- Keep conversion as the primary metric with guardrails on page speed, payment errors, and disputes; investigate the slower load time, which could be eating into any gain.
- Optionally: ship to modern browsers only behind a holdout if there's a business reason to move faster, while measuring the long-run effect.

**Scoring anchors:**
- 5/5 insight generation: catches the sample ratio mismatch and its cause, recomputes the like-for-like effect, notices the novelty pattern, and recommends a clean re-run with guardrails.
- 3/5: questions the result (asks about segments or time) and finds one issue, but still recommends shipping or doesn't quantify the corrected effect.
- 1/5: accepts the 4.2% at face value and recommends shipping, or asks only about statistical significance.
