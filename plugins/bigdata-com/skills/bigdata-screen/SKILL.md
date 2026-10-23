---
name: bigdata-screen
description: >-
  Find candidate companies with the Bigdata.com screener and tearsheets: a screen on size, sector,
  geography, valuation and fundamentals from the user's criteria, then a ranked shortlist with the
  numbers behind each name and the reasons to look further. Use when the user asks to find stocks,
  screen for companies, for ideas that fit a profile, or who else does what a named company does.
  Not for a view on one name, which bigdata-quick-take covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, multiples-and-peers, roic, base-rates, expectations
  bigdata-sector-primer: auto
---

# Screen

This skill turns a profile the user describes into a shortlist worth an analyst's time: the criteria written down as thresholds, the screen run in two stages (the screener for what it can filter, the tearsheets for valuation and fundamentals), the survivors ranked on metrics that persist and relate to value rather than on last year's growth, the numbers behind every name, what the price implies for the top names, and the specific reason each one deserves a closer look or a caution. A screen generates candidates; judgment about why each one screens well comes after. The output is never a buy list. "List US semiconductor companies above $10bn" gets the screener table with its as-of date and the Data line, without a ranking.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-screen"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Write the criteria as a table before the first call: the user's words, the threshold, whether the screener or the tearsheet applies it, and whether it is the user's or assumed.

- **What the screener filters:** market cap, share price, beta, daily volume, dividend per share, sector, industry, country, exchange, actively trading, ETF or fund. Its sector labels are its own list, not those of `find_securities`. Without a country or exchange it covers NASDAQ, NYSE, NYSE American and Toronto listings only; other markets need a country or exchange. Values are in each listing's currency and are not converted, so keep one country per screen when sizes must compare.
- **What the tearsheet applies afterwards:** valuation multiples, growth, margins, ROIC, gross profitability, leverage, cash conversion, estimate revisions.
- **Vague words become stated thresholds,** labelled assumed with the reason: "small cap", "cheap", "quality", "growing", "low debt". Define "quality" with persistent measures (gross profitability, ROIC, operating margin stability) and say so.
- **"Who else does what X does"** is a peer search: candidates by industry classification and by value drivers (growth, margin, ROIC, turnover, capital intensity), as `references/multiples-and-peers.md` step 7 sets out, with the overlap between the two lists reported.

Ask one question only when the criteria leave the universe in the thousands and nothing in the request narrows it (no size, sector or geography). Otherwise state the assumed thresholds in the header and proceed.

## Gather

Each step says what it must produce.

1. **First stage.** `bigdata_screen_companies` with the mapped filters, actively trading, ETFs and funds excluded unless asked for. Page through with the cursor until the list is complete. Done when the candidate count and the as-of time are recorded. If more than about 100 survive, tighten with a stated liquidity or size floor before the second stage and say so.
2. **Current figures.** `bigdata_portfolio_tearsheet` over the candidates for price, market cap, one-day move, last EPS surprise, price targets and sentiment (100 names at most with those columns; up to 3,000 with price and market cap alone). Done when every candidate has a current market cap.
3. **Second stage.** `bigdata_company_tearsheet` with `company_overview, fundamentals, estimates` for each candidate that passed the first stage, or for the 20 to 40 nearest the criteria when more survive. Done when five periods of statements, the FactSet ROIC, margins, total assets, net debt, enterprise value, the forward multiples and consensus with its vintage are in hand for each.
4. **Why each top name screens well.** For the top five to ten after ranking, `bigdata_search`, one company per call: recent news, the last call's main issue, and any one-off item, disposal, restatement or controversy that flatters or depresses the screened metrics. Done when each top name has a dated reason for its numbers, or a note that none was found.
5. **Dates.** `bigdata_events_calendar` for the top names' next reports. Done when each has a date.
6. **Sector primers.** For each sector among the top names, read its section of `references/sector-primers.md` for the metrics that apply and the traps (banks and insurers are not screened on ROIC or EV multiples).

## Analyse

1. **Apply the criteria.** Compute each second-stage metric the same way for every company, and record which names fail which criterion. Names that fail one criterion narrowly are worth listing separately, because screens that disagree are informative. Done when the pass and fail table exists with the computed values.

2. **Rank on persistent, value-relevant metrics.** From `references/base-rates.md` (table 6): gross profitability and operating margin persist strongly from year to year; sales growth persists weakly and net income growth not at all. Rank on gross profitability (gross profit over total assets), ROIC and operating margin level and stability, each measured against its sector median from tables 7 and 8 rather than in absolute terms, so a staples company and a software company are not compared on raw margins. From `references/roic.md`, use the FactSet ROIC field for every company, name it once, and never mix it with a hand-built figure. One-year growth may be shown but does not drive the rank. Banks and insurers rank on ROE against an assumed cost of equity and price to book. Show the rank on each metric as well as any composite, and label the composite's weights judgment. Done when the ranking table shows each metric, its sector median and the rank.

3. **Valuation beside returns.** From `references/multiples-and-peers.md`: the multiple the sector's convention calls for (forward EV/EBITA or P/E, P/B for banks), built the same way for every name, always shown next to ROIC and growth. A low multiple on a low return is not cheap. For cyclicals, say whether the multiple sits on peak or trough earnings. Done when each shortlisted name has its multiple, its ROIC and growth beside it, and the sector median.

4. **What the price implies for the top names.** From `references/expectations.md`, for the top three to five: forward P/E against the steady-state P/E at an assumed cost of equity, and the NOPAT growth the enterprise value implies at an assumed cost of capital against consensus. Place consensus growth in its size class from `references/base-rates.md` with the share of companies that achieved it and the sample label. Done when each top name has its implied bar and base-rate sentence.

5. **Reasons to look further, and reasons for caution.** For each top name: why it screens well, with evidence from step 4 of Gather; the way it could be a trap (a one-off gain, peak-cycle margins, leverage, an accounting choice the primer flags, a business in decline at a low multiple); and the next thing an analyst would check. Then check the list as a whole: is it mostly one size, one sector or one cheap-valuation tilt, so that the screen is a factor bet rather than a set of company-specific ideas? It covers currently listed companies only. Done when every top name has both a reason and a caution, and the list-level check is written.

6. **A peer search.** When the user asked who else does what a named company does, resolve the named company first and pull its tearsheet with the same sections. Build two candidate lists: the screener on its industry, and companies close on the value drivers (growth, operating margin, ROIC, capital turnover, capital intensity) from the second stage, wherever they are classified. Rank by distance from the named company on those drivers rather than by quality, state the selection rule before showing any multiple, and report how many classification peers survive. Done when each peer has a stated reason and the overlap count is given.

Special cases:

- **Banks and insurers.** No EV multiples and no ROIC: ROE against an assumed cost of equity, price to book, and the primer's capital and credit lines. Screen them separately from industrial companies.
- **Cyclicals.** A high margin or ROIC at the peak of the cycle is not persistent. Show the five-period range next to the latest value and flag any name whose latest margin sits at the top of it.
- **Loss-making or early-stage companies.** Gross profitability and ROIC are not meaningful when NOPAT or invested capital is negative; rank them, if at all, on gross margin and revenue against forward EV/Sales, and say so.
- **Several countries.** Convert market caps to one currency with the rate and date stated (derived) before applying a size threshold, because the screener does not convert.

## Write

Follow `references/output-standard.md`.

```
# Screen: <the profile in a few words>, <date>
Data as of: screen <as-of time>; prices <date>; estimates <date>; statements <latest period>.

## Summary
Four to six sentences: the criteria, how many companies passed each stage, what the top names
have in common, the main caution about the list, and what would change the ranking.

## Criteria
| User's words | Threshold | Applied by | User's or assumed | Reason |

## Funnel
Universe, after the screener, after the fundamental criteria, shortlisted. One line each.

## Shortlist
| Rank | Company (ticker) | Market cap | Gross profitability vs sector | ROIC vs sector | Operating margin and 5y range | Multiple vs sector | Consensus growth | Basis | Source |

## What the price implies for the top names
| Company | Forward P/E | Steady-state P/E | Implied growth | Consensus growth | Base-rate share | Basis | Source |

## The top names
One short paragraph each: why it screens well, the caution, the next check, the next report date.

## Near misses
Names that failed one criterion narrowly, with the criterion.

## What would change this list
Two to four conditions: a criterion that would change the shortlist, a data revision, a dated event.

## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. A narrow listing request gets the screener table, its as-of time and the Data line, with the footer. State under the shortlist that it is a list of candidates for further work, not a buy list.

## Checks before sending

1. Every criterion is written as a threshold, with assumed ones labelled and explained.
2. The funnel shows counts at each stage and the screen's as-of time and coverage (exchanges, countries, currency).
3. The ranking uses persistent metrics against sector medians; one-year growth does not drive it.
4. One ROIC definition for every company, named once; banks and insurers are handled on ROE and book value.
5. Every multiple sits next to ROIC and growth, and none is called cheap on its own.
6. The top names have the price-implied bar and a base-rate sentence with sample and period.
7. Every top name has a reason and a caution; the list-level factor check is written.
8. No buy list, target, rating or weighting language.
9. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- A view on one name from the list: `bigdata-quick-take`; the full work: `bigdata-deep-dive`. Peers and multiples for one company: `bigdata-comps`.
- The user's profile is really a sector or a theme: `bigdata-sector` or `bigdata-theme`.
- After delivering, make one offer: save the shortlist as a Bigdata.com watchlist. Act only on a clear yes.
