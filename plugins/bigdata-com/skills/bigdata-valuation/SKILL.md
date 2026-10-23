---
name: bigdata-valuation
description: >
  What a company is worth, from Bigdata.com fundamentals and estimates: the growth, margin and return the price implies, a reinvestment-consistent DCF with the terminal value and the equity bridge checked, cross-checked with multiples, and given as a range with the assumptions and sensitivities. Use when the user asks what a stock is worth, whether it is cheap or expensive, for a DCF, a fair value, or what is priced in. Not for peer multiples alone, which bigdata-comps covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, valuation, multiples-and-peers, base-rates, roic, forecasting-discipline
  bigdata-sector-primer: auto
---

# Valuation

This skill writes the valuation a portfolio manager would sign off on: what the price already assumes, stated first and without judgment, then an enterprise DCF in which growth is paid for by reinvestment, returns are checked every year, the continuing value is tested against its share of the total and the multiple it implies, and the equity bridge is shown per share. It ends in a range with three probability-weighted cases and a sensitivity table, cross-checked with peer multiples, never in a point or a price target. It is sized to the question: "what growth does the price imply for Micron?" gets the reverse DCF with its arithmetic and the base-rate sentence, not the full model.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-valuation"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Establish three things before gathering data: what the user wants (a full valuation range, only what the price implies, or one input such as the cost of capital or the terminal value), the currency of the cash flows (which sets the risk-free rate), and the type of business, because a bank, an insurer, a deep cyclical, a company growing above 15 percent a year, an emerging-market company and a multi-business company each need the special case below. The valuation date is today and the price is the latest close in the tearsheet.

Ask one question only when the answer changes the work: the name resolves to more than one listing, or the user seems to hold a cost-of-capital or horizon assumption they want used. Otherwise state the assumptions in the Assumptions line and proceed.

If `find_securities` returns the company as Private, say there is no price to read expectations from and no consensus to anchor on. Offer a DCF from whatever statements the tearsheet carries, without the price-implied and benchmark steps, or hand off to `bigdata` for a document-based profile.

## Gather

Work through these in order. Each step says what it must produce.

1. **Tearsheet, in several calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, events_calendar`; then `fundamentals`, then `fundamentals` again with the period control set to the five years before, if the tool allows it; then `estimates`; then `revenue_segmentation`. Done when the price and 52-week range, market cap, the EV field, ten years of statements (or five, noted in Gaps), invested capital, capex, gross and net PP&E, stock-based compensation, consensus to four years out with its vintage and estimate counts, and five years of segments are in hand.
2. **The annual filing notes.** `bigdata_search` in fast mode for the latest annual report with the reporting period filter, then `bigdata_fetch_document`. Read the tax reconciliation, the lease note, the pension note, the option and RSU tables, minorities and equity-method stakes, restricted and overseas cash, litigation and restructuring accruals, debt maturities and fair value, and the share count on the cover page. Done when each bridge item has a figure with its page, or is marked not disclosed.
3. **Management's plan.** The last earnings call by fast search with the reporting period filter, then fetch. Done when guidance, the capex plan and any medium-term targets are quoted verbatim with the call date. Management targets are opinions, recorded as such.
4. **Evidence for the horizon and the terminal return.** Two or three `bigdata_search` calls, one aspect each: market growth and the company's share, pricing in the industry, entrants and exits. Done when the length of the competitive advantage and the return on new investment after it have at least one dated piece of evidence each.
5. **Peers for the cross-check.** `bigdata_screen_companies` on the industry and size, then `bigdata_company_tearsheet` with `fundamentals, estimates` for four to eight peers chosen by value drivers. Done when each peer's EV inputs, forward EBITA or the sector's multiple base, ROIC and consensus growth are in hand.
6. **Cost-of-capital inputs.** Not in Bigdata.com, except where `bigdata_country_tearsheet` carries the government bond yield and inflation for the currency of the cash flows; take them from there with the date, labelled reported. The equity risk premium, beta and target weights are assumed, each with its source and date. If `bigdata_computer` can return a monthly price series, compute beta from 60 monthly returns against a broad index.
7. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read it for the metrics, the accounting traps and the valuation convention before analysing.

## Analyse

Each step names the reference file it loads and ends in what it must produce.

1. **What the price implies.** Load `references/expectations.md` and run steps 1 to 5. Build EV from market cap and net debt, adding minorities, preferred, the pension deficit and leases when the EV field leaves them out. NOPAT1 is consensus EBIT for the next fiscal year at the operating tax rate. Solve g = (EV x WACC - NOPAT1) / (EV - NOPAT1 / ROIIC) at a stated ROIIC, and the implied competitive advantage period with formula 3a; split EV into steady-state value and future value creation; place the forward P/E against 1 / cost of equity. Then place the implied growth in its size and horizon class with `references/base-rates.md`, converting real to nominal. Done when the report can say "the price needs X percent NOPAT growth at Y percent ROIIC, which Z percent of companies in the A to B size class achieved" with every input labelled.

2. **Rebuild history.** Load `references/roic.md` and run steps 1 to 11: the definition line; NOPAT on EBITA at the operating tax rate from the tax note, never the effective or statutory rate, because the interest shield is counted once, in WACC; invested capital built from the operating and the financing side and reconciled; excess cash stripped at 2 percent of sales for steady companies and 5 percent for less predictable ones; ROIC with and without goodwill on average capital; ROIC split into margin times turnover; ROIIC over three and five years. Historicals are continuing, core and controlled (`references/valuation.md` step 1). Done when the history table exists and the FactSet ROIC field is compared in one line, never mixed into the same table.

3. **Cost of capital.** From `references/valuation.md` step 3 and the input table in `references/roic.md`: the 10-year government yield in the currency of the cash flows, never a bill; a named equity risk premium with its date (an implied premium is preferred); beta from 60 monthly returns or the peer median unlevered beta relevered to the target structure, naming the unlevering formula used; the cost of debt at the yield on long-term debt for investment grade; target market-value weights. Show prevailing and normalized WACC, each labelled assumed. Check that the cost of equity exceeds the cost of debt and the risk premium exceeds the credit spread. Done when every input has a source and a date and a range of at least plus and minus 1 point is carried to the sensitivity.

4. **Horizon.** From `references/valuation.md` step 4: set the explicit period by time to maturity, the length of the competitive advantage and visibility, not by habit; 10 to 15 years with 5 to 7 in detail is the McKinsey practice, and a three-stage model is used when growth is high. Bound the advantage period with the reversion table in `references/roic.md` (company advantage against sector barriers) and the market-implied period in `references/expectations.md` table 2 (about 8 years on average, about 5 in competitive industries to about 15 in stable ones, 1976 to 2007, verify). Done when the horizon, its reasons and the growth path fading to the terminal rate are stated.

5. **Revenue and margins.** From `references/valuation.md` step 5: spend most of the time on revenue, bound it top-down (market times share) and bottom-up (customers times revenue per customer), build price, volume and currency multiplicatively, and forecast costs as ratios to their drivers. Treat consensus as biased upward. Every growth and margin figure gets its base rate from `references/base-rates.md`: growth by size class and horizon with the share that achieved it, beyond three years blended toward the class median; margins faded toward the sector mean with the horizon-matched r (expected = mean + r x (current - mean)). Done when every line has a driver and every growth or margin claim carries its base-rate sentence with sample and period.

6. **Reinvestment.** From `references/valuation.md` step 6: capex bottom-up, not a share of revenue; depreciation by vintage over asset lives; net capex = change in net PP&E + depreciation, never the change in gross PP&E; working capital at a constant share of revenue unless there is a reason; future stock awards in the forecast as a cost. Done when capex, depreciation and net investment are shown for each year.

7. **Check every forecast year.** From `references/valuation.md` step 7: ROIC = NOPAT margin x capital turnover, and implied growth = ROIC x reinvestment rate against the forecast growth. Flag any jump in turnover and any year with negative implied capex. Done when the year-by-year table shows ROIC, turnover and implied against forecast growth with no unexplained jump.

8. **Continuing value.** From `references/valuation.md` step 8: CV = NOPAT(t+1) x (1 - g / RONIC) / (WACC - g) on normalized, mid-cycle NOPAT, with g at or below the economy's nominal growth. RONIC equals WACC for most companies; near the later-year ROIC only where the moat evidence from Gather step 4 supports a durable advantage, and then with modest growth. Discount from the end of the last explicit year. Uncertainty goes into the cases, not into a higher discount rate or a haircut. Done when g, RONIC and WACC are stated with reasons.

9. **Test the continuing value.** From `references/valuation.md` step 9 and formula 5 in `references/expectations.md`: report the terminal share of EV against the UBS rule of thumb (70 to 80 percent for a 5-year explicit period, 50 to 60 percent for 10 years; a rule of thumb, not a statistic) and the implied terminal EV/EBITDA against today's. The terminal multiple should be below today's because multiples fall as a company matures; at or above it, find the error or name the story that justifies it. Done when both figures are reported and any breach is explained.

10. **Bridge to equity, per share.** From `references/valuation.md` step 10: all liquid securities less operating cash (2 to 4 percent of revenue, a rating-agency rule of thumb, verify); restricted cash only if it sat in the cash line; overseas cash net of repatriation tax; debt at fair value if rates moved; the pension deficit after tax; leases only if the cash flows were lease-adjusted; minorities and non-core stakes at market value; unpaid restructuring and litigation at present value; options and RSUs. Count shares from the filing, not an aggregator, and do not divide by diluted shares if options were deducted at value. Done when the bridge table shows every item in total and per share.

11. **Sensitivity.** From `references/valuation.md` step 11: a WACC by terminal growth table of value per share with the base case in the center, and a row or column for RONIC where the continuing value dominates. Done when the table is complete and a reader can see how far value moves for half a point of WACC.

12. **Three cases.** Base, downside and upside run through the whole model with second-order effects on reinvestment and margin, as `references/valuation.md` step 11 requires, with probabilities from `references/forecasting-discipline.md` steps 3 and 4: integers that sum to 100, each anchored to a reference-class share from `references/base-rates.md`, never a default split. Equity in each case is max(EV - claims, 0). Average the values, not the inputs. Done when three values, their probabilities with the source of each weight, what must be true in each, the expected value and the loss case are shown.

13. **Multiples cross-check.** Load `references/multiples-and-peers.md` and run steps 1 to 5 and 8 to 10 for one multiple: EV built the same way for the company and each peer, the metric cleaned, the forward EV/EBITA (or the sector's base) with the peer median shown with and without the outlier, the justified multiple from EV / EBITA = (1 - T) x (1 - g / ROIC) / (WACC - g), and the multiples the DCF implies. Done when the DCF-implied multiple, the peer median and the justified multiple sit side by side and any gap is explained by a driver.

14. **Benchmark and range.** From `references/valuation.md` step 12: compare the value range and the expected value with the price and the 52-week range, and explain any gap in economic terms. Assume the market is right unless there is a specific reason it is not, and say what that reason is. Aim for a precision of about plus or minus 15 percent; a half-point change in WACC is about a 10 percent change in value at a forward P/E of 15 to 16. Done when the range, the expected value, the gap to the price and the implied expectations from step 1 are stated together.

A narrow question gets steps 1, 3 and 14 (what the price implies, at a stated cost of capital, against the price), with the arithmetic shown.

Special cases, from `references/valuation.md`:

- **Bank or insurer.** No enterprise DCF and no net debt, because interest is operating. Value cash flow to equity at the cost of equity: CFE = net income - increase in book equity + other comprehensive income, with equity growth set by the capital ratio. CV = NI(t+1) x (1 - g / RONE) / (ke - g); P/B = (ROE - g) / (ke - g), so a premium to book needs ROE above ke. Model through-the-cycle loan losses and forecast margins from forward rates. The cross-check is P/B against ROE, not EV multiples.
- **Cyclical.** Build a normal-cycle case with the continuing value on mid-cycle profit and ROIC and a new-trend case that extrapolates recent results, each with an economic rationale (demand, capacity, entry and exit), and weight them. Show the mid-cycle margin next to the consensus margin.
- **High growth** (organic revenue growth above 15 percent a year). Start from the future: size the addressable market, cap share from an analogous saturated market, set the long-run margin and capital intensity from mature analogues, then work back to today. Compare the revenue ramp with the median of analogues. Negative invested capital makes ROIC meaningless; say so and use margins and capital intensity instead.
- **Emerging market.** Scenario DCF with at least a business-as-usual and a crisis case at a global-investor cost of capital with no country premium; a country premium applies only to promised cash flows, never to probability-weighted ones. Local risk-free = (1 + US rf) x (1 + local inflation) / (1 + US inflation) - 1. Triangulate with multiples.
- **Multi-business.** Value each unit on its own ROIC, growth and WACC, value corporate costs as a negative unit, and reconcile unit NOPAT and capital to the consolidated totals. A blended multiple matches none of the units.
- **Distressed.** Do not deduct the market value of debt. In each case, equity = max(EV - face value of claims, 0), then weight.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) valuation, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.

## The valuation
Four to eight sentences: what the price implies and how rare that is against base rates, the value
range and the expected value against the price, the one or two assumptions the value turns on, and
what would change the reading. No rating, no target.

## What the price implies
| Measure | Value | Basis | Source |
EV and its build, NOPAT1, cost of capital and range, implied growth at the stated ROIIC, implied
competitive advantage period, steady-state share of EV, P/E against steady-state P/E, base-rate share.

## Assumptions
| Input | Value | Range | Reason | Source and date | Basis |
Risk-free, equity risk premium, beta, cost of debt, weights, WACC prevailing and normalized,
operating tax rate, horizon, terminal g, RONIC.

## History
| FY | Revenue | EBITA margin | Turnover | ROIC ex goodwill | ROIC with goodwill | ROIIC | Basis | Source |
Definition line under the table. FactSet ROIC compared in one line.

## Forecast
| Year | Revenue growth | Consensus | Base rate | EBITA margin | Net investment | ROIC | Turnover |
| Implied growth (ROIC x reinvestment) | FCF | Basis |
First years, a fade year and the last year at minimum.

## Continuing value and checks
Formula with g, RONIC and WACC; PV of explicit period and of CV; terminal share against the rule
of thumb; implied terminal EV/EBITDA against today's.

## Equity bridge
| Item | Amount | Per share | Basis | Source |
Ending in equity value per share and the share count source.

## Sensitivity
WACC rows by terminal growth columns, value per share, base case in the center.

## Cases
| Case | What must be true | Value per share | Probability | Weight anchor | Basis |
Expected value; loss case next to gain case.

## Multiples cross-check
| Measure | Company | Peer median (ex outlier) | Justified | DCF-implied | Basis |

## Range against the price
Value range, expected value, price and 52-week range, the gap explained in economic terms.

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. Offer a spreadsheet-style table export or a Word document when the host can create files. For a narrow question, answer it in the method's terms with the relevant table and the sources, and keep the footer.

## Checks before sending

1. "What the price implies" comes before the forecast, and the summary reads consistently with it.
2. Every cost-of-capital input has a source and a date, and the risk-free rate is in the currency of the cash flows.
3. NOPAT uses the operating tax rate from the tax note, and the interest shield appears only in WACC.
4. ROIC, turnover and implied growth are shown for every forecast year, with no unexplained jump and no negative implied capex.
5. The continuing value uses the value-driver formula with a stated RONIC, its share of EV is reported, and the implied terminal multiple is below today's or the reason is given.
6. The bridge lists every item per share, and the share count comes from a filing.
7. The WACC by growth table is present, with the base case in the center.
8. Case probabilities are integers that sum to 100, each anchored to a named reference class; the expected value averages values, not inputs.
9. Each growth and margin claim carries a base-rate sentence with sample and period; dated figures carry "(verify)".
10. The output is a range and an expected value. No price target, no buy, hold or sell, no rating word.
11. The special case was applied if the company is a bank, insurer, cyclical, high-growth, emerging-market, multi-business or distressed company.

## Hand-offs

- The user wants peer multiples on their own: `bigdata-comps`. The cases built out with signposts: `bigdata-scenarios`. The view and the claims behind it: `bigdata-thesis`.
- The company reports soon and the user wants the setup: `bigdata-earnings-preview`.
- After delivering, make one offer: save the valuation to the user's Bigdata.com account so later searches can find it. Act only on a clear yes.
