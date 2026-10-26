---
name: bigdata-valuation
description: >-
  What a company is worth: the growth, margin and return the price implies, a DCF with the equity
  bridge checked, multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is
  priced in. Not peers only: bigdata-comps.
---

# Valuation

This skill writes a valuation a professional reader can check line by line: what the price already assumes, stated first; an enterprise DCF in which growth is paid for by reinvestment and returns are checked every year; the equity bridge per share; and a range of three cases cross-checked against peer multiples. Never a point value or a price target. Size it to the question: "what growth does the price imply for Micron" gets the reverse DCF and its base-rate sentence, not the full model. A portfolio manager wants the range against the price and what would change it. A corporate reader (strategy, corporate development, investor relations) wants the same arithmetic for a different decision, a target's price against its value or their own share price against the plan, without the investor measures (competitive advantage period, steady-state P/E) unless they ask for them.

## Before starting

- If the Bigdata.com tools are not available, say so and ask the user to connect the Bigdata.com connector. Give no figures from memory in the meantime; an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-valuation"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need below to a tool, with fallbacks when a tool is missing. Read it before the first call. Open the method files named below when a step needs more than this page gives.

## Scope

Resolve the company and take its listing status from the lookup. Settle what the user wants (the full range, only what the price implies, or one input such as the cost of capital), the currency of the cash flows (it sets the risk-free rate), and whether a special case applies: bank or insurer, deep cyclical, growth above 15 percent a year, emerging market, multi-business, distressed. `references/valuation.md` has an entry for each. Ask a question only when the answer changes the work; otherwise state the assumption and go on. A private company has no price to read expectations from: offer a DCF on the statements the tearsheet carries, or hand off to `bigdata`.

## Gather

1. **The company's numbers.** Profile and quote, segments, five fiscal years of annual statements, ratios and key metrics (annual interval; five periods is the limit), consensus to four years out with its vintage and estimate counts. Invested capital, capex, gross and net PP&E and stock-based compensation are needed later.
2. **The annual filing.** The latest annual report in full, with its fiscal year fixed rather than inferred: the tax reconciliation, the notes behind each bridge item (pensions, leases, minorities, investments), debt maturities, the cover-page share count.
3. **Management's plan.** The last earnings call transcript: guidance, the capex plan and any medium-term targets, quoted with the call date. Targets are opinions and are recorded as such.
4. **Evidence for the horizon.** Two or three searches, one aspect each: market growth and the company's share, pricing in the industry, entrants and exits. The length of the competitive advantage and the return on new investment rest on this.
5. **Peers.** Four to eight, from a screen on industry and size and from peers named in filings, with statements, estimates and ratios, pulled as a set where the account allows.
6. **Cost-of-capital inputs.** The government bond yield and inflation for the cash-flow currency from the country data, dated. The equity risk premium, beta and target weights are assumed, each with its source. Compute beta from 60 monthly returns against a broad index when the prices are available.
7. **The sector primer.** The company's sector in `references/sector-primers.md`: its metrics, accounting traps and valuation conventions.

## Analyse

The cost of capital and the history come first, so that one discount rate and one return on new capital run through everything after.

1. **Cost of capital** (`references/valuation.md`, cost of capital; the inputs table in `references/roic.md`). Prevailing and normalised WACC, each labelled assumed, with a range of at least plus and minus one point carried to the sensitivity. Check beta before using it: Nvidia's raw 60-month beta of 2.2 gave a 14 percent cost of capital at which no plausible forecast reached the price. Blume-adjust it, compare it with peers and the sector, and treat a cost of equity outside roughly 8 to 12 percent for a US large cap as something to explain rather than use silently. Show the value at the market-implied rate as well.
2. **History** (`references/roic.md`). NOPAT at the operating tax rate from the tax note, with the interest shield living once, in WACC. Invested capital from both sides, with operating cash kept at 2 percent of sales (5 for less predictable businesses) and the excess stripped out. ROIC with and without goodwill. ROIIC as a three-year rolling figure, because five periods allow no longer window and a single year is never evidence. Compare the FactSet ROIC field in one line, never mixed into the same table.
3. **What the price implies** (`references/expectations.md`). EV from market cap and net debt, adding minorities, preferred, the pension deficit and leases where the EV field leaves them out. Split EV into steady-state value (normalised NOPAT over the cost of capital, with excess cash added once in the bridge and never inside the perpetuity) and future value creation; solve for the growth and the competitive advantage period the price needs; place that growth against the base rates in `references/base-rates.md`, real converted to nominal. The report should be able to say "the price needs X percent growth at Y percent ROIIC, which Z percent of companies this size achieved."
4. **Horizon** (`references/valuation.md`). Set the explicit period from time to maturity, the evidence on the competitive advantage from Gather step 4, and visibility. Quote the market-implied period beside it as a comparison. Do not set the horizon from it, or the price is being tested against itself.
5. **Revenue, margins and reinvestment** (`references/valuation.md`, `references/base-rates.md`). Treat consensus as biased upward: every growth and margin figure gets its base rate with sample and period, blended toward the class median beyond three years, with margins faded toward the sector mean. Capex is the change in net PP&E plus depreciation, and net investment is the change in net PP&E, never the change in gross PP&E. Stock awards are a cost in the forecast and nothing more. Check every year for ROIC, turnover and implied growth against forecast growth; a jump with no driver, or a negative implied capex, means an input is wrong.
6. **Continuing value** (`references/valuation.md`). The value-driver formula with g, RONIC and WACC stated, and RONIC above WACC only where the evidence supports a durable advantage. Report its share of total value and the EV/EBITDA it implies against today's multiple; an implied terminal multiple above today's needs a reason or a changed input. Uncertainty goes into the cases, not into a higher discount rate.
7. **Equity bridge, per share**, item by item, with the share count from the filing and the operating cash deduction shown.
8. **Sensitivity and cases** (`references/forecasting-discipline.md`). WACC by terminal growth on value per share, base case in the centre, with a RONIC row where the continuing value dominates. Three cases, with what must be true in each and probabilities anchored to a reference class rather than a default split; equity in each case is max(EV minus claims, 0); average the values, not the inputs.
9. **Multiples cross-check** (`references/multiples-and-peers.md`). One multiple, with the peers selected by value drivers and the selection rule stated first; the DCF-implied multiple, the peer median with and without the outlier and the justified multiple side by side, and any gap explained by a driver.
10. **The range against the price.** Assume the market is right unless there is a specific, evidenced reason it is not, and say what the reason is.

A narrow question gets steps 1, 3 and 10, with the arithmetic shown.

## Write

Follow `references/output-standard.md`. Lead with what the price implies and how rare that is against base rates, the range and expected value against the price, the one or two assumptions the value turns on, and what would change the reading. Then the tables a reader will want to check: what the price implies, the assumptions (value, range, reason, source, basis), history, the forecast, the continuing value and its checks, the bridge, the sensitivity, the cases, the multiples cross-check, and the range against the price. That is the natural order for a full valuation. A narrower question keeps only the tables it needs, and a table has a row only where there is a figure; what the data could not give is one line under Gaps. For a corporate reader, the implications for their decision come before the investor measures. A full valuation runs two to four pages, with history and the forecast at about five rows each.

## Checks before sending

1. One WACC and one three-year ROIIC run through what the price implies, the forecast and the continuing value, and beta passed the check or the report says why not.
2. NOPAT uses the operating tax rate, the interest shield appears only in WACC, and excess cash is added once, in the bridge.
3. Net investment is the change in net PP&E, and no forecast year has a negative implied capex or an unexplained jump in ROIC.
4. The continuing value's share and its implied terminal multiple are reported, and the horizon was not set from the market-implied period.
5. Probabilities sum to 100 with a named reference class, and the expected value averages values.
6. Every number in the opening agrees with its table, and the output is a range and an expected value, with no target and no rating word.
