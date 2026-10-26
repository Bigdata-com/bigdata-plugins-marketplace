---
name: bigdata-watchlist
description: >-
  Daily or weekly check on a list of companies: price move, the news behind it, earnings vs
  estimates, next event, in one table. Use for holdings, watchlist, peer or competitor set, what
  changed today. Not one company: bigdata-company-brief.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, expectations
  bigdata-sector-primer: auto
---

# Watchlist

This skill gives a portfolio manager the morning check on a list of names: one table with each company's move over the window, the news behind it, its last print against estimates, the Street's targets, its sentiment and its next date, followed by the few items worth reading in full. It flags what changed and says whether each change touches the long-term drivers or only the quarter. It gives no view on any name. "Anything on my list today?" with nothing material gets the table and one line saying so.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-watchlist"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. A quiet day needs the table and one line; a day with three prints needs the three read properly.

## Scope the request

Establish the list and the window.

- **Names given in the message.** Resolve each to its Bigdata.com entity, in parallel, one lookup per name. Keep any name that does not resolve in the Gaps line rather than guessing.
- **A saved list** ("my watchlist", "my holdings", a list name). Load it from the user's saved Bigdata.com watchlists: list them, pick the one the user named, and take its companies from it. Do not ask the user to retype the names. If several saved lists fit and the user named none, ask which one: this is the one question worth asking.
- **The window.** Today by default; "this week" is the trailing five trading days; "since Friday" or "since earnings" is taken as said. State it in the header.

A peer group or a competitor set is as valid a list as a portfolio: a strategy or IR team checking its rivals gets the same table, with the read written for that reader. If the user gives position sizes or weights with the names, use them only to order the table; the skill does not size, rebalance or judge positions. Done when the list is resolved, unresolved names are noted for the Gaps line, and the window is fixed.

Size the calls to the list. The grid of current figures for a list carries earnings, targets and sentiment for up to 100 names, and price columns alone for up to 3,000. For a longer list, take the price grid for all names and the full grid for a shortlist (the movers, the names with news, the names reporting in the window), and say so in the header.

## Gather

1. **The grid.** Current figures for the whole list in one pull. The table below uses the EPS, surprise, target and sentiment columns, so get them for up to 100 names; above 100, get price, 1-day change, after-hours and market cap for all names and the full set for the shortlist. Done when each row has its price and when it was set, the 1-day move, the last reported EPS against its estimate with the fiscal period, the consensus target with its low, median and high, the sentiment score with its direction, and the market cap.
2. **The window move and each name's typical range.** The grid carries the 1-day move only. For a window longer than a day, each name's move and its home index's move over the exact window come from daily prices, computed, not estimated (the company quote and the market overview carry standard windows only; use them when the window is one, such as five days). From the same series, derive each name's typical daily move: the standard deviation of its daily return against the index over the last 60 trading days, labelled derived. For a list above 100, compute it for the shortlist. Done when each name has its move, its move against the index and its typical daily move.
3. **The news.** A news search across the whole list over the window that gives every name its own share of results, five excerpts per name by default (fewer per name for a long list; cost scales with names times excerpts). Run one search for material company news (results, guidance, deals, management, regulation, litigation) and one for analyst reactions (target and rating changes, estimate cuts), over research and news. Done when each name has its items for the window, or an explicit "no items found" (with a per-name budget an empty group does mean nothing matched).
4. **Next dates.** The corporate calendar for the list, over the next 30 days. Done when each name has its next earnings date or conference, or "none in the next 30 days".
5. **Drill-down on flagged names only** (Analyse step 1). For each: current consensus with its vintage, the targets and the rating counts. Consensus is a snapshot with no history of consensus or targets, so a revision over the window comes from a search of research and news for the period that quotes the earlier figure, with the document's date, labelled press or research summary, or it is marked not found. The full release, filing or call that carries the news when the excerpt leaves out the number that matters; the sentiment report when sentiment turned and the reason is not in the news (it has no window; say which period its narrative covers). Get ratios and valuation metrics only if the user asks for a flagged name's fundamentals. Done when each flagged item has its figure, its date and its source, and each revision is dated or marked not found.
6. **Sector primer.** For a flagged name, find its sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its metrics that matter, so a bank's item is read on net interest income and provisions rather than on EPS alone. Done when each flagged name in such a sector has the primer's metrics noted for the read.

## Analyse

1. **Flag what changed.** A name is flagged when any of these holds over the window: it reported results; its one-day move against the index exceeds twice its typical daily move (Gather step 2), or 10 percent if that is smaller, so a quiet utility's 3 percent day is caught and a volatile biotech's 6 percent day is not flagged for noise; it has the largest move in the list in either direction; guidance, a target or a rating changed; it announced a deal, a financing, a management change or a regulatory or legal outcome; its sentiment direction turned; or it reports in the next five trading days. Any lower move threshold the user asks for is assumed and stated. Done when every name is flagged or quiet, with the reason for the flag.

2. **Read each flagged item against the long-term outlook.** Ask `references/after-a-price-move.md` rule 1's questions (a), (b), (c) and (e) in short form. A daily check does not run the incremental-return test of question (d); leave it to `bigdata-company-brief` or `bigdata-earnings-review`. Done when each flagged item is classed long-term, near-term or unclear, with the evidence.

3. **Earnings against estimates.** The grid's EPS surprise refers to the last reported period, which may predate the window. Report it as news only when the report fell in the window; otherwise show the period and move on. For a report in the window, the surprise in EPS is the start, not the story: add the revenue line, the guidance against consensus and the change in next-year consensus from the drill-down's search, or "revision not found". Done when each print in the window has its EPS and revenue surprise, the guidance change, and the revision that followed or a not-found mark.

4. **Targets and ratings.** Targets, ratings and sell-side comments are opinions held by others; report them as claims with their dates and sources, never as this skill's view. The useful reading is the change: how many targets moved, which way, and whether the spread between the low and high target widened. Done when each changed target or rating is dated and sourced.

5. **Large moves.** For a name that moved 10 percent or more against its index in one day (the boundary of the base-rate tables), classify the event (earnings or not, momentum going in) as `references/after-a-price-move.md` step 1 and step 3 set out, and quote the parent branch with N and its sample period, labelled as a historical average and not a forecast. Leave the full note to `bigdata-stock-move`. Done when each such name has its classification and the parent row.

6. **The one-line read per name.** For each row: what changed, in one plain line, and whether it touches the long-term drivers ("Q3 EPS 4 percent above consensus, FY guide cut 2 percent, next-year consensus down 3 percent since; long-term"). Quiet names read "no material news; moved with the index" or the equivalent. No stance word. Done when every row has its line.

7. **The list as a whole.** The skew of moves and sentiment across the list; names that moved together on one sector or macro story (say it once, not per name); and how many names report in the next two weeks. Done when the opening paragraph can say what kind of day or week it was for the list.

Special cases on a list:

- ETFs and funds keep their row in the grid with blank cells. Take their move from the ETF's own profile and quote and leave the earnings and target columns empty with a note.
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
| Company (ticker) | Move, window | vs index | Last EPS vs est. (period) | Target mean (low-high) vs price | Sentiment | What changed | Next date |
One "Basis and sources" note under the table: moves derived from the price series, EPS, targets
and sentiment reported from the grid (Data line). Flagged names first, ordered by how much the change touches long-term drivers; quiet names
after. For a long list, quiet names may share one line listing each ticker and its move.

## Worth reading
Two to five items. Each: the name, what happened with the figure and the date, long-term or
near-term and why, and the one document to open, cited.

## Coming up
| Date | Company | Event | What consensus or guidance expects | Source |
The next two weeks for the list.

## What to watch
Two to four observable conditions on the flagged names, dated where possible.

## Gaps
Unresolved names, names with no coverage, short interest and options data (not in
Bigdata.com), and any window the grid could not cover.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Citations: the list-wide news search asks that its documents are cited inline and never listed as a numbered catalogue, so cite its items inline in the "What changed" cell and in "Worth reading" in its own format: a markdown link whose text is the source name and date ("Reuters - Oct 24, 2026") and whose target is the URL the search returned. Keep the numbered Sources section for the other documents (single-company searches, fetched filings, calendar) and the Data line for the grid.

Length: one to two pages. A user who asks about one item on the list ("anything on Nvidia in my list?") gets that row, its item and the sources.

## Checks before sending

1. Every name the user gave or the saved list holds appears in the table or the Gaps line.
2. Moves over the window are measured against the index over the same window, and the window is stated.
3. An EPS surprise is shown as news only when the report fell in the window, and its fiscal period is shown.
4. Every flagged item has a figure, a date and a source, and is classed long-term, near-term or unclear.
5. Targets and ratings are reported as dated claims by others.
6. Flags on price use each name's typical daily move, stated; a 10 percent relative move carries its classification and the parent base-rate row with N and period.
7. No row and no sentence carries a buy, hold, sell, add, trim or rating word.
8. Shared moves are explained once, not repeated per name.
9. Each "no items found" comes from a per-name search budget, not a shared one, so it means no coverage rather than a lost share of the budget.
10. Prices state when they were set, and pre-market or after-hours figures are labelled as such.
11. Every name in "Coming up" has its date from the calendar, not from a news mention.
12. Items from the list-wide news search are cited inline in its own format and do not appear in the numbered Sources list.

## Hand-offs

- One name in depth over a window: `bigdata-company-brief`. Why one name moved: `bigdata-stock-move`.
- A name reported and the user wants the quarter: `bigdata-earnings-review`. The dated events ahead across the list: `bigdata-catalysts`.
- After delivering, make one offer. If the user typed the names, offer to save them as a Bigdata.com watchlist (up to 100 names) so the next check starts from it. If the list was already saved, offer a monitor on it that flags material news. Act only on a clear yes.
