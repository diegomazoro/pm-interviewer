*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 56 — Meta: A Marketplace Test That Looks Too Good (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Facebook Marketplace. Your team tested a new 'Recommended for you' section that shows buyers more items they might like. In the test, buyers sent 10% more messages to sellers than the control group. The team wants to launch it to everyone. Your director asks whether we can trust this result. How would you evaluate it?"

**Objective (private reference, reveal only if asked directly):** Determine whether the test result reflects real value and would hold at full launch.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "What's the goal of Marketplace?" | Successful local transactions: buyers and sellers actually completing sales. | On request -- key framing fact |
| 2 | "How was the test randomized?" | Buyers were randomly split 50/50. Sellers weren't split -- every seller could receive messages from both groups. | On request -- key fact |
| 3 | "Did completed sales go up?" | Reveal Exhibit 1 once asked about completed sales or outcomes. | On request |
| 4 | "How did sellers react?" | Reveal Exhibit 2 once asked about sellers. | On request |
| 5 | "Were control buyers affected?" | Reveal Exhibit 3 once asked about the control group over time. | On request |
| 6 | "How long did the test run?" | Three weeks. | On request |
| 7 | "Which items do recommendations show?" | Mostly popular, well-priced items that many buyers like. | On request |

**Guardrail reminder:** Do not mention interference, seller capacity, or that both groups share sellers unless asked -- the candidate should question the test design on their own.

---

## C. Exhibits / data

**Exhibit 1 — Outcomes per 1,000 Buyers (3 weeks)**

| Metric | Control | Test |
|---|---|---|
| Messages to sellers | 1,000 | 1,100 |
| Completed sales | 120 | 124 |

**Exhibit 2 — Seller Side (sellers of recommended items)**

| Metric | Before test | During test |
|---|---|---|
| Messages received per listing | 6 | 14 |
| Share of messages that get a reply | 72% | 51% |
| Items marked sold within 48 hours of listing | 31% | 46% |

**Exhibit 3 — Control Group Over Time**

| Metric | Week before test | During test |
|---|---|---|
| Control buyers: completed sales per 1,000 buyers | 128 | 120 |
| Control buyers: "item already sold" replies | 9% | 17% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Start from the goal (completed sales), not messages.
2. Check the experiment design in a two-sided marketplace: shared sellers mean the groups interact.
3. Look at seller capacity and effects on control buyers.
4. Decide and propose a better test design.

**Correct core insight:** The test overstates the benefit. Buyers in both groups compete for the same sellers' items. Recommendations push test buyers toward popular items, which sell faster -- so control buyers increasingly find items already sold (9% to 17%) and their sales fall (128 to 120). The test vs. control gap partly comes from test buyers taking sales from control buyers, not creating new ones. Messages are up 10%, but completed sales only 3% vs. a depressed control, and sellers are overloaded (reply rate 72% to 51%).

**Quantitative reasoning a strong candidate shows:**
- Sales lift vs. control: 124 vs. 120 = +3%, not +10%.
- Against the pre-test baseline (128), test buyers' 124 is actually lower -- the true overall effect may be about zero or negative.

**A strong final recommendation includes:**
- Don't launch based on this test; messages is the wrong success metric.
- Re-run with a design that avoids interference: randomize by geographic area (local markets), so test and control don't share sellers.
- Primary metric: completed sales; guardrails: seller reply rate, "already sold" rate, buyer satisfaction.
- Consider spreading recommendations across more items so demand doesn't pile on a few sellers.

**Scoring anchors:**
- 5/5 insight generation: identifies interference from shared sellers, uses control-group decline and seller overload as evidence, computes the real sales effect, and proposes geo randomization.
- 3/5: switches to completed sales and notices seller overload, but misses interference.
- 1/5: recommends launching because messages went up 10%.
