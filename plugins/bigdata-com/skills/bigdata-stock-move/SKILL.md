---
name: bigdata-stock-move
description: >-
  Why a stock moved: the trigger, headline vs change in the long-term outlook, revisions, base
  rates for what follows a move that size. Use for why is X down, why did our stock drop, what
  moved it. Not the quarter: bigdata-earnings-review.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, expectations, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Stock move

This skill answers "why is it down" the way a portfolio manager wants it answered: the trigger with its source, then whether the move reflects a change in the company's long-term outlook or a one-quarter headline, then what the people who set the price did next (estimates, targets, ratings), and then what history says follows a move like this, conditioned on the things that matter. It does not say whether to buy the dip.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-stock-move"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A move explained by one filing needs one section, not six.

## Scope the request

Resolve the company with `find_securities`. Fix the window: the day the user names, today if they say "today", the week if they say "this week". If the user names no window, take the largest one-day move in the last five trading days from the daily series in `bigdata_computer`. Confirm the size of the move from the price series before explaining it, because a user's "down 10 percent" is sometimes 4 percent after a partial recovery. The reader may be a holder, an analyst or the company's own IR team asking why its stock moved; the evidence is the same, and the note says what the move means for that reader.

Ask one question only when the ticker is ambiguous. Otherwise state the window and the move in the header. Done when the company is resolved and the window and the size of the move are fixed from the price series.

## Gather

1. **Prices and the tearsheet.** `bigdata_computer` on the daily series of the stock and its index (the S&P 500 or the home-market index, stated) for the window and the 30 trading days before it, so the stock and the index are compared over the exact window and the pre-event price is known. Then `bigdata_company_tearsheet` in two calls: `company_overview, analyst_ratings, latest_earnings, earnings_calendar, analyst_estimates`, then `financial_statements, financial_ratios, key_metrics` with `interval` annual. The competitors block in `company_overview` gives the peer set for step 5 and for the proxies. Done when the stock and index moves over the window, the pre-event price, the current consensus and target with their vintage, the rating counts, the peers, the last report date and the next one are in hand.
2. **The trigger.** `bigdata_search` for news on the company in the window, then a second search for the company's own filings and releases in the window (8-K, pre-announcement, guidance change, management change, financing). Done when the earliest dated item that explains the move is identified, with its source, or the search shows no company-specific item.
3. **Sell-side, before and after.** `bigdata_search` for research and news that quote analyst reactions in the window (target changes, rating changes, estimate cuts), then a second search for the consensus and mean target quoted in documents from the 13 weeks before the event, since the tearsheet carries no history. Done when the before and after figures are listed with the date of the document each came from, labelled press or research summaries, or marked as none found.
4. **If the trigger was earnings.** `bigdata_fetch_document` on the transcript and the release. Done when guidance and the exchange that moved the stock are quoted.
5. **Peers and the sector, every time.** `bigdata_portfolio_tearsheet` on the peers from step 1 for their move over the same day or window, and a `bigdata_search` on the sector for the window (a peer's print, a regulatory action, a macro release, a rotation). The move splits into the part the peers shared and the part specific to the company. Done when the peer and sector moves are tabled and the company-specific part is stated, or the move is recorded as unexplained.
6. **Sentiment.** `bigdata_sentiment_tearsheet` (it takes no window; its narrative covers recent coverage). Done when the direction of coverage around the event is known and cited.
7. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, then read to the next `## ` heading) and read its metrics that matter and its accounting traps, so the trigger is read on the sector's own drivers (a bank on net interest income and provisions, a software company on net retention and billings). Done when the sector's two or three decisive metrics are noted.

## Analyse

1. **Classify the event.** From `references/after-a-price-move.md`: the move relative to the index (the stock's return minus the index's, and the beta-adjusted figure computed with `bigdata_computer` as the file's formulas 1 to 3 set out, stating which one is used), the part shared with the peers from Gather step 5, whether the trigger was an earnings release or something else, and whether the move is one day or several. Done when the note states "a one-day move of X percent against the index, earnings-driven" or its equivalent.

2. **Separate the headline from the long-term outlook.** The price capitalises years of cash flow, so a large move is the market revising its view of the company's long-term growth, margins or returns, not reacting to one quarter. State which of the three the trigger changes and by how much, from the evidence: a guidance cut that lowers the growth path, a margin disclosure that resets the steady state, a capital raise that dilutes the per-share claim, a regulatory action that shortens the competitive advantage period. If the trigger changes none of them (a headline with no change in the outlook), say so and say what the move then implies. `references/expectations.md` gives the implied-growth arithmetic: compare the growth the enterprise value implied before the move with the growth it implies after, at a stated cost of capital. Done when the note has one paragraph that says what the market changed its mind about, with the arithmetic labelled derived.

3. **What the estimate-setters did.** Consensus for the next fiscal year and the mean target before the window (from the dated documents in Gather step 3) and after it (the tearsheet snapshot with its vintage), the number of target changes and their direction, the rating changes. The reading: price down with estimates down is a fundamental revision; price down with estimates flat is a multiple or positioning move; price down with estimates up is unusual and worth saying. Done when the three quantities are tabled with the date and source of each, or the before figures are marked not found.

4. **Condition the base rates.** The tables in `references/after-a-price-move.md` cover one-day moves of 10 percent or more against the index: table 1 for drops, table 2 for gains. Pick the row for the event type and the company's momentum state, step down to valuation and quality only while N stays at about 50 or more, and quote N, the sample period, the event-day move and the cumulative abnormal return at 30, 60 and 90 days, as a historical average (verify), not a forecast. For a smaller or multi-day move, say the tables do not cover it and skip the row. Momentum, valuation and quality are proxied as the reference file sets out and scored as they stood before the event: the 52-week price performance relative to the sector, excluding the event, plus the 13-week revisions and target changes from Gather step 3 for momentum; forward P/E, EV/EBITDA, free cash flow yield and price to book re-based to the pre-event price (the file's formula 4) against the peers from Gather step 1 for valuation, so a stock is never scored cheap because it just fell; the FactSet ROIC level against those peers, its spread over an assumed cost of capital and the five-year margin history for quality. Each proxy is labelled derived and the note says that the original study used HOLT scores that Bigdata.com does not carry. Done when the row is quoted with its sample, period and parent row, and the three proxies are stated, or the note says the move is outside the tables.

5. **The downside and the catalysts from here.** From `references/downside-and-catalysts.md`: who is likely selling and why (forced sellers after an index change or a rating downgrade, holders who owned it for the thing that just broke), read from the filings and news in the window and from `fund_trends_history` with the caveat that 13F data is quarterly and lagged; what the floors are (net cash, asset value, and a private-market value only where a dated transaction gives one); and the next dated event that resolves the question the move raised. Done when the note names the next date and the floor, or says neither exists.

A full note carries steps 1 to 5; step 4 is read from `references/after-a-price-move.md` in this run, never from memory. When the move is under the 10 percent the tables cover, or spread over several days, step 4 says the tables do not cover it and quotes the nearest row as context only, labelled out of sample. Moves with no identifiable trigger get steps 1, 3 and 4, and the note says the trigger was not found in Bigdata.com.

## Write

Follow `references/output-standard.md`.

```
# <Company> (<ticker>): <direction> <X> percent on <date or window>, <Y> percent against <index>
Data as of: prices <date>; estimates <date>; newest document <date>.

## What happened
Four to six sentences: the trigger with its source and time, what the market changed its mind
about, what the estimate-setters did, and what history says about the next three months for
this kind of move. No rating.

## The trigger
Timeline table: time or date, event, basis, source. Then the quote that matters, if there is one.

## Headline or outlook
The paragraph from step 2, with the implied-growth figures before and after labelled derived.

## What the estimate-setters did
| Measure | Before | After | Change | Date | Basis | Source |
Rows: next-year consensus sales and EPS, mean target, rating counts, notable target changes.

## What history says
The base-rate row with N, the event-day move and the 30, 60 and 90-day abnormal returns,
the three conditioning proxies with their values and basis, and one sentence of caution on
the sample. No buy or sell sentence.

## Floors and the next date
Who is selling, the floor if one exists, the next dated event.

## What would change this reading
Two to four observable conditions.

## Gaps
Short interest, option prices and intraday flows are not in Bigdata.com, and 13F positioning is quarterly; say so when they matter. Pre-event consensus and targets come from dated documents, or are marked not found.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one to two pages. A user who asks only "what happened to X today" gets the first three sections and the sources, with the base-rate row reduced to one sentence inside "What happened".

## Checks before sending

1. The move, the index move and the peer move over the same window come from the price series, not from the user's number, and the valuation proxies are re-based to the pre-event price.
2. The trigger has a source and a time, or the note says none was found.
3. The headline-versus-outlook paragraph names which of growth, margin, return or duration changed, or says none did.
4. The base-rate row is quoted with N, period and sample as a historical average, the proxies are labelled derived, and a move the tables do not cover is labelled out of sample.
5. No sentence recommends buying, selling, adding or trimming; the base rates condition a view, they do not make one.
6. Every figure has a Basis label and a source number, and every before-the-event consensus or target figure names the dated document it came from.
7. The next dated event is named with its date, or its absence is stated.

## Hand-offs

- The move was the earnings print and the user wants the full quarter: `bigdata-earnings-review`.
- The user wants the catalysts beyond the next date: `bigdata-catalysts`.
- The user wants a view on the stock after the move: `bigdata-quick-take`, which can reuse this note's implied-growth arithmetic.
- After delivering, make one offer: a monitor on the company's news for the next two weeks. Act only on a clear yes.
