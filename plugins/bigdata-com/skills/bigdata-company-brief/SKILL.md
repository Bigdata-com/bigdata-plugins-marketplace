---
name: bigdata-company-brief
description: >-
  What happened at one public company over a window, from Bigdata.com news, filings, transcripts
  and research: the events in order, each with its source and what it means for the drivers of
  value, then the two or three that matter most. Use when the user asks what is happening with a
  company, to catch them up on a name, for recent developments, or for a summary of the last
  month. Not for a view on the stock, which bigdata-quick-take covers, or for one day's price
  move, which bigdata-stock-move covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Company brief

This skill catches a portfolio manager up on one company: every material event over the window in date order, each with its source, the value driver it touches and whether it changes the long-term outlook or only the quarter, then the two or three events that matter most, what the price and the estimate-setters did, and the next dates. The test of the brief is that a reader can tell what changed in the company's value drivers, not only what was in the news. It gives no view on the stock.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not write the brief from memory or the web.
- Pass `plugin_slug: "bigdata-company-brief"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. A quiet month needs a short brief that says it was quiet; a month with a deal and a guidance cut needs both read properly.

## Scope the request

Resolve the company with `find_securities`. Take the window from the user ("last month", "since the print", "this quarter"); the last 30 days by default. If the user gave an angle (a product, a lawsuit, a deal), the brief leads with it and still covers the rest of the window in short.

For a window longer than about three months, split each search by month or quarter, because one search per period returns fuller coverage than one search across a long span (`references/working-with-bigdata.md`, "Search well").

Ask one question only if the name is ambiguous. If the company is Private, the price, estimate and target sections do not exist; write the brief from documents and say so in the header.

## Gather

1. **Tearsheet, in two calls.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data, latest_earnings, events_calendar, estimates`, then `fundamentals, revenue_segmentation`. Done when the price move over the window against the index, consensus for the next two fiscal years with its 30-day change and its vintage, the target and rating counts, the last report and the next date, and the revenue, margin and segment base needed to size an event are in hand.
2. **The events, one aspect per search.** `bigdata_search` over the window, keeping the user's time words: the company's news; its own filings and releases (8-K or local equivalent, press releases, investor presentations); results and guidance if it reported in the window; deals, partnerships and financing; products and contracts; regulatory and legal matters, searched on their own so they are not buried under earnings headlines; management and board changes. Done when each aspect has its dated items or an explicit "none found".
3. **The documents that carry the numbers.** `bigdata_fetch_document` on the release, filing or call transcript when the excerpt leaves out the figure an event turns on (a guidance range, a deal price, a contract value, a fine). If the company reported in the window, read the call for guidance and for the exchange that moved the stock. Done when each material event has its figure.
4. **The Street's reaction.** `bigdata_search` over research and news for target, rating and estimate changes in the window. Done when the changes are dated and sourced, or recorded as none found.
5. **Peers and the industry.** One or two searches for events at competitors, suppliers or customers in the window that bear on the company (a rival's launch or price cut, a peer's print, a regulatory change across the industry). Done when the competitive context can be written in two to four sentences with sources.
6. **Sentiment.** `bigdata_sentiment_tearsheet` for the window. Done when the direction and the stories behind it are known.
7. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read its "metrics that matter" section, so each event is tied to the sector's own drivers.

## Analyse

1. **Build the dated event list.** One row per event: date, what happened in one factual line, category (results and guidance; products and contracts; deals, partnerships and financing; regulatory and legal; management and governance; other), and source. Cite the company's own document first and the press second; merge duplicates. Mark each row fact or opinion, from `references/downside-and-catalysts.md` rule 4: a filed contract or a reported figure is a fact, a management claim, a sell-side view or an unnamed-source report is an opinion. Done when every event in the window is on the list once, with its date and source.

2. **Tie each event to a value driver.** From `references/expectations.md`, formula 4: name the trigger the event works through (sales by volume or by price and mix; operating costs through operating leverage, scale or cost efficiency; investment efficiency) and the driver it moves (sales growth, operating margin, the incremental investment rate). Add the two drivers the formula does not name when they apply: how long the company can keep earning above its cost of capital (a patent ruling, a new entrant, a regulatory change), and the per-share claim (dilution, debt, a buyback). Size the effect where the figures allow, for example a contract's annual value as a share of sales or a fine as a share of free cash flow, labelled derived. Where the size cannot be inferred, state the mechanism instead. Done when each material event has a driver, a direction for that driver (raises, lowers, unclear) and a size or a mechanism.

3. **Say which drivers matter for this company.** Where the company earns near its cost of capital, events that change the return on new investment move value and growth news does not; where it earns well above it, sales growth moves value (`references/expectations.md`, formula 4; use the FactSet ROIC against a stated, assumed cost of capital). Done when the brief says in one sentence which kind of event this company's value is most sensitive to, and weighs the events by it.

4. **Run the long-term outlook test.** The price capitalises many years of cash flow, so an event matters to value when it changes cash flow beyond the next year, not when it changes the quarter's accounting line ("A Long Look at Short-Termism", 2014, p.10; `references/expectations.md`). For each material event ask: did guidance, FY+2 consensus or long-term growth change; is the effect recurring or one-time; does cash flow move with the earnings line; is the item diagnostic (it changes the odds that the drivers play out) or does it only look causal (an EPS-dilution headline on an acquisition whose synergies exceed the premium; "Cultivating Your Judgment Skills", 2013, p.10). Done when each material event is classed long-term, near-term or unclear, with the evidence.

5. **Set the events against the price and the estimates.** The move over the window against the index; the change in next-year and FY+2 consensus; the target and rating changes. Price down with estimates down reads as a fundamental revision; price down with estimates flat as a multiple or positioning move; a move with no event to explain it is said to be unexplained, not given a story. A one-day move of 10 percent or more against the index is named and handed to `bigdata-stock-move`. Done when the table of measures at the start and end of the window is complete.

6. **Rank the top two or three.** Order by the size of the effect on a long-term driver, then by certainty (a filed fact over a report, an announced event over a rumoured one), not by the number of headlines. Done when the brief can name the two or three events that change the company's value drivers and say why each outranks the rest.

7. **The next dates.** From the events calendar and the events in the window that set up a later decision (a regulatory ruling pending, a deal vote, a court date, the next report), from `references/downside-and-catalysts.md` table 2. Done when each open item has a date or window, or is marked open-ended.

Special cases:

- **Banks and insurers.** Tie events to the primer's drivers (net interest income and margin, provisions and credit quality, capital ratios; premiums, the combined ratio and reserve development) rather than to sales and operating margin.
- **Conglomerates.** Tie each event to the segment it affects and size it against that segment's revenue and profit, not the group's.
- **Early-stage or loss-making companies.** The driver most events touch is cash runway. State the burn rate and the runway as derived and any funding assumption as assumed (`references/downside-and-catalysts.md` rule 5).
- **A window that contains the earnings report.** The report anchors the brief: lead the event list with the results against consensus and the guidance change, and offer `bigdata-earnings-review` for the full quarter.
- **A window with nothing material.** Say so in the first sentence, give the table of measures and the next dates, and stop.

## Write

Follow `references/output-standard.md`.

```
# <Company> (<ticker>): what happened, <window start> to <window end>
Data as of: price <date>; estimates <date>; latest statements <period>; newest document <date>.

## What happened
Four to six sentences: the two or three events that matter and the driver each moves, whether
they change the long-term outlook, what the price and the estimates did, and the next date.
No view on the stock.

## The events
| Date | Event | Category | Driver affected | Effect (direction, size or mechanism) | Long-term or near-term | Fact or opinion | Basis | Source |
In date order. Then one line: "No items found in: <categories searched with no result>."

## The two or three that matter
One short paragraph each: the facts with figures, the mechanism, why it outranks the rest,
and what would confirm or contradict its effect.

## What the market and the Street did
| Measure | Start of window | End of window | Change | Basis | Source |
Price vs index, next-year and FY+2 consensus sales and EPS, mean target, rating counts,
sentiment.

## Competitive context
Two to four sentences, sourced: what peers, suppliers, customers or regulators did that bears
on the company.

## Next dates
| Date or window | Event | What it decides | Source |

## What would change this view
Two to four observable conditions, dated where possible.

## Gaps
## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

Length: one to two pages. A narrow question ("any legal news on X this month?") gets the matching rows, their reading and the sources.

## Checks before sending

1. Every event has a date and a source, and the company's own document is cited where one exists.
2. Every material event names the driver it moves and a size or a mechanism; none carries only a "positive" or "negative" label.
3. Each material event is classed long-term, near-term or unclear, with the evidence.
4. The regulatory and legal search was run on its own, and empty categories are listed as searched.
5. The top two or three are ranked by effect on long-term drivers and certainty, not by headline count.
6. Price and estimate changes over the window are tabled with their vintage.
7. Opinions (management claims, sell-side views, unnamed sources) are marked as such.
8. No bullish, bearish, buy, hold, sell or rating word anywhere.
9. The competitive context cites at least one source about a company other than the subject.
10. A one-day move of 10 percent or more against the index is named and handed to `bigdata-stock-move`, not explained here.

## Hand-offs

- The user wants a view on the stock: `bigdata-quick-take`. One day's move: `bigdata-stock-move`.
- The company reported and the user wants the quarter: `bigdata-earnings-review`. The events ahead: `bigdata-catalysts`.
- After delivering, make one offer: a monitor on the company's news, so the next brief starts from what changed since this one. Act only on a clear yes.
