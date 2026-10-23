---
name: bigdata-watchlist
description: >-
  Check a list of companies at once from Bigdata.com data: price and move over the window, the
  news that explains it, earnings against estimates, target and rating changes, sentiment, and the
  next event for each name, as one table plus the items worth reading. Use when the user names
  several companies and asks what changed, what they should know today, or for a daily or weekly
  check on their holdings or watchlist. Not for a single company in depth, which
  bigdata-company-brief covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, expectations
  bigdata-sector-primer: auto
---

# Watchlist

This skill gives a portfolio manager the morning check on a list of names: one table with each company's move over the window, the news behind it, its last print against estimates, the Street's targets, its sentiment and its next date, followed by the few items worth reading in full. It flags what changed and says whether each change touches the long-term drivers or only the quarter. It gives no view on any name. "Anything on my list today?" with nothing material gets the table and one line saying so.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not check the list from memory or the web. Stop there: give no view, drivers, risks, figures or dates from memory while the tools are missing, and do not fall back to web search.
- Pass `plugin_slug: "bigdata-watchlist"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A quiet day needs the table and one line; a day with three prints needs the three read properly.

## Scope the request

Establish the list and the window.

- **Names given in the message.** Resolve each with `find_securities`, in parallel, one call per name. Keep any name that does not resolve in the Gaps line rather than guessing.
- **A saved list** ("my watchlist", "my holdings", a list name). Call `bigdata_get_watchlist` with no id to list the user's own watchlists, pick the one the user named, then call it again with that id to load the entity ids. Do not ask the user to retype the names. If several saved lists fit and the user named none, ask which one: this is the one question worth asking.
- **The window.** Today by default; "this week" is the trailing five trading days; "since Friday" or "since earnings" is taken as said. State it in the header.

If the user gives position sizes or weights with the names, use them only to order the table; the skill does not size, rebalance or judge positions. Done when the list is resolved, unresolved names are noted for the Gaps line, and the window is fixed.

Size the calls to the list. The portfolio tearsheet returns earnings, targets and sentiment for up to 100 names, and price columns alone for up to 3,000. For a longer list, take the price grid for all names and the full grid for a shortlist (the movers, the names with news, the names reporting in the window), and say so in the header.

## Gather

1. **The grid.** `bigdata_portfolio_tearsheet` with the list's entity ids and all metrics (or price, 1-day change, after-hours and market cap only, for lists above 100). Done when each row has its price and when it was set, the 1-day move, the last reported EPS against its estimate with the fiscal period, the consensus target with its low, median and high, the sentiment score with its direction, and the market cap.
2. **The window move, when the window is longer than a day.** The grid carries the 1-day move only. Take each name's move over the window from `company_overview` in `bigdata_company_tearsheet`, or from a price series through `bigdata_computer`, and the home index's move over the same window from `bigdata_market_tearsheet`. Done when each name has its move and its move against the index, labelled derived.
3. **The news.** `bigdata_watchlist_search` in fast mode, with the saved list's id or the inline entity ids, a timestamp filter for the window, and the default budget of five excerpts per name (fewer per name for a long list; cost scales with names times excerpts). Run one query for material company news (results, guidance, deals, management, regulation, litigation) and one for analyst reactions (target and rating changes, estimate cuts), with the research and news categories. Done when each name has its items for the window, or an explicit "no items found" (with a per-name budget an empty group does mean nothing matched).
4. **Next dates.** `bigdata_events_calendar` with `calendar_type` set to `corporate_calendar`, the entity ids, and a window running to the next 30 days. Done when each name has its next earnings date or conference, or "none in the next 30 days".
5. **Drill-down on flagged names only** (Analyse step 1). For each: `bigdata_company_tearsheet` with `analyst_estimates, analyst_ratings` for the 30-day consensus revision and the rating counts; `bigdata_fetch_document` on the release, filing or call that carries the news when the excerpt leaves out the number that matters; `bigdata_sentiment_tearsheet` when sentiment turned and the reason is not in the news. Done when each flagged item has its figure, its date and its source.
6. **Sector primer.** For a flagged name in a sector with a section in `references/sector-primers.md`, read its "metrics that matter" section, so a bank's item is read on net interest income and provisions rather than on EPS alone. Done when each flagged name in such a sector has the primer's metrics noted for the read.

## Analyse

1. **Flag what changed.** A name is flagged when any of these holds over the window: it reported results; it moved 10 percent or more against its index (the threshold the base-rate tables in `references/after-a-price-move.md` use); it has the largest move in the list in either direction; guidance, a target or a rating changed; it announced a deal, a financing, a management change or a regulatory or legal outcome; its sentiment direction turned; or it reports in the next five trading days. Any lower move threshold the user asks for is assumed and stated. Done when every name is flagged or quiet, with the reason for the flag.

2. **Read each flagged item against the long-term outlook.** From `references/after-a-price-move.md` rule 1, in short form: did consensus for FY+2 or long-term growth change, or guidance; are the drivers recurring (price, volume, margin structure) or one-time; does cash flow agree with the earnings line; is the information diagnostic, or does it only look causal (an EPS-dilution headline on a deal whose synergies exceed the premium). Which revision matters depends on the company: where it earns near its cost of capital the return on new investment moves value and growth does not, and where it earns well above it sales growth moves value (`references/expectations.md`, formula 4; use the FactSet ROIC against a stated, assumed cost of capital). Done when each flagged item is classed long-term, near-term or unclear, with the evidence.

3. **Earnings against estimates.** The grid's EPS surprise refers to the last reported period, which may predate the window. Report it as news only when the report fell in the window; otherwise show the period and move on. For a report in the window, the surprise in EPS is the start, not the story: add the revenue line, the guidance against consensus and the 30-day change in next-year consensus from the drill-down. Done when each print in the window has its EPS and revenue surprise, the guidance change, and the revision that followed.

4. **Targets and ratings.** Targets, ratings and sell-side comments are opinions held by others; report them as claims with their dates and sources, never as this skill's view. The useful reading is the change: how many targets moved, which way, and whether the spread between the low and high target widened. Done when each changed target or rating is dated and sourced.

5. **Large moves.** For a name that moved 10 percent or more against its index in one day, classify the event (earnings or not, momentum going in) as `references/after-a-price-move.md` step 1 and step 3 set out, and quote the parent branch with N and its sample period, labelled as a historical average and not a forecast. Leave the full note to `bigdata-stock-move`. Done when each such name has its classification and the parent row.

6. **The one-line read per name.** For each row: what changed, in one plain line, and whether it touches the long-term drivers ("Q3 EPS 4 percent above consensus, FY guide cut 2 percent, next-year consensus down 3 percent since; long-term"). Quiet names read "no material news; moved with the index" or the equivalent. No stance word. Done when every row has its line.

7. **The list as a whole.** The skew of moves and sentiment across the list; names that moved together on one sector or macro story (say it once, not per name); and how many names report in the next two weeks. Done when the opening paragraph can say what kind of day or week it was for the list.

Special cases on a list:

- ETFs and funds keep their row in the grid with blank cells. Take their move from `bigdata_etf_tearsheet` and leave the earnings and target columns empty with a note.
- A private company has no market data. Keep its row for news and dates and mark the price columns "private".
- A non-US listing is measured against its home index, in local currency; say so in the column note.
- Outside trading hours the price is the last close. For a US name before the open, include the pre-market trade from the grid and say which figure is the latest and when it was set.
- A company with two listings appears once, on the listing the user named or the primary one.
- A bank or insurer that reported is read on the primer's lines (net interest income, provisions, combined ratio), not on EPS alone.

## Write

Follow `references/output-standard.md`.

```
# <List name or "Watchlist"> check: <window>, <date>
Data as of: prices <date and time>; estimates <date>; newest document <date>.
Covered: <n> names; <shortlist rule, if the list was above 100>.

## What changed
Three to six sentences: the flagged names and why, the shared story if there is one, the
list's skew, the next dates that matter. No view on any name.

## The list
| Company (ticker) | Move, window | vs index | Last EPS vs est. (period) | Target mean (low-high) vs price | Sentiment | What changed | Next date | Basis | Source |
Flagged names first, ordered by how much the change touches long-term drivers; quiet names
after. For a long list, quiet names may share one line listing each ticker and its move.

## Worth reading
Two to five items. Each: the name, what happened with the figure and the date, long-term or
near-term and why, and the one document to open, cited.

## Coming up
| Date | Company | Event | What consensus or guidance expects | Source |
The next two weeks for the list.

## What would change this view
Two to four observable conditions on the flagged names, dated where possible.

## Gaps
Unresolved names, names with no coverage, short interest and options data (not in
Bigdata.com), and any window the grid could not cover.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one to two pages. A user who asks about one item on the list ("anything on Nvidia in my list?") gets that row, its item and the sources.

## Checks before sending

1. Every name the user gave or the saved list holds appears in the table or the Gaps line.
2. Moves over the window are measured against the index over the same window, and the window is stated.
3. An EPS surprise is shown as news only when the report fell in the window, and its fiscal period is shown.
4. Every flagged item has a figure, a date and a source, and is classed long-term, near-term or unclear.
5. Targets and ratings are reported as dated claims by others.
6. A 10 percent relative move carries its classification and the parent base-rate row with N and period.
7. No row and no sentence carries a buy, hold, sell, add, trim or rating word.
8. Shared moves are explained once, not repeated per name.
9. Each "no items found" comes from a per-name search budget, not a shared one, so it means no coverage rather than a lost share of the budget.
10. Prices state when they were set, and pre-market or after-hours figures are labelled as such.
11. Every name in "Coming up" has its date from the calendar, not from a news mention.

## Hand-offs

- One name in depth over a window: `bigdata-company-brief`. Why one name moved: `bigdata-stock-move`.
- A name reported and the user wants the quarter: `bigdata-earnings-review`. The dated events ahead across the list: `bigdata-catalysts`.
- After delivering, make one offer. If the user typed the names, offer to save them as a Bigdata.com watchlist (up to 100 names) so the next check starts from it. If the list was already saved, offer a monitor on it that flags material news. Act only on a clear yes.
