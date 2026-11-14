*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 48 — OpenAI: Does Memory Drive Retention? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on ChatGPT. A few months ago you launched memory, which lets ChatGPT remember things about users across conversations. Users can turn it on in settings. Your analytics show that users with memory turned on have 25% higher 30-day retention than users without it. Leadership wants to turn memory on by default for everyone, expecting retention to go up. How would you evaluate whether that's the right decision?"

**Objective (private reference, reveal only if asked directly):** Determine whether memory actually causes higher retention, and what to expect from turning it on by default.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How did users get memory -- did they choose it?" | They opted in by turning it on in settings. About 20% of active users have it on. | On request |
| 2 | "Were users with memory on already different before they turned it on?" | Reveal Exhibit 1 once asked about prior behavior or differences between groups. | On request |
| 3 | "Was there any experiment?" | Reveal Exhibit 2 once asked about experiments, holdouts, or causal evidence. | On request |
| 4 | "Are there risks to turning it on by default?" | Some users are uncomfortable with an assistant remembering personal details; there are also regulatory considerations in some regions. | On request |
| 5 | "How is retention measured?" | Share of users who are active again 30 days after a given week. | On request |
| 6 | "What do users say about memory?" | Reveal Exhibit 3 once asked about user feedback or research. | On request |

**Guardrail reminder:** Do not mention self-selection or correlation vs. causation -- the candidate should question the 25% on their own.

---

## C. Exhibits / data

**Exhibit 1 — Behavior in the Month Before Turning Memory On**

| Metric | Users who later turned memory on | Users who didn't |
|---|---|---|
| Days active per month | 14 | 6 |
| 30-day retention (measured before memory existed) | 78% | 61% |

**Exhibit 2 — Small Randomized Test (memory on by default for a random 5% of new users)**

| Metric | Memory on by default | Memory off by default |
|---|---|---|
| 30-day retention | 52.0% | 51.0% |
| Users who turned memory off within 2 weeks | 9% | -- |

**Exhibit 3 — User Feedback Themes**

- Heavy users: "It's great not to repeat myself."
- Some users: "It remembered something I didn't want it to."
- Many light users had never noticed memory was on.

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Question causality: users chose memory -- are they different?
2. Look at pre-existing differences (self-selection).
3. Use experimental evidence to estimate the true effect.
4. Weigh benefits against risks of default-on.

**Correct core insight:** The 25% is mostly self-selection: users who turned memory on were already much more engaged (14 vs. 6 active days, and 78% vs. 61% retention before memory existed -- already about 28% higher). The randomized test shows the real effect of default-on is small: 52.0% vs. 51.0%, about 2% relative. Meanwhile, 9% turn it off and some users are uncomfortable. Turning it on by default won't deliver anything close to a 25% gain.

**Quantitative reasoning a strong candidate shows:**
- Pre-existing gap: 78 / 61 = about 28% higher retention before memory -- the observed 25% doesn't exceed it.
- Causal effect: (52.0 - 51.0) / 51.0 = about 2% relative.

**A strong final recommendation includes:**
- Don't justify default-on with the 25%; reset expectations to the experimental effect.
- Decide on default-on based on the small gain vs. trust and regulatory risk -- possibly default-on with clear notice and easy controls, or prompting heavy users to turn it on.
- Run a larger randomized test, measuring retention, opt-outs, and trust signals.
- Teach the team to use holdouts for feature impact claims.

**Scoring anchors:**
- 5/5 insight generation: identifies self-selection, uses pre-period data and the experiment to estimate the real effect, and weighs it against risks.
- 3/5: suspects self-selection but doesn't quantify or use the experiment.
- 1/5: accepts the 25% and recommends default-on.
