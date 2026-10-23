---
name: bigdata-macro-compare
description: >-
  Countries, regions or blocs compared on the same indicators from Bigdata.com country tearsheets,
  news and research: growth, inflation, rates, currencies, fiscal and external positions, market
  performance, and the reasons for the differences. Use when the user asks to compare economies,
  for a G7 or regional comparison, which country or economy looks stronger, or for a global macro
  overview. Not for one country in depth, which bigdata-country covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline
  bigdata-sector-primer: none
---

# Macro compare

This skill writes the cross-country comparison a portfolio manager uses to see where economies and policies diverge: the same indicators for every member, measured for the same period where the data allows, the reasons for each difference with evidence, the central banks' paths against what markets price, and what would change the picture. It replaces separate G7, regional and country-sector notes. It answers "which looks stronger" on stated dimensions with the evidence, and makes no allocation or ranking call. "How does euro-area inflation compare with the US" gets the two rows, the periods, the reason for the gap and the sources, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-macro-compare"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish three things before gathering data:

- **The members.** Named countries; a bloc (the G7 is the United States, Japan, Germany, the United Kingdom, France, Italy and Canada); the euro area as one member through the tearsheet's `EMU` code; or a region without a code ("Asia ex-Japan", "emerging markets"), which is built from its largest economies. Name the economies used for a region and say that a regional figure is an unweighted median unless a source gives a weighted aggregate. "A global macro overview" with no members means the G7 plus China and India, stated as an assumption.
- **The angle.** Growth, inflation, policy, currencies, rates, equities or credit. The note leads with it.
- **The horizon.** Assume the next twelve months and state it.

A sector within a country goes to `bigdata-sector` with a country scope, not here. With more than about eight members, the full table covers all of them and the narrative goes deep only on the outliers. Ask one question only when the members cannot be inferred and the user gave no region or bloc.

## Gather

Each step says what it must produce.

1. **Country tearsheets.** `bigdata_country_tearsheet` once per member, in parallel. Done when the same indicators (growth, inflation, unemployment, policy rate, currency, primary index, the fiscal and trade sections' latest releases) are in hand for every member with release dates, and any missing cell is recorded as "not available" rather than dropped.
2. **One market snapshot.** `bigdata_market_tearsheet` once, so currencies, rates and indexes are compared at the same moment. Done when every member's currency and index have a reading from the same snapshot.
3. **Calendar.** `bigdata_events_calendar` with the economic calendar across the members over the horizon. Done when each central bank's next meeting and the next major releases are listed.
4. **The reasons and the paths.** `bigdata_search`, one country, one aspect and one period per call: the central bank's latest decision and guidance; the rate path the market prices, as quoted in research and news; fiscal deficit, debt and rating actions; the current account and external debt; politics with dates; official and private forecasts; sovereign yields and spreads outside the United States. Then comparative research on the largest divergences ("why euro-area growth lagged the US"). Done when each member has a dated reading for every row and each large difference has at least one sourced explanation or is marked unexplained.

## Analyse

1. **The like-for-like table.** Every member on the same rows: real GDP growth year on year for the same quarter where possible; headline and core CPI; unemployment, noting national definitions; the policy rate; the 10-year yield; the currency's change against one common base over stated windows; the primary index's return in local currency and in the common currency (derived); the fiscal balance and gross debt as a share of GDP; the current account as a share of GDP. Record the period of every cell, because release calendars differ and a quarter-old reading is not comparable with this month's. Done when the table has Basis and Source columns and every cell has its period.

2. **Facts, opinions and expectations kept apart.** From `references/forecasting-discipline.md`, rule 1: releases and decisions are facts; forecasts, guidance and ratings are opinions; priced rate paths, spreads and currency forwards are expectations. Done when every comparison sentence uses one tag and opinions are attributed.

3. **The reasons for the differences.** For each row where members diverge materially, the explanation with evidence: the policy rate gap, fiscal stance, energy and commodity exposure, the sector mix of output, demographics, the currency's pass-through to prices, credit conditions. Do not invent a cause: if no source explains a gap, say it is unexplained. Done when each material divergence has a sourced reason or the unexplained label.

4. **Policy divergence.** Each central bank's stance, last action and guidance, its own projected path, and the path the market prices, with the rate differentials that matter for the currencies. Members that share a currency and a central bank (euro-area members) have one policy rate, so differentiate them on growth, fiscal position and spreads against the area's benchmark yield, not on monetary policy; a pegged currency follows its anchor's path. Done when the policy table shows both paths per central bank and their gap.

5. **What is priced in.** For each member: the priced rate path, the sovereign spread, the currency's move and, where sources give it, the equity market's multiple against its own history. Set these against the facts and the forecast ranges and say where pricing and evidence differ most. Done when each member has its priced line and the largest differences are named.

6. **A common shock.** Choose the one cross-country uncertainty that matters most over the horizon (a global slowdown, an energy price shock, a US rates move, a trade measure). Describe how each member is exposed, through trade, financing, commodities or policy room, and, from rule 2 in `references/forecasting-discipline.md`, give two or three cases with integer probabilities that sum to 100, each with a reason from a reference class, never a default split. Done when every member has an exposure line and the cases have signposts.

7. **"Which looks stronger".** Answer on named dimensions (growth momentum, inflation against target, fiscal room, external balance, policy room), each judged from the table. Order members on a dimension the user chose and say which; do not combine the dimensions into one score or rank by attractiveness. Done when the answer names its dimensions and the evidence.

## Write

Follow `references/output-standard.md`.

```
# <Members or bloc>: macro comparison, <date>
Data as of: releases to <date> (periods per cell in the table); market snapshot <date>; newest document <date>.
Scope: <members, how a region was built, angle, horizon>.

## The view
Four to eight sentences: the main divergences, their reasons, where policy paths and market
pricing differ, and what would change the picture. No allocation call.

## Comparison table
| Indicator | <Member 1> | <Member 2> | ... | Period | Basis | Source |
Same rows for every member; "not available" where missing.

## Why they differ
One paragraph per material divergence, with the evidence and its tag.

## Policy divergence
| Central bank | Rate | Last action | Guidance | Bank's path | Market's path | Gap | Source |
[Shared-currency members: the note on differentiating them.]

## What is priced in
Per member: rate path, spread, currency, equity multiple, against the evidence.

## Exposure to <the common shock>
| Member | Channel | Exposure | Basis | Source |
The cases with probabilities and signposts.

## On the dimensions asked
The "which looks stronger" answer on named dimensions, if asked.

## Calendar
The next decisions and releases across members.

## What would change this view
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages. A narrow question gets the relevant rows with their periods, the reason for the difference and the sources, and the footer.

## Checks before sending

1. Every member sits on identical rows, and every cell states its period.
2. Gaps read "not available"; no member was dropped from a row to make the table look complete.
3. Regional figures say which economies they cover and whether they are weighted.
4. Each material divergence has a sourced reason or is marked unexplained.
5. Euro-area members are differentiated on growth, fiscal position and spreads, not on the shared rate.
6. Each central bank shows its own path and the market's path.
7. Probabilities are integers that sum to 100, each with a reason.
8. No ranking by attractiveness, no overweight, underweight or allocation language.
9. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- One country in depth: `bigdata-country`. A sector inside one country: `bigdata-sector` with the country scope.
- Today's market moves: `bigdata-markets-today`. A cross-border theme: `bigdata-theme`.
- After delivering, make one offer: a monitor on the members' central bank decisions, or save the comparison to the user's Bigdata.com account. Act only on a clear yes.
