*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 5 — Notion: Drop in Retention (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM at Notion, focused on the personal/individual user segment (not teams). Looking at cohort data, the Week-4 retention rate for new signups has dropped from 38% to 26% over the last two months, for users who signed up organically (not from a paid ad campaign). Leadership wants to understand why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the Week-4 retention drop for organic individual signups and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is Week-4 retention defined exactly?" | % of signups who are still active (opened the app and edited a page) in the 7-day window ending on day 28. | On request |
| 2 | "Did the onboarding flow change recently?" | Yes — a new onboarding flow launched ~10 weeks ago, replacing a 3-step guided setup with a single templated "AI-generated workspace" step meant to get users to a filled-in workspace faster. | On request — key fact |
| 3 | "Did signup volume or the mix of signup sources change?" | Signup volume is up ~15% (more organic signups than before, partly from a viral social post), but the question specifically already isolates organic users, so this is a secondary consideration, not the core answer. | On request |
| 4 | "Did anything change about pricing or free-tier limits?" | No changes to free tier limits or pricing in this window. | On request |
| 5 | "What does the AI-generated workspace actually produce for a new user?" | It auto-creates a workspace with template pages (notes, tasks, docs) based on a couple of onboarding survey answers (e.g., "what will you use Notion for"). | On request |
| 6 | "Is there data on whether people use or delete the AI-generated content?" | Reveal Exhibit 1 once asked. | On request |
| 7 | "Did activation metrics (e.g., % who create their first page) change?" | Activation (creating/editing at least one page in the first session) actually went up slightly, from 71% to 76%, since the AI step guarantees a populated workspace immediately. | On request — important counterintuitive fact: activation improved but retention worsened |
| 8 | "Is there a difference in retention between users who keep vs. delete the AI-generated content?" | Reveal Exhibit 2 once asked — this is the key diagnostic cut. | On request |
| 9 | "Any change in mobile vs. desktop signup mix?" | No meaningful shift. | On request |
| 10 | "Can I see exhibits / cohort data?" | Hand over Exhibit 1 once framework proposed. | Framework-gated |

**Guardrail reminder:** The counterintuitive twist here (activation up, retention down) is the crux of the case — don't confirm or deny the candidate's hypothesis about why; just supply the requested data.

---

## C. Exhibits / data

**Exhibit 1 — AI-Generated Workspace Content Fate (first 7 days)**

| Outcome | % of new users |
|---|---|
| Kept most/all AI-generated content, added little of their own | 54% |
| Deleted some AI-generated content, replaced with own pages | 31% |
| Deleted all AI-generated content immediately | 15% |

**Exhibit 2 — Week-4 Retention by Content Behavior**

| Behavior group | Week-4 Retention |
|---|---|
| Kept most/all AI-generated content (54% of users) | 18% |
| Deleted some, added own pages (31% of users) | 42% |
| Deleted all AI content immediately (15% of users) | 35% |

**Exhibit 3 (reveal only if asked for qualitative/survey detail) — Exit/Lapsed-User Survey Snippets**

- "It felt like a demo, not my actual notes." 
- "I didn't really set anything up myself, so I forgot Notion existed."
- "The AI-made pages didn't match what I actually needed."

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Define/scope the metric (segment, definition, size of drop).
2. Map the user journey from signup → activation → ongoing engagement, and identify what changed at each stage.
3. Generate hypotheses (onboarding/product change, external factors, user-mix change, measurement artifact).
4. Use cohort/behavioral data to test and prioritize hypotheses.

**Correct core insight:** The new AI-generated onboarding raised surface-level activation (more people "have a populated workspace" on day 1) but actually undermines the behavior that predicts long-term retention: users personally building their workspace. Exhibit 2 shows this directly — the majority who passively keep AI-generated content (54% of users) retain far worse (18%) than the users who engage and personalize their space (42% and 35%). So activation and retention have been decoupled by the redesign: the new flow optimizes for a vanity/short-term metric (page exists) rather than the real driver (personal investment/ownership of content), which the qualitative data (Exhibit 3, "it felt like a demo") confirms.

**A strong final recommendation includes:**
- Redesign the AI onboarding step to prompt active customization rather than passive acceptance (e.g., AI drafts a starting point but requires the user to edit/confirm at least one page before finishing onboarding).
- Track and optimize for a better proxy activation metric (e.g., "% who personally edited a page in session 1") instead of just "workspace populated."
- Consider a lightweight prompt/nudge during week 1 for users who haven't touched their AI-generated content, to drive the personalization behavior that correlates with retention.
- Recommend an A/B test of the revised flow against the current one before a full rollout, using Week-4 retention (not just activation) as the success metric.

**Scoring anchors:**
- 5/5 insight generation: candidate identifies the activation/retention decoupling, requests and correctly interprets Exhibit 2's behavioral cut as the causal story (not just a correlation to note), and designs a fix that targets personalization behavior specifically.
- 3/5: candidate notices the onboarding change and the retention drop but doesn't connect it to the specific behavioral mechanism (content ownership) shown in Exhibit 2.
- 1/5: candidate never asks about the onboarding change, or treats the volume increase (a secondary factor) as the main story.
