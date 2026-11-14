*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 43 — Anthropic: API Platform Priorities for Mid-Market Customers (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Anthropic's API platform team, which serves companies building products on Claude. Next quarter you have capacity for two of these three projects: self-serve higher rate limits for growing startups, data residency in the EU, and a usage and cost dashboard with budget alerts. Each has internal champions. Your director wants a recommendation. How would you approach it?"

**Objective (private reference, reveal only if asked directly):** Choose two of three platform projects based on the goal and quantified impact, and explain the tradeoff.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the platform team's goal?" | Grow API revenue from mid-market customers -- companies spending $10K to $500K a year. | On request -- key framing fact |
| 2 | "How much effort does each take?" | All three are roughly half a quarter each, so two fit. | On request |
| 3 | "What's the problem with rate limits today?" | Growing customers must email sales to raise their limits, which takes about 5 business days. | On request |
| 4 | "Who needs EU data residency?" | Reveal Exhibit 1 once asked about demand for each project. | On request |
| 5 | "Is there revenue tied to each?" | Reveal Exhibit 2 once asked about revenue impact. | On request |
| 6 | "Why a cost dashboard?" | Customers say they can't predict monthly bills, and some cap usage to avoid surprises. | On request |
| 7 | "Are any of these blocking deals?" | Yes -- EU residency is a hard requirement in some regulated deals. If asked for numbers, reveal Exhibit 2. | On request |
| 8 | "What do competitors offer?" | Some competitors already offer EU data residency; most offer self-serve limit increases; cost dashboards vary. | On request |

**Guardrail reminder:** Do not tell the candidate which two to pick -- several combinations can be defended with the data.

---

## C. Exhibits / data

**Exhibit 1 — Demand by Project (mid-market)**

| Project | Customers asking | Note |
|---|---|---|
| Self-serve rate limits | 1,400 | Mostly fast-growing startups |
| EU data residency | 120 | Mostly regulated European companies (finance, health); a hard requirement |
| Cost dashboard and budget alerts | 900 | Across all segments |

**Exhibit 2 — Estimated Annual Revenue Impact**

| Project | Estimate |
|---|---|
| Self-serve rate limits | Customers waiting on limit increases lose about 5 days of growth; estimated +$18M a year from faster scaling. |
| EU data residency | 40 deals currently blocked, average $300K a year each, about half expected to close if residency ships. |
| Cost dashboard | Customers who cap usage out of bill fear spend about 15% less than similar customers; estimated +$9M a year. |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Anchor on the goal (mid-market API revenue).
2. Estimate revenue impact and confidence for each.
3. Consider strategic factors: blocked deals, competitive gaps, customer trust.
4. Pick two and state the tradeoff.

**Quantification a strong candidate does:**
- EU residency: 40 x $300K x 50% = about $6M a year now, but these are large, sticky, regulated customers and a competitive gap.
- Rate limits: about $18M a year, broadest reach (1,400 customers), easy to justify.
- Cost dashboard: about $9M a year, plus trust and fewer billing surprises.

**Correct core insight:** On near-term revenue, rate limits ($18M) and the cost dashboard ($9M) win. EU residency is smaller near-term (~$6M) but strategic: it opens a regulated segment competitors already serve, and blocked deals don't come back once they choose a competitor. A strong candidate either picks rate limits + dashboard (maximizing near-term revenue) or rate limits + residency (strategic), explaining why. Rate limits is in nearly every strong answer.

**A strong final recommendation includes:**
- Self-serve rate limits as the clear first pick.
- A justified second pick, with the tradeoff spelled out.
- A plan for the third (e.g. a lightweight interim version, or next quarter).
- Metrics: time to limit increase, mid-market revenue growth, blocked deals closed, customers capping usage.

**Scoring anchors:**
- 5/5 business sense: anchors on the goal, quantifies all three, weighs strategic value against near-term revenue, and explains the choice.
- 3/5: picks a reasonable pair without quantification or without addressing the strategic angle.
- 1/5: picks based on number of requests alone, or without connecting to the goal.
