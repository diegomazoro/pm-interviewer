*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 19 — Stripe: Billing Roadmap for Next Half (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Stripe Billing, the product businesses use to run subscriptions and invoicing. You own the roadmap for the next half-year, and there are three big candidates competing for your team's capacity: upgrades to usage-based billing, support for new e-invoicing regulations in Europe, and a smarter system for recovering failed subscription payments. You can't fully build all three. Your director wants a recommendation on what to build and why. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend how to allocate next half's Billing capacity across the three initiatives, with explicit reasoning and acknowledged tradeoffs.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the team's goal or strategy for this half?" | Billing's goal for the year is net revenue retention: keep and grow revenue from existing Billing customers. Winning new segments is welcome but secondary this half. | On request -- key framing fact |
| 2 | "How much capacity do we have?" | Two squads for about ten weeks each -- roughly 20 squad-weeks in total. | On request |
| 3 | "How much effort does each option take?" | Usage-based billing upgrades: about 16 squad-weeks for the full scope. EU e-invoicing: about 20 squad-weeks to support every EU country. Failed-payment recovery: about 8 squad-weeks. | On request |
| 4 | "Can any of these be scoped down?" | Yes. Usage-based: a first version with prepaid credits and real-time usage alerts takes about 8 squad-weeks. E-invoicing: supporting only the two countries with mandates already in force takes about 8 squad-weeks; the rest of the EU has no deadline yet. Failed-payment recovery can't be meaningfully split. | On request -- a strong candidate should think to ask |
| 5 | "Is there a deadline on any of these?" | Yes -- the e-invoicing mandate in two EU countries takes effect in about eight months. After that, merchants there legally can't send B2B invoices from a tool that doesn't support the required format. | On request -- crux fact |
| 6 | "Who is asking for each, and how much revenue is behind them?" | Reveal Exhibit 1 once asked about demand, requesters, or revenue. | On request |
| 7 | "What's the expected impact of each?" | Reveal Exhibit 2 once asked about impact, value, or business case. | On request |
| 8 | "Do competitors offer these already?" | Specialized usage-billing startups offer stronger usage-based features and are actively pitching AI companies. Local European invoicing tools already support the new format. Failed-payment recovery is offered by most billing tools in some form, with varying quality. | On request |
| 9 | "Is there churn risk tied to any of these?" | Reveal Exhibit 2 once asked. | On request |

**Guardrail reminder:** Do not tell the candidate which option or combination to choose, whether the regulatory deadline makes e-invoicing mandatory, or how to split capacity -- several allocations are defensible; the point is a consistent framework, quantified tradeoffs, and a clear recommendation.

---

## C. Exhibits / data

**Exhibit 1 — Demand and Revenue Behind Each Option**

| Option | Accounts requesting | Who they are | Share of Billing net revenue from these accounts | Revenue growth of these accounts YoY |
|---|---|---|---|---|
| Usage-based billing upgrades | 1,900 | Mostly AI and developer-tool startups | 7% | +140% |
| EU e-invoicing | 650 | Mid-sized B2B businesses in the two mandate countries | 18% | +12% |
| Failed-payment recovery | 300 | Mixed; few merchants know it's possible | All Billing merchants would benefit | n/a |

Billing net revenue: about $600M a year.

**Exhibit 2 — Estimated Impact**

| Option | Estimate |
|---|---|
| Usage-based billing upgrades | 12% of requesting accounts say they are evaluating a specialized usage-billing tool. Hard to quantify near-term revenue; strategic value is staying the default for the fastest-growing segment. |
| EU e-invoicing (mandate countries) | 30% of affected accounts told their account managers they will switch providers if the format isn't supported by the deadline. |
| Failed-payment recovery | Expected to recover about 0.8% of recurring payment volume that currently fails for good. Recurring volume on Billing: about $90B a year. Stripe earns about 2.9% on recovered payments. |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Anchor on the stated goal (net revenue retention this half) and the capacity constraint (20 squad-weeks) before comparing options.
2. Evaluate options on consistent criteria: revenue protected or gained, strategic fit, urgency/deadlines, effort, and confidence.
3. Ask whether options can be scoped down, rather than treating it as all-or-nothing.
4. Quantify where possible, then recommend an allocation and state what's being given up.

**Quantification a strong candidate does:**
- E-invoicing revenue at risk: 18% x $600M = about $108M from affected accounts; 30% threatened churn = about $32M a year at risk, with a hard deadline.
- Failed-payment recovery: 0.8% x $90B = about $720M of recovered merchant volume; at about 2.9%, roughly $21M a year of new Stripe revenue, plus fewer merchants losing subscribers.
- Usage-based: 7% x $600M = about $42M today, growing 140% -- small now, but the fastest-growing segment, with 12% actively evaluating competitors.

**Correct core insight:** The scoped e-invoicing work (8 squad-weeks) is effectively non-negotiable: it protects the largest amount of revenue (~$32M a year), has a hard legal deadline, and maps directly to the retention goal -- while the remaining EU countries have no deadline and can wait. That leaves 12 squad-weeks for a genuine tradeoff: failed-payment recovery (8 weeks, ~$21M a year, high confidence, fits the retention goal) versus the scoped usage-based first version (8 weeks, strategic protection of the fastest-growing segment, lower near-term confidence). Both can't fit alongside e-invoicing. Either choice can score well if argued from the goal and numbers; recovery fits the stated retention goal more directly, while usage-based is the stronger long-term bet.

**A strong final recommendation includes:**
- Scoped e-invoicing for the two mandate countries first, with a plan to revisit the rest of the EU when new deadlines are announced.
- A clear call on the second slot with reasoning tied to the stated goal and numbers, and an explicit statement of what's being traded off.
- A mitigation for the deprioritized option (e.g. account-manager outreach to at-risk AI startups, or a lightweight usage-alerts feature).
- How the decision will be measured (revenue retained in mandate countries, recovered volume, usage-segment churn).

**Scoring anchors:**
- 5/5 business sense: anchors on the goal, asks about scoping and deadlines, quantifies at least two options, and recommends a capacity allocation with explicit tradeoffs.
- 3/5: picks a reasonable option but treats it as all-or-nothing, skips quantification, or ignores the regulatory deadline.
- 1/5: picks based on request volume or personal preference (e.g. "AI is hot, build usage-based") without connecting to the goal, capacity, or numbers.
