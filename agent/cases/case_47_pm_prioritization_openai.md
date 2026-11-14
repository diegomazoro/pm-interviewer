*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 47 — OpenAI: Growing Seats in Business Accounts (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on ChatGPT's business plans, sold to companies by the seat. Next quarter you can build one of three projects: an admin analytics dashboard showing how the company uses ChatGPT, connectors to internal tools like company drives and wikis, or better sharing of projects and conversations between colleagues. Your director wants to know which one to build and why. How would you decide?"

**Objective (private reference, reveal only if asked directly):** Pick the project that best drives the stated goal, using data on what predicts seat expansion.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the goal for business plans this year?" | Grow seats within existing business accounts (seat expansion). | On request -- key framing fact |
| 2 | "How much effort does each take?" | All three are about one quarter for the team. | On request |
| 3 | "What predicts whether an account adds seats?" | Reveal Exhibit 1 once asked about drivers of expansion or account data. | On request |
| 4 | "Who asks for each project?" | Reveal Exhibit 2 once asked about requests, demand, or who wants each. | On request |
| 5 | "Who decides to buy more seats?" | Usually the team lead or department head who sees colleagues getting value, with sign-off from IT or finance. | On request |
| 6 | "Do competitors offer these?" | Most offer some connectors; admin analytics is common; collaboration features vary. | On request |
| 7 | "Is there a risk of churn tied to any of these?" | Admins at large accounts say a lack of usage visibility makes it hard to justify renewal budgets. | On request |

**Guardrail reminder:** Do not tell the candidate which project to pick or which driver matters most -- let them use the data.

---

## C. Exhibits / data

**Exhibit 1 — Seat Growth Over 6 Months by Account Behavior**

| Account behavior | Seat growth |
|---|---|
| Accounts where 30%+ of users have shared a conversation or project with a colleague | +48% |
| Accounts where fewer than 10% have shared | +9% |
| Accounts with an admin who checks usage reports monthly | +16% |
| Accounts without | +13% |
| Accounts that connected at least one internal tool (pilot) | +22% |
| Similar accounts that didn't | +14% |

**Exhibit 2 — Requests (last 2 quarters)**

| Project | Requests | Main requester |
|---|---|---|
| Admin analytics dashboard | 2,100 | IT admins |
| Internal tool connectors | 1,600 | Team leads and end users |
| Better sharing | 700 | End users |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Anchor on the goal: seat expansion.
2. Identify what drives expansion (spread of value between colleagues).
3. Evaluate each project against that driver, plus confidence and risk.
4. Recommend and plan to validate causality.

**Correct core insight:** Requests point to the admin dashboard, but the data on expansion points to sharing: accounts where sharing is common grow seats +48% vs. +9%, because value spreading between colleagues is what makes department heads buy more seats. Admin reporting barely correlates with growth (+16% vs. +13%). Connectors show a moderate lift (+22% vs. +14%) from a pilot. A strong candidate notes the sharing data is correlation (engaged accounts both share more and grow), so plans to validate -- but still sees it as the strongest bet for the goal. The admin dashboard has a renewal angle worth noting.

**A strong final recommendation includes:**
- Build better sharing, explaining the link between sharing and seat growth.
- Validate with a staged rollout and measure seat growth vs. a holdout.
- Note the admin dashboard as a renewal/retention lever for later, possibly a lightweight version.
- Metrics: share of users who share, seat growth per account, invites from shared content.

**Scoring anchors:**
- 5/5 business sense: anchors on seat expansion, uses the behavior data over request counts, recognizes correlation vs. causation, and has a validation plan.
- 3/5: picks sharing or connectors with some data, but doesn't address causality or the request-count trap.
- 1/5: picks the admin dashboard because it has the most requests.
