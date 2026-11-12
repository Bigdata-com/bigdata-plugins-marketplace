# Operating leverage, addressable market and profit pools

How far margin and earnings move when sales move, how much revenue the company can capture while earning above its cost of capital, and where industry profit is moving. Keep sales growth, profit growth and value creation apart and give ranges; straight-line margin extrapolation is the common error.

## Inputs

| Input | Where it comes from |
|---|---|
| Revenue and its segments, COGS, SG&A, R&D, depreciation, EBIT, interest, net debt, PP&E, capex | Annual statements and revenue segmentation, five fiscal years |
| Consensus sales, EBIT and EPS to four years out, surprise history, guidance | Estimates and latest earnings |
| Fixed and variable cost, capacity utilisation, price, volume and mix, customer counts, penetration | Filings and transcripts, by search. When they do not give a figure, state it as an assumption |
| Market size, adoption, competitor capacity and pricing | Research and news, by search |
| Incremental margins per case, cost of capital, amortisable lives | Not in the data. State each once; cost of capital as valuation.md (cost of capital) sets out |

## Sources of margin change

Split each year's change in operating margin into price and mix, volume (operating leverage, which spreads fixed costs over more units), economies of scale (lower unit cost as the company grows) and cost efficiencies (whatever sales do). Mistaking operating leverage for scale predicts falling unit costs as the company adds capacity.

## Cost structure and operating margin beta

Classify cost lines as fixed or variable from the filings, or regress the change in EBIT on the change in sales over five to ten years; the slope is the operating margin beta. All costs are variable in the long run, SG&A is sticky, and the fixed share falls as a company grows. Changes in capacity utilisation and operating margin correlated 0.59 (1967 to 2014).

Operating margin beta and sales link by sector, top 1,000 global companies excluding financials and utilities, 1950 to 2014, constant dollars:

| Sector | Beta, 1-year / 3-year | Correlation of sales growth with US GDP | Mean operating margin |
|---|---|---|---|
| Materials | 0.19 / 0.16 | 0.53 | 12.1% |
| Information technology | 0.17 / 0.16 | 0.55 | n/a |
| Telecom | 0.17 / 0.19 | 0.51 | 21.6% |
| Energy | 0.13 / 0.10 | 0.12 | n/a |
| Health care | 0.12 / 0.12 | 0.43 | 15.7% |
| Industrials | 0.08 / 0.08 | 0.74 | 7.9% |
| Consumer discretionary | 0.08 / 0.07 | 0.77 | 8.2% |
| Consumer staples | 0.07 / 0.07 | 0.37 | 8.3% |
| All | 0.11 / 0.10 | 0.65 | |

The beta is past co-movement, not an incremental margin to assume. Fixed-asset intensity, highest first: energy, materials, telecom, industrials, IT, discretionary, health care, staples. For financials, utilities and real estate, compute the company's own beta.

## Margin response

- Contribution margin CM = 1 - variable cost ratio. EBIT = sales x CM - fixed cost. The incremental margin on extra sales equals CM.
- New margin - old margin = (CM - old margin) x (change in sales / new sales).
- Degree of operating leverage DOL = CM / operating margin = percent change in EBIT / percent change in sales at the base point. It rises sharply near breakeven.
- Degree of financial leverage DFL = EBIT / (EBIT - interest). Percent change in EPS is about DOL x DFL x percent change in sales.

Run a downside and an upside with different incremental margins. Use net debt and interest coverage (credit.md, coverage and leverage ratios). High operating plus high financial leverage carries the most earnings risk.

## Sales sensitivity around consensus

From consensus sales and EBIT, compute the implied incremental margin and compare it with the contribution margin, the company's beta, the sector beta and the threshold margin. Compute EPS at sales 1 and 3 percent above and below consensus, or 5 when asked. Widen the range where the beta is high: forecast errors are larger there, the worst come from high-operating-leverage companies that miss on sales, and sales changes reach margins by more than analysts assume in both directions.

## Threshold margin

Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 - tax rate)].

Threshold margin = (prior EBIT + incremental threshold margin x incremental sales) / (prior sales + incremental sales).

Growth at a margin below the threshold destroys value, however fast it is.

## Addressable market

The revenue a company could earn with 100 percent share of a market it can serve while creating value; it stops where the return on incremental investment falls below the cost of capital. Management's figure is a claim to test.

- Classify the product on two axes: current or new technology, current or new customers. New technology for new customers has unknown adopters and speed; use scenarios.
- Bottom-up: customers x revenue per customer through the funnel (population, eligible, with access, product share, usage and persistence, price); conversion and persistence cut it far below the eligible count. Check demand (payer against user, buyer resources, saturation, elasticity, cyclicality, substitution) and supply (capacity, distribution, regulation, local scale). Show size against price.
- Top-down: market x share path. The market definition decides the answer, so bound the forecast with both routes; a larger declared market can be a looser definition.
- Limits: scale is usually local, so the market at acceptable returns is smaller than the national one. Customers using a fraction of the features refuse to pay for more. Network effects count only where users interact (payments, marketplaces, search); without them, leaders rarely exceed 40 percent share.
- Shakeouts let survivors outgrow the market: industry sales doubling while the number of firms halves quadruples sales per survivor.
- Almost two-thirds of more than 1,700 drug peak-sales forecasts missed by 40 percent or more.
- Base-rate check: z = (implied revenue CAGR - reference mean) / reference standard deviation, against the size-matched class (base-rates.md, real sales growth by starting size).

## Adoption curve

Bass model: N(t) - N(t-1) = [p + q x N(t-1) / m] x [m - N(t-1)], where p is the innovation coefficient, q the imitation coefficient, m eventual adopters and N cumulative adopters. Peak new adopters per period = m x (p + q)^2 / (4q), reached at t = ln(q / p) / (p + q) when q exceeds p.

Parameters across more than 50 products, 1920s to 1990s: p average 0.037, median 0.025; q average 0.327, median 0.280. Diffusion has sped up (years for half of US households to adopt: telephone 71, PC 19, cell phone 14, internet 10), so older parameters understate speed.

Unit demand = new users + replacements. Replacements become most unit sales within five to seven years for many products and about twelve for almost all; then forecast the replacement cycle, not penetration. Do not extrapolate the steep middle of the S-curve.

## Profit pools

Width = share of industry invested capital, height = ROIC - WACC, area = economic profit, on three- to five-year averages, today against five and ten years ago (industry-structure.md, profit pool).

## Interpretation and limits

- After a large acquisition, re-estimate the cost structure.
- Forecast sales from GDP for discretionary and industrials, where the correlation is above 0.7, not for staples, health care or energy.
- For banks and insurers, financing is operations; use the bank case (valuation.md, special cases).
- For an early-stage company, test the long-run margin against analogues; fixed-cost leverage lifts margins at low ROIC.
- For a cyclical at peak margin, do not read the margin as a run rate.
