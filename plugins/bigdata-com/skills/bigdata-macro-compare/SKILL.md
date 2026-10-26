---
name: bigdata-macro-compare
description: >-
  Countries or regions compared on the same indicators: growth, inflation, real rates, currencies,
  why they differ. Use for compare economies, which country is stronger right now, where to
  expand. Not one country: bigdata-country.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline
  bigdata-sector-primer: none
---

# Macro compare

This skill writes the cross-country comparison a reader uses to see where economies and policies diverge: the same indicators for every member, measured for the same period where the data allows, the reasons for each difference with evidence, the central banks' paths against what markets price, and what would change the picture. The reader may be a portfolio manager, or a corporate team choosing where to expand, source or hedge. It replaces separate G7, regional and country-sector notes. It answers "which looks stronger" on stated dimensions with the evidence, and makes no allocation or ranking call. "How does euro-area inflation compare with the US" gets the two rows, the periods, the reason for the gap and the sources, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-macro-compare"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish four things before gathering data:

- **The members.** Named countries; a bloc (the G7 is the United States, Japan, Germany, the United Kingdom, France, Italy and Canada); the euro area as one member, which the country data covers as a whole; or a region without a code ("Asia ex-Japan", "emerging markets"), which is built from its largest economies. Name the economies used for a region and say that a regional figure is an unweighted median unless a source gives a weighted aggregate. "A global macro overview" with no members means the G7 plus China and India, stated as an assumption.
- **The angle.** Growth, inflation, policy, currencies, rates, equities or credit. The note leads with it.
- **The reader.** A corporate team asking where to expand, where to source or which currencies to hedge is a valid request. For expansion, lead with demand growth, policy room and the rules on foreign ownership and repatriation; for sourcing, with trade policy, costs, the currency and dated disruptions; for hedging, with real rate differentials, external positions and the priced paths. Write the implications for that reader; the evidence and the arithmetic stay the same, and the answer lays the options side by side without choosing.
- **The horizon.** Assume the next twelve months and state it.

A sector within a country goes to `bigdata-sector` with a country scope, not here. With more than about eight members, the full table covers all of them and the narrative goes deep only on the outliers. Ask one question only when the members cannot be inferred and the user gave no region or bloc.

## Gather

Each step says what it must produce.

1. **Country tearsheets.** The economic overview for each member, in parallel. Done when the same indicators (growth, inflation, unemployment, policy rate, currency, primary index, the fiscal and trade sections' latest releases) are in hand for every member with release dates, and any missing cell is recorded as "not available" rather than dropped.
2. **One market snapshot.** Current market levels in one pull, so currencies, indexes and US Treasury yields are compared at the same moment. It carries US Treasuries only: every other member's 10-year yield comes from a search in step 4, at whatever date its source gives, so the yield row mixes dates; flag it in the table and in Gaps. Done when every member's currency and index have a reading from the same snapshot and each yield cell has its own date.
3. **Calendar.** The economic calendar across the members over the horizon. Done when each central bank's next meeting and the next major releases are listed.
4. **The reasons and the paths.** Searches, one country, one aspect and one period per call: the central bank's latest decision and guidance; the rate path the market prices, as quoted in research and news; the 10-year government yield outside the United States; fiscal balance, primary balance, gross and net debt, interest cost and rating actions, wherever the tearsheet's fiscal section lacks them, each dated; the current account, reserves and external debt due within a year; trade openness (exports plus imports over GDP), the commodity trade balance and the external financing need, for the common-shock step; politics with dates; official and private forecasts; sovereign spreads. Then comparative research on the largest divergences ("why euro-area growth lagged the US"). Done when each member has a dated reading for every row, or "not available", and each large difference has at least one sourced explanation or is marked unexplained.

## Analyse

Every figure comes from a country tearsheet, the market snapshot or a dated search result; arithmetic on them is labelled derived.

1. **The like-for-like table.** Every member on the same rows: real GDP growth year on year for the same quarter where possible, and nominal growth where found; headline and core CPI; unemployment, noting national definitions; the policy rate and the real policy rate (policy rate - inflation, derived, naming the inflation measure); the 10-year yield and the real 10-year yield (same rule); the currency's change against one common base over stated windows; the primary index's return in local currency and in the common currency (derived); the fiscal balance, gross debt and, where sources give it, net debt, as shares of GDP; interest cost as a share of government revenue where available; the current account as a share of GDP. Record the period of every cell, because release calendars differ and a quarter-old reading is not comparable with this month's. Done when every cell has its period, every rates and growth row says nominal or real, and the yield row's mixed dates are flagged.

2. **Facts, opinions and expectations kept apart.** From `references/forecasting-discipline.md`, rule 1: releases and decisions are facts; forecasts, guidance and ratings are opinions; priced rate paths, spreads and currency forwards are expectations. Done when every comparison sentence uses one tag and opinions are attributed.

3. **Debt dynamics.** For each member with the inputs, the r minus g rule, a standard identity of public finance (not from the method files): debt-stabilising primary balance = (r - g) / (1 + g) x d, with d gross debt over GDP, r the effective nominal interest rate on government debt (interest paid over the previous year's debt, derived) and g nominal GDP growth. Compute it, with the working shown, and set it against the actual primary balance; the gap is the fiscal adjustment the arithmetic implies, and members where r has moved above g lose fiscal room fastest. Done when each member has r, g, d, the required and the actual primary balance with periods, or "not available".

4. **The reasons for the differences.** For each row where members diverge materially, the explanation with evidence: the policy rate gap, fiscal stance, energy and commodity exposure, the sector mix of output, demographics, the currency's pass-through to prices, credit conditions. Do not invent a cause: if no source explains a gap, say it is unexplained. Done when each material divergence has a sourced reason or the unexplained label.

5. **Policy divergence.** Each central bank's stance, last action and guidance, its own projected path, and the path the market prices, with the real rate differentials that matter for the currencies. Members that share a currency and a central bank (euro-area members) have one policy rate, so differentiate them on growth, fiscal position and spreads against the area's benchmark yield, not on monetary policy; a pegged currency follows its anchor's path. Done when the policy table shows both paths per central bank and their gap.

6. **What is priced in.** For each member: the priced rate path, the sovereign spread, the currency's move and, where sources give it, the equity market's multiple against its own history. Set these against the facts and the forecast ranges and say where pricing and evidence differ most. Done when each member has its priced line and the largest differences are named.

7. **A common shock.** Choose the one cross-country uncertainty that matters most over the horizon (a global slowdown, an energy price shock, a US rates move, a trade measure). Measure each member's exposure with figures from step 4 of Gather: trade openness, the commodity trade balance (net exporter or importer, as a share of GDP), the external financing need, and the policy room left by the real rate and the debt dynamics. From rule 2 in `references/forecasting-discipline.md`, give two or three cases with integer probabilities that sum to 100. The probabilities are judgment, each with a reason drawn from a named historical analogue found in the tearsheets' history and the news (an earlier oil shock, a past tightening cycle), never a default split and never an invented base rate; the reference classes in the method files are company and equity samples and give no macro base rates. Done when every member has its exposure figures and the cases have analogues and signposts.

8. **"Which looks stronger".** Answer on named dimensions (growth momentum, inflation against target, fiscal room, external balance, policy room), each judged from the table. For a corporate reader, set the dimensions that matter to the decision (demand, costs, currency, rules) side by side per member. Order members on a dimension the user chose and say which; do not combine the dimensions into one score or rank by attractiveness. Done when the answer names its dimensions and the evidence.

## Write

Follow `references/output-standard.md`.

```
# <Members or bloc>: macro comparison, <date>
Data as of: releases to <date> (periods per cell in the table); market snapshot <date>; newest document <date>.
Scope: <members, how a region was built, angle, reader, horizon>.

## The view
Four to eight sentences: the main divergences, their reasons, where policy paths and market
pricing differ, the implication for the reader, and what would change the picture. No allocation call.

## Comparison table
| Indicator | <Member 1> | <Member 2> | ... up to seven members |
Each cell carries its period; split into further tables beyond seven members. "Not available"
where missing. Basis and sources: one line under the table; the yield row's mixed dates flagged.

## Debt dynamics
| Member | r | g | Debt / GDP | Required primary balance | Actual primary balance | Gap | Basis |

## Why they differ
One paragraph per material divergence, with the evidence and its tag.

## Policy divergence
| Central bank | Rate (nominal, real) | Last action | Guidance | Bank's path | Market's path | Gap | Source |
[Shared-currency members: the note on differentiating them.]

## What is priced in
Per member: rate path, spread, currency, equity multiple, against the evidence.

## Exposure to <the common shock>
| Member | Trade openness | Commodity balance | External financing need | Policy room | Basis | Source |
The cases with probabilities, analogues and signposts.

## On the dimensions asked
The "which looks stronger" answer on named dimensions, or the options side by side for a corporate reader.

## Calendar
The next decisions and releases across members.

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages. A narrow question gets the relevant rows with their periods, the reason for the difference and the sources, and the footer.

## Checks before sending

1. Every member sits on identical rows, and every cell states its period; non-US yields are flagged as mixed-date search figures.
2. Gaps read "not available"; no member was dropped from a row to make the table look complete.
3. Every rates and growth row says nominal or real; real rates name the inflation measure.
4. Regional figures say which economies they cover and whether they are weighted.
5. Each material divergence has a sourced reason or is marked unexplained.
6. Euro-area members are differentiated on growth, fiscal position and spreads, not on the shared rate.
7. Each central bank shows its own path and the market's path.
8. Common-shock exposure is measured in figures; probabilities are integers that sum to 100, each with a named analogue, and no base rate is invented.
9. No ranking by attractiveness, no overweight, underweight or allocation language; a corporate reader gets the options side by side, not a choice.
10. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- One country in depth, including a country risk premium for an entry decision: `bigdata-country`. A sector inside one country: `bigdata-sector` with the country scope.
- Today's market moves: `bigdata-markets-today`. A cross-border theme: `bigdata-theme`.
- After delivering, make one offer: a monitor on the members' central bank decisions, or save the comparison to the user's Bigdata.com account. Act only on a clear yes.
