*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 6 — Revolut: Support Ticket Bottleneck (PM Diagnostic + Ops Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Revolut, owning the customer support experience for the core banking app. Over the past 6 weeks, support ticket volume has grown 60%, and average first-response time has gone from 4 hours to over 24 hours. Customers are complaining loudly on social media. Your Head of Product wants a plan by end of week. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose why ticket volume/response time degraded and recommend a prioritized plan (short-term and structural).

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Did the support team's headcount or staffing change?" | No layoffs or reductions; headcount has actually grown slightly (+5%) over this period, but not enough to match the 60% ticket growth. | On request |
| 2 | "What are people contacting support about — top categories?" | Reveal Exhibit 1 (ticket category breakdown) once asked. | On request |
| 3 | "Did any product or feature launch recently?" | Yes — a new "instant card freeze/unfreeze" self-service feature launched 7 weeks ago, plus a new international transfer product launched 6 weeks ago in 3 new countries. | On request — key fact |
| 4 | "Is ticket growth uniform across regions/products, or concentrated?" | Concentrated — the new international transfer countries account for a disproportionate share of new tickets relative to their user base. | Reveal if asked to break down by region/product |
| 5 | "What's the resolution time once an agent picks up a ticket (vs. wait time)?" | Actual handling time per ticket is roughly unchanged (~12 minutes avg); the growth is almost entirely in queue/wait time before an agent starts. | On request — important: this is a volume/capacity problem, not an efficiency-per-ticket problem |
| 6 | "Is there a self-service or FAQ deflection system, and is it working?" | Yes, a chatbot/FAQ deflects an estimated 30% of inbound contacts before reaching a human agent — this rate hasn't changed recently. | On request |
| 7 | "Are the new international transfer tickets a new type of issue, or the same as usual (failed transfer, fees, etc.)?" | Mostly new: confusion about transfer fees/FX rates and delays in the new corridors — categories the support team has little existing documentation or training for. | Reveal if asked about the nature of new-country tickets |
| 8 | "Is this expected to be temporary (launch spike) or ongoing?" | Some launch-spike effect is likely, but the transfer volume in new countries is still growing week over week, not leveling off yet. | On request |
| 9 | "What's the cost/feasibility of hiring more agents quickly, or of a temporary fix?" | Hiring and training a new support agent takes ~3 weeks; contractor/temp agents are available faster (~1 week) but need extra oversight and can't handle complex cases well initially. | On request |
| 10 | "Can I see the ticket volume/category data?" | Hand over Exhibit 1 once a framework is proposed. | Framework-gated |

**Guardrail reminder:** Don't tell the candidate whether the root cause is the card-freeze feature or the international transfer launch — let the region/category breakdown (Exhibit 1) speak for itself once requested.

---

## C. Exhibits / data

**Exhibit 1 — Ticket Volume by Category (6 weeks ago vs. now, indexed to 6-weeks-ago total = 100)**

| Category | 6 Weeks Ago | Now |
|---|---|---|
| Card issues (lost/stolen/freeze confusion) | 25 | 30 |
| International transfers (fees, FX, delays) | 10 | 55 |
| Account access / login | 20 | 22 |
| General billing questions | 30 | 33 |
| Other | 15 | 16 |
| **Total (index)** | **100** | **156** |

**Exhibit 2 — Tickets by Region (new transfer countries vs. rest of business)**

| Region | % of active users | % of new tickets (last 2 weeks) |
|---|---|---|
| 3 new transfer-launch countries | 8% | 41% |
| Rest of business (existing markets) | 92% | 59% |

**Exhibit 3 (reveal only if asked about the card-freeze feature specifically) — Card Freeze Feature Usage**

The instant freeze/unfreeze feature is used correctly by ~90% of users without contacting support; the remaining ~10% contact support mostly because the "unfreeze" button is hard to find in the app, not because the feature fails.

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Scope and quantify the problem (volume, wait time vs. handle time, which segments/categories are driving it).
2. Generate hypotheses: demand-side (new launches, external events), supply-side (staffing/capacity), and process (deflection, routing, training gaps).
3. Use category/region data to isolate the dominant driver(s).
4. Propose a prioritized, phased plan: immediate triage, near-term fix, structural/preventive fix.

**Correct core insight:** This is fundamentally a demand-capacity mismatch driven overwhelmingly by one source: the new international transfer launch. Exhibit 1 shows international transfer tickets grew 5.5x while other categories grew modestly; Exhibit 2 shows the 3 new-launch countries (8% of users) generate 41% of new tickets. Since per-ticket handling time is unchanged (~12 min), the bottleneck is queue capacity, not agent inefficiency — and the transfer-related tickets are compounded by the support team lacking documentation/training for the new corridors' issues (fees/FX confusion), which likely makes those specific tickets slower and more escalation-prone even though the aggregate handle-time average hasn't moved yet. The card-freeze feature (Exhibit 3) is a real but much smaller contributor, mostly a discoverability/UI issue rather than a functional bug.

**A strong final recommendation includes:**
- Immediate: temporarily surge staffing (contractors for simpler ticket types to free up trained agents for transfer-related tickets) and consider a temporary in-app banner/proactive notice about known transfer delays in the new countries to preempt tickets.
- Near-term: build/expand a specific FAQ and macro/response templates for the new-corridor fee and FX questions, and train a subset of agents specifically on this category to reduce handle time and escalations.
- Structural/preventive: treat support-capacity planning as a required part of future market/feature launches (staffing and documentation ready before launch, not after), and fix the freeze/unfreeze button discoverability as a smaller, cheap win.
- Suggest a metric to track recovery: first-response time and category-specific ticket volume trend, checked weekly, not just aggregate volume.

**Scoring anchors:**
- 5/5 insight generation: candidate isolates the international transfer launch as the dominant driver using Exhibit 2's disproportionate share, correctly distinguishes a queue/capacity problem from a handle-time/efficiency problem, and proposes a phased (immediate/near-term/structural) plan.
- 3/5: candidate identifies the transfer launch as a factor but doesn't quantify its disproportionate contribution, or proposes only a generic "hire more agents" fix without addressing training/documentation gaps.
- 1/5: candidate assumes general headcount shortage or the card-freeze feature is the main cause without requesting the category/region breakdown.
