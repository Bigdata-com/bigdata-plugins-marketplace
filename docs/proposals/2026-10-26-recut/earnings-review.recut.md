---
name: bigdata-earnings-review
description: >-
  After a company reports: results vs consensus and guidance, what changed in the outlook, thesis
  check, reaction, peer read-across. Use for how did X do, beat or miss, a competitor's print. Not
  the setup: bigdata-earnings-preview.
---

# Earnings review

This skill writes the note the morning after a print: results against consensus and guidance, what made the beat or miss, the guidance change and what management stopped saying, whether the long-term outlook moved, the thesis check or the Street's reception, the quality of the quarter, the reaction, the read-across to peers, and the next date. It sizes to the question: "did Nike beat" gets the results table and the guidance line; "give me a reaction note" gets the short form; "analyse Nike's quarter" gets the full review. A portfolio manager with a thesis wants it tested against the quarter. A supplier, customer, competitor or the company's own investor-relations team wants what the print means for their business, and their questions set the order of the note; the valuation refresh and the thesis vocabulary are for the investor reader. No rating, no action.

## Before starting

- If the Bigdata.com tools are not available, say so and ask the user to connect the Bigdata.com connector. Give no figures from memory in the meantime; an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-earnings-review"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need below to a tool, with fallbacks when a tool is missing. Read it before the first call. Open the method files named below when a step needs more than this page gives.

## Scope

Settle the company, the quarter (the latest reported one unless the user names another, confirmed from the latest-earnings record), and the form: a reaction note when the user asks for a reaction or "does it change the thesis" in a sentence, the full review otherwise. Settle the reader: a thesis stated by the user is tested; "does it change the thesis" with none stated tests the prevailing bull and bear cases from the preview-period research, labelled as the Street's; a corporate reader gets "how the Street received it" instead of a thesis check, and the implications for their business. Check the premise of the question against the release before building on it: "GM lowered its 2026 outlook" was a narrowed range with the midpoint unchanged, and the note says so plainly. If the company has not reported yet, hand off to `bigdata-earnings-preview`; if the transcript is not yet in Bigdata.com, write from the release and say so.

## Gather

1. **The company's numbers.** Profile and quote; the latest quarter against consensus and the next report date; consensus with its vintage, ratings and targets; quarterly statements and segments for the quarter and the year-ago quarter; five fiscal years of annual statements (annual interval) for the three-year rolling ROIIC. For the surprise record, the actuals the consensus data gives for past quarters, or searches for the prior two to four prints, with the count noted.
2. **The release and the call for the quarter reported**, with the period fixed rather than inferred: the reported figures, segments and KPIs, the new guidance quoted with its ranges, the non-GAAP reconciliation, and the Q&A exchanges that bear on the drivers.
3. **The guidance it replaces.** The full transcript of the previous quarter's call, fixed to that quarter: it carries the guidance being replaced. Annual guidance may have been set earlier in the year and updated since. Never take the prior guidance from memory or from the press.
4. **The quarterly filing, if out.** Cash flow, working capital, provisions and any accounting or segment change for the quarter and the year-ago quarter.
5. **The Street's reaction.** Two or three searches since the release, one aspect each: revisions and target changes, rating changes, the reasons analysts and the press gave for the move, each dated and labelled press or research summary.
6. **Peer read-across.** One or two searches for what competitors, suppliers and customers said about the print or about the same driver.
7. **The price reaction.** Daily prices for the stock and its index over the event day and the 60 months before it, so the event-day return, the index return, beta and the abnormal return are computed rather than estimated.
8. **Consensus before the print.** The estimates feed has no history, so search research and news dated before the release for the FY+1, FY+2 and long-term growth figures, labelled as press or research summaries, or mark each not found.
9. **The sector primer.** The company's sector in `references/sector-primers.md`: the metrics that matter and the accounting traps. A bank's or insurer's tables follow the primer's lines.

## Analyse

1. **Results against consensus and guidance.** For sales, gross margin, EBIT or EBITA and its margin, EPS, free cash flow and the sector's key operating metric: the actual, consensus with its vintage and estimate count, the surprise, the guidance range and the actual against its midpoint, the change on the prior year. Place the surprise against the company's own record over the quarters found, so the reader sees whether this one is large for this company. A metric the company does not guide gets no guidance cell; a figure the data could not give goes under Gaps.
2. **What made the beat or miss** (`references/earnings-quality.md`, the quarter against the year-ago quarter). Decompose the surprise only as far as the company discloses it: segments, its own bridge, the tax rate, the share count, below-the-line items. Where there is no split, say so; never estimate one. Label each part recurring or one-time, and say which way cash disagreed with earnings.
3. **Prior guidance against new.** One row per guided metric: the prior range with its date, the new range, the change at the midpoint, consensus before the call for the same period. If the company guides one quarter, state what the change implies for the year. Then compare the language with the prior call: which metrics or KPIs management stopped reporting, which claims it dropped or softened, whether the Q&A turned more defensive. Dropped disclosures are a quality signal.
4. **Whether the long-term outlook changed** (`references/after-a-price-move.md`, the headline-versus-outlook questions; `references/expectations.md` for implied growth). The price capitalises many years of cash flow, so the question is whether the quarter changed them: consensus before and after, the three-year rolling ROIIC, and the perpetual growth the enterprise value implied before and after the print at a stated cost of capital labelled assumed. Classify the quarter as a change in the long-term outlook, a short-term event, or unclear, and say whether the size of the move matches the change in long-term cash flow.
5. **The thesis check, or how the Street received it** (`references/forecasting-discipline.md`). With a thesis: list its premises, tag each piece of evidence from the quarter as fact or opinion, test any kill criteria against their thresholds, and give each premise one word, intact, strengthened, weakened or broken; the thesis takes the word of its weakest load-bearing premise. One quarter's noise does not break a multi-year thesis, and a guidance cut on the linchpin driver is not noise. Without a thesis: the revisions, target and rating changes and the reasons given, dated.
6. **Estimate and valuation refresh**, for the investor reader: targets before and after, forward P/E, EV/EBITDA and free cash flow yield on the old and the new consensus, the implied growth from step 4; where the outlook changed, three scenarios re-weighted from a reference class rather than a default split. No price target of the note's own.
7. **Quality signals for the quarter.** Cash from operations against net income, receivable and inventory days, deferred revenue against revenue growth where it applies, one-off items and whether that type recurred, reserve releases, stock compensation against revenue, guidance credibility over the quarters found. Each row: this quarter, the year-ago quarter, the direction, and the threshold next quarter that would turn noise into a flag.
8. **The market reaction** (`references/after-a-price-move.md`). The event-day move against the index, simple and beta-adjusted, decomposed into fundamental news, a change in the multiple, and flows. For a move of 10 percent or more against the index in one day, the base-rate row with its sample and period, called historical. Under 10 percent the published samples do not apply; stop at the decomposition.
9. **Peer read-across.** What the print says for competitors, suppliers and customers (a price rise rivals can follow, a demand comment that reaches the supply chain), set against what they said, facts and opinions kept apart.
10. **The next date**, from the calendar, plus any dated event the call named: an investor day, a guidance update, a launch, a regulatory decision, a maturity.

For a cyclical, show the quarter's margin against the mid-cycle margin before reading a beat as a new run rate. For a bank, replace the working-capital tests with net interest margin, provisions against charge-offs and reserve coverage, and the EV multiples with price to book against return on equity.

## Write

Follow `references/output-standard.md`. Lead with the result against consensus and guidance, what made it, the guidance change, whether the long-term outlook moved, the thesis word or the Street's reception, the reaction, and the next date, in four to eight sentences, in the reader's terms. The results table and the guidance table come next, because everything else rests on them. Then the sections the question needs, in the order the question asked them: for a thesis holder, the thesis check, the valuation refresh, quality signals, the reaction, the read-across; for a supplier, customer or competitor, what the print means for their business, then the Street's reception and the read-across, with the investor sections left out unless asked. A row exists only where there is a figure. A reaction note is the results table, the guidance table and the thesis or Street line, two or three sentences each. The full review runs two to four pages.

## Checks before sending

1. The premise of the question was checked against the release, and the note says so where it did not hold.
2. The prior guidance is quoted from the earlier call with its date, next to the new range.
3. Consensus carries its vintage and estimate count, and the before-the-print figures are dated before the release.
4. The surprise is split only as far as the company disclosed it, each part labelled recurring or one-time.
5. The base-rate row appears only for a one-day move of 10 percent or more against the index.
6. Every number in the opening agrees with its table, nothing in a corporate reader's note serves only an investor, and there is no rating, target or action.
