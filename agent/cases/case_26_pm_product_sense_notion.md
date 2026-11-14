*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 26 — Notion: Keeping Team Workspaces from Getting Messy (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Notion. Teams love how easy it is to create pages, but after a year or two, many team workspaces turn into a mess: outdated docs, duplicate pages, and nobody's sure which version is the right one. People start saying 'I can never find anything in Notion.' How would you design a solution to keep team workspaces healthy over time?"

**Objective (private reference, reveal only if asked directly):** Design an approach that keeps team workspaces trustworthy and findable over time, with a clear target user, MVP, tradeoffs, and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What size of teams are we talking about?" | Mostly companies of 50 to 2,000 people on the Business or Enterprise plan, where many teams share one workspace. | On request |
| 2 | "How do people look for things today?" | Mostly search and the sidebar. Some teams have a "wiki home" page, but it's often out of date. | On request |
| 3 | "How bad is the problem, in numbers?" | Reveal Exhibit 1 once asked for data on workspace health, search, or stale content. | On request |
| 4 | "Who maintains the workspace today?" | Usually nobody officially. In some companies an ops person or team lead does occasional cleanup. | On request |
| 5 | "Why does this matter for Notion's business?" | "Can't find anything" is one of the top reasons cited when larger customers move their docs to another tool at renewal time. | On request -- business context |
| 6 | "What do users say they want?" | Reveal Exhibit 2 once asked about user research or what users want. | On request |
| 7 | "Can pages have owners or expiry dates today?" | Some teams add an "owner" property by hand, but there's no built-in ownership, review date, or verification status for regular pages. | On request |
| 8 | "Are there any constraints?" | Deleting or hiding content is sensitive: people get very upset if something they rely on disappears. | On request |

**Guardrail reminder:** Do not tell the candidate whether to focus on search, ownership, cleanup, or AI, or which user (admins vs. everyday members) to design for -- they need to make that call.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a pilot that automatically archived pages nobody had opened in 90 days, search satisfaction went up, but 12% of the archived pages turned out to be important reference docs that people only open once a year, like the holiday policy or the annual planning template -- and the support tickets from those cases were very angry."

---

## C. Exhibits / data

**Exhibit 1 — Workspace Health in Companies with 2+ Years on Notion**

| Metric | Value |
|---|---|
| Pages not opened in the last 6 months | 64% |
| Searches where the user clicked no result | 38% |
| Searches where the user clicked the 4th result or lower | 22% |
| Topics with two or more pages that look like duplicates | 1 in 3 |

**Exhibit 2 — User Research Themes (interviews with 40 team members and 15 admins)**

- "I don't know if this page is still true." (most common theme)
- "I found three versions of the onboarding doc."
- Admins: "I'd clean it up, but I don't know what's safe to delete."
- "I'd keep my team's pages up to date if someone reminded me."

---

## D. Model answer / "what good looks like"

**Strong problem framing:** reframes the problem from "find" to "trust" -- Exhibit 2's top theme is not knowing whether a page is still true. Picks a specific user: e.g. team leads who own team knowledge, or admins at mid-size companies -- not "everyone."

**Product taste:** strong ideas include page ownership and "verified until" dates with reminders to owners; search that ranks verified and recently-reviewed pages higher and flags likely duplicates; a workspace health view for admins with safe suggestions (merge duplicates, assign owners) rather than auto-deletion; "stale" labels instead of hiding. An ambitious option: AI that detects outdated or conflicting content and asks the owner to confirm.

**Prioritization & tradeoffs:** MVP like page owners + verification status + search boost for verified pages, leaving out automatic archiving and AI cleanup for v1. Discusses the tradeoff between automatic cleanup and the fear of losing content.

**Business judgment & metrics:** ties to retention of larger customers at renewal. Metrics: search success rate (clicked a result in the top 3), share of frequently viewed pages that are verified, admin cleanup actions. Guardrails: restore requests, complaints about missing content.

**Composure under the follow-up:** the twist shows that "not opened recently" is a bad proxy for "not needed." A strong candidate adapts: don't remove content automatically; use signals like ownership and links, label rather than archive, ask owners before anything is hidden, and treat rarely-opened reference docs as a separate category. A weak candidate abandons cleanup entirely or ignores the risk.

**Scoring anchors:**
- 5/5: reframes to trust, specific user, ownership/verification-style MVP, metrics on search success and verified content, thoughtful adaptation to the twist.
- 3/5: solid search or cleanup ideas but generic user, no MVP boundary, or vague metrics.
- 1/5: "better search" or "auto-delete old pages" with no understanding of trust, and no adaptation after the twist.
