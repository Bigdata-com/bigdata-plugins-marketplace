---
name: bigdata-sector
description: >-
  How an industry works: structure and profit pool, drivers and metrics, what is priced in, where
  a named company sits. Use for a sector or industry outlook, our industry, which sectors look
  interesting. Not a theme: bigdata-theme.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, base-rates, multiples-and-peers, operating-leverage-and-tam, expectations
  bigdata-sector-primer: auto
---

# Sector

This skill writes the sector note a reader needs before allocating attention to an industry or deciding how to compete in it: how the industry makes money and who keeps the profit, where it sits in its cycle, the few drivers and metrics that decide results, how long above-average returns have historically lasted in it, what the prices of its leading companies already assume, which companies matter and for what reason, and, when the user names one, where that company sits. The reader may be a portfolio manager, or a corporate strategy, finance or investor-relations team reading about its own industry. It covers one sector, several sectors on the same measures, or one sector inside a country. It is about the industry: one company's competitive advantage is `bigdata-moat`. It names no picks and makes no overweight or underweight call. "How do banks make money" gets the primer's economics with current figures for two or three banks, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-sector"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Establish five things before gathering data:

- **The sector and its sub-industries.** Map the user's words to a section of `references/sector-primers.md` (the contents list at the top names the sections) and to the sub-industries that sit under it. Analyse the profit pool at the sub-industry level, because a sector average hides who earns the return. "Tech" spans software, semiconductors and internet platforms, which have separate primers and different economics; cover each part the user meant.
- **The subject company**, if any: "my company", "our industry", "where does X sit". Resolve it to its Bigdata.com entity, put it in the depth set whatever its size, and add the section "Where <company> sits". Write the implications for that reader (the user's own company, a competitor, a customer, a supplier or a target).
- **The geography.** Default to the user's market when it is known, otherwise global, and state it. The screener covers primary listings on NASDAQ, NYSE, NYSE American and Toronto unless a country or exchange is passed, so a global scope needs a screen per major market, and the note says which markets were screened. With a country or region, the sector becomes the companies domiciled or operating there, and step 10 of the analysis applies. `bigdata-theme` uses the same default.
- **One sector or several.** For several, every sector gets the same measures so the comparison is like for like. "Which sectors look interesting" with no list is a triage, not twelve deep runs: rank the sectors first (Gather step 0), then run the full method for the three or four that stand out.
- **The angle.** A debate the user cares about, a holding, a cycle question, a competitive position. The note leads with it.

Ask one question only when the request could mean two sets of companies with different economics and nothing in it points to one. Otherwise state the assumption under the title and proceed. If the sector has no section in the primer bundle, say so in the Gaps line and build the metrics from the method files.

## Gather

Each step says what it must produce.

0. **Triage, for "which sectors look interesting" only.** The market overview's sector rows (performance over its standard windows), then one page of a screen per sector, largest names first, for the size and count of each. Rank the sectors on the measure the user named, or on recent performance and the spread between the sector's best and worst large names, and say which measure. Done when three or four sectors are chosen with the measure and the figures that chose them.
1. **The primer.** Find the sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read all of its subsections before any data call. Done when the value drivers, the metric definitions, the accounting traps, the persistence row, the valuation conventions, the mid-cycle guidance and the macro indicators to watch are noted.
2. **The universe.** A screen on the sector or industry, the geography and a market-cap floor, actively trading, ETFs excluded. The screener's sector labels differ from those of the entity lookup; use its own list. Outside the default exchanges pass a country or exchange, and keep one country per screen when market caps must be comparable, because currencies are not converted. Page through until the list is complete. Done when the companies covering most of the sector's market cap are listed, the share they cover and the exchanges screened are stated, and each is assigned to a sub-industry.
3. **The grid.** Price and market cap for the universe, in one pull for the set. Add surprise, target or sentiment columns only when the user asks for them, because they cap the grid at 100 names. Done when every company has a current market cap.
4. **The depth set.** Choose eight to fifteen companies per sector (five to eight per sector when comparing several): the largest by market cap, the ones whose returns stand out in either direction, any recent entrant with real share, and the subject company. For each: profile, key metrics and consensus; five fiscal years of annual statements and ratios; segment and geographic revenue with the rating counts and targets. Pull them as a set rather than one company at a time where the account allows. Done when five fiscal years of statements, the FactSet ROIC, margins, invested capital (equity for banks and insurers), consensus to at least two fiscal years with its vintage, the rating counts and targets, and segment and geographic revenue are in hand for each. Five annual periods may not span a full cycle; say so in Gaps rather than fetch older filings.
5. **Industry evidence.** Searches, one aspect and one period per call: industry size and market shares; pricing and price-cost spread; capacity additions, entrants and exits; regulation and policy; the live debates (research and news that state the bull and bear sides); the primer's leading indicators (orders, utilisation, inventories, rates). Fetch a document when a figure sits in a table the excerpt cuts off. Done when each step of the industry-structure method has evidence or a stated gap, and each debate has both sides with sources.
6. **Calendar.** The corporate calendar for the depth set's next reports and the sector's conferences, and the economic calendar for the macro releases the primer names. Done when the next dated events over three months are listed.
7. **Country backdrop**, only with a country scope. The country's economic overview. Done when growth, inflation, the policy rate, the currency and the macro sections the sector depends on (housing for building materials, retail sales for retailers) are in hand with dates.

## Analyse

1. **Structure and profit pool.** From `references/industry-structure.md`, steps 1 to 8, per sub-industry: the life-cycle phase and industry class; the industry map; the profit pool for the latest fiscal year and the earliest of the five annual periods, with width as each company's share of the sub-industry's invested capital and height as ROIC minus an assumed cost of capital; the four-firm ratio or HHI with the share of the market it covers; share stability; the price trend; entry and exit, tested first among the forces; and the remaining forces as root-cause tests. Use the FactSet ROIC field for every company, name it once, and show the spread at the cost of capital plus and minus one point; set the cost of capital as the inputs table of `references/expectations.md` says. Banks and insurers: width is each company's share of the sub-industry's equity, height is ROE minus the cost of equity, as the primer says. Done when the profit pool table shows who holds the width, who earns the spread and who gained or lost each over the five years, and the forces table has a verdict and evidence per force.

2. **Cycle position.** For a cyclical sector (the primer's mid-cycle section says which), take margins and ROIC over the five annual periods, set the mid-cycle margin from the primer's mid-cycle guidance and the long-run trend rather than at a peak or trough, and compare the latest margin and the consensus margin with it. Read the primer's leading indicators for direction. Label each sub-industry early, mid or late cycle, or not cyclical, with the evidence. State that a forward P/E on peak earnings looks low and on trough earnings looks high, and widen ranges at turning points. Done when the latest, consensus and mid-cycle margins sit in one table with the basis for mid-cycle labelled assumed.

3. **Drivers and metrics.** From the primer's metric table, the three to five drivers that decide the sector's results now, each with its latest reading across the depth set where disclosed, the direction, and the source. From `references/operating-leverage-and-tam.md` and the operating margin beta in `references/base-rates.md`, state what a stated change in sector sales does to operating profit, and say where the companies' own cost structures differ from the sector beta. Done when the driver table is complete and each driver has dated evidence.

4. **Persistence and fade.** From `references/base-rates.md` (tables 6 to 9), the sector's persistence figures for gross profitability, operating margin and CFROI, with the sample label; the tables use their own sector names (consumer staples, information technology, telecom services), so name the row used. For the leaders, the expected margin in five years as sector mean plus r times the gap, and the reversion of returns with the CFROI r applied to ROIC labelled judgment. Done when the fade table carries the sample and period and says which leaders sit furthest from the mean.

5. **What is priced in.** From `references/expectations.md`, for three to six leaders: forward P/E against the steady-state P/E (formula 1), the NOPAT growth the enterprise value implies (formula 2, with ROIIC as a three-year rolling figure, the most five annual periods allow) against consensus, and the share of value that rests on future value creation. Place consensus growth in its size class from `references/base-rates.md` table 2, three-year column. At the sector level, the median forward multiple from `references/multiples-and-peers.md` against the sector's own history, compared only at a similar point in the cycle and paired with ROIC. Banks: price to book against ROE. Done when each leader has implied growth against consensus with its base-rate share, and the note can say in two sentences whether the bar for the sector is high or low.

6. **The companies that matter and why.** Name each by its role, with the number behind it: holds the widest part of the profit pool at a positive spread; gaining width or spread; a large company earning below its cost of capital; the marginal producer that sets price in a commodity industry; the entrant or disruptor; the company whose next report settles a live debate. Done when every named company has a role, a figure and a source. This is a map of the industry, not a list of picks.

7. **Where the subject company sits**, when the user named one. Its share of sub-industry revenue and invested capital, its margin, ROIC (or ROE) and forward multiple, each against the sub-industry median and range from the depth set, its place in the profit pool and its direction over the five years, and which forces and debates bear on it most. Done when each measure sits against the median with its source, and two or three sentences say what the position means for that reader.

8. **The debates.** Two to four live debates, each with both sides, where consensus sits (estimates, targets, the price-implied bar), the evidence that would settle it and when that evidence arrives. Done when each debate has a dated signpost.

9. **Several sectors.** Put every sector on the same rows: profit pool spread and its direction, cycle position, persistence r, forward multiple against its own history at a comparable cycle point, implied growth against consensus, and the base-rate share for that growth. Order the table by a measure the user chose, or by the spread, and say which. Do not rank sectors by attractiveness. Done when the comparison table is complete with a Basis and sources note.

10. **A sector within a country.** Confirm each company's exposure from geographic revenue, so a listing in the country is not mistaken for business there. Link the country backdrop to the sector's drivers, cover the policy that shapes the outcome (subsidies, tariffs, foreign-ownership rules, regulated returns), and set the companies' multiples and returns against global peers in the same sub-industry so a country premium or discount is visible. Done when the exposure column and the global comparison exist.

## Write

Follow `references/output-standard.md`.

```
# <Sector> [in <country>]: sector note, <date>
Data as of: prices <date>; estimates <date>; statements <latest period>; newest document <date>.
Scope: <sub-industries, geography and exchanges screened, companies covered and their share of sector market cap>.

## The view
Four to eight sentences: how the sector makes money and who keeps it, the cycle position, the
two drivers that matter now, whether the price-implied bar is high or low, where the subject
company sits if one was named, and what would change the reading. No rating word.

## How the industry makes money
The primer's economics applied to the latest figures; the industry map.

## Structure and profit pool
| Company | Sub-industry | Share of invested capital | ROIC | Spread | Economic profit | Change over five years | Basis |
Sources in a note under the table. Concentration line with coverage; share stability; the forces
table (force, verdict, evidence, source).

## Where <company> sits                   (when the user named one)
| Measure | <Company> | Sub-industry median | Range | Basis | Source |
(share, margin, ROIC or ROE, forward multiple, profit-pool position); what it means for the reader.

## Cycle position
| Sub-industry | Latest margin | Consensus margin | Mid-cycle margin | Position | Basis | Source |
Leading indicators with dates.

## Drivers and metrics
| Driver | Metric | Latest reading | Direction | Basis | Source |
The sales-to-profit sensitivity, inside view and sector beta.

## Persistence and fade
The sector's r values with the sample label; the leaders' expected margins and returns.

## What is priced in
| Company | Forward P/E | Steady-state P/E | Implied growth | Consensus growth | Base-rate share | Basis | Source |
Sector multiple against its own history at a comparable cycle point. Two closing sentences.

## Companies that matter
One line each: role, figure, source.

## Debates and signposts
Each debate: both sides, where consensus sits, the evidence that settles it, its date.

## Accounting traps
The primer's traps that apply to the companies covered, with any found in the filings read.

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Several sectors: replace the single-sector tables with the comparison table from step 9 and one short section per sector; a triage adds one line per sector screened out, with the figure that ruled it out. A sector within a country adds a "Country backdrop" section after the view and an exposure column in the companies table. Length: four to eight pages. A narrow question gets the relevant step with its table and sources, and the footer.

## Checks before sending

1. The primer section was read, or its absence is stated in Gaps.
2. The universe states its coverage (count, share of market cap, geography, exchanges screened, as-of date).
3. The profit pool is built per sub-industry over the five annual periods, with one ROIC definition for every company (equity and ROE for banks and insurers) and the cost of capital stated as assumed with a sensitivity.
4. A cyclical sector shows the mid-cycle margin next to the latest and consensus margins, and Gaps says the series stops at five years.
5. Every persistence or base-rate figure carries its sample and period and is not presented as current.
6. "What is priced in" covers named leaders with implied growth against consensus.
7. A named subject company sits against the sub-industry median on every measure, written for the user's role.
8. Every named company has a role and a figure; no picks list, no overweight, underweight or rating language.
9. Several sectors sit on identical rows; a country scope confirms exposure from geographic revenue.
10. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- A theme that cuts across sectors: `bigdata-theme`. One company in depth: `bigdata-deep-dive`; its peers on multiples: `bigdata-comps`; one company's competitive advantage and its duration: `bigdata-moat`.
- A deal that would change the industry's structure: `bigdata-deal-analysis`.
- A country's economy rather than a sector in it: `bigdata-country`. Companies that fit criteria: `bigdata-screen`.
- After delivering, make one offer: save the companies that matter as a Bigdata.com watchlist, or a monitor on the sector's debates. Act only on a clear yes.
