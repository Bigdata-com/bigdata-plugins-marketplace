---
name: bigdata-markets-today
description: >-
  Market wrap for a day, week or month: what moved across indexes, sectors, rates and currencies,
  the news behind it. Use for what happened in markets, why everything is red, a morning briefing.
  Not one company: bigdata-stock-move.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, forecasting-discipline
  bigdata-sector-primer: none
---

# Markets today

The wrap someone reads before the open or after the close: what moved across asset classes over the window and by how much, why, each reason tied to a source, and what is scheduled next and what it would test. Never a trade, an allocation or a rotation call. Size the work to the question: "why is oil up?" gets the row, the reason with its source and the next event that tests it, not the full wrap.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-markets-today"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a wrap that answers it with fewer tables and rows is the better wrap.
- **The window is fixed before anything is read.** "Today" is the latest session; "this week" or "last week" is a stated span of sessions taken from the daily series, as is any past date ("the week of the Fed meeting"). The header states the window, the region and the time the data was pulled, and says when a market was still trading. Before the US open, the US one-day figure is the previous session: lead with Asia-Pacific and Europe and say that US cash markets have not opened.
- **A move earns a sentence when it matters to the window:** it is the largest in its group, it reverses the direction of the trailing month, or it breaks from the rest of its group (one sector up while the index falls). In a full wrap the benchmarks the reader expects (the main index in each region, the US 2-year and 10-year, EUR/USD and USD/JPY, Brent or WTI, gold, bitcoin) appear regardless; a question about one asset gets that asset.
- **Facts kept apart from attributed opinions.** A release with its actual against consensus, a central bank decision, a company's published result or a filed deal is a fact; a strategist's or a reporter's reason for a move is written as theirs, with the source named in the sentence ("Reuters attributed the fall to..."). When no source links a move to a cause, the note says no cause was found, because a cause is easy to invent for any move (`references/forecasting-discipline.md`, facts, opinions and expectations).
- **The story has to fit across assets.** A rates story should show in yields, the dollar and the growth against value spread; a growth scare in cyclical sectors, commodities and the curve; a risk-off day in the VIX and in high yield against investment grade. When the assets disagree with the stated reason, say so.
- **Fundamentals, discount rate or flows.** The main equity move is put down, in a sentence, to news about earnings, a change in the rate the market discounts them at, or flows (rebalancing, options expiry, quarter-end), or a stated mix. Flows are named only when a source reports them; a small move with no news is a normal outcome, not a puzzle (`references/after-a-price-move.md`, decomposing the move).
- **Macro surprises computed** from the calendar's actual against its consensus, never taken from a headline's "beat" or "miss".
- **Breadth, when the question is whether a move was broad or narrow,** read from what the data carries: the number of the eleven US sectors up against down and the spread between the best and worst sector; an equal-weight ETF against the cap-weighted index when its daily series is available. The Russell 2000 against the S&P 500 is a size read, not breadth, and the wrap calls it that. Factor rows are already relative to the S&P 500.
- **Single stocks only as index drivers.** A company that moved 10 percent or more against the index gets one line with its trigger and source; the history of what follows large single-stock moves belongs to a stock-move note, not here.
- **A scheduled event earns a place when it tests one of the window's stories,** with its date, the period it covers, consensus and the previous figure in the sentence, and which story it would confirm or contradict.
- **Positioning questions, when the user asks what the window means for positioning.** One paragraph names the questions a book would ask after this window (rates, earnings or flows; broad or narrow; which factor carried it; which event tests it next) and what the data says on each, in observations and dated conditionals. It never says buy, sell, add, trim, rotate, hedge, overweight or underweight.
- **Rows that mislead.** Crypto trades every day, so its multi-day figures cover a different span from equities; a market closed for a holiday was closed, not flat; a large commodity move near expiry can be the contract roll, so check a source before calling it news; the VIX is quoted as a level and a change in points, the points computed from the level and the percent.

## Where it goes wrong

- **The snapshot's five-day column read as last week.** It runs from the snapshot's own refresh time and can cover fewer sessions; a week, or any window that is not the trailing one, comes from the daily series.
- **Yield changes read as basis points.** The snapshot's yield change columns are percent of the yield; basis points come from the yield levels or from dated reports.
- **A spread in the text that its table does not give.** Every spread is computed from the table's own rows.
- **Citations assembled at the end.** The link goes next to each figure as it is captured, and figures from the data sets go on the Data line.
- **A snapshot level set against a press intraday figure.** Quote one, with its time.

## What the data has, and does not

The market snapshot covers the major indexes and the VIX, US sector ETFs, equity factor ETFs (returns relative to the S&P 500), US Treasury yields only, currency pairs, crypto, commodity futures and bond ETFs in one pull; it is a snapshot as of now, its multi-day columns run from its own refresh time, and its yield changes are percent of the yield. Index moves come from the index rows; country ETF rows are US-dollar proxies whose return includes the currency, used only for markets the index list lacks, and the note says it is a dollar figure. Non-US yields (Bunds, gilts, JGBs) come from dated reports or go in the Gaps line. The economic calendar carries actual, consensus and previous for each release; the corporate calendar carries earnings dates, conferences, IPOs and delistings. Intraday prices, fund flows, positioning, option prices and advance-decline counts have no structured field; news and research often carry them, so search before stating a gap. The snapshot asks that its data sources be named, which the Data line does.

## Write

`references/output-standard.md` holds the rules. The title carries the day's finding in one line ("Yields, not earnings, took the S&P 500 down 1.2 percent"). The header states the window, how it differs from what the user asked if it does, the region and the pull time. The opening gives the main moves with their numbers, the reason for each and who gave it, whether the move was broad or narrow, and the next event that tests it, in plain sentences. The body follows the question, with the benchmarks first in each asset class and the unit on every figure. What is scheduled next and what each event tests close the wrap, with the positioning questions where they apply. Sub-headings state the finding ("Rates did the work; earnings barely moved"), never the asset class alone.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every move is over the stated window, from the snapshot for the trailing one or the daily series for any other, with yield changes in basis points.
- Every number in the opening agrees with the body, and every spread in the text is computed from the figures the wrap shows.
- Every reason has a source named in the sentence, and a move with no cause found says so.
- Every code name or internal term (a facility name, a policy acronym) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
