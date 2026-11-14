*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 44 — Anthropic: Is the Thumbs-Up Rate Telling the Truth? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on the Claude consumer app. Your team tested a new response style -- more detailed, more thorough answers -- against the current one. In the test, the thumbs-up rate on responses rose from 72% to 78%. The team wants to make it the default for everyone. Your director asks you to check whether that's the right call. How would you evaluate it?"

**Objective (private reference, reveal only if asked directly):** Determine whether the new response style truly improves the user experience and is worth shipping.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is thumbs-up rate calculated?" | Thumbs-up divided by all thumbs (up plus down) on responses. | On request |
| 2 | "How many responses get any rating?" | Reveal Exhibit 1 once asked about rating volume or how many users rate. | On request |
| 3 | "Where is the thumbs button?" | At the end of each response. | On request |
| 4 | "How did user behavior change -- retention, conversation length?" | Reveal Exhibit 2 once asked about retention, engagement, or other metrics. | On request |
| 5 | "What about cost?" | Reveal Exhibit 3 once asked about cost or guardrails. | On request |
| 6 | "Was there any independent quality evaluation?" | Yes -- a blind human evaluation compared 2,000 response pairs. Reveal Exhibit 3 if asked for the results. | On request |
| 7 | "How long did the test run?" | Three weeks, with users randomly split 50/50. | On request |

**Guardrail reminder:** Do not mention selection bias, the rating rate, or response length -- the candidate should question the thumbs metric on their own.

---

## C. Exhibits / data

**Exhibit 1 — Rating Volume**

| Metric | Current style | New style |
|---|---|---|
| Share of responses that get any thumbs rating | 3.0% | 1.5% |
| Average response length | 280 words | 520 words |
| Thumbs-up rate | 72% | 78% |

**Exhibit 2 — User Behavior**

| Metric | Current style | New style |
|---|---|---|
| Day-7 retention | 41.0% | 41.2% (not significant) |
| Messages per conversation | 4.1 | 3.6 |
| Share of users who ask "shorter please" or similar | 2% | 7% |

**Exhibit 3 — Guardrails**

| Metric | Current style | New style |
|---|---|---|
| Compute cost per conversation | baseline | +35% |
| Blind human evaluation: new style preferred | -- | 52% vs. 48% (not significant) |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Understand the metric: who gives thumbs and when.
2. Check for selection bias: did the new style change who rates?
3. Look at outcome metrics (retention, engagement) and guardrails (cost, quality).
4. Decide, with a better measurement plan.

**Correct core insight:** The thumbs-up rate is biased. The button is at the end of each response; with answers almost twice as long, half as many responses get rated (3.0% to 1.5%), and the people who scroll to the end of a long answer are likely the most satisfied. Real outcomes are flat: retention unchanged, users send fewer messages per conversation, 7% ask for shorter answers, blind evaluation shows no significant preference -- and cost per conversation is up 35%. There's no evidence it's better, and it's clearly more expensive.

**Quantitative reasoning a strong candidate shows:**
- Rated responses halved: the 78% comes from a smaller, more self-selected group.
- Cost: +35% per conversation with no retention gain -> negative return at scale.

**A strong final recommendation includes:**
- Don't ship as default.
- Use better metrics: retention, task completion, blind evaluations, explicit length-preference signals.
- Explore adaptive length (detailed when the question needs it, concise otherwise) or a user setting.
- Fix the measurement: put the feedback control where it's equally visible regardless of length, or sample users for ratings.

**Scoring anchors:**
- 5/5 insight generation: identifies selection bias from halved rating volume and longer answers, checks retention, blind eval, and cost, and recommends not shipping plus better metrics.
- 3/5: notices cost or flat retention but doesn't identify the rating bias.
- 1/5: recommends shipping because thumbs-up went up.
