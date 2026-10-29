# Multiples and peers

Whether a multiple is built consistently across peers, what it says about the market's expectations, and what multiple the company's returns, growth and risk justify. A multiple is shorthand for a cash-flow model: it hides the forecast rather than avoiding it. Build every multiple the same way, explain it by value drivers, and read it as a statement of expectations, never as a call that a stock is cheap.

## Inputs

| Input | Where it comes from |
|---|---|
| Market cap, EV, multiples, net debt, ROIC, ROE, margins, cash conversion | Key metrics and ratios, for the target and each peer |
| Debt, cash, minorities, leases, pensions, equity-method stakes, attributable net income | Annual statements |
| Consensus sales, EBITDA, EBIT, EPS, FCF, long-term growth | Estimates, with their date |
| Peer candidates | A company screen on sector, size, growth, margin and return; competitors named in filings |
| Non-recurring items, JV income, option and share tables | Filings, by text search and the full document |
| Cost of capital | Not in the data; roic.md, cost of capital inputs |

The reported EV and EBITDA do not show how claims were treated or whether EBITDA was cleaned. Rebuild EV from the balance sheet for the target and every peer, and say which figure is quoted.

## Building the multiple

- **Match claimants.** Equity multiples (P/E, P/B) use parent-shareholder value and net income attributable to the parent. Enterprise multiples put every claimant in the numerator.
- **EV at market values** = market cap + debt (at fair value when yields have moved) + preferred + minorities + unfunded pensions + leases + options - non-operating assets at market value (excess cash, equity stakes, surplus property). Use average or seasonally adjusted net debt. Leases go in EV only when the metric is before rent; core EV goes with a core metric.
- **Clean the metric**, or the multiple capitalises one-offs. Reverse non-recurring items and put the present value of an unpaid cash cost in the equity bridge. Take equity-accounted JV income out of EBITDA and add the stake in the bridge; leaving it in can move EV/EBITDA by two turns. A "one-time" charge in most of the last five years is a cost.
- **Same basis for every peer**: growth, ROIC, margin, cash conversion and leverage.

## Which multiple and which base

| Multiple | Use when | Watch for |
|---|---|---|
| EV/Sales | Losses; restructuring candidates | Margin differences; revenue recognition |
| EV/EBITDA | Peers with similar capital intensity | Ignores capex; invalid across sectors |
| EV/EBITA | Capital intensity differs | Depreciation policy |
| EV/NOPAT | A degeared P/E; tax differences | Subjective adjustments |
| EV/FCF | Smoothed, normalised FCF | Lumpy cash flow |
| P/B, EV/IC | Asset-heavy businesses and banks, always beside ROE or ROIC | Historical-cost book values |
| P/E | Clean earnings, similar leverage | Negative earnings; leverage |
| PEG | Within a sector, similar returns | Ignores ROIC; growth without a spread looks cheap |
| EV per unit of capacity or subscriber | Same-industry checks against replacement cost | Says nothing about profitability |

Bases: historical (average price over past profit, for trading ranges), current (price over trailing and one or two forecast years), forward (price x (1 + cost of capital) - investor cash flow), partial-forward (current equity value with forecast net debt). Prefer forward multiples: historical earnings yields scatter far more across peers (6.0 against 3.7 percent dispersion). Prefer EV/EBITA to EV/EBIT, because acquired-intangible amortisation is an accounting artefact, and to EV/EBITDA where capital intensity or outsourcing differs: two businesses identical except for outsourcing can trade at 6.0x and 8.6x EBITDA and both at 10x EBITA.

Summarise peers with the median, shown with and without any outlier. A market-relative multiple or the company's own history is a benchmark only when returns, growth, rates, risk premium, tax and accounting are unchanged, or at a comparable point in the cycle.

## Peer selection by value drivers

Build two lists: one by industry classification, one by the drivers of value (growth, margin, ROIC, turnover, leverage, capital intensity), and report how many classification peers survive the driver test. A firm in another industry can be closer on drivers than one in the same industry. Also match risk, size, geography, business model, life-cycle stage, and organic against acquired growth.

State the selection rule before showing any multiple: a rule written afterwards tends to pick high-multiple peers. Listed peer sets are small and survivor-biased; for a niche industry, widen to global listings or adjacent sub-industries and say so. Test the median with and without the closest and the most distant peer.

## What a multiple implies

- Returns form: EV / NOPAT = (1 - g / ROIC) / (WACC - g); EV / EBITA = (1 - T) x (1 - g / ROIC) / (WACC - g), with T the operating tax rate. At ROIC = WACC, growth adds nothing.
- One-stage cash form: EV / EBITDA = [FCFF x (1 + g) / (WACC - g)] / EBITDA, which separates cash conversion, risk and growth.
- Two-stage: EV = NOPAT x (1 - gA / RONIC-A) / (WACC - gA) x [1 - ((1 + gA) / (1 + WACC))^N] + NOPAT x (1 + gA)^N x (1 - gB / RONIC-B) / [(WACC - gB) x (1 + WACC)^N], with value-adding growth gA for N years, then gB below WACC. Single-stage forms overstate; prefer two stages.
- Single-stage P/E = (ROE - g) / [ROE x (COE - g)], with COE the cost of equity. ROE 12 percent, g 5 percent and COE 10 percent give 11.7x.
- Linking identities: EV / IC = EV / NOPAT x ROIC; P/B = P/E x ROE; EV / Sales = EV / EBITA x EBITA margin.
- Adjusted PEG = EV multiple / (100 x expected EBITA growth). PEG has no standard growth window, assumes value is proportional to growth, and ignores ROIC.

Split the actual multiple into a steady-state part, 1 / COE for P/E and 1 / WACC for EV/NOPAT, and the turns paid for value creation. A multiple below the steady-state part means the market prices no value creation or expects earnings to fade; it is not by itself a bargain.

Earnings multiples hide ROIC differences at low growth: at 4 percent growth, a 15 percent ROIC gives 2.5x invested capital and 10.6x EBITA, a 10 percent ROIC 1.5x and 9.6x. Show value to invested capital beside earnings multiples, and chart multiples against ROIC or ROE, not growth.

Cross-check with the DCF: back out the multiples it implies; the implied terminal multiple should sit below today's.

| Reference level | Figure | Population and period |
|---|---|---|
| Steady-state P/E | Average 10.4x, standard deviation 2.7 | US market, 1961 to 2013 |
| Forward EV/EBITA | Most 7x to 11x; low growth and margin 7x, low growth and high margin 9x, high growth and margin 11x to 13x | S&P 500 non-financials, December 2009 |

Recompute steady-state levels from the current risk-free rate and risk premium.

## The warranted P/E

Warranted forward P/E = sum over t = 1 to N of (1 + g)^(t-1) x (1 - g / ROIIC) / (1 + k)^t, plus (1 + g)^N / [k x (1 + k)^N], with k the cost of capital, N the years of advantage and year-one earnings of 1.

**Warranted forward P/E at an 8 percent cost of capital over 15 years**

| Earnings growth | ROIIC 4% | 8% | 16% | 24% |
|---|---|---|---|---|
| 4% | 7.1x | 12.5x | 15.2x | 16.1x |
| 6% | 3.3x | 12.5x | 17.1x | 18.6x |
| 8% | NM | 12.5x | 19.4x | 21.8x |
| 10% | NM | 12.5x | 22.4x | 25.7x |

The same 15.0x can mean 12 percent growth at an 8.8 percent ROIIC, 6 percent at 11.0, or 3 percent at 23.0, so state which path the price assumes.

## Banks

No EV multiples: interest is operating. P/B = (ROE - g) / (ke - g); P/E = (1 - g / ROE) / (ke - g). A premium to book needs ROE above the cost of equity.

## Errors

| Error | Fix |
|---|---|
| Leverage differs across peers | EV multiples; when the unlevered P/E is below 1 / cost of debt, P/E falls as leverage rises |
| Cyclical on peak or trough earnings | Normalise to mid-cycle; consensus tends to ignore the cycle, so a forward P/E looks low at the peak and high at the trough |
| High multiple on depressed earnings read as overvaluation | Normalised earnings |
| Loss-making growth company on earnings | Forward EV/Sales with the long-run margin stated |
| Emerging-market listing taken at face value | Prices are weaker anchors; triangulate with a DCF |
