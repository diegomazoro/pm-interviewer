*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 25 — Figma: Regional Pricing in Emerging Markets (PM Strategy & Growth Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Figma's monetization team. In countries like India, Brazil, and Indonesia, Figma has a huge and fast-growing base of free users, but very few of them pay. Some people internally want to introduce lower regional prices in these markets; others worry it would cannibalize revenue and be abused. Leadership has asked for your recommendation. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend whether and how Figma should introduce regional pricing in emerging markets, weighing revenue, strategic value, and abuse risk.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the goal -- revenue, market share, something else?" | Leadership wants long-term growth in these markets, but doesn't want to lose meaningful revenue doing it. | On request |
| 2 | "How big are these markets for Figma today?" | Reveal Exhibit 1 once asked about size, users, revenue, or conversion. | On request |
| 3 | "What does Figma charge today?" | One global price: about $15 per editor per month for the Professional plan, billed in US dollars. | On request |
| 4 | "Would people pay at a lower price?" | Reveal Exhibit 2 once asked about willingness to pay or price sensitivity. | On request |
| 5 | "Who are the free users in these markets?" | A mix of students, freelancers, and designers at small agencies and startups. Many work for clients in the US and Europe. | On request |
| 6 | "What about abuse -- people outside the region buying the cheaper plan?" | Teams can try to use a local card or VPN. Billing can check card country, billing address, and tax ID, which would catch most -- but not all -- of it. | On request |
| 7 | "Who are the competitors in these markets?" | Free and cheaper local tools, plus template-based design tools with local pricing. Several are growing fast among students and freelancers. | On request |
| 8 | "Has anyone done this before?" | Reveal Exhibit 3 once asked about benchmarks or other companies' experience. | On request |

**Guardrail reminder:** Do not tell the candidate whether to introduce regional pricing, which price to choose, or how to handle abuse -- let them weigh the revenue math against strategy and risk.

---

## C. Exhibits / data

**Exhibit 1 — Emerging Markets Snapshot**

| Metric | Emerging markets | Rest of world |
|---|---|---|
| Monthly active editors | 8.5M | 16.5M |
| Paid conversion (share of active editors on a paid plan) | 1.2% | 6% |
| Share of Figma's total revenue | 6% | 94% |

**Exhibit 2 — Survey of Free Professional Users in Emerging Markets**

| Monthly price | Share who say they would pay |
|---|---|
| $15 (today) | 4% |
| $10 | 19% |
| $6 | 48% |

Note: stated willingness to pay in surveys usually overstates actual conversion by a wide margin.

**Exhibit 3 — Benchmark: Comparable SaaS Tool's Regional Pricing**

| Metric | Value |
|---|---|
| Regional price cut | 60% |
| Paid conversion in those markets | 1.0% -> 3.5% within a year |
| Revenue leakage from customers outside the region using the regional plan | about 1.5% of rest-of-world revenue in the first year, falling after billing checks were tightened |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the goal and today's baseline.
2. Model the revenue impact in-region, using realistic (not survey) conversion.
3. Estimate the downside: leakage from other regions.
4. Add the strategic value: market share, future customers, competition.
5. Recommend a way to test and the guardrails.

**Quantitative reasoning a strong candidate shows:**
- Today in-region: 8.5M x 1.2% = 102,000 paid editors x $15 x 12 = about $18.4M a year.
- With a 60% cut ($6) and benchmark conversion of 3.5%: 8.5M x 3.5% = 297,500 x $6 x 12 = about $21.4M -- roughly +$3M, modest.
- Leakage risk: total revenue is about $18.4M / 6% = about $307M; rest of world about $288M; 1.5% leakage = about $4.3M -- larger than the in-region gain.
- So on year-one revenue alone, regional pricing is roughly break-even or slightly negative unless leakage is controlled.

**Correct core insight:** The case for regional pricing is not short-term revenue -- the math is close to neutral and depends on controlling abuse. The real case is strategic: millions of future designers are forming habits now, cheaper competitors are winning students and freelancers, and today's 1.2% conversion leaves Figma exposed. The deciding factor is whether leakage can be kept well below the in-region gain.

**A strong final recommendation includes:**
- Run a controlled test in one or two markets with strong billing checks (local currency, card country, tax ID).
- Consider a price above $6 (e.g. $8-10) to balance conversion and leakage, or target specific segments (students, local freelancers).
- Success metrics: in-region paid conversion and revenue, leakage rate, competitive share among new designers; guardrail: rest-of-world revenue.
- Don't trust the 48% survey number; plan using benchmark conversion.

**Scoring anchors:**
- 5/5 business sense: models both in-region gain and leakage, recognizes the revenue case is near-neutral, makes the strategic argument, and proposes a controlled test with guardrails.
- 3/5: models in-region revenue but ignores leakage, or uses the survey numbers at face value.
- 1/5: recommends cutting prices because "more people will pay," without numbers or risk analysis.
