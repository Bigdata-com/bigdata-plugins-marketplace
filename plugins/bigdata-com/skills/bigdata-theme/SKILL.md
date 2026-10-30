---
name: bigdata-theme
description: >-
  A theme or trend end to end: how it works, beneficiaries and losers, addressable market,
  companies with real exposure from segment revenue. Use for themes, trends, who benefits from X,
  how exposed are we. Not one sector: bigdata-sector.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, operating-leverage-and-tam, expectations, valuation, base-rates
  bigdata-sector-primer: auto
---

# Theme

A note on how a theme works, where along the chain the money flows and where it is competed away, how large the market can get at an acceptable return, which companies earn a real share of revenue from it, what their prices already assume, and the dated evidence that would confirm or break it. Never a picks list, a weighted basket or a "how to play it" line. A company asking how exposed it or a rival is asks a different question: that company's exposure, the link it sits on and what the theme does to it against the most exposed peers come first, as trade-offs rather than a recommendation. Size the work to the question: "who supplies the cooling for AI data centres" gets the exposed companies on that link with their sources, not the full note.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-theme"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **The boundary before the search.** One sentence on what changes and who pays whom as a result, the links in scope (inputs, makers, integrators, users, the incumbents displaced), a five-year horizon and the user's market, or global, because an unbounded theme produces an unbounded report. When the theme spans several distinct chains and the user gave no hint, cover the chain at summary depth and go deep on the link with the most evidence.
- **Candidates from three routes.** The screen per major market, the holdings of thematic ETFs as a seed list, and search, with non-US names resolved, because search alone misses exposed companies that are not in the news. Peer sets are pulled in one batch, not company by company.
- **Entry tested before volume becomes returns, when the question is where the money stays.** A link with low barriers sees its returns competed toward the cost of capital however fast volume grows, so no claim that growth turns into profit stands without the entry test behind it. The note says in sentences, with evidence, which link holds a scarce asset or a position others cannot copy and where the profit pool is moving; a link-by-link judgment only where the reader is choosing among links (`references/industry-structure.md`, entry and exit, profit pool; `references/operating-leverage-and-tam.md`, profit pools).
- **Losers named with beneficiaries, when the question asks who gains**: first-order and second-order beneficiaries and the companies displaced by substitution, each with the mechanism.
- **The addressable market two ways, when the question asks how large it can get.** Bottom-up through the funnel with a price sensitivity, and top-down as market times share path with the definition stated, because the definition alone can move the answer by an order of magnitude. Then the limits: scale that is local, features customers will not pay for, network effects only where users interact, and the market ending where incremental investment stops earning its cost of capital. The result is a range, and the assumptions it rests on are stated once in plain words where the range is given (`references/operating-leverage-and-tam.md`, addressable market).
- **The S-curve, when the theme is about adoption.** Never extrapolate the steep middle of the curve: test announced capacity against a demand peak, not the current growth rate; once replacements dominate unit sales, forecast the replacement cycle; project unit cost from cumulative output with a floor set by input costs. New technology for new customers gets two or three adoption cases whose weights start from how fast comparable products were adopted, stated with their population and period, and whose outcomes do not overlap; older products' adoption speeds understate recent ones (`references/operating-leverage-and-tam.md`, adoption curve).
- **Exposure from segment and geographic revenue, when the question asks who is exposed.** Theme revenue share is theme-related segment revenue over total revenue, with the segment's growth and margin where disclosed. Where segments mix theme and other revenue, use the company's own disclosure of theme revenue, backlog or orders, never two measures in one comparison, and leave a blank where there is none rather than estimating a share from the narrative. Separate material exposure from the theme in the name only, with the threshold and its reason. Order by theme revenue share with no weights; a named company is covered whatever its exposure.
- **What the prices assume, when the question asks it.** For the most exposed companies the question turns on, the NOPAT growth the enterprise value implies at a three-year rolling return on new investment, against consensus (`references/expectations.md`, implied growth); then the growth the theme segment must deliver with the rest of the company held at consensus. The inputs appear once, from the latest filings (share count, net debt including leases and stakes outside the operating business, tax rate, the cost of capital with its yield, beta and premium in one clause, and the year the cash flows start), so the reader can rebuild each figure, and every later figure uses them (`references/valuation.md`, cost of capital). Where the question is whether the group is priced for more than the market can hold, add up the theme revenue the exposed prices imply in the horizon year and set it against the top of the market range.
- **How often growth like this happened, only when the case rests on it and the answer changes the reading.** The revenue growth the market range and the prices imply is placed among companies of the same size, as the share that reached it, because growth rates are skewed; nominal growth is converted to real before the comparison, and the population and period are in the same sentence (`references/base-rates.md`, real sales growth by starting size, real and nominal growth). Otherwise it stays in the working.
- **Signposts with a threshold and a date**: adoption data, prices and unit costs, capex and capacity announcements, policy decisions, the exposed companies' reports, each saying what reading would change the view.

## Where it goes wrong

- **Data pulled company by company.** Pull the peer set in one batch.
- **Exposure on mixed measures.** Revenue, orders, backlog and broker estimates set side by side as one share; keep one measure per comparison, and say when no like-for-like comparison exists.
- **Prose that disagrees with its table.** Read every comparison in the text off the table.
- **Cost of equity and WACC conflated.** Equity measures use the cost of equity and enterprise-value measures use WACC; state each once.
- **Figures that do not tie to their own inputs.** Recompute every computed figure (growth ranges, leverage multiples) from the inputs shown.
- **Citations assembled at the end** land on documents that cannot hold the claim. The link goes next to the fact when the fact is captured.

## What the data has, and does not

Five fiscal years of revenue by segment and by geography with annual statements and ratios, nothing older; theme revenue is rarely its own segment, so it comes from filings and calls when the company discloses it. Consensus is a snapshot with its date and no revision history. The screener covers primary listings on NASDAQ, NYSE, NYSE American and Toronto unless a country or exchange is given, so a global theme needs a screen per major market, and the note names the markets screened; non-US and private names are added by resolving them. An ETF's holdings data lists the top ten holdings only, so it seeds the candidate list and is not evidence of exposure. The current-figures grid takes up to 3,000 names with price and market cap, 100 once surprise, target or sentiment columns are added. Market size has no structured field; research and industry documents carry estimates, each with its own definition and date. The corporate calendar carries earnings dates and conferences; policy decisions, regulatory deadlines and product launches come from news and filings. The country data covers the economies where production or policy concentrates, and gives the risk-free rate for the cost of capital. Each exposed sector's metrics and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Cooling keeps its margin; the racks compete it away"), not the theme's name. The opening answers the question first: of the mechanism, where the profit stays along the chain, the market range, what the most exposed prices already assume and the signpost that matters most, the ones the question asks. The body follows the question, the user's parts in the user's order under their names; an exposure list is ordered by theme revenue share and carries no weights. The note closes on the signposts with their thresholds and dates. Sub-headings state the finding, never the step.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- Every exposure share comes from segment or geographic revenue or the company's own disclosure, one measure per comparison, and where beneficiaries are named, losers are named beside them.
- No claim that volume becomes profit stands without the entry test behind it.
- Every number and every comparison in the opening and the text agrees with its source figure; every price-implied figure can be rebuilt from inputs stated once on the page, and the net debt is the same figure everywhere.
- No judgment appears as a label or a bolded category; each is a sentence with its evidence.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
