---
name: bigdata-thesis
description: >-
  An investment thesis as testable claims from Bigdata.com data: where the view differs from
  consensus and why, the evidence for and against each claim, what the price already implies, the
  catalysts that would prove it, and the kill criteria with dates. Use when the user asks for a
  thesis, a variant view, the bull and bear case, what the market is missing, or to stress-test
  their idea. Not for a full initiation report, which bigdata-deep-dive covers.metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, forecasting-discipline, downside-and-catalysts, industry-structure
  bigdata-sector-primer: auto
---

# Thesis

This skill writes a thesis the way a portfolio manager wants to read one before committing capital: first what the price already implies, measured without judgment; then the two to four claims where the evidence points away from consensus, each written so it can be proved or disproved by a date; the evidence for and against each claim with its source, facts kept apart from opinions; why the gap exists and who is on the other side; the loss case before the upside; the catalyst path; a premortem; and kill criteria with dates, written now so they cannot drift later. A variant view is "a well-founded view that was meaningfully different from the market consensus" (Steinhardt, quoted in Mauboussin, Expectations Investing). Agreeing with consensus more enthusiastically is not one, and when the evidence supports no claim that differs, the thesis says so. It gives no buy or sell call.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-thesis"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Establish whose thesis it is. If the user brings an idea to stress-test, their claims are the claims: write each in the template, test it, and do not swap in new ones (add a claim only if the evidence turns up one that matters more, and say so). If the user asks for a thesis or a variant view with no idea of their own, the claims come from the analysis. Note the direction the user leans, long or short, because the premortem runs against it. The default horizon is twelve months, because forecast skill decays beyond about a year; a longer view is broken into dated questions inside that window.

Ask one question only when the answer changes the work: the user asks to stress-test their idea without stating it (ask for it in one or two sentences), or the name resolves to more than one listing. Otherwise state the horizon and the direction under the header and proceed.

If the company is Private, say there is no price to read expectations from, and offer `bigdata-deep-dive` or a document-based profile through `bigdata` instead.

## Gather

Work through these in order. Each step says what it must produce.

1. **Tearsheet, in several calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, events_calendar`; then `fundamentals, estimates`; then `revenue_segmentation, company_funds_holders, fund_trends_history`. Done when EV and its inputs, five periods of statements, consensus to four years out with vintage, estimate counts and 30 and 90-day revisions, targets and rating counts, the next report date, segments, and the 13F holders now and a year ago are in hand.
2. **The last two earnings calls.** `bigdata_search` in fast mode with the reporting period filter, then `bigdata_fetch_document` on each. Done when guidance, management's claims about the drivers (recorded as opinions) and the questions analysts kept pressing are listed with the call dates.
3. **The latest annual filing.** Search and fetch. Done when the risk factors that changed from the prior year, segment economics, contingent liabilities, the pension position, related-party items and covenants are noted with page or section, or marked absent.
4. **The debate.** Three to five `bigdata_search` calls, one aspect each: the bull arguments in research and news, the bear arguments, the reasons behind the highest and lowest targets, the controversy in the last twelve months, and insider purchases or sales. Done when the consensus narrative and the main dissent are each stated with dated sources.
5. **Evidence per driver.** One search per driver the claims will rest on (pricing, volumes, share, customers, capacity, regulation), each in a single period. Done when every candidate claim has at least one dated fact, or is marked as having none.
6. **Industry evidence, when a claim concerns the durability of returns.** Searches for market shares and their stability, pricing in the industry, and entrants and exits, as the evidence table in `references/industry-structure.md` lists. Done when each of those has evidence or a stated gap.
7. **Dated events.** `bigdata_events_calendar` for the company's events over the horizon, plus searches for regulatory, contract, product and deal dates. Done when each claim has at least one dated event that would test it.
8. **Sentiment.** `bigdata_sentiment_tearsheet` for 90 days. Done when the direction of media sentiment and the stories driving it are known. Short interest and options are not in Bigdata.com; say so in Gaps when positioning matters.
9. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read it before analysing, so the claims are about the drivers the sector turns on.

## Analyse

Each step names the reference file it loads and ends in what it must produce.

1. **What the price implies, first.** Load `references/expectations.md` and run steps 1 to 6: EV, NOPAT1 from consensus, the implied perpetual growth at a stated ROIIC and cost of capital (assumed, with a range of plus and minus 1 point), the implied competitive advantage period, the steady-state share of EV, and the forward P/E against 1 / cost of equity. Measure the height of the bar without judging it. Then place the implied growth in its size and horizon class with `references/base-rates.md`. Done when the report can say "the price needs X percent NOPAT growth at Y percent ROIIC for Z years, which A percent of companies in the B to C size class achieved", every input labelled.

2. **Write down consensus.** The consensus for sales, margin, EPS and free cash flow for the next two fiscal years, with vintage, counts and revisions; the target range and rating counts; and the consensus narrative from Gather step 4. Consensus is opinion and is labelled so. Done when the consensus table exists before any claim is written; a variant view cannot differ from a consensus that has not been written down.

3. **Find the candidate claims.** Use the value-trigger rule in `references/expectations.md` formula 4 to decide which driver can move value: incremental return where ROIIC is near the cost of capital, sales growth where it is well above, and growth as a destroyer where it is below. Run the "if, then" test on that driver (consensus 2 points either way, carried through margin and investment), remembering that analysts consistently underestimate how sales changes reach margins. Where a claim concerns how long excess returns last, test it with `references/industry-structure.md` steps 4 to 7 and 10 (share stability, pricing power, rivalry, entry and exit, the source of advantage against the margin and turnover signature), bounded by the market-implied period of about 8 years (1976 to 2007, verify) and the sector persistence in `references/base-rates.md`. Keep a claim only if its effect on value per share is large enough to matter, and state the effect. Done when two to four candidate claims each name a driver, a direction against consensus and a value effect, or the step finds none.

4. **Write each claim in the template.** Each claim is a scorable question (`references/forecasting-discipline.md` step 1): a checkable outcome, a window, and a threshold. The template, kept from the variant-perception work:
   - **Claim:** "Consensus models [X] for [metric] in [period]; the evidence points to [Y] because [mechanism], which would mean [Z] of value per share against the [W] embedded in the price."
   - **What consensus assumes:** the figure, its vintage and source.
   - **Evidence for** and **evidence against:** each item dated, sourced, and tagged fact, opinion or expectation.
   - **What proves it:** the observable, the threshold and the date.
   - **What kills it:** the observable, the threshold and the date.
   - **By when:** the window in which the claim resolves.
   Done when every claim fills every line, or the missing line is named as a gap.

5. **Take the outside view on each claim.** From `references/base-rates.md` steps 2 to 4 and 6: the reference class, its N, sample and period, and where the claim sits in the distribution. Claim an exception only with a specific, evidenced reason, never one analogy. Shrink an extrapolated trend toward the class with the persistence r (estimate = base rate + r x (observed - base rate)). Done when each claim carries its base-rate sentence.

6. **Weigh the evidence.** From `references/forecasting-discipline.md` rules 1 and 7. Tag every item fact (can be disproved: a reported figure, a filed contract), opinion (cannot: a forecast, a rating, "management expects"), or expectation (what the price implies). Search for disconfirming evidence by name: the bear case, filings that contradict management, research with the opposite view. Separate diagnostic evidence, which changes the probability of the claim, from pseudo-diagnostic evidence, which only looks causal, such as an EPS headline that leaves long-term cash flow unchanged. Done when each claim shows the disconfirming searches run and what they found, and opinions are not counted as facts.

7. **Put a probability on each claim.** From `references/forecasting-discipline.md` rule 2: a granular integer percentage with the date it applies to, anchored on the reference class from step 5 and adjusted for the evidence from step 6, labelled judgment. Use numbers, never words such as "likely". Done when each claim has its probability, anchor and date.

8. **Explain why the gap exists.** From `references/downside-and-catalysts.md` steps 4 and 5: ask what is wrong with it, test each candidate reason, and check who is on the other side: index deletions, mandate or minimum-price rules, a downgrade, spin-off selling, a dividend cut, no coverage, dumping after a miss; compare 13F holders now with a year ago. For a short idea, ask who is forced to buy. A gap with no structural reason is a warning that the claim may be wrong, and the thesis says so. Done when the reason is named with evidence, or its absence is stated.

9. **The downside before the upside.** From `references/downside-and-catalysts.md` steps 1 to 3: what must go right for the price to hold; the floors per share (net-net working capital, tangible book, a liquidation value with the haircuts stated as assumed, a stressed cash-flow value with capex equal to depreciation); and the events that would turn a temporary fall into a permanent loss (a capital raise, forced selling, a covenant breach, loss of market access), each marked present, absent or unknown. Where floors do not apply, as for software and services, use the stressed cash-flow value and cash runway; for banks and insurers test book value and earnings quality instead. Done when the loss case per share is stated before any upside figure.

10. **Lay out the catalyst path.** From `references/downside-and-catalysts.md` step 7 and tables 2 and 3: each catalyst with its type, who decides it, its date or window, the claim it tests, and its potency on certainty, timing, the share of the gap it closes and whether the decider gains from closing it. Then step 8: what happens if nothing happens, since without a catalyst value can erode or the gap can widen. Done when every claim is tested by at least one dated event, and the no-catalyst outcome is stated.

11. **Cases and expected value.** From `references/forecasting-discipline.md` steps 4 and 7: the thesis case, the consensus case and the downside case, each with a value per share from the value-driver arithmetic in `references/expectations.md` (formula 2 solved forward at the case's growth and ROIIC), and integer probabilities that sum to 100 with weights from the reference class, never a default split. Show the loss case next to the gain case. Done when the expected value sits next to the price with the source of each weight. For full cases run through a model, hand off to `bigdata-scenarios`.

12. **Run the premortem.** From `references/forecasting-discipline.md` rule 3: assume the thesis failed badly a year from now and write at least three reasons, each mapped to a claim or a kill criterion. If the user leans short, or the thesis is bearish, run it on the bullish outcome instead. Done when the reasons are listed and mapped.

13. **Write the kill criteria now.** From `references/forecasting-discipline.md` rule 4 and table 4 in `references/downside-and-catalysts.md`: for each claim and for the thesis as a whole, a driver, a checkable threshold and a date, drawn from the events calendar, guidance and filing dates. Include the standard conditions: conservative value falls below the price, management or accounting proves unreliable, funding or covenant stress, a catalyst that has not occurred by its date. A price fall alone is not a kill criterion; it is a prompt to re-test value. Done when every kill criterion is observable and dated, and the date it was written is stated.

14. **Record the forecasts.** From `references/forecasting-discipline.md` step 9: list each probability with its date and resolution condition so the thesis can be scored later, and say which Brier scale is meant. Done when the record table exists.

If no claim survives steps 3 to 7, the honest output is that there is no variant view on this name now: state what the price implies, the consensus, what the evidence shows, and what would have to change for a view to form. A manufactured disagreement is worse than none.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) thesis, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.
Horizon: <months>. Direction tested: <long or short, or none>.

## The thesis
Four to eight sentences: what the price implies, where the evidence differs from consensus and on
which driver, how strong the evidence is, the loss case, the next date that tests the thesis and
the first kill criterion. No rating.

## What the price implies
| Measure | Value | Basis | Source |
The value trigger in one line, with its reason.

## Consensus
| Metric | FY1 | FY2 | 30d / 90d revision | Estimates (n) | Vintage | Source |
Target range and rating counts. The consensus narrative in two sentences, labelled opinion.

## The claims
One block per claim, in the template from Analyse step 4, then:
| Evidence | For or against | Fact, opinion or expectation | Date | Source |
Base-rate sentence. Probability with its anchor and date.

## Why the gap exists
The reason, the seller or buyer on the other side, the holder changes.

## Downside first
| Floor | Per share | Price as percent of floor | Basis | Source |
Permanent-loss conditions, each present, absent or unknown. Loss case per share.

## Catalyst path
| Date or window | Event | Claim tested | Decider | Potency and why | Source |
What happens if nothing happens.

## Cases and expected value
| Case | What has to be true | Value per share | Probability | Weight anchor | Basis |
Expected value; loss case next to gain case.

## Premortem
Three or more reasons, each mapped to a claim or kill criterion.

## Kill criteria
Written <date>.
| Driver | Threshold | Date | Where it will be observed |

## Forecast record
| Question | Probability | Date | Resolves when |

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: four to eight pages. Offer a Word document when the host can create files. For a narrow question ("what is the market missing?"), answer with what the price implies, the consensus line and the one or two claims in the template, with sources and the footer.

## Checks before sending

1. What the price implies and the consensus table both come before the first claim.
2. Every claim fills the template: claim, what consensus assumes, evidence for and against with sources, what proves it, what kills it, by when.
3. Each claim has a base-rate sentence with N, sample and period, and a probability with its anchor and date.
4. Facts, opinions and expectations are tagged separately, and the disconfirming searches are shown with their results.
5. The reason the gap exists is named, or its absence is flagged as a warning.
6. The loss case and the floors appear before any upside value.
7. Every claim is tested by a dated catalyst, and the no-catalyst outcome is stated.
8. Case probabilities are integers that sum to 100 with weights from a reference class.
9. The premortem has at least three reasons mapped to claims or kill criteria.
10. Every kill criterion has a driver, a threshold and a date; none is a price level alone.
11. No buy, hold, sell, rating, target price or position size anywhere. When no claim survives, the report says there is no variant view.

## Hand-offs

- The user wants the full initiation report: `bigdata-deep-dive`. The valuation range behind the cases: `bigdata-valuation`. The cases with signposts in full: `bigdata-scenarios`. What could go wrong, in depth: `bigdata-risk`. The dated events alone: `bigdata-catalysts`.
- After delivering, make one offer: a Bigdata.com monitor on the kill criteria and catalysts, so the user hears when one is hit. Act only on a clear yes.
