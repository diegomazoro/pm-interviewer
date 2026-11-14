*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 37 — Linear: Pricing When AI Agents Do the Work (PM Strategy & Growth Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Linear's strategy team. Linear charges per seat -- per human user. But more and more customers use AI coding agents that pick up issues, write code, and close them, with fewer humans needed for the same amount of work. Leadership worries this could slowly shrink revenue even as Linear becomes more valuable. They want your recommendation on how Linear's business model should adapt. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend how Linear should adapt its pricing and business model as AI agents take on more work, balancing revenue, customer value, and competitive risk.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is Linear priced today?" | A fixed price per human seat per month, with plan tiers. AI agents can be connected for free. | On request |
| 2 | "How much work do agents do today?" | Reveal Exhibit 1 once asked about agent usage. | On request |
| 3 | "Is seat growth actually slowing?" | Reveal Exhibit 2 once asked about seat growth or revenue impact. | On request |
| 4 | "What do customers think about paying for agents?" | Reveal Exhibit 3 once asked about customer attitudes or research. | On request |
| 5 | "What are competitors doing?" | Some competitors still price per seat; one recently added charges per agent action, which got a lot of negative feedback from customers. | On request |
| 6 | "Does Linear have costs that scale with agent use?" | Somewhat -- agent activity creates many more API calls, notifications, and storage, but costs are still small relative to revenue. | On request |
| 7 | "What's the goal?" | Keep revenue growing with the value customers get, without slowing adoption of agents on Linear. | On request |

**Guardrail reminder:** Do not tell the candidate which pricing model to choose (per seat, per agent, usage-based, platform fee, or hybrid) -- let them reason from the data and customer attitudes.

---

## C. Exhibits / data

**Exhibit 1 — Agent Usage**

| Metric | Value |
|---|---|
| Workspaces with at least one AI agent connected | 22% |
| In those workspaces, share of issues closed by an agent | 18% (and rising about 3 points per quarter) |
| Workspaces where agents close more than 40% of issues | 3% |

**Exhibit 2 — Seat Growth and Output (last 12 months)**

| Segment | Seat growth | Issues closed growth |
|---|---|---|
| Workspaces with heavy agent use | +4% | +35% |
| Workspaces with no agent use | +18% | +16% |

**Exhibit 3 — Customer Interviews (40 engineering leaders)**

- "I'd pay more if Linear clearly makes agents more productive -- but not per action, I can't budget that."
- "Predictable pricing is non-negotiable for our finance team."
- "Linear is where we manage both humans and agents now -- it's more valuable than before."

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Quantify the risk: is seat-based revenue diverging from the value delivered?
2. Understand what customers value and what they'll accept (predictability).
3. Compare pricing options: per seat (status quo), per agent, per action/usage, platform/tier, hybrid.
4. Recommend, with a transition plan and metrics.

**Correct core insight:** The risk is real but early. Heavy-agent workspaces close 35% more issues while adding only 4% more seats -- value is rising while revenue per unit of work falls. Agent share is growing ~3 points a quarter, so waiting is risky. But customers want predictability and reject per-action pricing (a competitor got backlash). The best direction is a predictable hybrid: keep seats, and add agent capacity as a tier feature or a fixed per-agent fee, priced on the value of managing agents in Linear -- not metered per action.

**Quantitative reasoning a strong candidate shows:**
- Revenue per closed issue in heavy-agent workspaces: seats +4% vs. output +35% -> revenue per issue closed falls about 23% (1.04 / 1.35).
- Trend: 18% of issues by agents, +3 points a quarter -> about 30% within a year in those workspaces.

**A strong final recommendation includes:**
- Introduce predictable agent pricing (e.g. a number of agents included per plan, extra agents at a flat monthly price) rather than per-action usage.
- Build agent-specific value worth paying for (agent assignment, review queues, agent performance insights).
- Roll out first to new customers or as an optional plan, grandfather existing customers for a period.
- Metrics: revenue per workspace vs. issues closed, agent adoption rate (shouldn't drop), churn on the new pricing.

**Scoring anchors:**
- 5/5 business sense: quantifies the divergence, uses customer attitudes to reject per-action pricing, proposes a predictable hybrid with agent-specific value and a transition plan.
- 3/5: recognizes the risk and proposes a pricing change, but ignores predictability or the competitor backlash.
- 1/5: recommends charging per agent action immediately, or ignoring the issue because revenue is still growing.
