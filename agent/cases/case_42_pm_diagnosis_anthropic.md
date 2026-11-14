*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 42 — Anthropic: Rising Churn Among Paid Subscribers (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Anthropic, working on the Claude consumer app. Over the last two months, monthly churn among paid Pro subscribers has risen from 5% to 8%, even though new signups keep growing and satisfaction surveys on answer quality are higher than ever. Your Head of Product wants to understand why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the rise in Pro subscriber churn and recommend a response.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is churn measured?" | Share of Pro subscribers active at the start of the month who cancel or don't renew during the month. | On request |
| 2 | "Did anything change two months ago?" | A new, more capable model became the default for Pro users two months ago. | On request -- key fact |
| 3 | "Did pricing or plans change?" | No changes to price or plans. | On request -- rules out pricing |
| 4 | "Is churn rising across all types of users?" | Reveal Exhibit 1 once asked for churn by segment or use case. | On request |
| 5 | "What do cancelling users say?" | Reveal Exhibit 2 once asked about cancellation reasons or feedback. | On request |
| 6 | "Did usage limits change?" | The message limits per time window didn't change, but each message with the new model uses more of the limit, because it reasons longer and writes longer answers. | Reveal only if asked specifically about limits or usage caps |
| 7 | "Are users hitting usage limits more often?" | Reveal Exhibit 3 once asked about limit hits. | On request |
| 8 | "Did competitors launch anything?" | A competitor launched a coding-focused plan around the same time, but no other major changes. | On request |

**Guardrail reminder:** Do not connect the new model, usage limits, and coding-heavy users for the candidate -- let them request the exhibits and find the mechanism.

---

## C. Exhibits / data

**Exhibit 1 — Monthly Churn by Main Use Case (Pro subscribers)**

| Main use case | Share of Pro subscribers | Churn before | Churn now |
|---|---|---|---|
| Coding | 30% | 5% | 13% |
| Writing and analysis | 45% | 5% | 6% |
| Other / mixed | 25% | 5% | 6% |

**Exhibit 2 — Top Cancellation Reasons (last 2 months)**

| Reason | Share |
|---|---|
| "I keep hitting the usage limit" | 46% |
| "Too expensive for what I use" | 18% |
| "Switched to another tool" | 17% |
| Other | 19% |

**Exhibit 3 — Usage Limit Hits**

| Metric | Before new model | Now |
|---|---|---|
| Pro subscribers hitting the limit at least once a week | 9% | 27% |
| Churn among those who hit the limit weekly | 7% | 15% |
| Churn among those who don't | 4.5% | 4.6% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify churn and rule out pricing and quality (quality surveys are up).
2. Look at what changed (new default model) and segment churn by use case.
3. Use cancellation reasons and limit data to find the mechanism.
4. Recommend fixes that balance user experience and cost.

**Correct core insight:** The better model is causing churn indirectly. It uses more of the usage limit per message (longer reasoning and answers), so users -- especially coding users who send many long messages -- hit the limit much more often (9% to 27% weekly). Users who hit the limit churn at 15%; others are unchanged. Coding users' churn jumped from 5% to 13%, and a competitor's coding plan gives them somewhere to go.

**Quantitative reasoning a strong candidate shows:**
- Weighted churn now: 0.30 x 13% + 0.45 x 6% + 0.25 x 6% = 3.9 + 2.7 + 1.5 = 8.1% -- coding explains most of the increase.
- Limit hits: 27% x 15% + 73% x 4.6% = 4.05 + 3.36 = about 7.4% -- consistent with the overall rise.

**A strong final recommendation includes:**
- Short term: show users how much limit they have left, offer a lighter model option when limits are close instead of a hard stop, and let users choose a faster model for simple tasks.
- Medium term: a higher tier for heavy coding users, or limits calibrated to the new model's usage.
- Metrics: weekly limit-hit rate, churn among limit-hitters, churn of coding users; guardrail: compute cost per subscriber.

**Scoring anchors:**
- 5/5 insight generation: connects the new model to limit consumption, isolates coding users, quantifies churn by segment, and recommends limit-aware fixes.
- 3/5: finds that limits are the main complaint but doesn't connect to the new model or segment.
- 1/5: assumes quality or competitors caused it without checking limits.
