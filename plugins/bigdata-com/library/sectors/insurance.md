# Insurance

This primer covers property and casualty (P&C, non-life) insurers, life insurers and reinsurers. Insurance brokers take no underwriting risk and are fee businesses; value them with the standard enterprise methods and `roic.md`. Managed-care health insurers run on medical cost ratios and membership and fit this primer only in part. The source texts say little about insurers directly; most of what follows is judgment and is marked "(verify)". No figure here is a current fact.

## How the sector makes money and what drives value

An insurer collects premiums now and pays claims later. It earns from two sources:

- Underwriting: premiums earned minus claims and expenses. A P&C insurer that prices well makes an underwriting profit; many run near breakeven and rely on investment income (judgment).
- Investment income on the float: the premiums held until claims are paid, plus the insurer's own capital, invested mostly in bonds.

For a P&C insurer the value drivers are the combined ratio across the pricing cycle, the adequacy of loss reserves, the size, growth and cost of the float, the yield earned on it, and the capital the regulator and rating agencies require per unit of premium. For a life insurer they are the spread between the investment yield and the rate credited to policyholders, mortality and morbidity margins, fees on assets in unit-linked and variable products, persistency (how many policies stay in force), and the value of new business. In both, value depends on return on equity against the cost of equity and on how much of the earnings can be paid out without breaching capital requirements (judgment, applying McKinsey ch. 36 bank logic, which the source states for banks only).

## Metrics that matter

| Metric | Definition | Why it matters | Indicative range (judgment, verify) |
|---|---|---|---|
| Loss ratio | claims and claim expenses / earned premium | Pricing and claims trend | varies by line |
| Expense ratio | underwriting expenses / earned (or written) premium | Scale and distribution cost | about 25% to 35% for P&C |
| Combined ratio | loss ratio + expense ratio | Below 100% is an underwriting profit | about 90% to 105% across a cycle for commercial P&C |
| Accident-year combined ratio ex catastrophes | combined ratio for the current year's policies, excluding cat losses and prior-year reserve changes | Underlying profitability | the line to trend |
| Prior-year reserve development | change in estimates for past years' claims | Reserve adequacy; favourable releases flatter earnings | persistent adverse development is a warning |
| Catastrophe losses vs budget | cat losses / the company's cat load | Volatility and pricing of cat risk | compare over five or more years |
| Renewal rate change and premium growth | price change on renewing policies; net premiums written growth | Where the pricing cycle is | read against loss-cost trend |
| Net investment yield | net investment income / average invested assets | Return on float | moves with reinvestment rates |
| Solvency ratio | available / required capital (Solvency II SCR coverage; US risk-based capital) | Payout and growth capacity | large European insurers often about 150% to 250% SCR coverage |
| Operating ROE | operating earnings / average equity excluding unrealised gains and losses | The return that drives price to book | about 8% to 16% |
| Life: value of new business, new-business margin, contractual service margin (CSM) | present value of profits on new policies; CSM is the unearned profit under IFRS 17 | Growth and quality of new sales | trend, not level |

These come from the earnings release, the financial supplement and the solvency reports; use `bigdata_search` and `bigdata_fetch_document`.

## Financial statements and accounting traps

- Claims reserves, including incurred-but-not-reported losses, are estimates. Earnings depend on them, and long-tail lines (liability, workers' compensation) take years to settle. Watch insurer loss reserves (Berkowitz, Security Analysis 6th ed., pp. 341-342).
- Reserve releases from prior years raise reported earnings without new business profit. Separate them out.
- Realised investment gains are not earning power (Graham and Dodd, Security Analysis, pp. 417-418). Use operating earnings.
- Growth can depress reported earnings when acquisition costs are expensed. Adding auto insurance customers may cost up to 20% to 30% more than their first-year premiums; the part that is not replacing lapsed customers is investment in growth, so a growing insurer such as GEICO reports earnings below steady-state free cash flow (Berkowitz, Security Analysis 6th ed., p. 342; historical). Ask whether new-business costs are expensed or deferred.
- Rising rates create unrealised losses on the bond portfolio that cut book value through other comprehensive income while the liabilities may not be marked. Compare ROE and P/B on equity excluding these marks as well as including them.
- Life accounting changed: IFRS 17 and the US long-duration targeted improvements took effect around 2023 (verify by company). Profit on new business now sits in the CSM and emerges over time. Do not compare pre- and post-change figures without restating.
- Reinsurance recoverables are credit exposure to reinsurers.
- Payoffs are spread over years and depend on mortality, interest, defaults and currency, so insurers' true returns and risks are hard to see from outside (McKinsey ch. 16). Klarman avoided P&C insurers as having "unanalyzable assets and liabilities" (Margin of Safety, 1991); the principle that remains is to state plainly what cannot be checked.
- The accrual, EBITA and working-capital tests in `earnings-quality.md` do not apply; reconcile earnings to the change in equity.

## Profit pool and competitive dynamics

Insurance is fragmented globally: 441 listed firms and a four-firm revenue concentration of 19.9% (Mauboussin and HOLT, Global Industry Profit Pools, July 2016, data for 2015; verify). Individual lines and countries are more concentrated (judgment). P&C pricing moves in a cycle driven by the supply of capital: after good years capital enters and prices soften; after large losses or capital depletion prices harden (judgment). Reinsurance also competes with capital-markets capacity such as catastrophe bonds (judgment, verify). Advantages come from underwriting data and discipline in specialty lines, low-cost distribution in personal lines, and scale in claims handling. In life and annuities, insurers backed by asset managers and private capital compete on investment yield, often through private credit (judgment, verify). Capital rules limit capital allocation; understand them before judging buybacks or growth (Mauboussin, Capital Allocation, 2015, p. 45).

## Persistence and fade

- The gross profitability, operating margin and operating leverage tables in `base-rates.md` exclude financials (Base Rate Book, 2016, sections 2.5, 2.6, 2.8). Do not apply them to an insurer.
- The CFROI table includes financials, measured by HOLT on cash flow return on equity: four-year r 0.43, median 7.5%, mean 8.3% (global, 1983-2015); older cut r 0.43, mean 6.8% (1986-2012). Insurers are not shown separately; the group also holds banks and, before 2016, REITs (judgment, verify).
- Not in the sources: an insurer-specific fade rate or combined-ratio base rate. Use the company's and peers' own ten-year combined ratio and reserve development history and say so.

## Valuation conventions and pitfalls

**Why enterprise multiples and the ROIC build do not apply.** An insurer's main liabilities are policyholder reserves, the float. They fund the investment portfolio, and the income on that portfolio is operating income. There is no clean split between operating assets and financing, the investment portfolio is not "excess cash" that can be netted, and the binding constraint is regulatory capital, not leverage chosen by management. EV/EBITDA and an enterprise DCF at a WACC therefore have no consistent basis. Use return on equity on adjusted net income against the cost of equity, and value cash flow to equity at the cost of equity (Mauboussin and Callahan, Calculating ROIC, 2014, p. 11; McKinsey ch. 36 for the same logic in banks).

**The alternatives.**

- Price to book (or tangible book, and book excluding unrealised marks) against sustainable operating ROE: justified P/B = (ROE - g) / (ke - g). A premium to book needs ROE above the cost of equity. At an assumed ke of 10% and g of 3%, ROE of 10% and 15% justify about 1.0x and 1.7x book (derived).
- P/E on operating earnings, normalised for a catastrophe load at its long-run average, with reserve development and realised gains removed.
- Equity DCF on distributable cash: the dividends the operating subsidiaries can pay after holding target solvency capital (judgment; McKinsey ch. 36 cash flow to equity applied to insurers).
- Life insurers: embedded value or price to embedded value, a multiple of value of new business, and, under IFRS 17, shareholders' equity plus CSM net of tax as a proxy for value (judgment, verify).

**Pitfalls.** Capitalising a low-catastrophe or reserve-release year. Comparing price to book across insurers with different exposure to rate-driven book marks. Ignoring holding-company leverage when subsidiaries are well capitalised. Assuming investment yields stay at today's level when the portfolio reprices. Using one point estimate: run scenarios on cat losses, reserve development and rates.

## Questions for the earnings call

- What is renewal rate change by line against your loss-cost trend, and where is the gap closing?
- Which accident years drove reserve development, and in which lines?
- What was the catastrophe load against actual losses, and what changed at the latest reinsurance renewal?
- What is the new-money yield against the portfolio yield, and how fast does the book reprice?
- What is the solvency ratio sensitivity to rates, spreads and equity markets, and what level governs capital return?
- How much of the investment portfolio sits in private credit or other less liquid assets?
- Life: how did lapses, the CSM roll-forward and new-business margin move?

## What to watch at the macro level

Interest rates (investment income, unrealised marks, life liability values); inflation, especially in claims severity and litigation costs in long-tail lines; catastrophe frequency and severity, including climate trends; credit spreads and defaults in the portfolio; equity markets for variable and unit-linked products; reinsurance pricing; and capital regulation (Solvency II review, US risk-based capital, group capital standards; verify current status).

## Sources

Mauboussin and Callahan, Calculating ROIC (2014); McKinsey, Valuation 5th ed. (2010), ch. 16 and 36; Graham and Dodd, Security Analysis 6th ed. (2009), Berkowitz essay and pp. 417-418; Klarman, Margin of Safety (1991); Mauboussin, Base Rate Book (2016), Reversion to the Mean (2013), Capital Allocation (2015); Mauboussin and HOLT, Global Industry Profit Pools (2016). The metrics, ranges, accounting changes and competition notes are judgment.
