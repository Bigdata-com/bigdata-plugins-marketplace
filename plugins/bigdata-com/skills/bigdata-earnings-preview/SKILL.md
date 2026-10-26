---
name: bigdata-earnings-preview
description: >-
  Setup before a company reports: drivers of the quarter, consensus vs guidance, what the price
  implies, scenarios, what to check first. Use for an earnings preview, what to expect when X
  reports. Not results: bigdata-earnings-review.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, operating-leverage-and-tam, forecasting-discipline, after-a-price-move, valuation
  bigdata-sector-primer: auto
---

# Earnings preview

This skill writes the note a portfolio manager reads the evening before a company reports: what the quarter turns on, what the market expects and already pays for, what management promised, how a miss or beat on sales reaches earnings, and what to look at first when the release hits. It is sized to the question. "What is consensus for Micron's quarter?" gets the consensus table and the guidance line with sources, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-earnings-preview"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish three things before gathering data, from the request or from the events calendar: the company (resolved to its Bigdata.com entity), the quarter being reported (fiscal year and quarter, from the company's next report date or the corporate calendar), and the user's angle if they gave one (a position, a driver they care about, a peer that just reported). Assume the next unreported quarter when the user does not say. The reader may be the company's own IR or finance team preparing for its print, or a competitor, customer or supplier reading the setup: write the implications for that reader (the questions the Street will press, the bar the print must clear), with the same evidence and no call.

Ask one question only if the answer changes the work: the company name resolves to more than one listing, or the user seems to want a different quarter than the next one. Otherwise state the assumption in the header and proceed.

If the lookup returns the company as Private, say that the estimates and market data do not exist for it and offer a document-based summary of what is known about its results instead.

## Gather

Work through these in order.

1. **The company's numbers.** Profile and quote, the next report date and the latest quarter against consensus; consensus with its vintage, the ratings and targets, and the 13F holder changes and options activity; five fiscal years of annual statements, valuation metrics and segments (annual periods, not the default quarters); and quarterly statements for the prior quarter and the same quarter a year earlier. Done when the report date, the consensus for the quarter and the next fiscal year with its vintage, the actuals and surprises the estimates section gives for past quarters, any guidance fields, the targets and rating counts, the 13F holder changes and options activity, five fiscal years and five quarters of statements are in hand.
2. **The last earnings call.** The full transcript of the previous quarter's call, with the period fixed to that quarter rather than inferred. Done when management's guidance for the quarter being previewed is quoted verbatim with its ranges, and the questions analysts pressed on are listed. Guidance for the next quarter is given on the current quarter's call, so the call to read is the one for the quarter before the one being previewed, never a later one.
3. **What changed since that call.** Three to five searches, one aspect each: company news since the last print; the company's own filings or releases since then (8-K, pre-announcements, investor-day material); peer and supplier prints that bear on the quarter; sell-side notes on the setup (research and news that quote analysts); the data points the drivers depend on (pricing, volumes, channel checks, macro series). Done when every driver in the analysis has at least one dated piece of evidence or is marked as having none.
4. **Revisions and the print record.** Consensus is a snapshot with no history, and the latest-earnings record is one quarter. Two searches: research and news over the last 90 days that quote the quarter's or the year's consensus at an earlier date (the revision route), and the results releases or reports of the prior two to four prints (dates, actual against consensus, guidance given). Use the actuals the consensus data gives for past quarters before searching. Done when each revision found is quoted with its document's date and labelled press or research summary, or marked not found, and the number of past quarters found is stated.
5. **The typical earnings-day move.** Daily prices for the stock and its index around the last four print dates found in step 4 (the day after for an after-market report), and over the run since the last print, computed, not estimated, since the company's quote gives standard windows only. Done when each found print has its move against the index, the median absolute move is stated with the number of prints, and the run since the last print against the index is in hand, all labelled derived.
6. **Sentiment and positioning.** The sentiment report (it has no window; say which period its narrative covers), and the holder and options data from step 1: 13F holders and options activity, quarterly and lagged, so it shows who held the stock last quarter, not who is positioned today. Options prices, implied volatility and short interest are not in Bigdata.com; say so in Gaps. Done when the direction of news sentiment into the print, its period, and the holder changes with their quarter are known.
7. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its metrics that matter, its accounting traps and its "Questions for the earnings call" subsection (some sectors title it "Questions a specialist asks on the earnings call"). Banks and insurers report different lines (net interest income, provisions, combined ratio) and the preview's tables follow the primer. Done when the sector's reporting lines, traps and call questions are noted, or their absence is stated.

## Analyse

1. **Build the consensus table.** For the quarter: sales, gross margin, EBIT and EBIT margin, EPS, free cash flow and capex where estimates exist, each with the mean, the number of estimates if given, the revision found in Gather step 4 with its date (or "not found"), the prior-year actual and the implied growth, the prior quarter for the sequential comparison, and the company's guidance range with the midpoint. Label each cell reported, derived or assumed. The vintage of the consensus is the estimate date given with it. Done when a reader can see in one table what the Street expects, how it moved, and what management guided.

2. **Guidance credibility.** From the past quarters found in Gather step 4, actuals against the guidance midpoint (the estimates section carries guidance for some metrics; the releases and transcripts carry the rest), state the company's pattern: how often it beats its own midpoint, by how much, and whether the beat has been shrinking. Say in one line what the pattern implies for the printed number against the guide. Done when the pattern is stated with the count of quarters it rests on.

3. **The drivers of the quarter.** Name three to five drivers that decide the print, in order of weight: volume, price and mix, the largest cost lines, the segment that moves the total, currency, anything the company flagged. For each driver: what consensus assumes (derived from the estimates, or stated as not inferable), the evidence since the last call with its date and source, and the direction of risk against consensus. The value-trigger logic in `references/expectations.md` (formula 4) says which revisions matter for this company, classified on the three-year rolling ROIIC from the annual statements, never one year: incremental return where it is near the cost of capital, sales growth where it is well above. Done when every driver has evidence or an explicit "no new evidence" and a direction.

4. **Consensus against base rates.** Where consensus growth over the next few years is the question (a high multiple resting on it, or a guide well above history), place it in the reference class from `references/base-rates.md`: the three-year column for the size class by prior-year sales (the one-year column is noisy), with the share of companies that achieved it and the real-to-nominal conversion stated. Not every growth figure needs one. Done when each growth figure the note leans on carries a sentence of the form "requires X percent nominal growth a year over three years, about Y percent real, which Z percent of companies in the A to B size class achieved (historical base rate, sample and period)".

5. **What is priced in.** From `references/expectations.md`: the price move since the last print against the index; the forward P/E against the steady-state P/E at a stated cost of equity (an assumption, shown with its basis); the growth the enterprise value implies at the stated cost of capital (the WACC from `references/valuation.md`) against consensus; the direction of estimate revisions against the direction of the price (expectations rising, falling, or price moving without revisions); the sentiment trend; the analyst targets' range against the price. Done when the note says in two sentences whether the bar for the quarter is high or low and why.

6. **The sales-to-margin sensitivity.** From `references/operating-leverage-and-tam.md` and the company's own cost structure (gross margin, the fixed-cost lines in the five years of statements): what a sales miss or beat of a stated size does to EBIT and EPS. Use the sector's operating-margin beta from `references/base-rates.md` as the outside view and the company's own history of margin change per unit of sales change as the inside view, and show both. Done when the note gives the EPS effect of a 3 percent and a 5 percent sales miss and beat, labelled derived, with the formula.

7. **Scenarios.** Three cases, from `references/forecasting-discipline.md`: beat and raise, in line, miss or cut. For each: what has to be true on the drivers, the printed sales and EPS against consensus, the probability, the likely stock reaction given what is priced in and sized against the typical earnings-day move from Gather step 5, and, where the likely reaction is a one-day move of 10 percent or more against the index, the base rates in table 1 and table 2 of `references/after-a-price-move.md` with N and the sample period, called historical. Probabilities sum to 100 and start from the company's own beat rate, with the number of quarters it rests on, rather than a default split. Most companies beat a consensus that was walked down into the print, so a beat alone is the expected case and tells little: the reaction turns on the size of the beat against the company's typical beat, and on the guide against next-period consensus. Write each case in those terms, citing the company's own record where found. Done when the three rows are complete and the expected value of the cases is consistent with the "what is priced in" paragraph.

8. **What to check first.** Five to seven items in the order a reader should check them when the release lands: the metric, the consensus or guided figure, the threshold that changes the reading. Then five questions for the call, each tied to a driver or to a claim management made last time, starting from the primer's earnings-call questions (Gather step 7) and adapted to this company. Done when each item has its metric, figure and threshold, and each question names its driver or claim.

For a cyclical, state where the company sits in its cycle and show the mid-cycle margin next to the consensus margin, as `references/valuation.md` requires, so a peak-margin print is not read as a run rate. For a bank, use the primer's lines and skip the sales-to-margin step; the equivalent is net interest income against rate assumptions and provisions against the credit cycle.

## Write

Follow `references/output-standard.md`. The note has these sections in this order.

```
# <Company> (<ticker>) earnings preview: Q<n> FY<yyyy>, reports <date, time, before or after market>
Data as of: estimates <date>; latest statements <period>; newest document <date>.

## The setup
Four to eight sentences. First the bar for the quarter: consensus against the guide, the
revisions found, and the stock's run into the print against the index. Then what the price
implies, with the figures (the forward P/E against the steady-state P/E, or the implied growth
against consensus) and their basis; then whether the bar is high or low and why, and the one
thing that would make this print matter beyond the quarter. No rating.

## The quarter at a glance
| Metric | Consensus (n) | Revision found (date) | Guidance (low, mid, high) | Prior year | Growth | Prior quarter |
One "Basis and sources" note under the table: consensus reported with its vintage; revisions
press or research summaries; growth derived.

## Guidance record
| Quarter | Guided midpoint | Actual | Difference | Basis | Source |
The past quarters found (say how many). One sentence on the pattern, and the median earnings-day
move against the index over the prints found.

## Drivers
One subsection per driver, each with: consensus assumption, evidence since the last call (dated),
direction of risk.

## Consensus against base rates
The sentences from step 4, for the growth figures the note leans on.

## What is priced in
Price since last print vs index; forward P/E vs steady-state P/E; implied growth vs consensus;
estimate revisions vs price; sentiment; target range. Two closing sentences.

## Sensitivity
| Sales vs consensus | EBIT effect (inside view) | EBIT effect (sector beta) | EPS effect | Basis | Source |
Rows for -5, -3, +3, +5 percent.

## Scenarios
| Case | What has to be true | Sales / EPS vs consensus | Probability | Likely reaction | Watch for | Basis | Source |

## What to check first
Numbered list, metric, figure, threshold.

## Questions for the call
Five, each with the driver or claim it tests.

## What would change this reading
Two to five dated or observable conditions.

## Gaps
What Bigdata.com could not answer (options prices and short interest, whisper numbers, consensus
history not found in search, a missing transcript).

## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. For a narrow question, answer it in the method's terms with the relevant table and the sources, and keep the footer.

## Checks before sending

1. The guidance quoted is from the call for the quarter before the one previewed, verbatim, with a citation.
2. The consensus table states its vintage and the number of estimates where available.
3. The setup paragraph states the bar for the quarter, then the price-implied figures, before any sentence that reads as a view, and every number in it carries a citation or a basis word.
4. Each growth figure the note leans on has its base-rate sentence from the three-year class, with the share and sample label.
5. The sensitivity rows show the formula and the inside and outside views.
6. Scenario probabilities sum to 100, are anchored to a stated beat rate with its quarter count, and the cases are written on the size of the beat and the guide, not on beat or miss alone.
7. No buy, hold, sell, overweight, underweight, accumulate, avoid, or rating word anywhere.
8. Every figure carries a Basis label and a source number, or appears in the Gaps line.
9. Nothing in the note comes from memory or the web; a driver with no evidence says so.
10. The cost of equity and cost of capital used are stated as assumptions with their basis.

## Hand-offs

- The company has already reported the quarter: use `bigdata-earnings-review`.
- The user wants the full valuation behind "what is priced in": `bigdata-valuation`.
- The user asks what else is coming for the name beyond the print: `bigdata-catalysts`.
- After delivering, make one offer: save a monitor that flags the company's news until the report date, or the note itself to the user's Bigdata.com account. Act only on a clear yes.
