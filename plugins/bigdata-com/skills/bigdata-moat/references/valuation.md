# Valuation

What one share is worth under stated assumptions, and what must be true for the price to be right. Use an enterprise DCF that ties cash flow to growth and returns, so nothing grows without the investment it needs. End in a range with probabilities, never a point or a price target. Most DCFs fail from inconsistency, not arithmetic.

## Inputs

| Input | Where it comes from |
|---|---|
| Statements, PP&E, invested capital, leases, stock compensation, net debt, market cap, EV, price, 52-week range | Company statements, key metrics and overview, five annual periods |
| Consensus sales, EBIT, EBITDA, capex, FCF, long-term growth to four years out | Estimates, with their date |
| Tax, pension and option notes; restricted and overseas cash; share count; minorities; accruals | Filings |
| Risk-free rate | 10-year government yield in the currency of the cash flows, from the country data |
| Equity risk premium, beta, credit spread, target weights | Not in the data. State each once, with its date |

Treat consensus as biased upward: one-year-out S&P 500 earnings forecasts have run 10 points or more above actuals.

## Historical returns and tax

Rebuild at least five years of EBITA, operating working capital, invested capital without excess cash, and ROIC with and without goodwill, split into margin and turnover (roic.md, ROIC decomposition). Use continuing, core and controlled operations. Set the operating tax rate on EBITA from the tax note, excluding one-offs and the interest shield; never the levered effective or statutory rate.

## Cost of capital

WACC = D/V x kd x (1 - Tm) + E/V x ke, with ke = rf + beta x ERP, at target market-value weights.

- Risk-free rate: 10-year yield in the currency of the cash flows, not the domicile; never a bill rate. Prefer an implied equity risk premium.
- Beta: 60 monthly returns against a broad index, with standard error and R-squared. Blume-adjust the regression (two-thirds raw plus one-third of 1.0) and set it beside the peer median unlevered beta relevered to the target structure (unlevered = levered / (1 + D/E); roic.md, cost of capital, gives the version with tax) and the sector beta. When the regression is far from both, above about 1.6 for a large profitable company or with R-squared below 0.3, use the peer or sector figure and say why.
- Sanity range: for US large caps at a 5 percent risk-free rate, the cost of equity sits between roughly 8 and 12 percent. Outside it, the input is wrong more often than the market.
- Cost of debt: yield to maturity on long-term debt when investment grade. Below investment grade the yield overstates the expected cost; use adjusted present value.
- Checks: cost of equity above cost of debt; risk premium above the credit spread.
- Show prevailing and normalised WACC, and the rate at which the base case equals the price, so the reader sees how much of any gap is the discount rate.

## Horizon, revenue and margins

Set the horizon by maturity, length of advantage and visibility, typically 10 to 15 years with 5 to 7 in detail, fading growth to a terminal rate at or below the economy's. Spend most time on revenue: bound it top-down (market x share) and bottom-up (customers x revenue per customer), and place the growth in its size class (base-rates.md, real sales growth by starting size). Compound price, volume and currency: (1.04)(1.12)(0.95) - 1 = 10.7 percent, not 11.0. Forecast costs as ratios to their drivers.

## Reinvestment and consistency checks

- Capex bottom-up; depreciation by vintage over asset lives.
- Capex = change in net PP&E + depreciation; net investment = capex - depreciation = change in net PP&E. Never use change in gross PP&E.
- Growth = RONIC x net investment / NOPAT; FCF = NOPAT - net investment.
- Each forecast year: ROIC = NOPAT margin x capital turnover, and implied growth = ROIC x reinvestment rate against forecast growth. Flag a turnover jump (1.2x to 3.0x in five years) and any negative implied capex.

## Continuing value

Value-driver formula: value = NOPAT(t+1) x (1 - g / RONIC) / (WACC - g), with g perpetual NOPAT growth and RONIC the return on new capital. At RONIC = WACC it reduces to NOPAT(t+1) / WACC.

- Use NOPAT at mid-cycle revenue and margin.
- RONIC equals WACC for most companies; near the later-year ROIC only for an evidenced durable advantage, and then with modest growth.
- Discount from the end of the last explicit year.
- Report the terminal share of EV and the implied terminal EV/EBITDA, which should sit below today's. Typical terminal share: 70 to 80 percent with 5 explicit years, 50 to 60 with 10; above 100 when the explicit years consume cash.
- Cross-check: invested capital + present value of each year's invested capital x (ROIC - WACC) must equal the DCF value.

## Equity bridge

Deduct only non-equity claims in EV; add only equity claims outside it. Show each item in total and per share.

- Add liquid securities, not only cash, less operating cash (2 percent of sales for steady companies, 5 for less predictable or faster-growing ones); overseas cash net of repatriation tax; non-core and joint-venture stakes at market value. Remove restricted cash if it sat in the cash line.
- Deduct debt at fair value when rates have moved, pension deficit after tax, leases only if cash flows were lease-adjusted, minorities at market value, unpaid restructuring and litigation at present value, options and RSUs.
- Shares from filings, not aggregators; not diluted when options were deducted at option value.
- Mid-year convention: present value x (1 + WACC)^0.5. Roll forward: value x (1 + r) - distributions per share.

## Sensitivity and cases

Show a WACC by terminal-growth table of value per share, base case in the centre. Run base, downside and upside through the whole model, with second-order effects on reinvestment and margin and probabilities summing to 100 (forecasting-discipline.md, scenario weights). Average the values, not the inputs; scenario equity = max(scenario EV - claims, 0). Put uncertainty in the cases, not in the discount rate or a haircut. Half a point on WACC moves value about 10 percent at a forward P/E of 15 to 16, so plus or minus 15 percent is realistic precision.

## Benchmark against the price

Compare value per share with the price and 52-week range and explain any gap in economic terms; assume the market is right without a specific reason otherwise. Solve for the growth and return on new capital the price implies (expectations.md, implied growth).

## Reference figures

- ROIC persistence, 1995 to 2005: 67 percent of companies above 20 percent stayed above 20; 57 percent of those below 10 stayed below 10.
- Growth, 1965 to 2007: median real revenue growth 5.4 percent a year; the top quintile's edge fell under 5 points by year 5 and under 2 by year 10.

## Error catalogue

| Error | Fix |
|---|---|
| Horizon short or arbitrary | Set by maturity and advantage; three stages when growth is high |
| Terminal value dominates | Present-value split and implied terminal multiple |
| Terminal value as FCF x (1 + g) / (WACC - g) with unrelated g | Value-driver formula |
| Capex as a share of revenue; depreciation forced to capex | Bottom-up capex; vintage depreciation |
| ROIC unchecked | ROIC, turnover and implied growth each year |
| Interest shield counted twice | Operating tax on EBITA; shield only in WACC |
| Cash or JV income counted twice | One debt approach; JV income out of FCFF, stake in the bridge |
| Cash flow and discount rate mismatched | FCFF at WACC; FCFE at levered cost of equity |
| Currency or inflation mismatched | Risk-free in the cash-flow currency; nominal with nominal |
| Beta or premium unchecked | Cost of capital checks above |
| Bridge or share count wrong | Item-by-item bridge; shares from filings |
| Stock compensation counted twice or not at all | Past awards in bridge or share count; future awards in the forecast |
| Single point | Sensitivity table and three cases |
| Not benchmarked | Price and 52-week range |
| Base year extrapolated naively | Working capital at a constant share of revenue |

## Special cases

- **Banks.** Interest is operating: no enterprise DCF, no net debt. Value cash flow to equity at the cost of equity: CFE = net income - increase in book equity + other comprehensive income, with equity growth set by the capital ratio (Tier 1 or CET1 on risk-weighted assets). CV = NI(t+1) x (1 - g / RONE) / (ke - g); when RONE = ROE, P/B = (ROE - g) / (ke - g), so P/B above 1 needs ROE above ke. Let ke move with leverage and asset mix. Model through-the-cycle loan losses by category, test reserves, forecast margins from forward rates, and split net interest income into spread, maturity mismatch and matched-maturity charges.
- **Cyclicals.** Build a normal-cycle case on mid-cycle profit and ROIC and a new-trend case extrapolating recent results, each with an economic rationale (demand, capacity, entry and exit), and weight them. Consensus tends to ignore the cycle; prices behave like a 50/50 blend of perfect and zero foresight.
- **High growth** (organic growth above 15 percent a year). Start from the future: size the market, cap share by a saturated market, take long-run margin and capital intensity from mature analogues, then work back and weight scenarios to growth base rates. Compare the ramp with the analogues' median, not mean. Negative invested capital makes ROIC meaningless; expensed marketing and technology overstate early returns.
- **Emerging markets.** Scenario DCF with at least a business-as-usual and a crisis case, at a global investor's cost of capital with no country premium; a premium on probability-weighted cash flows double counts risk. Local risk-free = (1 + US rf) x (1 + local inflation) / (1 + US inflation) - 1. Cost of debt = dollar risk-free + systematic spread + inflation differential. Triangulate with multiples. State the crisis probability and its basis: twenty emerging economies had a real GDP fall above 5 percent about once every five years.
- **Multi-business.** Value each unit on its own ROIC, growth and WACC (peer beta relevered to the unit). Eliminate intercompany sales, value corporate costs as a negative unit, reconcile to consolidated NOPAT and capital. Sum of the parts holds only against peers of similar performance.
- **Distressed.** Do not deduct the market value of debt. Per scenario, equity = max(EV - face value of claims, 0), then weight.
- **Inflation and currency.** Match inflation in cash flows and discount rate. Translation gains are not cash flow. Never apply the parent's WACC to a subsidiary's local-currency cash flows.

## Interpretation and limits

- When the terminal share is large, check value by business unit and economic profit before concluding value arises after the forecast.
- When RONIC is set above WACC, the moat evidence must support it; RONIC = WACC is the default, not a haircut.
- When an exit multiple comes from today's market or a recent deal, it is circular; use the value-driver formula.
- When stock compensation is material, state its treatment once and count each award once.
