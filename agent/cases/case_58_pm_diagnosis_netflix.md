*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 58 — Netflix: Early Cancellations Rising in Mexico (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Netflix, responsible for new member experience in Latin America. In Mexico, the share of new members who cancel within their first 30 days has risen from 12% to 19% over the last two months. Other Latin American countries look stable. Your Head of Product wants to know why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the rise in 30-day cancellations among new members in Mexico and recommend a response.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is early cancellation measured?" | Share of new members in a given week who cancel within 30 days of signing up. | On request |
| 2 | "Did prices or plans change in Mexico?" | No price or plan changes in the last six months. | On request -- rules out pricing |
| 3 | "Did the content catalog change?" | No major titles left the catalog; new releases were on a normal schedule. | On request |
| 4 | "Did the number of new members change?" | Yes -- new signups in Mexico rose about 70% over the same two months. | On request -- key fact |
| 5 | "Where are the new members coming from?" | Reveal Exhibit 1 once asked about acquisition channels or where signups come from. | On request |
| 6 | "Is cancellation different by channel?" | Reveal Exhibit 2 once asked for cancellation by channel or segment. | On request |
| 7 | "How do these new members use Netflix?" | Reveal Exhibit 3 once asked about viewing behavior. | On request |
| 8 | "Did we start any partnerships?" | Yes -- two months ago Netflix started a partnership with a mobile carrier that offers Netflix free for the first month with certain phone plans, then charges it on the phone bill. | On request |

**Guardrail reminder:** Do not connect the carrier partnership, the channel mix, and the cancellation rate for the candidate -- let them find it through the exhibits.

---

## C. Exhibits / data

**Exhibit 1 — New Members by Channel, Mexico (monthly)**

| Channel | Before partnership | Last 2 months |
|---|---|---|
| Direct signups | 100,000 | 100,000 |
| Carrier partnership | 0 | 70,000 |

**Exhibit 2 — 30-Day Cancellation by Channel**

| Channel | 30-day cancellation |
|---|---|
| Direct signups | 12% |
| Carrier partnership | 29% |

**Exhibit 3 — First-Week Viewing (hours)**

| Channel | Median hours watched in first week |
|---|---|
| Direct signups | 6.5 |
| Carrier partnership | 1.0 |
| Carrier members who never activated a profile | 38% of carrier members |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the metric; rule out price and content.
2. Notice the signup surge and look at the channel mix.
3. Compare cancellation by channel (mix shift vs. real deterioration).
4. Diagnose why carrier members cancel and recommend fixes.

**Correct core insight:** Nothing got worse for direct members (still 12%). The overall rate rose because of a mix shift: the carrier partnership added 70,000 members a month who cancel at 29%. Many of them never really started using Netflix (38% never activated a profile, median 1 hour in week one) -- they got it "free" with their phone plan, not because they chose it.

**Quantitative reasoning a strong candidate shows:**
- Blended rate: (100,000 x 12% + 70,000 x 29%) / 170,000 = (12,000 + 20,300) / 170,000 = about 19%.
- Even with high cancellation, the partnership adds about 70,000 x 71% = about 50,000 retained members a month.

**A strong final recommendation includes:**
- Report cancellation by channel; don't treat the blended rise as a product problem.
- Improve onboarding for carrier members: activation reminders through the carrier, simple profile setup, personalized first recommendations.
- Work with the carrier on targeting (offer it to customers likely to watch) and messaging before the first charge.
- Evaluate the partnership on retained members and lifetime value, not on the blended cancellation rate.

**Scoring anchors:**
- 5/5 insight generation: identifies the mix shift, computes the blended rate, sees direct members are unchanged, and focuses on carrier activation.
- 3/5: blames the partnership but doesn't show the mix math or recognize the partnership's net value.
- 1/5: assumes content or price issues without segmenting by channel.
