# Spec: Forecasting discipline

## 1. Purpose
This method answers: how to build probabilities, scenarios, kill criteria and a stated view so a portfolio manager can check each one. It covers attaching numbers to beliefs, separating facts, opinions and price-implied expectations, range width, decision rules, and presenting a view with the evidence that would disprove it. Jobs: thesis and variant perception, memo, scenario analysis, earnings preview and reaction, risk assessment. The output describes the balance of evidence and what would change it; it gives no Buy, Hold or Sell and no position size (the notes contain sizing material; excluded on purpose).
Evidence: Mauboussin papers (Credit Suisse unless stated): "Sharpening Your Forecasting Skills" (28 Sep 2015, "FC"), "Methods to Improve Decisions" (24 Feb 2014, "MI"), "Cultivating Your Judgment Skills" (7 May 2013, "JD"), "IQ versus RQ" (12 May 2015, "RQ"), "Outcome Bias and the Interpreter" (15 Oct 2013, "OB"), "Thirty Years: Ten Attributes of Great Investors" (4 Aug 2016, "30Y"), "A Long Look at Short-Termism" (18 Nov 2014, "ST"), and "Expectations Investing" (CFA Institute Conference Proceedings Quarterly, Sept 2006, "EI"). "Design choice" marks this spec's own implementation, not a paper.

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Facts: reported numbers, guidance, dated events | Tearsheet financials, estimates (actuals, guidance), filings, transcripts, events calendar | reported |
| Opinions: management claims, broker views, ratings, targets | Transcripts, broker research, analyst targets and ratings | reported (as a claim) |
| Expectations: what the price and consensus imply | expectations.md; tearsheet consensus estimates | derived |
| Base rates for reference-class weights | base-rates.md | reported (historical) |
| Probabilities, scenario weights, thresholds | The analyst or the skill | assumed or judgment |

## 3. Procedure
1. Write each question so it can be scored: checkable outcome, time window, relevance to the decision (FC p.13). Prefer horizons of months to one year; 3 to 5 year forecasts are close to unforecastable (FC pp.13, 17). For a long-horizon view, cluster small dated questions (FC pp.14-15). Done when each has an outcome, date and threshold.
2. Separate facts, opinions and expectations (4.1). Done when each evidence sentence is tagged.
3. Take the outside view first: reference class, base rate, then specifics (FC p.11; MI pp.3-4; base-rates.md). Done when the base rate, N and sample are quoted.
4. Build scenarios (4.2). Done when probabilities sum to 100 percent and each has a reason and a reference-class number.
5. Run a premortem (4.3). Done when at least three failure reasons (design choice) are written, each mapped to a driver or kill criterion.
6. Write kill criteria (4.4). Done when each has a driver, a threshold and a date.
7. Compute expected value and range (4.5); apply the decision rules (4.6).
8. State the view with its disconfirming evidence (4.7).
9. Record the forecast so it can be scored (4.8).

## 4. Method

### 4.1 Facts, opinions and expectations
- Facts can be disproved (a reported figure, a filed contract). Opinions cannot (a forecast, a rating, "management expects"). Mark them separately; when opinion outweighs fact, update toward the base rate (MI p.7).
- Expectations are what the price implies; fundamentals are what the analyst forecasts. Write the implied bar first. A variant perception is "a well-founded view that was meaningfully different from the market consensus" (EI p.61).
- Cash is a fact, profit is an opinion (30Y). Reconcile earnings to cash flow.
- Information is pseudo-diagnostic if it looks causal but does not change the probability of the thesis (EPS dilution from an acquisition) and subtly diagnostic if it does (present value of synergies against the premium) (JD p.10). Ask whether an earnings change alters long-term cash flow or only an accounting line (ST p.10).

### 4.2 Probabilities and scenarios
- Use granular integer percentages (70, 75, 80, even 71 or 72); granular forecasts were more accurate, and forecasters who used 50 percent most were less accurate than average (FC p.7).
- Scenario probabilities must sum to 100 percent (EI p.69). Include explicit downside scenarios.
- No default 25/50/25 or 30/40/30. Derive each weight from a reference class (growth, margin, M&A or turnaround outcomes), state it with a reason and a date, and let weights be asymmetric when the evidence is (decisions-price-moves.md Part 3, item 2; JD p.6). GAP: the notes give no table that converts a base rate into a scenario weight; the conversion is the analyst's judgment and is labelled as such.
- Shrink extrapolated trends toward the base rate (formula in base-rates.md; JD p.6).
- Use numbers, not words: in 1951 "serious possibility" meant 80 percent to one analyst and 20 to another (FC p.7).
- Scope sensitivity: a hazard probability over 6 months should usually exceed that over 3 months (regular forecasters gave 40 and 41 percent; superforecasters 15 and 24; FC p.16).
- Update by the right amount. Under-reaction comes from inattention, answering an easier question and confirmation bias; over-reaction from weighting irrelevant information and lack of commitment to a reasoned view (FC p.7). Bayes check (JD p.9): P(H | evidence) = P(H) x L / [P(H) x L + (1 - P(H)) x (1 - L)], L the reliability of the evidence. Source cab example: base rate 15 percent, reliability 80 percent gives 41 percent, not 80.
- Diverse estimates that agree at 75 percent justify a higher aggregate because each carries unshared information (FC p.12). GAP: no extremizing factor in the notes.

### 4.3 Premortem (MI pp.5-6)
Assume the thesis has failed one year from now and write why; prospective hindsight produced 25 percent more reasons, more specific (Russo and Schoemaker). Steps: prepare; imagine the failure; list reasons independently; consolidate; revisit the plan; review the list periodically. Run it on the bullish case when the base case is bearish.

### 4.4 Kill criteria with dates
Linchpin analysis (MI pp.6-7): (1) identify the main uncertain drivers; (2) state the working premise for each; (3) give evidence and reasoning; (4) name signposts that would make a premise unreliable; (5) name events that could reverse the outcome. Each kill criterion has a driver, a threshold and a date. Dated checks: next earnings date (events calendar), guidance (estimates), filing dates. GAP: the notes give no kill-criteria template or example; the driver, threshold and date form is this spec's design choice built from FC p.13 and MI pp.6-7.

### 4.5 Expected value and range
- Expected value = sum of p_i x V_i over scenarios, sum of p_i = 1 (EI p.68).
- Overconfidence: investors project ranges that are too narrow (EI p.68). Of 1,985 participants (self-selected), average confidence was about 70 percent against just under 60 percent correct; answers at 100 percent confidence were right 77 percent of the time (RQ). Consensus SD of 3-year sales growth is 8 to 12 percent against 18 to 19 percent in history (base-rates.md). Do not set a range narrower than the reference class without a stated reason; include a decline case.
- Use frequency from a reference class for sales and profit growth; frequency needs stationarity (EI p.69; 30Y).

### 4.6 Decision rules (EI p.68)
1. Use expected value. The magnitude of being right matters more than the frequency (EI p.68); compare the gain when right with the loss when wrong (30Y).
2. Require a margin of safety: a substantial discount of price to expected value, which also absorbs turnover, costs and taxes. GAP: the three notes give no numeric size.
3. Guard against overconfidence (4.5).
4. Judge process, not outcome, where luck is large (OB). A post-mortem separates information available then, quality of analysis, and luck.
5. After a 10 percent or more one-day move, classify the event and quote the base rate before explaining it; people invent a cause for any effect (OB; decisions-price-moves.md Part 1, sections 1 and 2).

### 4.7 Stating a view with disconfirming evidence
Order: (1) implied bar from the price (derived); (2) base rate for that bar (reported, historical); (3) the view as a probability range with a date (judgment); (4) supporting facts and supporting opinions, listed separately; (5) disconfirming evidence from an explicit search, shown and weighed (30Y attribute 6; MI p.7), for example the bear case, filings that contradict management, broker research with the opposite rating; (6) kill criteria with dates; (7) what would change the view and the update size in probability points.

### 4.8 Scoring
Brier score = (forecast - outcome)^2. FC sums over event and non-event, scale 0 to 2, 0.50 for a 50/50 guess (55 percent on an event that happens scores 0.405; 65 percent scores 0.245). MI is single-sided, scale 0 to 1 (80 percent rain: 0.04 if it rains, 0.64 if not). State the scale. Calibration: 70 percent forecasts come true about 70 percent of the time. Discrimination: high probabilities go to events that happen. Keep a decision journal (date, expectation, reasons, probabilities).

## 5. Interpretation rules
- A probability is a reference-class result adjusted by judgment; label it judgment.
- Do not rely on one recalled analogy; use all cases and weight by similarity (JD pp.5-8).
- Quote N, dispersion and sample dates with any base-rate average.
- Forecast skill decays beyond about one year (FC pp.13, 17). Black swans are unforecastable; model gray swans with distributions (FC pp.16-17).
- With no reference class, say so and widen the range; do not default to 50 percent.

## 6. Output lines
- "Price-implied bar: X (derived). Reference-class base rate for this bar: Y percent, N cases, sample (reported, historical)."
- "Scenarios: A at p1 percent, B at p2 percent, C at p3 percent; sum 100 percent; weights from [class] (judgment)."
- "Probability-weighted value: V (derived from assumed weights)."
- "Facts: [list] (reported). Opinions: [list] (reported as claims). Disconfirming evidence: [list], or none found after searches for [terms]."
- "Kill criterion: if [driver] is below [threshold] by [date], the thesis fails (judgment)."

## 7. Sources
Notes: decisions-price-moves.md (Part 1 sections 3 to 11, Parts 2 and 3); expectations-multiples-dcf.md (section 1.2, EI pp.68-69); base-rates.md (sections 1.1 to 1.4). Papers as in section 1.
