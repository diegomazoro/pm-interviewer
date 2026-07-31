*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 4 — Figma: Drop in Customer Satisfaction (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Figma. Every quarter, the company surveys users and tracks an NPS-style satisfaction score. This quarter, satisfaction among Professional-plan (paid, small team) users dropped from 42 to 28 — a big drop — while Enterprise and Free-tier users stayed flat. Your VP of Product wants to know why, and what you'd do about it. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the cause of the Professional-plan satisfaction drop and recommend a response.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is satisfaction measured — survey, in-app, timing?" | Quarterly in-app survey, single 0–10 "how likely to recommend" question plus optional free-text comment, sent to a random sample of active users per tier. | On request |
| 2 | "Did anything change for Professional-plan users this quarter — pricing, features, limits?" | Yes — two changes: (1) Professional plan price increased 20% two months ago, (2) a new default "AI design suggestions" feature was rolled out to all Professional users, on by default. | On request — key fact, should surface this |
| 3 | "Did usage/engagement metrics change for this segment (logins, files created, time in app)?" | Roughly flat — no meaningful change in login frequency or files created. | On request |
| 4 | "What do the free-text comments say?" | Reveal Exhibit 1 (sample verbatim themes) once candidate asks for qualitative detail. | On request |
| 5 | "Did churn/cancellation rate change for this segment?" | Cancellations ticked up slightly (from 3%/month to 4.5%/month) but the survey drop is much larger in magnitude than the churn change so far — suggesting dissatisfaction is running ahead of actual churn. | On request |
| 6 | "Is the AI feature something users can turn off?" | Yes, but it's on by default and the setting to disable it is two menus deep; usage data shows only 8% of Professional users have turned it off. | Reveal if asked about the feature's configurability |
| 7 | "Did the price increase apply to Enterprise and Free tiers too?" | No — only Professional. Enterprise pricing is negotiated separately per contract; Free tier has no price. | On request — explains why other tiers stayed flat, important scoping clue |
| 8 | "How does the new AI feature actually perform / any quality complaints?" | Reveal Exhibit 2 (AI suggestion acceptance rate data) once asked about feature quality. | On request |
| 9 | "What's the size of this segment — how many users, how much revenue?" | ~180,000 Professional-plan users, roughly $65M of annual recurring revenue. | On request |
| 10 | "Can I see the data / exhibits?" | Hand over Exhibit 1 once a framework/hypothesis structure is proposed. | Framework-gated |

**Guardrail reminder:** Do not tell the candidate whether it's the price increase or the AI feature driving the drop — both are real, independent factors; let them use the exhibits to weigh which matters more, or conclude both matter.

---

## C. Exhibits / data

**Exhibit 1 — Sample of Free-Text Survey Comments (Professional tier, this quarter)**

- "Paying more for basically the same tool doesn't feel great." (price-related, ~40% of comments coded this way)
- "The new AI suggestions get in the way, I didn't ask for them." (AI-feature-related, ~35% of comments)
- "Wish it was easier to turn off the auto-suggestions." (AI-feature-related)
- "Price hike came out of nowhere, no extra value I can see." (price-related)
- Remaining ~25% of comments: unrelated/neutral or praise.

**Exhibit 2 — AI Design Suggestion Feature Usage Data**

| Metric | Value |
|---|---|
| % of Professional users who saw a suggestion this quarter | 92% |
| % who accepted at least one suggestion | 22% |
| % who dismissed all suggestions shown to them | 61% |
| % who disabled the feature entirely | 8% |
| Avg. suggestions shown per active session | 3.4 |

**Exhibit 3 (reveal only if asked about competitive context) — Competitive Note**

A competitor design tool announced a similar AI feature as opt-in (off by default) around the same time, marketed as "AI when you want it." No pricing change from that competitor this quarter.

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build (PM-style diagnostic):**
1. Confirm the metric and scope it (which segment, how measured, how big a deal is it — e.g., revenue at risk).
2. Generate hypotheses across categories: pricing/value perception, product changes, external/competitive, and measurement/sampling artifacts.
3. Use engagement + qualitative + business data to test each hypothesis.
4. Prioritize the most supported hypothesis(es) and recommend action, with a way to measure impact.

**Correct core insight:** Two independent, compounding causes hit the same segment at the same time: a 20% price increase (value-perception hit, no engagement change) and an intrusive, on-by-default AI feature with a low acceptance rate (22%) and high dismissal rate (61%) that many users can't easily turn off. The qualitative data (Exhibit 1) shows both themes appearing roughly equally, so a strong candidate should conclude it's not an either/or — both need addressing — rather than searching for one root cause.

**A strong final recommendation includes:**
- Make the AI suggestion feature opt-in (or at minimum put the disable toggle one click away), directly responding to the dismissal-rate and comment data.
- Reassess the price increase: consider whether a value-add (e.g., messaging the AI feature as a benefit, once it's less intrusive) or a partial rollback/grandfathering for existing users is warranted, especially since churn is trending up faster than before.
- A/B test or phased rollout of any fix, with a plan to re-survey a sample rather than wait a full quarter to see if satisfaction recovers.
- Flag revenue at risk (~$65M ARR segment, churn already ticking from 3% to 4.5%) to prioritize this appropriately versus other roadmap items.

**Scoring anchors:**
- 5/5 insight generation: candidate identifies both causes, uses Exhibit 2's acceptance/dismissal data to argue the AI feature is genuinely a UX problem (not just a matter of taste), and doesn't force a single root cause.
- 3/5: candidate finds one of the two causes and treats it as the whole story.
- 1/5: candidate guesses at causes without requesting the product-change or qualitative data at all.
