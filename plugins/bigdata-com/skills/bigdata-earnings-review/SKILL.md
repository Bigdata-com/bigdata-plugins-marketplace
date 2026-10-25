---
name: bigdata-earnings-review
description: >-
  After a company reports: results vs consensus and guidance, what changed in the outlook, thesis
  check, reaction, peer read-across. Use for how did X do, beat or miss, a competitor's print. Not
  the setup: bigdata-earnings-preview.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, after-a-price-move, earnings-quality, forecasting-discipline, base-rates
  bigdata-sector-primer: auto
---

# Earnings review

This skill writes the note the morning after a print: results against consensus and guidance, the guidance change, whether the long-term outlook moved, the thesis or the Street's reception, the read-across to peers, the quality of the beat or miss, the reaction, and the next date. It sizes to the question. "Did Nike beat?" gets the results table and the guidance line. "Give me a reaction note" gets the short form, one to two pages. "Analyse Nike's quarter" gets the full review. It gives no rating and no action.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-earnings-review"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call, including which call carries which quarter's guidance.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the quarter needs it.

## Scope the request

Establish four things before gathering data. The company, resolved with `find_securities`. The quarter: the latest reported one unless the user names another, confirmed from `latest_earnings` and the events calendar. The form: a reaction note when the user asks for a reaction, "how should I read this", or "does it change the thesis" in a sentence; the full review otherwise. The thesis: a stated one (a case, a driver, kill criteria) is tested; "does it change the thesis" with none stated tests the prevailing bull and bear cases from the preview-period research, labelled as the Street's. With no thesis (a corporate or IR reader, a competitor's or customer's print), "How the Street received it" replaces the thesis check, and the note writes the implications for that reader: our pricing, our orders, our next call.

Ask one question only if the answer changes the work: the user refers to "my thesis" without stating it, or the name resolves to more than one listing. Otherwise state the assumptions in the header and proceed.

If the company has not reported the quarter yet, say so and hand off to `bigdata-earnings-preview`. If the transcript is not yet in Bigdata.com, write from the release and say the call will be added when it is available.

## Gather

1. **Tearsheet, in four calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, latest_earnings, earnings_calendar`; then `analyst_estimates, analyst_ratings`; then `financial_statements, revenue_segmentation` at the default quarterly interval (the quarter and the same quarter a year earlier); then `financial_statements, key_metrics` with `interval` annual (five fiscal years, for the three-year rolling ROIIC). `latest_earnings` is one quarter: for the surprise and guidance record use the actuals in `analyst_estimates`, else search for the prior two to four prints. Done when the quarter's actual, consensus and surprise, the past quarters found (with the count), guidance fields, consensus with its vintage, targets, ratings, statements and the next date are in hand.
2. **The release and the call for the quarter just reported.** `bigdata_search` in fast mode with the reporting period filter set to the quarter, for the earnings release and the transcript, then `bigdata_fetch_document` on both. Done when the reported figures, the segment and KPI figures, the new guidance quoted verbatim with its ranges, the non-GAAP reconciliation, and the two or three Q&A exchanges that bear on the drivers are in hand.
3. **The guidance it replaces.** `bigdata_search` in fast mode for the previous quarter's call, with the reporting period filter set to that quarter, and `bigdata_fetch_document` on it. Annual guidance may have been set earlier in the year and updated since. Done when every metric in the new guidance has its prior range, the date it was given, and the call it came from.
4. **The quarterly filing, if out.** Search for the 10-Q or interim report for the quarter and fetch it. Done when the cash flow, working capital, provisions and any accounting or segment change for the quarter and the year-ago quarter are in hand, or the filing is noted as not yet available.
5. **The Street's reaction.** Two or three `bigdata_search` calls, one aspect each, since the release: estimate revisions and target changes reported in research and news; rating changes; the explanations analysts and the press gave for the stock's move. Done when the revisions are listed with dates and sources, or marked none found, and labelled as press or research summaries.
6. **Peer read-across.** One or two `bigdata_search` calls since the release for what competitors, suppliers and customers said about the print or about the same driver (a rival's comment on pricing, a supplier's order book). Done when two to four read-across items are sourced, or none were found.
7. **The price reaction.** `bigdata_computer` on the daily price series for the stock and its index (the S&P 500 or the home-market index; state which) for the event day and the 60 months before it. Done when the event-day return, the index return, the beta over 60 months and the abnormal return are computed, with the working shown.
8. **Consensus before the print.** The estimates section carries no history, so search research and news in the weeks before the report for documents that quote consensus for FY+1, FY+2 and long-term growth, and label each figure press or research summary with its document's date. Done when the "before" column of the outlook table has dated figures, or each is marked not found.
9. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its metrics that matter and its accounting traps; a bank's or insurer's tables follow the primer's lines. Done when the sector's reporting metrics and accounting traps are noted.

## Analyse

1. **Results against consensus and guidance.** For sales, gross margin, EBIT or EBITA and its margin, EPS, free cash flow and the sector's key operating metric: the actual, the consensus with its vintage and the number of estimates, the surprise in percent (or basis points for margins), the guidance range and the actual against its midpoint, and the change on the prior year. Place the surprise against the company's own record over the past quarters found (Gather step 1, with the count), so the reader sees whether this one is large for this company. Done when one table carries all of it, every cell labelled reported or derived.

2. **What made the beat or miss, and does it recur.** Decompose the surprise only as far as the company discloses it: its segments, its own bridge (volume, price and mix, currency, cost lines) and the reported tax rate, share count and below-the-line items. Where it gives no split, say the split is not available; never estimate one. Run `references/earnings-quality.md` steps 2, 3, 5 and 7 on the quarter against the same quarter a year earlier. Then label each part of the surprise recurring or one-time. Done when the note says how much of the beat or miss was operating and how much came from tax, buybacks, reserve releases, gains or timing, and which way cash disagreed with earnings.

3. **Prior guidance against new.** One row per guided metric: the prior range with its date, the new range, the change at the midpoint, and consensus before the call for the same period. If the company guides one quarter, state what the change implies for the year. Done when every metric the company guides on has a row, and metrics it stopped guiding on are flagged.

   **Compare the language with the prior call.** Both transcripts are in hand (Gather steps 2 and 3): which metrics or KPIs management stopped reporting or quoting, which claims from last quarter it dropped or softened, and whether the Q&A turned more defensive (more questions on one topic, shorter or deflected answers). Dropped disclosures are a quality signal (`references/earnings-quality.md` step 11). Done when the changes are listed with quotes from both calls, or the note says the language held.

4. **What changed in the long-term outlook.** The price capitalises many years of cash flow, so the question is whether the quarter changed them. Answer the five questions of rule 1 in `references/after-a-price-move.md`, with (a) as the consensus table before and after (Gather step 8 against the tearsheet), and (d) classified on the three-year rolling ROIIC from the annual statements (`references/expectations.md`, formula 4), never one year. Then, from formula 2 in `references/expectations.md`, compute the perpetual growth the enterprise value implied before the print and after it, at a stated cost of capital labelled assumed with a range of plus and minus one point. Done when the note classifies the quarter as a change in the long-term outlook, a short-term event or unclear, and says whether the size of the stock's move matches the change in long-term cash flow.

5. **The thesis check, or how the Street received it.** With no thesis to test (Scope), report instead how the Street received the print: the revisions found, the target changes and their direction, the rating changes, and the reasons analysts gave, each dated and labelled press or research summary. Done when each is listed or marked not found. With a thesis, from `references/forecasting-discipline.md`: list the premises of the thesis being tested (the user's, or the prevailing bull case and bear case), tag each piece of evidence from the quarter as a fact or an opinion, and test any kill criteria the user wrote against their thresholds and dates. Give each premise one word: Intact (neither confirmed nor contradicted materially), Strengthened (a reported fact confirms it), Weakened (a reported fact contradicts it short of a kill threshold) or Broken (a kill criterion is crossed or the premise is disproved). The thesis takes the word of its weakest load-bearing premise. One quarter's noise does not break a multi-year thesis; a guidance cut on the linchpin driver is not noise. Done when each premise has its word, the fact behind it with a source, and the thesis has its overall word with one sentence of reasoning.

6. **Estimate and valuation refresh.** The consensus before and after sits in the step 4 table; do not repeat it. Here: the number of target changes and their direction, the mean target before and after, and rating changes, from Gather step 5. Then the valuation before and after: price, forward P/E, EV/EBITDA and free cash flow yield on the old and the new consensus, the steady-state P/E at the stated cost of equity from formula 1 in `references/expectations.md`, and the implied growth from step 4. Where the outlook changed, re-weight three scenarios (`references/forecasting-discipline.md`), with probabilities from a reference class (the company's own record, the three-year base rates in `references/base-rates.md`), not a default split. Done when the table shows each measure before and after with dates, and the note states what the market now prices in. No price target of the note's own.

7. **Quality signals for the quarter.** One table: cash from operations against net income, DSO, inventory days, deferred revenue growth against revenue growth for subscription businesses, one-off items in the quarter and whether that type recurred in prior quarters, reserve releases, stock compensation against revenue, and guidance credibility (the actual against the midpoint over the quarters found). Each row: this quarter, the year-ago quarter, the direction, and the threshold next quarter that would turn noise into a flag. Done when each row has a value or a "not disclosed" and a watch-for.

8. **The market reaction against the base rates.** State the event-day move against the index, simple and beta-adjusted (Gather step 7), state which one meets the 10 percent trigger, and decompose the move into fundamental news, a change in the multiple, and flows (`references/after-a-price-move.md` rule 2). If the move was 10 percent or more against the index in one day, run that file's procedure steps 1 to 5 as an earnings event: the proxies scored before the print, the earnings row with N, its sample period, the abnormal returns at 30, 60 and 90 days, the dispersion statement and the parent branch, called historical, and the note that the proxies are not HOLT scores. Under 10 percent, say the published base rates do not cover it and stop at the decomposition. Done when the note has the classification and the row, or the statement that none applies.

9. **Peer read-across.** What the print says for competitors, suppliers and customers (a price increase that rivals can follow, a demand comment that reaches the supply chain), set against what they said about it in Gather step 6. Facts and opinions kept apart. Done when each read-across item names the company, the mechanism and its source.

10. **The next date.** The next earnings date from the calendar, and any other dated event the call or the release named: an investor day, a guidance update, a product launch, a regulatory decision, a debt maturity. Done when the note names at least one date and what it will resolve.

For a cyclical, show the quarter's margin against the mid-cycle margin before reading a beat as a new run rate. For a bank, replace step 2's working-capital tests with net interest margin, provisions against charge-offs and reserve coverage, and step 6's EV multiples with price to book against return on equity.

## Write

Follow `references/output-standard.md`. The full review has these sections in this order; the reaction note keeps the ones marked (R) and shortens each to its table and two or three sentences.

```
# <Company> (<ticker>) earnings review: Q<n> FY<yyyy>, reported <date>
Data as of: price <date>; estimates <date, before and after>; statements <period>; newest document <date>.

## What happened (R)
Four to eight sentences: the result against consensus and guidance, what made it, the guidance
change, whether the long-term outlook moved, the thesis word or the Street's reception, the
stock's reaction against the base rate, and the next date. No rating, no action.

## Results against consensus and guidance (R)
| Metric | Actual | Consensus (n, vintage) | Surprise | Guidance (low, mid, high) | vs midpoint | YoY |
One "Basis and sources" note under the table. One line on the surprise against the company's
record over the quarters found, with the count.

## What made the beat or miss
The decomposition from disclosed segments or the company's bridge, each part labelled
recurring or one-time, with cash against earnings; "split not disclosed" where it is not.

## Guidance: prior against new (R)
| Metric | Period | Prior range (date) | New range | Change at midpoint | Consensus before | Source |
Then what management stopped saying: metrics, claims and Q&A tone against the prior call.

## The long-term outlook
| Measure | Before print | After print | Change | Source |
Rows: FY+1, FY+2 and later consensus (the only before-and-after consensus table in the note),
long-term growth, implied perpetual growth at the stated cost of capital. Then the five answers
and the classification.

## Thesis check, or How the Street received it
| Premise | Evidence this quarter | Fact or opinion | Word | Source |
Overall: Intact, Strengthened, Weakened or Broken, with one sentence. Kill criteria tested.
With no thesis: revisions, target and rating changes, and the reasons given, dated.

## Valuation and targets
| Measure | Before | After | Change | Basis | Source |
Targets, ratings, forward multiples and implied growth; consensus is in the outlook table.
Scenario table if re-weighted: | Case | What must be true | Probability | Value range | Basis |

## Peer read-across
Two to four items: the company affected, what the print implies for it, what it said, sources.

## Quality signals
| Signal | This quarter | Year-ago quarter | Direction | Watch for next quarter | Source |

## Market reaction (R)
Move against the index, beta-adjusted; the decomposition; the base-rate row with N, sample and
period, or the statement that the move is outside the published samples.

## Next date (R)
The event, the date, what it resolves.

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: the full review two to four pages; the reaction note one to two pages. A narrow question ("did they beat") gets the relevant table, the sources and the footer.

## Checks before sending

1. The prior guidance comes from the call for the quarter before the one reported, quoted with its date, next to the new range.
2. Consensus carries its vintage and estimate count; "before" figures are dated before the release; consensus before and after is tabled once.
3. The implied growth before and after uses a cost of capital labelled assumed.
4. The surprise is split only where the company disclosed it, each part labelled recurring or one-time, with cash against earnings.
5. The thesis word is one of the four with a sourced fact per premise, or the Street's reception is dated and sourced.
6. The base-rate row appears only for a one-day move of 10 percent or more against the index, with N and period.
7. The surprise and guidance record states how many quarters it rests on.
8. No buy, hold, sell, add, trim, price target or rating language; every figure has a Basis label and a source number, or is in Gaps.

## Hand-offs

- The company has not reported yet: `bigdata-earnings-preview`.
- The user wants a full revaluation after the print: `bigdata-valuation`. A deeper look at the accounting: `bigdata-earnings-quality`.
- The stock moved on something other than the results: `bigdata-stock-move`.
- After delivering, make one offer: a monitor on the company's news and filings until the next report date, or the review saved to the user's Bigdata.com account. Act only on a clear yes.
