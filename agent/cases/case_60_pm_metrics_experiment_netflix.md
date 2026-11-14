*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 60 — Netflix: Artwork That Gets Clicks (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Netflix's personalization team. You tested a new way of choosing the artwork -- the image shown for each title on the home screen. In the test, the click-through rate on titles went up 8%. The team wants to roll it out to everyone. Your director asks you to make sure it's actually better for members. How would you evaluate the result?"

**Objective (private reference, reveal only if asked directly):** Determine whether the higher click-through represents real value for members, and decide whether to ship.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the goal of artwork personalization?" | Help members find something they'll enjoy, faster -- ultimately more satisfied members who keep their subscription. | On request -- key framing fact |
| 2 | "How was the test run?" | Members randomly split 50/50 for four weeks. | On request |
| 3 | "What happens after members click?" | Reveal Exhibit 1 once asked about what happens after the click, viewing, or abandonment. | On request |
| 4 | "What kind of artwork does the new method choose?" | It tends to pick more dramatic images -- action scenes or popular actors -- even when they aren't central to the story. | On request |
| 5 | "What about longer-term metrics?" | Reveal Exhibit 2 once asked about satisfaction, retention, or long-term metrics. | On request |
| 6 | "Did members watch more overall?" | Total viewing hours were about the same in both groups. | On request |

**Guardrail reminder:** Do not mention qualified plays, abandonment, or misleading artwork -- the candidate should look beyond click-through rate on their own.

---

## C. Exhibits / data

**Exhibit 1 — After the Click (per 1,000 title impressions)**

| Metric | Control | Test |
|---|---|---|
| Clicks | 50 | 54 |
| Plays abandoned within 5 minutes | 10 | 17 |
| Plays watched for 15+ minutes | 32 | 30 |

**Exhibit 2 — Longer-Term Signals (4 weeks)**

| Metric | Control | Test |
|---|---|---|
| Time spent browsing before starting something | 6.0 min | 6.8 min |
| Members saying "I found something I wanted to watch" (survey) | 71% | 66% |
| Monthly cancellations | 2.0% | 2.1% (not significant) |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Start from the goal (find enjoyable content faster), not clicks.
2. Look at what happens after the click: real viewing vs. quick abandonment.
3. Check longer-term member signals.
4. Decide and redefine the success metric.

**Correct core insight:** The new artwork is better at getting clicks, not at helping members choose. More clicks lead to more quick abandonment (10 to 17 per 1,000), and fewer plays that last 15+ minutes (32 to 30). Members browse longer and fewer say they found something they wanted. Dramatic artwork that isn't representative of the title is close to clickbait -- it works against the goal.

**Quantitative reasoning a strong candidate shows:**
- Click-through: 54 vs. 50 = +8%.
- Qualified plays (15+ minutes): 30 vs. 32 = -6%.
- Abandonment rate among clicks: 17/54 = 31% vs. 10/50 = 20%.

**A strong final recommendation includes:**
- Don't ship.
- Change the success metric to qualified plays (e.g. 15+ minutes) or satisfaction, not click-through.
- Constrain artwork to images representative of the title; retrain the selection method on qualified plays.
- Guardrails: abandonment, browsing time, satisfaction survey, cancellations over a longer period.

**Scoring anchors:**
- 5/5 insight generation: looks past clicks to abandonment and qualified plays, uses survey and browsing data, and redefines the metric.
- 3/5: notices more abandonment but still leans toward shipping, or doesn't redefine the metric.
- 1/5: recommends shipping because click-through went up 8%.
