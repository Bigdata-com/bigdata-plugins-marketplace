# Utilities

This primer covers regulated electric, gas and water utilities, integrated utilities that also own generation, and the unregulated power and renewables businesses that often sit in the same group. Independent power producers and merchant generators are commodity businesses; value them with the cyclical methods in `valuation.md` and the energy primer. Every figure below is a historical figure or a rough range, never a current fact.

## How the sector makes money and what drives value

A regulated utility is a local monopoly. In exchange, a regulator sets the prices it may charge so that it recovers its operating costs, the depreciation of its assets, taxes, and an allowed return on its rate base (in the UK and Europe, the regulated asset base, RAB): the net investment the regulator recognises. Allowed revenue is roughly operating costs + depreciation + taxes + rate base x allowed return.

The value drivers follow from that:

- Rate base growth, which comes from the capital spending plan the regulator approves (grid replacement, transmission, generation, resilience).
- The allowed return on equity and the allowed equity share of the capital structure.
- The gap between earned and allowed ROE. Regulatory lag, the delay between spending or cost inflation and new rates, pushes earned ROE below allowed.
- Cost recovery mechanisms: fuel and purchased-power pass-through, revenue decoupling, trackers and riders, storm cost securitisation.
- The allowed return against the true cost of capital. Value per unit of rate base rises only when the earned return exceeds the cost of capital.

Unregulated segments (merchant generation, contracted renewables, trading) earn on power prices, contract terms and tax incentives, and carry commodity risk.

## Metrics that matter

| Metric | Definition | Why it matters | Indicative range, US regulated utilities |
|---|---|---|---|
| Rate base and growth | regulated net investment; annual change | Main earnings growth driver | about 5% to 9% a year in recent plans |
| Allowed ROE and equity ratio | return and equity share set in the last rate case | Sets earnings per unit of rate base | ROE about 9% to 10.5%; equity about 45% to 55% |
| Earned ROE | regulated net income / regulated equity | Shows regulatory lag and cost control | gap to allowed of 0 to 1.5 points is common |
| Capex plan | spending by year and category | Feeds rate base; sets funding needs | |
| FFO / debt | funds from operations / total debt | The ratio rating agencies watch | thresholds for low investment grade often about 12% to 16% |
| Holding company debt share | parent debt / total debt | Leverage outside the regulated entities | higher share means more risk to equity |
| Dividend payout | dividends / EPS | Equity funding need | about 60% to 75% |
| Customer bill growth | change in average bill | Affordability limits future rate increases | above inflation draws political pressure |
| Load growth | change in electricity sales volume | New demand (data centres, electrification) | was near zero for years; now rising in some regions |

Rate case filings and decisions, capital plans and rate base are in investor presentations and regulatory filings; search for them and read the full document.

## Financial statements and accounting traps

- Regulatory assets and liabilities: costs the regulator has allowed the utility to defer and recover later, and amounts it must return. If a regulator disallows recovery, the asset is written off (ASC 980 in the US).
- Allowance for funds used during construction (AFUDC): a non-cash return booked on assets under construction. It lifts reported earnings before the asset earns cash; large capex programmes make it material.
- Free cash flow after capex and dividends is usually negative. The gap is funded with debt and new equity, so EPS growth can be diluted. Track equity issuance, including forward sales and at-the-market programmes.
- Fuel and purchased-power costs pass through with a lag, creating under- or over-recovery balances that swing working capital without changing earnings.
- Depreciation rates are set in rate cases and change at each one; reported margins move for regulatory, not operating, reasons.
- Separate regulated from unregulated earnings. Losses or gains in trading, merchant power or tax-credit sales can hide in consolidated EPS.
- Old coverage tests do not transfer: in 1929 buyers of utility bonds with thin interest coverage relied on the earnings trend and lost; the specific utility coverage tests of the 1930s are out of date. The lesson that stands: test coverage under a bad rate case or a cost shock, not on the trend.

## Profit pool and competitive dynamics

Regulated utilities do not compete for customers in their franchise areas; they compete for capital and for the regulator's approval. Returns are close to the cost of capital by design, and the data match: utilities had a median ROIC of 6.3% without goodwill, low and stable, over 1965-2007 (US non-financial companies), and traded at about 1.5 times invested capital with ROIC of 6.9% and growth of 3.2% in 2006, against a median of 2.7 times for large non-financials. Unregulated power has been less kind: the economic spread of multi-utilities and unregulated power fell from -0.1 to -1.2 points between 2010 and 2015 (global listed companies). Water utilities had a four-firm concentration of 55.2% and multi-utilities 43.8% (global listed companies, 2015).

The quality of the regulator matters more than anything the company controls: whether allowed returns track the cost of capital, how long rate cases take, and whether costs such as storms or wildfire liability are shared with customers. Capital allocation choices are limited by allowed returns.

## Persistence and fade

- The gross profitability, operating margin and operating leverage tables in `base-rates.md` exclude utilities; do not apply them.
- The CFROI table includes utilities: four-year r 0.57, median 3.5%, mean 4.1%, standard deviation of the sector mean 0.8 points (global, live and dead, 1983-2015); the older cut gives r 0.54 and mean 4.1% (1986-2012). Returns are low and fairly persistent, with little excess to fade.
- Utilities have the longest asset lives of any sector, about 29.4 years against 6.6 for information technology (global companies, 2013).
- Sales and earnings growth tables cover all sectors; utility revenue includes pass-through fuel costs, so use rate base and EPS growth instead.

## Valuation conventions and pitfalls

**Why the standard ROIC build and generic enterprise multiples do not apply.** The ROIC method in `roic.md` assumes returns are set by competition and fade toward the cost of capital as rivals enter. A regulated utility's return is administered: the regulator sets it, usually near the cost of capital, so the moat and fade analysis does not describe what drives value. Value comes from how fast the rate base grows and how far earned ROE sits above the cost of equity. Generic EV/EBITDA comparisons mislead because EBITDA depends on depreciation rates and recovery timing set in rate cases, on pass-through fuel revenue, and on regimes that differ by jurisdiction, and because the debt level is set by the allowed capital structure rather than chosen freely. The same P/E can hide very different economics.

**The alternatives.**

- DCF on the regulated cash flows: roll the rate base forward (opening rate base + capex - regulatory depreciation), apply the allowed return, add recovered depreciation, and subtract capex; discount at the cost of capital. For a regulated-return utility, present-value analysis is the primary method, because cash flows are predictable.
- P/E against rate base growth and earned ROE, built as a sum of parts by jurisdiction, with unregulated segments valued separately on their own multiples or DCF.
- Price to book against earned ROE: justified P/B = (ROE - g) / (ke - g), as for banks.
- EV / RAB, the European and UK convention: a premium to RAB implies expected outperformance of allowed returns or growth.

**Pitfalls.** Treating the stock as a bond and ignoring rate base growth. Ignoring equity issuance needed to fund capex. Counting AFUDC as cash. Assuming earned equals allowed ROE. Comparing P/E across jurisdictions with different regulatory quality. Missing tail liabilities such as wildfire, which a point estimate cannot show; use scenarios. Reading past total returns as a guide: utilities returned 11.3% a year over 1996-2006 mainly through a rerating from a high starting earnings yield, despite low ROIC and growth.

## Questions for the earnings call

- What is the earned ROE by jurisdiction against allowed, and what closes the gap?
- What rate cases are pending, what is requested, and when are decisions due?
- How is the capex plan funded: how much new equity, when, and in what form?
- How much of the load growth forecast is under signed contracts, and who pays for the grid upgrades large customers require?
- What happens to FFO / debt under the plan, and how close is it to rating thresholds?
- What is the customer bill increase implied by the plan, against inflation?
- What recovery mechanisms exist for storm and wildfire costs, and what liability exposure remains?

## What to watch at the macro level

Long-term interest rates, which move both the cost of debt and how investors value stable dividends; inflation, which raises costs before rates reset; electricity demand from data centres, electrification and manufacturing; natural gas prices, which drive customer bills and political pressure on regulators; energy and climate policy, including tax incentives for renewables; and weather and wildfire risk. ETFs owned 7.8% of large-cap utility market value at 30 September 2016.
