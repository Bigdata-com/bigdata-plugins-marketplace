---
name: bigdata-moat
description: Industry structure and competitive advantage from Bigdata.com data: the industry map, the profit pool and where it is moving, share stability, pricing power, concentration, entry and exit, the five forces with evidence, the source of advantage and how long it lasts, and the disruption test. Use when the user asks about a company's moat, competitive position, industry structure, barriers to entry, or pricing power. Not for governance and incentives, which bigdata-capital-allocation covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, roic, base-rates, expectations
  bigdata-sector-primer: auto
---

# Moat

This skill answers whether a company's return above its cost of capital is likely to last, and for how long, in the sequence of Mauboussin and Callahan's "Measuring the Moat": the economics first, then the industry, then the company's own advantage, then how rivals behave and what could disrupt them. A moat has two dimensions, magnitude (the spread over the cost of capital times the capital that can earn it) and duration (how long the spread lasts). The output is a balance of evidence, an assumed duration in years bounded by base rates, and what would change it. It never gives a moat rating such as wide or narrow. A narrow question ("does Ferrari have pricing power?") gets that step with its evidence, not the full sequence.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-moat"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Fix the unit of analysis: the business unit the question is about, not the conglomerate ("Shell in LNG" is the integrated gas segment). A company with several units gets the sequence per material unit, aggregated at the end. Fix the industry and the peer set: the companies that compete for the same customers, from the filing's competition section and the screen, including private rivals and potential entrants where the evidence names them.

Ask one question only if the unit is genuinely ambiguous (the user names a company with several businesses and no segment, and the segments have different economics). Otherwise take the largest segment by operating profit, state it in the header, and proceed.

If the company is Private, use filings, news and research for the industry steps and say that the return tests rest on whatever statements Bigdata.com holds. For a bank or an insurer, judge ROE against the cost of equity in place of ROIC, and say the profit-pool and margin-and-turnover tests are adapted.

## Gather

The evidence plan follows the method's steps, one aspect and one period per search. Each step says what it must produce.

1. **Company tearsheet.** `bigdata_company_tearsheet` with `sections` set to `company_overview, revenue_segmentation, mergers_acquisitions` first, then `fundamentals`, then `jobs_data`. Request the five fiscal periods before the latest five if the tool's period controls allow it. Done when five to ten years of revenue, EBIT, margins, invested capital, goodwill and the FactSet ROIC field are in hand, with five years of segment revenue and the deal history.
2. **Peers.** `bigdata_screen_companies` on the industry and size, plus competitors named in the filing, then `bigdata_company_tearsheet` with `fundamentals` for four to eight of them. Done when each peer has revenue, ROIC, margins and invested capital for the same years, so the profit pool and the peer comparison can be built for today and, where the history allows, five and ten years ago.
3. **The annual filing.** Search and fetch the latest annual report. Read the business section (competition, customers, suppliers, distribution), the risk factors, the segment note with segment assets, customer concentration, and patents and licences with their expiries. Done when each item is noted with its section, or marked not disclosed.
4. **The industry map and the forces** (method steps 2 and 8). Searches, one each: the named suppliers and how concentrated they are; the largest customers and their concentration; contract terms and switching; the regulators and licences that touch profit; substitutes and how fast they are improving. Done when every party on the map has at least one dated source or a gap.
5. **Shares and the profit pool** (steps 3 and 4). Searches for industry size and market shares now and five years ago, from research, filings and news. Done when shares exist for the main competitors in two years five years apart, with the coverage stated (listed companies only, or the full market).
6. **Pricing** (step 5). Searches for price increases, discounting, mix and volume response in transcripts and news over the last five years, and whether the industry passed on supplier cost increases. Done when the price trend is dated and cited.
7. **Rivalry, entry and exit** (steps 6 and 7). Searches for capacity additions, new entrants, exits, consolidating deals and price wars, one aspect each, plus rivals' hiring from `jobs_data` or news. Done when entrants and exits over five years are listed with dates.
8. **Source of advantage** (step 10). Searches for retention, churn, renewal rates, contract length, scale economics in purchasing or distribution, and patent expiries. Done when each claimed source has a disclosed figure or a gap.
9. **Disruption** (step 11). Searches for low-price entrants, new-market products and technology shifts in the industry. Done when the candidates are listed with dates or the searches found none.
10. **Management's own account.** Search and fetch the last two earnings calls for what management says about pricing, share and competitors, and what analysts pressed on. Done when the relevant exchanges are quoted.
11. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read its profit-pool and persistence sections.

## Analyse

Load `references/industry-structure.md` before step 1, `references/roic.md` before step 2 and `references/base-rates.md` before step 13. Each step ends in what it must produce.

1. **Unit, stage and class.** Place the unit in a life-cycle phase (innovation, fading, mature, subpar) with a reason, and class the industry (fragmented, emerging, mature, declining, international, network, hypercompetitive) (method step 1). Done when the unit, the phase and the class are stated.

2. **The economics come first.** From `references/roic.md`: ROIC with and without goodwill on the method's definition line, the spread over a stated cost of capital (assumed, with the build shown once), and ROIC as margin times turnover over five to ten years. Apply the two tests for advantage: a return above the cost of capital, and a return above competitors, both over a full cycle. Name whether the figures are hand-built or the FactSet field, and do not mix them. Done when the company and the peer median are tabled with the spread and the decomposition, and both tests are answered.

3. **Industry map.** Suppliers, customers, complementors, regulators and potential entrants, firms in order of dominance, payment terms and incentives between them, labour and regulation (method step 2). Done when the map table names each party and how it touches profit.

4. **Profit pool.** Width is each firm's share of industry invested capital, height is ROIC minus WACC, area is economic profit, on three to five year averages, for today and five and ten years ago where the data allows (method step 3). Add the four-firm revenue ratio. Read who holds the width, whether high-spread firms are gaining width or only spread, and which wide firms destroy value. Done when the table shows who gained or lost width and spread.

5. **Share stability.** Average absolute five-year change in share across competitors (the method's formula), against the rule that 2.0 points or less is stable (Measuring the Moat, 2007-2012 data, verify). Done when one number, the firms it covers and a verdict are stated.

6. **Pricing power.** Five-year price trend of the product and the split of each margin change into price, mix and volume; whether supplier cost increases were passed on (method step 5). Done when the price evidence is dated and cited.

7. **Concentration and rivalry.** HHI or the four-firm ratio with the coverage stated; similarity of goals and ownership; asset specificity; demand variability with high fixed costs; industry growth (method step 6). Done when each item has evidence or a gap.

8. **Entry and exit, first among the forces.** Threat of entry is the most important force, so test it before the rest: barriers from the method's checklist (asset specificity, minimum efficient scale against market size, excess capacity, reputation, precommitment contracts, licences and patents, learning curve, network effects, exit barriers), entrants and exits over five years, and the entry and survival base rates in the method's reference table. Where barriers are low, entry pushes returns toward the cost of capital whatever the other forces show. Done when barriers are named with evidence and entrants and exits are listed.

9. **The remaining forces as root-cause tests.** Suppliers, buyers and substitutes with the method's diagnostic questions (step 8), each with a one-line verdict and its evidence. Done when the forces table is complete.

10. **Value chain.** Map the activities against peers; a chain that looks like the peers' means competition to be the best, and price wars (method step 9). Done when the activities that differ from peers are named.

11. **Source of advantage, tested against the numbers.** Production (process or scale; signature: lower gross margin, high asset turnover), consumer (habit, experience goods, switching costs, network effects; signature: high gross margin), external (licences, regulation, tariffs), or efficient scale (method step 10). A brand counts only if it raises willingness to pay or lowers supplier cost. Never accept a moat from brand, size or share alone. Done when the claimed source matches the margin-and-turnover split from step 2, or the mismatch is stated.

12. **Rivals' behaviour and the disruption test.** Repeated game with clear signals or a capacity race; innovation classed as sustaining, low-end disruptive or new-market disruptive; whether products overshoot customer needs, competition is shifting to speed and convenience, or components are modularising (method step 11). Check any "this is the next X" analogy against the condition that made it work. Done when one verdict is written with its evidence.

13. **Duration, bounded by base rates.** Set an assumed duration in years and a fade endpoint from the reversion table in `references/roic.md` (strong or weak advantage against strong or weak sector barriers: toward the sector average or toward the cost of capital). Bound it with the sector's four-year CFROI persistence r from `references/base-rates.md` table 9 (global companies, 1983-2015; CFROI is a proxy for ROIC and is labelled so), the ten-year ROIC transition table in `references/roic.md` (US non-financials, 1995 to 2005), the listed-company half-life of about ten years and the market-implied competitive advantage period of about eight years (about five in very competitive industries, about fifteen in stable ones; 1976-2007, verify). A duration longer than these needs evidence from steps 8 to 12. Industry explains about 44 percent of the variance in sustained high profits and segment-specific factors 90 percent or more for below-average firms (McGahan and Porter, 1981-1994), so show the dispersion inside the industry. Done when the years, the endpoint, the evidence and the base rates are stated together.

14. **Erosion signals to watch.** From the method's warning signs: costs not passed through, share lost to entrants in core segments, rising customer concentration, ROIC falling while revenue grows, rivals copying faster, staff leaving for competitors, suppliers or distributors integrating. Done when each signal that applies has the metric or source that would show it first.

For a cyclical, judge returns on three to five year averages. For an emerging industry where shares are unstable, say the share tests are weak evidence. Where the duration matters for the price, say that the price-implied competitive advantage period is computed in `bigdata-valuation`.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) moat and industry structure: <unit>, <date>
Data as of: statements <latest fiscal period>; newest document <date>; peers <names>.

## The reading
Four to eight sentences: the spread and whether both tests pass over a cycle, the source of
advantage and whether the numbers show it, the assumed duration with its bounds, the main threat,
and what would change the reading. No moat rating.

## Economics
| Year | ROIC ex goodwill | ROIC incl goodwill | WACC (assumed) | Spread | Margin | Turnover | Peer median ROIC | Basis | Source |
The definition line under the table; hand-built or FactSet named.

## The unit and its industry
Life-cycle phase and industry class with reasons.

## Industry map
| Party | Role | Concentration | Terms | How it touches profit | Source |

## Profit pool
| Firm | Share of industry capital | ROIC - WACC | Economic profit | Five years ago | Ten years ago | Basis | Source |
Four-firm ratio; coverage of the figures.

## Share stability and pricing power
The share-stability number and verdict; the price trend and the price, mix and volume split.

## Concentration, entry and exit
HHI or four-firm ratio with coverage; barriers with evidence; entrants and exits with dates;
the entry and survival base rates with their samples.

## Five forces
| Force | Verdict | Evidence | Source |
Entry first, then rivalry, suppliers, buyers, substitutes.

## Source of advantage
Type, the activities that differ from peers, and the margin-and-turnover signature against peers.

## Rivals and disruption
The interaction verdict and the disruption class with evidence.

## Duration
Assumed years, fade endpoint, the evidence, and the base rates that bound it, each labelled.
| Erosion signal | What would show it first | Current reading | Source |

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. The cost of capital appears once, in an Assumptions line, with its basis and a sensitivity of plus and minus one point on the spread. For a narrow question, answer with the relevant step, its evidence and table, and the sources, and keep the footer.

## Checks before sending

1. Both tests are shown: return above the cost of capital and above peers, over a full cycle.
2. Entry and exit were tested before the other forces.
3. Every step of the sequence has evidence with a date and source, or a stated gap.
4. Share-stability, HHI and four-firm figures state the firms and the share of the market they cover.
5. The claimed source of advantage is checked against the margin-and-turnover split.
6. No claim of advantage rests on brand, size or share alone.
7. The duration is in years, with a fade endpoint, and is bounded by the sector persistence figure, the half-life and the market-implied period, each with its sample and period.
8. No moat rating, score or "wide", "narrow" or "no moat" label; no recommendation.
9. Hand-built ROIC and the FactSet field are never mixed, and the definition line is shown.
10. Dated figures from the method carry "(verify)" and their period.

## Hand-offs

- The user asks about management, incentives or what the company does with its cash: `bigdata-capital-allocation`.
- The user wants the structure of a whole sector rather than one company's position: `bigdata-sector`.
- The user wants what the price assumes about the duration, or a value range: `bigdata-valuation`.
- After delivering, make one offer: a monitor on the erosion signals (entrants, price cuts, capacity additions, customer losses) for the company and its main rivals, or save the report to the user's Bigdata.com account. Act only on a clear yes.
