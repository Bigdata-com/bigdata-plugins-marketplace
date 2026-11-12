---
name: bigdata-country-analysis
description: >-
  One country's economy and markets, or several compared on the same indicators: growth, inflation,
  rates, currency, fiscal and external balances, politics, what is priced in. Use for a country
  outlook, political risk, market entry, compare economies, which country is stronger, where to
  expand.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, forecasting-discipline
  bigdata-sector-primer: none
---

# Country analysis

Never an allocation call, overweight or underweight, and never a single-number forecast: where growth, inflation and policy stand, what constrains them, and what markets already price, for one country or several on the same indicators. A decision about operating in a country is a different question and leads with its own arithmetic: market entry with demand growth, the currency path, the country risk premium and the rules on foreign ownership, capital movement and repatriation; currency exposure with the real rate differential, the external position and reserves; sourcing with trade policy, export controls, energy, labour and dated disruptions; a choice between countries with the options side by side and no choice made for the reader. Size the work to the question: "what did the Bank of Japan do yesterday" gets the decision, the statement's key line and what the market priced before and after; "how does euro-area inflation compare with the US" gets the two rows with their periods, the reason for the gap and the sources, not the full briefing.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-country-analysis"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **Facts, opinions and expectations kept apart in the writing.** Releases and decisions are facts; forecasts, official guidance, ratings and neutral-rate estimates are opinions, written as the named source's view; the priced rate path, breakevens, the sovereign spread, currency forwards and the index multiple are what the market expects, written as what it prices. Country notes most often go wrong by blending the three (`references/forecasting-discipline.md`, facts, opinions and expectations).
- **Nominal or real, said every time.** Every growth figure and rate says which it is, and every real figure names its inflation measure: headline or core year on year, or expected inflation when a dated forecast or breakeven is quoted. The real figure sits beside the nominal wherever inflation is high enough or different enough across countries to change the reading, and always for the policy stance.
- **The stance against a neutral range, when the question reaches policy.** The real policy rate set against a neutral real-rate range from the central bank's own estimate or dated research, always a range because the neutral rate is not observed. With no estimate found, say the stance cannot be placed and describe the real rate's direction. Then the bank's projected path against the path the market prices, the gap in basis points by meeting where sources allow.
- **Forecasts as a range across named sources**, with the spread from highest to lowest. Beyond about a year, scenarios and signposts replace point forecasts, because forecast accuracy decays past that horizon. The default horizon is twelve months, stated.
- **Debt dynamics by the interest rate against growth, when the question reaches fiscal room.** The change in the debt ratio = (r - g) / (1 + g) x d - primary balance, and the debt-stabilising primary balance = (r - g) / (1 + g) x d, with d gross debt over GDP, r the effective nominal rate (interest paid over the previous year's debt) and g nominal GDP growth. The gap between the required and the actual primary balance is the adjustment the arithmetic implies; where r has moved above g, fiscal room goes fastest. The inputs appear once on the page so the reader can rebuild the figure.
- **External tests, where they bind.** For emerging and pegged economies, or when the question reaches the external position: reserves in months of imports against three months; reserves against external debt due within a year against cover of one; the twelve-month financing need as the current account deficit plus external debt due. They bind less for a reserve-currency issuer or a free float, and there they stay in the working. Then which balance, fiscal or external, constrains policy first, as a sentence with its evidence.
- **A country risk premium only when the reader needs a cost of equity** (entry, a project, a valuation): the default spread times equity volatility over government bond volatility, the spread from a dated sovereign bond spread or CDS quote or a rating-based spread with its source, added to a mature-market equity risk premium named with its source. It is one stated figure with its inputs in a single clause.
- **A shared currency or a peg.** A euro-area member shares the area's policy rate, so it is differentiated on growth, fiscal position and its spread against the area's benchmark yield; a pegged currency follows its anchor's path.
- **Several countries on the same indicators**, the ones the question turns on, with the period of every figure, because release calendars differ and a quarter-old reading is not this month's. A region names the economies used and says a regional figure is an unweighted median unless a source gives a weighted aggregate; "a global overview" with no members means the G7 plus China and India, and the note says so. Where equity returns are compared, they appear in local and in one common currency.
- **Divergences explained from sources or called unexplained**, never given an invented cause.
- **A common shock measured, not described, when the question is how one shock lands across countries.** Measure it through the channels that carry it to each member, such as trade openness, the commodity trade balance, the external financing need and the policy room left by the real rate and the debt dynamics.
- **"Which looks stronger" on named dimensions** (growth momentum, inflation against target, fiscal room, external balance, policy room), ordered on a dimension the user chose. The dimensions are never combined into one score or a ranking by attractiveness.
- **Scenarios when the question turns on an uncertain event.** Two or three cases for the question that decides the horizon, each with the indicator that shows it first. The cases partition the outcomes, and each indicator used (the policy rate, inflation, the currency) has one cut-off across the note. Probabilities are integers that sum to 100 and start from how often the outcome followed in named earlier episodes (an earlier hiking cycle, a past election, a previous currency crisis), scaled to the window, never a default split; equity samples do not transfer to macro questions (`references/forecasting-discipline.md`, scenario weights from a reference class). Polls and betting odds quoted in the press are opinions, not probabilities. When forecasters or the market sit away from official guidance on the variable that matters, their figure is the bar the cases are cut on.
- **What is priced against the scenarios, where there are scenarios.** The probability-weighted path (rate, spread, currency) is stated, reconciles with the cases, and is set against what the market prices; the gap is what would move prices if the scenarios hold, not a call.

## Where it goes wrong

- **A risk-free rate taken from memory** when the country data carries the current 10-year yield.
- **A member dropped from a row** to make a comparison table look complete. Keep the member and say under the table which reading was not found, because a silent drop changes the comparison.
- **Yields of different dates read as one moment.** Non-US 10-year yields come from documents at their own dates; say so in the row.
- **Market-snapshot changes misread.** Its multi-day columns run from its own refresh time, not a Friday close, and its yield changes are percent of the yield, not basis points.
- **A euro-area member analysed on the shared policy rate**, which says nothing about that member.
- **A gap declared too early.** Sovereign spreads, the priced rate path and neutral-rate estimates have no structured field but are often in news and research; search before stating a gap.

## What the data has, and does not

The country data gives, per country, the latest readings for growth, labour, inflation, sentiment, trade, credit, the central bank and fiscal policy with release dates, consensus and surprise; a G7 comparison table; the primary index with its moves and moving averages; the currency's spot, performance by horizon and cross rates; upcoming events; and, for the United States only, the Treasury curve. The euro area is covered as a whole; a country it does not cover is built from documents, each indicator cited to its source. The risk-free rate and inflation for a currency come from it, never from memory while the tool is there. Outside the United States there is no structured field for sovereign yields, spreads and CDS levels, the market-priced rate path (there are no futures or swap prices), neutral-rate estimates, rating actions, debt maturities or foreign-ownership and capital rules; news, research and filings often carry them, so search before stating a gap. A market snapshot puts currencies, indexes and US Treasury yields at one moment. The economic calendar carries central bank meetings and major releases; budget and election dates come from news. A volatility ratio needs the index's daily series.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Brazil: real rates near 9 percent leave room to cut, the fiscal path does not"). The opening answers the question first: where growth, inflation and policy stand, the constraint that matters, and what markets price against the scenarios, as far as the question asks; for several countries, the main divergences and their reasons instead. The body follows the question, the user's parts in the user's order, every rate and growth figure saying nominal or real and a comparison carrying the period of each figure. What would change the reading closes the note. Sub-headings state the finding ("Reserves cover five months of imports"), never the step.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- Every rate and growth figure says nominal or real, and every real rate names its inflation measure.
- In a comparison, every figure carries its period, mixed-date yields are noted, and no dimension is folded into a combined score.
- Every number in the opening agrees with its table, and where there are scenarios, each indicator has one cut-off and the probability-weighted path matches the cases.
- No stance, constraint or judgment appears as a label or a bolded category; each is a sentence with its evidence.
- Every acronym or programme name (a facility, a fiscal rule) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
