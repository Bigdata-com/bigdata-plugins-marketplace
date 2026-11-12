---
name: bigdata-valuation
description: >-
  What a company is worth: the growth, margin and return the price implies, a DCF with the equity
  bridge checked, three cases with probabilities and signposts, a multiples cross-check, a range.
  Use for fair value, DCF, is it cheap, what is priced in, scenarios, what if a driver changes.
  Not peers only: bigdata-comps.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, valuation, roic, forecasting-discipline, multiples-and-peers
  bigdata-sector-primer: auto
---

# Valuation

A note on what a company is worth as a range of cases with an expected value, and what the price already assumes. Never a point value or a price target. Size the work to the question: "what growth does the price imply for Micron" gets the implied growth and, where the answer rests on it, one sentence on how often companies of that size achieved it, not the full model; "what happens to Micron if DRAM prices fall 10 percent" gets that driver moved by the user's shock size, the second-order effects on margins and reinvestment, and the value per share, not three full cases.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-valuation"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **What the price implies, first.** Solve for the growth and the years of excess return the enterprise value needs at a three-year rolling return on new investment, and say whether that bar is high or low and why (`references/expectations.md`, implied growth, implied competitive advantage period). When the answer rests on a multi-year growth rate, the sentence carries how often companies of that size achieved it, after converting nominal to real, with the population and period in the same sentence (`references/base-rates.md`, real sales growth by starting size, real and nominal growth). The steady-state value and the share of the price paid for growth stay in the working unless the user asks what the multiple means.
- **The inputs once, so the reader can rebuild the value.** From the latest filing: the share count from the cover page, cash, debt, leases, stakes outside the operating business, the pension deficit after tax, minorities and the net debt they give, the operating tax rate, and the discounting convention (mid-year or year-end). They appear once and every later figure uses them, because a value the reader cannot rebuild on the page cannot be checked (`references/valuation.md`, equity bridge).
- **One cost of capital through everything.** One stated figure, with the 10-year yield in the cash-flow currency from the country data, the beta and the premium behind it in a single clause and no regression statistics. A regression beta is adjusted toward 1 and set beside the peer and sector figures before use; a cost of equity outside roughly 8 to 12 percent for a US large cap is explained before it is used. When the value differs from the price, say how much of the gap is the discount rate: the value at a point higher and lower, and the rate at which the base case equals the price, in a sentence (`references/valuation.md`, cost of capital).
- **ROIC built from the statements.** NOPAT at the operating tax rate from the tax note, invested capital from both sides, and a three-year rolling return on new investment (`references/roic.md`, NOPAT, invested capital, ROIIC and the spread). Goodwill is shown in and out when acquisitions are a material part of invested capital. The data set's ROIC field is compared in one line, never mixed with the built figure.
- **A forecast that fades.** Growth blended toward the size-class median beyond three years and margins faded toward the sector mean, because unusual levels revert; a year-by-year check that ROIC, turnover and implied capex hold together (`references/valuation.md`, horizon, revenue and margins, reinvestment and consistency checks; `references/base-rates.md`, regression to the mean). Where the value rests on a multi-year margin, the sentence carries how margins in the sector have reverted, with population and period.
- **Continuing value from growth, return on new capital and WACC**, each stated, with the return on new capital above WACC only where the evidence supports a durable advantage. When the continuing value carries most of the value, say what share it is and the EV/EBITDA it implies against today's multiple, because that is where an optimistic value hides (`references/valuation.md`, continuing value).
- **When the question is what it is worth, cases on two or three swing drivers**, everything else held the same. The cases partition the outcomes: each driver has one cut-off across the note and every value falls in exactly one case. What must be true in each case, with second-order effects carried (margins move with sales through the contribution margin, reinvestment with growth). Probabilities start from the share of companies of this size or sector that reached each case's driver value, or from the company's own record, never a default split; when brokers or the buy side sit above published consensus on the driver that matters, their figure is the bar the cases are cut on, and the note says so. The value for each case shows the figures it rests on, equity is never below zero, the expected value averages values, never inputs, and reconciles with the cases, and the loss case sits beside the gain case. One central case and one range (cost of capital and terminal growth) cover the sensitivity (`references/forecasting-discipline.md`, scenario weights from a reference class, expected value; `references/valuation.md`, sensitivity and cases).
- **Signposts, where there are cases.** A signpost is an observable with a threshold and a date or window that would move the odds between cases, written as a sentence, because the reader needs to know what to watch and when (earnings dates and conferences from the events calendar; regulatory, product and contract dates from filings and news, which the calendar does not carry). The reasons the base case could fail are worked through; one reaches the page only where it changes the reading, tied to its signpost (`references/forecasting-discipline.md`, premortem, kill criteria with dates).
- **Peers by value drivers, when the range needs a cross-check**, the selection rule stated before any multiple; the comparison reaches the page where it confirms or contradicts the range (`references/multiples-and-peers.md`, peer selection by value drivers, what a multiple implies).
- **The market is right** unless there is a specific, evidenced reason it is not, and the note says what the reason is.
- **Banks and insurers, deep cyclicals, growth above 15 percent a year, emerging markets, several businesses, distress** each change the method (`references/valuation.md`, special cases).

## Where it goes wrong

- **A raw regression beta** that gives a cost of capital at which no plausible forecast reaches the price. Adjust it and compare with peers and the sector first.
- **The interest shield twice.** NOPAT uses the operating tax rate; the shield lives once, in WACC.
- **Excess cash in the perpetuity.** Added once, in the bridge; operating cash stays at 2 percent of sales (5 for less predictable businesses).
- **Gross PP&E for net investment.** Capex is the change in net PP&E plus depreciation; net investment is the change in net PP&E. A negative implied capex, or a jump in ROIC with no driver, means an input is wrong.
- **The horizon set from the market-implied period**, which tests the price against itself. Quote it beside the chosen horizon as a comparison only.
- **A terminal multiple above today's with no reason.** Uncertainty goes into the cases, never into a higher discount rate or multiple.
- **Stock awards** treated as anything but a cost in the forecast.
- **A single year of return on new investment** read as evidence. Five annual periods allow a three-year figure and nothing longer.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, five periods being the limit; consensus to four years out as a snapshot with its date, with no revision history; the annual report in full with the fiscal year fixed, for the tax note, the bridge items, debt maturities and the cover-page share count; the risk-free rate and inflation for the cash-flow currency from the country data, never from memory while the tool is there; a beta from 60 monthly returns through the computing tool when prices are available, otherwise from a dated document with its source. There is no WACC field. Sector metrics and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("The price needs a decade of 12 percent growth; the base case gets to eight"), not the company's name alone. The opening gives what the price implies and how demanding that is, the range and expected value against the price, and the one or two assumptions the value turns on. The body follows the question, with only the tables it needs and a row only where there is a figure. The note closes on the signposts and what would change the range. Sub-headings state the finding, never the step.

## Before sending

- One cost of capital and one three-year return on new investment run through the implied growth, the forecast and the continuing value.
- The net debt and share count used anywhere match the inputs stated once, and every number in the opening agrees with the figure it came from.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Where there are cases, each driver has one cut-off across them, the probabilities sum to 100 and rest on a stated base, and the expected value reconciles with the cases; a range and an expected value, no target, no rating word.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
