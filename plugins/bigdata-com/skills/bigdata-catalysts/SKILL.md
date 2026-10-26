---
name: bigdata-catalysts
description: >-
  Dated events that could move a stock or a list, with expected impact and what is priced in. Use
  for what is coming up, events to watch, next catalysts. Not the earnings setup:
  bigdata-earnings-preview.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, downside-and-catalysts, forecasting-discipline, after-a-price-move, special-situations-arithmetic
  bigdata-sector-primer: auto
---

# Catalysts

This skill maps the dated events that could change a company's value or the market's view of it over a horizon: for each, the date or window, what has to happen, the mechanism by which it reaches value, the direction, the size, how certain the date and the outcome are, and what the market already expects. The events are ranked by expected impact and listed by date, and the note says what happens if none of them arrives. A catalyst is an event that resolves something by a date; a standing risk with no resolution date belongs in `bigdata-risk`. It gives no trade call. "When does X report?" gets the date, the time, the period and the consensus, with the source.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-catalysts"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. A company with one report and nothing else ahead needs a short note that says so.

## Scope the request

Resolve the company, or every name on the list, to its Bigdata.com entity, with its listing status taken from the lookup; for a saved list, load it from the user's saved Bigdata.com watchlists. Fix the horizon: the user's ("next quarter", "into year-end", "next 30 days"), or through the second earnings report ahead by default, which is about six months. Use the horizon as explicit dates for every calendar lookup.

For a list, the note gives each name its top catalysts in a shorter form and ranks the names by what the horizon decides for them. The subject may be the user's own company, a competitor, a customer, a supplier or a target: write what each event would mean for that reader (a rival's approval date, a customer's contract renewal), with the same evidence and no call. Ask one question only if a name is ambiguous. Done when every name is resolved and the horizon is a pair of explicit dates.

## Gather

1. **The calendar.** The corporate calendar for the company or the list over the horizon's dates. It carries earnings, conferences, IPOs and delistings only; investor days, shareholder meetings, deal votes, court dates and regulatory deadlines come from step 3. Done when every earnings date with its time and fiscal period and every conference in the horizon is listed.
2. **What the market expects now.** The company's profile and quote with the next report date, then consensus with its vintage and the ratings and targets. Consensus is a snapshot with no history of consensus or targets, so the recent revision comes from one search of research and news over the last 30 days that quotes the earlier figure, with the document's date, labelled press or research summary, or is marked not found. Done when current consensus for the next quarters and the fiscal year with its vintage, the revision found or not found, the company's guidance where given, the target range and rating counts, and the recent price move against the index are in hand. For a list, current figures for the set in one pull first (the surprise and target columns only if the list table uses them), then the company detail for the names whose catalysts need it.
3. **Events that are foreseeable but not on the calendar.** Searches, one aspect per search, over recent filings, transcripts and news: regulatory decisions and their deadlines; litigation milestones and court dates; product launches, clinical readouts or approvals; contract renewals and large customers; debt maturities, refinancing and covenant tests; buyback authorisations, spin-offs, asset sales, strategic reviews and activist stakes (the catalyst types in `references/downside-and-catalysts.md`, table 2); index changes, lock-up expiries and share-class events; management's own dated promises (a margin target by a date, a launch window). For the sector's own event types, find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its "What to watch at the macro level" and "Questions for the earnings call" subsections (some sectors title the second "Questions a specialist asks on the earnings call"). Done when each aspect has its dated items or an explicit "none found".
4. **The documents behind the dates.** The full filing or transcript that sets a date, a condition or a term (a merger agreement's outside date, a maturity schedule, an approval timeline). Done when each catalyst's date has a source a reader can check, or is marked estimated with the basis for the estimate.
5. **Macro releases, when they move the name.** For a bank, a homebuilder, a miner or another company whose value turns on rates, a commodity or a macro series, the economic calendar for the relevant country and category over the horizon. Done when the releases that bear on the company are dated with their consensus.
6. **Past reactions, for scheduled reports.** The dates of the last four earnings reports from a search for the company's results releases (the calendar looks forward only), then the stock's move against its index on each of those days from daily prices, computed, not estimated. Done when the typical size of the stock's earnings-day move is known with the number of prints found, labelled derived, or the Gaps line says the dates or the series were not available.

## Analyse

1. **Write each catalyst as a scorable question.** From `references/forecasting-discipline.md` procedure step 1: a checkable outcome, a date or window, and a reason it matters ("the regulator rules on the merger by 15 March; approval without remedies closes the deal at the stated price"). Done when every item reads as an outcome with a date, not as a theme.

2. **Fill the schema for each catalyst.**
   - Date or window, with the certainty of the date: fixed (filed or announced), estimated window (with its basis), or open-ended.
   - What has to happen: the outcome that would count.
   - Mechanism: how it reaches value, from `references/downside-and-catalysts.md` table 2. Either it changes a cash-flow driver (sales growth, margin, investment, the years of excess return) or it closes the gap between price and value (a sale, a breakup, a spin-off, a buyback, a recapitalisation, the end of forced selling), and who decides (management and board, outside holders, a regulator, a court).
   - Direction: positive, negative, or two-sided.
   - Size: in the driver's own terms where the figures allow (revenue, margin in basis points, value per share), labelled derived; for a scheduled report, the stock's typical earnings-day move from Gather step 6. Where neither exists, say so rather than writing "high".
   - Certainty of the outcome: an integer probability with its reference class, or labelled judgment when no reference class exists. Not 50 by default, and scope-sensitive: the chance an open-ended event happens within six months should be higher than within three (`references/forecasting-discipline.md` rule 2).
   - What the market expects: consensus and guidance for a report; the sell-side's stated expectation, marked as opinion, for other events; and where a traded price embeds the outcome (an announced deal's spread), the completion probability the price implies, net of carry, from `references/special-situations-arithmetic.md` formula 2, labelled derived with the break price assumed; hand the full spread arithmetic to `bigdata-special-situations`.
   Done when every catalyst has all seven fields, or a field marked "not found" with what was searched.

3. **Score potency.** From `references/downside-and-catalysts.md` table 3: certainty (announced and filed against hoped for), timing (dated against open-ended), the share of the gap or of the driver it would move, and whether the decider gains from the outcome. Rate high, medium or low with the reason, labelled judgment. The sources give no weights for the four tests and no base rates for how often announced catalysts complete; say so where it matters. Done when each catalyst has its potency and the reason.

4. **Read scheduled reports against what usually follows.** For each report, the consensus and guidance it will be measured against, the stock's typical earnings-day move, and, if the user asks what tends to follow a large reaction, the parent row of the base-rate tables in `references/after-a-price-move.md` for an earnings event and the stock's current momentum state, with N and the sample period, labelled a historical average and not a forecast. Done when each report has its bar and its typical move.

5. **Rank by expected impact, then list by date.** Rank by size, probability and potency together, not by the calendar: a large two-sided ruling in five months can outrank a routine report next week. Then give the same items by date. Done when the two or three catalysts that decide most over the horizon are named, with what each would change.

6. **What happens if nothing happens.** From `references/downside-and-catalysts.md` procedure step 8: without a catalyst, value can erode or the gap can widen. Done when the note gives the direction and the main cause, labelled judgment.

7. **The signal to watch.** For each of the top catalysts, the first observable sign of which way it is resolving and its date (a docket entry, a regulator's comment period, a pre-announcement window, a peer's print). If the user holds a thesis, map each signal to a kill criterion with a driver, a threshold and a date (`references/forecasting-discipline.md` rule 4). Done when each top catalyst has a dated signal.

Special cases:

- **Binary readouts** (a trial result, an approval, a court verdict). The library holds no base rates for these; label the probability judgment, widen it, and show both outcomes' effect on value rather than an average.
- **Spin-offs and index deletions.** The catalyst can be the end of forced selling as much as the event itself (`references/downside-and-catalysts.md` procedure step 5); date when the selling should be done.
- **Announced deals.** The spread is the market's expectation; give the implied probability and hand the full arithmetic to `bigdata-special-situations`.
- **Banks, miners and other macro-sensitive names.** The rate decisions, commodity data or stress-test results from Gather step 5 belong in the ranked table with their own dates.
- **Management's dated promises.** A margin target or launch by a date is a catalyst when missing it would change the market's view; record the promise verbatim with its source.

## Write

Follow `references/output-standard.md`.

```
# <Company> (<ticker>) catalysts: <horizon start> to <horizon end>
Data as of: price <date>; estimates <date>; newest document <date>.

## The horizon in brief
Four to six sentences: the two or three catalysts that decide most and what each would change,
what the market expects of each, the next date, and what happens if nothing happens. No call.

## What the market expects now
| Measure | Value | Basis | Source |
Consensus for the next quarter and fiscal year with its vintage, the revision found in search
(dated, press or research summary) or "not found", guidance, target range against price, price
move against the index, sentiment.

## Catalysts ranked by expected impact
| # | Catalyst: what has to happen [n] | Date or window (date certainty) | Mechanism and decider | Direction and size | Probability | Potency | What the market expects |
One "Basis and sources" note under the table: dates reported, sizes derived (formula named),
probabilities judgment or with their reference class, potency judgment.

## The top three in detail
One short paragraph each: the facts, the mechanism, what each resolution would mean for the
driver or the gap, the signal to watch with its date.

## By date
| Date | Event | Scheduled, foreseeable or open-ended | Rank | Source |

## If nothing happens
One or two sentences.

## What would change this reading
Two to four observable conditions, dated where possible.

## Gaps
Undated items, estimated dates, completion base rates (not in the sources), positioning and
options data (not in Bigdata.com).

## Sources, then the Data line, then the Powered by Bigdata.com line and the disclaimer.
```

For a list: one table across the names sorted by date with each name's top catalyst, then two or three sentences on the names whose horizon decides most. Length: one to two pages. A one-line question gets the date, the source and the footer.

## Checks before sending

1. Every catalyst has a date or window with its certainty stated; nothing undated is in the ranked table.
2. Standing risks with no resolution date are left out and pointed to `bigdata-risk`.
3. Each catalyst names its mechanism and its decider, and a size in the driver's terms or a statement that none could be inferred.
4. Probabilities are integers with a reference class or a judgment label, none is 50 by default, and longer windows carry higher odds than shorter ones for the same event.
5. Date certainty and outcome certainty are given separately.
6. What the market expects is stated for each catalyst, with sell-side views marked as opinion.
7. The list is ranked by expected impact and also given by date.
8. Base-rate rows carry N and the sample period and are called historical, not current.
9. No buy, sell, add, trim or rating word; potency describes the event, not a trade.

## Hand-offs

- The next report needs the full setup: `bigdata-earnings-preview`. The catalyst is a spin-off, a merger spread or a restructuring: `bigdata-special-situations`.
- Risks with no date: `bigdata-risk`. Probability-weighted values for the outcomes: `bigdata-scenarios`.
- After delivering, make one offer: a monitor that flags news on the top catalysts until their dates, or for a typed list of names, saving it as a Bigdata.com watchlist. Act only on a clear yes.
