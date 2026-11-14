*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 36 — Linear: Did the New Onboarding Hurt Activation? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Linear. A month ago your team launched a new onboarding flow for new workspaces. Since then, the activation rate -- the share of new workspaces that become active in their first two weeks -- has dropped from 40% to 36%. Some people on the team want to roll the new onboarding back immediately. What would you do?"

**Objective (private reference, reveal only if asked directly):** Determine whether the new onboarding actually hurt activation before deciding to roll it back.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is activation defined?" | A new workspace that creates at least 10 issues and has at least 2 active members in its first 14 days. | On request |
| 2 | "Was it an A/B test?" | No -- the new onboarding launched to everyone at once. This is a before/after comparison. | On request |
| 3 | "Did the number or type of signups change?" | Signups doubled in the same month after a popular video about Linear spread widely online. | On request -- key fact |
| 4 | "Who signed up from that video?" | Reveal Exhibit 1 once asked about the mix of signups. | On request |
| 5 | "Can I see activation by segment?" | Reveal Exhibit 2 once asked for activation by segment. | On request |
| 6 | "What changed in the new onboarding?" | It replaced an empty workspace with a guided setup: import from another tool, invite teammates, and a sample project. | On request |
| 7 | "Did anything else change?" | No other product changes. | On request |

**Guardrail reminder:** Do not mention the signup mix or segment-level activation unless asked, and do not say whether the onboarding is good or bad -- the candidate should find the mix shift on their own.

---

## C. Exhibits / data

**Exhibit 1 — Signup Mix**

| Segment | Before launch | After launch |
|---|---|---|
| Company teams (work email domain) | 60% | 30% |
| Solo users (personal email, hobby projects) | 40% | 70% |

**Exhibit 2 — Activation Rate by Segment**

| Segment | Before launch | After launch |
|---|---|---|
| Company teams | 55% | 60% |
| Solo users | 17.5% | 25.7% |
| Overall | 40% | 36% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Confirm the metric and how the comparison was made (before/after, not a test).
2. Look for other things that changed: traffic volume and mix.
3. Segment the metric to separate mix effects from real effects.
4. Decide, and set up a better way to measure going forward.

**Correct core insight:** This is a mix shift (Simpson's paradox). Activation went up in both segments -- company teams from 55% to 60%, solo users from 17.5% to 25.7% -- but the overall rate fell because the viral video brought in many more solo users, who activate much less. The new onboarding appears to help; rolling it back would be a mistake.

**Quantitative reasoning a strong candidate shows:**
- Before: 0.6 x 55% + 0.4 x 17.5% = 33 + 7 = 40%.
- After: 0.3 x 60% + 0.7 x 25.7% = 18 + 18 = 36%.
- Holding the old mix constant: 0.6 x 60% + 0.4 x 25.7% = 36 + 10.3 = about 46% -- an improvement of ~6 points.

**A strong final recommendation includes:**
- Don't roll back; explain the mix shift to the team.
- Report activation by segment (or mix-adjusted) going forward, since the headline number is sensitive to who signs up.
- Confirm with an A/B test or holdout for future onboarding changes.
- Optionally: consider whether solo users need a different activation definition (2 active members may not fit them).

**Scoring anchors:**
- 5/5 insight generation: identifies the mix shift, shows both segments improved, computes a mix-adjusted rate, and recommends keeping the onboarding plus segment reporting.
- 3/5: suspects the viral traffic matters but doesn't segment or quantify.
- 1/5: recommends rolling back based on the headline drop.
