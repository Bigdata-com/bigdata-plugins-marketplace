---
name: bigdata-thesis
description: >-
  Investment thesis: where the view differs from consensus, evidence for and against, bull and
  bear case, catalysts, kill criteria. Use for a thesis, variant view, bull and bear case,
  stress-test my idea. Not a full report: bigdata-deep-dive.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, valuation, base-rates, forecasting-discipline, downside-and-catalysts, industry-structure
  bigdata-sector-primer: auto
---

# Thesis

This skill writes a thesis the way a professional reader wants to test one: first what the price already implies, measured without judgment; then the two to four claims where the evidence points away from consensus, each written so it can be proved or disproved by a date; the evidence for and against each claim with its source, facts kept apart from opinions; why the gap exists and who is on the other side; the loss case before the upside; the catalyst path; a premortem; and kill criteria with dates, written now so they cannot drift later. A variant view is "a well-founded view that was meaningfully different from the market consensus" (Steinhardt, quoted in Mauboussin, Expectations Investing). Agreeing with consensus more enthusiastically is not one, and when the evidence supports no claim that differs, the thesis says so. It gives no buy or sell call.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-thesis"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Establish whose thesis it is. If the user brings an idea to stress-test, their claims are the claims: write each in the template, test it, and do not swap in new ones (add a claim only if the evidence turns up one that matters more, and say so). If the user asks for a thesis or a variant view with no idea of their own, the claims come from the analysis. An investor-relations or strategy team asking "what is the bull and the bear case on us" is a valid request: run the same method and write the implications for that reader (which claims the market is weighing, what evidence would move it); still give no call. Note the direction the user leans, long or short, because the premortem runs against it. The default horizon is twelve months, because forecast skill decays beyond about a year; a longer view is broken into dated questions inside that window.

Ask one question only when the answer changes the work: the user asks to stress-test their idea without stating it (ask for it in one or two sentences), or the name resolves to more than one listing. Otherwise state the horizon and the direction under the header and proceed. Done when the company is resolved, the claims' owner (the user's or the analysis) is settled, and the reader, horizon and direction are stated.

If the company is Private, say there is no price to read expectations from, and offer `bigdata-deep-dive`, which runs on private companies with the price-based sections left out.

## Gather

Work through these in order. Each step says what it must produce.

1. **Tearsheet, in four calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, analyst_ratings, earnings_calendar`; then `financial_statements, financial_ratios, key_metrics` with `interval` annual; then `analyst_estimates`; then `revenue_segmentation, fund_trends_history`. Done when EV and its inputs, five annual periods of statements, consensus to four years out with vintage and estimate counts, targets and rating counts, the next report date, segments, and the 13F position changes (quarterly and filed with a lag; label them so) are in hand.
2. **Revisions.** The tearsheet carries no history of consensus or targets. Search research and news for the last 30 and 90 days for reports that quote estimate or target changes; take the figure and the document's date, and label it "press or research summary". Done when each revision figure has a dated source, or is marked not found.
3. **The last two earnings calls.** `bigdata_search` in fast mode with the reporting period filter, then `bigdata_fetch_document` on each. Done when guidance, management's claims about the drivers (recorded as opinions) and the questions analysts kept pressing are listed with the call dates.
4. **The latest annual filing.** Search and fetch. Done when the risk factors that changed from the prior year, segment economics, contingent liabilities, the pension position, related-party items and covenants are noted with page or section, or marked absent.
5. **The debate.** Three to five `bigdata_search` calls, one aspect each: the bull arguments in research and news, the bear arguments, the reasons behind the highest and lowest targets, the controversy in the last twelve months, and insider purchases or sales. Done when the consensus narrative and the main dissent are each stated with dated sources.
6. **Evidence per driver.** One search per driver the claims will rest on (pricing, volumes, share, customers, capacity, regulation), each in a single period. Done when every candidate claim has at least one dated fact, or is marked as having none.
7. **Industry evidence, when a claim concerns the durability of returns.** The searches in the evidence table of `references/industry-structure.md` for steps 3 to 7. Done when each of those has evidence or a stated gap.
8. **Dated events.** `bigdata_events_calendar` for earnings dates and conferences over the horizon, plus searches of filings and news for regulatory, contract, product and deal dates, which the calendar does not carry. Done when each claim has at least one dated event that would test it.
9. **Sentiment.** `bigdata_sentiment_tearsheet` (it takes no window; say which period its narrative covers). Done when the direction of media sentiment and the stories driving it are known. Short interest and option prices are not in Bigdata.com; say so in Gaps when positioning matters.
10. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the value-driver, metrics and accounting-traps subsections, so the claims are about the drivers the sector turns on. Done when those are noted, or no primer applies.

## Analyse

Each step names the reference file it loads and ends in what it must produce.

1. **What the price implies, first.** `references/expectations.md` steps 1 to 6, with the cost of capital from `references/valuation.md` step 3 (assumed, with a range of plus and minus 1 point). Measure the height of the bar without judging it, then place the implied growth in its size and horizon class with `references/base-rates.md`. Done when the report can say "the price needs X percent NOPAT growth at Y percent ROIIC for Z years, which A percent of companies in the B to C size class achieved", every input labelled.

2. **Write down consensus.** The consensus for sales, margin, EPS and free cash flow for the next two fiscal years, with vintage, counts and the revisions found in Gather step 2; the target range and rating counts; and the consensus narrative from Gather step 5. Consensus is opinion and is labelled so. Done when the consensus table exists before any claim is written; a variant view cannot differ from a consensus that has not been written down.

3. **Find the candidate claims.** Use the value-trigger rule in `references/expectations.md` formula 4, classified on the three-year rolling ROIIC (labelled; a single year is never evidence, and a high reading can be operating leverage), to decide which driver can move value. Run its "if, then" test on that driver. Where a claim concerns how long excess returns last, test it with `references/industry-structure.md` steps 4 to 7 and 10, bounded by the sector persistence in `references/base-rates.md` table 9; quote the market-implied period of about 8 years (1976 to 2007, historical, not current) as a comparison only. Keep a claim only if its effect on value per share is large enough to matter, and state the effect. Done when two to four candidate claims each name a driver, a direction against consensus and a value effect, or the step finds none.

4. **Write each claim in the template.** Each claim is a scorable question (`references/forecasting-discipline.md` step 1): a checkable outcome, a window, and a threshold. The template, kept from the variant-perception work:
   - **Claim:** "Consensus models [X] for [metric] in [period]; the evidence points to [Y] because [mechanism], which would mean [Z] of value per share against the [W] embedded in the price."
   - **What consensus assumes:** the figure, its vintage and source.
   - **Evidence for** and **evidence against:** each item dated, sourced, and tagged fact, opinion or expectation.
   - **What proves it:** the observable, the threshold and the date.
   - **What kills it:** the observable, the threshold and the date.
   - **By when:** the window in which the claim resolves.
   Done when every claim fills every line, or the missing line is named as a gap.

5. **Take the outside view on each claim.** `references/base-rates.md` steps 2 to 4 and 6: the reference class, its N, sample and period, where the claim sits in the distribution, and the shrinkage toward the class (formula 1). Claim an exception only with a specific, evidenced reason. Done when each claim carries its base-rate sentence.

6. **Weigh the evidence.** `references/forecasting-discipline.md` rules 1 and 7: tag every item fact, opinion or expectation, search for disconfirming evidence by name, and separate diagnostic from pseudo-diagnostic evidence. Done when each claim shows the disconfirming searches run and what they found, and opinions are not counted as facts.

7. **Put a probability on each claim.** `references/forecasting-discipline.md` rule 2: a granular integer percentage with the date it applies to, anchored on the reference class from step 5 and adjusted for the evidence from step 6, labelled judgment. Done when each claim has its probability, anchor and date.

8. **Explain why the gap exists.** `references/downside-and-catalysts.md` steps 4 and 5, with the quarterly 13F changes as the holder evidence. For a short idea, ask who is forced to buy. A gap with no structural reason is a warning that the claim may be wrong, and the thesis says so. Done when the reason is named with evidence, or its absence is stated.

9. **The downside before the upside.** `references/downside-and-catalysts.md` steps 1 to 3, with the substitutes in its rule 5 where the floors do not apply (software and services, banks and insurers). Done when the loss case per share is stated before any upside figure.

10. **Lay out the catalyst path.** `references/downside-and-catalysts.md` steps 7 and 8 with tables 2 and 3, each catalyst tied to the claim it tests. Done when every claim is tested by at least one dated event, and the no-catalyst outcome is stated.

11. **Cases and expected value.** `references/forecasting-discipline.md` steps 4 and 7: the thesis case, the consensus case and the downside case. For each, solve the value-driver formula forward (`references/expectations.md` formula 2) at the case's growth and ROIIC to get EV, then bridge EV to equity per share item by item as `references/valuation.md` step 10 sets out: net debt, minorities, the after-tax pension deficit, leases where the cash flows were lease-adjusted, and options and RSUs, with the share count from filings. Integer probabilities sum to 100, with weights from the reference class, not a default split. Show the loss case next to the gain case. Done when the bridge is shown once, and the expected value per share sits next to the price with the source of each weight. For full cases run through a model, hand off to `bigdata-scenarios`.

12. **Run the premortem.** `references/forecasting-discipline.md` rule 3: assume the thesis failed badly a year from now and write at least three reasons, each mapped to a claim or a kill criterion. If the user leans short, or the thesis is bearish, run it on the bullish outcome instead. Done when the reasons are listed and mapped.

13. **Write the kill criteria now.** `references/forecasting-discipline.md` rule 4 and table 4 in `references/downside-and-catalysts.md`, for each claim and for the thesis as a whole, with dates from the calendar, guidance and filings. A price fall alone is not a kill criterion; it is a prompt to re-test value. Done when every kill criterion has a driver, a checkable threshold and a date, and the date it was written is stated.

If no claim survives steps 3 to 7, the honest output is that there is no variant view on this name now: state what the price implies, the consensus, what the evidence shows, and what would have to change for a view to form. A manufactured disagreement is worse than none.

## Write

Follow `references/output-standard.md`. The report has these sections in this order. The downside comes before the claims, because the claims carry value effects and the loss case has to be read first.

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
| Metric | FY1 | FY2 | 30d / 90d revision | Estimates (n) | Vintage | Basis | Source |
Revisions are press or research summaries, or "not found". Target range and rating counts. The
consensus narrative in two sentences, labelled opinion.

## Downside first
| Floor | Per share | Price as percent of floor | Basis | Source |
Permanent-loss conditions, each present, absent or unknown. Loss case per share.

## The claims
One block per claim, in the template from Analyse step 4, then:
| Evidence | For or against | Fact, opinion or expectation | Date | Source |
Base-rate sentence. Probability with its anchor and date.

## Why the gap exists
The reason, the seller or buyer on the other side, the quarterly holder changes.

## Catalyst path
| Date or window | Event | Claim tested | Decider | Potency and why | Source |
What happens if nothing happens.

## Cases and expected value
| Case | What has to be true | EV | Value per share | Probability | Weight anchor | Basis |
The equity bridge once, item by item. Expected value; loss case next to gain case.

## Premortem
Three or more reasons, each mapped to a claim or kill criterion.

## Kill criteria
Written <date>.
| Driver | Threshold | Date | Where it will be observed |

## What would change this reading
Two to five observable conditions, dated, each with the probability change it would cause.

## Gaps
What Bigdata.com could not answer, the assumptions that drive the value, and positioning data.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Every table with figures carries a Basis column (reported, derived, assumed or judgment) and a Source column, or one "Basis and sources" note under the table where the columns would pass eight.
Length: four to eight pages. Offer a Word document when the host can create files. For a narrow question ("what is the market missing?"), answer with what the price implies, the consensus line and the one or two claims in the template, with sources and the footer.

## Checks before sending

1. What the price implies, the consensus table and the downside all come before the first claim.
2. Every claim fills the template: claim, what consensus assumes, evidence for and against with sources, what proves it, what kills it, by when.
3. Each claim has a base-rate sentence with N, sample and period, and a probability with its anchor and date.
4. Facts, opinions and expectations are tagged separately, and the disconfirming searches are shown with their results.
5. The reason the gap exists is named, or its absence is flagged as a warning.
6. Value per share comes through the equity bridge, not EV divided by shares.
7. Every claim is tested by a dated catalyst, and the no-catalyst outcome is stated.
8. Case probabilities are integers that sum to 100 with weights from a reference class.
9. The premortem has at least three reasons mapped to claims or kill criteria, and every kill criterion has a driver, a threshold and a date; none is a price level alone.
10. Revisions carry a dated source or "not found"; ROIIC is three-year rolling and labelled.
11. No buy, hold, sell, rating, target price or position size anywhere. When no claim survives, the report says there is no variant view.

## Hand-offs

- The user wants the full initiation report: `bigdata-deep-dive`. The valuation range behind the cases: `bigdata-valuation`. The cases with signposts in full: `bigdata-scenarios`. What could go wrong, in depth: `bigdata-risk`. The dated events alone: `bigdata-catalysts`.
- After delivering, make one offer: a Bigdata.com monitor on the kill criteria and catalysts, so the user hears when one is hit. If the user wants the claims scored later, add a forecast record with it (`references/forecasting-discipline.md` step 9: each probability, its date and resolution condition, and the Brier scale named). Act only on a clear yes.
