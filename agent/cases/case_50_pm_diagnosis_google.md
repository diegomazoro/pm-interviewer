*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 50 — Google: Fewer User Reviews on Maps (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager on Google Maps. Over the last two months, the number of new reviews users write for places -- restaurants, shops, and so on -- has dropped 25%. Visits to places, measured by navigation and searches, are flat. Reviews are important because they keep place information fresh and useful. Your Head of Product wants to understand why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the drop in new reviews and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How do most reviews get written?" | About 70% of reviews come from a notification after a visit ("How was your visit to X?"); the rest from people opening a place page on their own. | On request -- key fact |
| 2 | "Is the drop gradual or sudden?" | Gradual -- it has grown week by week over the two months. | On request |
| 3 | "Is it Android, iOS, or both?" | Reveal Exhibit 1 once asked for a breakdown by platform. | On request |
| 4 | "Did we change anything in the review flow or notifications?" | No changes to the review flow or notification content. | On request |
| 5 | "Did anything change in the phones or operating system?" | Reveal Exhibit 2 once asked about devices, OS versions, or permissions. | On request |
| 6 | "Is there a pattern between new and old devices?" | Reveal Exhibit 3 once asked about new vs. old devices or users. | On request |
| 7 | "Could this be spam filtering removing reviews?" | No -- the spam filter removal rate is unchanged. | On request -- rules out filtering |
| 8 | "Is review quality or length different?" | No meaningful change in review length or rating distribution. | On request |

**Guardrail reminder:** Do not connect notification permissions, new devices, and the review drop for the candidate -- let them request the exhibits and find the mechanism.

---

## C. Exhibits / data

**Exhibit 1 — Change in New Reviews by Platform (last 2 months)**

| Platform | Change |
|---|---|
| Android | -33% |
| iOS | -4% |

**Exhibit 2 — Android Notification Permission**

A recent Android version requires apps to ask users for permission before sending notifications, instead of having it on by default. Over the last two months, a large wave of users upgraded to this version or bought new phones with it. Maps currently asks for this permission the first time it opens on the new version, with a generic system prompt.

| Metric | Value |
|---|---|
| Android users on the new version (now) | 65% (up from 15% two months ago) |
| Share of those who granted Maps notification permission | 15% |
| Share on older versions with notifications on | 92% |

**Exhibit 3 — Reviews per 1,000 Visits, Android**

| Group | Reviews per 1,000 visits |
|---|---|
| Users with notifications on | 12 |
| Users with notifications off | 3 |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify where reviews come from (mostly post-visit notifications).
2. Rule out demand (visits flat) and filtering.
3. Segment by platform and device; note the gradual shape (adoption of something).
4. Find the mechanism and recommend fixes.

**Correct core insight:** Most reviews depend on post-visit notifications. On the new Android version, notifications require permission, and only 15% grant it to Maps (vs. 92% having them on before). As more users upgrade (15% to 65%), fewer get the review prompt, and users without notifications write four times fewer reviews. This explains the gradual Android-only decline. It's a permission/distribution problem, not lower willingness to review.

**Quantitative reasoning a strong candidate shows:**
- Share of Android users with notifications on: before 0.15 x 15% + 0.85 x 92% = about 80%; now 0.65 x 15% + 0.35 x 92% = about 42%.
- Reviews per 1,000 visits: before 0.80 x 12 + 0.20 x 3 = 10.2; now 0.42 x 12 + 0.58 x 3 = 6.8 -- a drop of about a third, which matches the -33% on Android. More decline will come as adoption grows.

**A strong final recommendation includes:**
- Ask for notification permission at a meaningful moment with a clear explanation (e.g. after a trip, explaining what notifications are for), instead of on first launch.
- Add in-app review prompts (e.g. when opening Maps after a visit) for users without notifications.
- Track permission grant rate and reviews per visit by OS version.
- Expect further decline as adoption continues -- act soon.

**Scoring anchors:**
- 5/5 insight generation: links the review flow to notifications, finds the Android permission change, explains the gradual shape, quantifies, and recommends fixes.
- 3/5: finds it's Android-specific and permission-related but doesn't explain or quantify.
- 1/5: assumes users are less engaged or spam filtering changed without checking.
