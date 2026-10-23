---
name: bigdata-earnings-preview
description: Setup before a company reports, from Bigdata.com estimates, the last call, filings and news: the drivers of the quarter, consensus against guidance and base rates, what the price implies, the sales-to-margin sensitivity, scenarios with what to watch in each, and the metrics to check first. Use when the user asks for an earnings preview, what to expect when a company reports, the setup into the print, or what consensus is looking for. Not for results already reported, which bigdata-earnings-review covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, operating-leverage-and-tam, forecasting-discipline, after-a-price-move
  bigdata-sector-primer: auto
---

# Earnings preview

This skill writes the note a portfolio manager reads the evening before a company reports: what the quarter turns on, what the market expects and already pays for, what management promised, how a miss or beat on sales reaches earnings, and what to look at first when the release hits. It is sized to the question. "What is consensus for Micron's quarter?" gets the consensus table and the guidance line with sources, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not write a preview from memory or the web: an unsourced preview looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-earnings-preview"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call. It says how to resolve the company, which tearsheet sections to request, how to search and retry, and how estimates carry actuals, surprise and guidance.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the quarter needs it.

## Scope the request

Establish three things before gathering data, from the request or from the events calendar: the company (resolved with `find_securities`), the quarter being reported (fiscal year and quarter, from `events_calendar` in the tearsheet or `bigdata_events_calendar`), and the user's angle if they gave one (a position, a driver they care about, a peer that just reported). Assume the next unreported quarter when the user does not say.

Ask one question only if the answer changes the work: the company name resolves to more than one listing, or the user seems to want a different quarter than the next one. Otherwise state the assumption in the header and proceed.

If `find_securities` returns the company as Private, say that the estimates and tearsheet do not exist for it and offer a document-based summary of what is known about its results instead.

## Gather

Work through these in order. Each step says what it must produce.

1. **Tearsheet, in two calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, events_calendar, analyst_data, price_performance, latest_earnings, estimates` first, then a second call for `fundamentals, revenue_segmentation`. Done when the report date, the consensus for the quarter and the next fiscal year, the actual and surprise for the last eight quarters, any guidance fields, the price moves since the last print, the targets and rating counts, and five fiscal periods of statements are in hand.
2. **The last earnings call.** `bigdata_search` in fast mode for the transcript of the previous quarter's call with the reporting period filter set to that quarter, then `bigdata_fetch_document` on the transcript. Done when management's guidance for the quarter being previewed is quoted verbatim with its ranges, and the questions analysts pressed on are listed. Guidance for the next quarter is given on the current quarter's call, so the call to read is the one for the quarter before the one being previewed, never a later one.
3. **What changed since that call.** Three to five `bigdata_search` calls, one aspect each: company news since the last print; the company's own filings or releases since then (8-K, pre-announcements, investor-day material); peer and supplier prints that bear on the quarter; sell-side notes on the setup (research and news that quote analysts); the data points the drivers depend on (pricing, volumes, channel checks, macro series). Done when every driver in the analysis has at least one dated piece of evidence or is marked as having none.
4. **Sentiment and positioning.** `bigdata_sentiment_tearsheet` for the company over the last 90 days. Done when the direction of news sentiment into the print and the stories driving it are known. Short interest and options data are not in Bigdata.com; say so in the Gaps line if the user asks for positioning.
5. **Sector primer.** If the company is in a sector with a primer in `references/sectors/`, read it for the metrics the sector reports and the accounting traps before analysing. Banks and insurers report different lines (net interest income, provisions, combined ratio) and the preview's tables follow the primer.

## Analyse

1. **Build the consensus table.** For the quarter: sales, gross margin, EBIT and EBIT margin, EPS, free cash flow and capex where estimates exist, each with the mean, the number of estimates if given, the change in the mean over the last 30 and 90 days, the prior-year actual and the implied growth, the prior quarter for the sequential comparison, and the company's guidance range with the midpoint. Label each cell reported, derived or assumed. The vintage of the consensus is the tearsheet's estimate date. Done when a reader can see in one table what the Street expects, how it moved, and what management guided.

2. **Guidance credibility.** From the last eight quarters' actuals against the guidance midpoint (the estimates section carries guidance for some metrics; the transcripts carry the rest), state the company's pattern: how often it beats its own midpoint, by how much, and whether the beat has been shrinking. Say in one line what the pattern implies for the printed number against the guide. Done when the pattern is stated with the count of quarters it rests on.

3. **The drivers of the quarter.** Name three to five drivers that decide the print, in order of weight: volume, price and mix, the largest cost lines, the segment that moves the total, currency, anything the company flagged. For each driver: what consensus assumes (derived from the estimates, or stated as not inferable), the evidence since the last call with its date and source, and the direction of risk against consensus. The value-trigger logic in `references/expectations.md` says which revisions matter for this company: incremental return where it earns near its cost of capital, sales growth where it earns well above. Done when every driver has evidence or an explicit "no new evidence" and a direction.

4. **Consensus against base rates.** Place the consensus sales growth and EPS growth for the next fiscal year in the reference class from `references/base-rates.md`: the size decile by prior-year sales and the horizon, with the share of companies that achieved it, and the real-to-nominal conversion stated. Done when each growth figure carries a sentence of the form "requires X percent nominal growth, about Y percent real, which Z percent of companies in the A to B size class achieved over this horizon (top 1,000 global companies, 1950 to 2015)".

5. **What is priced in.** From `references/expectations.md`: the price move since the last print against the index; the forward P/E against the steady-state P/E at a stated cost of equity (an assumption, shown with its basis); the growth the enterprise value implies at the stated cost of capital against consensus; the direction of estimate revisions against the direction of the price (expectations rising, falling, or price moving without revisions); the sentiment trend; the analyst targets' range against the price. Done when the note says in two sentences whether the bar for the quarter is high or low and why.

6. **The sales-to-margin sensitivity.** From `references/operating-leverage-and-tam.md` and the company's own cost structure (gross margin, the fixed-cost lines in the five years of statements): what a sales miss or beat of a stated size does to EBIT and EPS. Use the sector's operating-margin beta from `references/base-rates.md` as the outside view and the company's own history of margin change per unit of sales change as the inside view, and show both. Done when the note gives the EPS effect of a 3 percent and a 5 percent sales miss and beat, labelled derived, with the formula.

7. **Scenarios.** Three cases, from `references/forecasting-discipline.md`: beat and raise, in line, miss or cut. For each: what has to be true on the drivers, the printed sales and EPS against consensus, the probability, the likely stock reaction given what is priced in and the base rates for post-earnings moves in `references/after-a-price-move.md`, and the single signal in the release or call that tells the reader which case is unfolding. Probabilities sum to 100 and start from the company's own beat rate and the sector's surprise history rather than a default split. Done when the three rows are complete and the expected value of the cases is consistent with the "what is priced in" paragraph.

8. **What to check first.** Five to seven items in the order a reader should check them when the release lands: the metric, the consensus or guided figure, the threshold that changes the reading. Then five questions for the call, each tied to a driver or to a claim management made last time.

For a cyclical, state where the company sits in its cycle and show the mid-cycle margin next to the consensus margin, as `references/valuation.md` requires, so a peak-margin print is not read as a run rate. For a bank, use the primer's lines and skip the sales-to-margin step; the equivalent is net interest income against rate assumptions and provisions against the credit cycle.

## Write

Follow `references/output-standard.md`. The note has these sections in this order.

```
# <Company> (<ticker>) earnings preview: Q<n> FY<yyyy>, reports <date, time, before or after market>
Data as of: estimates <date>; latest statements <period>; newest document <date>.

## The setup
Four to eight sentences: what the quarter turns on, whether the bar is high or low and why,
what management guided, and the one thing that would make this print matter beyond the quarter.
No rating.

## The quarter at a glance
| Metric | Consensus (n) | 30d / 90d change | Guidance (low, mid, high) | Prior year | Growth | Prior quarter | Basis | Source |

## Guidance record
Table of the last eight quarters: guided midpoint, actual, difference. One sentence on the pattern.

## Drivers
One subsection per driver, each with: consensus assumption, evidence since the last call (dated),
direction of risk.

## Consensus against base rates
The sentences from step 4, for sales and EPS.

## What is priced in
Price since last print vs index; forward P/E vs steady-state P/E; implied growth vs consensus;
estimate revisions vs price; sentiment; target range. Two closing sentences.

## Sensitivity
| Sales vs consensus | EBIT effect (inside view) | EBIT effect (sector beta) | EPS effect | Basis |
Rows for -5, -3, +3, +5 percent.

## Scenarios
| Case | What has to be true | Sales / EPS vs consensus | Probability | Likely reaction | Watch for |

## What to check first
Numbered list, metric, figure, threshold.

## Questions for the call
Five, each with the driver or claim it tests.

## What would change this view
Two to five dated or observable conditions.

## Gaps
What Bigdata.com could not answer (positioning data, whisper numbers, a missing transcript).

## Sources
Numbered. Then the Powered by Bigdata.com line and the disclaimer, verbatim from output-standard.md.
```

Length: two to four pages. For a narrow question, answer it in the method's terms with the relevant table and the sources, and keep the footer.

## Checks before sending

1. The guidance quoted is from the call for the quarter before the one previewed, verbatim, with a citation.
2. The consensus table states its vintage and the number of estimates where available.
3. "What is priced in" comes before any sentence that reads as a view.
4. Each growth figure has its base-rate sentence with the size class, horizon, share and sample label.
5. The sensitivity rows show the formula and the inside and outside views.
6. Scenario probabilities sum to 100 and are anchored to a stated beat rate, not a default split.
7. No buy, hold, sell, overweight, underweight, accumulate, avoid, or rating word anywhere.
8. Every figure carries a Basis label and a source number, or appears in the Gaps line.
9. Nothing in the note comes from memory or the web; a driver with no evidence says so.
10. The cost of equity and cost of capital used are stated as assumptions with their basis.

## Hand-offs

- The company has already reported the quarter: use `bigdata-earnings-review`.
- The user wants the full valuation behind "what is priced in": `bigdata-valuation`.
- The user asks what else is coming for the name beyond the print: `bigdata-catalysts`.
- After delivering, make one offer: save a monitor that flags the company's news until the report date, or the note itself to the user's Bigdata.com account. Act only on a clear yes.
