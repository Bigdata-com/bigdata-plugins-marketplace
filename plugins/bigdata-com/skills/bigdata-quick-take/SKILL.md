---
name: bigdata-quick-take
description: >-
  A one-page view on a stock from Bigdata.com data: what the price implies, the three drivers that
  matter now, the risks and what would change the view, and the next dated catalyst. Use when the
  user asks for a quick take, thoughts on a ticker, whether a stock is interesting, or a fast view
  on a name. Not for a full thesis or model, which bigdata-deep-dive and bigdata-valuation cover.
  It gives no buy or sell call.metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Quick take

One page, written the way a portfolio manager answers "what do you think of Micron" in a morning meeting: what the price already assumes, the three things that decide whether it is right, the two or three ways it goes wrong, and the next date that tells. Short does not mean loose: every number is sourced, the expectations arithmetic is shown, and the page says what would change the reading. It gives no rating.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not give a view from memory or the web.
- Pass `plugin_slug: "bigdata-quick-take"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. The page is the limit; the research behind it is not.

## Scope the request

Resolve the company with `find_securities`. If the user gave an angle ("is it interesting after the drop", "versus Samsung"), the page answers that angle. Do not ask a question unless the name is ambiguous; a quick take is asked for because the user wants it now.

If the company is Private, say that there is no price to read expectations from and offer a document-based summary instead.

## Gather

Four calls, no more unless a driver needs one.

1. `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, latest_earnings, events_calendar, estimates, fundamentals`. Done when market cap, enterprise value, the forward multiples, consensus for the next two fiscal years with 30-day changes, the last print's surprise, targets and ratings, the next report date, and the latest statements are in hand.
2. `bigdata_search` for the company's news over the last 30 days. Done when the two or three developments that moved the stock or the estimates are known with dates.
3. `bigdata_search` for the last earnings call, with the reporting period filter, and `bigdata_fetch_document` on it. Done when guidance and the one exchange that shows what management is worried about are known.
4. `bigdata_sentiment_tearsheet` for 90 days. Done when the direction of sentiment is known.

If the company is in a sector with a section in `references/sector-primers.md`, read the primer's "metrics that matter" section so the drivers are the sector's drivers.

## Analyse

1. **What the price implies.** From `references/expectations.md`: the forward P/E against the steady-state P/E (one over the cost of equity, stated as an assumption with its basis); the growth in NOPAT that the enterprise value implies at a stated cost of capital, against consensus growth; the share of the value that is steady state and the share that is future value creation. Then the base-rate sentence for consensus growth from `references/base-rates.md`. Done when the page can say in two sentences whether the price assumes a lot or a little, and whether consensus sits in a common or a rare part of its reference class.

2. **The three drivers.** The three things that decide whether the price-implied path is beaten or missed, in order of weight. For each: what consensus assumes, the latest evidence with its date and source, which way the risk runs. Use the value-trigger rule: where the company earns near its cost of capital the driver is incremental return, where it earns well above it is sales growth. Done when each driver has one dated piece of evidence.

3. **The risks.** Two or three, from `references/downside-and-catalysts.md`: the one that breaks the drivers, the one in the balance sheet or the accounting if there is one, the one from outside (regulation, a customer, a technology). Each with a sentence on how it would show up first. Done when each risk has an observable early signal.

4. **The next date.** The next earnings date from the calendar, plus any other dated event from the news (a product cycle, a regulatory decision, a capital-markets day). Done when the page names a date.

## Write

Follow `references/output-standard.md`. The whole page:

```
# <Company> (<ticker>) quick take, <date>
Data as of: price <date>; estimates <date>; latest statements <period>.

## The view
Three to five sentences in prose. What the price implies, whether the evidence supports it,
and what would change the reading. No rating word.

## What the price implies
| Measure | Value | Basis | Source |
Forward P/E, steady-state P/E at the stated cost of equity, implied NOPAT growth at the stated
cost of capital, consensus growth, base-rate share for that growth, 30-day estimate revision,
target range against price.

## The three drivers
Three short paragraphs, each: assumption, evidence with date, direction of risk.

## Risks and what would change the view
Two or three risks with their early signals, then one line on what would make the view more
positive and one on what would make it more negative.

## Next date
The event and the date.

## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one page. The assumptions (cost of equity, cost of capital) appear once, in the table, with their basis.

## Checks before sending

1. It fits on one page.
2. The expectations table has the steady-state P/E, the implied growth and the base-rate sentence, each labelled derived or assumed.
3. Three drivers, each with dated evidence from Bigdata.com.
4. Each risk has an early signal.
5. A dated next event.
6. No buy, hold, sell, overweight, underweight, interesting-at-this-price, or rating language. "Interesting" is answered with what the price assumes and what the evidence says.
7. Every figure has a source number or a Basis label.

## Hand-offs

- The user wants the thesis built out: `bigdata-thesis`. The full report: `bigdata-deep-dive`. The valuation range: `bigdata-valuation`.
- The user asks why it moved today: `bigdata-stock-move`.
- After delivering, make one offer: add the company to a Bigdata.com watchlist. Act only on a clear yes.
