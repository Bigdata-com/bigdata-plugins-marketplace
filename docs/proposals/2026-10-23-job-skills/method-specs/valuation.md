# Valuation discipline (enterprise DCF and its special cases)

Purpose: answer "what is one share worth under stated assumptions" and "what must be true for the current price to be right". Used by valuation, memo, earnings and scenario jobs. Every assumption is visible, cash flow is tied to growth and returns, and the result is a range. No recommendation.

## Inputs
- Reported (tearsheet, 5 fiscal periods per call): statements, PPE gross and net, invested capital, capex, leases, stock-based compensation, net debt, market cap, EV, price performance with 52-week range.
- Reported (filings via search and fetch_document): tax, pension, option and RSU notes, restricted and overseas cash, share count, minorities, litigation and restructuring accruals.
- Consensus (estimates, to FY+4): sales, EBIT, EBITDA, capex, FCF, long-term growth. Treat as biased upward (McKinsey ch.5: one-year-out S&P 500 earnings forecasts exceeded actuals by 10 points or more).
- Assumed: WACC. No field exists. Build it from a risk-free rate in the currency of the cash flows, equity risk premium, relevered peer beta, after-tax cost of debt and target market weights (McKinsey ch.11; DCF1 pp.49-64). GAP: Bigdata.com supplies none of these inputs; state source and date of each.
- GAP: the notes give no RSU procedure or worked stock-compensation adjustment (DCF2 p.17 names two effects only: awards outstanding and awards still to be granted). State the chosen treatment.

## Procedure
1. Rebuild history. Compute EBITA (operating profit before acquired-intangible amortisation), invested capital (operating working capital + net PPE + intangibles; exclude excess cash) and ROIC on average capital, with and without goodwill, for at least five years (McKinsey ch.7-8). Done: ROIC history split into margin and turnover.
2. Set tax. Apply an operating tax rate to EBITA, built from the tax note after removing one-offs and the interest shield; never the levered effective or statutory rate (McKinsey ch.25; DCF1 pp.26-32). The interest tax shield appears once, in WACC. Done: operating tax rate with derivation.
3. Set the horizon by time to maturity, length of competitive advantage and visibility, not by habit of 5 or 10 years (DCF1 pp.21-22). McKinsey (ch.9) uses 10 to 15 years. Fade growth to the terminal rate, at or below the economy's, by the last year. Done: horizon, reasons, growth path.
4. Forecast reinvestment consistently. Forecast capex bottom-up, not as a fixed share of revenue; depreciate each capex vintage over its asset life (waterfall); net capex = change in net PPE + depreciation (DCF1 pp.32-39; McKinsey ch.7). Done: capex, depreciation, net investment per year.
5. Check every forecast year: ROIC, ROIC = NOPAT margin x invested-capital turnover, and implied growth = ROIC x reinvestment rate against forecast growth. Flag sharp turnover rises (DCF2 pp.23-24: 1.2x to 3.0x in five years) and negative implied capex (McKinsey ch.9). Done: table, no unexplained jumps.
6. Compute continuing value with the formula below. Discount from the end of the last explicit year, not one year later (McKinsey ch.10). Done: RONIC, g, WACC stated with reasons.
7. Test the terminal value: share of EV, and implied terminal EV/EBITDA against today's multiple. Done: both reported.
8. Build the bridge, item by item, each also per share (DCF2 p.28). Deduct only non-equity claims captured in EV; add only equity claims not in EV (MULT p.28). Items: all liquid securities, not only "cash and equivalents"; working-capital cash (2 to 4 percent of revenue, verify) and restricted cash if in the cash line; overseas cash net of repatriation tax; debt at fair value if rates moved; pension deficit after tax; leases only if cash flows were lease-adjusted; minorities at market value; non-core stakes; unpaid restructuring and litigation at present value; options and RSUs; diluted share count from filings, not aggregators (DCF2 pp.5-17; McKinsey ch.12). Do not use diluted shares if options were deducted at option value. Done: bridge table.
9. Show sensitivity: WACC against terminal growth on value per share, base case in the centre (DCF2 pp.32-38).
10. Run base, downside and upside through the whole model, with second-order effects on reinvestment, growth and margin (DCF2 pp.39-51). Done: three outputs, probabilities, what must be true for each.
11. Benchmark per-share value against the price and 52-week range; explain the gap in economic terms (McKinsey ch.13: assume the market is right unless there is a specific reason). Solve for the growth the price implies (McKinsey ch.3).

## Formulas
- Value driver: Value = NOPAT(t+1) x (1 - g/RONIC) / (WACC - g). NOPAT = operating profit after tax; g = long-run growth; RONIC = return on new invested capital (McKinsey ch.2, p.39). Check: NOPAT 100, g 5%, WACC 10%: RONIC 10% gives 1,000; 20% gives 1,500.
- Continuing value at year t: CV(t) = NOPAT(t+1) x (1 - g/RONIC) / (WACC - g). If RONIC = WACC, CV = NOPAT(t+1) / WACC and growth adds nothing (McKinsey ch.10, p.215).
- Growth identity: g = RONIC x (net investment / NOPAT); FCF = NOPAT - net investment.
- Economic profit = invested capital x (ROIC - WACC); value = invested capital + PV of future economic profit (McKinsey ch.6).
- WACC = D/V x kd x (1 - tax) + E/V x ke, market weights (McKinsey ch.6, p.114). Cost of equity = risk-free + beta x equity risk premium.
- Mid-year adjustment: multiply PV by (1 + WACC)^0.5 (McKinsey ch.6). Price-target roll-forward: value x (1 + r) - distributions per share, r = discount rate (DCF1 pp.72-76).
- Unlevered beta = levered beta / (1 + D/E); relever at target D/E (McKinsey ch.11).
- Bank continuing value: NI(t+1) x (1 - g/RONE) / (ke - g); if RONE = ROE, P/B = (ROE - g) / (ke - g) (McKinsey ch.36, p.782). RONE = return on new equity.
- Scenario equity = max(scenario EV - claims, 0), then probability-weight. Do not deduct face-value debt from probability-weighted EV; do not average inputs (McKinsey ch.12-13).

## Reference tables
| Item | Guidance | Source |
|---|---|---|
| PV split, 5-year explicit | visible 20 to 30%, terminal 70 to 80% | DCF2 p.27 (rule of thumb, not statistic) |
| PV split, 10-year explicit | visible 40 to 50%, terminal 50 to 60% | DCF2 p.27 |
| Terminal share, book examples | 56 to 125% of value | McKinsey 2010 ch.10 |
| Implied terminal multiple | below today's; at or above signals an issue or a very strong story | DCF2 pp.29-31 |
| ROIC persistence, 10 years from 1995 | start above 20%: 67% stay above 20%; start below 10%: 57% stay below 10% | McKinsey 2010 ch.4 (verify) |
| ROIC reversion | top quintile 29% to 15% in 15 years | McKinsey 2010 ch.4 |
| Growth | median real 5.4%; top-quintile edge under 5 points by year 5, under 2 by year 10 | McKinsey 2010 ch.5 (verify) |
| Precision | WACC +0.5 point is about -10% value at forward P/E 15 to 16; aim for a range of plus or minus 15% | McKinsey 2010 ch.13 |

## Interpretation rules
- A large terminal share does not mean value arises after the forecast; check value by business component and economic profit (McKinsey ch.10).
- RONIC = WACC is not a default. For durable advantages set RONIC near the later-year ROIC with modest growth.
- Banks: no enterprise DCF. Use equity DCF at cost of equity, and P/B against ROE (P/B above 1 needs ROE above cost of equity). Interest is operating, so there is no net debt (McKinsey ch.36).
- Cyclicals: normalise to mid-cycle revenue and margin before any multiple or terminal value; weight a normal-cycle case against a new-trend case. 
- High growth (organic growth above 15% a year): start from a steady state 10 to 15 years out, size the addressable market, cap share with a saturated analogue, use medians of analogues not means, work backwards, weight scenarios (McKinsey ch.34).
- Emerging markets: scenario DCF at a global-investor cost of capital with no country premium, with at least a business-as-usual and a crisis case. If a country premium is used, apply it only to promised cash flows, never to probability-weighted ones. Local risk-free = (1 + US rate)(1 + local inflation)/(1 + US inflation) - 1 (McKinsey ch.33). GAP: no current crisis probabilities (book: about 20%, verify).
- Multi-business companies: value each unit on its own ROIC, growth and WACC, remove intercompany sales, value overhead as a negative unit. Sum of parts is valid only with peers of similar performance (McKinsey ch.13, 19).
- Distressed companies: do not deduct market value of debt; use scenarios with equity floored at zero (McKinsey ch.12).

## Output lines
- Price, 52-week range (reported). Operating tax rate (derived). Horizon and reasons (judgment).
- Revenue growth, margin, ROIC and turnover: first and last forecast year (assumed), with consensus (reported).
- Terminal g, RONIC, WACC (assumed), each with reason and source date.
- PV explicit, PV terminal, terminal share of EV, implied terminal EV/EBITDA against current (derived).
- EV, then each bridge item per share, then equity value per share (derived), share count source (reported).
- Value per share against price, as a premium or discount (derived).
- WACC by g table (derived). Scenario table: three values, probabilities (assumed, summing to 100%), expected value, what must be true (judgment).
- Balance of evidence and what would change it. No rating.

## Sources
Notes: mckinsey-part1.md, mckinsey-part2.md, expectations-multiples-dcf.md. Underlying: McKinsey, Valuation, 5th ed. (2010); Robinson and Weyns, UBS, "When DCF valuation goes rogue" Episodes I and II (2017) (DCF1, DCF2) and "How to analyse and talk the language of multiples" (2017) (MULT).
