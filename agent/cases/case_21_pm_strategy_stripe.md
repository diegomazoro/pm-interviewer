*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 21 — Stripe: Expanding into In-Person Payments for Small Businesses (PM Strategy & Growth Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Stripe's growth strategy team. Stripe is strongest in online payments, while in-person payments for small businesses in the US -- shops, restaurants, salons paying through card terminals -- are dominated by a few established players. Leadership is debating whether Stripe should push hard into in-person payments for small businesses, and if so, how. They've asked you for a recommendation. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend whether and how Stripe should pursue in-person payments for US small businesses, grounded in where Stripe has a right to win and the economics of each path.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's Stripe's goal here -- revenue growth, defending existing customers, something else?" | Leadership cares about both: new revenue growth, and not losing existing online merchants who also sell in person. They haven't said which matters more -- that's part of the recommendation. | On request |
| 2 | "Does Stripe already have any in-person product?" | Yes -- Stripe offers card terminals and an in-person API, today used mainly by software platforms and larger businesses that build their own checkout. There's no ready-made point-of-sale app for a small shop or restaurant. | On request -- important context |
| 3 | "How big is the market?" | US small-business in-person card volume is roughly $1.5 trillion a year. | On request |
| 4 | "Who are the main competitors and how strong are they?" | Reveal Exhibit 1 once asked about the competitive landscape. | On request |
| 5 | "Do Stripe's existing merchants also sell in person?" | Reveal Exhibit 2 once asked about the existing customer base, overlap, or omnichannel merchants. | On request -- key diagnostic fact |
| 6 | "What does it cost to win a customer in each path?" | Reveal Exhibit 3 once asked about acquisition cost, unit economics, or profitability. | On request |
| 7 | "How much does Stripe earn on in-person volume?" | After card network and bank fees, Stripe keeps about 0.5% of in-person payment volume as net revenue. | On request |
| 8 | "Why do small businesses choose their in-person provider?" | Restaurants and retailers mostly choose based on the point-of-sale software (menus, inventory, staff management, tables), with payments bundled in -- not on payments alone. | On request |
| 9 | "Are we losing existing merchants because we lack this?" | Reveal Exhibit 2 once asked. | On request |

**Guardrail reminder:** Do not tell the candidate which segment to target, whether to build a full point-of-sale product, or whether to enter at all -- several strategies are defensible; let them find the right-to-win argument and the economics from the data.

---

## C. Exhibits / data

**Exhibit 1 — US Small-Business In-Person Payments: Competitive Landscape**

| Player type | Approx. share of volume | Strength |
|---|---|---|
| Two leading all-in-one POS + payments providers | 45% | Full point-of-sale software for restaurants and retail, hardware, strong brand with small businesses |
| Traditional bank-owned processors | 35% | Existing bank relationships, but weak software |
| Vertical software platforms (salon, fitness, etc.) | 15% | Industry-specific software; many already use Stripe's in-person API |
| Others | 5% | -- |

**Exhibit 2 — Stripe's Existing US Small-Business Merchants**

| Metric | Value |
|---|---|
| Stripe US small-business merchants with a physical location | 140,000 |
| Their in-person volume, currently processed by another provider | $42B a year |
| Annual churn of these merchants (online + physical) | 6% |
| Annual churn of online-only small merchants | 2% |
| Most cited churn reason for merchants with a physical location | "Wanted one provider for online and in-store" |

**Exhibit 3 — Acquisition Economics by Path**

| Path | Customer acquisition cost (incl. hardware subsidy) | Avg. in-person volume per merchant per year | Payback period |
|---|---|---|---|
| Win new restaurants/shops from competitors | ~$1,800 | ~$150K | ~29 months |
| Cross-sell in-person to existing Stripe merchants | ~$300 | ~$150K | ~5 months |
| Grow through vertical software platforms using Stripe | Paid mostly by the platform | varies | n/a |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the objective (new revenue vs. defending the base) and what Stripe has today.
2. Size the opportunity, but distinguish the whole market from the part Stripe can realistically win.
3. Assess right to win: competitors' strengths vs. Stripe's assets (merchant base, developer platform, online + in-person data).
4. Compare paths on economics (acquisition cost, payback) and risk.
5. Recommend a path, a sequence, and how to measure success.

**Correct core insight:** Attacking the whole $1.5T market head-on against all-in-one POS providers is a weak play: small businesses choose on POS software, not payments, and winning them cold costs ~$1,800 with a ~30-month payback. Stripe's right to win is its own base: 140,000 existing merchants already sell in person, with $42B of in-person volume going to competitors, and they churn at 3x the rate of online-only merchants -- mostly because they want one provider. Cross-selling to them costs ~$300 with a ~5-month payback. The second lever is vertical software platforms, which already use Stripe's in-person API and own the software merchants actually choose on.

**Quantitative reasoning a strong candidate shows:**
- Revenue from cross-sell: e.g. capturing 25% of $42B = $10.5B volume x 0.5% = ~$52M a year in net revenue.
- Retention value: reducing churn of these merchants from 6% toward 2% protects their online revenue too.
- Unit economics: ~$150K volume x 0.5% = ~$750 net revenue per merchant per year, so $1,800 takes ~29 months to pay back while $300 takes ~5 months -- the cross-sell path is about 6x cheaper per merchant.

**A strong final recommendation includes:**
- Don't build a full restaurant/retail POS to compete head-on now.
- Go after omnichannel: a simple, ready-made in-person offering (terminal + unified online/in-store reporting and payouts) for existing Stripe merchants with physical locations, sold through existing relationships.
- Double down on vertical software platforms as the distribution channel for in-person payments.
- Success metrics: share of existing omnichannel merchants' in-person volume moved to Stripe, churn rate of merchants with a physical location, payback per acquired merchant.
- Risks: hardware and support operations are new muscles for Stripe; competitors may bundle online payments to defend.

**Scoring anchors:**
- 5/5 business sense: finds the right-to-win in the existing base, uses churn and acquisition-cost data to justify it, quantifies the opportunity, and recommends a sequenced strategy rather than "enter or don't."
- 3/5: recommends a reasonable direction but argues from market size alone, or misses the churn data and the defensive value.
- 1/5: recommends going head-on against established POS players because the market is big, without considering why merchants choose providers or the economics.
