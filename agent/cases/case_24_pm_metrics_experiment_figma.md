*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 24 — Figma: Did the New Commenting Experience Work? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Figma. Two months ago your team launched a redesigned commenting experience in the editor. Since launch, comments per weekly active user are up 30%, and the team wants to present it as a big success at the next all-hands. Your director asks you to make sure the story holds up. How would you evaluate whether this launch actually worked?"

**Objective (private reference, reveal only if asked directly):** Determine whether the redesign achieved its goal, and define the right success metric for it.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What was the goal of the redesign?" | To make design feedback faster: shorten the time between someone giving feedback and the design being updated. | On request -- key framing fact |
| 2 | "What changed in the redesign?" | Threads became easier to follow, comments can be resolved in one click, and the team added emoji reactions on comments. | On request |
| 3 | "How is 'comments per weekly active user' calculated?" | Total comment events logged in a week divided by weekly active users. | On request |
| 4 | "Are reactions counted as comments?" | Yes -- reactions are logged as comment events in the same table. | Reveal only if asked specifically about reactions or what counts as a comment event |
| 5 | "Was this an A/B test or a before/after comparison?" | Before/after. It launched to everyone at once; there was no holdout group. | On request |
| 6 | "Did anything else change around the launch?" | The launch happened in early September, when Figma usage seasonally rises as teams return from summer. | On request |
| 7 | "Can I see a breakdown of the comment numbers?" | Reveal Exhibit 1 once asked for a breakdown. | On request |
| 8 | "Is there data on how quickly feedback gets resolved?" | Reveal Exhibit 2 once asked about resolution, feedback speed, or outcome metrics. | On request |
| 9 | "What did last year's September look like?" | Comments per weekly active user rose about 6% from August to October last year with no product change. | On request |

**Guardrail reminder:** Do not point the candidate to the reactions, the seasonality, or the resolution data, and do not say whether the 30% is real -- they should question the metric and ask for the data on their own.

---

## C. Exhibits / data

**Exhibit 1 — Comment Events per Weekly Active User**

| Type | Before launch | After launch |
|---|---|---|
| Written comments and replies | 4.0 | 4.1 |
| Reactions | 0 (feature didn't exist) | 1.1 |
| Total comment events | 4.0 | 5.2 |

**Exhibit 2 — Feedback Speed**

| Metric | Before launch | After launch |
|---|---|---|
| Comment threads resolved within 7 days | 58% | 57% |
| Median time from first comment to a design edit on that frame | 2.4 days | 2.3 days |
| Threads resolved with one click (new feature) | -- | 31% of resolutions |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Start from the goal (faster feedback), not the reported metric.
2. Check the metric definition and what's driving the change.
3. Check causality: before/after without a holdout, plus seasonality.
4. Pick metrics that reflect the goal and judge the launch on those.

**Correct core insight:** The 30% is mostly a counting change. Reactions are logged as comment events: written comments went from 4.0 to 4.1 (+2.5%), while reactions -- which didn't exist before -- add 1.1. And even the small written-comment increase sits inside the ~6% seasonal rise seen last year. The metrics that reflect the goal are flat: 58% to 57% of threads resolved within 7 days, and median time to edit 2.4 to 2.3 days. So there's no evidence the launch made feedback faster -- it may still be a good experience (people use one-click resolve), but "comments up 30%" is not a success story.

**Quantitative reasoning a strong candidate shows:**
- Reactions explain most of the lift: (5.2 - 4.1) / (5.2 - 4.0) = 1.1 / 1.2, about 92%.
- Written comments: 4.0 to 4.1 = +2.5%, below last year's ~6% seasonal rise.

**A strong final recommendation includes:**
- Don't present the 30% at the all-hands; separate reactions from comments in logging.
- Redefine success around the goal: time from feedback to design change, share of threads resolved, possibly designer-reported feedback quality.
- Get causal evidence: a holdout or a staged rollout for future changes; compare against last year's seasonal baseline for now.
- Optionally investigate whether reactions replace written feedback (lower-quality feedback) as a guardrail.

**Scoring anchors:**
- 5/5 insight generation: catches the reactions counting issue, quantifies it, checks seasonality, and redefines success around feedback speed.
- 3/5: questions the metric or asks for outcome data but doesn't connect the pieces into a clear verdict.
- 1/5: accepts the 30% as success, or only proposes "run an A/B test" without examining the data.
