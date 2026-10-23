# Operating leverage, addressable market and profit pools

This method answers three linked questions. How much do margin and earnings move when sales move? How much revenue can the company capture while still earning above its cost of capital? Where in the industry is profit moving? It follows Mauboussin and Callahan's Operating Leverage (2016), Total Addressable Market (2015) and Global Industry Profit Pools (2016). Sales growth, profit growth and value creation are distinct (Operating Leverage, pp. 5-7): the method keeps them apart and gives ranges, because a margin forecast built by linear extrapolation is the common error (p. 17).

## When a skill loads this file

Earnings previews and reviews (the sales-to-margin sensitivity), deep dives, valuation (the revenue path and the incremental margin), thesis, sector and theme work (addressable market, adoption curve, profit pool). A narrow question ("what does a 5 percent sales miss do to EPS") gets steps 2, 3 and 6 only.

## Inputs

| Input | Where in Bigdata.com | Basis |
|---|---|---|
| Revenue, COGS, SG&A, R&D, depreciation, EBIT, interest, net debt, gross and net PP&E, capex, five fiscal periods per call | `bigdata_company_tearsheet`, `fundamentals` | reported |
| Consensus sales, EBIT, EPS to four years out, surprise history, company guidance | `estimates`, `latest_earnings` | reported |
| Revenue by product and geography, five years | `revenue_segmentation` | reported |
| Fixed and variable cost, capacity utilization, price against volume against mix, customer counts, penetration | `bigdata_search` on transcripts and filings | reported |
| Market size, adoption, competitor capacity and pricing | `bigdata_search` on research and news | reported |
| Incremental margins per scenario, cost of capital, amortizable lives | none | assumed |

Not in the sources and not in the tearsheet: capacity utilization and the fixed and variable split. Take them from filings, transcripts or research; otherwise state them as assumed.

## Procedure: operating leverage

1. **Decompose past margin changes.** Split each year's change in operating margin into price and mix, volume (operating leverage), economies of scale and cost efficiencies (Operating Leverage, pp. 8-10). These are different: operating leverage spreads preproduction costs over more units; economies of scale lower unit cost as the company grows (Home Depot gross margin rose from 27.7 to 29.9 percent, FY1996 to FY2001, on supplier terms); cost efficiencies happen whatever sales do. Goodyear 2011-2015: sales down 28 percent, volume down 8 percent, operating income up almost 50 percent through mix. Done when each of the last five years has the four-way split, or the missing pieces are named.
2. **Estimate the cost structure.** Classify cost lines as fixed or variable from the filings, or regress the change in EBIT on the change in sales over five to ten years to get the company's operating margin beta. Compare it with the sector beta below. Remember that all costs are variable in the long run, SG&A is sticky, and the fixed share falls as a company grows (p. 4). Done when the contribution margin and the beta are stated with the method.
3. **Compute the margin response** with the formulas below, for a downside and an upside with different incremental margins; leverage works in both directions. Check capacity utilization: its change and the change in operating margin correlated 0.59 (1967-2014, pp. 8-10). Done when the margin at each sales level is shown.
4. **Add financial leverage.** Use net debt, not gross, and interest coverage. High operating plus high financial leverage is the highest earnings risk; companies with high operating leverage tend to carry less debt (pp. 15-17). Done when the EPS sensitivity includes interest.
5. **Test whether growth creates value.** Compare the forecast incremental margin with the incremental threshold margin (formula below). Done when growth is labelled value-creating, neutral or destroying, with the numbers.
6. **Earnings preview use.** From consensus sales and EBIT compute the implied incremental margin; compare it with the contribution margin, the company's beta, the sector beta and the threshold margin. Compute EPS for sales 1 and 3 percent above and below consensus (5 percent when the skill asks). Widen the range where the beta is high, because forecast errors are larger there (pp. 2, 15). Done when the note states the EPS change per 1 percent of sales.

## Procedure: addressable market

TAM is the revenue a company could realize with 100 percent share of a market it can serve while creating shareholder value; it stops where return on incremental investment falls below the cost of capital (TAM, pp. 3-4). Management's TAM is a claim to test, not an input.

1. **Classify the product** on two axes: current or new technology, current or new customers. New technology for new customers has unknown adopters and speed; use scenarios (pp. 5-6). Done when the cell is named.
2. **Bottom-up size.** Customers times revenue per customer through the funnel: population, eligible, with access, product share, volume (usage, persistence), price. Conversion and persistence cut the funnel far below the eligible count: of 56 million US adults eligible for statins, about 25 million took them and about 25 percent of starters remained after five years (2015, pp. 6-7). Check demand (payer against user, buyer resources, saturation, elasticity, cyclicality, substitution) and supply (capacity, distribution footprint, regulation, incentives, local scale, niches) (pp. 7-9). Show size against price. Done when the funnel table and a price sensitivity exist.
3. **Top-down size.** Market times share path with the same substitution set. The definition of the market decides the answer: Uber's TAM ranged from $100bn (taxis) to $1.3tn (all ways of moving people and things) on definition alone (pp. 4, 8). Use both routes to bound the forecast (McKinsey ch. 9). Done when both sizes and the definitions are stated.
4. **Place it on the adoption curve.** Use the Bass model with analog parameters. Unit demand = new users plus replacements, and replacements are most unit sales within five to seven years for many products and within about twelve years for almost all; then forecast the replacement cycle, not penetration. Lengthening the cycle from three to four years cut 15-year cumulative units by 17 percent in the paper's example (pp. 15, 32-37). Do not extrapolate the steep middle of the S-curve: color TV makers built 14 million units of capacity against peak sales of 6 million (p. 11). Done when the stage (penetration, transition, maturity) is named.
5. **Apply the limits.** Scale is usually local, so the addressable market at acceptable returns is smaller than the national one (p. 16). Overshoot: customers use a fraction of the features and refuse to pay for more. Network effects count only where users interact (payments, marketplaces, search); otherwise market leaders rarely exceed 40 percent share (pp. 16-19). Done when each limit has a verdict.
6. **Check against base rates.** Compute the implied revenue CAGR and its z-score against the size-matched reference class in `references/base-rates.md`. Tesla in 2015 targeted about 50 percent a year for ten years from about $6bn; in 1,200+ cases of companies with $6bn to $13bn of sales the mean real ten-year CAGR was under 3 percent with a standard deviation under 8 percent, none above 40 percent, a z-score of about 5.9 (pp. 21-22). Done when the TAM is a range from three methods, with the base-rate z-score.
7. **Map the profit pool and its migration.** Width = share of industry invested capital, height = ROIC minus WACC, area = economic profit, three to five year averages, today against five and ten years ago (Profit Pools, pp. 1-2; procedure in `references/industry-structure.md`). A larger declared TAM can be a looser definition rather than a larger opportunity: GE's share of its own redefined TAM fell to under 10 percent by 2001 (TAM, p. 23). Done when the direction of value migration is stated.

## Formulas

- Contribution margin CM = 1 - variable cost ratio. EBIT = sales x CM - fixed cost. The incremental margin on extra sales equals CM (derived from Operating Leverage, p. 3).
- New margin - old margin = (CM - old margin) x (change in sales / new sales) (derived). It reproduces the paper's example: base $10M sales at a 20 percent margin; with 75 percent of costs fixed, margin is 56 percent at $25M and -40 percent at $5M; with 25 percent fixed, 32 percent and 0 percent (p. 3).
- Degree of operating leverage DOL = CM / operating margin = percent change in EBIT / percent change in sales at the base point (derived). It rises sharply near breakeven.
- Degree of financial leverage DFL = EBIT / (EBIT - interest). Percent change in EPS is about DOL x DFL x percent change in sales (derived). Check: EBIT from 100 to 120 with interest of 30 takes pretax profit from 70 to 90, plus 28.6 percent = 1.43 x 20 percent (pp. 15-17).
- Operating margin beta = slope of the regression of change in EBIT on change in sales (pp. 11-14).
- Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 - tax rate)]. Threshold margin = [prior EBIT + incremental threshold margin x incremental sales] / (prior sales + increase). Example: (0.35 + 0.25) x 0.10 / (1.10 x 0.65) = 8.4 percent (pp. 19-20).
- Bass: N(t) - N(t-1) = [p + q x N(t-1) / m] x [m - N(t-1)]; p = innovation coefficient, q = imitation coefficient, m = eventual adopters, N = cumulative adopters (TAM, p. 9). Peak new adopters per period = m x (p + q)^2 / (4q), standard form (the source text is garbled). Time of peak = ln(q/p) / (p + q) when q exceeds p (derived, standard Bass result).
- Base-rate z = (implied CAGR - reference mean) / reference standard deviation.

## Reference tables

Operating margin beta and sales link, top 1,000 global companies excluding financials and utilities, 1950-2014, constant dollars (Operating Leverage, pp. 5-7, 11-14; verify):

| Sector | Beta, 1-year / 3-year | Correlation of sales growth with US GDP | Mean operating margin |
|---|---|---|---|
| Materials | 0.19 / 0.16 | 0.53 | 12.1% |
| Information technology | 0.17 / 0.16 | 0.55 | not given |
| Telecom | 0.17 / 0.19 | 0.51 | 21.6% |
| Energy | 0.13 / 0.10 | 0.12 | not given |
| Health care | 0.12 / 0.12 | 0.43 | 15.7% |
| Industrials | 0.08 / 0.08 | 0.74 | 7.9% |
| Consumer discretionary | 0.08 / 0.07 | 0.77 | 8.2% |
| Consumer staples | 0.07 / 0.07 | 0.37 | 8.3% |
| All | 0.11 / 0.10 | 0.65 | |

A beta of 0.12 for health care sits below its 15.7 percent mean margin, so read the beta as past co-movement, not as an incremental margin to assume. Fixed-asset intensity, highest first: energy, materials, telecom, industrials, IT, discretionary, health care, staples (Exhibit 3).

Credit statistics by rating, S&P medians 2011-2013 (Operating Leverage, pp. 15-17; verify):

| Rating | AAA | AA | A | BBB | BB | B |
|---|---|---|---|---|---|---|
| Operating margin, % | 28.0 | 26.9 | 22.7 | 21.3 | 17.9 | 19.2 |
| EBIT interest coverage, x | 40.8 | 17.3 | 10.3 | 5.5 | 3.2 | 1.3 |
| Debt / total capital, % | 2.8 | 17.2 | 30.7 | 41.1 | 50.4 | 72.7 |

Bass parameters, 50+ products from the 1920s to the 1990s: p average 0.037, median 0.025; q average 0.327, median 0.280 (TAM, App. A). Diffusion has sped up: years for half of US households to adopt were telephone 71, PC 19, cell phone 14, internet 10 (p. 14), so old parameters understate speed.

Forecast accuracy: analysts are too optimistic on earnings growth, with larger errors where the beta is high (metals against food) and the worst errors for high-operating-leverage companies that miss on sales (Operating Leverage, pp. 2, 15). Analysts consistently underestimate how sales changes reach margins, on the upside and on the downside (Expectations Investing, 2006, p. 68). Drug peak-sales forecasts: almost two thirds of 1,700+ forecasts missed by 40 percent or more (TAM, p. 7).

## Interpretation and limits

- Operating leverage is not economies of scale: mistaking one for the other predicts falling unit costs as the company expands to meet demand (pp. 8-10). Cost efficiencies are separate again.
- DOL is not constant; it is highest near breakeven. A large acquisition changes the cost structure.
- Growth below the threshold margin destroys value, however fast it is.
- Sales forecasts from GDP work for cyclicals (discretionary, industrials), not for staples, health care or energy (correlations above).
- Industry shakeouts let survivors grow faster than the market: industry sales doubling while firms halve quadruples sales per survivor (TAM, pp. 11-12).
- Physical, service and knowledge businesses scale differently: sales growth needs assets, headcount, or neither (TAM, pp. 23-25).
- Not applicable: banks and insurers (financing is operations; use the bank case in `references/valuation.md`); early-stage companies (fixed-cost leverage lifts margins at low ROIC, so test the long-run margin by analogues); a cyclical at peak margin read as a run rate.
- Not in the sources: an operating margin beta for financials, utilities or real estate. Compute the company's own.

## Output lines

- "Last year's margin change of X points: price and mix A, volume B, scale C, efficiency D." Basis: derived.
- "Contribution margin C percent; own beta B against the sector's S (1950-2014); method: [regression or cost lines]." Basis: derived, assumed where the split is estimated.
- "Consensus implies an incremental margin of I percent against a contribution margin of C and a threshold margin of T." Basis: derived.
- "EPS moves about E percent per 1 percent of sales; at 3 percent below consensus EPS is [value]; financial leverage adds F points." Basis: derived.
- "TAM of $A to $B bottom-up and $C top-down; the implied revenue CAGR has a z-score of Z against [size class, period]." Basis: assumed and derived.
- "Adoption stage: [penetration, transition or maturity]; replacements are R percent of units." Basis: judgment.
- "Value is moving toward [segment of the chain], from the profit pool over [years]." Basis: judgment, with the pool derived.

## Sources

- Notes: tam-leverage-profit-pools.md (sections 1 to 3, 7 to 9); expectations-multiples-dcf.md (1.2, EI p.68); mckinsey-part1.md (chapter 9).
- Mauboussin, M. and Callahan, D., "Operating Leverage: A Framework for Anticipating Changes in Earnings", Credit Suisse, 14 June 2016, pp. 1-22 (pages without a title refer to this paper in the first procedure and the formulas).
- Mauboussin, M. and Callahan, D., "Total Addressable Market: Methods to Estimate a Company's Potential Sales", Credit Suisse, 1 Sep 2015, pp. 3-37.
- Mauboussin, M. et al., "Global Industry Profit Pools", Credit Suisse HOLT, July 2016, pp. 1-4.
- Mauboussin, M., "Expectations Investing: Reading Stock Prices for Better Returns", CFA Institute, Sep 2006, p. 68.
- Mauboussin, M. and Callahan, D., "Measuring the Moat", Credit Suisse, 2013 (profit pool method).
- Koller, T., Goedhart, M. and Wessels, D., Valuation, 5th ed., McKinsey, 2010, ch. 9 (top-down and bottom-up revenue).

<!-- Spec vs notes: the spec's GAP says the notes show analyst optimism and the weak-sales case, not an underestimate in both directions; the expectations note (Expectations Investing 2006, p. 68) says analysts underestimate the sales-to-margin link on the upside and the downside, so this file cites it and drops that GAP. -->
