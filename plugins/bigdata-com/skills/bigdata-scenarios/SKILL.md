---
name: bigdata-scenarios
description: >-
  Base, upside and downside cases for a company: driver assumptions, value and probability in
  each, expected value, signposts. Use for scenarios, probability-weighted value, what if a driver
  changes. Not the central DCF: bigdata-valuation.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline, base-rates, expectations, valuation, operating-leverage-and-tam
  bigdata-sector-primer: auto
---

# Scenarios

This skill builds three cases a professional reader can argue with: what the price already assumes, the two or three drivers that decide which case happens, each case run through the whole model so that a change in sales also moves margins, reinvestment and returns, a value per share for each, probabilities that come from what happened to similar companies rather than from a habit of 25, 50 and 25, the expected value next to the price with the loss case beside the gain case, and the dated signposts that will say which case is unfolding. It is sized to the question. "What happens to Micron if DRAM prices fall 10 percent?" gets the driver sensitivity and the value effect with the arithmetic, not three full cases.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-scenarios"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Establish the horizon (default: explicit years to the company's maturity, usually five to seven as `references/valuation.md` step 4 sets out, fading to the terminal rate after them, with a continuing value; signposts over the next twelve months, because forecast skill decays beyond about a year), the drivers the user wants tested if they named any, and whether the user brings their own cases or probabilities. If they do, test them against the reference class rather than replacing them, and say where they sit.

Ask one question only when the answer changes the work: the name resolves to more than one listing, or the user asks "what if a driver changes" without naming the driver or the size of the change. The subject may be the user's own company, a competitor, a customer or a supplier ("what happens to us if volumes fall 10 percent"); write the implications for that reader, and still give no call. Otherwise state the assumptions under the header and proceed. Done when the company, horizon, drivers and reader are stated.

If the company is Private, say there is no price to compare the expected value with, and build the cases on reported statements only.

## Gather

Work through these in order.

1. **The company's numbers.** Profile and quote, the ratings and price targets, and revenue by segment and geography; five fiscal years of annual statements, ratios and key metrics; consensus estimates with their vintage. Done when the price, EV and its inputs, five annual periods of statements (the data's limit; say so in Gaps), consensus to four years out with vintage and estimate counts, and the target range are in hand.
2. **Guidance and management's targets.** The full transcript of the last earnings call, with its period fixed rather than inferred. Done when guidance ranges, capex plans and medium-term targets are quoted verbatim with the call date.
3. **The debate.** Three or four searches, one aspect each: the bull arguments in research and news, the bear arguments, the reasons behind the highest and lowest analyst targets, and the controversy the last call's questions circled. Done when each candidate swing driver has the arguments on both sides with dates and sources.
4. **Driver evidence.** One search per swing driver (pricing, volumes, capacity, adoption, the macro series the driver depends on). Done when each driver has at least one dated data point, or is marked as having none.
5. **Cost structure.** Searches of transcripts and filings for fixed and variable costs, capacity utilization and the split of past margin changes into price, mix and volume. Done when the contribution margin can be estimated, or the split is marked not disclosed and will be estimated by regression.
6. **Bridge items.** From the latest annual filing by search and fetch: debt and maturities, leases, pensions, minorities, options and RSUs, the share count. Done when each claim on the enterprise value has a figure.
7. **Signpost dates.** The corporate calendar for the company's next earnings dates and conferences, plus searches of filings and news for dated regulatory, product or contract decisions, which the calendar does not carry. Done when every case has at least one dated event that would move its probability.
8. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the value-driver, profit-pool and macro subsections for the drivers and the cycle before building cases. Done when the sector's drivers and cycle are noted, or their absence is stated.

## Analyse

1. **What the price implies.** `references/expectations.md` steps 1 to 4 (formulas 1 and 2), at the three-year rolling ROIIC and the WACC from `references/valuation.md` step 3 (assumed, with a range of plus and minus 1 point). This WACC is used in every case. Done when the report can say which case the price sits closest to before any case is built.

2. **Choose the swing drivers.** Two or three drivers that decide value, held apart from everything else, which stays the same across cases so the cases can be read. Pick them with the value-trigger rule in `references/expectations.md` formula 4, classified on the three-year rolling ROIIC (labelled; a single year is never evidence). Done when each driver has the reason it decides value and the consensus assumption for it.

3. **Find the reference class for each driver.** `references/base-rates.md` steps 1 to 5, reading the distribution rather than the average and converting real to nominal with the inflation assumption stated. Done when each driver has its distribution with N, sample and period.

4. **Set the base case.** Consensus for the years it covers (up to four years out); for the later explicit years, blend toward the class median as `references/base-rates.md` step 6 sets out, fading to the terminal rate by the last explicit year. Treat consensus as biased upward (`references/base-rates.md` table 11, historical, not current) and say how far the base sits from it. Done when the base-case drivers are tabled next to consensus and the base rate, and any difference from consensus is explained.

5. **Set the downside and upside.** Place each at a stated point of the reference-class distribution, with a range at least as wide as history (`references/base-rates.md` step 7 and table 11). The downside includes a decline case where the class shows one, quoted from table 12 with its sample and period, historical, not current. Done when each case's driver values carry the share of the class that reached them.

6. **Run the second-order effects.** Changes in sales reach margins through operating leverage, and analysts consistently underestimate that link in both directions. From `references/operating-leverage-and-tam.md`: the contribution margin from the cost lines or the regression, checked against the sector's operating margin beta, with different incremental margins on the way down and the way up, and financial leverage on top. Then keep reinvestment consistent with growth (g = RONIC x net investment / NOPAT, with capex and net investment as `references/valuation.md` step 6 defines them) and check ROIC and turnover each year (`references/valuation.md` steps 6 and 7). Test each case's incremental margin against the threshold margin; growth below it destroys value. Done when each case has its margin, reinvestment, ROIC and turnover by year, and none rises without a stated reason.

7. **Value each case through the model.** `references/valuation.md` steps 8 to 11, with RONIC set by the case (near WACC in the downside, nearer the later-year ROIC in the upside only with evidence of a durable advantage) and the same WACC in every case, because uncertainty belongs in the cases and not in the discount rate. Bridge each case to equity per share with step 10; equity in each case = max(EV - claims, 0). Done when three values per share sit next to the price, each with its bridge.

8. **Assign the probabilities.** From `references/forecasting-discipline.md` rule 2 and steps 3 and 4. Start from the reference class: take the share of the class whose outcome falls in each case's range on the main swing driver, splitting the distribution at the midpoints between the case assumptions; then adjust each weight for the case evidence, say why and by how many points, and label the result judgment. Use integers that sum to 100; let the weights be asymmetric when the class and the evidence are. Never use a default split such as 25/50/25 or 30/40/30. With no usable reference class, say so and widen the range; do not default to 50. Done when each probability has its anchor, its adjustment, its reason and a date.

9. **Compute the expected value.** From `references/forecasting-discipline.md` formula 1: E = sum of p x V over the cases, averaging values, not inputs. Show the loss case next to the gain case, because the size of being right matters more than how often. Add the weight on the downside case at which the expected value equals the price (derived): hold the ratio of the base weight to the upside weight fixed at the step 8 values and solve for the downside weight, and say that this is how it was solved, because a different rule gives a different answer. It tells the reader what probability of the bad outcome the price already carries. Done when the expected value, its gap to the price, the loss and gain cases and the price-implied downside weight are shown.

10. **Test what happens if a driver changes.** The "if, then" analysis in `references/expectations.md` formula 4: move each swing driver 2 points either side of the base, or by the user's own shock size when they gave one ("DRAM prices fall 10 percent"), carry the second-order effects from step 6, and show the value per share. Done when each driver has its sensitivity row, and the driver that moves value most is named.

11. **Write the signposts.** From the linchpin method in `references/forecasting-discipline.md` rule 4: for each case, the observable that points to it, the threshold, the date or window (from the events calendar, guidance and filing dates), and how many probability points it would move. Record each probability with its date and resolution condition so it can be scored later (`references/forecasting-discipline.md` step 9). Done when every case has at least one dated signpost.

12. **Run the premortem.** From `references/forecasting-discipline.md` rule 3: assume the base case has failed badly a year from now and write at least three reasons, each mapped to a driver and a signpost. When the base case is bearish, run it on the bullish outcome instead. Done when the reasons are listed and each has a signpost.

A user who asks only what happens if one driver changes gets steps 1, 2, 6 and 10 for that driver, at the user's shock size, with the arithmetic.

Special cases: cyclicals, high growth, emerging markets, banks and insurers, and distressed companies. Read the matching entry under "Special cases" in `references/valuation.md` and build the cases its way: for a cyclical, a normal-cycle and a new-trend case (the 50/50 price fit there is a historical finding, not a default weight); for high growth, the addressable-market steps 2, 3 and 6 in `references/operating-leverage-and-tam.md`; for an emerging market, a crisis case with its probability and basis stated; for a bank or insurer, skip the operating-leverage step. Done when the case applied is named, or none applies.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) scenarios, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.

## The cases
Four to eight sentences: what the price implies, the swing drivers, the three values and their
probabilities with where the weights came from, the expected value against the price, the loss
case, and the first signpost with its date. No rating.

## What the price implies
| Measure | Value | Basis | Source |

## Swing drivers
| Driver | Why it decides value | Consensus assumption | Reference class (N, sample, period) | Source |

## Assumptions by case
| Driver or effect | Downside | Base | Upside | Consensus | Share of class reaching it | Basis | Source |
Rows for each swing driver, then incremental margin, EBIT margin, net investment, ROIC, turnover,
terminal g and RONIC.

## Value by case
| Case | EV | Claims | Equity value per share | Against price | Basis | Source |

## Probabilities
| Case | Reference-class anchor | Adjustment and reason | Probability | Date | Basis | Source |
Sum shown as 100.

## Expected value
The arithmetic written out; loss case next to gain case; downside weight at which the expected
value equals the price.

## If a driver changes
| Driver | -2 points | Base | +2 points | Basis | Source |

## Signposts
| Signpost | Points to | Threshold | Date or window | Probability shift | Source of the date |

## Premortem
Three or more reasons the base case fails, each with its signpost.

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. For a narrow question, answer it in the method's terms with the relevant table and the sources, and keep the footer.

## Checks before sending

1. "What the price implies" comes before the cases.
2. Two or three swing drivers, with everything else held the same across cases.
3. Each case's driver values carry the share of the reference class that reached them, with N, sample and period.
4. Second-order effects are run: margins move with sales through the contribution margin, and reinvestment is consistent with growth, with ROIC and turnover shown.
5. Probabilities are integers that sum to 100, each with a reference-class anchor and a stated adjustment; no default split.
6. The downside includes a decline case where the reference class shows one, and the range is at least as wide as history.
7. The expected value averages values, not inputs, and the loss case is shown next to the gain case.
8. Every signpost has a threshold and a date or window, and says how many probability points it moves.
9. The premortem lists at least three reasons, each tied to a signpost.
10. One WACC and the three-year ROIIC run through every case; the price-implied downside weight says how it was solved.
11. No price target, no buy, hold or sell, no rating word; the cost of capital is stated as an assumption with its range.

## Hand-offs

- The user wants the central valuation with the full DCF checks: `bigdata-valuation`. The view and its claims: `bigdata-thesis`. Cases around the next print only: `bigdata-earnings-preview`.
- After delivering, make one offer: a Bigdata.com monitor on the signposts, so the user hears when one fires. Act only on a clear yes.
