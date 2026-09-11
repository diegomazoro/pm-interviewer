*Note: this is a fictional practice scenario for interview training. It does not describe real events, data, or decisions at the named company.*

# Case File 16 — Mercado Libre: Active Buyer Growth Stalling in Two Markets (PM Diagnostic Case)

## A. Case prompt (read aloud to candidate at the start — nothing else revealed yet)

"You're a Product Manager on Mercado Libre's marketplace growth team. Monthly active buyers have kept growing in Brazil, Mexico, and Argentina, but in Colombia and Peru specifically, active buyer growth has stalled over the last two quarters -- even though overall online shopping demand in those two countries is still growing. Your VP of Growth wants to understand why, and what to do about it."

**Objective (private reference, reveal only if asked directly):** Diagnose why active buyer growth has stalled specifically in Colombia and Peru, and recommend a targeted response.

---

## B. Clarifying-question answer key

| # | Likely question | Answer | Reveal rule |
|---|---|---|---|
| 1 | "How is 'active buyer' defined?" | A unique user who completed at least one purchase in the trailing 30 days. | On request |
| 2 | "Has Mercado Libre changed its own pricing, fees, or app experience in Colombia/Peru recently?" | No major changes to fees, pricing, or the app itself in either country during this window. | On request |
| 3 | "Has overall online shopping demand in those countries actually slowed?" | No -- total e-commerce spend in both countries is still growing at roughly the same pace as before; it's specifically Mercado Libre's own active buyer count that's stalled. | On request — rules out a market-wide demand explanation |
| 4 | "Did marketing or promotional spend get cut in these countries?" | No, marketing spend in Colombia and Peru has stayed roughly flat quarter over quarter. | On request |
| 5 | "Has anything changed with shipping/delivery specifically in these two countries?" | No reported degradation in delivery times or logistics performance in Colombia or Peru during this window. | On request |
| 6 | "What does the competitive landscape look like there?" | Reveal Exhibit 1 once asked. | On request |
| 7 | "Is the stall concentrated in new buyers, returning buyers, or both?" | Reveal Exhibit 2 once asked. | On request — key diagnostic fact |
| 8 | "What kind of purchases do buyers in these countries typically make -- any difference from other markets?" | Reveal Exhibit 3 once asked. | On request — key diagnostic fact |

**Guardrail reminder:** Do not connect the competitive and price-point data for the candidate (e.g. do not say outright "Temu is winning your price-sensitive new buyers") -- let them request Exhibits 1-3 and draw that connection themselves.

---

## C. Exhibits / data

**Exhibit 1 — Shopping App Download Share by Country, Last Quarter**

| Country | Mercado Libre | Temu | Shein | Other |
|---|---|---|---|---|
| Brazil | 38% | 14% | 10% | 38% |
| Mexico | 34% | 18% | 12% | 36% |
| Argentina | 41% | 12% | 9% | 38% |
| Colombia | 22% | 31% | 19% | 28% |
| Peru | 20% | 29% | 17% | 34% |

**Exhibit 2 — Active Buyer Growth by Segment, Colombia & Peru, Year over Year**

| Segment | Growth |
|---|---|
| New buyers (first-ever purchase on Mercado Libre) | -18% |
| Returning buyers (previously active) | +3% |

**Exhibit 3 — Average Order Value & Category Mix (reveal if asked about price point or basket composition)**

| Metric | Colombia & Peru | Brazil, Mexico & Argentina |
|---|---|---|
| Average order value | $14 | $34 |
| Share of purchases in low-ticket categories (apparel accessories, phone cases, small home/electronics accessories, all under ~$15) | 62% | 31% |

---

## D. Model answer / "what good looks like"

**Framework a strong candidate should build:**
1. Scope the problem: confirm it's specific to Colombia/Peru and to Mercado Libre's own numbers, not a market-wide demand slowdown (question 3 rules this out).
2. Generate hypotheses: MELI-side changes (pricing, app, logistics), demand-side slowdown, or competitive share loss -- and systematically rule hypotheses out using the clarifying answers before requesting exhibits.
3. Segment the stalled metric (new vs. returning buyers) before assuming the whole funnel is broken.
4. Connect the competitive and basket-composition data to the segment finding rather than treating them as separate facts.

**Correct core insight:** The stall is concentrated entirely in new-buyer acquisition (-18% YoY) while returning buyers are stable-to-growing (+3%, Exhibit 2) -- existing loyal customers are unaffected. Colombia and Peru also show Mercado Libre losing far more app download share to Temu and Shein than in its stronger markets (Exhibit 1), and skew much more heavily toward the same low-ticket, price-sensitive categories (Exhibit 3) that Temu and Shein compete hardest on. Put together: new shoppers in these two markets are increasingly making their first purchase on Temu or Shein instead of Mercado Libre, specifically for the kind of low-ticket items that make up most of the demand there -- this is a new-buyer acquisition problem in a specific, price-sensitive segment, not a broad platform or demand problem.

**A strong final recommendation includes:**
- Avoid a blanket platform-wide price war (would erode margin on the much larger base of existing, unaffected buyers); instead target the specific new-buyer/low-ticket segment where share is actually being lost.
- Consider a narrowly-scoped response for Colombia/Peru: lower free-shipping thresholds or first-purchase incentives specifically on low-ticket categories, to compete for a new buyer's *first* purchase without discounting the whole marketplace.
- Recruit/support more local low-cost sellers in the specific vulnerable categories (Exhibit 3) so Mercado Libre is price-competitive on exactly the items new buyers are shopping for first.
- Propose tracking new-buyer acquisition and low-ticket category share specifically in these markets going forward, rather than only watching the blended active-buyer number, since it masked the real problem this time.

**Scoring anchors:**
- 5/5 insight generation: candidate isolates the new-buyer-only pattern (Exhibit 2), connects it to both the competitive share loss and the low-ticket basket skew (Exhibits 1 and 3), and proposes a targeted rather than platform-wide fix.
- 3/5: candidate identifies Temu/Shein competition as a factor but doesn't isolate that it's specifically a new-buyer, low-ticket problem, or proposes a broad price-matching response without weighing the margin trade-off.
- 1/5: candidate treats this as a generic "competitor is winning, cut prices" problem without requesting the segment or basket data at all.
