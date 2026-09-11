*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 15 — Jeeves: Making the Corporate Card Customers' Primary Card (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Jeeves, a corporate card and spend-management platform for startups and SMBs across Latin America, the US, and Europe. Companies sign up, get approved, and issue Jeeves cards to their employees -- but for a meaningful share of them, Jeeves ends up as a secondary card that gets used for a few months and then fades, rather than becoming the company's primary corporate card. Your Head of Product wants to improve retention by making Jeeves the card that new customers actually keep using. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Design an approach to increasing sustained (not just initial) primary-card usage among newly onboarded companies, with a clear v1 scope and concrete success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who's the user here -- who decides to keep using Jeeves?" | Two roles: the finance/founder admin who set up the account and controls card issuance, and the individual employees who actually swipe the card day to day. Both matter -- an admin can keep the account open while employee usage quietly fades. | On request |
| 2 | "What's the business motivation for this?" | Revenue scales with card spend volume (interchange), so a company that stops using Jeeves as its primary card is a real revenue and renewal risk even if they never formally cancel -- and it's cheaper to keep an already-onboarded customer active than to acquire a new one. | On request |
| 3 | "How is 'primary card' actually measured?" | Estimated from spend velocity and category mix, not a survey -- a company is considered "primary" if a large majority of their inferred card-eligible spend is running through Jeeves rather than another card. | On request |
| 4 | "Is onboarding itself the problem -- slow approval, hard card issuance?" | No -- onboarding and card issuance are fast (median approval within a day); the drop-off happens weeks to months AFTER cards are issued and initially used, not during signup. | On request |
| 5 | "What's already been tried?" | A 1% cashback pilot aimed at encouraging more usage. Reveal Exhibit 1 once asked for results or evidence. | On request or framework-gated |
| 6 | "What do competitors do here?" | Reveal Exhibit 2 (competitive landscape note) if asked. | On request |
| 7 | "Does usage differ by company size or industry?" | Only a weak relationship -- company size and industry don't cleanly separate companies that stay active from those that fade. | On request |
| 8 | "Is there any factor that does clearly separate retained companies from ones that fade?" | Yes -- reveal Exhibit 1's integration-connection data once asked for evidence or a pattern in who stays active. | On request or framework-gated |

**Guardrail reminder:** Do not tell the candidate which specific retention lever (accounting integrations, cashback/rewards, onboarding changes, card-issuance policy, etc.) is "the" right one, and do not confirm whether any specific idea they propose is correct -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "One thing that complicates this: we already ran a 1% cashback pilot to encourage more usage. It increased transaction volume by 22% in the first 30 days, but barely moved 90-day primary-card retention -- 40% versus 38% in the control group, not a meaningful difference. Meanwhile, companies that connected an accounting integration were far more likely to still be using Jeeves as their primary card at 90 days than companies that hadn't."

---

## C. Exhibits / data

**Exhibit 1 — Cashback Pilot & Usage Pattern Data (reveal once candidate asks for evidence or results)**

| Metric | Value |
|---|---|
| Card transaction volume in the 30 days after joining the 1% cashback pilot | +22% |
| Companies still using Jeeves as their primary card at 90 days, pilot group | 40% |
| Companies still using Jeeves as their primary card at 90 days, control group | 38% |
| Companies still using Jeeves as their primary card at 90 days, had connected an accounting integration | 61% |
| Companies still using Jeeves as their primary card at 90 days, had NOT connected an accounting integration | 29% |
| Companies that connect an accounting integration at all within their first 90 days | 24% |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

At least two competing corporate-card platforms build 1-click sync into major accounting software (QuickBooks, Xero, Contabilizei) into the onboarding flow itself, rather than leaving it as an optional setup step for later, and describe this integration as core to why finance teams keep the card as their system of record.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** separates the admin (who controls whether the
account stays open) from the employees (whose day-to-day swiping is what
actually drives "primary card" status), and narrows to a specific moment
in the lifecycle -- the weeks after initial card issuance, before habits
form -- rather than treating "improve retention" as one undifferentiated
problem.

**Product taste:** goes beyond "remind people to use their card" or "add
more rewards" -- e.g., proposes making accounting-integration setup part
of the onboarding flow itself (surfaced exhibit 1's own strongest signal
even before the twist), or proposes surfacing spend/categorization value
back to the admin early so they have a reason to actively route more
spend through Jeeves. Shows conviction in one direction rather than
listing several ideas with no pick.

**Prioritization & tradeoffs:** explicitly scopes a v1 -- e.g., prioritizes
a narrow set of the most common accounting platforms for a guided,
in-onboarding connection flow, deferring long-tail integrations or a
broader loyalty/rewards overhaul to a later phase, and states why (highest
correlation with retention, per exhibit 1) rather than trying to fix
every lever at once.

**Business judgment & metrics:** ties the direction back to the
interchange-revenue motivation stated up front, and proposes concrete
success metrics -- e.g., % of new companies connecting an integration
within their first 30 days, and 90-day primary-card retention itself --
plus a guardrail metric (e.g., support-ticket volume from a more
demanding onboarding flow) rather than a vague goal like "make the
product stickier."

**Composure under the follow-up:** the scripted twist (cashback barely
moved retention despite lifting short-term volume, while integration
connection strongly correlates with staying active) directly challenges
an incentive-only answer. A strong candidate adapts -- e.g., pivots from
"add more rewards" toward workflow integration as the real lever, or
explains how the two could combine -- rather than dismissing the data or
abandoning their framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the "incentives vs. workflow stickiness" tension (e.g., leads with
  integration-driven stickiness rather than rewards) even before the
  twist is revealed, and defends the choice.
- 3/5: candidate proposes a reasonable but generic engagement/rewards idea
  and adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("send reminders to use the
  card") with no segmentation, no metrics, and struggles to respond to
  the twist.
