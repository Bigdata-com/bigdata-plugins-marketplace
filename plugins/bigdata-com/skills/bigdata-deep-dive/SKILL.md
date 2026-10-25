---
name: bigdata-deep-dive
description: >-
  Full company research: economics, moat, earnings quality, capital allocation, what the price
  implies, valuation range, risks, catalysts. Use for a deep dive, initiation, investment memo,
  due diligence. Not one page: bigdata-quick-take.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, roic, valuation, multiples-and-peers, earnings-quality, capital-allocation, industry-structure, downside-and-catalysts, forecasting-discipline
  bigdata-sector-primer: auto
---

# Deep dive

This skill writes the full research report on one company: how the business makes money and how well, who it competes with and what protects it, whether the reported earnings are the real earnings, what management does with the cash, what the price assumes, what the company is worth under three cases, what breaks it, and what to watch. It runs four to eight pages and takes a few dozen tool calls. It gives no rating.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-deep-dive"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A company with one segment and no acquisitions needs no sum-of-the-parts and no deal history; a bank needs the primer's statements, not an enterprise DCF.

## Scope the request

Resolve the company with `find_securities`. Establish the reader and the angle: an investor testing a long or short idea, a corporate strategy team profiling a competitor, customer or supplier, someone running due diligence on a target, or a user with one question they want answered. Write the implications for that reader; the evidence, the arithmetic and the no-rating rule are the same for all of them. Fix the depth: a full report by default, or the sections they named. Ask one question only if the name is ambiguous or the user asked for something the report does not cover. Done when the company is resolved and the reader, angle and depth are fixed.

If `find_securities` marks the company Private, run the report on what the tearsheet and the documents give (the tearsheet works for private companies with different content). Skip the steps that need a share price or consensus (what the price implies, market multiples, positioning), and say in the header line and in Gaps which figures are missing. Done when the list of steps that cannot run is written down.

## Gather

The report rests on the tearsheet, the last three calls, the latest annual filing, the deal history, the peers and the calendar. Each step says what it must produce.

1. **Tearsheet in three calls.** `company_overview, c_level_leadership, mergers_acquisitions`; `financial_statements, financial_ratios, key_metrics` with `interval` annual; `analyst_estimates, revenue_segmentation, fund_trends_history`. The statements stop at five fiscal years; say so in Gaps. `c_level_leadership` and `mergers_acquisitions` need FactSet access: if either comes back empty, search for the executive team and for the deal history (announcements, prices, premiums) instead. Done when five annual periods of statements, the segments, consensus to the horizon, holders, deals and the executive team are in hand, or each missing one is named for Gaps.
2. **The last three earnings calls**, by `bigdata_search` with the reporting period filter and `bigdata_fetch_document`. Done when guidance history, the recurring questions and management's own framing of the drivers are known.
3. **The latest annual filing**, by search and fetch, read for the business description, the segment economics, the risk factors that changed from the prior year, related-party items, the pension and lease notes, and the share-count and compensation notes. Done when each of those is noted with the page or section.
4. **Industry evidence.** Three to six searches, one aspect each, following the evidence table in `references/industry-structure.md` (market shares, pricing, entrants and exits, regulation, suppliers and customers with power, technology that could change the structure). Done when each row of that table has evidence or an explicit gap.
5. **Peers.** `bigdata_screen_companies` on the industry and size, then two tearsheet calls per peer, `financial_statements, financial_ratios` with `interval` annual and `key_metrics, analyst_estimates`, for four to eight peers chosen by value drivers (`references/multiples-and-peers.md`). Done when the peer table in that file can be filled.
6. **Sell-side and news.** Searches for research notes and news over the last twelve months on the company's strategy, its capital allocation and its controversies. Done when three to five controversies are listed, each with the argument on both sides and a dated source.
7. **Dated events.** `bigdata_events_calendar` for the next earnings date and conferences over twelve months; then searches of filings and news for dated events the calendar does not carry (shareholder votes, court and regulatory dates, debt maturities, product launches, lock-up expiries). Done when each event has a date or a window and a source.
8. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the metrics, accounting-traps and valuation-conventions subsections. Done when the sector's metrics and accounting traps are noted, or the company has no primer and that is noted.

## Analyse

Each step names its reference file and the step numbers it runs. Each ends in what it must produce.

1. **The business.** How the company makes money by segment and geography, from the segment table and the filing: revenue, growth, margin and capital employed by segment where disclosed. Done when a table shows each segment's share of revenue and, where disclosed, of operating profit, and the text names the largest shift over the periods returned.

2. **The economics.** `references/roic.md` steps 1 to 11: NOPAT at the operating tax rate, invested capital from both sides, ROIC with and without goodwill, the margin and turnover split, ROIIC as a three-year rolling figure (labelled; the yearly series only shows change), and the spread. Build the cost of capital once here, by `references/valuation.md` step 3, and use the same figure in steps 6 and 7. Compare with the FactSet ROIC field and say which one the report quotes. Done when the ROIC series over the five annual periods is tabled with the decomposition and the spread at the stated cost of capital.

3. **Industry structure and moat.** `references/industry-structure.md` steps 1 to 12, with the profit pool over the five annual periods returned (the method's ten-year comparison is not available). Bound the duration judgment by the sector's persistence figure in `references/roic.md`. Done when each of the method's output lines is stated with evidence or a gap.

4. **Earnings quality.** `references/earnings-quality.md` steps 2 to 5, 10 and 13: the accrual ratio over the four years five annual periods allow, the EBITA rebuild, one-offs counted by recurrence, provisions, the earnings-to-equity residual, and the flags with severity. Stock compensation stays inside net income as a cost; never add it back or deduct it again (formula 8). Quote Piotroski and Altman Z as reported, with no zones. Done when the flags table is complete and the rebuilt EBITA sits next to reported operating profit.

5. **Capital allocation.** `references/capital-allocation.md` steps 1, 5, 6, 7 and 9. The statements carry buybacks, dividends and issuance by year; take the year-average price from `bigdata_computer` on the daily series and run the buyback test (formula 4) at that price, net of issuance, with the value per share at the time stated as assumed. Hand off to `bigdata-capital-allocation` for incentives and the full treatment. Done when the sources-and-uses table ties to the change in cash, each buyback year has a price-to-value line, and each major deal has its row.

6. **What the price implies.** `references/expectations.md` steps 1 to 7: steady state against future value creation (formula 1), the implied growth and competitive advantage period at the step 2 cost of capital (formulas 2 and 3a), the warranted against the actual multiple, and the base-rate sentence for consensus growth from `references/base-rates.md`. Done when the report says what the market assumes in growth, return and years.

7. **Valuation range.** `references/valuation.md` steps 4 to 12, with the horizon set by maturity, the step 3 advantage judgment and visibility, and the equity bridge per share item by item (step 10). Weight the three cases with `references/forecasting-discipline.md` rule 2 and cross-check with the comps table from `references/multiples-and-peers.md`. Apply the special case for a bank, a cyclical, a high-growth company or a conglomerate. Done when the range, the expected value and the WACC-by-growth table are complete and the terminal share and implied terminal multiple are stated.

8. **Premortem, risks and kill criteria.** First run the premortem in `references/forecasting-discipline.md` rule 3: assume the reading of the company has proved badly wrong a year from now and write why. Then `references/downside-and-catalysts.md` steps 2 to 6 and 9: the floors, permanent against temporary loss, why it is priced where it is, the latest quarterly 13F changes from `fund_trends_history` (lagged; short interest and option prices are not in Bigdata.com), the disconfirming search, and the kill criteria. Done when at least three premortem reasons map to a driver or a kill criterion, each risk has an early signal, and each kill criterion has a driver, a threshold and a date.

9. **Catalysts and what to watch.** The dated events from Gather step 7, scored with tables 2 and 3 of `references/downside-and-catalysts.md`, and the five metrics that tell whether the cases are on track. Done when every catalyst has a date or a window, a direction and a potency.

## Write

Follow `references/output-standard.md`. The report:

```
# <Company> (<ticker>): deep dive, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.

## What the evidence shows
Four to eight sentences in prose: what the business is, how good its economics are, what
protects them, whether the earnings are clean, what the price implies, the value range and
expected value, the main risk, and the next date. Implications for the reader named in scope.
No rating.

## The business
Segment table, geography table, trend over the periods returned.

## Economics
ROIC table with decomposition, three-year ROIIC, spread. Which ROIC is quoted.

## Industry structure and moat
The method's output lines, each with evidence. The duration judgment with its bounds.

## Earnings quality
Accrual series, EBITA rebuild, flags table with severity. Piotroski and Altman Z as reported.

## Capital allocation
Sources and uses, buyback return, deal table, leverage.

## What the price implies
Steady state vs future value creation, implied growth and CAP, warranted vs actual multiple,
base-rate sentence.

## Valuation
Forecast summary, continuing value and its checks, bridge per share, WACC x g table, the three
cases with probabilities and the expected value, comps cross-check, range.

## Risks and kill criteria
Premortem reasons; ranked risk table; floors; kill criteria with dates.

## Catalysts and what to watch
Catalyst table; the five metrics.

## What would change this reading
Two to five observable conditions, dated where possible, tied to the drivers and kill criteria.

## Gaps
The five-year limit on statements, assumptions that drive the range, data not in Bigdata.com.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Every table carries Basis and Source columns; where they would take a table past eight columns, put one "Basis and sources" note under it instead. Length: four to eight pages. Offer a Word document when the host can create files. A narrow question ("what is the ROIC trend?") gets the relevant section and the sources, not the full report.

## Checks before sending

1. The five annual periods were used, and Gaps says the series stops there.
2. The ROIC quoted is named (hand-built or FactSet) and the two are reconciled in one line; ROIIC is three-year rolling and labelled.
3. One cost of capital runs through the economics, the price-implied section and the valuation.
4. Every moat output line has evidence or a stated gap.
5. One-offs are counted by recurrence, the EBITA rebuild is shown, and stock compensation is neither added back nor deducted twice.
6. The buyback return is computed at the year-average prices paid, net of issuance.
7. "What the price implies" precedes the valuation and the opening section reads consistently with it.
8. Terminal value share, implied terminal multiple and the bridge per share are all shown.
9. Probabilities sum to 100 and are anchored to a reference class; the premortem has at least three reasons.
10. Kill criteria and catalysts have dates or observable thresholds.
11. No rating word. Every table has Basis and Source columns or the note under it, and every figure in prose has a citation or a basis word.
12. The special case was applied if the company is a bank, a cyclical, high growth or a conglomerate.

## Hand-offs

- The user wants only the thesis and its claims: `bigdata-thesis`. Only the valuation: `bigdata-valuation`. Only the moat: `bigdata-moat`. Only the peer multiples: `bigdata-comps`. Only the cases and their weights: `bigdata-scenarios`. Only the accounting: `bigdata-earnings-quality`. Only management's use of cash: `bigdata-capital-allocation`. Only what could go wrong: `bigdata-risk`. Only the balance sheet and debt: `bigdata-credit`.
- After delivering, make one offer: save the report to the user's Bigdata.com account, or turn the user's preferences for this report into a skill of their own. Act only on a clear yes.
