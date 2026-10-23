# Forecasting discipline

This method sets how a report turns beliefs into numbers a portfolio manager can check: scorable questions, facts kept apart from opinions and from what the price implies, scenario weights taken from a reference class, ranges as wide as history, a premortem, kill criteria with dates, and a view stated next to the evidence that would disprove it. It rests on Mauboussin's papers on forecasting and decisions (Credit Suisse, 2013 to 2016) and on "Expectations Investing" (2006). The output describes the balance of evidence and what would change it. It gives no buy, hold or sell call and no position size; the source papers discuss sizing, and that material is left out on purpose.

## When a skill loads this file

Load it wherever the report states probabilities, scenarios or a view: thesis and variant perception, scenarios, deep dive, earnings preview and review, risk, special situations. For a narrow question ("what are the odds X happens by June?") run steps 1, 3, 4 and 8 and answer with the probability, its reference class and its date.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Facts: reported numbers, guidance, dated events | `bigdata_company_tearsheet` (`fundamentals`, `estimates` with actuals and guidance), filings and transcripts via `bigdata_search`, `bigdata_events_calendar` | reported |
| Opinions: management claims, broker views, ratings, targets | Transcripts, research and news via `bigdata_search`; `analyst_data` | reported, as a claim |
| Expectations: what the price and consensus imply | `references/expectations.md`; `estimates` | derived |
| Base rates for weights and ranges | `references/base-rates.md` | reported (historical base rate) |
| Probabilities, scenario weights, thresholds | Chosen in the report, with reasons | assumed or judgment |

## Procedure

1. **Write each question so it can be scored.** A checkable outcome, a time window, and relevance to the decision (FC p.13). Prefer horizons of months to one year; forecasts 3 to 5 years out are close to unforecastable (FC pp.13, 17). For a long-horizon view, cluster several small dated questions whose pattern informs the big one (FC pp.14-15). Done when each question has an outcome, a date and a threshold.
2. **Separate facts, opinions and expectations** (rule 1). Done when each piece of evidence is tagged as one of the three.
3. **Take the outside view first.** Place the case in a reference class, quote the base rate with N and sample, then add the case specifics (FC p.11; MI pp.3-4; `references/base-rates.md`). Done when the base rate, N and sample period are quoted.
4. **Build the scenarios** (rule 2). Done when probabilities are integers that sum to 100, each with a reason and a reference-class number.
5. **Run a premortem** (rule 3). Done when at least three failure reasons are written, each mapped to a driver or a kill criterion. The minimum of three is this file's choice, not a figure from the papers.
6. **Write the kill criteria** (rule 4). Done when each has a driver, a threshold and a date.
7. **Compute the expected value and the range** (formula 1, rule 5), then apply the decision rules (rule 6). Done when the probability-weighted value, the low and high cases and the loss case are shown.
8. **State the view with its disconfirming evidence** (rule 7). Done when the disconfirming search is shown, with its result.
9. **Record the forecast so it can be scored later** (formula 3). Done when each probability has a date and a resolution condition.

## Formulas

**1. Expected value** (EI p.68): E = sum over scenarios of p_i x V_i, with the p_i summing to 1. Show the loss case next to the gain case: the size of being right matters more than how often (EI p.68; 30Y attribute 5).

**2. Updating** (JD p.9). P(H | evidence) = P(H) x L / [P(H) x L + (1 - P(H)) x (1 - L)], with L the reliability of the evidence. Source example (taxi problem): base rate 15 percent, witness 80 percent reliable, posterior about 41 percent (0.12 / 0.29), not 80. Shrinkage for extrapolated trends: estimate = base rate + c x (observed - base rate), c between 0 and 1, with the period-to-period correlation r as the proxy for c (JD p.6; formula 1 in `references/base-rates.md`). JD's example: a fund at 12 percent against a category average of 10 percent, c = 0.05, gives 10.1 percent.

**3. Brier score.** Brier = (forecast - outcome)^2, outcome 1 or 0. FC sums over the event and the non-event, on a 0 to 2 scale where a 50/50 guess scores 0.50; 55 percent on an event that happens scores 0.405 and 65 percent scores 0.245 (FC p.18). MI scores one side only, on a 0 to 1 scale: 80 percent rain scores 0.04 if it rains and 0.64 if not (MI pp.8-9). State which scale is used. Calibration: 70 percent forecasts come true about 70 percent of the time. Discrimination: high probabilities go to the events that happen.

## Rules

**1. Facts, opinions and expectations.**
- Facts can be disproved (a reported figure, a filed contract). Opinions cannot (a forecast, a rating, "management expects"). Mark them separately; when opinion outweighs fact, update toward the base rate (MI p.7).
- Expectations are what the price implies; fundamentals are what the analyst forecasts. Write the implied bar first. A variant perception is "a well-founded view that was meaningfully different from the market consensus" (EI p.61).
- Cash is a fact, profit is an opinion: reconcile earnings to cash flow (30Y attribute 1).
- Pseudo-diagnostic information looks causal but does not change the probability of the thesis (EPS dilution from an acquisition). Subtly diagnostic information does (the present value of synergies against the premium paid) (JD p.10). Ask whether an earnings change alters long-term cash flow or only an accounting line (ST p.10).

**2. Probabilities and scenarios.**
- Use granular integer percentages (70, 75, 80, even 71 or 72). Granular forecasts were more accurate, and forecasters who used 50 percent most were less accurate than average (FC p.7).
- Use numbers, not words. In 1951 "serious possibility" meant 80 percent to one analyst and 20 percent to another (FC p.7); "probable" was read as anything from 25 to 90 percent (MI pp.8-9).
- Scenario probabilities sum to 100 and include explicit downside scenarios (EI p.69).
- No default 25/50/25 or 30/40/30 split. Derive each weight from a reference class (growth, margin, M&A or turnaround outcomes), state it with a reason and a date, and let the weights be asymmetric when the evidence is (decisions-price-moves.md Part 3, item 2; JD p.6). Not in the sources: a table that converts a base rate into a scenario weight. The conversion is the analyst's judgment and is labelled so.
- Check scope: the probability of a hazard over 6 months should usually be materially higher than over 3 months. Regular forecasters gave 40 and 41 percent for the same event over the two windows; superforecasters gave 15 and 24 (FC p.16).
- Update by the right amount. Under-reaction comes from inattention, answering an easier question, and confirmation bias; over-reaction from weighting irrelevant information and from lack of commitment to a reasoned view (FC p.7).
- Several diverse estimates that agree at 75 percent justify a higher aggregate, because each carries unshared information (FC p.12). Not in the sources: a numeric extremizing factor.
- Use all the cases in a reference class weighted by similarity, not one recalled analogy (JD pp.5-8).

**3. Premortem** (MI pp.5-6). Assume the thesis has failed badly one year from now and write why. Prospective hindsight produced 25 percent more reasons, and more specific ones (Russo and Schoemaker, cited in MI). Steps: prepare; imagine the failure; list reasons independently; consolidate; revisit the plan; review the list periodically. When the base case is bearish, run it on the bullish outcome instead.

**4. Kill criteria.** Linchpin analysis (MI pp.6-7): (a) identify the main uncertain drivers; (b) state the working premise for each; (c) give the evidence and reasoning; (d) name the signposts that would make a premise unreliable; (e) name the events that could reverse the outcome. Each kill criterion has a driver, a threshold and a date. Dates come from the events calendar (next earnings), the estimates section (guidance) and filing dates. Not in the sources: a kill-criteria template or worked example; the driver, threshold and date form is this file's construction from FC p.13 and MI pp.6-7.

**5. Ranges.** People set ranges too narrow (EI p.68). Do not set a range narrower than the reference class without a stated reason, and include a decline case. Use frequencies from a reference class for sales and profit growth; frequencies need a stable system (EI p.69; 30Y attribute 5).

**6. Decision rules** (EI p.68).
- Use expected value, and compare the gain when right with the loss when wrong.
- A margin of safety means a substantial discount of price to expected value, which also absorbs turnover, costs and taxes. Not in the sources: a numeric size for it in these papers (see `references/downside-and-catalysts.md` for stated practices).
- Guard against overconfidence (table 1).
- Judge process, not outcome, where luck is large. A post-mortem separates the information available at the time, the quality of the analysis, and luck (OB).
- After a one-day move of 10 percent or more, classify the event and quote the base rate before explaining it; people invent a cause for any effect (OB; `references/after-a-price-move.md`).

**7. Stating a view.** In this order: (1) the implied bar from the price (derived); (2) the base rate for that bar (reported, historical); (3) the view as a probability with a date (judgment); (4) supporting facts and supporting opinions, listed separately; (5) disconfirming evidence from an explicit search, shown and weighed (30Y attribute 6; MI p.7): the bear case, filings that contradict management, research with the opposite view; (6) kill criteria with dates; (7) what would change the view and by how many probability points.

## Reference table

**Table 1. Evidence on overconfidence and the inside view** (historical findings; verify the period before quoting)

| Finding | Figure | Source and sample |
|---|---|---|
| Calibration test | Average confidence about 70 percent against just under 60 percent correct; answers at 100 percent confidence right 77 percent of the time; 82.7 percent of participants overconfident | RQ, 1,985 self-selected participants, May 2015 |
| Private equity deal forecasts | About 30 percent expected return for the focal deal against about 20 percent for two comparable deals recalled; over 80 percent revised down when shown the comparables | Base Rate Book 2016; JD pp.5-8 |
| M&A outcomes | About 60 percent of deals fail to create value for the acquirer | Sirower and Sahni, cited in JD p.5 and A |
| New businesses | About 50 percent survive 5 years or more, while over 80 percent of entrepreneurs rate their odds at 70 percent or higher | Base Rate Book 2016 |
| Executive confidence intervals | CFOs' 80 percent intervals for the stock market contained the outcome about one-third of the time | Base Rate Book 2016 |
| Analyst ranges | Consensus SD of 3-year sales growth 8 to 12 percent against 18 to 19 percent in history; net income 19 percent against 35 percent | Base Rate Book 2016 and Sales Growth v2, 2016 |
| Companies that shrink | 23 percent had negative 3-year real sales CAGR; 31 percent had lower net income after 3 years | Top 1,000 global companies, 1950-2015 |
| Forecasting tournaments | Superforecasters (top 2 percent of 2,800) about 30 percent more accurate than intelligence analysts; about 70 percent stayed in the top group the next year | FC pp.2-3, 2011-2015 |

## Interpretation and limits

- A probability is a reference-class result adjusted by judgment; label it judgment.
- Quote N, dispersion and sample dates with any base-rate average.
- Forecast skill decays beyond about one year (FC pp.13, 17). Black swans are unforecastable; model gray swans (extreme but modelable events) with distributions (FC pp.16-17).
- With no usable reference class, say so and widen the range. Do not default to 50 percent.
- A good outcome does not prove a good decision, and a bad one does not disprove it (OB).

## Output lines

- "Price-implied bar: X (derived). Base rate for this bar: Y percent of N cases, [sample and period] (reported, historical base rate)."
- "Scenarios: A at p1 percent, B at p2 percent, C at p3 percent; sum 100; weights from [reference class], adjusted for [reason] (judgment)."
- "Probability-weighted value: V; loss case L at p percent (derived from assumed weights)."
- "Facts: [list] (reported). Opinions: [list] (reported, as claims). Disconfirming evidence: [list], or none found after searches for [terms]."
- "Premortem: the thesis fails if [reason 1], [reason 2], [reason 3] (judgment)."
- "Kill criterion: if [driver] is below [threshold] by [date], the thesis fails (judgment; threshold assumed)."

## Sources

- Notes: decisions-price-moves.md (Part 1 sections 3 to 11, Parts 2 to 4); expectations-multiples-dcf.md (section 1.2, EI pp.68-69); base-rates.md (sections 1.1 to 1.4, 2.2, 2.4).
- Mauboussin and co-authors, Credit Suisse Global Financial Strategies: "Sharpening Your Forecasting Skills" (28 Sep 2015, "FC"); "Methods to Improve Decisions" (24 Feb 2014, "MI"); "Cultivating Your Judgment Skills" (7 May 2013, "JD"); "IQ versus RQ" (12 May 2015, "RQ"); "Outcome Bias and the Interpreter" (15 Oct 2013, "OB"); "Thirty Years: Ten Attributes of Great Investors" (4 Aug 2016, "30Y"); "A Long Look at Short-Termism" (18 Nov 2014, "ST"); The Base Rate Book (26 Sep 2016, "A").
- Mauboussin, "Expectations Investing", CFA Institute Conference Proceedings Quarterly, Sept 2006 ("EI").
