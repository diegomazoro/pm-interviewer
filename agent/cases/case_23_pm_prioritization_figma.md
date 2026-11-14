*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 23 — Figma: Choosing the Next Quarter's Editor Bet (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Figma's core editor team. Next quarter your team has capacity for roughly one major project, and three candidates keep coming up: full offline editing, performance improvements for very large files, and better branching and merging for design-system teams. Each has loud supporters inside the company. Your VP wants a recommendation she can defend to the exec team. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend which editor initiative to fund next quarter, with explicit criteria, quantified impact, and a view on confidence and risk.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the company's priority this year?" | Grow and retain revenue from Enterprise customers. Enterprise renewals and seat expansion are the top company goal. | On request -- key framing fact |
| 2 | "How much capacity do we have?" | One team for one quarter -- about 12 weeks. | On request |
| 3 | "How much effort does each take?" | Offline editing: about 24 weeks. Large-file performance: engineering estimates 8 to 14 weeks, because the root cause isn't fully understood yet. Branching improvements: about 8 weeks. | On request |
| 4 | "Can any of them be scoped down?" | Offline could ship as read-only offline (view and comment, no editing) in about 8 weeks. Performance could start with a 2-week investigation to narrow the estimate. Branching can't be meaningfully split. | On request |
| 5 | "Who wants each, and how much revenue is behind them?" | Reveal Exhibit 1 once asked about demand, requesters, or revenue. | On request |
| 6 | "Is any of this tied to churn or renewals?" | Reveal Exhibit 2 once asked about churn, renewals, or revenue at risk. | On request |
| 7 | "What do competitors offer?" | Some competitors offer offline editing, but it's rarely cited as the reason a company switched. Performance on big files is a frequent complaint in competitive deals. | On request |
| 8 | "How confident are we in each estimate?" | High confidence on branching and on read-only offline; low confidence on performance until the investigation is done. | On request |

**Guardrail reminder:** Do not tell the candidate which option to pick, whether to do the investigation first, or how to weigh confidence -- let them build the framework and reason from the goal and data.

---

## C. Exhibits / data

**Exhibit 1 — Demand Behind Each Option**

| Option | Requests (last 2 quarters) | Who's asking | Share from Enterprise accounts |
|---|---|---|---|
| Offline editing | 9,400 | Mostly individual and Professional-plan users | 8% |
| Large-file performance | 1,100 | Design-system and product teams at large companies | 72% |
| Branching improvements | 640 | Design-system teams | 65% |

**Exhibit 2 — Enterprise Renewal Risk (next two quarters)**

| Metric | Value |
|---|---|
| Enterprise accounts flagged "at risk" by account managers | 20 |
| At-risk accounts citing large-file performance as a main reason | 14 |
| Average annual contract value of those 14 accounts | $1.2M |
| At-risk accounts citing branching | 3 |
| At-risk accounts citing offline | 0 |
| Estimated seat expansion if branching ships (design-system teams adding contributors) | about $4M in new annual revenue |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Anchor on the goal (Enterprise retention and expansion) and the constraint (12 weeks).
2. Evaluate each option on consistent criteria: revenue impact on the goal, reach within Enterprise, effort, and confidence.
3. Probe scoping options and uncertainty rather than treating estimates as fixed.
4. Recommend, with a plan that handles the uncertainty and names what's traded off.

**Quantification a strong candidate does:**
- Performance: 14 at-risk accounts x $1.2M = about $16.8M of annual revenue at risk.
- Branching: about $4M of expansion, plus a smaller share of renewal risk (3 accounts).
- Offline: largest raw request count (9,400) but only 8% Enterprise and zero at-risk accounts -- weak fit with this year's goal, and 24 weeks doesn't fit the quarter.

**Correct core insight:** Raw request volume points to offline, but the goal points to performance: it protects about four times more revenue than branching adds. The catch is confidence -- the 8-14 week estimate could overrun the quarter. A strong candidate handles that explicitly: start with the 2-week investigation, then commit to performance if the estimate firms up within the remaining ~10 weeks, with branching (8 weeks, high confidence) as the fallback if it doesn't.

**A strong final recommendation includes:**
- Performance as the priority, sequenced as a 2-week investigation first with a clear decision point.
- Branching as the defined fallback, and as next quarter's candidate.
- Offline deprioritized with a reason (wrong segment for this year's goal); read-only offline noted as a cheap future option.
- Success metrics: at-risk account renewals, load and editing latency on large files, Enterprise satisfaction.

**Scoring anchors:**
- 5/5 business sense: anchors on the goal, quantifies revenue at risk, handles the confidence problem with a sequenced plan, and states tradeoffs.
- 3/5: picks performance or branching with reasonable logic but ignores the estimate uncertainty or doesn't quantify.
- 1/5: picks offline because it has the most requests, or picks without connecting to the goal.
