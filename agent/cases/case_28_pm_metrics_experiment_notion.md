*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 28 — Notion: Is Forms a Success? (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're the PM for Notion Forms, a new feature that lets users build forms whose responses land in a Notion database. Six weeks after launch, 1.2 million forms have been created, and leadership is calling it one of the most successful launches of the year. Your VP asks you to put together a proper success scorecard before the next planning cycle. How would you evaluate whether Forms is actually succeeding?"

**Objective (private reference, reveal only if asked directly):** Define meaningful success metrics for Forms and assess whether the launch is succeeding by those metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What was Forms supposed to achieve?" | Two things: replace external form tools so teams keep that work inside Notion, and bring new people into Notion through form respondents. | On request -- key framing fact |
| 2 | "How many people created the 1.2M forms?" | About 800,000 users. | On request |
| 3 | "How did people discover Forms?" | Two ways: a promotional banner shown to all users at launch with a "Try Forms" button that creates a sample form, and the regular "+ Form" option inside databases. | On request |
| 4 | "How many forms actually got responses?" | Reveal Exhibit 1 once asked about responses, usage, or forms being used. | On request |
| 5 | "Do people come back and create more forms?" | 15% of creators made a second form within 30 days. | On request |
| 6 | "What about respondents -- do they sign up for Notion?" | Reveal Exhibit 2 once asked about respondents or acquisition. | On request |
| 7 | "Is there data by how people found Forms?" | Reveal Exhibit 3 once asked for a breakdown by entry point or source. | On request |
| 8 | "Are teams replacing their external form tools?" | Early signal only: among workspaces that connected an external form tool integration before launch, 18% have stopped using that integration since. | On request |

**Guardrail reminder:** Do not suggest that "forms created" is a vanity metric, do not point to the banner or the entry-point breakdown, and do not propose metrics for the candidate -- they should define success themselves.

---

## C. Exhibits / data

**Exhibit 1 — Form Usage (first 6 weeks)**

| Metric | Value |
|---|---|
| Forms created | 1,200,000 |
| Forms with at least 1 response | 30% |
| Forms with 10+ responses | 12% |

**Exhibit 2 — Respondents**

| Metric | Value |
|---|---|
| Unique respondents who weren't Notion users | 9,000,000 |
| Of those, signed up for Notion within 30 days | 0.4% |

**Exhibit 3 — Forms by Entry Point**

| Entry point | Share of forms created | Forms with at least 1 response |
|---|---|---|
| Launch banner ("Try Forms") | 65% | 8% |
| "+ Form" inside a database | 35% | 71% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Start from the goals (replace external tools; acquire via respondents).
2. Separate vanity metrics (forms created) from value metrics (forms that collect responses, repeat creators, respondents who sign up, external tools replaced).
3. Segment by entry point to see where real usage comes from.
4. Propose a scorecard with targets and guardrails.

**Correct core insight:** "1.2M forms created" is inflated by curiosity clicks on the launch banner: 65% of forms came from the banner and only 8% of those ever got a response, versus 71% for forms created from inside a database. Only 30% of forms got any response, 15% of creators came back. The real signal is the organic, database-created forms: about 0.35 x 1.2M = 420,000 forms, of which ~71% are in active use. Acquisition is promising: 9M non-user respondents x 0.4% = about 36,000 new signups.

**Quantitative reasoning a strong candidate shows:**
- Forms with responses: 30% x 1.2M = 360,000; from the banner: 65% x 1.2M x 8% = about 62,000; from databases: 35% x 1.2M x 71% = about 298,000. Most real usage comes from the organic entry point.
- Respondent-driven signups: about 36,000 in six weeks.

**A strong final recommendation includes:**
- Retire "forms created" as the headline; use "active forms" (e.g. 10+ responses or responses in the last 2 weeks), repeat creators, and teams replacing external tools.
- Acquisition metric: respondent signups, with a plan to improve the 0.4% (e.g. better "made with Notion" experience).
- Set targets based on the organic baseline, not the launch spike.
- Guardrail: form spam/abuse, database clutter from unused sample forms.

**Scoring anchors:**
- 5/5 insight generation: identifies the banner inflation via the entry-point breakdown, quantifies real usage, and builds a scorecard tied to both goals.
- 3/5: recognizes forms created is a weak metric and proposes better ones, but doesn't use the data to size real usage.
- 1/5: accepts 1.2M as success, or lists generic metrics (DAU, NPS) not tied to the goals.
