*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 17 — Nubank: Cross-Selling Beyond the Credit Card Without Extending Bad Credit (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Nubank. A large share of customers still only actively use their Nubank credit card and haven't adopted any of Nubank's other products. Leadership wants to grow revenue per customer by getting more of these credit-card-only customers to also adopt personal loans or NuInvest, Nubank's investment product -- but the risk team is wary of extending more credit to customers who are still early or inconsistent in their credit history with Nubank. How would you approach growing cross-product adoption without increasing credit risk?"

**Objective (private reference, reveal only if asked directly):** Design an approach to cross-selling additional products to credit-card-only customers that grows revenue per customer while appropriately managing credit risk, with a clear v1 scope and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How big is the credit-card-only segment, and how long have they been customers?" | It's a large share of the base -- most have held a Nubank account for six months or more, but have never activated or used any product besides the credit card. | On request |
| 2 | "What's the business motivation here?" | As the core credit card business matures, cross-selling additional products is the main lever left to keep growing revenue per customer. | On request |
| 3 | "Which products are we cross-selling -- is one already prioritized?" | Two candidates are on the table: personal loans, and NuInvest (Nubank's investment/savings product). Neither has been prioritized yet -- that's an open decision. | On request |
| 4 | "What specifically worries the risk team?" | Extending personal loans to customers whose repayment history on the credit card is still thin or inconsistent increases expected default risk on those loans. | On request |
| 5 | "Is 'credit-card-only, 6+ months tenure' a uniform group, or does it vary?" | Reveal Exhibit 1 once asked -- it varies a lot by repayment behavior, not just tenure. | On request — key fact |
| 6 | "Has anything like this been tried already?" | Reveal Exhibit 2 once asked for pilot data or evidence. | On request or framework-gated |
| 7 | "What do competitors do here?" | At least one competing neobank has entered new segments cautiously via a secured, deposit-backed credit product rather than unsecured lending, to limit downside while building repayment history. | On request |
| 8 | "Is there a cross-sell option that doesn't carry credit risk at all?" | Yes -- NuInvest is the customer's own money; offering it doesn't expose Nubank to default risk the way a loan does. | On request |

**Guardrail reminder:** Do not tell the candidate to segment by repayment behavior instead of tenure, and do not confirm or rule out any specific product (loans vs. NuInvest) as the right one to lead with -- these are exactly the decisions the candidate should reason through themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "One thing that complicates this: we piloted proactively offering personal loans to all credit-card customers active 6 months or more. Adoption was solid at 24%, but the 90-day default rate among recipients who'd been minimum/partial-balance payers came in at 9.8% -- more than 3x what our existing risk models predicted for that tenure bucket. Recipients who'd always paid their statement in full defaulted at only 2.1%. Meanwhile, offering NuInvest to that same broad population had a 31% signup rate with no credit exposure at all."

---

## C. Exhibits / data

**Exhibit 1 — Credit-Card-Only Customers by Tenure and Repayment Behavior**

| Segment | % of credit-card-only base | Repayment behavior |
|---|---|---|
| Consistent full-balance payers, 6+ months tenure | 45% | Always pays statement in full, on time |
| Minimum/partial payers, 6+ months tenure | 30% | Frequently carries a balance; occasional late payment |
| New customers, under 6 months tenure | 25% | Not enough repayment history yet to classify |

**Exhibit 2 — Cross-Sell Pilot Results (reveal once candidate asks for pilot data or evidence)**

| Metric | Value |
|---|---|
| Loan offer acceptance rate, all credit-card customers active 6+ months | 24% |
| 90-day default rate, loan recipients who were "consistent full-balance payers" | 2.1% |
| 90-day default rate, loan recipients who were "minimum/partial payers" (same 6+ month tenure bucket) | 9.8% (vs. ~3% predicted by existing risk models for this tenure bucket) |
| NuInvest signup rate when offered to the same broad 6+ month population | 31% |
| Credit risk impact from NuInvest signups | None -- investment product, no credit extended |

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** recognizes that "cross-sell to credit-card-only
customers" bundles together two products with fundamentally different risk
profiles (credit vs. non-credit), and that "credit-card-only, 6+ months"
is not one uniform segment -- repayment behavior varies widely within it
(Exhibit 1), even before the twist confirms why that distinction matters.

**Product taste:** goes beyond "offer the loan to anyone who qualifies by
tenure" -- e.g., proposes leading with NuInvest as a low-risk, universal
entry point for cross-sell regardless of segment, while reserving loan
offers for customers whose actual repayment behavior (not just tenure)
signals lower risk. Shows conviction in a specific sequencing rather than
listing both products as equally viable to launch at once.

**Prioritization & tradeoffs:** explicitly scopes a v1 -- e.g., launches
NuInvest cross-sell broadly first (immediate, risk-free revenue-per-customer
lift), while treating loan cross-sell as a second phase gated by a
repayment-behavior-based eligibility model rather than tenure alone, and
states why (Exhibit 1/pilot risk data) instead of trying to solve both
products' rollout at once.

**Business judgment & metrics:** ties the recommendation back to the
revenue-per-customer motivation, and proposes concrete metrics -- e.g.
cross-sell adoption rate and incremental revenue per customer -- plus a
guardrail metric such as 90-day default rate by repayment-behavior segment,
so growth isn't pursued at the cost of a hidden risk spike.

**Composure under the follow-up:** the scripted twist (loan defaults
blew past prediction specifically among minimum/partial payers despite
meeting the tenure bar, while NuInvest adoption was strong and risk-free)
directly challenges a tenure-only eligibility answer. A strong candidate
adapts -- e.g., re-segments loan eligibility by actual repayment behavior
instead of tenure, or leans further into NuInvest-first sequencing --
rather than dismissing the data or abandoning their framework.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the "credit risk vs. cross-sell growth" tension (e.g., risk-free product
  first, behavior-gated credit second) even before the twist is revealed,
  and defends the choice.
- 3/5: candidate proposes a reasonable but generic cross-sell plan and
  adjusts adequately once the twist is revealed.
- 1/5: candidate proposes offering all products to all customers who meet
  a simple tenure bar, with no segmentation or risk consideration, and
  struggles to respond to the twist.
