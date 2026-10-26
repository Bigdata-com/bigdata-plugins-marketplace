---
name: bigdata-valuation
description: >-
  What a company is worth: the growth, margin and return the price implies, a DCF with the equity
  bridge checked, multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is
  priced in. Not peers only: bigdata-comps.
---

# Valuation

## The job

The reader wants to know what a company is worth and what the current price already assumes, with the arithmetic visible so they can disagree with an input rather than with the conclusion. The answer is a range and the two or three assumptions it turns on, never a point value or a target. Size it to the question: "what growth does the price imply for Micron" is a reverse DCF and a base-rate sentence, not a model.

## Who is asking

A portfolio manager or analyst wants what the price implies, a range against the price, and what would change it; they know the vocabulary. A corporate reader (strategy, corporate development, investor relations) wants the same arithmetic for a different decision: a target's price against its value, their own share price against the plan, a competitor's rating. For them, leave out the investor machinery (implied competitive advantage period, steady-state P/E, who must own the stock) unless they ask, and write the implications for their decision. Give no buy, sell or hold to anyone.

## What a complete answer covers

A checklist, not an outline. Cover what the question needs and say in one line what you left out.

- What the price implies: enterprise value, the growth and return on new capital the price needs, and how rare that is against base rates.
- The cost of capital, stated once with its inputs, with beta checked (see below).
- History: five years of returns on capital and reinvestment, so the forecast starts from what the company has done.
- The forecast: revenue, margins and reinvestment, with every year checked for return on capital and implied growth.
- The continuing value, tested against its share of total value and the multiple it implies.
- The equity bridge per share, item by item.
- Sensitivity to the cost of capital and terminal growth, and three cases with probabilities and what must be true in each.
- A multiples cross-check against peers chosen by value drivers.
- The range against the price, and what would change the reading.

Special cases change the method: banks and insurers (price to book against return on equity, no enterprise value), cyclicals (mid-cycle margin next to consensus), high growth, emerging markets, multi-business and distressed companies. `valuation.md` has an entry for each.

## Where this goes wrong

Each of these has appeared in a real valuation and is cheap to prevent.

- **A raw regression beta pushed through CAPM.** Nvidia's 60-month beta of 2.2 gave a 14% cost of capital at which no plausible forecast reached the price. Blume-adjust it, compare it with peers and the sector, keep the cost of equity for a US large cap inside roughly 8 to 12% unless there is a stated reason, and show the value at the market-implied rate as well.
- **Excess cash counted twice**, once inside the perpetuity and again in the bridge. Operating cash (2% of sales, 5% for less predictable businesses) stays in invested capital; the excess is added once, in the bridge.
- **Capex from gross PP&E.** Capex is the change in net PP&E plus depreciation; net investment is the change in net PP&E.
- **Stock-based compensation deducted twice**, as a cost and again as future dilution. It is a cost in the forecast, and that is all.
- **A one-year return on new capital.** Bigdata.com carries five annual periods, so ROIIC is a three-year rolling figure and says so.
- **Consensus as the base case.** Consensus runs above outcomes. Every growth and margin figure gets its base rate from `base-rates.md`, with the sample and period named and the words "historical, not current".
- **The terminal value doing the work unnoticed.** State its share of value and the EV/EBITDA it implies against today's; if the implied multiple is above today's, explain why or change an input.
- **The horizon set from the market-implied advantage period.** That bakes the price into the test of the price. Set the horizon from maturity, advantage and visibility, and quote the implied period as a comparison.
- **Averaging inputs instead of values** across cases. Average the three values.
- **A price target.** The output is a range and an expected value.

## Data

From Bigdata.com: profile and quote; five fiscal years of annual statements, ratios and key metrics (annual interval, not the default quarters); segments; consensus to four years out with its vintage; the latest annual report in full (the tax note, debt maturities, the cover-page share count); the last earnings call transcript, with guidance, the capex plan and any targets quoted with the date; statements and estimates for four to eight peers; the government bond yield and inflation for the cash-flow currency from the country data; monthly prices for the stock and a broad index over 60 months for beta. Two or three searches, one aspect each, for the evidence behind the horizon: market growth and share, pricing, entrants and exits. The sector's conventions from the sector primer.

`working-with-bigdata.md` maps each of these to a tool and says what to do when a tool is missing. Read it before the first call.

## Methods

Open these when a step needs more than the checklist gives: `valuation.md` for the DCF mechanics, the bridge and the special cases; `expectations.md` for what the price implies; `roic.md` for rebuilding invested capital and NOPAT; `base-rates.md` for the growth, margin and return distributions; `multiples-and-peers.md` for the cross-check; `forecasting-discipline.md` for case probabilities.

## Write

Follow the house style. Open with the answer: what the price implies, the range against the price, the assumptions it turns on, what would change it. Then the tables the reader will want to check, in the order the question suggests. A table has a row only where there is a figure; what the data could not give is one line under Gaps, not a cell. Assumptions appear once, with their reasons. Every number carries its unit, its period and either a link or the word derived or assumed.

## Before sending

1. One cost of capital and one ROIIC run through what the price implies, the forecast and the continuing value.
2. Every number in the opening paragraph agrees with its table.
3. Beta passed the check, or the report says why not.
4. The bridge adds excess cash once; capex comes from net PP&E.
5. The output is a range and an expected value, with no target and no rating word.
