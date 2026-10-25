---
name: bigdata-quick-take
description: >-
  One-page view on a stock or company: what the price implies, the drivers that matter now, risks,
  next catalyst. Use for quick take, a one-page read on X, thoughts on a ticker, is X interesting.
  Not a full thesis: bigdata-deep-dive.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Quick take

One page, written the way a portfolio manager answers "what do you think of Micron" in a morning meeting: what the price already assumes, the three things that decide whether it is right, the two or three ways it goes wrong, and the next date that tells. Short does not mean loose: every number is sourced, the expectations arithmetic is shown, and the page says what would change the reading. It gives no rating.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-quick-take"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. The page is the limit; the research behind it is not.

## Scope the request

Resolve the company with `find_securities`. If the user gave an angle ("is it interesting after the drop", "versus Samsung"), the page answers that angle. The subject may be the user's own company, a competitor, a customer or a supplier: the page then says what the price assumes about that company and what it means for the reader, still with no rating. Do not ask a question unless the name is ambiguous; a quick take is asked for because the user wants it now. Done when the company is resolved and any angle the user gave is noted.

If the company is Private, say that there is no price to read expectations from and offer a document-based summary instead.

## Gather

Five steps, no more unless a driver needs one.

1. `bigdata_company_tearsheet` in two calls: `company_overview, analyst_estimates, analyst_ratings, earnings_calendar`, then `financial_statements, financial_ratios, key_metrics` with `interval` annual. Done when market cap, enterprise value, the forward multiples, consensus for the next two fiscal years with its vintage, the last reported quarter's actual against consensus, targets and ratings, the next report date, the competitors block and five fiscal years of statements are in hand.
2. `bigdata_search` for the company's news over the last 30 days, and in the same pass for research and news that quote a consensus or target change over those 30 days (the tearsheet holds no history). Done when the two or three developments that moved the stock or the estimates are known with dates, and the revision is quoted with its document's date, labelled press or research summary, or marked not found.
3. `bigdata_search` for the last earnings call, with the reporting period filter, and `bigdata_fetch_document` on it. Done when guidance and the one exchange that shows what management is worried about are known.
4. `bigdata_sentiment_tearsheet` (it takes no window; say which period its narrative covers). Done when the direction of sentiment and its period are known.
5. **Peers, for one relative-valuation line.** Take two or three peers from the competitors block in `company_overview` (it carries symbol, price and market cap only, and `bigdata_portfolio_tearsheet` carries no multiples) and pull `key_metrics, analyst_estimates` for each with `bigdata_company_tearsheet`. When the user asks for a peer angle, take up to five. Done when each peer has its EV/EBITDA and its forward P/E (price over next-year consensus EPS, derived), or the line says which peers had no data.

Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its metrics that matter, so the drivers are the sector's drivers. Done when the sector's own drivers are noted, or no primer applies.

## Analyse

1. **What the price implies.** From `references/expectations.md`: the forward P/E against the steady-state P/E (one over the cost of equity, formula 1, stated as an assumption with its basis); the perpetual NOPAT growth that the enterprise value implies at a stated cost of capital and a stated incremental return (formula 2), against consensus growth; the share of the value that is steady state and the share that is future value creation (formula 1). The implied growth rests on the assumed incremental return, so state the ROIIC used (the three-year rolling figure from the inputs table, or an assumption) next to it. Then the relative-valuation line: forward P/E and EV/EBITDA against the peers' median from Gather step 5, so the read of the price is not only the steady-state P/E. Then the base-rate sentence for consensus growth from `references/base-rates.md`, from the three-year column for the company's size class (the one-year column is noisy), with its sample and period, called historical. For a bank, use price to book against return on equity; for a cyclical, normalise earnings to mid-cycle and say which margin; for a loss-making company, say the P/E is not meaningful and give the revenue the price needs at a stated margin path. Done when the page can say in two sentences whether the price assumes a lot or a little, and whether consensus sits in a common or a rare part of its reference class.

2. **The three drivers.** The three things that decide whether the price-implied path is beaten or missed, in order of weight. For each: what consensus assumes, the latest evidence with its date and source, which way the risk runs. Use the value-trigger rule (`references/expectations.md`, formula 4), classified on the three-year rolling ROIIC, never one year: near the cost of capital the driver is incremental return, well above it is sales growth. Done when each driver has one dated piece of evidence and a stated direction of risk.

3. **The risks and the downside line.** Two or three risks: the one that breaks the drivers, the one in the balance sheet or the accounting if there is one, the one from outside (regulation, a customer, a technology), each with a sentence on how it would show up first. Then the downside line, which is all `references/downside-and-catalysts.md` asks of a quick take: the price against the floors that apply (net cash, tangible book, a stressed cash-flow value; procedure step 2 and rule 5 for when they do not apply), per share, derived. Done when each risk has an observable early signal and the downside line names its floor or says none applies.

4. **The next catalyst.** The next earnings date from the calendar, plus any other dated event from the news (a product cycle, a regulatory decision, a capital-markets day), written as the file's catalyst output line: type, decider, date and potency. Done when the page names a date and what it decides.

## Write

Follow `references/output-standard.md`. The whole page:

```
# <Company> (<ticker>) quick take, <date>
Data as of: price <date>; estimates <date>; latest statements <period>; newest document <date>.

## The view
Three to five sentences in prose. What the price implies, whether the evidence supports it,
and what would change the reading. No rating word.

## What the price implies
| Measure | Value | Basis | Source |
Forward P/E, steady-state P/E at the stated cost of equity, implied NOPAT growth at the stated
cost of capital (Basis: derived, resting on the assumed incremental return, stated), consensus
growth, base-rate share for that growth (three-year class), forward P/E and EV/EBITDA against
the peer median, estimate revision found in search or "not found", target range against price,
the downside line.

## The three drivers
Three short paragraphs, each: assumption, evidence with date, direction of risk.

## Risks and what would change this reading
Two or three risks with their early signals, then one line on what would make the reading more
positive and one on what would make it more negative.

## Next catalyst
The event, the date and what it decides.

## Gaps
One line: what Bigdata.com could not answer, and any assumption that drives the result.

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one page, which means at most 450 words before Sources and one table. Cut drivers to a sentence each before cutting the expectations table. The assumptions (cost of equity, cost of capital) appear once, in the table, with their basis. A narrower question ("is the multiple high?") gets the relevant rows of the table, the base-rate sentence and the sources, not the full page.

## Checks before sending

1. It fits on one page: at most 450 words before Sources, one table.
2. The expectations table has the steady-state P/E, the implied growth with its assumed incremental return, the peer line, the downside line and the base-rate sentence from the three-year class, each labelled derived or assumed.
3. Three drivers, each with dated evidence from Bigdata.com.
4. Each risk has an early signal.
5. A dated next event.
6. No buy, hold, sell, overweight, underweight, interesting-at-this-price, or rating language. "Interesting" is answered with what the price assumes and what the evidence says.
7. Every figure has a source number or a Basis label.

## Hand-offs

- The user wants the thesis built out: `bigdata-thesis`. The full report: `bigdata-deep-dive`. The valuation range: `bigdata-valuation`.
- The user asks why it moved today: `bigdata-stock-move`.
- After delivering, make one offer: add the company to a Bigdata.com watchlist. Act only on a clear yes.
