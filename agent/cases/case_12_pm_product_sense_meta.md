*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 12 — Meta: Peer Favor-Sharing Inside Facebook Groups (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Meta, working on Facebook Groups. Members of local community groups -- neighborhood groups, parent groups, hobby groups -- already post informal asks and offers in the feed: someone needs a ladder for an afternoon, someone else is driving to the airport and can take a neighbor along, someone can watch a pet for a weekend. Right now this all happens as regular posts and comments, which get buried and are easy to miss. How would you design a way to help members of these groups exchange small favors and skills with each other?"

**Objective (private reference, reveal only if asked directly):** Design a structured mechanism for peer favor/skill exchange inside existing Groups, with a clear starting segment, a scoped mechanism, trust/follow-through considerations, and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Which type of group should we start with -- neighborhood, parent, hobby?" | Not decided -- that's part of what the candidate should reason through. Neighborhood groups have the most local, in-person favor exchange today; parent groups have high trust and frequent small asks (childcare swaps, hand-me-downs). | On request |
| 2 | "What's the business motivation here?" | This is primarily about deepening engagement and time-in-Groups, and strengthening Groups as a place for real-world local utility, not an immediate monetization play. | On request -- important scoping context |
| 3 | "What exists today?" | Members already post asks/offers as regular feed posts and comments; there's no dedicated post type, no way to see "open" vs. "resolved" requests, and nothing that resurfaces a matched request to both people. | On request |
| 4 | "Is there any payment or monetary exchange involved?" | Not in scope for v1 -- this is about informal, typically unpaid favor exchange, not a paid marketplace. | On request |
| 5 | "What are the trust and safety considerations?" | Group members are often real-world acquaintances or neighbors, which lowers (but doesn't eliminate) stranger-danger concerns; there's currently no reputation or follow-through signal specific to favor exchanges. | On request |
| 6 | "Do similar features exist elsewhere?" | Reveal Exhibit 2 (competitive note) if asked. | On request |
| 7 | "Is there any data on how asks/offers perform today?" | Reveal Exhibit 1 (pilot data) once the candidate asks for evidence, or once they propose an initial direction. | On request or framework-gated |
| 8 | "Who moderates this -- the group admins, or Meta?" | Existing group admins/moderators would still be responsible for the group generally; open question whether a favor-exchange feature needs its own moderation signal. | On request |

**Guardrail reminder:** Do not tell the candidate which group type, post format, or matching mechanism to pick, and do not confirm whether a dedicated "Ask/Offer" post type or any other specific idea is "the" right direction -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a small pilot, structured Ask/Offer posts got 3x more responses than a regular feed post asking for the same thing, but only about 20% of matches actually resulted in the favor happening, and group moderators reported an increase in reports about people not following through or feeling stood up."

---

## C. Exhibits / data

**Exhibit 1 — Pilot Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| Avg. responses per structured Ask/Offer post | 3x a regular feed post asking for the same thing |
| % of matched Ask/Offer pairs where the favor was confirmed to have actually happened | 20% |
| % increase in moderator reports mentioning "no-show" or "flaked" since the pilot began | 35% |
| % of posts that were resolved but left visibly "open" in the feed afterward | 58% |
| Avg. time between a match being made and the favor's scheduled time | 4 days |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

Other local-community apps have added similar favor/lending features, generally pairing the request itself with some lightweight commitment step (like a scheduled time or a mutual confirmation) rather than leaving it as an open-ended match with no follow-up.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** picks a specific starting segment rather than
"all Groups" -- e.g., neighborhood groups, where favors are inherently
local and time-sensitive, or parent groups, where trust is already high
and asks are frequent and low-stakes. Explicitly separates "getting a
match" from "the favor actually happening," since the prompt's core
complaint is visibility/burial, not lack of willing helpers.

**Product taste:** goes beyond "add a dedicated post type" -- e.g.,
proposes a lightweight commitment step once two people match (a
suggested time, a simple confirm-both-ways step) so a match isn't
considered "done" until it's actually scheduled, or a way to close out
and mark a post resolved so it stops cluttering the feed. Shows
conviction in a specific direction rather than listing options with no
pick.

**Prioritization & tradeoffs:** explicitly scopes v1 -- e.g., launch with
a single group type and a simple ask/offer format with manual
resolution, deferring reputation systems, payments, or cross-group
matching to later phases.

**Business judgment & metrics:** ties the recommendation to the stated
motivation (engagement, time-in-Groups, real-world utility) and proposes
concrete metrics -- e.g., rate of matches that convert to a confirmed
completed favor, not just response rate or match rate, plus a guardrail
metric like no-show/flake reports -- rather than a vague goal like "make
it easier to ask for help."

**Composure under the follow-up:** the scripted twist (high response
rate but low actual follow-through, and rising no-show complaints)
directly challenges a naive "just make asking easier and matches will
happen" answer. A strong candidate adapts -- e.g., adds a lightweight
mutual-confirmation or scheduling step before declaring a match
successful, or redesigns success metrics to track completed favors
rather than raw responses -- rather than dismissing the data or
abandoning their framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the follow-through tension (e.g., a mutual confirm/schedule step) even
  before the twist is revealed, and defends the choice.
- 3/5: candidate proposes a reasonable but generic matching feature and
  adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("let people post asks")
  with no segmentation, no metrics, and struggles to respond to the twist.
