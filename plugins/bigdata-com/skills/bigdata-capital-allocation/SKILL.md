---
name: bigdata-capital-allocation
description: How a company allocates capital, from Bigdata.com financial statements, filings and proxies: five years of sources and uses, whether buybacks and dividends created value, the returns on reinvestment and acquisitions, leverage, and what management is paid for. Use when the user asks about buybacks, dividends, capital returns, M&A track record, capital discipline, or management incentives. Not for a specific announced deal, which bigdata-deal-analysis covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, capital-allocation, roic, expectations
  bigdata-sector-primer: auto
---

# Capital allocation

This skill judges whether management turns cash into long-term value per share, the goal set by Mauboussin's "Capital Allocation" (2015): not growth, not earnings per share, not the share price. It tabulates five years of sources and uses, runs one numeric test per use (organic reinvestment, acquisitions, divestitures, dividends, buybacks, debt), reads what the proxy pays management for, and says what each finding means for value per share. Most actions are sound at one price and unsound at another, so every test compares what was paid with what was received. It gives no composite score and no rating. A narrow question ("was Apple's buyback a good use of cash?") gets the buyback test alone.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-capital-allocation"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Fix the window: five fiscal years by default, longer when the user asks about a decade of M&A or a CEO's tenure. Note the CEO changes in the window from `c_level_leadership`, because a new CEO often shifts the mix. Fix which deals count as material: state the threshold used (for example, a share of the buyer's market cap), since the sources give none.

Ask one question only if the answer changes the work: the user asks about "management" and the company has had several CEOs in the window, or the name is ambiguous. Otherwise state the window and threshold in the header and proceed.

If the company is Private, say there is no share price for the buyback and deal-reaction tests and run the sources-and-uses, reinvestment and deal-price tests from whatever statements and filings Bigdata.com holds. The method does not apply as written to banks and insurers (capital set by regulation), utilities (allowed returns), early-stage companies (ROIIC unstable) and many emerging markets (payout driven by ownership and buyback rules); say which tests were adapted and why.

## Gather

Each step says what it must produce.

1. **Tearsheet.** `bigdata_company_tearsheet` with `sections` set to `company_overview, c_level_leadership, price_performance` first, then `fundamentals`, then `mergers_acquisitions, dividends, estimates`. Request the five fiscal periods before the latest five if the window needs them and the tool's period controls allow it. Done when CFO, capex, depreciation, acquisitions, divestitures, working capital, dividends, buybacks, issuance, SBC, debt, gross and net PP&E, invested capital, the FactSet ROIC field, market cap and EV are in hand for every year, with the deal list and the executives.
2. **Repurchase actuals.** Search and fetch the annual and quarterly filings for the issuer repurchase tables: shares bought and average price paid by period, authorisations, and shares issued under compensation plans. Done when each year has shares bought, the average price, the amount spent and shares issued, or the gap is named. Authorisations are not purchases.
3. **Price series.** `bigdata_computer` for the daily share price over the window and around each material deal announcement, and for the market index over the same days. Done when the average price in each buyback year and the buyer's one-, three- and five-day moves against the index around each announcement can be computed.
4. **Each material deal.** One search per deal for the announcement: price, form of payment, the target's undisturbed price, the synergies claimed by type and timing, the integration cost, and the stated rationale. Then a search for later goodwill impairments, write-downs or disposals of the acquired unit. Done when each deal has its announcement source and its later record, or the gap is named.
5. **Divestitures and spin-offs.** Searches for disposals and spin-offs in the window, with price and rationale. Done when each is listed with its source.
6. **The proxy statement.** Search and fetch the latest proxy (DEF 14A or the local equivalent), and the prior one if the plan changed. Read the long-term plan's metrics and weights, absolute or relative TSR and against which peer group, the performance period, option expense, clawbacks, option repricing, related-party transactions, and the ownership and voting structure. Done when each item is recorded with its section.
7. **What management says it does.** Search for management's stated capital allocation priorities on calls and at investor days, and for insider sales during buyback periods. Done when the stated priorities are quoted with dates, to compare words with actions.
8. **Sector primer.** If the company's sector has a primer in `references/sectors/`, read its capital-intensity and valuation sections.

## Analyse

Load `references/capital-allocation.md` before step 1, `references/roic.md` before step 3 and `references/expectations.md` before step 4. Each step ends in what it must produce.

1. **Sources and uses.** Tabulate five years (method step 1). Sources: CFO, net debt issued, equity issued, divestiture proceeds. Uses: capex, acquisitions, increase in working capital, dividends, buybacks, debt repaid, change in cash, with R&D as a memo line since it sits inside CFO. Done when the table ties to the change in cash each year.

2. **Spending pattern.** Cents invested per dollar of sales change for working capital, net fixed capital and net M&A (formula 2, method step 2), with inflection points and CEO changes marked. The sources give no industry ranges, so compare with the company's own history and named peers. Done when the mix and any shift are stated.

3. **Reinvestment returns against the cost of capital.** From `references/roic.md`: ROIC with and without goodwill on the stated definition, the spread over a stated cost of capital (assumed, with its build), and ROIIC over rolling three and five years. ROIIC is not an economic return and is not compared with the cost of capital; use it for direction, and judge the hurdle with ROIC and the return on new capital against WACC. Add growth capex (capex minus depreciation) as a share of capex, asset life and age (formula 12), and actual growth against ROE times one minus the payout: growth well below it means cash beyond what the business can use (method step 4). Done when level, direction, the spread and the retention test are stated.

4. **The buyback return test, net of issuance.** For each year (method step 5): amount repurchased, average price paid, intrinsic value per share at the time, the buyback return against the cost of equity (formula 4: cost of equity divided by price over value), shares issued in the same year, and the net share count change. Value at the time is an assumption: build it with `references/expectations.md` from information available that year (the steady-state value from that year's NOPAT plus future value creation at the ROIIC and competitive advantage period the business had shown so far), and show the growth the average price paid implied against what the company had delivered to then. Lay the record against the valuation path: did buying rise when the stock was dear and stop when it was cheap? A later price fall does not prove an error. Buying back shares to offset SBC is not value creation. Name the funding source and note insider selling during buybacks. Done when each year has a price-to-value return and a net issuance figure.

5. **The EPS breakeven P/E.** Formula 6: one divided by the pre-tax yield on the cash used (or the pre-tax cost of the debt raised) times one minus the tax rate. A buyback below that P/E raises EPS and says nothing about value. Done when the breakeven sits next to the P/E paid each year, with the sentence that EPS accretion is not value.

6. **Dividend tests.** Coverage by free cash flow after SBC and after maintenance and growth needs; the funding source (free cash flow, debt, offshore cash or new equity, which is a false signal); total and net shareholder yield (formula 7), not dividend yield (method step 6). The sources give no coverage threshold. Done when coverage, funding source and net shareholder yield are stated for each year.

7. **The deal table.** For each material deal (method step 7): premium over the undisturbed price (formula 8); PV of cost and revenue synergies (formula 9) with cost synergies haircut and revenue synergies haircut heavily, against the synergy base rates in table 2 (86 percent of 90 deals captured at least 70 percent of planned cost savings; almost half captured under 70 percent of revenue synergies; McKinsey, verify); deal NPV (PV synergies minus premium); the predicted buyer move against the actual one-, three- and five-day move; SVAR and premium at risk (formula 10); payment form against the five-day base rates by payment; strategic category and its success rate from table 1; fit with McKinsey's five archetypes; return on price paid against the cost of capital (formula 11); and the later record of impairments and disposals. Done when every material deal has its row.

8. **Divestitures.** Each disposal or spin-off with its price against the unit's value to the company, and whether units earning below the cost of capital remain (method step 8). Done when each is listed with its rationale.

9. **Leverage against rating medians.** EBIT over interest and debt over total capital against the S&P medians in table 6 (US three-year medians 2011-2013, verify), and whether payouts were financed by borrowing (method step 9). Value barely changes with leverage except at coverage below about 2. Done when coverage and leverage are placed against the table; for a full credit view, hand off to `bigdata-credit`.

10. **The incentive review.** Classify each long-term plan metric (absolute or relative TSR, EPS, ROIC or capital efficiency, revenue, cash flow), the performance period, option expense, clawbacks, repricing and related-party dealings (method step 10), against the 2014 Cook survey shares in table 7 (verify). Absolute TSR is mostly luck; EPS and revenue targets can drive buybacks and deals that lift the metric without value. Note the ownership and voting structure, since it decides whom the plan serves. Answer the question: if the plan and value per share conflict, which way does the CEO go? Done when each metric is classified and the conflict question is answered.

11. **Verdict per use and what it means for value.** For each use, one line: value created, value neutral, value destroyed or not determinable, with the test that decides it and its basis label (method step 11). Then what each finding means for value per share going forward: whether reinvestment at the current spread adds value (the value-trigger rule in `references/expectations.md`: where returns on new capital sit near the cost of capital, growth adds nothing), the value transferred to sellers in buybacks above value or premiums above synergies, in currency per share, the net share count trend, and whether the incentive plan makes the pattern likely to continue. No composite score. Done when every use has its line and the forward implication is stated.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) capital allocation, FY<first> to FY<last>, <date>
Data as of: statements <latest fiscal period>; price <date>; proxy <year>; newest document <date>.

## The reading
Four to eight sentences: where the cash went, which uses created or destroyed value and by how much
per share, what management is paid for, and what the pattern means for value per share from here.

## Sources and uses
| Line | FY-4 ... FY0 | Total | Basis | Source |
Then the cents-per-dollar-of-sales-change line, with CEO changes marked.

## Reinvestment returns
| Year | ROIC ex goodwill | ROIC incl goodwill | WACC (assumed) | Spread | ROIIC 3y | ROIIC 5y | Growth capex share | Basis | Source |
The retention test in one line.

## Buybacks
| Year | Spent | Shares bought | Average price | Value per share at the time | Return vs cost of equity | Shares issued | Net share change | EPS breakeven P/E | P/E paid | Basis | Source |

## Dividends
| Year | Dividends | FCF after SBC | Coverage | Funding source | Net shareholder yield | Basis | Source |

## Acquisitions and divestitures
| Deal | Date | Premium | PV synergies (cost / revenue) | NPV | Predicted vs actual buyer move | SVAR | Payment | Category and base rate | Return on price paid | Later impairment or disposal | Source |
Disposals and spin-offs below.

## Leverage
EBIT / interest and debt / total capital against the rating medians; payouts financed by debt.

## Incentives and governance
| Plan element | Detail | Source |
The conflict question answered in one line.

## Verdict by use and what it means for value
| Use | Verdict | Deciding test | Value per share effect | Basis |
Then the forward implication in two to four sentences.

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. The cost of equity, the cost of capital and value per share at each buyback date appear once in an Assumptions line with their basis and a sensitivity. For a narrow question, answer with the relevant test, its table and the sources, and keep the footer.

## Checks before sending

1. The sources-and-uses table ties to the change in cash each year.
2. Buybacks use actual repurchases and prices paid, not authorisations, and are shown net of issuance.
3. Value per share at each buyback date is labelled assumed, built from information available at the time.
4. The EPS breakeven P/E appears with the statement that accretion is not value.
5. ROIIC is used for direction only and never compared with the cost of capital.
6. Every material deal has premium, synergies against base rates, SVAR and the later record, or a named gap.
7. Leverage is placed against the rating medians with their sample and period.
8. Each incentive metric is classified from the proxy, with its source.
9. No composite score, rating or recommendation; each use has its own verdict and basis.
10. Dated base rates carry "(verify)" and their period.

## Hand-offs

- The user asks about one announced or rumoured deal: `bigdata-deal-analysis`.
- The user wants the moat or industry structure behind the returns: `bigdata-moat`. The debt and refinancing in depth: `bigdata-credit`.
- After delivering, make one offer: a monitor on the company's buyback, dividend and M&A announcements, or save the report to the user's Bigdata.com account. Act only on a clear yes.
