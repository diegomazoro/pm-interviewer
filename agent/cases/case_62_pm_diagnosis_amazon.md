*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, features, or decisions at the named company.*

# Case File 62 — Amazon: Grocery Repeat Orders Dropping in One City (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager on Amazon's grocery delivery business. In Seattle, the share of customers who place a second grocery order within 30 days of their first has dropped from 55% to 44% over the last two months. Other cities look normal. Your director wants to know why and what to do. How would you approach this?"

**Objective (private reference, reveal only if asked directly):** Diagnose the drop in repeat grocery orders in Seattle and recommend a fix.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "Did prices, delivery fees, or promotions change in Seattle?" | No changes to prices, delivery fees, or promotions. | On request -- rules out pricing |
| 2 | "Did delivery times or reliability change?" | On-time delivery is stable at about 96%. | On request |
| 3 | "Did anything change operationally in Seattle?" | Two months ago a new fulfillment center opened in Seattle and took over about half of the city's grocery orders. | On request -- key fact |
| 4 | "Is the drop concentrated in certain customers or areas?" | Reveal Exhibit 1 once asked for a breakdown by area, fulfillment center, or customer type. | On request |
| 5 | "What do customers complain about?" | Reveal Exhibit 2 once asked about complaints, reviews, or feedback. | On request |
| 6 | "How are out-of-stock items handled?" | If an item is out of stock, the picker substitutes a similar item unless the customer opted out. | On request |
| 7 | "How does the new fulfillment center perform on stock and substitutions?" | Reveal Exhibit 3 once asked about inventory, stock levels, or substitutions. | On request |

**Guardrail reminder:** Do not connect the new fulfillment center, substitutions, and repeat orders for the candidate -- let them find the mechanism.

---

## C. Exhibits / data

**Exhibit 1 — 30-Day Repeat Rate by Fulfillment Center (Seattle)**

| Fulfillment center | Share of orders | Repeat rate |
|---|---|---|
| Existing center | 50% | 55% |
| New center | 50% | 33% |

**Exhibit 2 — Top Complaint Themes (Seattle, last 2 months)**

- "Half my order was substituted with things I didn't want."
- "I asked for organic milk and got regular."
- "Fresh produce was fine, but the substitutions ruined it."

**Exhibit 3 — Inventory and Substitutions**

| Metric | Existing center | New center |
|---|---|---|
| Items out of stock at picking time | 3% | 11% |
| Orders with at least one substitution | 6% | 18% |
| Customers rating substitutions as "acceptable" | 70% | 48% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Rule out price, fees, and delivery reliability.
2. Look for what changed in Seattle (new fulfillment center) and segment by it.
3. Use complaints and operational data to find the mechanism.
4. Recommend fixes and monitoring.

**Correct core insight:** The new fulfillment center has far more out-of-stock items (11% vs. 3%), so it substitutes in three times as many orders (18% vs. 6%), and those substitutions are worse (48% acceptable vs. 70%). First-time customers whose order came from the new center have a bad experience and don't return (33% vs. 55%). The existing center is unaffected.

**Quantitative reasoning a strong candidate shows:**
- Blended: 0.5 x 55% + 0.5 x 33% = 44% -- the new center explains the entire drop.

**A strong final recommendation includes:**
- Fix inventory at the new center (forecasting, stocking levels for top items) as the root cause.
- Short term: route first-time customers' orders to the existing center or to the center with the item in stock; improve substitution quality (customer preferences, ask before substituting).
- Win back affected customers (e.g. credit with an apology).
- Metrics: out-of-stock rate, substitution acceptance, repeat rate by center, especially for first orders.

**Scoring anchors:**
- 5/5 insight generation: segments by fulfillment center, finds the stock and substitution issue, shows the blended math, recommends root-cause and short-term fixes.
- 3/5: finds that substitutions are the issue but doesn't connect to the new center, or vice versa.
- 1/5: blames competition or pricing without segmenting.
