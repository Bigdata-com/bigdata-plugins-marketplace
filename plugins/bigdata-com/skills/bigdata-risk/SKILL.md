---
name: bigdata-risk
description: >-
  Downside analysis of a stock from Bigdata.com data: what would break the thesis, how much is at
  risk in each case, the floors from assets and private-market value, balance sheet and liquidity,
  and the risks ranked by probability and size with the signals to watch. Use when the user asks
  what could go wrong, about the risks, the downside, the bear case, or how much they could lose.
  Not for the credit of the company's debt, which bigdata-credit covers.metadata:
  bigdata-refs: working-with-bigdata, output-standard, downside-and-catalysts, forecasting-discipline, earnings-quality, credit, expectations
  bigdata-sector-primer: auto
---

# Risk

This skill answers "what could go wrong and how much could I lose" the way Klarman and Graham and Dodd define risk: the probability and amount of permanent loss at today's price, not volatility or beta. So it works downside first: what breaks each value driver and what the stock is worth then, what the floors are, whether the balance sheet survives stress, which risks matter most by probability and size, how the thesis fails in a premortem, and the dated conditions that would end it. It never gives a buy, hold or sell call, a stop-loss or a position size. A narrow question ("what is the floor under Intel?") gets the floor values per share against the price and stops.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-risk"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Establish the holder's side and horizon if the user gave them: a long holder's downside is the stock falling; a short seller's is the stock rising, and the premortem then runs on the bullish outcome. Assume a long holder and a twelve-month horizon when the user does not say, and state it. If the user has a thesis, take its drivers; otherwise name the three to five drivers the price depends on (sales growth, margin, capital intensity, the balance sheet, the duration of excess returns).

Ask one question only if the answer changes the work: the user says "my thesis" without stating it and the drivers cannot be inferred, or the name is ambiguous. Otherwise proceed.

Narrow questions map to steps in the Analyse section:
- "What is the floor?" or "how much could I lose?": steps 1 to 3.
- "Can the balance sheet take a downturn?": step 4, with the maturity table.
- "What are the biggest risks?": step 6, with the ranked table and early signals, drawing on steps 2 to 5 only as far as the ranking needs.
- "What would make me sell?": steps 8 and 9, stated as conditions, never as a call.

If the company is Private, say there is no price to measure loss against and give the floors and the balance-sheet stress only. For a bank or an insurer, asset and liability values are hard to verify, so test book value and earnings quality in place of liquidation value and use capital ratios in place of net debt (`references/downside-and-catalysts.md` and `references/credit.md`, interpretation rules).

## Gather

Each step says what it must produce.

1. **Tearsheet.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, events_calendar, estimates` first, then `fundamentals, revenue_segmentation`, then `company_funds_holders, fund_trends_history, mergers_acquisitions, c_level_leadership`. Done when the price, market cap, EV, net debt, share count, five years of statements and the balance sheet line by line, segment revenue, consensus with its vintage, the next report date, the FactSet Altman Z and Piotroski fields, and the holder changes over the last year are in hand.
2. **The annual filing.** Search and fetch the latest annual report and read the risk factors (and what changed from the prior year's), the debt note (maturities, covenants, facilities), pensions, leases, contingent liabilities and guarantees, deconsolidated entities, related parties, and the auditor's report. Done when each is noted with its section, or marked not disclosed.
3. **Material events since the annual filing.** Search the company's filings and releases since then (8-K or local equivalent: guidance changes, financing, management changes, litigation, rating actions). Done when each event is listed with its date.
4. **Credit signals.** `bigdata_get_credit_factor` for the company; read the tool description for what it returns. Done when the signals are recorded, or the tool's coverage gap is named.
5. **Risks by category.** One search each, recent window: regulatory and legal (investigations, litigation, antitrust, policy changes); competitive (share loss, price cuts, entrants, customer losses); operational (supply chain, key people, technology and cyber, execution); macro exposure (cycle, rates, currency, commodities, geopolitics); management and governance (departures, related parties, insider selling, activists). Done when each category has dated evidence or the searches found none.
6. **The disconfirming case.** Searches for bear-case research, short-seller reports, and filings that contradict management's statements. Done when the strongest opposing argument is quoted with its source, or the searches found none.
7. **Private-market comparables.** Searches for recent acquisitions of comparable businesses and the multiples paid, and the peers' `mergers_acquisitions` histories. Done when two or more transactions have a multiple, a date, the buyer, and how the deal was financed, or the comparables are named as not available.
8. **Management's account.** Search and fetch the last earnings call. Done when management's statements on the drivers, the balance sheet and the risks analysts pressed on are quoted.
9. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read its accounting traps, valuation conventions and macro sections.

## Analyse

Load `references/downside-and-catalysts.md` before step 1, `references/credit.md` before step 4, `references/earnings-quality.md` before step 5 and `references/forecasting-discipline.md` before step 6. Each step ends in what it must produce.

1. **What the price already assumes.** Price, market cap and EV; the forward P/E against one over an assumed cost of equity (above that, the price pays for growth and value creation; below it, the market expects none or expects earnings to fade); consensus growth and margin for the next two years (method step 1). A stock priced for high growth falls hard on a miss. Done when one line says what must go right for the current price to hold. The full implied-growth arithmetic belongs to `bigdata-valuation`.

2. **What breaks each driver, and by how much.** For each driver: the event that breaks it, with the evidence that it could happen; the driver's value if broken (for example, revenue growth at the bottom of the reference class, margin back to the trough of the last cycle); and the value per share in that case. Compute that value with the stressed cash-flow approach in method step 2: capex equal to depreciation, no cash released from working capital, a discount rate as conservative as the forecasts (assumed), and use rebuilt earnings where step 5 finds flags. Done when every driver has a break event, a value per share, and the loss from today's price, each labelled.

3. **The floors.** Per share, against the price (method step 2, formulas 2 to 4): net cash; net-net working capital; current-asset value; tangible book; liquidation value with the haircuts from table 1, which are 1930s industrial and retail experience and illustrative only (verify); and private-market value, from multiples that informed buyers recently paid for comparable businesses (Klarman, Margin of Safety, ch. 8). Treat private-market value as one input, not the arbiter: companies in an industry differ, multiples change, buyers overpay, and multiples paid with cheap debt or inflated stock overstate value. Compare earning power with asset value (formula 7): where earnings value far exceeds asset value, the assets show what remains if the advantage erodes. When the methods diverge, use the lower unless the report justifies otherwise. For software, platforms and services, tangible floors are thin: use the stressed cash-flow value and cash runway. For a cyclical, use multi-year average earnings. Done when each floor is shown per share with the price as a percentage of it, the downside range is stated low to high, and the margin of safety against the lower value is computed with formula 1.

4. **The balance sheet and liquidity under stress.** From `references/credit.md`, steps 2 to 8: the stability of the business (five-year EBITDA range and the sector's EBITDA volatility from table 3); leverage and coverage on the same period (formulas 1 to 4, total interest); the implied rating bucket from the medians in table 1 (US 2011-2013, verify); coverage after an assumed EBIT shock at least as large as the worst year in the window or the sector volatility (formula 6); debt due within 24 months with amounts, dates and funding source, covenant headroom, and whether repayment depends on market access; claims outside the debt line (leases, after-tax pension deficit, contingent liabilities, guarantees, deconsolidated entities, securitised receivables, related-party loans); free cash flow against capex and depreciation. Run the distress signals in the credit method's interpretation rules. Quote Altman Z and Piotroski as reported, with no cutoffs. Then mark each event that would turn a temporary price fall into a permanent loss (a need to raise capital, forced selling, a covenant breach, loss of market access) as present, absent or unknown (downside method step 3). Done when coverage after the shock, the maturity table and the permanent-loss events are stated.

5. **Accounting risk.** From `references/earnings-quality.md`: the accrual ratio over five periods (formula 1), recurring one-offs counted by recurrence, reserve releases, the equity residual, and the governance events, then the flags table with a severity level from table 3 (a scale designed for these skills, labelled so). Done when the level and the flags behind it are stated; where the level is 3 or 4, the figures not to rely on are named and step 2 uses the rebuilt earnings.

6. **The risks ranked by probability and size.** List the risks from steps 2 to 5 and the category searches, merging duplicates. For each: the probability over a stated window as an integer percent, anchored to a reference class where one exists and labelled judgment (`references/forecasting-discipline.md`, rule 2; a longer window carries a higher probability than a shorter one); the size as value per share lost, from step 2 or 3; whether the loss would be permanent or temporary; and the early signal that would show it first, with where to watch for it. Rank by expected loss (probability times size). Separate facts from opinions in the evidence: management claims, broker views and targets are opinions. Done when every ranked risk has a probability, a size, a permanence mark and an early signal.

7. **Why it is cheap and who is selling**, when the stock has fallen. Name the reason or say none was found, which is itself a warning; check the forced-seller constraints (index deletion, a downgrade below investment grade, a dividend cut, spin-off selling) against the holder changes (downside method steps 4 and 5). Done when the reason and the seller are named or marked unknown.

8. **The premortem.** Assume that one year from now the holding has lost badly, and write why (`references/forecasting-discipline.md`, rule 3). At least three reasons, each mapped to a driver or a kill criterion; when the user is short or the base case is bearish, run it on the bullish outcome. Done when the reasons are written and mapped.

9. **Kill criteria with dates.** From table 4 of the downside method and rule 4 of the forecasting method: for each main driver, the threshold that would end the thesis and the date by which it is checked, taken from the events calendar, guidance and filing dates. Include value falling below the price, a confirmed accounting or governance failure, funding or covenant stress, and a catalyst that does not occur by its date. A price fall alone is not a kill condition: re-test the thesis on value. Done when each criterion has a driver, a checkable threshold and a date.

Special cases:
- Non-US listings and emerging markets: demand a wider margin for incomplete disclosure, restricted share classes and illiquidity, and compare local accounting with peers in other countries.
- Loss-making or early-stage companies: the sources give no cash-runway method; state the burn rate and the runway as derived and the funding assumption as assumed, and treat a need to raise capital as a permanent-loss event.
- Cyclicals: set the break cases and the floors on multi-year average earnings and mid-cycle EBITDA, not the latest year.
- Holding companies: name which legal entity owes each debt, since holding-company debt can default while operating subsidiaries carry on.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) downside and risks, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.
Holder and horizon: <long or short>, <window>. Assumptions: cost of equity, stressed discount
rate, liquidation haircuts, EBIT shock, each with its basis.

## The downside
Four to eight sentences: what the price assumes, the downside range and floors against the price,
whether the balance sheet survives the stress case, the two or three risks that dominate expected
loss, and the earliest dated signal. No rating and no recommendation.

## What the price assumes
One short table: price, EV, forward P/E, one over the assumed cost of equity, consensus growth
and margin, each with Basis and Source.

## What breaks each driver
| Driver | What breaks it | Evidence | Value per share if broken | Loss from price | Basis | Source |

## Floors
| Floor | Value per share | Price as % of floor | Method and haircuts | Basis | Source |
Rows: net cash, net-net working capital, current-asset value, tangible book, liquidation,
private-market value, stressed cash-flow value. Downside range; margin of safety vs the lower value.

## Balance sheet and liquidity under stress
| Measure | Value | Rating median band | Basis | Source |
Coverage after the assumed shock; maturities within 24 months (amount, date, funding source);
claims outside the debt line; distress signals; Altman Z and Piotroski as reported; the
permanent-loss events marked present, absent or unknown.

## Accounting risk
Severity level with its reason and the flags behind it.

## Risks ranked by probability and size
| Rank | Risk | Category | Probability (window) | Size per share | Expected loss | Permanent? | Early signal | Source |

## Why it is cheap and who is selling
Only when the stock has fallen.

## Premortem
Three or more reasons, each mapped to a driver or kill criterion.

## Kill criteria
| Condition | Driver | Threshold | Date | Where the date comes from |

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. The cost of equity, the discount rate for the stressed case, the haircuts, the shock size and the probabilities appear once in an Assumptions line with their basis. For a narrow question, answer with the relevant step, its table and the sources, and keep the footer.

## Checks before sending

1. The downside and the floors come before anything that reads as upside.
2. Every floor is per share with the price as a percentage of it, and the liquidation haircuts are labelled illustrative 1930s figures (verify).
3. Private-market multiples name the deals, dates and financing, and inflated or debt-fuelled multiples are flagged.
4. The stress shock is at least as large as the worst year in the window or the sector volatility, and maturities within 24 months have amounts and dates.
5. Every ranked risk has an integer probability with a window, a size per share, a permanence mark and an early signal.
6. The premortem has at least three reasons, each mapped to a driver or a kill criterion.
7. Every kill criterion has a driver, a checkable threshold and a date; none is a price level alone.
8. Altman Z and Piotroski are quoted as reported, with no zones.
9. Facts and opinions are labelled apart, and the disconfirming search is shown with its result.
10. No buy, hold, sell, stop-loss, position size or rating word.

## Hand-offs

- The user wants the credit of the company's bonds or loans: `bigdata-credit`. The accounting in depth: `bigdata-earnings-quality`.
- The user wants the upside case and the full thesis: `bigdata-thesis`. Probability-weighted cases with an expected value: `bigdata-scenarios`.
- The user wants the dated events that could close or widen the gap: `bigdata-catalysts`.
- After delivering, make one offer: a monitor on the early signals and kill criteria (filings, rating actions, guidance changes, the named risks) until the last kill date. Act only on a clear yes.
