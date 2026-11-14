*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 49 — OpenAI: Should the Free Tier Have Ads? (PM Strategy & Growth Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on ChatGPT's monetization team. Hundreds of millions of people use the free version, and serving them costs a lot. Leadership is debating whether to introduce advertising in the free tier, and if so, how. They're worried about user trust and about hurting paid subscriptions. They want your recommendation. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Recommend whether and how to introduce ads in the free tier, weighing revenue, cost, trust, and impact on paid plans.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the goal -- cover costs, grow revenue, something else?" | Make the free tier sustainable and grow revenue, without damaging trust or the subscription business. | On request |
| 2 | "How many free users and what do they cost?" | Reveal Exhibit 1 once asked about users, costs, or economics. | On request |
| 3 | "What kinds of conversations do free users have?" | Reveal Exhibit 2 once asked about usage or intent. | On request |
| 4 | "How would ads affect trust?" | Reveal Exhibit 3 once asked about user sentiment, trust, or research. | On request |
| 5 | "How do free users become paid?" | About 3% of monthly free users upgrade within a year, mostly after hitting usage limits. | On request |
| 6 | "Do competitors have ads?" | Some AI search products show sponsored results; reactions have been mixed. Search engines have had ads for decades. | On request |
| 7 | "Are there conversations where ads would be inappropriate?" | Yes -- health, mental health, personal crises, and anything involving minors are sensitive. | On request |

**Guardrail reminder:** Do not tell the candidate whether to add ads, where to place them, or which users to exclude -- let them reason it through.

---

## C. Exhibits / data

**Exhibit 1 — Free Tier Economics (illustrative)**

| Metric | Value |
|---|---|
| Monthly free users | 500M |
| Average serving cost per free user per year | about $6 |
| Paid subscribers | 15M at about $240 a year |

**Exhibit 2 — Free-Tier Conversation Mix**

| Type | Share of conversations |
|---|---|
| Learning, writing, work tasks | 55% |
| Shopping and product research (e.g. "best running shoes under $100") | 12% |
| Travel and local recommendations | 8% |
| Personal, health, or emotional topics | 15% |
| Other | 10% |

**Exhibit 3 — User Research (survey of 5,000 free users)**

| Statement | Agree |
|---|---|
| "I'd accept clearly labeled sponsored suggestions when I'm shopping." | 58% |
| "I'd trust answers less if ads appeared in them." | 64% |
| "I'd pay to avoid ads." | 11% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the goal and the economics of the free tier.
2. Identify where ads fit naturally (commercial intent) vs. where they'd hurt trust.
3. Estimate revenue potential and costs to trust and subscriptions.
4. Design guardrails and a test plan.

**Quantitative reasoning a strong candidate shows:**
- Free tier cost: 500M x $6 = about $3B a year.
- Commercial-intent conversations: 12% shopping + 8% travel = 20% of conversations.
- Revenue sizing (candidate's own assumptions are fine), e.g. if ads in commercial-intent conversations earn $5-10 per user per year -> $2.5-5B, enough to cover most of the free-tier cost.
- Subscription risk: 11% would pay to avoid ads -- an upside for paid plans, not just a risk.

**Correct core insight:** Ads everywhere would damage trust (64% say they'd trust answers less) and the core value of the product. But a fifth of conversations already have commercial intent, where users are open to clearly labeled suggestions (58%). Ads limited to those moments, clearly separated from the answer, could cover most of the free tier's cost while keeping trust -- and an ad-free paid tier gives another reason to upgrade.

**A strong final recommendation includes:**
- Introduce ads only in commercial-intent conversations, clearly labeled and separated from the answer; never inside answers or in sensitive topics.
- Strict policy: ads never influence the model's answer.
- Test in a limited market first; measure revenue per user, trust metrics, retention of free users, and upgrades.
- Use "ad-free" as an added benefit of paid plans.

**Scoring anchors:**
- 5/5 business sense: sizes the cost and revenue, targets commercial intent, protects trust with clear rules, considers the subscription upside, and proposes a test.
- 3/5: reasonable recommendation without quantification, or ignores sensitive topics.
- 1/5: ads everywhere to maximize revenue, or rejects ads without considering the economics.
