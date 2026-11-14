*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 22 — Figma: Helping Non-Designers Create On-Brand Assets (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Figma. More and more people who aren't designers -- marketers, salespeople, people in operations -- open Figma to make quick assets like social posts, slides, or one-pagers. Design teams complain that these assets often break the brand: wrong fonts, off-brand colors, detached components. How would you design a better experience for non-designers creating assets in Figma?"

**Objective (private reference, reveal only if asked directly):** Design an approach that lets non-designers create assets quickly while keeping them on-brand, with a clear target user, MVP, tradeoffs, and success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Which companies or plans are we talking about?" | Mostly Organization and Enterprise customers that already have a design system in Figma. | On request |
| 2 | "Who are these non-designers, specifically?" | About half are marketers, a quarter are sales and customer success, and the rest are spread across operations, HR, and founders at smaller companies. | On request |
| 3 | "What are they typically making?" | Social media graphics, event banners, sales one-pagers, and internal presentation slides -- usually by duplicating an old file and editing it. | On request |
| 4 | "How do they learn Figma today?" | Mostly self-taught or shown by a designer once. Most use fewer than ten tools in the editor. | On request |
| 5 | "What exactly goes wrong with the brand?" | Reveal Exhibit 1 once the candidate asks what breaks or for data on brand issues. | On request |
| 6 | "What's the business motivation?" | Non-designer seats are the fastest-growing seat type at large customers, and they're a key argument for expanding Figma beyond the design team. But design leaders say they'll restrict access if brand quality keeps suffering. | On request -- important context |
| 7 | "How do design teams feel about this today?" | Reveal Exhibit 2 once asked about design teams' perspective, workload, or review process. | On request |
| 8 | "What do competitors do?" | Template-based design tools for non-designers are popular and easy, but design teams say they drift from the official design system because they're maintained separately. | On request |

**Guardrail reminder:** Do not tell the candidate whether to focus on marketers or another group, whether to lock things down or give flexibility, or whether templates are the right answer -- those are the calls they need to make and defend.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in an early pilot with locked, brand-approved templates, non-designers created three times more assets, but design teams ended up spending more time, not less, reviewing them -- and 40% of the templated assets still had components detached by the end."

---

## C. Exhibits / data

**Exhibit 1 — Brand Issues Found in a Sample of 500 Non-Designer Assets**

| Issue | Share of assets with the issue |
|---|---|
| Detached or edited design-system components | 52% |
| Off-brand colors (not from the shared library) | 38% |
| Wrong fonts or text styles | 31% |
| Outdated logo or imagery | 17% |
| No issues | 24% |

**Exhibit 2 — Design Team Perspective (survey of 120 design leads)**

| Signal | Value |
|---|---|
| Hours per week a design team spends fixing or reviewing non-designer assets | 6 hours (median) |
| Design leads who would "prefer non-designers make their own assets if quality were guaranteed" | 81% |
| Design leads who have considered restricting non-designer edit access | 44% |
| Most requested capability | "Let non-designers change content without touching the design" |

---

## D. Model answer / "what good looks like"

**Strong problem framing:** clarifies whose problem this is (non-designers want speed; design teams want brand safety) and picks a specific segment -- e.g. marketers at enterprise customers making recurring assets like social posts -- rather than "all non-designers." Notices from Exhibit 2 that design teams actually want non-designers to self-serve if quality holds.

**Product taste:** goes beyond "make templates." Strong ideas separate content from design: a simplified "content mode" where non-designers can only change text, images, and approved variants, while the layout and components stay linked to the design system; brand-aware guardrails (only library colors and fonts available); one-click "request design review" with diff view; automatic propagation when the design system updates. An ambitious option: assets that stay live-linked to the design system so brand updates flow through automatically.

**Prioritization & tradeoffs:** states an MVP -- e.g. a content-only editing mode on designer-published templates for the top asset types -- and leaves out things like AI generation or a full non-designer editor for v1. Discusses the flexibility vs. control tradeoff explicitly.

**Business judgment & metrics:** ties to non-designer seat growth and the risk of design leaders restricting access. Metrics: share of non-designer assets with zero brand issues, design-team review hours, assets created per non-designer. Guardrail: non-designer satisfaction / time to create an asset.

**Composure under the follow-up:** the twist shows locked templates increase volume but not quality or review savings -- people still detach components to get what they need. A strong candidate digs into why (templates don't cover their real needs, so they break them), and adapts: give approved flexibility (variants, swappable slots) rather than hard locks, and measure review time and issue rate, not asset volume.

**Scoring anchors:**
- 5/5: specific segment, content-vs-design separation idea, clear MVP with exclusions, metrics on brand quality and review time, and a thoughtful adaptation to the twist.
- 3/5: reasonable template-based solution but generic segment, or metrics focused only on asset volume.
- 1/5: proposes a generic tutorial or "restrict non-designers" with no view on both sides, and ignores the twist.
