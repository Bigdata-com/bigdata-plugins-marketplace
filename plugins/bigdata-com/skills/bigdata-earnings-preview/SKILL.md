---
name: bigdata-earnings-preview
description: >-
  Setup before a company reports: drivers of the quarter, consensus vs guidance, what the price
  implies, scenarios, what to check first. Use for an earnings preview, what to expect when X
  reports. Not results: bigdata-earnings-recap.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, valuation, operating-leverage-and-tam, forecasting-discipline
  bigdata-sector-primer: auto
---

# Earnings preview

A note on what to expect when a company reports, for someone who will act on it: what the quarter turns on, what the market expects and already pays for, what management promised, and what to check first when the release lands. Never a call on the stock. Size the work to the question: "what is consensus for Micron's quarter" gets the consensus line with its date and the guidance quoted from the last call, nothing more.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-earnings-preview"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **Guidance comes from the previous quarter's call.** The guidance for the quarter being previewed was given when the quarter before it was reported, so that transcript is the one to read, with its period fixed. Quote the range verbatim with its date, and note what analysts pressed on, because those are the questions that return.
- **Consensus is a snapshot, so revisions are reconstructed.** How the number moved since the last print comes from dated research and news that quote an earlier figure. A consensus walked down into the print changes what a beat means; when no earlier figure is found, say so.
- **The company's own guidance record.** Actual against the guided midpoint for every past quarter found, how often and by how much the company beats its own midpoint, and whether the beat is shrinking. A beat the size of the usual beat is the expected case, not news.
- **Read the latest filing, not only the call.** The 10-Q or annual report carries liquidity, financing plans, commitments, off-balance-sheet items and legal matters that the call and the press summarise loosely. Where the filing and the press line disagree, the filing wins and the note says so.
- **Drivers ranked.** Three to five, in order of weight (volume, price and mix, the largest cost lines, the segment that moves the total, currency), each with what consensus assumes for it, the evidence since the last call, and which way the risk runs, written into the sentence rather than as a repeated label. Any claim of acceleration or deceleration states the rate it is measured against.
- **What the price implies.** The run since the last print against the index, then the growth path the enterprise value implies for the business or the segment the question is about, and whether that bar is high or low and why (`references/expectations.md`, implied growth). The inputs behind the enterprise value appear once, from the latest filing: share count, cash, debt, leases, stakes carried outside the operating business and the net debt they give, the tax rate on the profit figure a multiple is applied to, and the discounting convention, so the reader can rebuild the figure on the page; every later number uses them. The cost of capital is one stated figure, with the yield, beta and premium behind it in a single clause and no regression statistics; the 10-year yield comes from the country data (`references/valuation.md`, cost of capital). One central case and one range cover the sensitivity. When the bar rests on a multi-year growth rate, the sentence that says so carries how often companies of that size achieved it, with the population and period in the same sentence (`references/base-rates.md`, real sales growth by starting size). The steady-state multiple and the share of the price paid for growth stay in the working unless the user asks what the multiple means.
- **What a point of the key driver is worth.** One or two sentences: what a point of growth in the segment that moves the stock adds to revenue and operating income this quarter, at the company's own incremental margin. The full sales-to-earnings sensitivity (3 and 5 percent miss and beat, inside and outside view) only when the user asks about a sales miss or beat (`references/operating-leverage-and-tam.md`, sales sensitivity around consensus).
- **Scenarios on the size of the beat and the guide.** Beat and raise, in line, miss or soft guide. Probabilities start from the company's own beat rate over the quarters found, never a default split. When brokers or the buy side sit above published consensus on the metric that matters, their figure is the bar the cases are cut on, and the note says so. When the question names spending or funding, the capex figure or its wording is a case variable with its own cut-off, not a side note. The cases partition the outcomes: every value of each metric used (growth rate, operating income, guide midpoint, capex) falls in exactly one case, and a metric has one cut-off in the whole note. The likely reaction for each case is sized on the earnings-day moves after past prints, listed so the reader can see them, and on the options-implied move when a document carries it; the probability-weighted expected move is stated and reconciles with the cases (`references/forecasting-discipline.md`, scenario weights and expected value).
- **What to check first, with thresholds.** Five to seven items in the order to read them when the release lands, each a metric, the consensus or guided figure, and the threshold that changes the reading, using the same cut-offs as the scenarios. When the company usually gives a figure on a different call (next year's capex on the fourth-quarter call), say so and set the trigger on the wording instead. Then at most five call questions, each tied to a driver or to a claim management made last time and none repeating a checklist item; the sector primer's questions are the starting list, rewritten for this company.
- **Peers reporting first.** Companies in the same business that report in the days before the print, and what in their release resets the bar (a cloud peer's growth and capex the night before). One or two lines in the setup and a line in what to check.
- **Items that move the stock without a number.** An accounting or policy change (asset lives, capitalisation, a segment redefinition), a buyback or dividend change, a management change, restructuring, a disclosure that starts or stops. One line each where they bear on the quarter, in the checklist when a tell exists.
- **Each case carries its tell in management's words.** Beside the numbers that define a case, the phrase or guidance wording that would signal it on the call, so the reader can place the quarter from the first minutes of the call.
- **Cyclicals and banks.** For a cyclical, the mid-cycle margin beside the consensus margin, so a peak-margin print is not read as a run rate. For a bank, net interest income against rate assumptions and provisions against the credit cycle, in place of the sales sensitivity.

## Where it goes wrong

- **Guidance read from the wrong call.** A search that lands on the call for the quarter being previewed, or a later one, has the period wrong.
- **A beat written as the bullish case.** Most companies beat; the reaction turns on the size of the beat against the usual beat and on the guide against next-period consensus.
- **A risk-free rate assumed** when the country data has the yield.
- **Citations assembled at the end.** The link goes next to the fact when the fact is captured.
- **The note mirrors the method.** The reader needs the bar, what is priced in, the scenarios and what to check first. A figure that does not change the reading stays in the working, and the working itself (files, formulas, labels) never reaches the page.
- **A gap declared too early.** Options-implied moves, credit spreads, whisper numbers and financing details are often in news, research and filings; search before stating a gap.
- **An event the user named retold at length.** When the question names last week's event, two lines of what happened, then the company's own exposure with figures from its filing.
- **A balance sheet from a press summary.** Debt, cash and stakes come from the latest filing; a broker's or news figure for them is used only when the filing is not found, and the note says so.

## What the data has, and does not

Consensus for the quarter and the next fiscal years is a snapshot with its date, with actuals and surprises for some past quarters and guidance fields where the company gives them; no revision history. The latest-earnings record covers one quarter; older prints come from the estimates actuals or the results releases. Five fiscal years of annual statements and five quarters, the limit in each case. The earnings-day moves around past prints and the run since the last print need daily prices for the stock and its index. The 13F and options-activity data is quarterly positioning, not prices. The risk-free rate is in the country data. The next report date is in the corporate calendar. A private company has no estimates or market data; offer a document-based summary instead. Sector reporting lines, traps and call questions are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the setup in one line ("AWS at 40 percent is the bar; the quarter itself is not the debate"), not the event. The opening gives the bar for the quarter and what the price implies, in plain sentences the reader can act on. The body follows the question. What to check first and the call questions close a full preview. Sub-headings state the finding ("Amazon beats its own midpoint by 2 percent"), never the step that produced it.

## Before sending

- The guidance quoted is verbatim from the call for the quarter before the one previewed, with its date and link.
- Scenario probabilities sum to 100, rest on a stated beat rate, and a probability-weighted expected move is given.
- Every number in the opening agrees with the figure it came from, and the net debt or enterprise value used anywhere matches the inputs stated once.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Each metric has one cut-off across scenarios and checklist, and the cases leave no value unassigned.
- Every code name or internal term (a project name, a contract metric) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a label such as derived, assumed or judgment; no sentence describes how the note was made.
