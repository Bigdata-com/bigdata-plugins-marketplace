---
name: bigdata-deep-dive
description: >-
  An initiation-style report on one company from Bigdata.com data: the business and its economics,
  industry structure and moat, earnings quality, capital allocation, what the price implies, a
  valuation range, risks, catalysts and what to watch, with every figure sourced. Use when the
  user asks for a deep dive, an initiation, an investment memo, full research on a company, or to
  understand a business properly. Not for a one-page view, which bigdata-quick-take covers, or for
  the thesis alone, which bigdata-thesis covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, roic, valuation, multiples-and-peers, earnings-quality, capital-allocation, industry-structure, downside-and-catalysts, forecasting-discipline
  bigdata-sector-primer: auto
---

# Deep dive

This skill writes the report an analyst hands a portfolio manager when they pick up coverage of a name: how the business makes money and how well, who it competes with and what protects it, whether the reported earnings are the real earnings, what management does with the cash, what the price assumes, what the company is worth under three cases, what breaks it, and what to watch. It runs four to eight pages and takes a few dozen tool calls. It gives no rating.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not write the report from memory or the web. Stop there: give no view, drivers, risks, figures or dates from memory while the tools are missing, and do not fall back to web search.
- Pass `plugin_slug: "bigdata-deep-dive"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A company with one segment and no acquisitions needs no sum-of-the-parts and no deal history; a bank needs the primer's statements, not an enterprise DCF.

## Scope the request

Resolve the company with `find_securities`. Establish the user's angle if they gave one (a long idea, a short idea, a peer to compare against, a question they want answered) and the depth: a full report by default, or the sections they named. Ask one question only if the name is ambiguous or the user asked for something the report does not cover. Done when the company is resolved and the angle and depth are fixed.

If the company is Private, offer `bigdata` for a document-based profile instead; the tearsheet, estimates and price-implied sections do not exist.

## Gather

The report rests on the tearsheet, the last three calls, the latest annual filing, the deal history and the peers. Each step says what it must produce.

1. **Tearsheet, all sections, in calls of two or three sections each** so no response is too large: `company_overview, c_level_leadership, analyst_ratings`; `company_overview, latest_earnings, earnings_calendar`; `financial_statements, financial_ratios, key_metrics` (with `interval` annual for five fiscal years; there is no period offset, so a longer series is noted in Gaps); `analyst_estimates`; `revenue_segmentation`; `fund_trends_history`; `mergers_acquisitions`; `hiring_trends`. Done when the statements (ten years if the tool provides them, otherwise the five returned, noted for the Gaps line), five years of segments, consensus to the horizon, holders, deals and the calendar are in hand.
2. **The last three earnings calls**, by `bigdata_search` with the reporting period filter and `bigdata_fetch_document`. Done when guidance history, the recurring questions and management's own framing of the drivers are known.
3. **The latest annual filing**, by search and fetch, read for the business description, the segment economics, the risk factors that changed from the prior year, related-party items, the pension and lease notes, and the share-count and compensation notes. Done when each of those is noted with the page or section.
4. **Industry evidence.** Three to six searches, one aspect each: market shares and their stability, pricing in the industry, new entrants and exits, regulation, the suppliers and customers with power, the technology that could change the structure. Done when each item of the `references/industry-structure.md` method has evidence or an explicit gap.
5. **Peers.** `bigdata_screen_companies` on the industry and size, then `bigdata_company_tearsheet` with `key_metrics, analyst_estimates, financial_statements, financial_ratios` for four to eight peers chosen by value drivers. Done when the peer table in `references/multiples-and-peers.md` can be filled.
6. **Sell-side and news.** Searches for research notes and news over the last twelve months on the company's strategy, its capital allocation and its controversies. Done when the controversies are listed.
7. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read it before analysing. Done when the sector's metrics and accounting traps are noted.

## Analyse

Each step names its reference file. Each ends in what it must produce.

1. **The business.** How the company makes money by segment and geography, from the segment table and the filing: revenue, growth, margin and capital employed by segment where disclosed. Done when a reader can see where the profit comes from and how that has shifted over five years.

2. **The economics.** From `references/roic.md`: NOPAT at the operating tax rate, invested capital built from both sides, ROIC with and without goodwill, with leases and capitalised R&D where they matter, ROIC as margin times turnover, ROIIC over the last three and five years, and the spread over a stated cost of capital. Compare with the FactSet ROIC field and say which one the report quotes. Done when the ROIC series (ten years if the statements allow, else five) is tabled with the decomposition and the spread.

3. **Industry structure and moat.** From `references/industry-structure.md`: the industry map, the profit pool and its direction, share stability, pricing power, concentration, entry and exit, the five forces with evidence, the source of advantage, the disruption test, and a judgment on how long the advantage lasts, bounded by the sector's persistence figures in `references/base-rates.md`. Done when each item in the method's output checklist is stated with evidence or a gap.

4. **Earnings quality.** From `references/earnings-quality.md`: the accrual ratio over five years, the EBITA rebuild with one-offs counted by how many years they recur, the provisions and reserve movements, revenue recognition and capitalisation checks, stock compensation as a cost, the earnings-to-equity reconciliation, and the red flags with severity. Piotroski and Altman Z are quoted from the tearsheet as reported. Done when the flags table is complete and the rebuilt EBITA sits next to reported operating profit.

5. **Capital allocation.** From `references/capital-allocation.md`: five years of sources and uses, the buyback return against the cost of equity at the prices paid, net of issuance, the dividend record, each major deal against its premium and the synergies claimed, reinvestment returns, leverage against rating medians, and what the proxy pays management for. Done when the sources-and-uses table and the deal table are complete and the incentive line is written.

6. **What the price implies.** From `references/expectations.md`: steady state against future value creation, the implied growth and the implied competitive advantage period at the stated cost of capital, the warranted multiple for the company's growth and return against the actual multiple, and the base-rate sentences for consensus growth from `references/base-rates.md`. Done when the report says what the market assumes in growth, margin, return and years.

7. **Valuation range.** From `references/valuation.md`: an explicit forecast over a horizon set by the competitive advantage judgment in step 3, with ROIC and turnover checked each year and the implied growth consistent with reinvestment; a continuing value with RONIC fading to WACC; the terminal-value share and the implied terminal multiple; the equity bridge per share with every item; the WACC-by-growth sensitivity; and the three cases run through the drivers with probabilities from `references/forecasting-discipline.md`. Cross-check with the comps table from `references/multiples-and-peers.md`. Apply the special case for a bank, a cyclical, a high-growth company or a conglomerate. Done when the range, the expected value and the sensitivity table are complete and the terminal checks are stated.

8. **Risks and the downside.** From `references/downside-and-catalysts.md`: the risks ranked by probability and size, what breaks each driver, the floors, the balance sheet under stress, and the kill criteria with dates. Done when each risk has an early signal and the kill criteria are observable.

9. **Catalysts and what to watch.** From `references/downside-and-catalysts.md` table 2: the dated events over the next twelve months, each with mechanism, direction, size and certainty, and the five metrics that tell whether the cases are on track. Done when every catalyst has a date or a window.

## Write

Follow `references/output-standard.md`. The report:

```
# <Company> (<ticker>): deep dive, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.

## What the evidence shows
Six to ten sentences in prose: what the business is, how good its economics are, what protects
them, whether the earnings are clean, what management does with the cash, what the price
implies, the value range and expected value, the main risk, and the next date. No rating.

## The business
Segment table, geography table, five-year trend. Every table carries Basis and Source columns.

## Economics
ROIC table with decomposition, ROIIC, spread. Which ROIC is quoted.

## Industry structure and moat
The checklist items, each with evidence. The duration judgment with its bounds.

## Earnings quality
Accrual series, EBITA rebuild, flags table with severity. Piotroski and Altman Z as reported.

## Capital allocation
Sources and uses, buyback return, deal table, leverage, incentives.

## What the price implies
Steady state vs future value creation, implied growth and CAP, warranted vs actual multiple,
base-rate sentences.

## Valuation
Forecast summary, continuing value and its checks, bridge per share, WACC x g table, the three
cases with probabilities and the expected value, comps cross-check, range.

## Risks and kill criteria
Ranked table; floors; kill criteria with dates.

## Catalysts and what to watch
Catalyst table; the five metrics.

## What would change this view
Two to five observable conditions, dated where possible, tied to the drivers and kill criteria.

## Gaps
Statement years not available, assumptions that drive the range, and data not in Bigdata.com.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: four to eight pages. Offer a Word document when the host can create files. A narrow question ("what is the ROIC trend?") gets the relevant section and the sources, not the full report.

## Checks before sending

1. Ten years of statements were used, or the Gaps line says why fewer.
2. The ROIC quoted is named (hand-built or FactSet) and the two are reconciled in one line.
3. Every moat checklist item has evidence or a stated gap.
4. One-offs are counted by recurrence, and the EBITA rebuild is shown.
5. The buyback return is computed at the prices paid, net of issuance.
6. "What the price implies" precedes the valuation and the opening section reads consistently with it.
7. Terminal value share, implied terminal multiple and the bridge per share are all shown.
8. Probabilities sum to 100 and are anchored to a reference class.
9. Kill criteria have dates or observable thresholds.
10. No rating word. Every table, including the catalysts and risks tables, has Basis and Source columns, and every figure in prose has a citation or a basis word.
11. The special case was applied if the company is a bank, a cyclical, high growth or a conglomerate.

## Hand-offs

- The user wants only the thesis and its claims: `bigdata-thesis`. Only the valuation: `bigdata-valuation`. Only the moat: `bigdata-moat`.
- After delivering, make one offer: save the report to the user's Bigdata.com account, or turn the user's preferences for this report into a skill of their own. Act only on a clear yes.
