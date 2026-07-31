*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 7 — Stripe: Increase in Fraudulent Transactions (PM Diagnostic + Trade-off Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Stripe, on the team responsible for payment fraud prevention. Over the past month, the fraud rate (confirmed fraudulent transactions as a % of total volume) has risen from 0.08% to 0.22% for a specific transaction type: card-not-present transactions from newly onboarded small merchants. Your Head of Risk wants a plan. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the cause of the fraud rate increase for this segment and recommend a response that balances fraud reduction against merchant/customer friction.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is 'fraud rate' measured, and is 0.22% actually a big deal?" | Measured as chargebacks confirmed as fraud (not just disputed) divided by total transaction volume, for this segment. Even though the absolute % looks small, the segment processes billions of dollars a month, so this represents a large and rapidly growing dollar loss. | On request |
| 2 | "Did the fraud model or risk rules change recently?" | No changes to the core ML fraud model in this window. | On request |
| 3 | "Did onboarding/KYC (know-your-customer) process change for new merchants?" | Yes — 2 months ago, Stripe simplified onboarding for small merchants below a certain volume threshold, reducing manual review and document requirements, to speed up time-to-first-transaction. | On request — key fact |
| 4 | "Is the fraud concentrated among specific merchant types or geographies?" | Reveal Exhibit 1 once asked — concentrated in a few merchant category codes (MCCs) and a specific onboarding cohort. | On request |
| 5 | "Are these legitimate merchants whose accounts got compromised, or fraudulent merchants signing up on purpose?" | Reveal Exhibit 2 once asked — this is the key diagnostic split. | On request |
| 6 | "What does the simplified onboarding flow skip, specifically?" | It skips manual review of business registration documents for merchants processing under $10K/month projected volume, relying instead on automated checks (business name/address matching, basic identity verification). | On request |
| 7 | "Has legitimate new-merchant volume/growth changed recently?" | Yes, new merchant signups in this segment are up 25% — the simplified onboarding was explicitly meant to drive this growth. | On request |
| 8 | "What friction would additional review add for legitimate merchants?" | Manual review adds ~2 business days to onboarding and requires document upload; historically this reduces small-merchant signup completion by ~15%. | On request — important trade-off fact |
| 9 | "Can transactions be flagged after the fact, or only prevented at onboarding?" | Both are possible: post-transaction risk scoring/holds exist but currently aren't tuned specifically for this new-merchant cohort. | On request |
| 10 | "Can I see exhibits / fraud breakdown data?" | Hand over Exhibit 1 once framework proposed. | Framework-gated |

**Guardrail reminder:** This case has a real business trade-off (fraud reduction vs. legitimate merchant friction/growth) — don't tell the candidate which side of the trade-off to favor; let them reason to a balanced recommendation using the data.

---

## C. Exhibits / data

**Exhibit 1 — Fraud Rate by Onboarding Cohort and Merchant Type**

| Segment | Fraud rate | Share of segment's new-merchant volume |
|---|---|---|
| Merchants onboarded via simplified flow (last 2 months) | 0.51% | 60% |
| Merchants onboarded via standard/manual review (same period) | 0.06% | 40% |
| Historical baseline (pre-simplified flow, all merchants) | 0.08% | — |

**Exhibit 2 — Nature of Fraudulent Transactions in the Simplified-Flow Cohort**

| Type | % of fraud losses in this cohort |
|---|---|
| Fraudulent merchant accounts set up specifically to process stolen card numbers ("bust-out" pattern: rapid high-value transactions, then account abandoned) | 70% |
| Legitimate merchant accounts later compromised (credential theft, etc.) | 20% |
| Other/unclear | 10% |

**Exhibit 3 (reveal only if asked about detection signals) — Bust-Out Pattern Signals**

Merchants following the fraudulent "bust-out" pattern share common signals: very high transaction velocity in the first 48 hours after onboarding, transaction values clustered near common stolen-card testing amounts, and shipping/delivery info that doesn't match the registered business address. These signals are detectable but the current post-onboarding monitoring isn't specifically tuned to flag this pattern quickly for the simplified-flow cohort.

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Scope and size the problem (is 0.22% actually material given volume; which cohort/segment is driving it).
2. Generate hypotheses: process change (onboarding), model/rules change, external fraud trend, segment growth/mix shift.
3. Distinguish fraud sub-types (compromised legitimate accounts vs. fraudulent accounts by design) since they require different fixes.
4. Weigh the fix against the business trade-off (friction/growth cost) rather than treating "reduce fraud" as a free action.

**Correct core insight:** The fraud increase is concentrated almost entirely in the new simplified-onboarding cohort (0.51% vs. 0.06% for standard review, per Exhibit 1), and within that cohort the dominant pattern (70%, Exhibit 2) is fraudsters deliberately exploiting the lighter-touch onboarding to set up accounts for a "bust-out" scheme — not existing legitimate merchants getting compromised. This means the fix should target the onboarding/detection gap specifically for this pattern, rather than broadly rolling back the simplified flow (which would sacrifice the legitimate 25% signup growth it was designed to create) or assuming it's a generic fraud-model degradation (the model itself didn't change).

**A strong final recommendation includes:**
- Don't fully reverse the simplified onboarding flow (that throws away the legitimate growth gain); instead, add targeted post-onboarding monitoring tuned to the bust-out signals in Exhibit 3 (transaction velocity, amount clustering, address mismatch) specifically for the simplified-flow cohort in its first 48–72 hours.
- Consider a risk-based hybrid: keep fast onboarding for most small merchants, but add a lightweight automated risk score at signup that routes higher-risk-looking applicants (certain MCCs, mismatched signals) into manual review, rather than applying friction to everyone.
- Address the smaller (20%) compromised-account slice separately (e.g., standard account-security measures: MFA, login anomaly detection) since it's a different problem with a different fix.
- Propose measuring both fraud rate and legitimate-merchant signup completion rate together going forward, so the team doesn't optimize one at the expense of the other.

**Scoring anchors:**
- 5/5 insight generation: candidate isolates the simplified-onboarding cohort as the driver, further splits fraud type using Exhibit 2, and proposes a targeted/risk-based fix that explicitly preserves the growth benefit rather than a blanket rollback.
- 3/5: candidate correctly blames the onboarding change but recommends reversing it entirely without weighing the growth trade-off, or doesn't distinguish fraud sub-types.
- 1/5: candidate treats this as a generic "fraud went up, add more rules" problem without isolating the cohort or requesting the onboarding-change fact.
