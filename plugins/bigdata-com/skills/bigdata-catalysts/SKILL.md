---
name: bigdata-catalysts
description: >-
  Dated events that could move a stock or a list, with expected impact and what is priced in. Use
  for what is coming up, events to watch, next catalysts. Not the earnings setup:
  bigdata-earnings-preview.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, downside-and-catalysts, forecasting-discipline, special-situations-arithmetic
  bigdata-sector-primer: auto
---

# Catalysts

The dated events that could change a company's value or the market's view of it over a horizon, ranked by expected impact and listed by date, each with what has to happen, how it reaches value, its size and odds, and what the market already expects, plus what happens if none arrives. A catalyst resolves something by a date; a standing risk with no resolution date belongs in `bigdata-risk`. Never a trade call. "When does X report?" gets the date, time, period and consensus with its source; a company with one report and nothing else ahead gets a short note that says so.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures, dates or view from memory or the web in the meantime.
- Pass `plugin_slug: "bigdata-catalysts"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **The horizon is a pair of dates.** The user's ("next quarter", "into year-end"), or through the second earnings report ahead by default, about six months. Every lookup uses those dates.
- **The events that decide most are usually off the calendar.** Search filings, transcripts and news one aspect at a time: regulatory decisions and deadlines; litigation milestones; launches, clinical readouts and approvals; contract renewals and large customers; debt maturities, refinancing and covenant tests; buybacks, spin-offs, asset sales, strategic reviews and activist stakes (`references/downside-and-catalysts.md`, catalysts); index changes, lock-up expiries and share-class events; and management's dated promises, quoted verbatim.
- **Each catalyst is a question that can be scored.** A checkable outcome, a date or window, and why it matters ("the regulator rules on the merger by 15 March; approval without remedies closes the deal at the stated price"); a theme cannot be scored (`references/forecasting-discipline.md`, questions that can be scored).
- **Each catalyst says how it reaches value and who decides.** Either it changes a cash-flow driver (growth, margin, investment, the years of excess return) or it closes the gap between price and value (a sale, a breakup, a spin-off, a buyback, the end of forced selling); the decider is the board, outside holders, a regulator or a court (`references/downside-and-catalysts.md`, catalysts). The date carries how sure it is: filed or announced, an estimated window and what it rests on, or open-ended.
- **Size in the driver's own terms.** Revenue, margin in basis points or value per share where the figures allow; for a scheduled report, the stock's typical earnings-day move against its index over the past prints found, with their number.
- **Odds start from a reference class or the company's own record, for the catalysts that decide most.** An integer probability resting on how often events of that kind resolved that way, with the population and period in the sentence, or on how often this company's approvals or launches arrived on time. Never 50 by default, and a longer window carries higher odds than a shorter one for the same event. With no reference class, the sentence says what the figure rests on and the range is wider (`references/forecasting-discipline.md`, granular probabilities). For a binary readout (a trial result, an approval, a verdict), search the published success rates for that kind of event and phase first.
- **What the market expects is part of each catalyst.** For a report, consensus with its date, the recent revision and the company's guidance. For other events, the sell-side's stated expectation as opinion. Where a traded price embeds the outcome, as an announced deal's spread does, the completion probability the price implies net of carry, with the break price (`references/special-situations-arithmetic.md`, merger arbitrage spread); the full spread arithmetic belongs to `bigdata-special-situations`.
- **How hard it would hit, judged on four tests.** Certainty (announced and filed against hoped for), timing (dated against open-ended), how much of the gap or the driver it would move, and whether the decider gains from the outcome. The judgment is a plain sentence with its reason, never a high, medium or low label (`references/downside-and-catalysts.md`, catalysts).
- **Ranked by expected impact, then listed by date.** Size, odds and those four tests together set the rank, not the calendar: a large two-sided ruling in five months can outrank a routine report next week.
- **What happens if nothing happens.** Without a catalyst, value can erode or the gap can widen; the note gives the direction and the main cause.
- **A first signal for each top catalyst.** The earliest observable sign of which way it is resolving, with its date (a docket entry, a peer's print). When the user holds a thesis, each signal becomes a kill criterion with a driver, a threshold and a date (`references/forecasting-discipline.md`, kill criteria with dates).
- **Spin-offs and index deletions.** The catalyst can be the end of forced selling; date when it should be done (`references/downside-and-catalysts.md`, why it is cheap and who is selling).
- **Rate- and commodity-driven names.** For a bank, a homebuilder or a miner, the rate decisions, data releases or stress tests that move it are ranked with the other catalysts, with their dates and consensus.
- **A list gets each name's top catalysts in short form**, the names ranked by what the horizon decides for them.
- **Hand-offs.** The full setup for the next report: `bigdata-earnings-preview`. A spin-off, merger spread or restructuring: `bigdata-special-situations`. Probability-weighted values for the outcomes: `bigdata-valuation`. What usually follows a large move: `bigdata-stock-move`.

## Where it goes wrong

- **A standing risk listed as a catalyst.** Anything with no resolution date leaves the list and is pointed to `bigdata-risk`.
- **Only the calendar searched.** It misses investor days, votes, court dates and regulatory deadlines.
- **An even split for odds.** A probability rests on a stated reference class or the company's record, never on 50 by default.
- **"High" written for size.** Size is a figure in the driver's terms or a sentence that none could be inferred.
- **A binary outcome averaged.** Both outcomes' effect on value is shown.
- **An estimated date written as fixed.** An estimate says what it rests on.
- **A gap declared too early.** Deal terms, approval timelines, maturity schedules and options-implied moves are often in filings, research and news; search before stating a gap.

## What the data has, and does not

The corporate calendar looks forward only and carries earnings, conferences, IPOs and delistings. Investor days, votes, court dates and regulatory deadlines come from filings, transcripts and news; the document that sets a date or term (a merger agreement's outside date, a maturity schedule) is the source a reader can check. Past report dates come from a search for results releases, and earnings-day moves from daily prices for the stock and its index. Consensus is a snapshot with its date and no history, so the recent revision comes from research and news over the last 30 days that quote an earlier figure; when none is found the note says so. The economic calendar carries macro releases by country and category with their consensus. For a list, current figures for up to 100 names come in one pull. A saved Bigdata.com watchlist is loaded by name, never re-asked. A private company has no market data or consensus. Sector event types, macro items and call questions are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the setup in one line with the company, the ticker and the horizon's dates ("The merger ruling in March decides more than two reports"). The opening gives the two or three catalysts that decide most, what each would change, what the market expects of each, the next date, and what happens if nothing happens. The body follows the question, the user's parts in the user's order. Without named parts, a full note gives what the market expects now, then the catalysts ranked by expected impact, each in a short paragraph carrying what the choices above give it, the top three with their first signal; a table of the catalysts only when there are more than four and the reader needs to compare them, and the same events in date order when the dates are what the reader will act on. A list gets one table in date order with each name's top catalyst, then a few sentences on the names whose horizon decides most. The note closes on two to four observable conditions that would change the reading, dated where possible. Sub-headings state the finding ("Approval is the only event that moves the gap"), never the step. One to two pages; a one-line question gets the date, the source and the footer.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- Every catalyst that decides most has a date or window with how sure it is, a mechanism, a decider, and a size in the driver's terms or a sentence that none could be inferred; none carries a high, medium or low label.
- Probabilities are integers resting on a stated reference class or the company's record, none is 50 by default, and the numbers in the opening agree with the body.
- Every code name or internal term (a drug code, a project name, a contract term) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.

**After the note**

Offer once a monitor that flags news on the top catalysts until their dates, or, for a typed list of names, saving it as a Bigdata.com watchlist. Act only on a clear yes.
