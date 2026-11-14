*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 34 — Linear: Drop in Weekly Active Teams at Large Workspaces (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Linear. Over the last six weeks, the number of weekly active teams in large workspaces -- companies with more than 500 people on Linear -- has dropped 15%. Smaller workspaces look normal. Your Head of Product wants to know what's going on and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose why weekly active teams dropped in large workspaces and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is a 'weekly active team' defined?" | A team where at least one member created, updated, or commented on an issue in Linear that week. | On request |
| 2 | "Did we ship any product changes in the last six weeks?" | A few small UI changes to the issue view for everyone; nothing specific to large workspaces. | On request |
| 3 | "Are large customers churning or reducing seats?" | No -- seat counts and contracts are unchanged. | On request -- rules out churn |
| 4 | "Is the drop gradual or sudden?" | Sudden: it started in a single week, about six weeks ago, and has stayed at the lower level since. | On request |
| 5 | "Did anything change with integrations?" | Reveal Exhibit 1 once asked about integrations. | On request |
| 6 | "Is the drop concentrated in certain teams or behaviors?" | Reveal Exhibit 2 once asked for a breakdown by segment, team type, or behavior. | On request |
| 7 | "Are people working less, or working elsewhere?" | Customer success heard from two large customers that "people stopped seeing Linear updates where they work," but no detail. | On request |
| 8 | "Did anything change externally around that week?" | Reveal Exhibit 3 once asked about external changes, partners, or third-party platforms. | On request |

**Guardrail reminder:** Do not connect the Slack integration, the platform change, and workspace size for the candidate -- let them request the exhibits and draw the connection themselves.

---

## C. Exhibits / data

**Exhibit 1 — Integration Health (large workspaces)**

| Integration | Error rate before | Error rate last 6 weeks |
|---|---|---|
| Slack (two-way sync of issues and notifications) | 0.5% | 41% |
| GitHub | 0.3% | 0.4% |
| Others | under 1% | under 1% |

**Exhibit 2 — Weekly Active Teams by Slack Integration Use (large workspaces)**

| Segment | Change in weekly active teams |
|---|---|
| Teams that use the Slack integration heavily | -28% |
| Teams that don't use the Slack integration | -1% |

**Exhibit 3 — External Change**

Six weeks ago, the chat platform changed its rate limits for apps posting into workspaces with more than 500 members. Apps that exceed the new limits have their messages rejected.

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the metric and rule out churn or seat loss.
2. Use the timing (sudden, one week) to look for a specific change -- internal or external.
3. Segment by workspace size, team type, and integration use.
4. Find the mechanism and recommend fixes for now and later.

**Correct core insight:** The drop isn't people leaving Linear -- it's the Slack integration breaking for large workspaces. The chat platform's new rate limits for big workspaces made 41% of Linear's Slack messages fail. Many teams in large companies interact with Linear mainly through Slack (notifications, quick replies, creating issues from messages); when those stopped arriving, they stopped touching Linear. Heavy Slack-integration teams dropped 28%, others barely moved.

**A strong final recommendation includes:**
- Immediate fix: batch and throttle Slack messages to stay under the new limits for large workspaces; prioritize the most important notifications.
- Tell affected customers what happened and when it's fixed.
- Monitoring: alerts on integration error rates, since this went unnoticed for weeks.
- Longer term: reduce dependency on one platform (digest notifications, better email and in-app notifications).
- Measure recovery: weekly active teams in large workspaces, Slack error rate.

**Scoring anchors:**
- 5/5 insight generation: uses the sudden timing, finds the Slack error spike, connects it to the external rate-limit change and workspace size, and recommends both a fix and monitoring.
- 3/5: finds the Slack integration issue but doesn't explain why only large workspaces, or recommends only a fix without monitoring.
- 1/5: assumes churn or a UI change caused it without checking integrations.
