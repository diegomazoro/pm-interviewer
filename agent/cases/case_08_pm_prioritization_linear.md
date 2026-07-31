*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 8 — Linear: Roadmap Prioritization Trade-off (PM Prioritization Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Linear. Your team has capacity for one major initiative next quarter, and two candidates are on the table: (1) a native mobile app (currently Linear is web/desktop only, with a weak mobile web experience), and (2) a customer-requested 'advanced automation/workflow rules' feature for power users. Your engineering lead wants your recommendation with reasoning, not just a gut call. How would you approach deciding?"

**Objective (private reference, reveal only if asked directly):** Recommend which initiative to prioritize next quarter, with clear reasoning and an acknowledgment of what's being traded off.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the company's current strategic priority — growth, retention, expansion upmarket?" | Current stated priority is growing seat count within existing enterprise/mid-market customers (expansion) and improving retention of teams already using Linear, rather than acquiring net-new logos this particular quarter. | On request — important framing fact |
| 2 | "How many users are asking for each feature, and who are they?" | Reveal Exhibit 1 once asked. | On request |
| 3 | "What's the engineering effort/size for each?" | Native mobile app: large, ~1 full quarter for a minimally viable version (issue viewing, commenting, notifications only — not full parity). Automation/workflow rules: medium, ~6 weeks for a first version covering the most-requested rule types. | On request |
| 4 | "Is there competitive pressure — do competitors have these already?" | Most competitors have some native mobile app already, seen as table-stakes by some prospects. Advanced automation is more differentiated — fewer competitors have it, and it's often cited as a reason power users choose one tool over another. | On request |
| 5 | "What do churn/win-loss reports say about either gap?" | Reveal Exhibit 2 once asked. | On request |
| 6 | "Would either feature require ongoing maintenance/support burden?" | Native mobile app has significant ongoing burden (2 more platforms to maintain, app store review cycles). Automation rules mostly reuse existing backend workflow infrastructure, lower ongoing burden. | On request |
| 7 | "Is there a partial/cheaper version of either option?" | Mobile: could ship a scoped-down "notifications + quick triage" mobile app instead of full parity, in about half the time. Automation: could ship the top 3 most-requested rule types first instead of the full rule-builder, in about 3 weeks instead of 6. | Reveal if asked about scoping down either option — a strong candidate should think to ask this |
| 8 | "How does each map to expansion/retention specifically (the stated priority)?" | Automation is disproportionately requested by existing large accounts already expanding seats — direct fit with the stated priority. Mobile app requests are more evenly spread across all account sizes and correlate more with net-new deal wins than expansion of existing accounts. | Reveal if asked to connect either option back to the stated strategic priority — this is the crux |
| 9 | "Can I see the request/data breakdown?" | Hand over Exhibit 1 once a framework (e.g., reach/impact/confidence/effort or similar) is proposed. | Framework-gated |

**Guardrail reminder:** Do not tell the candidate which option is "the right answer" — either can be argued well if reasoned from the stated priority and data; the point is to see if they build and apply a consistent prioritization framework rather than picking based on gut feel or personal preference.

---

## C. Exhibits / data

**Exhibit 1 — Feature Request Volume and Requester Profile**

| Feature | # of distinct accounts requesting (last 2 quarters) | % from existing large/expanding accounts | % from prospects (not yet customers) |
|---|---|---|---|
| Native mobile app | 340 | 45% | 35% (rest from small existing accounts) |
| Advanced automation/workflow rules | 210 | 70% | 10% (rest from small existing accounts) |

**Exhibit 2 — Win-Loss / Churn Notes (qualitative, sales & CS reported reasons, last 2 quarters)**

- Lost deals citing "no native mobile app": 18 deals, mostly early-stage prospects evaluating multiple tools.
- Churned or downgraded existing accounts citing "outgrew Linear's automation capabilities, moved workflows to a competitor/custom tooling": 9 accounts, all mid-to-large accounts that had been expanding seats before churning.
- Average contract value of the 9 automation-related churned accounts is notably higher than the average of the 18 mobile-related lost prospect deals.

**Exhibit 3 (reveal only if asked about effort/timeline specifics) — Effort Detail**

| Option | Full scope | Scoped-down version |
|---|---|---|
| Native mobile app | ~12 weeks, full team | ~6 weeks, notifications + triage only |
| Automation rules | ~6 weeks, full rule-builder | ~3 weeks, top 3 rule types only |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build (PM prioritization):**
1. Anchor on the stated strategic goal (expansion/retention of existing accounts, this quarter) before comparing options.
2. Evaluate each option against consistent criteria: reach/demand, impact on the stated goal, effort/cost, confidence, and strategic/competitive fit (a RICE-style or equivalent framework is fine).
3. Explicitly compare, rather than evaluating each option in isolation.
4. Consider scoped-down versions as alternatives to a binary choice.
5. Make a recommendation and state clearly what's being traded off (i.e., what happens to the option not chosen).

**Correct core insight:** Raw request volume favors mobile (340 vs. 210 accounts), which could tempt a candidate into picking it on a naive "more people want it" basis — but the stated priority is expansion/retention of existing accounts, not net-new logo acquisition, and the segmented data reverses the picture: automation is requested overwhelmingly by existing large/expanding accounts (70%) and is directly implicated in higher-value account churn (Exhibit 2, higher ACV), while mobile app demand skews toward prospects and lower-value churn/loss situations. Effort also favors automation (6 weeks vs. 12, with a further scoped-down 3-week option). A strong candidate should therefore favor automation given this quarter's specific stated priority, while explicitly noting mobile remains a real gap worth revisiting when the priority shifts toward net-new acquisition.

**A strong final recommendation includes:**
- A clear recommendation (automation, given the current expansion/retention priority) tied explicitly back to the segmented data, not just aggregate request counts.
- Consideration of the scoped-down version (top 3 rule types in ~3 weeks) as a way to potentially do a fast version of automation now and revisit capacity for a mobile MVP later in the same quarter or next.
- An explicit acknowledgment of the trade-off/opportunity cost: mobile app demand and the prospect-side deal losses are real and shouldn't be ignored indefinitely.
- A suggested way to validate the decision (e.g., track expansion-account retention/seat growth after shipping automation, and revisit mobile if the strategic priority shifts).

**Scoring anchors:**
- 5/5 business/commercial sense: candidate anchors on the stated strategic priority first, correctly reverses the naive "raw volume" read using the segmented data, and considers a scoped-down option rather than treating it as strictly binary.
- 3/5: candidate compares the two options on effort and demand but doesn't tie the decision back to the stated strategic priority, or picks based on raw request volume alone.
- 1/5: candidate picks an option based on personal preference/familiarity with the product category rather than the data provided, or never asks about the company's current strategic priority.
