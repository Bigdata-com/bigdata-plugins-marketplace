---
name: bigdata-screen
description: >-
  Find companies that fit criteria: size, sector, valuation, growth, quality or yield, ranked on
  what the user asked for. Use for screen for stocks, find ideas, companies like X, acquisition
  targets. Not one name: bigdata-quick-take.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, multiples-and-peers, roic, base-rates, expectations
  bigdata-sector-primer: auto
---

# Screen

This skill turns a profile the user describes into a shortlist worth an analyst's time: the criteria written down as thresholds, the screen run in two stages (the screener for what it can filter, the tearsheets for valuation and fundamentals), the survivors ranked on the user's own criteria or, when the user names none, on metrics that persist and relate to value rather than on last year's growth, the numbers behind every name, what the price implies for the top names, and the specific reason each one deserves a closer look or a caution. A screen generates candidates; judgment about why each one screens well comes after. The output is never a buy list. "List US semiconductor companies above $10bn" gets the screener table with its as-of date and the Data line, without a ranking.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-screen"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Write the criteria as a table before the first call: the user's words, the threshold, whether the screener, the tearsheet or a search applies it, and whether it is the user's or assumed. Mark the user's primary criterion, the one the shortlist is ranked on first.

- **Coverage, said up front.** The screener covers listed companies only. Without a country or exchange it covers primary listings on NASDAQ, NYSE, NYSE American and the Toronto Stock Exchange; other markets need a country code or an exchange from the tool's own list. Private companies are not in it: add named private companies through `find_securities` and searches for the rest, and say how they were found.
- **What the screener filters:** market cap, share price, beta, daily volume, dividend per share, sector, industry, country, exchange, actively trading, ETF or fund. Its sector labels are its own list, not those of `find_securities`. Values are in each listing's currency and are not converted, so keep one country per screen when sizes must compare.
- **What the tearsheet applies afterwards:** valuation multiples, growth, margins, ROIC, gross profitability, leverage, cash conversion. Estimate revisions are not a tearsheet field (it holds a current consensus snapshot); they come from a search per name and cannot filter a long list, so apply them to the shortlist only, labelled press or research summary.
- **Vague words become stated thresholds,** labelled assumed with the reason: "small cap", "cheap", "quality", "growing", "low debt". Define "quality" with persistent measures (gross profitability, ROIC, operating margin stability) and say so.
- **"Companies like X"** is a peer search: resolve X, read the competitors block in its `company_overview` first, then add candidates by industry classification and by value drivers (growth, margin, ROIC, turnover, capital intensity) as `references/multiples-and-peers.md` step 7 sets out, and report the overlap between the lists.
- **Corporate screens.** Acquisition targets, competitors, suppliers or customers for the user's own company are valid screens. Write the criteria in the user's terms (size the user could buy, overlap with its products, geography), and write each name's reason and caution for that reader: fit and obstacles for a target, threat for a competitor, dependence for a supplier.

Ask one question only when the criteria leave the universe in the thousands and nothing in the request narrows it (no size, sector or geography). Otherwise state the assumed thresholds in the header and proceed.

## Gather

1. **First stage.** `bigdata_screen_companies` with the mapped filters, actively trading, ETFs and funds excluded unless asked for. Page through with the cursor until the list is complete. Done when the candidate count, the as-of time and the exchanges covered are recorded. If more than about 100 survive, tighten with a stated liquidity or size floor and say so.
2. **Current figures.** `bigdata_portfolio_tearsheet` over the candidates for price and market cap. Request the surprise, target and sentiment columns only when the user asked for them, because they cap the grid at 100 names; with price and market cap alone it takes up to 3,000. Done when every candidate has a current market cap.
3. **Second stage.** Take the top N candidates on the user's primary criterion (state N; 20 to 30 is a workable default, all of them when fewer survive). For each, `bigdata_company_tearsheet` in two calls: `financial_statements, financial_ratios` with `interval` annual, then `key_metrics, analyst_estimates`. Done when five fiscal years of statements, the FactSet ROIC, margins, total assets, net debt, enterprise value, the forward multiples and consensus with its vintage are in hand for each, or the missing item is named.
4. **Why each top name screens well.** For the top five to ten after ranking, `bigdata_search`, one company per call: recent news, the last call's main issue, and any one-off item, disposal, restatement or controversy that flatters or depresses the screened metrics. Done when each top name has a dated reason for its numbers, or a note that none was found.
5. **Dates.** `bigdata_events_calendar` for the top names' next reports. Done when each has a date or is marked not found.
6. **Sector primers.** For each sector among the top names, find it in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read "Metrics that matter" and "Financial statements and accounting traps". Where the primer's metrics replace the default ranking (below), search each shortlisted name's latest supplement or presentation for them. Done when each sector's metrics and traps are noted and each shortlisted name in those sectors has its metrics or a not-found note.

## Analyse

1. **Apply the criteria.** Compute each second-stage metric the same way for every company, and record which names fail which criterion. Names that fail one criterion narrowly are worth listing separately, because screens that disagree are informative. Done when the pass and fail table exists with the computed values.

2. **Rank.** Rank on the user's criteria, in the order the user gave them, and show each criterion's value. Only when the user names no ranking criterion, use the default: gross profitability (gross profit over total assets), ROIC and operating margin level and stability, because `references/base-rates.md` table 6 shows these persist from year to year while sales growth persists weakly and net income growth not at all. Measure each against the sector median computed from the second-stage set, so a staples company and a software company are not compared on raw margins. Tables 7 and 8 give historical sector means (top 1,000 global companies, 1950 to 2015, ex-financials and utilities; historical, not current); their sector names differ from the screener's, so map them: consumer staples to Consumer Defensive, consumer discretionary to Consumer Cyclical, health care to Healthcare, information technology to Technology, materials to Basic Materials, telecom services to Communication Services (which also holds media), industrials and energy as named. Financial Services, Real Estate and Utilities have no base-rate row. Use the FactSet ROIC field for every company, name it once, and never mix it with a hand-built figure (`references/roic.md`). One-year growth may be shown but does not drive the default rank. Where the default does not fit, the primer's metrics replace it: REITs on FFO and AFFO (per share, and price over AFFO), utilities on allowed return and rate base growth, oil and gas producers on reserve life, reserve replacement and breakeven price, banks on ROTCE against an assumed cost of equity and price to tangible book, insurers on combined ratio and operating ROE against price to book. Show the rank on each metric as well as any composite, and label the composite's weights judgment. Done when the ranking table shows each metric, its sector median and the rank, and says whether the user's criteria or the default drove it.

3. **Valuation beside returns.** From `references/multiples-and-peers.md`: the multiple the sector's convention calls for (forward EV/EBITA or P/E, price to book for banks, price to AFFO for REITs), built the same way for every name, always shown next to ROIC and growth. A low multiple on a low return is not cheap. For cyclicals, say whether the multiple sits on peak or trough earnings. Done when each shortlisted name has its multiple, its ROIC and growth beside it, and the sector median.

4. **What the price implies for the top names.** From `references/expectations.md`, for the top three to five: forward P/E against the steady-state P/E (formula 1) and the NOPAT growth the enterprise value implies (formula 2), with the cost of capital set as its inputs table says and ROIIC as a three-year rolling figure, the most five annual periods allow. Place consensus growth in its size class from `references/base-rates.md` table 2, three-year column, with the share of companies that achieved it and the sample label. Done when each top name has its implied bar and base-rate sentence.

5. **Reasons to look further, and reasons for caution.** For each top name: why it screens well, with evidence from step 4 of Gather; the way it could be a trap (a one-off gain, peak-cycle margins, leverage, an accounting choice the primer flags, a business in decline at a low multiple); and the next thing an analyst would check. Then check the list as a whole: is it mostly one size, one sector or one cheap-valuation tilt, so that the screen is a factor bet rather than a set of company-specific ideas? It covers currently listed companies only. Done when every top name has both a reason and a caution, and the list-level check is written.

6. **A peer search.** When the user asked for companies like a named one, start from its competitors block, then build the two candidate lists from scope: the screener on its industry, and companies close on the value drivers from the second stage, wherever they are classified. Rank by distance from the named company on those drivers rather than by quality, state the selection rule before showing any multiple, and report how many classification peers survive. Done when each peer has a stated reason and the overlap count is given.

Special cases:

- **Banks and insurers.** No EV multiples and no ROIC: the primer's metrics above. Screen them separately from industrial companies.
- **Cyclicals.** A high margin or ROIC at the peak of the cycle is not persistent. Show the five-year range next to the latest value and flag any name whose latest margin sits at the top of it.
- **Loss-making or early-stage companies.** Gross profitability and ROIC are not meaningful when NOPAT or invested capital is negative; rank them, if at all, on gross margin and revenue against forward EV/Sales, and say so.
- **Several countries.** Convert market caps to one currency with the rate and date stated (derived) before applying a size threshold, because the screener does not convert.

## Write

Follow `references/output-standard.md`.

```
# Screen: <the profile in a few words>, <date>
Data as of: screen <as-of time>; prices <date>; estimates <date>; statements <latest period>.

## Summary
Four to six sentences: the criteria, the coverage, how many companies passed each stage, what
the top names have in common, the main caution about the list, and what would change the ranking.

## Criteria
| User's words | Threshold | Applied by | User's or assumed | Reason |

## Funnel
Universe and exchanges covered, after the screener, after the fundamental criteria, shortlisted
(N and the criterion it was cut on). One line each.

## Shortlist
| Rank | Company (ticker) | Market cap | <criterion 1> vs sector | <criterion 2> vs sector | <criterion 3> | Multiple vs sector | Consensus growth |
Basis and sources: one line under the table.

## What the price implies for the top names
| Company | Forward P/E | Steady-state P/E | Implied growth | Consensus growth | Base-rate share | Basis | Source |

## The top names
One short paragraph each: why it screens well, the caution, the next check, the next report date.

## Near misses
Names that failed one criterion narrowly, with the criterion.

## What would change this reading
Two to four conditions: a criterion that would change the shortlist, a data revision, a dated event.

## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: two to four pages. A narrow listing request gets the screener table, its as-of time and the Data line, with the footer. State under the shortlist that it is a list of candidates for further work, not a buy list.

## Checks before sending

1. Every criterion is written as a threshold, with assumed ones labelled and explained.
2. The funnel shows counts at each stage, the N cut and its criterion, and the screen's as-of time and coverage (exchanges, countries, currency, private names added).
3. The ranking follows the user's criteria; the default persistent-metric ranking appears only when the user named none, and sector metrics replace it where the primer says so.
4. One ROIC definition for every company, named once; banks, insurers, REITs and utilities are on their sector metrics.
5. Every multiple sits next to ROIC and growth, and none is called cheap on its own.
6. The top names have the price-implied bar and a base-rate sentence with sample and period; base-rate sector names are mapped to the screener's.
7. Every top name has a reason and a caution; the list-level factor check is written.
8. No buy list, target, rating or weighting language.
9. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- A view on one name from the list: `bigdata-quick-take`; the full work: `bigdata-deep-dive`. Peers and multiples for one company: `bigdata-comps`.
- A target from the list the user wants to price as a deal: `bigdata-deal-analysis`.
- The user's profile is really a sector or a theme: `bigdata-sector` or `bigdata-theme`.
- After delivering, make one offer: save the shortlist as a Bigdata.com watchlist. Act only on a clear yes.
