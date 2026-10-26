---
name: bigdata-valuation
description: >-
  What a company is worth: the growth, margin and return the price implies, a DCF with the equity
  bridge checked, multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is
  priced in. Not peers only: bigdata-comps.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, valuation, multiples-and-peers, base-rates, roic, forecasting-discipline
  bigdata-sector-primer: auto
---

# Valuation

This skill writes a valuation a professional reader can check line by line: what the price already assumes, stated first and without judgment, then an enterprise DCF in which growth is paid for by reinvestment, returns are checked every year, the continuing value is tested against its share of the total and the multiple it implies, and the equity bridge is shown per share. It ends in a range of three probability-weighted cases with a sensitivity table, cross-checked with peer multiples, never in a point value or a price target. It is sized to the question: "what growth does the price imply for Micron?" gets the reverse DCF with its arithmetic and the base-rate sentence, not the full model.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-valuation"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Establish three things before gathering data: what the user wants (a full valuation range, only what the price implies, or one input such as the cost of capital or the terminal value), the currency of the cash flows (which sets the risk-free rate), and the type of business, because a bank, an insurer, a deep cyclical, a company growing above 15 percent a year, an emerging-market company, a multi-business company and a distressed one each need a special case. The subject may be the user's own company, a competitor or an acquisition target; write the implications for that reader, and still give no target. The valuation date is today and the price is the latest close in the tearsheet.

Ask one question only when the answer changes the work: the name resolves to more than one listing, or the user seems to hold a cost-of-capital or horizon assumption they want used. Otherwise state the assumptions in the Assumptions line and proceed. Done when the company, the request, the cash-flow currency and the special case (or none) are stated.

If the lookup returns the company as Private, say there is no price to read expectations from and no consensus to anchor on. Offer a DCF from whatever statements the tearsheet carries, without the price-implied and benchmark steps, or hand off to `bigdata` for a document-based profile.

## Gather

Work through these in order.

1. **The company's numbers.** Profile and quote, and revenue by segment and geography; five fiscal years of annual statements, ratios and key metrics (five periods is the most available, and no older periods exist); consensus estimates with their vintage. Done when the price and 52-week range, market cap, the EV field, five fiscal years of statements (the data's limit, noted in Gaps when more would have helped), invested capital, capex, gross and net PP&E, stock-based compensation, consensus to four years out with its vintage and estimate counts, and the segments are in hand.
2. **The annual filing notes.** The latest annual report in full, with its fiscal year fixed rather than inferred. Read the tax reconciliation and every note behind an item in `references/valuation.md` step 10, plus debt maturities and the share count on the cover page. Done when each bridge item has a figure with its page, or is marked not disclosed.
3. **Management's plan.** The full transcript of the last earnings call, with its period fixed rather than inferred. Done when guidance, the capex plan and any medium-term targets are quoted verbatim with the call date. Management targets are opinions, recorded as such.
4. **Evidence for the horizon and the terminal return.** Two or three searches, one aspect each: market growth and the company's share, pricing in the industry, entrants and exits. Done when the length of the competitive advantage and the return on new investment after it have at least one dated piece of evidence each.
5. **Peers for the cross-check.** Candidates from a screen on the industry and size and from peers named in filings, then annual statements, estimates and ratios for the peer set, pulled as a set rather than one company at a time where the account allows, for four to eight peers. Done when each candidate's EV inputs, forward EBITA or the sector's multiple base, ROIC and consensus growth are in hand for the selection in Analyse step 13.
6. **Cost-of-capital inputs.** Not in Bigdata.com, except where the country's economic data carries the government bond yield and inflation for the currency of the cash flows; take them from there with the date, labelled reported. The equity risk premium, beta and target weights are assumed, each with its source and date. If monthly prices for the stock and a broad index over the last 60 months are available, compute beta from the 60 monthly returns, with the working shown. Done when each input has a value, a date and a Basis label, and beta is computed or its source named.
7. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the metrics, accounting-traps and valuation-conventions subsections. Done when the sector's convention is noted, or its absence is stated.

## Analyse

The cost of capital and the history come first, so one discount rate and one ROIIC run through every later step.

1. **Cost of capital.** `references/valuation.md` step 3, with the inputs table in `references/roic.md`; name the unlevering formula used. Done when every input has a source and a date, prevailing and normalized WACC are each labelled assumed, the two checks in step 3 pass, and a range of at least plus and minus 1 point is carried to the sensitivity.

2. **Rebuild history.** `references/roic.md` steps 1 to 11 and `references/valuation.md` steps 1 and 2: NOPAT at the operating tax rate from the tax note (the interest shield lives once, in WACC), invested capital from both sides, excess cash stripped at the roic.md step 6 allowance (2 percent of sales, 5 percent for less predictable or faster-growing companies), ROIC with and without goodwill, margin times turnover, and ROIIC as a three-year rolling figure, labelled (five annual periods allow no longer window; a single year is never evidence). Done when the history table exists and the FactSet ROIC field is compared in one line, never mixed into the same table.

3. **What the price implies.** `references/expectations.md` steps 1 to 5 at the step 1 WACC and the step 2 ROIIC. Build EV from market cap and net debt, adding minorities, preferred, the pension deficit and leases when the EV field leaves them out. Split EV with formula 1: steady-state value = normalised NOPAT / cost of capital, with excess cash added once in the equity bridge, never inside the perpetuity. Solve formula 2 for implied growth and formula 3a for the implied competitive advantage period. Place the implied growth in its size and horizon class with `references/base-rates.md`, converting real to nominal. Done when the report can say "the price needs X percent NOPAT growth at Y percent ROIIC, which Z percent of companies in the A to B size class achieved" with every input labelled.

4. **Horizon.** `references/valuation.md` step 4: set the explicit period by time to maturity, the length of the competitive advantage (judged from the Gather step 4 evidence and the reversion table in `references/roic.md`) and visibility. Do not bound it with the market-implied advantage period from step 3, because that would set the forecast from the price it is meant to test; quote the implied period next to the chosen horizon as a comparison only. Done when the horizon, its reasons and the growth path fading to the terminal rate are stated.

5. **Revenue and margins.** `references/valuation.md` step 5, treating consensus as biased upward. Every growth and margin figure gets its base rate from `references/base-rates.md` steps 2 to 6 (growth by size class and horizon, blended toward the class median beyond three years; margins faded toward the sector mean with the horizon-matched r). Done when every line has a driver and every growth or margin claim carries its base-rate sentence with sample and period.

6. **Reinvestment.** `references/valuation.md` step 6: capex = change in net PP&E + depreciation, and net investment = change in net PP&E; never the change in gross PP&E. Future stock awards go in the forecast as a cost. Done when capex, depreciation and net investment are shown for each year.

7. **Check every forecast year.** `references/valuation.md` step 7. Done when the year-by-year table shows ROIC, turnover and implied against forecast growth with no unexplained jump and no negative implied capex.

8. **Continuing value.** `references/valuation.md` step 8, with RONIC above WACC only where the Gather step 4 evidence supports a durable advantage. Uncertainty goes into the cases, not into a higher discount rate or a haircut. Done when g, RONIC and WACC are stated with reasons.

9. **Test the continuing value.** `references/valuation.md` step 9 and `references/expectations.md` formula 5; the UBS terminal-share figures are a rule of thumb, not a statistic. Done when the terminal share and the implied terminal EV/EBITDA against today's are reported and any breach is explained.

10. **Bridge to equity, per share.** `references/valuation.md` step 10, item by item, with the share count from the filing. Done when the bridge table shows every item in total and per share, including the operating cash deducted.

11. **Sensitivity.** `references/valuation.md` step 11: WACC by terminal growth on value per share, base case in the center, with a RONIC row where the continuing value dominates. Done when a reader can see how far value moves for half a point of WACC.

12. **Three cases.** `references/valuation.md` step 11, with probabilities from `references/forecasting-discipline.md` steps 3 and 4, each anchored to a reference-class share from `references/base-rates.md`, never a default split. Equity in each case is max(EV - claims, 0). Average the values, not the inputs. Done when three values, their probabilities with the source of each weight, what must be true in each, the expected value and the loss case are shown.

13. **Multiples cross-check.** `references/multiples-and-peers.md` steps 1 to 10 for one multiple, including the peer selection by value drivers in step 7 with the selection rule stated before any multiple is shown. Done when the DCF-implied multiple, the peer median with and without the outlier and the justified multiple sit side by side and any gap is explained by a driver.

14. **Benchmark and range.** `references/valuation.md` step 12. Assume the market is right unless there is a specific reason it is not, and say what that reason is. Done when the range, the expected value, the gap to the price in economic terms and the implied expectations from step 3 are stated together.

A narrow question gets steps 1, 3 and 14 (the cost of capital, what the price implies, against the price), with the arithmetic shown.

Special cases: bank or insurer, cyclical, high growth, emerging market, multi-business, distressed. Read the matching entry under "Special cases" in `references/valuation.md` and apply it before step 4; for a cyclical show the mid-cycle margin next to the consensus margin, and for a bank cross-check with P/B against ROE, not EV multiples. Done when the case applied is named in the Assumptions line, or none applies.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) valuation, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.

## The valuation
Four to eight sentences: what the price implies and how rare that is against base rates, the value
range and the expected value against the price, the one or two assumptions the value turns on, and
what would change the reading. No rating, no target.

## What the price implies
| Measure | Value | Basis | Source |
EV and its build, NOPAT1, cost of capital and range, implied growth at the stated ROIIC, implied
competitive advantage period, steady-state share of EV, P/E against steady-state P/E, base-rate share.

## Assumptions
| Input | Value | Range | Reason | Source and date | Basis |
Risk-free, equity risk premium, beta, cost of debt, weights, WACC prevailing and normalized,
operating tax rate, horizon (with the market-implied period beside it), terminal g, RONIC, special case.

## History
| FY | Revenue | EBITA margin | Turnover | ROIC ex goodwill | ROIC with goodwill | ROIIC 3-yr |
Basis and sources note under the table. Definition line. FactSet ROIC compared in one line.

## Forecast
| Year | Revenue growth | Consensus | Base rate | EBITA margin | Basis |
| Year | Net investment | ROIC | Turnover | Implied growth (ROIC x reinvestment) | FCF | Basis |
First years, a fade year and the last year at minimum. Sources note under the tables.

## Continuing value and checks
Formula with g, RONIC and WACC; PV of explicit period and of CV; terminal share against the rule
of thumb; implied terminal EV/EBITDA against today's.

## Equity bridge
| Item | Amount | Per share | Basis | Source |
Ending in equity value per share and the share count source.

## Sensitivity
WACC rows by terminal growth columns, value per share, base case in the center.

## Cases
| Case | What must be true | Value per share | Probability | Weight anchor | Basis | Source |
Expected value; loss case next to gain case.

## Multiples cross-check
| Measure | Company | Peer median (ex outlier) | Justified | DCF-implied | Basis | Source |
Selection rule in one line.

## Range against the price
Value range, expected value, price and 52-week range, the gap explained in economic terms.

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. To fit, keep History and Forecast to five rows each and the continuing-value section to four lines; when the user asked for part of the valuation (what the price implies, one input), drop the sections they did not ask for. Offer a spreadsheet-style table export or a Word document when the host can create files. For a narrow question, answer it in the method's terms with the relevant table and the sources, and keep the footer.

## Checks before sending

1. "What the price implies" comes before the forecast, and the summary reads consistently with it.
2. One WACC and one three-year ROIIC run through the price-implied step, the forecast and the continuing value; every cost-of-capital input has a source and a date, and the risk-free rate is in the currency of the cash flows.
3. NOPAT uses the operating tax rate from the tax note, and the interest shield appears only in WACC.
4. ROIC, turnover and implied growth are shown for every forecast year, with no unexplained jump and no negative implied capex; net investment is the change in net PP&E.
5. The continuing value uses the value-driver formula with a stated RONIC, its share of EV is reported, and the implied terminal multiple is below today's or the reason is given.
6. The horizon is set by maturity, advantage and visibility; the market-implied period appears only as a comparison.
7. The bridge lists every item per share, the operating cash deduction is 2 or 5 percent of sales, and the share count comes from a filing.
8. The WACC by growth table is present, with the base case in the center.
9. Case probabilities are integers that sum to 100, each anchored to a named reference class; the expected value averages values, not inputs.
10. Each growth and margin claim carries a base-rate sentence with sample and period; dated figures carry their source and period and are called historical. No table passes eight columns.
11. The output is a range and an expected value, with the matching special case applied where one fits. No price target, no buy, hold or sell, no rating word.

## Hand-offs

- The user wants peer multiples on their own: `bigdata-comps`. The cases built out with signposts: `bigdata-scenarios`. The view and the claims behind it: `bigdata-thesis`.
- The subject is an acquisition target and the user wants the price, premium and synergies: `bigdata-deal-analysis`.
- The company reports soon and the user wants the setup: `bigdata-earnings-preview`.
- After delivering, make one offer: save the valuation to the user's Bigdata.com account so later searches can find it. Act only on a clear yes.
