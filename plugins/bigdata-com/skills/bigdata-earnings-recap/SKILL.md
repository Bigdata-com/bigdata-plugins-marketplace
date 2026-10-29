---
name: bigdata-earnings-recap
description: >-
  After a company reports: results vs consensus and guidance, what changed in the outlook, thesis
  check, reaction, peer read-across. Use for how did X do, beat or miss, a competitor's print. Not
  the setup: bigdata-earnings-preview.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, earnings-quality, after-a-price-move, expectations, valuation, forecasting-discipline
  bigdata-sector-primer: auto
---

# Earnings recap

A note on a print that has landed, for someone who will act on it: results against consensus and guidance, what made the beat or miss, the guidance change, whether the long-term outlook moved, the thesis check or the Street's reception, the reaction, the read-across and the next date. Never a rating, a price target or an action. When the company is the user's competitor, customer or supplier, the question is what the print means for the user's business (pricing, orders, their own next call), and that read-across leads. Size the work to the question: "did Nike beat" gets the results against consensus and guidance and the guidance line; "give me a reaction note" gets those plus the thesis or Street line and the reaction, a sentence or three each; "analyse Nike's quarter" gets the full review.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-earnings-recap"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a note that answers it with fewer tables and pieces is the better note.
- **The premise checked against the release first.** A question that says the company "lowered" its outlook may describe a narrowed range with the midpoint unchanged; the note says so plainly before building on it.
- **Prior guidance from the earlier call.** The guidance being replaced was given on the previous quarter's call, read with its period fixed and quoted with its date beside the new range; annual guidance may have been set earlier in the year and updated since.
- **The surprise against the company's own record, when the size of the beat or miss matters,** over the quarters found, with the count, so the reader sees whether it is large for this company.
- **The beat or miss split only as far as the company discloses it.** Segments, its own bridge, the tax rate, the share count, below-the-line items; where there is no split, the note says so and never estimates one. Each part says in its sentence whether it recurs, and cash is set against earnings for the quarter and the year-ago quarter (`references/earnings-quality.md`, rebuilding EBITA, recurring one-offs and provisions).
- **What management stopped saying.** The two transcripts compared for metrics no longer disclosed, claims dropped or softened and a Q&A that turned defensive; only what changed reaches the page. A dropped disclosure is a quality signal.
- **Whether the long-term outlook moved, judged by cash flow beyond the next year,** because the price capitalises many years of it. The evidence is consensus for the next years before and after the print (the before figures from research and news dated before the release), the three-year rolling ROIIC, and, where the move is large enough to need it, the growth the enterprise value implied before and after (`references/after-a-price-move.md`, long-term outlook test; `references/expectations.md`, implied growth and which revision moves value). The judgment is a plain sentence with that evidence (the print changes long-term cash flow, it does not, or the evidence does not settle it yet), never a label or a bolded category, and the size of the move is judged against the change in long-term cash flow. Where an enterprise value is used, its inputs appear once (share count, net debt with leases and stakes outside the operating business, tax rate, discount convention) and the before and after figures both use them. The cost of capital is one stated figure, with the yield, beta and premium in a single clause and no regression statistics, and the 10-year yield comes from the country data (`references/valuation.md`, cost of capital). One central case and one range cover the sensitivity.
- **The thesis check, when the user has a thesis or the Street's reception is the question.** The premises are the user's, or the prevailing bull and bear cases from research published before the print, attributed to the Street. Facts are kept apart from opinions, and kill criteria are tested against their thresholds. Whether each premise held, strengthened, weakened or broke is said in a sentence with its evidence, never as a label or a column of verdicts; the thesis stands only as well as its weakest load-bearing premise. One quarter's noise does not break a multi-year thesis, and a guidance cut on the driver the thesis rests on is not noise (`references/forecasting-discipline.md`, facts, opinions and expectations, and kill criteria with dates).
- **Scenarios re-weighted only where the outlook changed.** The cases partition the outcomes with one cut-off per metric across the note; probabilities move from the earlier weights by what the print showed, starting from the company's own record, never a default split; each case's value shows the figures it rests on, and the probability-weighted result is stated and reconciles with them (`references/forecasting-discipline.md`, updating on evidence and expected value).
- **Quality signals checked, and written up only where one moved.** Cash from operations against net income, receivable and inventory days, deferred revenue against revenue, recurring one-offs, reserve releases, stock compensation against revenue and guidance credibility are read against the year-ago quarter; one that moved earns a sentence with the level next quarter that would turn noise into a flag (`references/earnings-quality.md`, revenue recognition and working capital).
- **The reaction decomposed, when the reaction is part of the question.** The event-day move against the index, simple and beta-adjusted, split into fundamental news, a change in the multiple and flows (`references/after-a-price-move.md`, abnormal return and decomposing the move). Only when the print moved the stock 10 percent or more against the index in one day, and the history changes the reading, does the note add what stocks in the same situation did over the following 30 to 90 days, with the population and period in the sentence and the spread beside the average; below 10 percent the history does not cover the move and stays out (`references/after-a-price-move.md`, drift after one-day drops, drift after one-day gains, and reading the drift tables).
- **Cyclicals and banks.** For a cyclical, the quarter's margin against the mid-cycle margin before a beat is read as a run rate. For a bank, net interest margin, provisions against charge-offs and reserve coverage in place of working capital, and price to book against return on equity in place of enterprise-value multiples.

## Where it goes wrong

- **A risk-free rate taken from memory** when the country data has the yield.
- **Prior guidance from the press.** Press summaries round ranges and drop dates; the earlier call is the source.
- **A surprise split the company did not disclose.** An estimated split reads as the company's own; say the split is not disclosed.
- **Drift history quoted for a move under 10 percent** or over several days. It is outside the population.
- **Consensus before and after shown twice.** It belongs once, in the outlook comparison.
- **One year of ROIIC read as a change in the outlook.** A single year can be operating leverage; five annual periods allow a three-year figure.
- **Citations assembled at the end.** The link goes next to each figure and quote as it is captured.

## What the data has, and does not

The latest-earnings record covers one quarter against consensus; the surprise record for earlier quarters comes from the estimates actuals or from the results releases of the prior two to four prints. Consensus is a snapshot with its date and estimate count and no history, so the before-the-print figures come from research and news dated before the release; where none is found, the note says so. The release and the call for the latest quarter carry next quarter's guidance; the prior call carries the guidance being replaced; both are found with fiscal year and quarter fixed. If the transcript is not yet in, the note is written from the release and says so; if the quarterly filing is not out, cash flow and provisions wait for it. Revisions, target and rating changes since the release come from dated research and news. Quarterly statements and segments for the quarter and the year-ago quarter; five fiscal years of annual statements for the three-year ROIIC. The event-day abnormal return and a 60-month beta need daily prices for the stock and its index; the quote carries standard windows only. The risk-free rate is in the country data. The next earnings date is in the corporate calendar; an investor day, regulatory decision or maturity the call named comes from the call and filings. A company whose results are not yet out belongs to the preview. Sector metrics and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Nike's beat was inventory release; the guide cut is the news"), not the event. The opening gives the result against the bar, what made it, whether the long-term outlook moved and what the reaction prices, in plain sentences the reader can act on. The results against consensus and guidance and the prior and new guidance come next, because everything else rests on them; then the body follows the question. The next date and what would change the reading close the note. Sub-headings state the finding, never the step that produced it.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- The premise was checked against the release, and the prior guidance is quoted from the earlier call with its date beside the new range.
- Every number in the opening agrees with the body, and the net debt or enterprise value used anywhere equals the inputs stated once.
- Whether the long-term outlook moved, and how each premise fared, are sentences with their evidence; no verdict word stands alone as a label or a bolded category.
- Drift history appears only if the one-day move against the index was 10 percent or more, and the scenarios, if any, have one cut-off per metric.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
