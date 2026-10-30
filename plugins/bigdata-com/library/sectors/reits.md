# Real estate investment trusts (REITs)

This primer covers listed equity REITs and listed property companies: owners of offices, shopping centres, logistics warehouses, apartments, self-storage, healthcare property, data centres and towers. Mortgage REITs hold loans and securities, not buildings; treat them with the banks primer's logic (spread, credit, leverage, book value). No figure here is a current fact.

## How the sector makes money and what drives value

A REIT earns rent. Net operating income (NOI) is rent and recoveries minus property operating costs. Value comes from four things:

- Internal growth: occupancy, rent increases on renewal and new leases, and contractual escalators. Same-store NOI growth measures it.
- Asset values: the market capitalisation rate (cap rate, NOI / property value) at which buyers price the properties. A small change in cap rates moves asset value a lot: at a 5% cap rate, a 0.5-point rise cuts value by about 9% (derived: 5 / 5.5 - 1).
- External growth: acquisitions and development. These add value only when the yield on new investment exceeds the REIT's cost of capital, and issuing equity above net asset value (NAV) is accretive while issuing below it dilutes.
- Leverage and the cost of debt.

In the US a REIT avoids corporate tax by distributing at least 90% of taxable income (other countries' regimes differ). Little cash is retained, so growth depends on access to equity and debt markets.

## Metrics that matter

| Metric | Definition | Why it matters | Rough range |
|---|---|---|---|
| Same-store (like-for-like) NOI growth | NOI change for properties owned in both periods | Organic growth; check how the pool is defined | about 0% to 5% a year in normal markets |
| Occupancy, physical and economic | leased area / total; rent collected / potential rent | Demand; free-rent periods open a gap between the two | differs by property type |
| Leasing spreads, cash and straight-line | new rent / expiring rent - 1 | Mark-to-market of the rent roll | negative spreads are a warning |
| Lease expiry schedule and weighted average lease term | rent expiring by year; rent-weighted remaining term | Rollover risk and upside | flag years with more than about 15% of rent expiring |
| FFO | net income + real estate depreciation and impairments - gains on property sales (Nareit definition) | Standard earnings measure; comparable across companies | |
| AFFO | FFO - maintenance capex, leasing costs and tenant improvements - straight-line rent and other non-cash items | Cash available for distribution; definitions vary by company | |
| AFFO payout | dividends / AFFO | Dividend coverage | above 100% means the dividend is not covered |
| Net debt / EBITDA and fixed charge coverage | net debt / EBITDA; EBITDA / (interest + preferred dividends) | Leverage and refinancing risk | about 5x to 7x for many US REITs |
| Debt maturity and share secured | debt due by year; secured / total | Refinancing wall | |
| Implied cap rate | NOI / (equity market value + debt + preferred - non-income assets) | Price the market puts on the properties | compare with private-market deals |

FFO, AFFO and same-store NOI come from the company's supplemental package; search for them and read the full document.

## Financial statements and accounting traps

- Depreciation on buildings under historical-cost accounting (US GAAP) rarely matches economic wear, and land does not depreciate; FFO adds it back. But buildings do need recurring capital spending, so FFO overstates cash. AFFO subtracts maintenance capex, which management estimates. Benchmark capex as a share of NOI against peers over several years; office typically needs far more than logistics (roughly 10% to 15% of NOI for office against 5% to 10% for logistics).
- Straight-line rent books escalating leases evenly, so reported revenue exceeds cash early in a lease.
- Development: interest and overhead are capitalised during construction, which lifts earnings before the asset produces rent.
- Gains on property sales and impairments distort net income; FFO removes them, but a REIT that keeps selling assets at gains is shrinking its earnings base.
- Company-defined AFFO, "core FFO" and same-store pools change over time. Reconcile each to Nareit FFO and note definition changes.
- Under IFRS (Europe, UK, much of Asia) investment property is often carried at fair value, so earnings include revaluation gains and book value approximates NAV. Use the industry's recurring earnings and NAV measures (EPRA in Europe) rather than IFRS profit.
- Appraised values lag transactions and issuer-paid appraisals have misled before: 1920s real estate bonds were sold on appraisals claiming 66 2/3% cover above the loan. Check appraisals against recent deals.
- Unconsolidated joint ventures: add the REIT's share of their debt.

## Profit pool and competitive dynamics

Rents are set locally by supply and demand for each property type. New supply arrives with a lag of years, which makes property markets cyclical. Listed REITs compete for assets with private real estate funds, pension funds and sovereign investors, and private buyers often set the marginal cap rate. Advantages come from location quality that new supply cannot replicate, scale in operating platforms (apartments, self-storage, logistics), tenant relationships, and a lower cost of capital that lets a REIT buy accretively. Structural demand shifts are large: online retail for logistics and against some shopping centres, remote work for offices, and data and power demand for data centres. ETFs owned 10.6% of large-cap real estate market value, against 7.8% for utilities and 4.3% for technology (30 September 2016), which affects flows and correlation.

## Persistence and fade

- The gross profitability, operating margin and operating leverage tables in `base-rates.md` exclude financials and utilities. REITs were classified in the financials sector until GICS created a real estate sector in 2016, so they are outside those tables.
- In the CFROI table they would sit inside financials (four-year r 0.43, median 7.5%; global, 1983-2015). That figure mixes banks, insurers and REITs; do not use it as a REIT fade rate.
- There are no REIT-specific base rates for same-store NOI growth or AFFO growth. Use the company's and peers' own history across at least one property cycle and say so.

## Valuation conventions and pitfalls

**Why the standard enterprise multiples and ROIC build do not apply.** The standard ROIC build divides NOPAT by book invested capital. A REIT's book capital is depreciated historical cost (under US GAAP), so ROIC on book overstates returns on old portfolios and says nothing about returns at market value. EBITDA ignores the capital spending a building needs, and EV/EBITDA against other sectors ignores that most of a REIT's value sits in assets priced by the property market. The enterprise view survives in one form: the implied cap rate compares the REIT's whole capital structure with its NOI, and it is useful because it can be checked against private-market transactions. Net debt / EBITDA remains the standard leverage measure.

**The alternatives.**

- NAV: gross asset value = forward NOI by segment / market cap rate for that segment, plus development at cost (or a discounted stabilised value once de-risked), plus land and other assets, minus debt at market value, preferred equity and other liabilities. NAV per share sets up the premium or discount to NAV.
- P/FFO and P/AFFO against growth in AFFO per share, compared within a property type, since capex intensity differs between types. AFFO yield against the cost of debt and the risk-free rate.
- Dividend discount as a cross-check, given the payout requirement.
- Excess real estate can be valued by appraisal, value per square metre or a rental DCF; the same tools apply to a REIT's assets.

**Pitfalls.** Using one portfolio-wide cap rate instead of rates by segment and quality, weighted by NOI. Using cap rates from stale appraisals. Not stressing NAV for cap-rate expansion (a rise of 0.5 to 1.0 point is a usual test). Comparing P/FFO across property types. Taking company AFFO without checking maintenance capex. Valuing development at stabilised value before leasing. Ignoring dilution from equity issued below NAV.

## Questions for the earnings call

- What were cash leasing spreads by market, and what is the mark-to-market on leases expiring in the next two years?
- What is the gap between physical and economic occupancy, and how much free rent was granted?
- What maintenance capex and tenant improvement spend per square foot are in AFFO, and how does it compare with the past five years?
- At what cap rates did recent sales and purchases close, against the cap rate in your NAV?
- What is the refinancing plan for debt due in the next 24 months, and at what rate?
- What yield on cost do development projects target, and how much is pre-leased?
- Which tenants are on a watch list, and what share of rent do they pay?

## What to watch at the macro level

Long-term interest rates and credit spreads, which move cap rates and refinancing costs; bank and securitised lending to commercial property; the new supply pipeline by market; demand drivers by property type (employment and office use, consumer spending, e-commerce, household formation, data and power demand); inflation, which helps rents with indexation and short leases but raises costs; and private-market transaction volume, since thin volume makes appraisals less reliable.
