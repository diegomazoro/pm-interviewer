*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 18 — Stripe: Helping Small Merchants Handle Disputes (PM Product Sense Case)

**Case type:** product_sense

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager at Stripe. When a customer disputes a card payment -- a chargeback -- the merchant has a limited window to respond with evidence, or they automatically lose the money plus a dispute fee. Large merchants have dedicated teams for this, but small businesses on Stripe tend to find disputes confusing and stressful, and most of them lose. How would you design a better experience to help small merchants deal with disputes?"

**Objective (private reference, reveal only if asked directly):** Design an approach that helps small merchants handle disputes better, with a clear target user, a concrete MVP, a view on tradeoffs, and defined success metrics.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Who counts as a 'small merchant' here?" | Businesses processing under roughly $1M a year on Stripe, usually with no dedicated finance or operations staff -- the founder or one generalist handles disputes when they come up. | On request |
| 2 | "How does the dispute process work today for these merchants?" | Stripe emails the merchant and shows the dispute in the Dashboard. The merchant has 7 to 21 days, depending on the card network, to upload evidence (receipts, shipping proof, customer communication) in a form, after which the card issuer decides. | On request |
| 3 | "How often do small merchants get disputes?" | Most get very few -- the median small merchant sees 2 to 3 disputes a year -- so they rarely build familiarity with the process. A minority in higher-risk categories (digital goods, travel, subscriptions) get them monthly. | On request |
| 4 | "What's the main reason small merchants lose?" | Reveal Exhibit 1 once the candidate asks why merchants lose or asks for data on dispute outcomes. | On request |
| 5 | "What are the most common dispute reasons?" | "Product not received" and "fraudulent / unrecognized charge" together make up about two-thirds of small-merchant disputes; "subscription canceled" and "product not as described" make up most of the rest. | On request |
| 6 | "What does Stripe gain if merchants win more disputes?" | Merchants who lose disputes churn at noticeably higher rates and contact support more; dispute handling is also a frequent reason small merchants say they'd consider a competitor that "takes care of it for them." | On request -- business context |
| 7 | "Are there constraints from the card networks?" | Yes -- evidence must be specific to the transaction, and card networks discourage generic or templated submissions; the issuer ultimately decides, not Stripe. | On request |
| 8 | "Is there any data on what merchants do once a dispute arrives?" | Reveal Exhibit 2 once the candidate asks about merchant behavior during disputes. | On request |
| 9 | "What do competitors offer?" | Some payment providers offer paid "chargeback protection" that covers the loss for a fee; others offer no special help. | On request |

**Guardrail reminder:** Do not tell the candidate which merchant segment, dispute reason, or solution type (prevention, response tooling, automation, insurance-style protection) to focus on, and do not confirm whether automating evidence submission is a good idea -- those are the decisions the candidate needs to make and defend.

**Solution-gated follow-up (deliver once, verbatim, only after the candidate proposes a concrete initial solution/direction -- not before):** "Interesting -- one thing that complicates this: in an internal pilot, automatically drafting the evidence response for merchants raised the share of disputes that got a response from 22% to 71%, but the win rate on those auto-drafted responses was only 18%, compared with 41% for responses merchants wrote themselves, and one card network flagged the volume of low-quality submissions."

---

## C. Exhibits / data

**Exhibit 1 — Small-Merchant Dispute Outcomes (last 12 months)**

| Outcome | Share of disputes |
|---|---|
| Merchant never responded (automatic loss) | 78% |
| Merchant responded and won | 9% |
| Merchant responded and lost | 13% |

Win rate among merchants who responded: 41%.

**Exhibit 2 — Merchant Behavior After a Dispute Notification (survey + product data)**

| Signal | Value |
|---|---|
| Merchants who opened the dispute in the Dashboard | 64% |
| Merchants who started the evidence form | 35% |
| Merchants who submitted the evidence form | 22% |
| Top reason given for not responding (survey) | "Didn't know what evidence to provide" (47%) |
| Second reason | "Not worth my time for the amount" (31%) |
| Median disputed amount for small merchants | $85 |

---

## D. Model answer / "what good looks like"

**Strong problem framing:** clarifies the goal (merchant recovery of funds vs. merchant retention vs. reducing dispute volume) and picks a specific segment -- e.g. low-frequency small merchants selling physical goods, whose main gap is not knowing what evidence to provide -- rather than "all small merchants." Uses Exhibit 2 to locate the drop-off: most merchants see the dispute but abandon the form.

**Product taste:** goes beyond "make the form simpler." Strong ideas include guided, reason-specific evidence checklists ("for 'product not received,' upload tracking showing delivery"), automatically pulling evidence Stripe already has (shipping tracking, customer email, IP/device match, prior successful purchases by the same card), a triage view telling the merchant whether a dispute is worth fighting, and prevention (clearer statement descriptors, receipts, and refund-before-dispute nudges). An ambitious option: Stripe pre-fills transaction-specific evidence and the merchant reviews and adds context, rather than fully automatic submission.

**Prioritization & tradeoffs:** states an MVP -- e.g. guided checklists plus pre-filled evidence for the two biggest dispute reasons -- and explicitly leaves out things like insurance-style protection or full automation for v1, with reasons (cost, network rules, quality).

**Business judgment & metrics:** ties it to merchant retention and support load, and to Stripe's relationship with card networks. Primary metric: dispute win rate (or funds recovered) per dispute received, not just response rate. Guardrails: win rate among responded disputes, network quality flags, merchant time spent.

**Composure under the follow-up:** the twist shows that maximizing response rate through full automation backfires -- more responses, lower quality, network risk. A strong candidate adjusts: keep the merchant in the loop (Stripe drafts, merchant confirms and adds specifics), only auto-submit where Stripe has strong transaction-specific evidence, and shift the success metric from "responses submitted" to "disputes won." A weak candidate either ignores the twist or abandons automation entirely without reasoning.

**Scoring anchors:**
- 5/5 overall: specific segment grounded in Exhibit 2's drop-off, a concrete MVP with stated exclusions, metrics centered on wins rather than submissions, and a thoughtful adaptation to the twist.
- 3/5: reasonable ideas (simpler form, templates) but generic segment, no clear MVP boundary, or metrics limited to response rate.
- 1/5: jumps straight to "Stripe should auto-respond to everything" or "offer chargeback insurance" without understanding why merchants lose, and doesn't adapt after the twist.
