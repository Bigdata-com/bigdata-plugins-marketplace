---
name: bigdata-earnings-review
description: >-
  After a company reports, from Bigdata.com results, the transcript, estimates and reactions:
  results against consensus and guidance, what changed in the long-term outlook, new guidance
  against old, the thesis check, estimate and valuation refresh, quality signals, the market
  reaction, and the next date. Use when the user asks how a company did, to analyse its earnings,
  whether it beat or missed, or whether the quarter changes the thesis. Not for the setup before
  the report, which bigdata-earnings-preview covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, after-a-price-move, earnings-quality, forecasting-discipline, base-rates
  bigdata-sector-primer: auto
---

# Earnings review

This skill writes what a portfolio manager wants the morning after a print: the numbers against consensus and against what management promised, the guidance before and after, whether the quarter changed the company's long-term outlook or only the quarter, whether the thesis still holds and on what evidence, what the estimates and the valuation look like now, whether the beat or miss was made of cash or of accounting, how the stock reacted against the base rates for post-earnings moves, and the next date that matters. It sizes to the question. "Did Nike beat?" gets the results table and the guidance line. "Give me a reaction note" gets the short form, one to two pages. "Analyse Nike's quarter" gets the full review. It gives no rating and no action.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not. Stop there: give no view, drivers, risks, figures or dates from memory while the tools are missing, and do not fall back to web search.
- Pass `plugin_slug: "bigdata-earnings-review"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call. It explains which call carries which quarter's guidance and how estimates carry actuals, surprise and guidance.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the quarter needs it.

## Scope the request

Establish four things before gathering data. The company, resolved with `find_securities`. The quarter: the latest reported one unless the user names another, confirmed from `latest_earnings` and the events calendar. The form: a reaction note when the user asks for a reaction, "how should I read this", or "does it change the thesis" in a sentence; the full review otherwise. The thesis: if the user states one (a long or short case, a driver they own the stock for, kill criteria they wrote), the thesis check tests it; if not, test the prevailing bull case and bear case, built from the preview-period research and the last call, and label them as the Street's cases rather than the user's.

Ask one question only if the answer changes the work: the user refers to "my thesis" without stating it, or the name resolves to more than one listing. Otherwise state the assumptions in the header and proceed.

If the company has not reported the quarter yet, say so and hand off to `bigdata-earnings-preview`. If the transcript is not yet in Bigdata.com, write from the release and say the call will be added when it is available.

## Gather

1. **Tearsheet, in two calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, latest_earnings, analyst_estimates, earnings_calendar, analyst_ratings` first, then `financial_statements, financial_ratios, key_metrics, revenue_segmentation`. Done when the actuals, consensus and surprise for the quarter and the last eight quarters, the company's guidance fields, consensus for the next quarter and for FY+1 to the furthest year given with the estimate vintage, the price moves around the report date, targets and rating counts, five fiscal periods of statements, and the next report date are in hand.
2. **The release and the call for the quarter just reported.** `bigdata_search` in fast mode with the reporting period filter set to the quarter, for the earnings release and the transcript, then `bigdata_fetch_document` on both. Done when the reported figures, the segment and KPI figures, the new guidance quoted verbatim with its ranges, the non-GAAP reconciliation, and the two or three Q&A exchanges that bear on the drivers are in hand.
3. **The guidance it replaces.** `bigdata_search` in fast mode for the previous quarter's call, with the reporting period filter set to that quarter, and `bigdata_fetch_document` on it. Guidance for the quarter just reported was given on that call; annual guidance may have been set at the start of the fiscal year and updated since. Done when every metric in the new guidance has its prior range, the date it was given, and the call it came from.
4. **The quarterly filing, if out.** Search for the 10-Q or interim report for the quarter and fetch it. Done when the cash flow statement, receivables, inventory, deferred revenue, provisions and any change in accounting or segment reporting for the quarter and the same quarter a year earlier are in hand, or the note says the filing is not yet available.
5. **The Street's reaction.** Two or three `bigdata_search` calls, one aspect each, since the release: estimate revisions and target changes reported in research and news; rating changes; the explanations analysts and the press gave for the stock's move. Done when the revisions are listed with dates and sources, or marked none found, and labelled as press or research summaries.
6. **The price reaction.** `bigdata_computer` on the daily price series for the stock and its index (the S&P 500 or the home-market index; state which) for the event day and the 60 months before it. Done when the event-day return, the index return, the beta over 60 months and the abnormal return are computed, with the working shown.
7. **Consensus before the print.** If the estimates section carries no history, search for research and news in the weeks before the report that quote consensus for FY+1, FY+2 and long-term growth. Done when the "before" column of the outlook table has figures with dates, or the note says the history is not available and uses the earliest vintage found.
8. **Sector primer.** Read the company's section in `references/sector-primers.md` for the metrics the sector reports and its accounting traps. Banks report net interest income, provisions and capital; insurers report the combined ratio and reserve development; the tables follow the primer. Done when the sector's reporting metrics and accounting traps are noted.

## Analyse

1. **Results against consensus and guidance.** For sales, gross margin, EBIT or EBITA and its margin, EPS, free cash flow and the sector's key operating metric: the actual, the consensus with its vintage and the number of estimates, the surprise in percent (or basis points for margins), the guidance range and the actual against its midpoint, and the change on the prior year. Place the surprise against the company's own last eight quarters of surprises so the reader sees whether this one is large for this company. Done when one table carries all of it, every cell labelled reported or derived.

2. **What made the beat or miss, and does it recur.** Decompose the surprise into volume, price and mix, segment, currency, cost lines, tax rate, share count and below-the-line items. From `references/earnings-quality.md`, run steps 2, 3, 5 and 7 on the quarter against the same quarter a year earlier: cash from operations against net income, the operating profit rebuilt without one-off gains and charges, the contribution of reserve releases, and receivables, inventory and deferred revenue against revenue. Then label each part of the surprise recurring or one-time. Done when the note can say how much of the beat or miss was operating, how much came from tax, buybacks, reserve releases, gains or timing, and in which direction cash disagreed with earnings.

3. **Prior guidance against new.** One row per guided metric: the prior range with its date, the new range, the change at the midpoint, and consensus before the call for the same period. State what the change implies for the second half or the next year if the company guides only one quarter. Guidance sets the forward numbers the price rests on, so this table comes before the long-term outlook. Done when every metric the company guides on has a row, and metrics it stopped guiding on are flagged.

4. **What changed in the long-term outlook.** The price capitalises many years of cash flow, so the question is whether the quarter changed them. From rule 1 in `references/after-a-price-move.md`, answer the five questions:
   - (a) Consensus for FY+2 and beyond, long-term growth and guidance, before and after the print, with the change.
   - (b) Whether the drivers of the surprise recur (price, volume, margin structure) or are one-time.
   - (c) Whether cash flow agrees with the earnings line; the market follows cash when the two diverge.
   - (d) Which revision matters for this company, from the value-trigger rule in `references/expectations.md`: incremental return where it earns near its cost of capital, sales growth where it earns well above it.
   - (e) Whether the news is diagnostic, changing the probability of the thesis, or only looks causal.

   Then, from formula 2 in `references/expectations.md`, compute the perpetual growth the enterprise value implied before the print and after it, at a stated cost of capital labelled assumed with a range of plus and minus one point. Done when the note classifies the quarter as a change in the long-term outlook, a short-term event or unclear, and says whether the size of the stock's move matches the change in long-term cash flow.

5. **The thesis check.** From `references/forecasting-discipline.md`: list the premises of the thesis being tested (the user's, or the prevailing bull case and bear case), tag each piece of evidence from the quarter as a fact or an opinion, and test any kill criteria the user wrote against their thresholds and dates. Give each premise one of four words:
   - Intact: the evidence neither confirms nor contradicts it materially.
   - Strengthened: a reported fact now confirms it.
   - Weakened: a reported fact contradicts it without crossing a kill threshold.
   - Broken: a kill criterion is crossed, or the premise the thesis rests on is disproved.

   The thesis takes the word of its weakest load-bearing premise. Update by the right amount: one quarter's noise does not break a multi-year thesis, and a guidance cut on the linchpin driver is not noise. Done when each premise has its word, the fact behind it with a source, and the thesis has its overall word with one sentence of reasoning.

6. **Estimate and valuation refresh.** Consensus for FY+1 and FY+2 sales, EBIT and EPS before and after the print, the number of target changes and their direction, the mean target before and after, and rating changes, from step 5 of Gather. Then the valuation before and after: price, forward P/E, EV/EBITDA and free cash flow yield on the old and the new consensus, the steady-state P/E at the stated cost of equity from formula 1 in `references/expectations.md`, and the implied growth from step 4. Where the outlook changed, re-weight the scenarios: from `references/forecasting-discipline.md`, three cases with what must be true in each, probabilities that sum to 100 taken from a reference class (the company's own beat-and-raise record, the base rates for the growth now implied in `references/base-rates.md`) rather than a default split, and the probability-weighted range. Done when the table shows each measure before and after with dates, and the note states what the market now prices in. No price target of the note's own.

7. **Quality signals for the quarter.** One table: cash from operations against net income, DSO, inventory days, deferred revenue growth against revenue growth for subscription businesses, one-off items in the quarter and whether that type recurred in prior quarters, reserve releases, stock compensation against revenue, and guidance credibility (the actual against the midpoint for the last eight quarters). Each row has this quarter, the same quarter a year earlier, the direction, and the watch-for: the threshold next quarter that would turn the signal from noise into a flag. Done when each row has a value or a "not disclosed" and a watch-for.

8. **The market reaction against the base rates.** From `references/after-a-price-move.md`: state the event-day move against the index, simple and beta-adjusted, and say which one is tested against the 10 percent trigger (step 6 of Gather), and decompose the move into fundamental news, a change in the multiple, and flows. If the move was 10 percent or more against the index in one day, classify it as an earnings event, score momentum, valuation and quality before the print with the proxies in table 5, and quote the earnings row from table 1 (drops, January 1990 to June 2014) or table 2 (gains, January 1990 to July 2015) with N, the event-day move and the mean abnormal return at 30, 60 and 90 trading days, the dispersion statement from step 5 of that file (table 4 gives the published cells), and the parent branch when the leaf N is under about 50. Say that the proxies are not the HOLT scores the papers used. If the move was under 10 percent, say that the published base rates do not cover it and stop at the decomposition. Done when the note has the classification, the row or the statement that none applies, and one sentence on what the row does and does not say.

9. **The next date.** The next earnings date from the calendar, and any other dated event the call or the release named: an investor day, a guidance update, a product launch, a regulatory decision, a debt maturity. Done when the note names at least one date and what it will resolve.

For a cyclical, show the quarter's margin against the mid-cycle margin before reading a beat as a new run rate. For a bank, replace step 2's working-capital tests with net interest margin, provisions against charge-offs and reserve coverage, and step 6's EV multiples with price to book against return on equity.

## Write

Follow `references/output-standard.md`. The full review has these sections in this order; the reaction note keeps the ones marked (R) and shortens each to its table and two or three sentences.

```
# <Company> (<ticker>) earnings review: Q<n> FY<yyyy>, reported <date>
Data as of: price <date>; estimates <date, before and after>; statements <period>; newest document <date>.

## What happened (R)
Four to eight sentences: the result against consensus and guidance, what made it, the guidance
change, whether the long-term outlook moved, the thesis word, the stock's reaction against the
base rate, and the next date. No rating, no action.

## Results against consensus and guidance (R)
| Metric | Actual | Consensus (n, vintage) | Surprise | Guidance (low, mid, high) | vs midpoint | YoY | Basis | Source |
One line on the surprise against the company's eight-quarter record.

## What made the beat or miss
The decomposition, each part labelled recurring or one-time, with cash against earnings.

## Guidance: prior against new (R)
| Metric | Period | Prior range (date) | New range | Change at midpoint | Consensus before | Source |

## The long-term outlook (R)
| Measure | Before print | After print | Change | Source |
Rows: FY+1, FY+2 and later consensus, long-term growth, implied perpetual growth at the stated
cost of capital. Then the five answers and the classification.

## Thesis check (R)
| Premise | Evidence this quarter | Fact or opinion | Word | Source |
Overall: Intact, Strengthened, Weakened or Broken, with one sentence. Kill criteria tested.

## Estimates and valuation
| Measure | Before | After | Change | Basis | Source |
Scenario table if re-weighted: | Case | What must be true | Probability | Value range | Basis |

## Quality signals
| Signal | This quarter | Year-ago quarter | Direction | Watch for next quarter | Source |

## Market reaction (R)
Move against the index, beta-adjusted; the decomposition; the base-rate row with N, sample and
period, or the statement that the move is outside the published samples.

## Next date (R)
The event, the date, what it resolves.

## What would change this view
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: the full review two to four pages; the reaction note one to two pages. A narrow question ("did they beat", "what did they guide") gets the relevant table and the sources, and keeps the footer.

## Checks before sending

1. The prior guidance comes from the call for the quarter before the one reported, is quoted with its date, and sits next to the new range.
2. Consensus figures carry their vintage and the number of estimates, and the "before" figures are dated before the release.
3. The long-term outlook section shows FY+2 and later consensus before and after, and the implied growth before and after at a cost of capital labelled assumed.
4. Every part of the surprise is labelled recurring or one-time, and the note says whether cash agreed with earnings.
5. The thesis word is one of the four, each premise has a sourced fact, and facts are kept apart from opinions.
6. The base-rate row is quoted only for a one-day move of 10 percent or more against the index, with N, sample and period; otherwise the note says the samples do not cover the move.
7. Scenario probabilities, if shown, sum to 100 and name their reference class.
8. No buy, hold, sell, add, trim, price target or rating language; the note describes the evidence and what would change it.
9. Every figure has a Basis label and a source number, or appears in the Gaps line.

## Hand-offs

- The company has not reported yet: `bigdata-earnings-preview`.
- The user wants a full revaluation after the print: `bigdata-valuation`. A deeper look at the accounting: `bigdata-earnings-quality`.
- The stock moved on something other than the results: `bigdata-stock-move`.
- After delivering, make one offer: a monitor on the company's news and filings until the next report date, or the review saved to the user's Bigdata.com account. Act only on a clear yes.
