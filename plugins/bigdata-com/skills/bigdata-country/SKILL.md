---
name: bigdata-country
description: >-
  A country or region from the Bigdata.com country tearsheet, news and research: growth,
  inflation, rates, currency, fiscal and external balances, politics and policy, markets, and what
  is priced in. Use when the user asks about a country's economy, outlook, political risk, or
  markets, or for a country briefing. Not for comparisons across countries, which
  bigdata-macro-compare covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline
  bigdata-sector-primer: none
---

# Country

This skill writes the country briefing a portfolio manager reads before taking risk in a market: where growth, inflation and policy stand on the latest releases, how the fiscal and external accounts hold up, what politics could change and when, and what the rates, currency and equity markets already price. It keeps three things apart that most country notes blend: the facts (releases and decisions), the opinions (forecasts by officials, economists and rating agencies) and the expectations embedded in market prices. Forecasts appear as ranges with their sources. It gives no allocation call. "What did the Bank of Japan do yesterday" gets the decision, the statement's key line and what the market priced before and after, not the full briefing.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not. Stop there: give no view, drivers, risks, figures or dates from memory while the tools are missing, and do not fall back to web search.
- Pass `plugin_slug: "bigdata-country"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish three things before gathering data:

- **The country.** Check that the country tearsheet covers it (the tool's description lists the codes; "EMU" is the euro area as a whole). If it does not, say so and build the briefing from search alone, marking each indicator's source. A multi-country region other than the euro area ("Southeast Asia", "emerging markets") is a comparison: hand it to `bigdata-macro-compare`.
- **The angle.** Rates, the currency, equities, credit, political risk, or a general briefing. The briefing leads with the user's angle and keeps the rest short.
- **The horizon.** Assume the next twelve months and state it. Forecast accuracy decays beyond about a year, so a longer horizon gets scenarios and signposts rather than point forecasts.

Do not ask a question unless the country name is ambiguous. State the assumptions under the title.

## Gather

Each step says what it must produce.

1. **Country tearsheet.** `bigdata_country_tearsheet` for the country. Done when the latest readings for growth, labour, inflation, sentiment, trade, credit, central bank and fiscal policy are in hand with their release dates, consensus and surprise; the G7 comparison table; the primary index with its moves and moving averages; the currency's spot, performance by horizon and cross rates; the upcoming events; and for the United States the Treasury curve.
2. **Euro-area member.** Also call the tearsheet for `EMU`. Done when the ECB's latest decision and the euro-area aggregates are in hand, because a member's policy rate is set for the whole area.
3. **Calendar.** `bigdata_events_calendar` with the economic calendar for the country over the horizon. Done when the next central bank meeting, the next GDP, inflation and labour releases, and any scheduled auction or budget date are listed with dates.
4. **Policy, fiscal, external, politics and markets.** `bigdata_search`, one aspect and one period per call, keeping the user's time words:
   - the central bank's latest decision and statement (fetch the statement or minutes for the exact wording) and its own projections;
   - the rate path the market prices, as quoted in research and news (futures or swaps pricing);
   - the fiscal position: deficit, debt, interest cost, financing need, and rating agency actions;
   - the external position: current account, reserves, external debt, capital flows;
   - politics: elections, coalition changes, policy announcements, and the dates attached to them;
   - official and private forecasts for growth and inflation (the central bank, the IMF, economists' surveys);
   - sovereign yields and spreads, which the tearsheet carries only for the United States;
   - the equity market's earnings and valuation, and the currency's drivers.
   Done when every indicator in the facts table has a dated reading and every forecast has an attributed source.
5. **Global context**, when the country is sensitive to it (an exporter of commodities, a dollar borrower). `bigdata_market_tearsheet` once. Done when the relevant commodity, dollar and global rates moves are in hand.

## Analyse

1. **The facts.** Each indicator with its latest reading, the prior reading, the trend, the comparison that gives it meaning (target, consensus, potential growth, peers in the G7 table) and the release date. Done when the facts table is complete, with "not available" in place of any gap rather than a dropped row.

2. **Facts, opinions and expectations kept apart.** From `references/forecasting-discipline.md`, rule 1: tag every piece of evidence as a fact (a release, a decision, a filed budget), an opinion (a forecast, guidance from officials, a rating, an economist's view) or an expectation (what market prices imply: the priced rate path, inflation breakevens where quoted, the sovereign spread, the currency's forward or consensus, the equity index's multiple). Done when every line in the analysis carries one of the three tags.

3. **Growth and inflation.** Momentum from the latest releases and their surprises, the drivers (consumption, investment, trade, government), and where growth runs against the economy's potential as sources estimate it. Forecasts as a range across the sources found, with the spread between the highest and lowest, not one number. Done when growth and inflation each have the latest fact, the range of forecasts with sources, and the main driver.

4. **Monetary policy.** The stance, the last action and its date, the guidance in the statement's own words, the central bank's projections, and the path the market prices. The gap between the bank's path and the market's path is the thing to watch; state it in basis points and by meeting where sources allow. Where the country shares a currency and a central bank (a euro-area member), the policy rate is the same across the area, so differentiate the country on growth, fiscal position and its sovereign spread against the area's benchmark, not on monetary policy. Where the currency is pegged, the anchor central bank's path is the relevant one. Done when the stance, the two paths and their gap are stated with sources.

5. **Fiscal and external balances.** Deficit, debt, interest cost as a share of revenue where sources give it, the financing need, the current account, reserves and external debt, with the rating and outlook. Say which balance would constrain policy first and what would trigger it. Done when each balance has a dated figure and the constraint is named.

6. **Politics and policy.** The dated political events over the horizon, what each could change in fiscal, regulatory or trade policy, and how markets have priced it. Where a probability is needed, take it from a reference class and label it judgment; polls and odds quoted in the press are opinions, not probabilities. Check that probabilities scale with the time window. Done when each event has a date, a mechanism and, where given, a probability with its basis.

7. **Scenarios for the main uncertainty.** From rule 2 in `references/forecasting-discipline.md`, two or three cases for the question that decides the next twelve months (a recession or not, a policy turn, an election outcome), each with what has to be true, the indicator that would show it first, and a probability. Probabilities are integers that sum to 100, each with a reason from a reference class, and never a default split. Done when the cases, their signposts and the probability-weighted reading are stated.

8. **Markets and what is priced in.** The equity index against its region and its own moving averages, the currency's performance and drivers, yields and spreads. Compare what markets price with the scenario probabilities and the range of forecasts, and say where the two differ and by how much. That gap is what would move prices if the scenarios are right; it is not a call. Done when each market line has a reading, a source and the comparison with the scenarios.

## Write

Follow `references/output-standard.md`.

```
# <Country>: country briefing, <date>
Data as of: releases to <date>; market data <date>; newest document <date>.
Scope: <angle, horizon>.

## The view
Four to eight sentences: where growth, inflation and policy stand, the constraint that matters,
what markets price against the scenarios, and what would change the reading. No allocation call.

## Facts
| Indicator | Latest | Prior | Trend | Comparison (target, consensus, G7) | Release date | Basis | Source |
GDP growth, CPI, core inflation, unemployment, policy rate, 10-year yield, currency, primary
index, fiscal balance, debt, current account, reserves.

## Growth and inflation
Drivers; forecast ranges with sources.

## Monetary policy
Stance, last action, guidance quoted, the bank's path against the market's path.
[Euro-area member: the shared-rate note and the spread against the area benchmark.]

## Fiscal and external position
Balances, rating, the binding constraint.

## Politics and policy
| Date | Event | What it could change | Probability and basis | Source |

## Scenarios
| Case | What has to be true | First signal | Probability | Market reading if it happens |

## Markets and what is priced in
Equities, currency, rates and spreads; the comparison with the scenarios.

## Calendar
The next dated releases and decisions.

## Facts, opinions, expectations
One line each listing the main items under each tag.

## What would change this view
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages. A narrow question gets the relevant indicator or decision with its comparison, its date, the market's reading and the sources, and the footer.

## Checks before sending

1. Every indicator has a release date and a source, or reads "not available".
2. Facts, opinions and expectations are tagged and never merged in one sentence without labels.
3. Forecasts are ranges with named sources, not single numbers.
4. The central bank's own path and the market's path are both stated, with their gap.
5. A euro-area member is differentiated on growth, fiscal position and spread, not on the shared policy rate.
6. Scenario probabilities are integers that sum to 100, each with a reason, and scale with the horizon.
7. No overweight, underweight, buy, sell or allocation language.
8. Nothing comes from memory or the open web without saying so in Gaps.

## Hand-offs

- Several countries, a region or a bloc compared: `bigdata-macro-compare`. A sector inside the country: `bigdata-sector` with the country scope.
- Today's moves across markets: `bigdata-markets-today`. A theme such as reshoring or energy policy: `bigdata-theme`.
- After delivering, make one offer: a monitor on the country's central bank decisions and major releases, or save the briefing to the user's Bigdata.com account. Act only on a clear yes.
