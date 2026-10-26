---
name: bigdata-moat
description: >-
  Competitive advantage of one company: profit pool, share stability, pricing power, entry and
  exit, five forces, how long the advantage lasts. Use for moat, competitive position, barriers to
  entry. Not the whole industry: bigdata-sector.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, roic, base-rates, expectations
  bigdata-sector-primer: auto
---

# Moat

This skill answers whether a company's return above its cost of capital is likely to last, and for how long, in the sequence of Mauboussin and Callahan's "Measuring the Moat": the economics first, then the industry, then the company's own advantage, then how rivals behave and what could disrupt them. A moat has two dimensions, magnitude (the spread over the cost of capital times the capital that can earn it) and duration (how long the spread lasts). The output is a balance of evidence, an assumed duration in years bounded by base rates, and what would change it. It never gives a moat rating such as wide or narrow. A narrow question ("does Ferrari have pricing power?") gets that step with its evidence, not the full sequence.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-moat"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Fix the unit of analysis: the business unit the question is about, not the conglomerate ("Shell in LNG" is the integrated gas segment). A company with several units gets the sequence per material unit, aggregated at the end. Fix the industry and the peer set: the companies that compete for the same customers, from the filing's competition section and the screen, including private rivals and potential entrants where the evidence names them. The subject may be the user's own company ("how durable is our position"), a competitor, a supplier or a customer; write the implications for that reader.

Ask one question only if the unit is genuinely ambiguous (the user names a company with several businesses and no segment, and the segments have different economics). Otherwise take the largest segment by operating profit, state it in the header, and proceed. Done when the unit, the industry, the peer set and the reader are stated.

If the company is Private, use filings, news and research for the industry steps and say that the return tests rest on whatever statements Bigdata.com holds. For a bank or an insurer, judge ROE against the cost of equity in place of ROIC, and say the profit-pool and margin-and-turnover tests are adapted.

## Gather

The evidence plan follows the steps of `references/industry-structure.md` and its evidence table, one aspect and one period per search.

1. **The company's numbers.** Profile and quote, revenue by segment and geography, and the deal history; then five fiscal years of annual statements, ratios and key metrics. Done when five annual periods of revenue, EBIT, margins, invested capital, goodwill and the FactSet ROIC field are in hand, with segment revenue and the deal history (or a search for the deal history when the account lacks FactSet M&A).
2. **Peers.** The competitors block in the company profile, a screen on the industry and size, and competitors named in the filing; then five fiscal years of annual statements, ratios and key metrics for four to eight of them, pulled as a set rather than one company at a time where the account allows. Done when each peer has revenue, ROIC, margins and invested capital for the same five fiscal years, so the profit pool can be built for the start and the end of that window. The method's ten-year comparison is not available; say so in Gaps.
3. **The annual filing.** Search and fetch the latest annual report. Read the business section (competition, customers, suppliers, distribution), the risk factors, the segment note with segment assets, customer concentration, and patents and licences with their expiries. Done when each item is noted with its section, or marked not disclosed.
4. **The industry map and the forces** (method steps 2 and 8). Searches, one each: the named suppliers and how concentrated they are; the largest customers and their concentration; contract terms and switching; the regulators and licences that touch profit; substitutes and how fast they are improving. Done when every party on the map has at least one dated source or a gap.
5. **Shares** (method step 4). Searches for industry size and market shares now and five years ago, from research, filings and news. Done when shares exist for the main competitors in two years five years apart, with the coverage stated (listed companies only, or the full market).
6. **Pricing** (step 5). Searches for price increases, discounting, mix and volume response in transcripts and news over the last five years, and whether the industry passed on supplier cost increases. Done when the price trend is dated and cited.
7. **Rivalry, entry and exit** (steps 6 and 7). Searches for capacity additions, new entrants, exits, consolidating deals and price wars, one aspect each. Done when entrants and exits over five years are listed with dates.
8. **Source of advantage** (step 10). Searches for retention, churn, renewal rates, contract length, scale economics in purchasing or distribution, and patent expiries. Done when each claimed source has a disclosed figure or a gap.
9. **Disruption** (step 11). Searches for low-price entrants, new-market products and technology shifts in the industry. Done when the candidates are listed with dates or the searches found none.
10. **Management's own account.** Search and fetch the last two earnings calls for what management says about pricing, share and competitors, and what analysts pressed on. Done when the relevant exchanges are quoted.
11. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the profit-pool and persistence-and-fade subsections. Done when the sector's profit-pool and persistence figures are noted, or their absence is stated.

## Analyse

Load `references/industry-structure.md` before step 1, `references/roic.md` before step 2 and `references/base-rates.md` before step 13. Where a step names a method step, run it there; the line below keeps what this skill adds and the done condition.

1. **Unit, stage and class** (method step 1). Done when the unit, the phase and the class are stated with a reason each.

2. **The economics come first.** `references/roic.md` steps 1 to 11: ROIC with and without goodwill on the definition line, the spread over a stated cost of capital (assumed, the build shown once), and ROIC as margin times turnover over the five annual periods. Apply the two tests for advantage: a return above the cost of capital, and a return above competitors, both over a full cycle (for a cyclical, on three-to-five-year averages). Name whether the figures are hand-built or the FactSet field, and do not mix them. Done when the company and the peer median are tabled with the spread and the decomposition, and both tests are answered.

3. **Industry map** (method step 2). Done when the map table names each party and how it touches profit.

4. **Profit pool** (method step 3), over the five annual periods: the latest three-year average against the first year of the window, for the company and each peer, with the four-firm revenue ratio. Done when the table shows who gained or lost width and spread over the window.

5. **Share stability** (method step 4 and its formula), against the 2.0-point rule (Measuring the Moat, 2007 to 2012 data, historical). Done when one number, the firms it covers and a verdict are stated.

6. **Pricing power** (method step 5). Done when the price evidence is dated and cited and the margin change is split into price, mix and volume where disclosed.

7. **Concentration and rivalry** (method step 6). Done when HHI or the four-firm ratio is stated with its coverage and each rivalry item has evidence or a gap.

8. **Entry and exit, first among the forces** (method step 7, with the barrier checklist and the entry and survival base rates). Test it before the rest, because where barriers are low, entry pushes returns toward the cost of capital whatever the other forces show. Done when barriers are named with evidence and entrants and exits are listed.

9. **The remaining forces as root-cause tests** (method step 8). Done when the forces table has a one-line verdict and evidence for suppliers, buyers and substitutes.

10. **Value chain** (method step 9). Done when the activities that differ from peers are named.

11. **Source of advantage, tested against the numbers** (method step 10). Never accept a moat from brand, size or share alone. Done when the claimed source matches the margin-and-turnover split from step 2, or the mismatch is stated.

12. **Rivals' behaviour and the disruption test** (method step 11). Check any "this is the next X" analogy against the condition that made it work. Done when the rivals' behaviour is classed (repeated game with clear signals, or capacity race) and the main innovation threat is classed (sustaining, low-end disruptive or new-market disruptive), each with at least one dated source, and any analogy has been tested.

13. **Duration, bounded by base rates.** Set an assumed duration in years and a fade endpoint from the reversion table in `references/roic.md` (strong or weak advantage against strong or weak sector barriers). Then compute the bounds:
    - The sector's persistence as a half-life: half-life = period x ln 0.5 / ln r, with r the sector's four-year CFROI persistence from `references/base-rates.md` table 9 and period 4 (an r of 0.56 gives about 4.8 years). It is the time for half the spread over the sector mean to fade. CFROI is a proxy for ROIC; label it so.
    - The ten-year ROIC transition table in `references/roic.md` (US non-financials, 1995 to 2005) for the company's starting band.
    - The listed-company half-life of about ten years (1975 to 2009, historical).
    Take the shortest bound that the evidence supports as the ceiling for the assumed duration; a longer duration needs evidence from steps 8 to 12, named. Show the market-implied competitive advantage period (`references/expectations.md` table 2, about eight years on average, 1976 to 2007) next to the result as a comparison only, never as a bound, because the point is to judge the price against the fundamentals. Show the dispersion inside the industry, since segment-specific factors explain most of the variance for below-average firms (`references/industry-structure.md`, interpretation). Done when the years, the endpoint, the half-life arithmetic, the bound used and why, and the market-implied comparison are stated together.

14. **Erosion signals to watch** (the method's warning signs of erosion). Done when each signal that applies has the metric or source that would show it first.

For an emerging industry where shares are unstable, say the share tests are weak evidence. Where the duration matters for the price, say that the price-implied competitive advantage period is computed in `bigdata-valuation`.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) moat and industry structure: <unit>, <date>
Data as of: statements <latest fiscal period>; newest document <date>; peers <names>.

## The reading
Four to eight sentences: the spread and whether both tests pass over a cycle, the source of
advantage and whether the numbers show it, the assumed duration with its bounds, the main threat,
and what would change the reading. Implications for the reader named in scope. No moat rating.

## Economics
| Year | ROIC ex goodwill | ROIC incl goodwill | WACC (assumed) | Spread | Margin | Turnover | Peer median ROIC |
Basis and sources note and the definition line under the table; hand-built or FactSet named.

## The unit and its industry
Life-cycle phase and industry class with reasons.

## Industry map
| Party | Role | Concentration | Terms | How it touches profit | Basis | Source |

## Profit pool
| Firm | Share of capital, latest | Share of capital, FY-4 | Spread, latest | Spread, FY-4 | Economic profit | Basis | Source |
Four-firm ratio; coverage of the figures; the five-year window stated.

## Share stability and pricing power
The share-stability number and verdict; the price trend and the price, mix and volume split.

## Concentration, entry and exit
HHI or four-firm ratio with coverage; barriers with evidence; entrants and exits with dates;
the entry and survival base rates with their samples.

## Five forces
| Force | Verdict | Evidence | Basis | Source |
Entry first, then rivalry, suppliers, buyers, substitutes.

## Source of advantage
Type, the activities that differ from peers, and the margin-and-turnover signature against peers.

## Rivals and disruption
The interaction class and the disruption class with evidence.

## Duration
Assumed years, fade endpoint, the evidence, the half-life arithmetic and the bound used, each
labelled; the market-implied period beside it as a comparison.
| Erosion signal | What would show it first | Current reading | Basis | Source |

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. The cost of capital appears once, in an Assumptions line, with its basis and a sensitivity of plus and minus one point on the spread. For a narrow question, answer with the relevant step, its evidence and table, and the sources, and keep the footer.

## Checks before sending

1. Both tests are shown: return above the cost of capital and above peers, over a full cycle.
2. Entry and exit were tested before the other forces.
3. Every step of the sequence has evidence with a date and source, or a stated gap.
4. Share-stability, HHI and four-firm figures state the firms and the share of the market they cover.
5. The claimed source of advantage is checked against the margin-and-turnover split.
6. No claim of advantage rests on brand, size or share alone.
7. The duration is in years, with a fade endpoint; the sector persistence is converted to a half-life with the arithmetic shown; the shortest well-supported bound is used; the market-implied period appears only as a comparison.
8. No moat rating, score or "wide", "narrow" or "no moat" label; no recommendation.
9. Hand-built ROIC and the FactSet field are never mixed, and the definition line is shown.
10. Dated figures from the method carry their source and period and are called historical. No table passes eight columns.

## Hand-offs

- The user asks about management, incentives or what the company does with its cash: `bigdata-capital-allocation`.
- The user wants the structure of a whole sector rather than one company's position: `bigdata-sector`.
- The user wants what the price assumes about the duration, or a value range: `bigdata-valuation`.
- After delivering, make one offer: a monitor on the erosion signals (entrants, price cuts, capacity additions, customer losses) for the company and its main rivals, or save the report to the user's Bigdata.com account. Act only on a clear yes.
