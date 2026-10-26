---
name: bigdata-country
description: >-
  One country's economy and markets: growth, inflation, rates, currency, fiscal and external
  balances, politics, what is priced in. Use for a country outlook, political risk, market entry.
  Not several countries: bigdata-macro-compare.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline
  bigdata-sector-primer: none
---

# Country

This skill writes the country briefing a reader needs before taking risk in a market or doing business there: where growth, inflation and policy stand on the latest releases, how the fiscal and external accounts hold up, what politics could change and when, and what the rates, currency and equity markets already price. The reader may be a portfolio manager, or a corporate strategy, treasury or supply-chain team weighing entry, currency exposure or sourcing. It keeps three things apart that most country notes blend: the facts (releases and decisions), the opinions (forecasts by officials, economists and rating agencies) and the expectations embedded in market prices. Forecasts appear as ranges with their sources. It gives no allocation call. "What did the Bank of Japan do yesterday" gets the decision, the statement's key line and what the market priced before and after, not the full briefing.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-country"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish four things before gathering data:

- **The country.** Check that the country tearsheet covers it (the tool's description lists the codes; "EMU" is the euro area as a whole). If it does not, say so and build the briefing from search alone, marking each indicator's source. A multi-country region other than the euro area ("Southeast Asia", "emerging markets") is a comparison: hand it to `bigdata-macro-compare`.
- **The angle.** Rates, the currency, equities, credit, political risk, or a general briefing. The briefing leads with the user's angle and keeps the rest short.
- **The reader.** Market entry, currency exposure and supply-chain exposure to the country are valid requests from a corporate team. For entry, lead with demand growth, the currency path, the country risk premium and the rules on foreign ownership, capital movement and repatriation. For currency exposure, lead with the real rate differential, the external position and the reserves. For a supply chain, lead with trade policy, export controls, energy and labour, and dated disruptions. Write the implications for that reader; the evidence and the arithmetic stay the same.
- **The horizon.** Assume the next twelve months and state it. Forecast accuracy decays beyond about a year, so a longer horizon gets scenarios and signposts rather than point forecasts.

Do not ask a question unless the country name is ambiguous. State the assumptions under the title.

## Gather

Each step says what it must produce.

1. **Country tearsheet.** The country's economic overview. Done when the latest readings for growth, labour, inflation, sentiment, trade, credit, central bank and fiscal policy are in hand with their release dates, consensus and surprise; the G7 comparison table; the primary index with its moves and moving averages; the currency's spot, performance by horizon and cross rates; the upcoming events; and for the United States the Treasury curve.
2. **Euro-area member.** Also the same overview for the euro area as a whole. Done when the ECB's latest decision and the euro-area aggregates are in hand, because a member's policy rate is set for the whole area.
3. **Calendar.** The economic calendar for the country over the horizon. Done when the next central bank meeting, the next GDP, inflation and labour releases, and any scheduled auction or budget date are listed with dates.
4. **Policy, fiscal, external, politics and markets.** Searches, one aspect and one period per call, keeping the user's time words:
   - the central bank's latest decision and statement (fetch the statement or minutes for the exact wording), its own projections, and its published estimate of the neutral rate if it gives one;
   - the rate path the market prices, as quoted in research and news (futures or swaps pricing);
   - the fiscal position: primary and overall balance, gross debt, interest cost, the financing need, and rating agency actions;
   - the external position: current account, reserves, imports, short-term external debt, external debt due within a year, capital flows;
   - politics: elections, coalition changes, policy announcements, and the dates attached to them;
   - official and private forecasts for growth and inflation (the central bank, the IMF, economists' surveys), and inflation expectations where quoted;
   - sovereign yields and spreads (against US Treasuries, Bunds or the CDS market, as sources quote them), which the tearsheet carries only for the United States;
   - for an entry or exposure question: foreign-ownership rules, capital controls, export controls and trade measures;
   - the equity market's earnings and valuation, and the currency's drivers.
   Done when every indicator in the facts table has a dated reading and every forecast has an attributed source, or the row reads "not available".
5. **Global context**, when the country is sensitive to it (an exporter of commodities, a dollar borrower). Current market levels across commodities, the dollar and global rates, in one pull. Done when the relevant commodity, dollar and global rates moves are in hand.

## Analyse

Every figure in these steps comes from the country tearsheet or a dated search result. Arithmetic on those figures is labelled derived; an input the analyst chooses is labelled assumed with its reason.

1. **The facts.** Each indicator with its latest reading, the prior reading, the trend, the comparison that gives it meaning (target, consensus, potential growth, peers in the G7 table) and the release date. Show rates and growth twice, nominal and real: real GDP growth and nominal GDP growth; the policy rate and the real policy rate; the 10-year yield and the real 10-year yield. Done when the facts table is complete, every rates and growth row says nominal or real, and "not available" stands in place of any gap rather than a dropped row.

2. **Facts, opinions and expectations kept apart.** From `references/forecasting-discipline.md`, rule 1: tag every piece of evidence as a fact (a release, a decision, a filed budget), an opinion (a forecast, guidance from officials, a rating, an economist's view, a neutral-rate estimate) or an expectation (what market prices imply: the priced rate path, inflation breakevens where quoted, the sovereign spread, the currency's forward or consensus, the equity index's multiple). The tags sit with each claim in the text and tables; there is no separate tag section. Done when every line in the analysis carries one of the three tags.

3. **Growth and inflation.** Momentum from the latest releases and their surprises, the drivers (consumption, investment, trade, government), and where growth runs against the economy's potential as sources estimate it. Forecasts as a range across the sources found, with the spread between the highest and lowest, not one number. Done when growth and inflation each have the latest fact, the range of forecasts with sources, and the main driver.

4. **Monetary policy and the real rate.** The stance, the last action and its date, the guidance in the statement's own words, the central bank's projections, and the path the market prices. Then the stance in numbers:
   - Real policy rate = policy rate - inflation (derived). Say which inflation measure is used: headline or core year on year, or expected inflation when a dated forecast or breakeven is quoted. Do the same for the 10-year yield.
   - Set the real policy rate against a neutral real rate range, taken from the central bank's own estimate or research quoted in a dated search result (an opinion; the neutral rate is not observed, so it is always a range). Above the range is restrictive, below it accommodative. If no estimate is found, say the stance cannot be placed against neutral and describe the real rate's direction instead.
   - The gap between the bank's path and the market's path, in basis points and by meeting where sources allow.
   Where the country shares a currency and a central bank (a euro-area member), the policy rate is the same across the area, so differentiate the country on growth, fiscal position and its sovereign spread against the area's benchmark. Where the currency is pegged, the anchor central bank's path is the relevant one. Done when the stance, the real rates with their inflation measure, the neutral range with its source or a not-found note, the two paths and their gap are stated.

5. **Debt dynamics.** The r minus g rule, a standard identity of public finance (not from the method files): the change in the debt ratio = (r - g) / (1 + g) x d - primary balance, where d is gross government debt over GDP, r the effective nominal interest rate on that debt (interest paid over the previous year's debt, derived), g nominal GDP growth, and the primary balance is the balance before interest as a share of GDP (surplus positive). The debt-stabilising primary balance = (r - g) / (1 + g) x d. Compute both from the latest year's figures and from the forecasts found, each input dated, with the working shown. When r is below g the debt ratio can fall with a primary deficit; when r rises above g, a primary surplus is needed, and the gap between the required and the actual primary balance is the fiscal adjustment the arithmetic implies. Done when r, g, d, the actual and the debt-stabilising primary balance are tabled with periods, and the gap is stated with its sign.

6. **External position.** The current account as a share of GDP; reserves in months of imports (reserves / monthly imports of goods and services, derived), read against the conventional three-month rule of thumb (an IMF convention, labelled as such); reserves against short-term external debt due within a year, read against cover of one (the Greenspan-Guidotti rule, labelled as such); and the external financing need over twelve months = current account deficit + external debt due (derived). Rules of thumb are conventions for emerging and pegged economies; for a reserve-currency issuer or a free float say they bind less. Then which balance, fiscal or external, would constrain policy first and what would trigger it, with the rating and outlook. Done when each external figure has its period and source, each rule of thumb is named as a convention, and the binding constraint is named.

7. **Country risk premium**, when the reader needs a cost of equity for the country (entry, a project, a valuation) or asks about country risk. Damodaran's approach, labelled assumed throughout: country risk premium = default spread x (equity market volatility / government bond volatility). Take the default spread from the sovereign's foreign-currency bond spread or CDS quoted in a dated search result, or, when the country has no such market, from a rating-based default spread quoted with its source and date. Take the volatility ratio from a dated source, or compute the equity side from the index's daily series, through the computing tool or the host's code execution, and say where the bond side came from. Add the premium to a mature-market equity risk premium named with its source. Done when the premium, each input, its source and date, and the assumed label are shown, or the step is marked not needed.

8. **Politics and policy.** The dated political events over the horizon, what each could change in fiscal, regulatory or trade policy, and how markets have priced it. Polls and odds quoted in the press are opinions, not probabilities. Done when each event has a date and a mechanism, and any probability has its basis as in step 9.

9. **Scenarios for the main uncertainty.** From rule 2 in `references/forecasting-discipline.md`, two or three cases for the question that decides the next twelve months (a recession or not, a policy turn, an election outcome), each with what has to be true, the indicator that would show it first, and a probability. Probabilities are judgment: integers that sum to 100, each with its reason drawn from named historical analogues found in the tearsheet's history and the news (an earlier hiking cycle, a past election, a previous currency crisis), never a default split and never an invented base rate. The reference classes in the method files are company and equity samples; they give no macro base rates, so say so rather than borrow one. Check that probabilities scale with the time window. Done when the cases, their analogues, their signposts and the probability-weighted reading are stated.

10. **Markets and what is priced in.** The equity index against its region and its own moving averages, the currency's performance and drivers, yields and spreads. Compare what markets price with the scenario probabilities and the range of forecasts, and say where the two differ and by how much. That gap is what would move prices if the scenarios are right; it is not a call. Done when each market line has a reading, a source and the comparison with the scenarios.

## Write

Follow `references/output-standard.md`.

```
# <Country>: country briefing, <date>
Data as of: releases to <date>; market data <date>; newest document <date>.
Scope: <angle, reader, horizon>.

## The view
Four to eight sentences: where growth, inflation and policy stand, the constraint that matters,
what markets price against the scenarios, the implication for the reader, and what would change
the reading. No allocation call.

## Facts
| Indicator | Latest | Prior | Trend | Comparison (target, consensus, G7) | Release date | Basis | Source |
GDP growth (real, nominal), CPI, core inflation, unemployment, policy rate (nominal, real),
10-year yield (nominal, real), currency, primary index, primary and overall fiscal balance, debt,
current account, reserves.

## Growth and inflation
Drivers; forecast ranges with sources.

## Monetary policy
Stance, last action, guidance quoted, real policy rate against the neutral range and its source,
the bank's path against the market's path.
[Euro-area member: the shared-rate note and the spread against the area benchmark.]

## Fiscal and external position
| Measure | Value | Period | Rule or comparison | Basis | Source |
(r, g, debt ratio, primary balance, debt-stabilising primary balance, reserves in months of
imports, reserves over short-term external debt, external financing need)
The binding constraint and the rating.

## Country risk premium                    (when needed)
Default spread, volatility ratio, premium; each input with source, date and the assumed label.

## Politics and policy
| Date | Event | What it could change | Probability and basis | Source |

## Scenarios
| Case | What has to be true | Analogue | First signal | Probability | Market reading if it happens |

## Markets and what is priced in
Equities, currency, rates and spreads; the comparison with the scenarios.

## Calendar
The next dated releases and decisions.

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages. A narrow question gets the relevant indicator or decision with its comparison, its date, the market's reading and the sources, and the footer.

## Checks before sending

1. Every indicator has a release date and a source, or reads "not available"; every figure comes from the tearsheet or a dated search result.
2. Facts, opinions and expectations are tagged where they appear and never merged in one sentence without labels.
3. Every rates and growth row says nominal or real; real rates name the inflation measure used.
4. The neutral range, the reserve and short-term debt rules of thumb and the r minus g identity are each labelled with their source or as a convention.
5. Forecasts are ranges with named sources, not single numbers.
6. The central bank's own path and the market's path are both stated, with their gap.
7. A euro-area member is differentiated on growth, fiscal position and spread, not on the shared policy rate.
8. Scenario probabilities are integers that sum to 100, each with a named analogue, and scale with the horizon; no base rate is invented.
9. No overweight, underweight, buy, sell or allocation language; a corporate reader gets the trade-offs, not a decision.
10. Nothing comes from memory or the open web without saying so in Gaps.

## Hand-offs

- Several countries, a region or a bloc compared, or a choice between countries for expansion or sourcing: `bigdata-macro-compare`. A sector inside the country: `bigdata-sector` with the country scope.
- Today's moves across markets: `bigdata-markets-today`. A theme such as reshoring or energy policy: `bigdata-theme`.
- After delivering, make one offer: a monitor on the country's central bank decisions and major releases, or save the briefing to the user's Bigdata.com account. Act only on a clear yes.
