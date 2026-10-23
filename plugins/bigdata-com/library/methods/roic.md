# Return on invested capital

## Purpose

This method answers what the company earns on the capital its operations use, how that compares with its cost of capital, and where that return is heading. ROIC moves by a factor of two or more on definitions alone (Procter and Gamble 2006: 10.6 percent with goodwill in capital, 26.2 percent without; Damodaran 2007, pp. 43-45), so the method fixes each choice, states it, and applies it identically to peers. Starting ROIC is already in the price; a stock moves on changes in returns against expectations (Mauboussin and Callahan 2013, Economic Returns, pp. 2-7). The output is a definition line, a ROIC bridge, a spread over a stated cost of capital and a reasoned reversion path, never a rating.

## When a skill loads this file

Whenever a report states a return on capital, a spread, a moat or a fade assumption: deep dives, valuation, moat, earnings quality, capital allocation, thesis and sector work. A narrow question ("what is the ROIC") gets the definition line, ROIC with and without goodwill, the FactSet field and the spread, not the full bridge. Banks and insurers use adjusted ROE (see Interpretation and limits).

## Inputs

| Input | Where in Bigdata.com | Basis |
|---|---|---|
| Revenue, EBIT, amortization of acquired intangibles, pretax income, tax expense, interest expense and income, non-operating income, R&D | `bigdata_company_tearsheet`, section `fundamentals` (income statement), five fiscal periods per call | reported |
| Receivables, inventory, prepaid, payables, accruals, deferred revenue, net and gross PP&E, goodwill and intangibles, cash and securities, debt, lease liabilities where reported, equity, minority interest, invested capital field | `fundamentals` (balance sheet) | reported |
| FactSet ROIC, margins, cash conversion cycle | `fundamentals` (ratios) | reported |
| Revenue by segment | `revenue_segmentation` (revenue only, no segment capital) | reported |
| Tax reconciliation, lease note, deferred tax note, R&D, restructuring and impairment history, segment assets | `bigdata_search` on filings, then `bigdata_fetch_document` for the note | reported |
| Risk-free rate, equity risk premium, beta, credit spread, target weights | Not in Bigdata.com. Beta can be computed with `bigdata_computer` where it returns a price series; otherwise cite an industry beta | assumed |

For a ten-year series request earlier periods if the tool allows it; otherwise work with five and say so in Gaps.

## Procedure

1. **State the definition.** One line naming: tax method (operating or cash), average or opening capital, goodwill in or out, leases, R&D, the excess cash rule. Done when the line sits under every ROIC table and peers use the same line.
2. **Build NOPAT.** EBITA = EBIT plus amortization of acquired intangibles. Apply the operating tax rate from the tax reconciliation note: statutory plus state or local rate, plus recurring operating items (foreign rate differences, credits that scale with revenue), excluding one-offs and the interest tax shield (McKinsey ch. 7, 25). Never use reported tax or the effective rate: they contain the interest shield, which WACC already counts (Damodaran 2007, p. 8). Optional cash-tax row: subtract the increase in net operating deferred tax liabilities (Mauboussin and Callahan 2014, pp. 2-3). Done when NOPAT ties to the tax note and the rate is written down.
3. **Classify unusual items.** One-time: remove. Recurring at intervals (restructuring every three years): spread per year. Recurring but volatile: average. Recurring with sign flips (currency translation): ignore (Damodaran 2007, pp. 37-39). Count how many of the last five years carry a "one-time" charge; recurring ones are costs. Done when each item has a class.
4. **Build invested capital from the operating side.** Operating working capital (operating cash, receivables, inventory, prepaid, less payables, accruals, deferred revenue, taxes payable; no excess cash, no interest-bearing items) plus net PP&E plus goodwill and acquired intangibles plus other net operating assets (McKinsey ch. 7). Keep an item only if the company could not earn the same NOPAT without it (Mauboussin and Callahan 2014, p. 5). Done when every balance-sheet line is classed operating, non-operating or financing.
5. **Build it from the financing side and reconcile.** Debt plus lease liabilities plus unfunded pensions plus equity plus minority interest, less excess cash and non-operating assets. A gap between the two sides is a missed item. Compare with the tearsheet invested capital field. Done when the two sides agree or the difference is explained.
6. **Strip excess cash.** Operating cash allowance: 2 percent of sales for steady companies, 5 percent for less predictable or faster-growing ones (Mauboussin and Callahan 2014, pp. 6-7; McKinsey ch. 7 uses 2 percent). Remove the same amount from equity and keep interest on cash out of NOPAT. Done when the allowance and the amount removed are shown.
7. **Show ROIC with and without goodwill.** Without goodwill and acquired intangibles measures the operating business and is the basis for peer comparison; with them measures the return on all capital raised, premiums included (McKinsey ch. 8; Mauboussin and Callahan 2014, pp. 7-8). Add cumulative impairments and amortization back to goodwill. Judge an acquisition by its net present value, not by ROIC (Mauboussin and Callahan 2014, fn. 12). Done when both columns appear.
8. **Treat leases.** State whether the statements capitalize leases (ASC 842 and IFRS 16 put most leases on balance sheet from 2019; verify for the company and the period). If capitalized, add the implied interest (prior-year lease liability x pre-tax cost of secured debt) to EBITA and keep the liability in capital and in debt. For earlier periods, estimate the leased asset with the formula below. The WACC debt weight changes too. Done when ROIC is shown before and after.
9. **Capitalize R&D when it is material.** Advertising or customer acquisition only with evidence of a multi-year benefit (Damodaran 2007, pp. 27-28). Choose an amortizable life (pharma about 10 years, software short), build the research asset, replace R&D expense with amortization in EBITA and add the asset to capital. Operating taxes do not change because R&D is deductible in full (McKinsey ch. 28). Say so if the R&D history is shorter than the life. Done when the life and the adjusted ROIC are shown.
10. **Compute and decompose.** Headline ROIC on average of opening and closing capital (McKinsey ch. 8); show the opening-capital variant (Damodaran 2007, p. 7). Decompose into (1 - operating tax rate) x EBITA margin x capital turnover over five to ten years, with working capital in days. High margin points to a consumer advantage, high turnover to a production advantage (Mauboussin and Callahan 2014, pp. 12-14). Segment ROIC needs segment assets from the filing. Done when the series and the decomposition are tabled.
11. **Compute ROIIC, the cost of capital and the spread.** ROIIC over one, three and five years. WACC from the build in `references/valuation.md`, shown as prevailing and normalized, each labelled (Mauboussin and Callahan 2013, Cost of Capital, pp. 22-25). Economic profit in currency. Done when spread and economic profit sit next to ROIC for every year.
12. **Set the reversion path** with the fade table and persistence figures below, and give the reason from the competitive evidence in `references/industry-structure.md`. Done when the path names a starting spread, years, an endpoint and the reason.

## Formulas

- ROIC = NOPAT / average invested capital. NOPAT = EBITA x (1 - operating tax rate).
- Cash NOPAT = EBITA - (operating taxes - increase in net operating deferred tax liability).
- Economic profit = invested capital x (ROIC - WACC) = NOPAT - WACC x invested capital. Use one capital definition for both terms (McKinsey ch. 6).
- ROIC = (1 - t) x (EBITA / revenue) x (revenue / invested capital). Days of an item = 365 x item / revenue (inventory and payables on COGS).
- Growth identity: g = ROIC x investment rate; investment rate = net investment / NOPAT; FCF = NOPAT - net investment (McKinsey ch. 2).
- Value driver: value = NOPAT(t+1) x (1 - g / RONIC) / (WACC - g), RONIC = return on new invested capital (McKinsey ch. 2 and 10).
- ROIIC, one year = (NOPAT(t) - NOPAT(t-1)) / (IC(t-1) - IC(t-2)) (Mauboussin and Callahan 2014, p. 10). Rolling n-year form (derived): (NOPAT(t) - NOPAT(t-n)) / (IC(t-1) - IC(t-n-1)); use n = 3 and 5 when investment is lumpy.
- Research asset = sum over t = -(n-1) to 0 of R&D(t) x (n + t) / n, n = amortizable life; current-year R&D is unamortized. Adjusted EBIT = EBIT + R&D - amortization of the research asset (Damodaran 2007, p. 20).
- Leased asset value(t-1) = rental expense(t) / (kd + 1 / asset life); kd = cost of secured debt, asset life = PP&E / annual depreciation (McKinsey ch. 27).
- WACC = D/V x kd x (1 - Tm) + E/V x ke, target market-value weights; ke = rf + beta x ERP.
- Unlevered beta: beta_u = beta_L / [1 + (1 - T) x D/E] (Mauboussin and Callahan 2013, pp. 14-19); McKinsey's form without the tax term, beta_L = beta_u x (1 + D/E), assumes the tax shield carries operating risk (ch. 11). State which one is used. Adjusted beta = 0.67 x raw + 0.33.
- Expected value of a persistent metric in four years = sector mean + r x (current - sector mean), r = four-year persistence (Mauboussin, How to Model Reversion to the Mean, 2013).

## Reference tables

**Cost of capital inputs** (all assumed; fetch current values on the valuation date)

| Item | Rule or range | Source |
|---|---|---|
| Risk-free rate | 10-year government yield in the currency of the cash flows; never a bill | McKinsey ch. 11; Mauboussin and Callahan 2013, p. 18 |
| Equity risk premium | 4.5 to 5.5 percent (May 2009, verify); Damodaran implied 5.7 percent and Credit Suisse 4.5 percent (Oct 2013, verify); textbooks 3 to 10 percent | McKinsey ch. 11; Mauboussin and Callahan 2013, pp. 11-13 |
| Beta | 60 monthly returns against a broad value-weighted index, never a local index; industry median unlevered beta relevered to target D/E | McKinsey ch. 11 |
| Cost of equity, large non-financial companies | about 9 percent, range 8 to 10 percent (late 2009, verify) | McKinsey ch. 2 |
| Median cost of capital, US | about 8 percent (1963-2008) | McKinsey ch. 4 |

Checks: cost of equity above cost of debt; equity risk premium above the credit spread.

**ROIC level and persistence, US non-financial companies, ROIC without goodwill** (McKinsey ch. 4, Compustat, 5,000+ companies)

| Item | Figure | Period |
|---|---|---|
| Median ROIC | about 10 percent, annual medians 7 to 11 percent | 1963-2008 |
| Median ROIC, later years | about 17 percent | 2005-2008 |
| Top quintile (above 20 percent) | median falls from 29 to 15 percent over 15 years, not to 10 | 1963-2008 |
| Industry medians | pharma and biotech 23.5 percent; utilities 6.3 percent; commodities 5.8 percent | 1965-2007 |

Ten-year transition, 1995 to 2005 (rows sum to 100):

| Start | Below 10 percent | 10 to 20 percent | Above 20 percent |
|---|---|---|---|
| Below 10 percent | 57 | 28 | 15 |
| 10 to 20 percent | 25 | 40 | 35 |
| Above 20 percent | 19 | 14 | 67 |

**Four-year persistence of CFROI by sector** (HOLT, global, live and dead companies above about $250M market cap, 1983-2015; The Base Rate Book, 2016). CFROI is an inflation-adjusted, IRR-style return, not ROIC; use r as a guide to speed (higher r, slower reversion) and the median as a level guide only.

| Sector | 4-year r | Median CFROI, percent |
|---|---|---|
| Consumer staples | 0.78 | 8.1 |
| Consumer discretionary | 0.67 | 8.0 |
| Health care | 0.64 | 8.3 |
| Industrials | 0.62 | 6.7 |
| Utilities | 0.57 | 3.5 |
| Telecom services | 0.55 | 5.7 |
| Information technology | 0.50 | 8.5 |
| Financials | 0.43 | 7.5 |
| Materials | 0.41 | 4.6 |
| Energy | 0.35 | 5.0 |

All companies, ex financials and utilities: one-year r 0.78, four-year r 0.56.

**Reversion path by advantage** (Damodaran 2007, pp. 59-60, Table 12)

| Company advantage | Sector barriers | Near term | Later |
|---|---|---|---|
| Strong, sustainable | Strong | company ROIC | toward sector average |
| Strong, sustainable | Weak or none | company ROIC | toward cost of capital |
| Weak, slipping | Strong | toward sector average | sector average |
| Weak, slipping | Weak or none | toward cost of capital | cost of capital |

Near-term length follows the advantage's explicit life (a patent with six years left gives six years). Conventions: HOLT fades over five years, then removes 10 percent of the spread over the long-run average each year, then sets return to the cost of capital (a convention, not an empirical law). Mature companies have earned at most 2 to 3 points over their cost of capital over long periods; Damodaran uses this as a cap on perpetual excess return and the cost of capital as a floor (2007, p. 63).

**Size of definitional effects** (illustrations; dated, never current figures)

| Choice | Example | Source |
|---|---|---|
| Goodwill | Cisco FY2013: 125.4 percent without, 34.1 percent with | Mauboussin and Callahan 2014, pp. 7-8 |
| Leases | US retail 2006: 19.74 percent to 10.95 percent; Starbucks 2006 spread over WACC 15.09 to 5.38 points | Damodaran 2007, pp. 33-37 |
| Leases | Home Depot 2008: 9.2 percent to 8.0 percent | McKinsey ch. 7 |
| R&D | PharmaCo: 42 percent expensed, about 13 percent capitalized on an 8-year life | McKinsey ch. 28 |

## Interpretation and limits

- Two tests for advantage: ROIC above the cost of capital and above peers, over a full cycle (Mauboussin and Callahan 2014, pp. 12-14). Value needs the spread and the capital deployed at it, so judge economic profit, not ROIC alone.
- Show ROIC, ROIIC and RONIC for every forecast year. Forecast ROIC stays near today's level, trends to the industry median, or trends to WACC, with a stated reason (McKinsey ch. 9). Fading a top-quintile company to WACC is usually too conservative given the transition table; a recovery for a low-ROIC company needs a specific cause.
- Never compare ROIIC with WACC; a high ROIIC can be operating leverage. Use it to spot change: Dell's average ROIC stayed high while marginal returns swung widely (Damodaran 2007, p. 51).
- Flag ROIC lifted by write-offs that shrink capital (a $10bn asset earning $0.5bn is 5 percent; write off half and it reads 10 percent; Damodaran 2007, pp. 37-39). Buybacks lift ROE, not ROIC.
- Flag any jump in capital turnover and any forecast that implies negative capex (McKinsey ch. 9, 13).
- Never put the FactSet ROIC field and a hand-built ROIC in one comparison; name which one each line quotes. Apply identical adjustments to every peer.
- Does not apply to banks and insurers: use ROE on adjusted net income against the cost of equity, decomposed with leverage (Mauboussin and Callahan 2014, p. 11). Captive finance arms: separate them and use ROE on allocated equity; a blended figure is meaningless (McKinsey ch. 7, 12). Negative NOPAT or negative invested capital: ROIC is meaningless; use the high-growth case in `references/valuation.md`. Cyclicals: use three to five year averages. High inflation: nominal ROIC rises mechanically (McKinsey ch. 29).
- Not in the sources: the FactSet ROIC definition (tax rate, goodwill, leases, average or year-end capital). Test it against the hand-built figure.
- Not in the sources: a fitted speed of ROIC reversion by sector. The persistence figures are for CFROI; state the r used and that it is a proxy.
- Not in the sources: amortizable R&D lives by industry beyond pharma (about 10 years) and software (short). State the life as an assumption and show one alternative.

## Output lines

- "ROIC ([definition line]) is X percent without goodwill and Y percent with goodwill in FY[n]; the FactSet field shows Z percent." Basis: derived; FactSet field reported.
- "NOPAT uses an operating tax rate of t percent, built from the tax note [n]." Basis: derived.
- "Capitalizing leases moves ROIC from A to B percent; capitalizing R&D on an N-year life moves it to C percent." Basis: derived, with life assumed.
- "ROIC is a margin of M percent times turnover of T times; the change since FY[n] came from [margin or turnover]." Basis: derived.
- "ROIIC over three and five years is A and B percent." Basis: derived.
- "WACC is W percent prevailing and V percent normalized (risk-free, ERP, beta and weights stated with sources and dates)." Basis: assumed.
- "Spread S points; economic profit of [currency amount] in FY[n]." Basis: derived.
- "Reversion path: from S points to E over N years, because [competitive evidence]; the sector's four-year CFROI persistence is r (HOLT, 1983-2015)." Basis: judgment, with the base rate reported.

## Sources

- Damodaran, A., "Return on Capital (ROC), Return on Invested Capital (ROIC) and Return on Equity (ROE): Measurement and Implications", July 2007, pp. 3-65.
- Mauboussin, M. and Callahan, D., "Calculating Return on Invested Capital", Credit Suisse, 4 June 2014, pp. 1-15.
- Mauboussin, M. and Callahan, D., "Estimating the Cost of Capital", Credit Suisse, 8 Oct 2013, pp. 2-34.
- Mauboussin, M. and Callahan, D., "Economic Returns, Reversion to the Mean, and Total Shareholder Returns", Credit Suisse, 6 Dec 2013, pp. 1-8.
- Mauboussin, M. et al., "The Base Rate Book", Credit Suisse, 26 Sep 2016 (CFROI persistence), and "How to Model Reversion to the Mean", 17 Sep 2013.
- Koller, T., Goedhart, M. and Wessels, D., Valuation, 5th ed., McKinsey and Company, 2010, chapters 2, 4, 6 to 11, 25, 27 to 29.

<!-- Spec vs notes: the spec labels "cost of equity 8 to 10 percent" with the 1963-2008 period; the McKinsey note dates it late 2009 and gives 1963-2008 only for the 8 percent median cost of capital, so the table follows the note. -->
