*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 46 — OpenAI: Mobile Usage Drop in Japan (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at OpenAI working on the ChatGPT mobile app. Over the last four weeks, daily active users of the mobile app in Japan have dropped 12%, while every other major market kept growing. Web usage in Japan looks normal. Your Head of Product wants to know why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the drop in mobile daily active users in Japan and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is a daily active user defined?" | A user who sends at least one message in the mobile app that day. | On request |
| 2 | "Is the drop sudden or gradual?" | Sudden -- it started within two days, about four weeks ago. | On request |
| 3 | "Did we release an app update around then?" | Yes, a new version of the app was released for both iOS and Android about four weeks ago, with a redesigned message composer. | On request -- key fact |
| 4 | "Is it iOS, Android, or both?" | Reveal Exhibit 1 once asked for a breakdown by platform. | On request |
| 5 | "Did anything change in Japan specifically -- competitors, news, pricing?" | No pricing changes or major news; a local competitor had a normal month. | On request -- rules out external causes |
| 6 | "Is there anything unusual in how people use the app now?" | Reveal Exhibit 2 once asked about behavior changes, message patterns, or session data. | On request |
| 7 | "What do Japanese users say in app reviews?" | Reveal Exhibit 3 once asked about reviews or feedback. | On request |
| 8 | "How do Japanese users type?" | Most use a Japanese keyboard where you type sounds and press Enter to confirm converting them into characters before you finish the sentence. | Reveal only if asked about typing or keyboard input |

**Guardrail reminder:** Do not connect the new composer, Japanese keyboard input, and the Enter key for the candidate -- let them find the mechanism from the data.

---

## C. Exhibits / data

**Exhibit 1 — Daily Active Users Change in Japan (last 4 weeks)**

| Platform | Change |
|---|---|
| iOS | -19% |
| Android | -2% |
| Web | +3% |

**Exhibit 2 — Message Patterns in Japan, iOS (before vs. after update)**

| Metric | Before | After |
|---|---|---|
| Share of messages under 5 characters | 4% | 23% |
| Share of messages deleted or edited within 10 seconds | 2% | 15% |
| Sessions ending within 30 seconds of first message | 8% | 21% |

**Exhibit 3 — App Store Reviews in Japan (last 4 weeks, sample themes)**

- "It sends my message before I finish typing!"
- "Unusable since the update."
- "I have to type in another app and paste."

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Clarify the metric and timing (sudden -> look for a specific change).
2. Rule out external causes; focus on the app update.
3. Segment by platform and look at behavior.
4. Identify the mechanism and recommend a fix plus prevention.

**Correct core insight:** The redesigned composer on iOS sends the message when the user presses Enter -- but Japanese keyboard users press Enter to confirm character conversion mid-sentence. So messages get sent half-written (short messages up from 4% to 23%, quick edits and deletes up), users get frustrated and leave (iOS -19%, while Android, which handles this differently, is barely affected). It's a localization bug in the input handling, not a demand problem.

**A strong final recommendation includes:**
- Hotfix: don't send on Enter while the keyboard is composing characters (respect the input composition state); consider a send button only for these languages.
- Communicate the fix to users in Japan.
- Check other languages with similar keyboards (Chinese, Korean).
- Prevention: add input-method tests to the release checklist; monitor key markets by platform after releases.
- Metrics: short-message share, DAU recovery in Japan iOS.

**Scoring anchors:**
- 5/5 insight generation: uses timing and platform split, finds the half-sent messages, connects them to Japanese keyboard input, and recommends a fix and prevention.
- 3/5: finds that the update caused it on iOS but not the mechanism.
- 1/5: blames competition or seasonality without examining the update.
