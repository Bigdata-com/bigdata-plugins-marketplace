# What the price implies

What the company must deliver for today's price to be fair: growth, return on new investment, and years of excess return. Measure the bar before judging it, then say whether the company clears it. Keep what the company will deliver apart from what the price already assumes: a good company is a good stock only when the price misjudges the fundamentals.

## Inputs

| Input | Where it comes from |
|---|---|
| Market cap, enterprise value, net debt | Company key metrics. Add minorities, preferred stock, pension deficit and leases from the balance sheet when the EV figure leaves them out |
| EBIT, income tax, pretax income, sales, capex, depreciation, working capital, invested capital | Annual statements, five fiscal years |
| Tax rate | Income tax / pretax income, normalised for one-off items |
| Consensus sales, EBIT and EPS to four years out, long-term growth | Estimates, with their date and the number of estimates |
| NOPAT | EBIT x (1 - tax rate). Next year's NOPAT uses consensus EBIT |
| Net investment | Change in working capital + capex - depreciation + acquisitions. Treat large R&D as investment |
| Return on incremental invested capital (ROIIC) | (next year's NOPAT - this year's NOPAT) / this year's net investment, as a three-year rolling average. A single year is noise or operating leverage |
| Cost of capital | Not in the data. Cost of equity = 10-year government yield in the currency of the cash flows (from the country data) + beta x equity risk premium, with the beta checked as valuation.md sets out. WACC weights it with the after-tax cost of debt at market values. State each input once and show plus and minus one point |

Free cash flow here is cash earnings minus investment, where cash earnings = sales x operating margin less cash taxes.

## Steady state and value creation

- Firm value = steady-state value + future value creation.
- Steady-state value = NOPAT / cost of capital. This is the operating business with current profit lasting forever and new investment earning only its cost of capital. Excess cash is added once, in the equity bridge, never inside the perpetuity.
- Future value creation = net investment x (ROIIC - cost of capital) x CAP / [cost of capital x (1 + cost of capital)], where CAP is the competitive advantage period in years, the time over which new investment earns more than its cost.
- Equity value = steady state + future value creation + excess cash - debt and other senior claims.
- Steady-state P/E = 1 / cost of equity. The forward P/E divided by it is the share of the price paid for growth: 1.0 means the market pays for none; below 1.0 it expects earnings to fade; the higher above 1.0, the more rests on future value creation.

## Implied growth

From enterprise value = next year's NOPAT x (1 - g / ROIIC) / (WACC - g), where g is perpetual NOPAT growth and g / ROIIC the reinvestment rate:

g = (EV x WACC - NOPAT) / (EV - NOPAT / ROIIC)

Substitute the result back to check it. The formula is undefined when ROIIC equals WACC, because growth then changes nothing, and it needs g below WACC. When EV x WACC is below next year's NOPAT the price implies shrinking profit: value = NOPAT x (1 + g) / (cost of capital - g) with g negative, and a low multiple can be fair.

For a segment or a growth path rather than perpetual growth, solve for the revenue path the price needs: value the other segments at a stated multiple, assign the remainder to the segment, and find the growth rate that, at a stated margin and return on new capital over a stated number of years, produces that value. State each assumption once and show the range across the retail multiple, the margin and the discount rate.

## Implied competitive advantage period

CAP = (EV - steady-state value) x cost of capital x (1 + cost of capital) / [net investment x (ROIIC - cost of capital)], with next year's net investment held constant each year.

Market-implied CAPs have averaged about 8 years, about 5 in highly competitive industries and about 15 in stable ones (US companies, 1976 to 2007). CAPs cluster by business type, so judge one against a group of similar companies, not in isolation.

## Which revision moves value

Classify on the three-year rolling ROIIC against WACC:

- ROIIC near WACC: the return on new investment moves value; growth does not.
- ROIIC well above WACC: sales growth moves value.
- ROIIC below WACC: faster growth destroys value.

Then run the cases on the driver that matters: if consensus sales growth moves two points either way, what happens to margin, investment and value. Sales changes reach margins by more than analysts assume, on the way up and on the way down.

## Cross-checks

- **Warranted forward P/E** for g, ROIIC, a cost of equity k and N years of advantage: the sum over t = 1 to N of (1 + g)^(t-1) x (1 - g / ROIIC) / (1 + k)^t, plus (1 + g)^N / [k x (1 + k)^N]. The same multiple can mean fast growth on a thin spread or slow growth on a wide one, so state which the price assumes.
- **Implied terminal multiple** from any DCF: terminal value over final-year EBITDA or NOPAT. It should sit below today's multiple; at or above it, the valuation has an error or rests on an unusually strong story. Terminal value is typically 70 to 80 percent of EV with five explicit years and 50 to 60 percent with ten.
- **Base rates.** Place the implied growth in the company's size class (base-rates.md). A bar in a rare part of the distribution needs a specific, evidenced reason.
- **Index context.** Steady-state value has been about two-thirds of the S&P 500's value on average since 1961 and future value creation about one-third.

## Special cases

- Banks: price to book against return on equity (P/B = P/E x ROE), not an enterprise-value formula.
- Cyclicals: normalise NOPAT to mid-cycle before solving, and state the margin used.
- Loss-making or early-stage companies: next year's NOPAT is not meaningful. State the margin path assumed and solve for the revenue the price needs.
- Companies with different leverage: compare on unlevered multiples.
- Non-US listings: the risk-free rate is the one for the currency of the cash flows, not the domicile, adjusted when the government bond carries default risk.
- A company's own past multiple is a target only when returns, growth, rates, the risk premium, tax and accounting are unchanged.
- A near-term miss is not a change in long-term value: the price capitalises many years of cash flow.
