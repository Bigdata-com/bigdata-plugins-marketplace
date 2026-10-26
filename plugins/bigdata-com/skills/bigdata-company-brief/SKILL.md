---
name: bigdata-company-brief
description: >-
  What happened at one company, each item with source, date and what it means. Use for what is
  happening at X, catch me up, latest news, a competitor update. Not a view: bigdata-quick-take;
  one day's move: bigdata-stock-move.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, downside-and-catalysts, after-a-price-move
  bigdata-sector-primer: auto
---

# Company brief

This skill catches a portfolio manager up on one company: every material event over the window in date order, each with its source, the value driver it touches and whether it changes the long-term outlook or only the quarter, then the two or three events that matter most, what the price and the estimate-setters did, and the next dates. The test of the brief is that a reader can tell what changed in the company's value drivers, not only what was in the news. It gives no view on the stock.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-company-brief"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. A quiet month needs a short brief that says it was quiet; a month with a deal and a guidance cut needs both read properly.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Take the window from the user ("last month", "since the print", "this quarter"); the last 30 days by default. If the user gave an angle (a product, a lawsuit, a deal), the brief leads with it and still covers the rest of the window in short. The subject may be the user's own company, a competitor, a customer or a supplier: write the implications for that reader (what a rival's price cut means for us, what a customer's capex cut means for our orders), and still give no view on the stock.

For a window longer than about three months, split each search by month or quarter, because one search per period returns fuller coverage than one search across a long span (`references/working-with-bigdata.md`, "Search well").

Ask one question only if the name is ambiguous. If the company is Private, the price, estimate and target sections do not exist; write the brief from documents and say so in the header. Done when the company is resolved, the window is fixed and the header states both.

## Gather

1. **The company's numbers.** Profile and quote, consensus with its vintage and the ratings and targets; the latest quarter against consensus and the next report date; and five fiscal years of annual statements, ratios and segments (annual periods, not the default quarters), so the five years give a three-year rolling ROIIC. Done when current consensus for the next two fiscal years with its vintage, the target and rating counts, the last report and the next date, and the revenue, margin, free cash flow and segment base needed to size an event are in hand.
2. **Prices over the window.** Daily prices for the stock and its index (the S&P 500 or the home-market index, stated) over the window and the 60 trading days before it, computed, not estimated; the company's quote carries standard windows only. If no daily series is available for the index, take the index's change for the nearest standard window from the market overview and say so. From the same series derive the stock's typical one-day range: twice the standard deviation of its daily return against the index over the 60 trading days before the window, labelled derived. Done when the stock and index moves over the exact window, the largest one-day move against the index, and the typical range are in hand.
3. **The events, one aspect per search.** Searches over the window, keeping the user's time words: the company's news; its own filings and releases (8-K or local equivalent, press releases, investor presentations); results and guidance if it reported in the window; deals, partnerships and financing; products and contracts; regulatory and legal matters, searched on their own so they are not buried under earnings headlines; management and board changes. Done when each aspect has its dated items or an explicit "none found".
4. **The documents that carry the numbers.** The full release, filing or call transcript when the excerpt leaves out the figure an event turns on (a guidance range, a deal price, a contract value, a fine). If the company reported in the window, read the call for guidance and for the exchange that moved the stock. Done when each material event has its figure.
5. **The Street's reaction.** Consensus and targets are a current snapshot with no history, so the start-of-window figures come from search. A search over research and news for target, rating and estimate changes in the window, then a second search for the consensus and mean target quoted in documents dated near the start of the window. Quote each figure with the document's date and label it press or research summary. Done when the changes and the start-of-window figures are dated and sourced, or marked not found.
6. **Peers and the industry.** One or two searches for events at competitors, suppliers or customers in the window that bear on the company (a rival's launch or price cut, a peer's print, a regulatory change across the industry). Done when the competitive context can be written in two to four sentences with sources.
7. **Sentiment.** The sentiment report (it has no window; its narrative covers recent coverage, so say which period that is and whether it matches the brief's window). Done when the direction, the stories behind it and the period covered are known.
8. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its metrics that matter, so each event is tied to the sector's own drivers. Done when the sector's two or three decisive metrics are noted, or no primer applies.

## Analyse

1. **Build the dated event list.** One row per event: date, what happened in one factual line, category (results and guidance; products and contracts; deals, partnerships and financing; regulatory and legal; management and governance; other), and source. Cite the company's own document first and the press second; merge duplicates. Mark each row fact or opinion, from `references/downside-and-catalysts.md` rule 4: a filed contract or a reported figure is a fact, a management claim, a sell-side view or an unnamed-source report is an opinion. Done when every event in the window is on the list once, with its date and source.

2. **Tie each event to a value driver.** From `references/expectations.md`, formula 4: name the trigger the event works through (sales by volume or by price and mix; operating costs through operating leverage, scale or cost efficiency; investment efficiency) and the driver it moves (sales growth, operating margin, the incremental investment rate). Add the two drivers the formula does not name when they apply: how long the company can keep earning above its cost of capital (a patent ruling, a new entrant, a regulatory change), and the per-share claim (dilution, debt, a buyback). Size the effect where the figures allow, for example a contract's annual value as a share of sales or a fine as a share of free cash flow, labelled derived. Where the size cannot be inferred, state the mechanism instead. Done when each material event has a driver, a direction for that driver (raises, lowers, unclear) and a size or a mechanism.

3. **Say which drivers matter for this company.** Where the return on new investment is near the cost of capital, events that change that return move value and growth news does not; where it is well above, sales growth moves value (`references/expectations.md`, formula 4). Classify on the three-year rolling ROIIC from the five annual periods (the file's inputs table), labelled derived, never on a single year; if the statements do not allow it, use the FactSet average ROIC as a proxy and label it so. The cost of capital is assumed, built as the inputs table sets out, with its inputs stated. Done when the brief says in one sentence which kind of event this company's value is most sensitive to, on which measure, and weighs the events by it.

4. **Run the long-term outlook test.** The price capitalises many years of cash flow, so an event matters to value when it changes cash flow beyond the next year, not when it changes the quarter's accounting line (`references/after-a-price-move.md`, rule 1). Ask the rule's questions (a), (b), (c) and (e) of each material event; question (d) is step 3. Done when each material event is classed long-term, near-term or unclear, with the evidence.

5. **Set the events against the price and the estimates.** The move over the window against the index (Gather step 2); the change in next-year and FY+2 consensus and the target and rating changes, from the dated documents in Gather step 5 against the current consensus snapshot. Price down with estimates down reads as a fundamental revision; price down with estimates flat as a multiple or positioning move; a move with no event to explain it is said to be unexplained, not given a story. A one-day move outside the stock's typical range or of 10 percent against the index, whichever is smaller for this stock, is named and handed to `bigdata-stock-move`; a quiet stock's 4 percent day can matter more than a volatile stock's 8 percent. The 10 percent figure stays as the boundary of the base-rate tables in `references/after-a-price-move.md`. Done when the table of measures at the start and end of the window is complete, with every start figure dated or marked not found.

6. **Rank the top two or three.** Order by the size of the effect on a long-term driver, then by certainty (a filed fact over a report, an announced event over a rumoured one), not by the number of headlines. Done when the brief can name the two or three events that change the company's value drivers and say why each outranks the rest.

7. **The next dates.** The next report date and conferences from the corporate calendar; and from the filings and news in Gather step 3, the items that set up a later decision (a regulatory ruling pending, a deal vote, a court date), since the calendar carries only earnings, conferences, IPOs and delistings. Type them with `references/downside-and-catalysts.md` table 2. Done when each open item has a date or window, or is marked open-ended.

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
| Date | Event [n] | Category | Driver affected | Effect (direction, size or mechanism) | Long-term or near-term | Fact or opinion |
In date order, with the citation number in the Event cell. Under the table, one "Basis and sources"
note (events reported; sizes derived, with the formula). Then one line: "No items found in:
<categories searched with no result>."

## The two or three that matter
One short paragraph each: the facts with figures, the mechanism, why it outranks the rest,
and what would confirm or contradict its effect.

## What the market and the Street did
| Measure | Start of window | End of window | Change | Basis | Source |
Price vs index, next-year and FY+2 consensus sales and EPS, mean target, rating counts,
sentiment. Start-of-window consensus and targets are press or research summaries with the
document's date, or "not found".

## Competitive context
Two to four sentences, sourced: what peers, suppliers, customers or regulators did that bears
on the company.

## Next dates
| Date or window | Event | What it decides | Source |

## What to watch
Two to four observable conditions, dated where possible.

## Gaps
Categories with no result, a private company's missing price and estimates, and anything the sources did not settle.

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
10. A one-day move outside the stock's typical range, or of 10 percent against the index if that is smaller, is named and handed to `bigdata-stock-move`, not explained here.
11. Start-of-window consensus and targets carry a document date and the label press or research summary, or are marked not found.

## Hand-offs

- The user wants a view on the stock: `bigdata-quick-take`. One day's move: `bigdata-stock-move`.
- The company reported and the user wants the quarter: `bigdata-earnings-review`. The events ahead: `bigdata-catalysts`.
- After delivering, make one offer: a monitor on the company's news, so the next brief starts from what changed since this one. Act only on a clear yes.
