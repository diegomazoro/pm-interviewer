*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 11 — Google: Improving Indoor Navigation in Large Venues (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Google, working on Maps. Users navigate Maps confidently outdoors, but once they step inside a large venue -- an airport, a big-box mall, a stadium -- GPS gets unreliable and Maps mostly stops being useful. People end up wandering, asking staff, or falling back on paper signage. How would you approach improving the experience for indoor navigation in these large venues?"

**Objective (private reference, reveal only if asked directly):** Design an approach to indoor wayfinding for large venues, with a clear starting venue type/segment, an MVP mechanism given today's technical constraints, and metrics that tie back to the business.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Which venue type should we focus on -- airports, malls, stadiums?" | Not decided -- that's part of what the candidate should reason through. Airports have the most acute pain (time pressure, unfamiliar layouts) but malls and stadiums have higher visit frequency. | On request |
| 2 | "What's the business motivation for investing here?" | It's seen as a way to deepen Maps' role as the default navigation surface everywhere, and venues have shown interest in paid placement/directory listings if Maps can reliably drive foot traffic to them. | On request -- important scoping context |
| 3 | "What exists today for indoor navigation?" | Some large venues already have a basic static floor plan viewable in Maps, but there's no real-time blue-dot positioning or turn-by-turn indoors for most locations. | On request |
| 4 | "What's the technical constraint here?" | GPS doesn't penetrate most large indoor structures reliably; precise indoor positioning generally requires the venue to install Bluetooth beacons or Wi-Fi positioning infrastructure and share floor-plan data, which is a partnership and rollout effort per venue, not something Maps can do unilaterally. | On request |
| 5 | "Do users need to grant anything for this to work?" | Yes -- accurate indoor position typically requires precise location permissions and, in some designs, Bluetooth scanning, which not all users enable. | On request |
| 6 | "What do competitors or venue-specific apps offer?" | Reveal Exhibit 2 (competitive note) if asked. | On request |
| 7 | "Is there any usage data on how people search for indoor help today?" | Reveal Exhibit 1 (search/usage data) once the candidate asks for evidence, or once they propose an initial direction. | On request or framework-gated |
| 8 | "Would this require charging venues or advertisers?" | Not decided -- open question for the candidate to weigh as part of business judgment. | On request |

**Guardrail reminder:** Do not tell the candidate which venue type, positioning technology, or feature mechanism to pick, and do not confirm whether full turn-by-turn indoor navigation or any other specific approach is "the" right direction -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a pilot at two airports with full indoor turn-by-turn navigation, users who enabled it reached their gate 4 minutes faster on average, but only 12% of users opted into the precise-location permission required to use it, and among those who declined, satisfaction with the existing simple floor-plan view actually dropped compared to before the feature existed."

---

## C. Exhibits / data

**Exhibit 1 — Search & Usage Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| % of Maps searches inside large venues that are for a specific gate, store, or section | 71% |
| % of those searches where the user re-searches or backtracks within 2 minutes (sign of being lost) | 33% |
| Avg. self-reported time spent finding a specific point inside a large unfamiliar venue | 9 minutes |
| % of users who said they'd asked a staff member or another person for directions indoors in the last month | 44% |
| % opt-in rate for precise-location permission in the indoor navigation pilot | 12% |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

Several airports and malls offer their own standalone wayfinding apps with dedicated indoor maps, but adoption is low because travelers and shoppers rarely think to download a venue-specific app in the moment they need directions.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** picks a specific starting venue type rather
than "all large venues" -- e.g., airports first, since exhibit 1 shows
high re-search/backtrack rates and question 2 confirms acute time
pressure and partnership interest there. Explicitly separates the
"finding a specific point" use case (71% of searches) from full
point-to-point indoor turn-by-turn.

**Product taste:** goes beyond "just add indoor GPS" -- e.g., proposes
starting with a lightweight static-plus-contextual layer (showing the
user's general zone/nearest landmark rather than a precise blue dot),
or a fallback experience that degrades gracefully when permissions
aren't granted, rather than assuming full precise positioning is a
prerequisite. Shows conviction in a specific direction rather than
listing options with no pick.

**Prioritization & tradeoffs:** explicitly scopes an MVP -- e.g., launch
with a handful of high-traffic partner airports and a coarse "which
concourse/section are you in" experience before investing in full
beacon-based precise positioning everywhere, explicitly deferring
malls and stadiums.

**Business judgment & metrics:** ties the recommendation to the stated
motivation (deepening Maps as default navigation surface, venue
partnership revenue) and proposes concrete metrics -- e.g., reduction in
re-search/backtrack rate, time-to-destination indoors, and permission
opt-in rate -- rather than a vague goal like "make indoors work like
outdoors."

**Composure under the follow-up:** the scripted twist (low permission
opt-in undermines the full precise-navigation approach, and the fallback
experience actually got worse) directly challenges a naive "just build
full indoor turn-by-turn" answer. A strong candidate adapts -- e.g.,
designs a permission-light fallback tier, invests in improving the
no-permission floor-plan experience rather than only the premium path,
or rethinks the value proposition shown to users before asking for
permission -- rather than dismissing the data or abandoning their
framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the low-opt-in tension (e.g., a permission-light default plus an
  optional premium precise mode) even before the twist is revealed, and
  defends the choice.
- 3/5: candidate proposes a reasonable but generic full-navigation
  solution and adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("add indoor maps") with
  no segmentation, no metrics, and struggles to respond to the twist.
