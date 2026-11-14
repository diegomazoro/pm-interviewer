*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 64 — Amazon: A Widget Everyone Clicks (PM Metrics & Experimentation Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a PM on Amazon's homepage. Your team tested a 'Buy it again' widget at the top of the homepage that shows items customers bought before. In the test, the widget was responsible for 8% of all orders, and the team reports it as one of the most successful homepage features ever. Your director asks whether it actually increased sales. How would you evaluate it?"

**Objective (private reference, reveal only if asked directly):** Determine whether the widget created new orders or just moved existing orders to a new entry point.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How was 'responsible for 8% of orders' measured?" | Orders where the customer clicked on the widget before buying. | On request |
| 2 | "Was there a control group?" | Yes -- customers were randomly split 50/50 for six weeks. | On request |
| 3 | "What happened to total orders per customer?" | Reveal Exhibit 1 once asked about total orders or comparing groups. | On request |
| 4 | "Where did orders come from in each group?" | Reveal Exhibit 2 once asked about the source of orders or other entry points. | On request |
| 5 | "What else is on the homepage?" | Personalized recommendations for new products and deals usually sit at the top; the widget pushed them down. | On request |
| 6 | "What's the goal of the homepage?" | Help customers find what they need and discover new products, growing total sales. | On request |

**Guardrail reminder:** Do not mention cannibalization or attribution -- the candidate should question the 8% on their own.

---

## C. Exhibits / data

**Exhibit 1 — Orders per Customer (6 weeks)**

| Metric | Control | Test |
|---|---|---|
| Orders per customer | 3.20 | 3.21 (difference not significant) |
| Sales per customer | $142 | $141 (not significant) |

**Exhibit 2 — Where Orders Came From**

| Entry point | Control | Test |
|---|---|---|
| Search | 52% | 47% |
| Order history ("Your orders" page) | 9% | 4% |
| Homepage recommendations for new products | 11% | 9% |
| "Buy it again" widget | -- | 8% |
| Other | 28% | 32% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Question attribution: "orders through the widget" isn't the same as "extra orders."
2. Compare total orders and sales between groups.
3. See where orders shifted from.
4. Decide based on total value and side effects.

**Correct core insight:** The widget didn't create new orders -- total orders (3.20 vs. 3.21) and sales ($142 vs. $141) didn't change. It moved existing repeat purchases from search and order history into the widget. It also pushed down recommendations for new products (11% to 9% of orders), which hurts discovery -- a long-term cost. The 8% is attribution, not incremental impact.

**Quantitative reasoning a strong candidate shows:**
- Orders shifted into the widget: search -5 points, order history -5 points, new-product recommendations -2 points.
- No significant change in total orders or sales.

**A strong final recommendation includes:**
- Don't report the widget as a big win; judge features on incremental sales vs. control, not attributed orders.
- Decide on convenience grounds: the widget may still save customers time (measure time to order), but consider placing it lower so it doesn't push down discovery.
- Metrics: total sales per customer, new-product discovery, time to complete repeat orders.

**Scoring anchors:**
- 5/5 insight generation: identifies attribution vs. incrementality, uses the control comparison, shows where orders came from, flags the discovery cost.
- 3/5: notices total orders didn't change but doesn't explain the shift or the discovery cost.
- 1/5: accepts the 8% as success.
