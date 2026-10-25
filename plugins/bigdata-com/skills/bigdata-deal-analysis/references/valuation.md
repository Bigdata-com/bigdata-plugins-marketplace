# Valuation

This method answers two questions: what one share is worth under stated assumptions, and what must be true for the current price to be right. It uses an enterprise DCF in which cash flow is tied to growth and returns, so no forecast can grow without the investment that growth needs, and it ends in a range with probabilities, never a point or a price target. Most DCFs fail from inconsistency rather than arithmetic: reinvestment that does not support growth, unchecked ROIC, a dominant terminal value, a careless equity bridge, mismatched currency and inflation (Robinson and Weyns, DCF Episode I, 2017, p. 5). The method is built to catch those.

## When a skill loads this file

Valuation, deep dives, memos, scenarios, earnings reviews that revise value, and any job that states what the price implies. Load `references/roic.md` (NOPAT, invested capital, cost of capital inputs), `references/multiples-and-peers.md` (cross-check) and `references/expectations.md` (reverse DCF). A narrow question ("what growth does the price imply") gets steps 1, 3 and 12 only.

## Inputs

| Input | Where in Bigdata.com | Basis |
|---|---|---|
| Statements, PP&E gross and net, invested capital, capex, leases, stock-based compensation, net debt, market cap, EV | `bigdata_company_tearsheet`, `financial_statements`, `financial_ratios`, `key_metrics`; five periods per call, `interval` annual for fiscal years | reported |
| Price, 52-week range, performance | `company_overview` | reported |
| Consensus sales, EBIT, EBITDA, capex, FCF, long-term growth to four years out, with vintage | `analyst_estimates` | reported |
| Tax, pension, option and RSU notes; restricted and overseas cash; share count; minorities; litigation and restructuring accruals | `bigdata_search`, `bigdata_fetch_document` on filings | reported |
| Risk-free rate, equity risk premium, beta, credit spread, target weights | Not in Bigdata.com | assumed, each with source and date |

Treat consensus as biased upward: one-year-out S&P 500 earnings forecasts exceeded actuals by 10 points or more (McKinsey ch. 5). Not in the sources: any Bigdata.com field for cost of capital inputs; state each one's source and date.

## Procedure

1. **Rebuild history.** At least five years: EBITA, operating working capital, invested capital without excess cash, ROIC on average capital with and without goodwill, split into margin and turnover (McKinsey ch. 7-8; method in `references/roic.md`). Historicals should be continuing, core and controlled (DCF I, pp. 13-25). Done when the ROIC history table exists.
2. **Set the operating tax rate** on EBITA from the tax note, excluding one-offs and the interest shield; never the levered effective or the statutory rate. The interest shield lives once, in WACC (McKinsey ch. 25; DCF I, pp. 26-32). Done when the rate and its derivation are shown.
3. **Build the cost of capital.** Risk-free: 10-year government yield in the currency of the cash flows, not of the domicile, never a bill. Equity risk premium: name the source and date (an implied premium is preferred). Beta: 60 monthly returns against a broad index, or the peer median unlevered beta relevered to the target structure; show the standard error. Cost of debt: yield to maturity on long-term debt for investment grade; below investment grade the yield overstates the expected cost, so use APV. Weights: target market values. Show prevailing and normalized WACC, each labelled. Check: cost of equity above cost of debt; risk premium above the credit spread (McKinsey ch. 11; Mauboussin and Callahan, Cost of Capital, 2013, pp. 7-26; DCF I, pp. 48-71). Done when every input has a source and date.
4. **Set the horizon** by time to maturity, length of competitive advantage and visibility, not by habit (DCF I, pp. 21-22). McKinsey uses 10 to 15 years, with 5 to 7 in detail (ch. 9). Fade growth to the terminal rate, at or below the economy's, by the last year. Done when horizon, reasons and growth path are stated.
5. **Forecast revenue and margins.** Spend most time on revenue: bound it top-down (market x share) and bottom-up (customers), and check it against base rates (`references/base-rates.md`). Build price, volume and currency multiplicatively: (1.04)(1.12)(0.95) - 1 = 10.7 percent, not 11.0 (DCF I, pp. 13-25). Forecast costs as ratios to drivers, not growth rates. Done when every line has a driver.
6. **Forecast reinvestment consistently.** Capex bottom-up, not a fixed share of revenue; depreciation by vintage over asset lives; capex = change in net PP&E + depreciation, and net investment = capex - depreciation = change in net PP&E; never use change in gross PP&E (DCF I, pp. 32-39; McKinsey ch. 7). Done when capex, depreciation and net investment are shown per year.
7. **Check every forecast year.** ROIC = NOPAT margin x capital turnover, and implied growth = ROIC x reinvestment rate against forecast growth. Flag a turnover jump (1.2x to 3.0x in five years in DCF Episode II, pp. 23-24) and any negative implied capex (McKinsey ch. 9). Done when the table shows no unexplained jump.
8. **Compute the continuing value** with the value driver formula. Base it on normalized NOPAT (mid-cycle revenue and margin). Set RONIC from the moat evidence: WACC for most companies, near the later-year ROIC for durable advantages, with modest growth. Discount from the end of the last explicit year, not one year later (McKinsey ch. 10). Done when g, RONIC and WACC are stated with reasons.
9. **Test the continuing value.** Report its share of EV and the implied terminal EV/EBITDA against today's; the terminal multiple should be lower (DCF II, pp. 26-31). Done when both are reported.
10. **Bridge to equity, item by item, each also per share** (DCF II, p. 28). Deduct only non-equity claims captured in EV; add only equity claims not in EV (Multiples, p. 28). Items: all liquid securities, not only cash; less operating cash (2 percent of sales for steady companies, 5 percent for less predictable or faster-growing ones; Mauboussin and Callahan 2014, pp. 6-7; McKinsey ch. 7); restricted cash if it sat in the cash line; overseas cash net of repatriation tax; debt at fair value if rates moved; pension deficit after tax; leases only if cash flows were lease-adjusted; minorities and non-core stakes at market value; unpaid restructuring and litigation at present value; options and RSUs. Count shares from filings, not aggregators. Do not divide by diluted shares if options were deducted at option value (DCF II, pp. 5-17; McKinsey ch. 12). Done when the bridge table is complete.
11. **Show sensitivity and scenarios.** A WACC by terminal growth table on value per share, base case in the center (DCF II, pp. 32-38). Base, downside and upside run through the whole model with second-order effects on reinvestment and margin (pp. 39-51), with probabilities that sum to 100 and weights from `references/forecasting-discipline.md`. Average the values, not the inputs. Done when three values, probabilities and what must be true for each are shown.
12. **Benchmark against the price.** Compare value per share with the price and 52-week range and explain any gap in economic terms; assume the market is right unless there is a specific reason (McKinsey ch. 13). Solve for the growth and ROIC the price implies (McKinsey ch. 3; `references/expectations.md`). Done when the gap and the implied expectations are stated.

## Formulas

- Value driver: value = NOPAT(t+1) x (1 - g / RONIC) / (WACC - g). Check: NOPAT 100, g 5 percent, WACC 10 percent gives 1,000 at RONIC 10 percent and 1,500 at 20 percent (McKinsey ch. 2).
- Continuing value CV(t) = NOPAT(t+1) x (1 - g / RONIC) / (WACC - g); at RONIC = WACC, CV = NOPAT(t+1) / WACC (McKinsey ch. 10).
- g = RONIC x net investment / NOPAT; FCF = NOPAT - net investment.
- Economic profit = invested capital x (ROIC - WACC); value = invested capital + PV of future economic profit (McKinsey ch. 6).
- WACC = D/V x kd x (1 - Tm) + E/V x ke; ke = rf + beta x ERP. Unlevered beta = levered beta / (1 + D/E), relevered at target D/E (McKinsey ch. 11); `references/roic.md` gives the version with tax.
- Mid-year: multiply PV by (1 + WACC)^0.5. Price roll-forward: value x (1 + r) - distributions per share (DCF I, pp. 72-76).
- Scenario equity = max(scenario EV - claims, 0), then probability-weight (McKinsey ch. 12-13).

## Error catalogue

| Error | Fix | Source |
|---|---|---|
| Horizon too short or arbitrary | Set by maturity and advantage period; three stages when growth is high | DCF I, pp. 21-22 |
| Terminal value dominates | Report PV split and implied terminal multiple | DCF II, pp. 26-31 |
| Terminal value as FCF x (1 + g) / (WACC - g) with unrelated g | Value driver formula with RONIC | DCF I, pp. 40-45 |
| Capex as a share of revenue; depreciation forced to capex | Bottom-up capex; vintage depreciation | DCF I, pp. 32-39 |
| ROIC unchecked | ROIC, turnover and implied growth each year | DCF II, pp. 20-26 |
| Interest shield counted twice | Operating tax on EBITA; shield only in WACC | DCF I, pp. 26-32 |
| Cash or JV income counted twice | Net-debt or gross-debt approach, not both; JV income out of FCFF, stake in bridge | DCF I, pp. 17-18, 66-68 |
| Cash flow and discount rate mismatched | FCFF at WACC; FCFE at levered cost of equity | DCF I, pp. 22, 65-66 |
| Currency or inflation mismatched | Risk-free in the cash-flow currency; nominal with nominal | DCF I, pp. 49-53 |
| Beta or premium unchecked | Read R-squared and standard error; sector beta; implied premium | DCF I, pp. 48-71 |
| Bridge or share count wrong | Tick-box bridge; shares from filings | DCF II, pp. 5-17 |
| Stock compensation counted twice or not at all | Past awards in the bridge or share count; future awards in the forecast | DCF II, p. 17 |
| Single point | Sensitivity and three scenarios | DCF II, pp. 32-51 |
| Not benchmarked | Price and 52-week range | DCF II, pp. 28-29 |
| Naive base-year extrapolation | Hold working capital at a constant share of revenue | McKinsey ch. 10 |

## Reference tables

| Item | Guidance | Source |
|---|---|---|
| PV split, 5-year explicit | visible 20 to 30 percent, terminal 70 to 80 | DCF II, p. 27 (rule of thumb) |
| PV split, 10-year explicit | visible 40 to 50 percent, terminal 50 to 60 | DCF II, p. 27 (rule of thumb) |
| Terminal share in book examples | 56 to 125 percent of value | McKinsey ch. 10 |
| ROIC persistence, 1995 to 2005 | above 20 percent: 67 percent stay above 20; below 10 percent: 57 percent stay below 10 | McKinsey ch. 4 (verify) |
| Growth | median real revenue growth 5.4 percent (1965-2007); top-quintile edge under 5 points by year 5, under 2 by year 10 | McKinsey ch. 5 (verify) |
| Precision | WACC +0.5 point is about -10 percent value at a forward P/E of 15 to 16; aim for plus or minus 15 percent | McKinsey ch. 13 |

## Special cases

- **Banks.** No enterprise DCF and no net debt: interest is operating. Value cash flow to equity at the cost of equity, CFE = net income - increase in book equity + other comprehensive income, with equity growth set by the capital ratio (Tier 1 or CET1 on risk-weighted assets). CV = NI(t+1) x (1 - g / RONE) / (ke - g); if RONE = ROE, P/B = (ROE - g) / (ke - g), so P/B above 1 needs ROE above ke. Let ke move with leverage and asset mix. Model through-the-cycle loan losses by category and test reserve adequacy. Forecast margins from forward rates. Split net interest income into economic spread, maturity-mismatch and matched-maturity charges; a one-point change in loan rates moved the book's example bank's ROE by about 12 points (McKinsey ch. 36). Use scenarios.
- **Cyclicals.** Perfect-foresight DCF values are nearly flat while cash flows swing; consensus tends to ignore the cycle. Build a normal-cycle scenario with CV on mid-cycle profit and ROIC and a new-trend scenario extrapolating recent results, give each an economic rationale (demand, capacity, entry and exit), and weight them. Market prices fit a 50/50 blend of perfect and zero foresight (McKinsey ch. 35).
- **High growth** (organic revenue growth above 15 percent a year). Begin with the future: size the addressable market, cap share using an early saturated market, set long-run margin and capital intensity from mature analogues, work back to today and weight scenarios. Compare the revenue ramp with the median, not the mean, of analogues; negative invested capital makes ROIC meaningless and expensed marketing and technology overstate early returns (McKinsey ch. 34). The book's example weights three scenarios 20/50/30 for an expected $751m; calibrate weights to growth base rates.
- **Emerging markets.** Primary: scenario DCF with at least a business-as-usual and a crisis case at a global-investor cost of capital with no country premium. A country premium applies only to promised cash flows, never to probability-weighted ones: mixing double counts risk. Local risk-free = (1 + US rf) x (1 + local inflation) / (1 + US inflation) - 1 (1.04 x 1.048 / 1.001 - 1 = 8.9 percent for Brazil, 2009). Global beta and premium; cost of debt = dollar rf + systematic spread + inflation differential. Triangulate with multiples, since prices are weaker anchors (McKinsey ch. 33). Twenty emerging economies saw a real GDP fall above 5 percent about once every five years (book period, verify).
- **Multi-business companies.** Value each unit on its own ROIC, growth and WACC (peer unlevered beta relevered to the unit's structure); eliminate intercompany sales; value corporate costs as a negative unit; reconcile unit NOPAT and capital to the consolidated totals. A blended multiple matches none of the units (ConsumerCo: 8.5x, 5.9x and 11.2x units, 8.8x combined). Sum of the parts is valid only with peers of similar performance (McKinsey ch. 13, 19).
- **Distressed.** Do not deduct the market value of debt. For each scenario, equity = max(EV - face value of claims, 0), then weight: EV of 1,500 or 900 at 50/50 against debt of 1,200 gives equity of 150 (McKinsey ch. 12).
- **Inflation and currency.** Inflation in the cash flows matches inflation in the discount rate; translation gains are not cash flow; never use the parent's WACC for a subsidiary's local-currency cash flows (McKinsey ch. 29-30).

## Interpretation and limits

- A large terminal share does not mean value arises after the forecast; check value by business component and economic profit (McKinsey ch. 10).
- RONIC = WACC is not a default haircut, and RONIC above WACC needs modest growth. Uncertainty belongs in scenarios, not in a higher discount rate or a haircut (McKinsey ch. 2, 10).
- Exit multiples taken from today's market or a deal are circular (McKinsey ch. 10).
- Not in the sources: a procedure for RSUs and stock compensation beyond the two effects named (DCF II, p. 17). State the treatment and do not count an award both as an expense in FCF and in the share count.
- Not in the sources: current crisis probabilities for emerging markets (the book's frequency is about one in five years). State the probability used and its basis.

## Output lines

- Price and 52-week range. Basis: reported.
- Operating tax rate with derivation. Basis: derived.
- Horizon and reasons. Basis: judgment.
- Revenue growth, margin, ROIC and turnover for the first and last forecast years, with consensus beside them. Basis: assumed; consensus reported.
- Terminal g, RONIC and WACC, each with reason and source date. Basis: assumed.
- PV of the explicit period, PV of the continuing value, terminal share of EV, implied terminal EV/EBITDA against today's. Basis: derived.
- EV, each bridge item per share, equity value per share, share count source. Basis: derived; share count reported.
- Value per share against price, as a premium or discount. Basis: derived.
- WACC by growth table. Basis: derived.
- Scenario table: three values, probabilities summing to 100 with their source, expected value, what must be true. Basis: assumed, judgment.
- "At the current price the market implies [growth] at [ROIC] for [years]." Basis: derived.
- Balance of evidence and what would change it. No rating, no target. Basis: judgment.

## Sources

- Notes: McKinsey, Valuation, 5th ed. (chapters 2 to 13, sections 3 and 4); McKinsey, Valuation, 5th ed. (chapters 19, 25, 29, 30, 33 to 36, sections 3 and 4); Mauboussin, Expectations Investing; Robinson and Weyns, UBS multiples and DCF papers (2017) (sections 2.3, 3.1, 3.2, 6).
- Koller, T., Goedhart, M. and Wessels, D., Valuation, 5th ed., McKinsey, 2010, chapters 2 to 13, 19, 25, 29, 30, 33 to 36.
- Robinson, D. and Weyns, G., "When DCF valuation goes rogue", Episode I (6 Sep 2017, pp. 5-88) and Episode II (25 Sep 2017, pp. 4-52), UBS (cited as DCF I and DCF II); "How to analyse and talk the language of multiples", UBS, Mar 2017, p. 28.
- Mauboussin, M. and Callahan, D., "Estimating the Cost of Capital", Credit Suisse, 8 Oct 2013, pp. 7-26.

<!-- Spec vs notes: no numeric conflicts. The emerging-market crisis frequency is quoted as the book states it (a fall of more than 5 percent in real GDP about once in five years); the spec's "about 20%" is the same figure expressed as a probability. -->
