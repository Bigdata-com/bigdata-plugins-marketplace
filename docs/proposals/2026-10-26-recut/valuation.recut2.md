---
name: bigdata-valuation
description: >-
  What a company is worth: the growth, margin and return the price implies, a DCF with the equity
  bridge checked, multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is
  priced in. Not peers only: bigdata-comps.
---

# Valuation

Never a point value or a price target: a range of cases, an expected value, and what the price already assumes. A corporate reader (strategy, corporate development, investor relations) gets the same arithmetic for their own decision and none of the investor measures unless asked. Size the work to the question: "what growth does the price imply for Micron" gets the reverse DCF and one base-rate sentence, not the full model.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-valuation"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. Open a method file at the part named below only when the work needs more than this page gives.

## Method choices that are not the default

- **Expectations first.** Split enterprise value into steady-state value (normalised NOPAT over the cost of capital) and future value creation, solve for the growth and the competitive advantage period the price needs, and place that growth against the base rate for companies of this size, real converted to nominal, so the report can say "the price needs X percent growth at Y percent ROIIC, which Z percent of companies this size achieved" (`references/expectations.md`; `references/base-rates.md`).
- **One cost of capital through everything.** Prevailing and normalised WACC, each labelled assumed, a range of at least plus and minus one point in the sensitivity, and the value at the market-implied rate shown (`references/valuation.md`, cost of capital).
- **ROIC built from the statements.** NOPAT at the operating tax rate, invested capital from both sides, with and without goodwill, and a three-year rolling ROIIC (`references/roic.md`). The FactSet ROIC field is compared in one line, never mixed into the same table.
- **The forecast carries base rates.** Every growth and margin figure with its reference class, sample and period; growth blended toward the class median beyond three years, margins faded toward the sector mean; a year-by-year check that ROIC, turnover and implied capex hold together (`references/valuation.md`, forecast; `references/forecasting-discipline.md`).
- **Continuing value by the value-driver formula**, with g, RONIC and WACC stated, RONIC above WACC only where the evidence supports a durable advantage, and its share of value and implied EV/EBITDA reported against today's multiple.
- **Cases.** What must be true in each, probabilities from a reference class rather than a default split, equity as max(EV minus claims, 0), and the expected value averaged over values, never over inputs (`references/forecasting-discipline.md`).
- **Peers by value drivers**, the selection rule stated before the multiple (`references/multiples-and-peers.md`).
- **The market is right** unless there is a specific, evidenced reason it is not, and the report says what the reason is.
- Special cases (bank or insurer, deep cyclical, growth above 15 percent a year, emerging market, multi-business, distressed) each have a section in `references/valuation.md`.

## Where it goes wrong

- **A raw regression beta.** Nvidia's 60-month beta of 2.2 gave a 14 percent cost of capital at which no plausible forecast reached the price. Blume-adjust, compare with peers and the sector, and explain any cost of equity outside roughly 8 to 12 percent for a US large cap before using it.
- **The interest shield twice.** NOPAT uses the operating tax rate from the tax note; the shield lives once, in WACC.
- **Excess cash in the perpetuity.** Added once, in the bridge; operating cash stays at 2 percent of sales (5 for less predictable businesses).
- **Gross PP&E for net investment.** Capex is the change in net PP&E plus depreciation; net investment is the change in net PP&E. A negative implied capex, or a jump in ROIC with no driver, means an input is wrong.
- **The horizon set from the market-implied period**, which tests the price against itself. Quote it beside the chosen horizon as a comparison only.
- **A terminal multiple above today's with no reason.** Uncertainty goes into the cases, never into a higher discount rate or multiple.
- **Stock awards** treated as anything but a cost in the forecast.
- **A single year of ROIIC** read as evidence. Five annual periods allow a three-year figure and nothing longer.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, five periods being the limit; consensus to four years out as a snapshot with its vintage, with no revision history; the annual report in full with the fiscal year fixed, for the tax note, the bridge items, debt maturities and the cover-page share count; the risk-free rate and inflation for the cash-flow currency from the country data, never assumed while the tool is there; a beta from 60 monthly returns through the computing tool when prices are available, otherwise assumed with its source; no WACC field anywhere. Sector metrics and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the shared rules. Open with what the price implies and how rare that is, the range and expected value against the price, the one or two assumptions the value turns on, and what would change the reading. Then only the tables the question needs, a row only where there is a figure. For a corporate reader, the implications for their decision come before the investor measures.

## Before sending

- One WACC and one three-year ROIIC run through what the price implies, the forecast and the continuing value, and the beta passed its check or the report says why not.
- Every number in the opening agrees with its table.
- A range and an expected value, no target, no rating word.
