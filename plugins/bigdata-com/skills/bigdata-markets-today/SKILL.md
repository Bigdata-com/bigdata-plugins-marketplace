---
name: bigdata-markets-today
description: >-
  Market wrap for a day, week or month: what moved across indexes, sectors, rates and currencies,
  the news behind it. Use for what happened in markets, why everything is red, a morning briefing.
  Not one company: bigdata-stock-move.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, forecasting-discipline
  bigdata-sector-primer: none
---

# Markets today

This skill writes the market wrap a portfolio manager reads before the open or after the close: what moved across asset classes over the window and by how much, why, with each reason tied to a source, what is scheduled next and what each release would test, and one paragraph on what the window means for the questions a book would ask about its positioning. It gives no trade, allocation or rotation call. "Why is the market down today?" gets the moves, the reasons and the sources in a few paragraphs, not the full wrap.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-markets-today"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the window needs it.

## Scope the request

Fix three things from the request before gathering data.

- **The window.** Today, this week or this month, mapped to the market tearsheet's 1D, 5D and 1M columns. These are trailing windows: 5D is the last five trading days, not week-to-date, and 1M is the trailing month, not month-to-date. When the user's window and the column differ, say which one the wrap uses in the header and note the difference in the Gaps line. The tearsheet is a snapshot as of now: a past date or window ("how did markets do last Tuesday", "the week of the Fed meeting") comes from daily series of the indexes, yields and assets the wrap needs, computed, not estimated, and from searches dated to that window for the reasons, and the header says so.
- **The region.** Global by default, with the US first, then Europe and Asia-Pacific. If the user names a region or a market ("European close", "how did Japan do"), lead with it and keep one line on the others.
- **The angle.** If the user asks why the market moved, the "Why" section carries the answer and the rest is short. If they ask about one asset class (rates, oil, crypto), the wrap centres on it.

A morning briefing before the US open reads the US 1D column as the previous session; lead with the Asia-Pacific and European sessions and say that US cash markets have not opened.

Do not ask a question unless the region is unclear and the answer changes the wrap. State the window, the region and the time the data was pulled in the header. If a market was still trading when the data was pulled, say so, because the 1D column then reads a session in progress. Done when the header states the window, the region and the pull time.

## Gather

1. **Market tearsheet.** The current market snapshot across asset classes, in one pull. Done when the window's moves are in hand for the major indexes (including the VIX), the US sector ETFs, the equity factor ETFs, the Treasury yields (changes in percentage points; convert to basis points), the currency pairs and crypto, the commodities and the bond ETFs. Use the Major Indexes rows for index moves; use the country ETF rows only for markets the index list does not cover, and label them as US-dollar ETF proxies, since their return includes the currency. The factor ETF rows are returns relative to the S&P 500, not absolute returns; read and label them that way. The yield rows are US Treasuries only: take a non-US yield (Bunds, gilts, JGBs) from a dated search result, or put it in the Gaps line.
2. **Macro releases in the window.** The economic calendar over the window's dates, for the regions in scope, high- and medium-impact releases. Done when each release that landed in the window is listed with its period, actual, consensus and previous figure, so the surprise is a reported fact rather than a commentator's word.
3. **The reasons.** One search per move worth explaining, in the user's time words: the main equity move ("Why did US stocks fall today?"), then each outlier in rates, currencies, commodities, crypto or a sector, then any central bank decision or speech in the window. Done when every row the wrap will discuss has a sourced reason, or a note that the searches found none. A reason that names no source does not go in the wrap.
4. **Companies that moved the index.** A search for the stocks that led or lagged the main index in the window, and the earnings calls on the corporate calendar over the window to see which large companies reported. Done when the two or three company stories behind the index move are named with sources, or the move is shown to be broad.
5. **What is scheduled next.** The economic calendar for the next five trading days (or the next week or month, matching the window), high- and medium-impact releases, and the earnings calls on the corporate calendar for the same period in the regions in scope. Done when the next high-impact releases have dates, periods and consensus figures, and the reports from the largest companies and from companies tied to the window's story are picked out.
6. **Only if the user asks about one economy.** The country's economic profile for the growth, inflation and rates context. Done when the economy's growth, inflation and policy rate are in hand with their dates.

## Analyse

1. **Rank the moves.** Within each asset class, order the rows by the size of the move over the window, in the right unit: percent for prices, basis points for yields. A move is worth a sentence when it is the largest in its group, when it reverses the direction of the trailing month, or when it breaks from the rest of its group (one sector up while the index falls). Those three tests are this skill's convention, labelled judgment. Done when the wrap has its five to ten rows that matter, plus the benchmark rows the reader expects: the main index in each region, the US 2-year and 10-year yields, EUR/USD and USD/JPY, Brent or WTI, gold and bitcoin.

2. **Attribute each move, facts apart from opinions.** From `references/forecasting-discipline.md` rule 1: a data release with its actual against consensus, a central bank decision, a company's reported result and a filed deal are facts; a strategist's or a reporter's explanation of why the market moved is an opinion and is written as "attributed by [source] to ...". People invent a cause for any effect (`references/forecasting-discipline.md` rule 6 and the introduction of `references/after-a-price-move.md`), so when no source links a move to a cause, write "no cause established in the sources reviewed" rather than supplying one. Done when every reason in the wrap is tagged fact or attributed opinion, with its source.

3. **Check that the story fits across assets.** A reason should explain more than one row. A rates story should show in yields, the dollar and the growth and value factor spread; a growth scare should show in cyclical sectors, commodities and the yield curve; a risk-off day should show in the VIX and in credit ETFs (high yield against investment grade). When the assets disagree with the stated reason, say so. Done when each main reason is shown to be consistent or inconsistent with the cross-asset pattern, labelled judgment.

4. **Separate fundamentals, the discount rate and flows.** From `references/after-a-price-move.md` rule 2: an index move is news about earnings, a change in the rate at which the market discounts them, or supply and demand from flows (index rebalancing, options expiry, quarter-end, a mandate constraint). Name flows only when a source reports them. Most day-to-day moves are flows and positioning, so a small move with no news is a normal outcome, not a puzzle. Done when the main equity move is assigned to one of the three, or to a stated mix, with the evidence.

5. **Breadth and leadership.** The tearsheet has no equal-weight index and no advance-decline data, so read breadth from what it carries: the number of the eleven US sectors up against down, and the dispersion between the best and the worst sector over the window, in percentage points (derived). Read size separately: the Russell 2000 against the S&P 500 says whether small companies led or lagged, which is a size read, not breadth, and the wrap says so. Then growth against value and momentum against low volatility from the factor rows, which are already relative to the S&P 500. Done when the wrap can say in one sentence whether the move was broad or narrow across sectors, which size led, and which factor carried it, each labelled derived.

6. **Single stocks.** When a company in the index moved 10 percent or more against it, name it, the trigger with its source, and whether it was an earnings release. Do not run the base-rate tables here; that is `bigdata-stock-move`'s job. Done when each such name has one line.

7. **What comes next.** For each high-impact release or report in the next period: the date, the period it covers, the consensus and the previous figure, and the question from this window it answers (a rates move tested by the next inflation print, a growth scare tested by the next payrolls or purchasing-managers data). Done when each item names what it would confirm or contradict.

8. **What it means for positioning questions.** One paragraph, no recommendation. It names the questions a book would ask after this window and what the data says about each: was the move driven by rates, earnings or flows; was it broad or narrow; which factor or sector carried it; which scheduled event is most likely to test it, and what reading would contradict the window's story. It does not say to buy, sell, add, trim, rotate, hedge or over- or underweight. Done when every sentence in it is an observation from the data or a conditional tied to a dated event.

Special cases that change how a row reads:

- Crypto trades every day, so its 1D and 5D columns cover a different span from equities; say so when the wrap compares them.
- A market closed for a holiday shows no move; write that it was closed, not that it was flat.
- Currency pairs move in quote terms: USD/JPY up is a stronger dollar, EUR/USD up a weaker one. Write the move as the currency that strengthened.
- Commodity rows are futures. A large one-day move near expiry can be the contract roll; check a source before explaining it as news.
- The VIX is a level in points; quote the level and the change in points, not only the percent change. The tearsheet gives the percent change, so the change in points is derived from the level and the percent; label it.
- Fixed-income ETF rows move inversely to yields and include credit spread changes; use the yield rows for rates and the ETF rows for credit.

## Write

Follow `references/output-standard.md`. The market tearsheet asks that its data sources be named: put them in the Data line.

```
# Markets <today | this week | this month>: <the main move in a few words>, <date or window>
Data as of: market data <date, time, which markets open or closed>; newest document <date>.
Window: <1D | 5D | 1M>, <how it differs from what the user asked, if it does>.

## What happened
Four to six sentences: the main moves with numbers, the reason for each with its source and
whether it is a reported fact or an attributed opinion, whether the move was broad or narrow,
and the next event that tests it. No call.

## What moved
| Asset | Level | Move over window | Unit | Basis | Source |
Grouped: equity indexes and VIX; sectors and factors; rates; currencies and crypto;
commodities; credit. Benchmark rows first, then the movers that matter. Factor rows are
marked "relative to S&P 500"; the VIX change in points is derived.

## Why
One short paragraph per main move: the reason, fact or attributed opinion, the source, and
whether the cross-asset pattern fits it.
| Release | Period | Actual | Consensus | Previous | Surprise | Basis | Source |
for the macro releases in the window.

## Companies that moved the index
Two or three lines, each with the trigger and the source. Omit when the move was broad.

## What is scheduled next
| Date | Event | Period | Consensus | Previous | What it tests | Basis | Source |

## What it means for positioning questions
One paragraph, observations and dated conditionals only.

## What to watch
Two to four observable conditions, dated where possible.

## Gaps
Intraday prices, flows, positioning and options data, equal-weight indexes and advance-decline
data are not in Bigdata.com; non-US yields not found in search; a window that differs from the
tearsheet's columns; a move with no cause found.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one to two pages. A narrow question ("why is oil up?") gets the row, the reason with its source, the next event that tests it, the sources and the footer.

## Checks before sending

1. Every move comes from the market tearsheet, or for a past window from the daily series, computed, with its unit; yields are in basis points or percentage points, not percent.
2. The window used is stated, and a mismatch with the user's window is in the Gaps line.
3. Index moves come from the Major Indexes rows; any country ETF row is labelled as a US-dollar proxy.
4. Every reason has a source and is tagged fact or attributed opinion; an unexplained move says so.
5. Macro surprises are computed from the calendar's actual and consensus, not taken from a headline.
6. The cross-asset check is stated for each main reason.
7. Each scheduled event says what it would confirm or contradict.
8. The positioning paragraph contains no buy, sell, add, trim, rotate, hedge, overweight or underweight.
9. The Data line names the market tearsheet and calendar as data sets, with the retrieval time.
10. Breadth is read from sector counts and dispersion, the Russell 2000 line is called size, and factor rows are labelled relative to the S&P 500.

## Hand-offs

- One stock's move: `bigdata-stock-move`. One company's news over a window: `bigdata-company-brief`.
- One economy in depth: `bigdata-country`. Several economies side by side: `bigdata-macro-compare`. One sector: `bigdata-sector`.
- After delivering, make one offer: a monitor on the story that drove the window (a central bank, a commodity, a sector), so the user hears when it moves again. Act only on a clear yes.
