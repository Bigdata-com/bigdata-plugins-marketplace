# Return on invested capital

What the company earns on the capital its operations use, how that compares with its cost of capital, and where the return is heading. Definitions alone move ROIC by a factor of two or more, so state each choice once (tax method, average or opening capital, goodwill, leases, R&D, excess cash) and apply it identically to every peer. Today's ROIC is already in the price; a stock moves when returns change against expectations. End with the spread over a stated cost of capital and a reasoned reversion path, never a rating.

## Inputs

| Input | Where it comes from |
|---|---|
| Income statement, balance sheet and reported invested capital | Annual statements and key metrics, five fiscal years |
| Reported ROIC, margins, cash conversion cycle | Company ratios |
| Segment revenue; tax, lease, deferred tax and segment notes; restructuring and impairment history | Segment data and filings, read in full for the note |
| Risk-free rate | Country data |
| Equity risk premium, beta, credit spread, target weights | Not in the data. Compute beta from the price series or take a peer or sector beta; state each once, with its date |

## NOPAT

NOPAT = EBITA x (1 - operating tax rate), where EBITA = EBIT + amortisation of acquired intangibles.

- Operating tax rate: statutory plus state or local rate, plus recurring operating items from the tax reconciliation (foreign rate differences, credits that scale with revenue), excluding one-offs and the interest shield. Never use reported tax or the effective rate: both contain the interest shield, which WACC already counts.
- Cash NOPAT = EBITA - (operating taxes - increase in net operating deferred tax liability). Show it as a second row when deferred taxes are large.
- Unusual items: remove a one-time item; spread one that recurs at intervals (restructuring every three years) across the years; average one that recurs but swings; ignore one that flips sign (currency translation). A "one-time" charge in most of the last five years is a cost.
- Keep interest on cash out of NOPAT.

## Invested capital

From the operating side: operating working capital (operating cash, receivables, inventory, prepaid, less payables, accruals, deferred revenue and taxes payable; nothing interest-bearing) + net PP&E + goodwill and acquired intangibles + other net operating assets. Keep an item only if the company could not earn the same NOPAT without it.

From the financing side: debt + lease liabilities + unfunded pensions + equity + minority interest - excess cash - non-operating assets. A gap between the two sides is a missed item. Compare the result with the reported field.

ROIC = NOPAT / average of opening and closing invested capital. Show the opening-capital variant beside it.

## Excess cash

Allow operating cash of 2 percent of sales for steady companies and 5 percent for less predictable or faster-growing ones. Remove the rest from operating capital and the same amount from equity.

## Goodwill

Show ROIC with and without goodwill and acquired intangibles. Without them measures the operating business and is the basis for peer comparison; with them measures the return on all capital raised, premiums included. Add cumulative impairments and amortisation back to goodwill. For a serial acquirer the two figures can differ by a factor of three. Judge an acquisition by its net present value, not by ROIC.

## Leases

Most statements capitalise leases from 2019 (ASC 842, IFRS 16). When they do, add the implied interest (prior-year lease liability x pre-tax cost of secured debt) to EBITA and keep the liability in capital and in debt. For earlier periods, estimate the leased asset:

Leased asset (t-1) = rental expense (t) / (kd + 1 / asset life), with kd the cost of secured debt and asset life = PP&E / annual depreciation.

Capitalising leases also changes the debt weight in WACC. For US retailers in 2006 it cut average ROIC from about 20 to 11 percent.

## Capitalised R&D

Capitalise R&D when it is material; advertising or customer acquisition only with evidence of a multi-year benefit. Use an amortisable life of about 10 years for pharma and a short one for software; elsewhere state the life as an assumption and show one alternative.

- Research asset = sum over t = -(n-1) to 0 of R&D(t) x (n + t) / n, with n the amortisable life; current-year R&D is unamortised.
- Adjusted EBITA = EBITA + R&D - amortisation of the research asset.

Add the research asset to invested capital. Operating taxes do not change, because R&D is deductible in full. When the R&D history is shorter than the life, the asset is understated; say so.

## ROIC decomposition

ROIC = (1 - operating tax rate) x (EBITA / revenue) x (revenue / invested capital).

Track margin and turnover over five to ten years, with working capital in days: 365 x item / revenue (inventory and payables on cost of goods sold). A high margin points to an advantage with customers, high turnover to one in production. Flag any jump in turnover and any forecast that implies negative capex.

## ROIIC and the spread

- ROIIC, one year = (NOPAT(t) - NOPAT(t-1)) / (IC(t-1) - IC(t-2)).
- ROIIC, rolling n years = (NOPAT(t) - NOPAT(t-n)) / (IC(t-1) - IC(t-n-1)), with n = 3. A one-year figure is noisy and a high reading can be operating leverage: use the yearly series to spot change, and compare only the three-year figure with WACC.
- Economic profit = invested capital x (ROIC - WACC) = NOPAT - WACC x invested capital, with one capital definition in both terms. Report it in currency.
- Growth = ROIC x investment rate, where investment rate = net investment / NOPAT. The value-driver formula that ties growth, RONIC and WACC to value is in valuation.md, continuing value.

An advantage passes two tests: ROIC above the cost of capital and above peers, over a full cycle. Value needs the spread and the capital deployed at it, so judge economic profit, not ROIC alone.

## Cost of capital inputs

WACC = D/V x kd x (1 - Tm) + E/V x ke, at target market-value weights, with ke = rf + beta x ERP. The risk-free rate, beta regression and checks are in valuation.md, cost of capital.

- Unlevered beta = levered beta / [1 + (1 - T) x D/E]. The form without the tax term, levered = unlevered x (1 + D/E), assumes the tax shield carries operating risk. State which form is used.
- Beta from a broad value-weighted index, never a local one; adjusted beta = 0.67 x raw + 0.33.
- Equity risk premium: estimates ran 4.5 to 5.7 percent from 2009 to 2013, and published ranges span 3 to 10. Prefer a current implied premium.
- Reference levels: cost of equity for large non-financial companies about 9 percent, range 8 to 10 (late 2009); median cost of capital of US companies about 8 percent (1963 to 2008).

## Persistence and reversion

**ROIC levels, US non-financial companies, ROIC without goodwill, more than 5,000 companies**

| Measure | Figure | Period |
|---|---|---|
| Median ROIC | About 10 percent; annual medians 7 to 11 percent | 1963 to 2008 |
| Top quintile (above 20 percent) | Median falls from 29 to 15 percent over 15 years, not to 10 | 1963 to 2008 |
| Industry medians | Pharma and biotech 23.5 percent; utilities 6.3; commodities 5.8 | 1965 to 2007 |

**Ten-year ROIC transition, US non-financial companies, 1995 to 2005** (percent of companies; rows sum to 100)

| Start | Below 10 percent | 10 to 20 percent | Above 20 percent |
|---|---|---|---|
| Below 10 percent | 57 | 28 | 15 |
| 10 to 20 percent | 25 | 40 | 35 |
| Above 20 percent | 19 | 14 | 67 |

**Four-year persistence of cash-flow returns by sector, global listed companies above about $250 million market cap, live and dead, 1983 to 2015.** The measure is an inflation-adjusted, IRR-style cash-flow return, not ROIC: use r for the speed of reversion (higher r, slower) and the median as a level guide only, and state the r used.

Expected value in four years = sector mean + r x (current value - sector mean).

| Sector | Four-year r | Median cash-flow return, percent |
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

All companies excluding financials and utilities: one-year r 0.78, four-year r 0.56.

**Reversion path by advantage**

| Company advantage | Sector barriers | Near term | Later |
|---|---|---|---|
| Strong, sustainable | Strong | Company ROIC | Toward the sector average |
| Strong, sustainable | Weak or none | Company ROIC | Toward the cost of capital |
| Weak, slipping | Strong | Toward the sector average | Sector average |
| Weak, slipping | Weak or none | Toward the cost of capital | Cost of capital |

The near term lasts as long as the advantage's explicit life: a patent with six years left gives six years. A common convention fades the return over five years, then removes 10 percent of the remaining spread a year; it is not an observed law. Mature companies have earned at most 2 to 3 points above their cost of capital over long periods: use that as the cap on perpetual excess return and the cost of capital as the floor.

Forecast ROIC, ROIIC and RONIC for each year: hold near today's level, trend to the industry median, or trend to WACC, with a reason from the competitive evidence (industry-structure.md). Fading a top-quintile company to WACC is usually too conservative given the transition table; a recovery for a low-ROIC company needs a specific cause.

## Special cases

- Banks and insurers: ROE on adjusted net income against the cost of equity, decomposed with leverage. Captive finance arms: separate them, ROE on allocated equity.
- Negative NOPAT or invested capital: ROIC is meaningless; use the high-growth case (valuation.md, special cases).
- Cyclicals: three- to five-year averages. High inflation: nominal ROIC rises mechanically.

## Interpretation and limits

- When a write-off shrinks capital, ROIC rises with no change in the business: a $10bn asset earning $0.5bn returns 5 percent; write off half and it reads 10 percent. Buybacks lift ROE, not ROIC.
- The reported ROIC field does not state its tax, goodwill, lease or averaging choices. Test it against the hand-built figure, never mix the two in one comparison, and name which one each line quotes.
- With five annual periods, the trend covers five years and ROIIC one three-year window; say so.
