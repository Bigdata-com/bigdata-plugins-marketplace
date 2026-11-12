---
name: bigdata-moat
description: >-
  Competitive advantage of one company: profit pool, share stability, pricing power, entry and
  exit, five forces, how long the advantage lasts. Use for moat, competitive position, barriers to
  entry. Not the whole industry: bigdata-sector.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, roic, valuation, base-rates, expectations
  bigdata-sector-primer: auto
---

# Moat

A note on whether a company's return above its cost of capital is likely to last and for how long, for someone who will act on it: the balance of evidence, a duration in years with its bounds, and what would change it. Never a moat rating ("wide", "narrow", "no moat" or a score) and never a call on the stock. A moat has two dimensions, magnitude (the spread times the capital that can earn it) and duration. Size the work to the question: "does Ferrari have pricing power" gets the five-year price trend, the margin change split into price, mix and volume, and whether cost increases were passed on, not the profit pool or the duration.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-moat"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a note that answers it with fewer tables and tests is the better note.
- **The business unit, not the conglomerate.** The unit the question is about ("Shell in LNG" is the integrated gas segment); without one named, the largest segment by operating profit, and the note says which. Several material units each get the tests, brought together at the end (`references/industry-structure.md`, industry map).
- **The economics before the story.** Two tests over a full cycle: a return above the cost of capital and a return above competitors, on three-to-five-year averages for a cyclical. ROIC built from the statements, with and without goodwill, against the peer median, split into margin and turnover where the split shows the source of advantage, and economic profit in currency, because value needs the spread and the capital deployed at it (`references/roic.md`, ROIC decomposition and ROIIC and the spread). The cost of capital is one stated figure, with the yield, beta and premium in a single clause and no regression statistics, and the spread is shown a point either way (`references/valuation.md`, cost of capital).
- **The profit pool, when the question is who keeps the industry's profit,** because a share chart hides whether share earns its cost of capital: each firm's share of industry invested capital against its spread over the cost of capital, the latest three-year average against the start of the window, with the four-firm revenue ratio, so the reader sees who gained or lost (`references/industry-structure.md`, profit pool and concentration and HHI). Otherwise it stays in the working.
- **Share stability, when share is offered as evidence of the moat,** as one number: the average absolute change in share over five years, set against the two-point line that separates stable from unstable, with the firms it covers and the share of the market they hold, said in a sentence (`references/industry-structure.md`, share stability).
- **Pricing power from prices, not margins alone, when pricing is the claimed advantage or the question.** The five-year price trend, each margin change split into price, mix and volume, and whether supplier cost increases were passed on (`references/industry-structure.md`, pricing power).
- **Entry and exit tested first among the forces,** because where barriers are low, entry pushes returns toward the cost of capital whatever the other forces show. Barriers named with evidence, entrants and exits with dates, set against how often entrants survive. Another force earns a line only where it bears on how long the return lasts, tested on root causes and never given an attractiveness grade; otherwise the forces stay in the working (`references/industry-structure.md`, entry and exit and bargaining power).
- **The claimed source of advantage checked against the numbers.** Production advantages show as lower gross margin and high turnover, consumer advantages as high gross margin; a brand counts only if it raises willingness to pay or lowers supplier cost. Retention, churn, contract length and patent expiries where disclosed (`references/industry-structure.md`, moat tests).
- **Rivals and the disruption threat described, not classed.** Whether rivals behave as a repeated game with clear signals or race for capacity, and whether the main innovation threat improves the incumbents' product, attacks from the low end or opens a new market, each written as a plain sentence with its dated evidence, never as a label; any "this is the next X" analogy tested against the condition that made the first case work (`references/industry-structure.md`, disruption signs).
- **Duration in years, bounded by history.** A duration and the level the return fades to, then the bounds, worked: the sector's four-year cash-return persistence converted to a half-life in years (period times ln 0.5 over ln r, so r of 0.56 over four years gives about 4.8 years), the ten-year ROIC transition for the company's starting band, and the listed-company half-life of about ten years. The shortest well-supported bound is the ceiling, and a longer duration names its evidence. The page carries the duration, the fade level and the bound that limits them, in a sentence; where the sector figure sets the bound, the note says once in plain words that it measures cash returns rather than ROIC, and the other bounds stay in the working unless they change the reading (`references/industry-structure.md`, competitive advantage period; `references/roic.md`, persistence and reversion; `references/base-rates.md`, CFROI by sector). The period the price implies sits beside the result as a comparison only, because using it as a bound tests the price against itself (`references/expectations.md`, implied competitive advantage period).
- **Erosion signals with what would show them first:** costs not passed through, share lost to entrants in core segments, rising customer concentration, ROIC falling while revenue grows, suppliers or distributors integrating.
- **Special cases.** Banks and insurers on return on equity against the cost of equity, with the profit-pool and margin-and-turnover tests adapted. In an emerging industry shares are unstable, so the share tests are weak evidence and the barrier and moat tests carry the weight (`references/industry-structure.md`, limits).

## Where it goes wrong

- **A moat accepted from brand, size or share alone.** The spread over a cycle against peers, with the margin and turnover signature, is the evidence.
- **Concentration figures without coverage.** Listed peer sets are older, larger and survivor-biased and miss private rivals; every share, HHI and four-firm figure says which firms it covers and what share of the market they hold.
- **Persistence quoted as a correlation.** A reader cannot use an r; it becomes a half-life in years.
- **The period the price implies used as a bound** on the duration.
- **A vendor ROIC field and a hand-built ROIC mixed** in one table. They differ in tax rate, goodwill and leases; the note says which one each line uses.
- **A ten-year profit pool claimed.** Five annual periods per company allow the latest three years against the start of a five-year window, no more.
- **Citations assembled at the end.** Each share, price and entry fact carries its link as it is captured.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics per company, the limit, so a ten-year comparison goes in Gaps; peers come as a set in one batch, from the competitors block, an industry screen and the competitors named in the filing. Revenue by segment and geography is in the company data; segment assets, customer concentration, patents and licences come from the annual filing's business, risk-factor and segment notes. Industry size and market shares have no structured field; research, filings and news carry them, rarely for the full market. Price increases, discounting and pass-through come from transcripts and news over the last five years; entrants, exits, capacity additions and price wars from news. The deal history needs FactSet access; otherwise it comes from search. The cost of capital is built, with the risk-free rate from the country data. A private company's return tests rest on whatever statements exist; the industry tests run from filings, news and research. Sector profit pools and persistence figures are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Ferrari's moat is price, and it has held through two cost cycles"). The opening gives the spread and whether both tests pass over a cycle, the source of advantage and whether the numbers show it, the duration with its bounds, the main threat, and what would change the reading, in plain sentences. The body follows the question, with the economics before the industry and the company's own advantage, because the sequence is the argument. What would show erosion first closes the note. Sub-headings state the finding, never the test that produced it.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with the body.
- Both tests are shown, return above the cost of capital and above peers over a full cycle, and the claimed source matches the margin and turnover split or the mismatch is stated.
- The duration is in years with the level it fades to, and the period the price implies appears only as a comparison.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
