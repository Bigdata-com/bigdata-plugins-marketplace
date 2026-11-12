# Forecasting discipline

How to turn beliefs into numbers the reader can check, each stated next to the evidence that would disprove it. The output describes the balance of evidence and what would change it. It gives no buy, hold or sell call and no position size.

## Inputs

| Input | Where it comes from |
|---|---|
| Facts: reported numbers, guidance, dated events | Company tearsheet (statements, estimates with actuals and guidance), filings and transcripts through search, the corporate calendar |
| Opinions: management claims, broker views, ratings, targets | Transcripts, research and news through search; the ratings section of the tearsheet |
| Expectations: what the price and consensus imply | expectations.md; estimates |
| Base rates for weights and ranges | base-rates.md |
| Probabilities, scenario weights, thresholds | Chosen in the report, each with its reason |

## Questions that can be scored

Each question has a checkable outcome, a time window and a bearing on the decision. Prefer horizons of months to one year; three to five years out is close to unforecastable. For a long-horizon view, write several small dated questions whose answers inform the big one.

## Facts, opinions and expectations

- A fact can be disproved: a reported figure, a filed contract. An opinion cannot: a forecast, a rating, "management expects". Keep them in separate lists. When opinion outweighs fact, move toward the base rate.
- Expectations are what the price implies; fundamentals are what the analyst forecasts. Write the implied bar first. A variant view is a well-founded view meaningfully different from consensus.
- Cash is a fact and profit an opinion: reconcile earnings to cash flow.
- Ask whether a piece of news changes long-term cash flow or only an accounting line. EPS dilution from an acquisition looks causal but does not move the probability of the thesis; the present value of synergies against the premium paid does.

## Scenario weights from a reference class

Take the outside view first: place the case in a reference class, quote the base rate with its N and period, then add the specifics of the case (base-rates.md, choosing the reference class).

- Derive each scenario weight from the class (growth, margin, M&A or turnaround outcomes), state it with a reason and a date, and let the weights be asymmetric when the evidence is. Never use a default split such as 25/50/25 or 30/40/30. The step from frequency to weight is a judgment; say so once.
- Weights sum to 100 and include an explicit downside scenario.
- Use all the cases in the class, weighted by similarity, not one recalled analogy.
- Reference points: about 60 percent of acquisitions fail to create value for the acquirer; about half of new businesses survive five years.
- With no usable reference class, say so and widen the range. Do not default to 50 percent.

## Granular probabilities

- Use numbers, not words: readers have taken "serious possibility" to mean anything from 20 to 80 percent.
- Use granular integer percentages (70, 75, even 72). Granular forecasts score better, and forecasters who lean on 50 percent score worse.
- Check scope: the probability of a hazard over six months should usually be materially higher than over three.
- Independent estimates that agree at 75 percent justify a higher combined figure, because each carries information the others lack.
- Update by the right amount. Under-reaction comes from inattention and confirmation bias; over-reaction from weighting irrelevant news.

## Updating on evidence

P(H | evidence) = P(H) x L / [P(H) x L + (1 - P(H)) x (1 - L)], with L the reliability of the evidence. For an extrapolated trend, shrink toward the base rate: estimate = base rate + c x (observed - base rate), c between 0 and 1, with the period-to-period correlation r as the proxy for c (base-rates.md, regression to the mean).

## Expected value

E = sum over scenarios of p_i x V_i, with the p_i summing to 1. Show the loss case next to the gain case: the size of being right or wrong matters more than how often. A margin of safety is a substantial discount of price to expected value, wide enough to absorb error, costs and taxes (downside-and-catalysts.md, margin of safety).

## Ranges as wide as history

People set ranges too narrow: executives' 80 percent intervals for the stock market have contained the outcome about one time in three, and consensus dispersion of three-year growth has run at about half of history. Do not set a range narrower than the reference class without a stated reason, and include a decline case. Frequencies need a stable system; where the system has changed, widen further.

## Premortem

Assume the thesis has failed badly one year from now and write why. Treating the failure as fact produces more, and more specific, reasons than asking what could go wrong. List reasons independently, consolidate them, revise the plan, and revisit the list at each review. When the base case is bearish, run it on the bullish outcome.

## Kill criteria with dates

Name the main uncertain drivers and the working premise for each, with its evidence. For each premise, name the signposts that would make it unreliable and the events that could reverse the outcome. Each kill criterion has a driver, a threshold and a date. Take dates from the events calendar (next earnings), guidance in the estimates, and filing dates.

## Stating a view

In this order:

1. The bar the price implies.
2. The base rate for that bar.
3. The view as a probability with a date.
4. Supporting facts and supporting opinions, listed separately.
5. Disconfirming evidence from an explicit search, shown and weighed: the bear case, filings that contradict management, research with the opposite view.
6. Kill criteria with dates.
7. What would change the view, and by how many probability points.

## Scoring a forecast

Record each forecast with its probability and date so it can be scored with the Brier score, (forecast - outcome)^2 with the outcome 1 or 0, stating whether the score covers one side (0 to 1) or both (0 to 2). Good forecasts are calibrated, so 70 percent calls come true about 70 percent of the time, and discriminate, giving high probabilities to the events that happen.

## Interpretation and limits

- When quoting a base-rate average, give N, dispersion and period.
- Black swans cannot be forecast. Model gray swans, extreme but modelable events, with distributions.
- After a one-day move of 10 percent or more, classify the event and quote the base rate before explaining it, because a cause is easy to invent for any move (after-a-price-move.md).
- Where luck is large, judge the process, not the outcome. A post-mortem separates the information available at the time, the quality of the analysis, and luck.
