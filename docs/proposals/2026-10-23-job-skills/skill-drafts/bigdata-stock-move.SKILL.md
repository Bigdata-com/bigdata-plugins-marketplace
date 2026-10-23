---
name: bigdata-stock-move
description: Why a stock moved, from Bigdata.com news, filings, transcripts and the tearsheet: the trigger, what changed in the long-term outlook as opposed to the headline, estimate and target revisions, and the historical base rates for what follows a move of that size and kind. Use when the user asks why a stock is up or down, what happened to a ticker today, or what drove a share price this week. Not for a quarter's results in full, which bigdata-earnings-review covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, expectations, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Stock move

This skill answers "why is it down" the way a portfolio manager wants it answered: the trigger with its source, then whether the move reflects a change in the company's long-term outlook or a one-quarter headline, then what the people who set the price did next (estimates, targets, ratings), and then what history says follows a move like this, conditioned on the things that matter. It never says whether to buy the dip.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not explain the move from memory or the web.
- Pass `plugin_slug: "bigdata-stock-move"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A move explained by one filing needs one section, not six.

## Scope the request

Resolve the company with `find_securities`. Fix the window: the day the user names, today if they say "today", the week if they say "this week". If the user names no window, take the largest move in the last five trading days from `price_performance`. Confirm the size of the move from the tearsheet before explaining it, because a user's "down 10 percent" is sometimes 4 percent after a partial recovery.

Ask one question only when the ticker is ambiguous. Otherwise state the window and the move in the header.

## Gather

1. **Tearsheet.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, latest_earnings, events_calendar, estimates, fundamentals`. Done when the move over the window, the index move over the same window, the consensus with its 30-day change, the target and rating counts, the last report date and the next one are in hand.
2. **The trigger.** `bigdata_search` for news on the company in the window, then a second search for the company's own filings and releases in the window (8-K, pre-announcement, guidance change, management change, financing). Done when the earliest dated item that explains the move is identified, with its source, or the search shows no company-specific item.
3. **Sell-side and holders.** `bigdata_search` for research and news that quote analyst reactions in the window (target changes, rating changes, estimate cuts). Done when the revisions are listed with dates, or marked as none found.
4. **If the trigger was earnings.** `bigdata_fetch_document` on the transcript and the release. Done when guidance and the exchange that moved the stock are quoted.
5. **If no company-specific trigger.** Search the sector, the peers and the market for the window (a peer's print, a regulatory action, a macro release, a rotation). Done when the move is attributed to a sector or market factor with evidence, or recorded as unexplained.
6. **Sentiment.** `bigdata_sentiment_tearsheet` for the last 30 days. Done when the direction before and after the event is known.

## Analyse

1. **Classify the event.** From `references/after-a-price-move.md`: the move relative to the index (the stock's return minus the index's), whether the trigger was an earnings release or something else, and whether the move is one day or several. Done when the note states "a one-day move of X percent against the index, earnings-driven" or its equivalent.

2. **Separate the headline from the long-term outlook.** The price capitalises years of cash flow, so a large move is the market revising its view of the company's long-term growth, margins or returns, not reacting to one quarter. State which of the three the trigger changes and by how much, from the evidence: a guidance cut that lowers the growth path, a margin disclosure that resets the steady state, a capital raise that dilutes the per-share claim, a regulatory action that shortens the competitive advantage period. If the trigger changes none of them (a headline with no change in the outlook), say so and say what the move then implies. `references/expectations.md` gives the implied-growth arithmetic: compare the growth the enterprise value implied before the move with the growth it implies after, at a stated cost of capital. Done when the note has one paragraph that says what the market changed its mind about, with the arithmetic labelled derived.

3. **What the estimate-setters did.** Consensus for the next fiscal year before and after the window, the number of target changes and their direction, the rating changes. The reading: price down with estimates down is a fundamental revision; price down with estimates flat is a multiple or positioning move; price down with estimates up is unusual and worth saying. Done when the three quantities are tabled with dates.

4. **Condition the base rates.** From the Man Overboard tables (drops of 10 percent or more against the index, January 1990 to June 2014) or the Celebrating the Summit tables (gains of 10 percent or more, January 1990 to July 2015) in `references/after-a-price-move.md`, pick the row for the event type and the company's momentum state, and quote N, the event-day move and the cumulative abnormal return at 30, 60 and 90 days. Momentum, valuation and quality are proxied from the tearsheet as the reference file sets out: estimate revisions and the 90-day price move for momentum; forward P/E and EV/EBITDA against the sector and the company's own five-year range for valuation; the FactSet ROIC and margin history for quality. Each proxy is labelled derived and the note says that the original study used HOLT scores that Bigdata.com does not carry. Done when the row is quoted with its sample and period and the three proxies are stated.

5. **The downside and the catalysts from here.** From `references/downside-and-catalysts.md`: who is selling and why (forced sellers after an index change or a rating downgrade, holders who owned it for the thing that just broke), what the floors are (net cash, asset value, private-market value where it applies), and the next dated event that resolves the question the move raised. Done when the note names the next date and the floor, or says neither exists.

Moves under 5 percent against the index get steps 1 to 3 only, in a page. Moves with no identifiable trigger get steps 1, 3 and 4, and the note says the trigger was not found in Bigdata.com.

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
Timeline table: time or date, event, source. Then the quote that matters, if there is one.

## Headline or outlook
The paragraph from step 2, with the implied-growth figures before and after labelled derived.

## What the estimate-setters did
| Measure | Before | After | Change | Date | Source |
Rows: next-year consensus sales and EPS, mean target, rating counts, notable target changes.

## What history says
The base-rate row with N, the event-day move and the 30, 60 and 90-day abnormal returns,
the three conditioning proxies with their values and basis, and one sentence of caution on
the sample. Never a buy or sell sentence.

## Floors and the next date
Who is selling, the floor if one exists, the next dated event.

## What would change this view
Two to four observable conditions.

## Gaps
Short interest, options and intraday flows are not in Bigdata.com; say so when they matter.

## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one to two pages. A user who asks only "what happened to X today" gets the first three sections and the sources.

## Checks before sending

1. The move and the index move over the same window come from the tearsheet, not from the user's number.
2. The trigger has a source and a time, or the note says none was found.
3. The headline-versus-outlook paragraph names which of growth, margin, return or duration changed, or says none did.
4. The base-rate row is quoted with N, period and sample, and the proxies are labelled derived.
5. No sentence recommends buying, selling, adding or trimming; the base rates condition a view, they do not make one.
6. Every figure has a Basis label and a source number.
7. The next dated event is named with its date, or its absence is stated.

## Hand-offs

- The move was the earnings print and the user wants the full quarter: `bigdata-earnings-review`.
- The user wants the catalysts beyond the next date: `bigdata-catalysts`.
- The user wants a view on the stock after the move: `bigdata-quick-take`, which reads this note's "what is priced in" arithmetic.
- After delivering, make one offer: a monitor on the company's news for the next two weeks. Act only on a clear yes.
