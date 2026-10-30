---
name: bigdata-watchlist
description: >-
  Daily or weekly check on a list of companies: price move, the news behind it, earnings vs
  estimates, next event, in one table. Use for holdings, watchlist, peer or competitor set, what
  changed today. Not one company: bigdata-company-brief.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move
  bigdata-sector-primer: auto
---

# Watchlist

The morning check on a list of names, for someone who holds or follows them: what moved and against what, the news behind it, the last print where it fell in the window, the Street's targets and sentiment as dated claims, and each name's next date, then the few items worth reading in full. The note says what changed and whether each change touches the long-term drivers or only the quarter. It gives no view on any name. A peer or competitor set is as valid a list as a portfolio. Size the work to the day: a quiet day gets the grid and one line; a day with three prints needs the three read properly.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures, dates or view from memory or the web in the meantime.
- Pass `plugin_slug: "bigdata-watchlist"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **The window is fixed first, and every move is measured over it against the home index.** Today by default; "this week" is the trailing five trading days; "since Friday" or "since earnings" is taken as said. A non-US listing is measured against its home index in local currency.
- **What counts as a change is set per name.** A name is flagged when, over the window, it published results; its one-day move against the index exceeds twice its typical daily move (the standard deviation of its daily return against the index over the last 60 trading days) or 10 percent, whichever is smaller; it has the largest move in the list either way; guidance, a target or a rating changed; it announced a deal, a financing, a management change or a regulatory or legal outcome; its sentiment direction turned; or it reports in the next five trading days. The per-name threshold catches a quiet utility's 3 percent day and leaves a volatile biotech's 6 percent day as noise. A lower threshold the user asks for is used and stated.
- **Each flagged item is read against the long-term outlook.** Whether consensus beyond next year or guidance changed and by how much, whether the drivers recur, whether cash flow agrees with the earnings line, and whether the news changes the thesis or only looks causal (`references/after-a-price-move.md`, long-term outlook test). The judgment is stated as a plain sentence with its evidence ("next year's consensus is unchanged and the charge does not recur, so the case stands"), never as a label or a bolded category, because what the reader needs is whether to reopen the case.
- **A print in the window is more than its EPS surprise.** When a name reported in the window, read the revenue line, the guidance against consensus, and the change in next-year consensus since the print from dated research or news, or a line saying none was found. A bank or insurer is read on net interest income and provisions, or the combined ratio, not on EPS alone.
- **Targets and ratings are claims by others; the change is what matters.** When targets moved in the window, say how many moved, which way, and whether the low-to-high spread widened, each with its date and source; unchanged targets need no line.
- **A large move is measured, not explained.** For a one-day move of 10 percent or more against the index, one sentence says whether it came on earnings, over one day or several, and how much the peers shared (`references/after-a-price-move.md`, classifying the event). What follows such a move belongs to `bigdata-stock-move`.
- **A shared story is told once**, in the opening, not repeated per row.
- **Depth only for flagged names.** The full release, filing or call when the excerpt leaves out the number that matters; current consensus, targets and rating counts; the sentiment report when sentiment turned and the news does not say why. Valuation metrics only when the user asks.
- **Position sizes order the rows and do nothing else.** The note does not size, rebalance or judge positions.
- **Hand-offs.** One name in depth: `bigdata-company-brief`. Why one name moved: `bigdata-stock-move`. The quarter for a name that published results: `bigdata-earnings-recap`. Dated events ahead across the list: `bigdata-catalysts`.

## Where it goes wrong

- **An old EPS surprise written as news.** The grid's surprise belongs to the last period with results; it is news only when that report fell in the window.
- **A name and its index measured over different dates.** Both use the same stated window.
- **One fixed move threshold for the whole list.** It flags volatile names on noise and misses a real move in a quiet one.
- **A shared news budget across the list.** The largest names take the results and an empty row means nothing; each name gets its own share.
- **A date taken from a news mention.** Dates ahead come from the calendar.
- **A name that does not resolve is guessed.** It goes in the Gaps line as the user gave it.
- **A revision declared missing too early.** Earlier consensus and targets are often quoted in research and news; search the window before stating a gap.

## What the data has, and does not

A saved Bigdata.com watchlist is loaded by name, never re-asked; when several fit and the user named none, which one is the only question worth asking. Typed names are resolved one lookup per name, in parallel.

The grid of current figures carries price and when it was set, the one-day move, pre-market and after-hours trade, market cap, the last EPS against its estimate with the fiscal period, the consensus target with low, median and high, and sentiment with its direction, for up to 100 names; price columns alone go to 3,000. Above 100, the price grid covers every name and the full grid a shortlist (movers, names with news, names reporting in the window), and the note says so. The quote carries fixed windows only; any other window, and each name's typical daily move, come from daily prices for the name and its index.

Consensus and targets are snapshots with no history, so a revision is reconstructed from dated documents. The news search across a list can give each name its own share, five excerpts per name by default and fewer for a long list; material company news and analyst reactions run as separate searches. The corporate calendar looks forward and carries earnings, conferences, IPOs and delistings. The sentiment report has no window; say which period its narrative covers.

An ETF keeps its row with its move from its own quote and blank earnings and target cells. A private company has news and dates only; its price cells read "private". Outside trading hours the price is the last close, with the pre-market trade for a US name before the open. A company with two listings appears once. Sector reporting lines are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the day's finding in one line with the list's name, the window and the date ("Banks led the list down on provisions this week"); the line under it says when prices and estimates were set. The opening says what kind of day or week it was: the flagged names and why, the shared story if there is one, the skew of moves and sentiment, and the next dates that matter. The body follows the question. A full check carries one grid of the names, flagged first and ordered by how much the change touches long-term drivers, because the reader scans it for what to reopen; it holds only what the reader compares across names that day, and quiet names on a long list may share one line. Then a short list of two to five items worth reading, each with its figure and date, a sentence on whether it touches the long-term case and why, and the one document to open, cited. Then the next two weeks of dated events from the calendar, with what consensus or guidance expects. The note closes on two to four observable conditions on the flagged names, dated where possible, and a Gaps line. Sub-headings state the finding, never the step. One to two pages; a question about one name gets that row, its item and the sources.

## Before sending

- Every name the user gave or the saved list holds appears in the grid or the Gaps line, and every move is against the index over the same stated window.
- An EPS surprise appears as news only when the report fell in the window, and every flagged item has a figure, a date, a source and a sentence on whether it touches the long-term case.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with the grid, and every date ahead comes from the calendar.
- Targets and ratings appear as dated claims by others; no row or sentence carries a stance word on any name.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.

**After the note**

If the user typed the names, offer once to save them as a Bigdata.com watchlist (up to 100 names); if the list was already saved, offer a monitor that flags material news on it. Act only on a clear yes.
