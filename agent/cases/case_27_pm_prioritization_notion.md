*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 27 — Notion: Which Growth Bets to Fund (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Notion's growth team. Next quarter you have engineers for about ten weeks of work, and three projects are on the table: a referral program, improvements to the template gallery, and a redesign of the flow for inviting teammates. Everyone has a favorite. Your manager wants a prioritized plan with the reasoning behind it. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Prioritize the growth projects within ten weeks of capacity, using the funnel and the goal to estimate impact.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the growth team's goal?" | New paid teams per month. Signups alone don't count unless they turn into paying teams. | On request -- key framing fact |
| 2 | "How much effort is each project?" | Referral program: about 6 weeks. Template gallery improvements: about 4 weeks. Invite flow redesign: about 5 weeks. | On request |
| 3 | "What does the funnel look like today?" | Reveal Exhibit 1 once asked for funnel or conversion data. | On request |
| 4 | "What impact do we expect from each?" | Reveal Exhibit 2 once asked about expected impact or estimates. | On request |
| 5 | "How confident are those estimates?" | Referral: based on a test Notion ran two years ago -- fairly confident. Templates: based on a small test last quarter -- fairly confident. Invite flow: based on a benchmark from a similar product, not tested at Notion -- less confident. | On request |
| 6 | "Where do new signups come from?" | About half come from templates and content shared publicly, the rest from word of mouth, search, and invites. | On request |
| 7 | "Why does inviting teammates matter?" | Workspaces with three or more active members are much more likely to become paying teams. | On request |
| 8 | "Can we test before fully building?" | Yes -- any of the three could be tested with a lighter version first, at the cost of about a week. | On request |

**Guardrail reminder:** Do not tell the candidate which project to prioritize or how to combine them -- let them use the funnel to estimate impact and make a call.

---

## C. Exhibits / data

**Exhibit 1 — Monthly Funnel**

| Step | Value |
|---|---|
| New signups per month | 2,000,000 |
| Signups who invite at least one teammate | 9% |
| Of inviters, workspaces that reach 3+ active members | 40% |
| Of 3+ member workspaces, share that become paid teams | 22% |
| Paid conversion of solo users (never invite anyone) | about 0.3% |

**Exhibit 2 — Estimated Impact of Each Project**

| Project | Expected effect |
|---|---|
| Referral program | +3% signups; referred users convert to paid at the average rate for signups (about 1%) |
| Template gallery | +10% signups; but these signups convert to paid at about 0.5% |
| Invite flow redesign | Invite rate from 9% to 12% of signups |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Anchor on the goal: new paid teams, not signups.
2. Map each project to where it acts in the funnel.
3. Estimate each project's impact on paid teams, adjusting for confidence and effort.
4. Fit the best combination into ten weeks and plan how to validate.

**Quantification a strong candidate does:**
- Referral: 2M x 3% = 60,000 extra signups x 1% = about 600 paid teams a month. 6 weeks.
- Templates: 2M x 10% = 200,000 extra signups x 0.5% = about 1,000 paid teams a month. 4 weeks.
- Invite flow: 2M x 3 points = 60,000 extra inviters x 40% x 22% = about 5,300 paid teams a month. 5 weeks.
- Invite flow is roughly 5x the next option, even with a heavy confidence discount.

**Correct core insight:** The project that looks least like "growth" (invite flow) has by far the biggest effect on paid teams, because it acts at the step where conversion jumps -- solo users barely pay, teams with 3+ members convert at 22%. Templates bring the most signups but low-value ones. Within ten weeks, invite flow (5) + templates (4) = 9 weeks fits; referral (6) doesn't fit alongside the invite flow. Because the invite-flow estimate is the least proven, a strong candidate validates it early (a lighter test first) while still prioritizing it.

**A strong final recommendation includes:**
- Invite flow redesign first, with an early test to confirm the uplift.
- Templates second (cheap, still positive), or referral if the candidate argues for its confidence -- with the reasoning.
- Explicitly not doing referral this quarter (or templates), and why.
- Metrics: invite rate, workspaces reaching 3+ members, new paid teams per month.

**Scoring anchors:**
- 5/5 business sense: anchors on paid teams, quantifies all three through the funnel, recognizes the invite flow's leverage, handles confidence, and fits the plan into ten weeks.
- 3/5: prioritizes reasonably but stops at signups, or quantifies only one project.
- 1/5: picks the template gallery or referral because "more signups," without using the funnel.
