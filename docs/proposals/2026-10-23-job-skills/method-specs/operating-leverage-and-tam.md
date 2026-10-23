# Operating leverage, TAM and profit pools

Purpose: translate a change in sales into a change in margin and earnings, size the revenue opportunity a company can capture while earning above its cost of capital, and show where industry profit is moving. Used by earnings, company, valuation, thesis, sector and theme jobs.

Source tags (all Mauboussin and Callahan, Credit Suisse): [OL] Operating Leverage, Jun 2016; [T15] Total Addressable Market, Sep 2015; [PP] Global Industry Profit Pools, Jul 2016; [MM] Measuring the Moat, Jul 2013.

## 1. Inputs
- Reported, tearsheet: revenue, COGS, SG&A, R&D, depreciation, EBIT, interest, net debt, PPE gross and net, capex, revenue segments (5 years), for 5 to 10 years across calls; consensus sales, EBIT and EPS with surprise history and guidance.
- Search: transcripts and filings for fixed cost, capacity utilization, price versus volume versus mix, penetration and customer counts; broker research for market size and adoption; news for competitor capacity and pricing.
- Assumed: incremental margins in each scenario, cost of capital (see roic.md).

## 2. Procedure
1. Split each past margin change into price and mix, volume (operating leverage), scale economies and cost efficiencies [OL p.8-10]. Goodyear 2011-15: sales down 28%, volume down 8%, operating income up almost 50% through mix.
2. Estimate the fixed and variable split. Classify cost lines from filings or regress change in EBIT on change in sales over 5 to 10 years to get the company's operating margin beta. Compare with the sector beta. Done: contribution margin and beta, with method.
3. Compute the margin response (formulas below). Run a downside and an upside with different incremental margins; operating leverage is symmetric. Check capacity utilization: change in utilization and change in operating margin correlate 0.59 (1967-2014) [OL p.9].
4. Add financial leverage: net debt, not gross, and interest coverage. High operating plus high financial leverage is the highest earnings risk [OL p.15-17].
5. Test whether growth creates value: compare the forecast incremental margin with the incremental threshold margin. Done: created, neutral or destroyed.
6. Earnings preview: take consensus sales and EBIT, compute the implied incremental margin, compare with the company's contribution margin, its beta and the threshold margin, then compute EPS for sales 1% and 3% above and below consensus. Widen ranges where the beta is high. Done: EPS per 1% of sales.
7. Size TAM (section 6).
8. Build the profit pool and its migration (step 3 of industry-structure.md).

## 3. Formulas
- Contribution margin CM = 1 minus variable cost ratio. EBIT = sales x CM minus fixed cost. Incremental margin on extra sales = CM (derived from [OL p.3]).
- New margin minus old margin = (CM minus old margin) x (change in sales / new sales). Derived; it reproduces the paper's example ([OL p.3]): base $10M sales, 20% margin; 75% fixed gives 56% at $25M and negative 40% at $5M; 25% fixed gives 32% and 0%.
- Degree of operating leverage = CM / margin = percent change in EBIT / percent change in sales (derived). It rises as margin approaches breakeven.
- Degree of financial leverage = EBIT / (EBIT minus interest). Percent change in EPS is about DOL x DFL x percent change in sales (derived; check: EBIT 100 to 120 with interest 30 gives profit 70 to 90, plus 28.6% = 1.43 x 20%) [OL p.15-17].
- Operating margin beta = slope of regression of change in EBIT on change in sales [OL p.11-14].
- Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 minus tax)]. Threshold margin = [prior EBIT + incremental threshold margin x incremental sales] / (prior sales + increase). Example: (0.35 + 0.25) x 0.10 / (1.10 x 0.65) = 8.4% [OL p.19-20].
- Unit demand = new users + replacements [T15 p.15].
- Bass: N(t) minus N(t-1) = [p + q x N(t-1)/m] x [m minus N(t-1)]; p innovation, q imitation, m eventual adopters. Peak new adopters per period = m x (p+q)^2 / (4q) (the note says the source text is garbled; standard form); time of peak = ln(q/p)/(p+q), when q exceeds p (derived) [T15 p.9-11].
- Base-rate check: z = (implied CAGR minus reference mean) / reference standard deviation [T15 p.21-22].

## 4. Reference tables (dated; verify)
Operating margin beta, top 1,000 global companies excluding financials and utilities, 1950-2014, one-year / three-year [OL p.11-14]:
| Sector | Beta | Sales correlation with US GDP |
|---|---|---|
| Materials | 0.19 / 0.16 | 0.53 |
| IT | 0.17 / 0.16 | 0.55 |
| Telecom | 0.17 / 0.19 | 0.51 |
| Energy | 0.13 / 0.10 | 0.12 |
| Health care | 0.12 / 0.12 | 0.43 |
| Industrials | 0.08 / 0.08 | 0.74 |
| Consumer discretionary | 0.08 / 0.07 | 0.77 |
| Consumer staples | 0.07 / 0.07 | 0.37 |
All: 0.11 / 0.10. A beta of $0.12 per $1 is below health care's mean margin of 15.7%, so read beta as past co-movement, not as an incremental margin to assume. Fixed-asset intensity, highest first: energy, materials, telecom, industrials, IT, discretionary, health care, staples [OL Exh.3]. GAP: no beta for financials, utilities or real estate; the skill computes the company's own.

Bass parameters, 50+ products to the 1990s: p average 0.037, median 0.025; q average 0.327, median 0.280 [T15 App. A]. Years for half of US households: telephone 71, PC 19, cell phone 14, internet 10, so old parameters understate speed [T15 p.14].

Growth check: Tesla 2015, management 50% CAGR for 10 years from about $6B sales; reference class of 1,200+ cases at $6B to $13B: mean real CAGR under 3%, standard deviation under 8%, none above 40%; z about 5.9 [T15 p.21-22]. Refresh from base-rates.md (size-matched).

Forecast error: analysts are too optimistic on earnings growth; errors are larger where beta is high (metals versus food) and worst for high operating leverage with weak sales [OL p.2, 15].

## 5. Interpretation rules
- Operating leverage is not economies of scale: mistaking the two predicts falling unit costs as the company grows (Home Depot gross margin 27.7% to 29.9% came from supplier terms) [OL p.9]. Cost efficiencies are separate again.
- All costs are variable in the long run; SG&A is sticky; the fixed share falls as the company grows [OL p.4].
- DOL is highest near breakeven. M&A changes the cost profile.
- Sales growth, profit growth and value creation are distinct; growth below the threshold margin destroys value [OL p.5-7, 19].
- GAP: the notes document optimism and the weak-sales case, not an underestimate in both directions. The two-sided effect in the skill is derived arithmetic (symmetric leverage), so label it derived, not as a documented analyst bias.
- GAP: the tearsheet has no capacity utilization or fixed and variable cost split; both come from filings, transcripts or analyst estimates, and are assumed otherwise.
- Not applicable: banks and insurers (financing is operations), early-stage companies (fixed-cost leverage lifts margin even at low ROIC), cyclical peaks read as normal.

## 6. TAM procedure and rules
TAM = revenue at 100% share in a market the company can serve while creating value; the limit is where return on incremental capital falls below cost of capital [T15 p.3-4]. Management's TAM is a claim, not an input.
1. Classify: current or new technology, current or new customers. New technology with new customers has unknown adopters and speed; use scenarios [T15 p.5-6].
2. Bottom-up: customers x revenue per customer through the funnel: population, eligible, access, product share, volume, price. Conversion and persistence cut it far below eligible numbers (statins: 56M eligible, 25M on drug, 25% persistent at five years). Add demand checks (payer versus user, saturation, elasticity, cyclicality, substitution) and supply checks (capacity, local scale, regulation, niches) [T15 p.6-9]. Show size against price.
3. Top-down: market x share path, using the same substitution set. Uber's TAM ranged $100B to $1.3T on definition alone [T15 p.4, 8].
4. Diffusion: place the product on the S-curve; use the Bass peak and analog parameters; replacements dominate unit sales within 5 to 12 years, so forecast the replacement cycle, not penetration (3 to 4 years cut 15-year units 17%) [T15 p.15, 33]. Color TV: 14M units of capacity against 6M peak sales [OL p.5-7].
5. Limits: scale is local (addressable TAM below national); overshoot (customers refuse feature upgrades); network effects only for combinatorial networks, leaders otherwise rarely exceed 40% share [T15 p.16-19].
6. Base rates: compute the implied CAGR and its z-score against the size-matched class. Done: three methods and a range.
7. Profit pools and value migration: spread x capital by firm, 3 to 5 year averages, today versus 5 and 10 years ago [PP p.1-2]. Health care pool $65B (2002), $116B (2007), $118B (2012), pharma share from about two thirds to two fifths [MM App. B p.55]. A larger declared TAM can be a looser definition (GE) [T15 p.23].

## 7. Output lines
- "Margin change last year: price and mix X, volume Y, scale Z, efficiency W points." Derived.
- "Contribution margin C%, own beta B versus sector S; method: [regression or cost lines]." Derived, assumed.
- "Consensus implies incremental margin I% versus threshold margin T%." Derived.
- "EPS changes by E% per 1% sales miss; financial leverage adds F." Derived.
- "TAM $A to $B (bottom-up), $C (top-down); base-rate z-score Z." Assumed, derived.
- "Value migrating toward [segment] of the chain." Judgment.

## 8. Sources
Notes: tam-leverage-profit-pools.md (sections 1 to 3, 7), base-rates.md (2.8), roic-moat.md (paper E). Papers: the four tagged reports.
