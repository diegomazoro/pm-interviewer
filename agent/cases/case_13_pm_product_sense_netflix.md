*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 13 — Netflix: Helping Groups Agree on What to Watch (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Netflix. A common frustration among households and roommates is that multiple people want to watch something together but can't agree on what -- they end up scrolling through the home screen for fifteen minutes, or give up and watch something nobody's excited about. How would you design a feature to help groups of people decide together what to watch?"

**Objective (private reference, reveal only if asked directly):** Design a group decision-making feature for shared viewing, with a clear starting segment, a scoped mechanism, and metrics tied to both discovery and actual watch behavior.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What kind of group are we talking about -- a household, a couple, remote friends?" | Not decided -- that's part of what the candidate should reason through. Households/roommates sharing a physical TV are the most common case reported; remote friends watching separately but wanting to pick together is a smaller but growing pattern. | On request |
| 2 | "What's the business motivation for solving this?" | Prolonged, indecisive browsing is associated with session abandonment (leaving without watching anything), so this is framed as a way to reduce abandonment and increase satisfaction with what's ultimately watched, not just discovery engagement. | On request -- important scoping context |
| 3 | "What exists today?" | Recommendations today are generated per individual profile; there's no mechanism that combines multiple people's preferences into a single joint recommendation or decision flow. | On request |
| 4 | "Is there a technical constraint around combining profiles?" | Profile-level viewing history and taste data can be combined for people using the same account/household, but there are privacy considerations around exposing one profile's specific viewing history to another profile. | On request |
| 5 | "What do competitors or other apps do here?" | Reveal Exhibit 2 (competitive note) if asked. | On request |
| 6 | "Is there any data on how long people spend browsing before watching, or abandoning?" | Reveal Exhibit 1 (browse behavior data) once the candidate asks for evidence, or once they propose an initial direction. | On request or framework-gated |
| 7 | "Does this need to work in real time (everyone home at once) or can it be async?" | Open question -- both patterns exist; real-time (everyone on the couch right now) is the more commonly described pain point. | On request |
| 8 | "Should this only surface titles already in the catalog, or could it influence what gets recommended long-term?" | Open question for the candidate to weigh -- not decided whether this is a one-time decision tool or something that also feeds back into future recommendations. | On request |

**Guardrail reminder:** Do not tell the candidate which group type, decision mechanism, or specific matching approach to pick, and do not confirm whether a swipe-and-match style feature or any other specific idea is "the" right direction -- these are exactly the decisions the candidate should reason through and prioritize themselves.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in a prototype test of a swipe-and-match feature, where each person swipes on titles and the app surfaces whatever everyone likes, groups reached a matched title 68% of the time within two minutes, but 40% of those matched titles were abandoned within the first ten minutes of playback -- a higher abandonment rate than titles picked without using the tool at all."

---

## C. Exhibits / data

**Exhibit 1 — Browse Behavior Data (reveal once candidate asks for evidence, or once an initial direction is proposed)**

| Metric | Value |
|---|---|
| Avg. time spent browsing before pressing play, multi-viewer sessions | 14.5 minutes |
| Avg. time spent browsing before pressing play, single-viewer sessions | 4 minutes |
| % of multi-viewer sessions that end with no title played at all | 22% |
| % of multi-viewer sessions where the title played is later abandoned in the first 10 minutes | 18% |
| % match rate within 2 minutes in swipe-and-match prototype | 68% |
| % of swipe-and-match "matched" titles abandoned within first 10 minutes of playback | 40% |

**Exhibit 2 — Competitive Landscape Note (reveal only if asked)**

Other streaming and social apps have shipped simple "everyone votes, majority wins" style pickers for group decisions, generally optimized for speed of reaching a decision rather than for how satisfied the group ends up being with the pick.

---

## D. Model answer / "what good looks like"

This is a PRODUCT SENSE case -- graded on the 5-dimension product sense
rubric (problem framing & segmentation, product taste, prioritization &
tradeoffs, business judgment & metrics, communication & composure under
follow-ups), not the diagnostic 8-dimension rubric. There is no single
"correct" feature design; what matters is the quality of reasoning.

**Strong problem framing:** picks a specific starting segment rather than
"everyone" -- e.g., co-located households/roommates sharing one TV at
one moment, since exhibit 1 shows the sharpest browsing-time and
abandonment gap there. Explicitly separates "reaching a decision
quickly" from "reaching a decision people actually want to watch through,"
since the prompt's real complaint spans both.

**Product taste:** goes beyond "let everyone swipe and take the overlap"
-- e.g., proposes weighting toward strength of preference (a title one
person loves and nobody hates) rather than pure overlap, or building in
a "veto" rather than requiring mutual "like," or surfacing why a title
was picked so the group has context and buy-in. Shows conviction in a
specific direction rather than listing options with no pick.

**Prioritization & tradeoffs:** explicitly scopes v1 -- e.g., launch for
households with 2-4 profiles on one account, using a simple
swipe/react mechanism, deferring async cross-account matching (separate
friends watching separately) and long-term recommendation feedback loops
to later phases.

**Business judgment & metrics:** ties the recommendation to the stated
motivation (reducing abandonment, protecting satisfaction) and proposes
concrete metrics -- e.g., reduction in sessions ending with no title
played, plus a guardrail metric like early-abandonment rate of the
picked title (not just time-to-decision or match rate) -- rather than a
vague goal like "make picking faster."

**Composure under the follow-up:** the scripted twist (fast matches that
get abandoned quickly -- a "lowest common denominator" problem) directly
challenges a naive "just find the overlap and match fast" answer. A
strong candidate adapts -- e.g., shifts the mechanism to weight strong
preference over simple overlap, adds a "veto" instead of requiring
mutual approval, or redefines success as completed-watch rate rather
than match-speed -- rather than dismissing the data or abandoning their
framework entirely.

**Scoring anchors:**
- 5/5 product taste: candidate's design anticipates or elegantly resolves
  the lowest-common-denominator tension (e.g., preference-weighted
  matching or veto-based design) even before the twist is revealed, and
  defends the choice.
- 3/5: candidate proposes a reasonable but generic swipe-and-match idea
  and adjusts adequately once the twist is revealed.
- 1/5: candidate proposes a single vague idea ("let everyone vote") with
  no segmentation, no metrics, and struggles to respond to the twist.
