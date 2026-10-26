---
name: bigdata-theme
description: >-
  A theme or trend end to end: how it works, beneficiaries and losers, addressable market,
  companies with real exposure from segment revenue. Use for themes, trends, who benefits from X,
  how exposed are we. Not one sector: bigdata-sector.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, operating-leverage-and-tam, industry-structure, expectations, base-rates
  bigdata-sector-primer: auto
---

# Theme

This skill writes the theme note a reader wants before acting on a theme: the mechanism that makes the theme real, where along the chain the money flows and where it is competed away, how large the market can get at an acceptable return, measured two ways and tested, which companies earn a meaningful share of their revenue from it, what their prices already assume, and the dated evidence that would confirm or break the theme. The reader may be a portfolio manager, or a corporate strategy team asking how exposed its own company or a rival is. The note measures the bar the prices set before it describes the opportunity. It names no picks and delivers an exposure list, not a weighted basket. "Who supplies the cooling for AI data centres" gets the exposure table for that link and its sources, not the full note.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-theme"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Write down the theme's boundary before searching, because an unbounded theme produces an unbounded report:

- **The mechanism.** One sentence on what changes (a technology, a regulation, a demographic shift, a cost curve, a policy) and who pays whom as a result.
- **The sub-themes and links of the chain** in scope: suppliers of inputs, makers, integrators, users, and the incumbents it displaces.
- **The horizon and geography.** Assume a five-year horizon, and the user's market when it is known, otherwise global, and state both (`bigdata-sector` uses the same default). The screener covers primary listings on NASDAQ, NYSE, NYSE American and Toronto unless a country or exchange is passed, so a global scope needs a screen per major market; add other non-US names by resolving them to their Bigdata.com entities and through search, and say which markets were screened.
- **The subject company**, if any: "how exposed are we", "how exposed is X". Resolve it to its Bigdata.com entity, run it through the exposure steps whatever its size, and add its exposure line to the template. Write the implications for that reader (the user's own company, a competitor, a customer or a supplier).
- **The product cell** from `references/operating-leverage-and-tam.md`: current or new technology, for current or new customers. New technology for new customers needs scenarios, because both the number of adopters and the speed are unknown.

Ask one question only when the theme names several distinct chains (for example "AI" as chips, as software, or as adoption by users) and the user gave no hint of which; otherwise cover the chain at summary depth, go deep on the link with the most evidence, and say so.

## Gather

Each step says what it must produce.

1. **The theme's evidence.** Searches, one aspect and one period per call: adoption or penetration data; spending and capex tied to the theme; price and unit-cost trends; policy, subsidies and regulation; supply constraints and capacity announcements; estimates of the market's size with their definitions; the case against the theme. Fetch the document when a market-size figure needs its definition. Done when each link of the chain has evidence or a stated gap and every market-size estimate found is listed with its source, definition and date.
2. **Candidates.** From the searches (named suppliers, customers, contract winners), a screen on the industries of each link in each market screened, and the holdings of thematic ETFs where one exists. An ETF's holdings data lists the top ten holdings only, so it seeds the list rather than completing it; an ETF's holdings are candidates, not evidence of exposure. Resolve all to their Bigdata.com entities, including non-US and private names found in search. Done when ten to thirty candidates are listed by link, with losers as well as beneficiaries, and the markets screened are stated.
3. **Exposure.** For each candidate: the profile and five fiscal years of revenue by segment and by geography; five fiscal years of annual statements and ratios; key metrics and consensus. Ask for annual periods, since the default is quarters, and pull them as a set rather than one company at a time where the account allows. Done when five fiscal years of revenue by segment and by geography, margins, invested capital and consensus with its vintage are in hand for each, or the missing item is named.
4. **Exposure the segments do not show.** For candidates whose segments mix theme and non-theme revenue, a search of the latest filing and call for disclosed theme revenue, backlog, orders or capex tied to the theme. Done when each candidate has a theme revenue figure with its basis, or is marked "not disclosed".
5. **Current prices.** Price and market cap for the candidates, in one pull for the set. Add surprise, target or sentiment columns only when the user asks for them, because they cap the grid at 100 names. Done when every candidate has a current market cap.
6. **Geography and dates.** The economic overview of the countries where production or policy concentrates, when that matters to the theme; the corporate calendar for the exposed companies' next reports and conferences; searches for the dated events the corporate calendar does not carry (policy decisions, regulatory deadlines, product launches). Done when each signpost has a date or a window, or is marked undated.
7. **Sector primers.** For each sector the exposed companies sit in, find it in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read "Metrics that matter" and "Financial statements and accounting traps". Done when each exposed sector's metrics and traps are noted.

## Analyse

1. **How the theme works.** The mechanism, the chain with the flow of money between links, the business category of each link (physical, service or knowledge, which decides whether growth needs assets, people or neither), and where the theme sits on its adoption curve. Done when a reader can see who pays, who is paid, and why now.

2. **Beneficiaries, losers and where the profit stays.** For each link: first-order beneficiaries, second-order beneficiaries, and the losers by substitution, each with the mechanism. Then, from `references/industry-structure.md`, test entry first: a link with low barriers sees its returns competed toward the cost of capital however fast volume grows, so name the link that holds a scarce asset or a position others cannot copy, and say where the profit pool is moving (`references/operating-leverage-and-tam.md`, procedure step 7). Done when every link has a verdict on whether volume growth turns into returns, with evidence.

3. **The addressable market, two ways.** From `references/operating-leverage-and-tam.md`: bottom-up through the funnel (population, eligible, with access, share, usage and persistence, price), with a price sensitivity; top-down as market times share path, with the market's definition stated, because the definition alone can move the answer by an order of magnitude. Then the limits: scale that is local, overshoot, network effects only where users interact, and the return condition that the market ends where incremental investment stops earning its cost of capital. Done when the market is a range from both routes with the definitions, each assumption labelled.

4. **The adoption curve and the S-curve warning.** Place the theme in penetration, transition or maturity, with analog diffusion parameters quoted with their source and period as historical, and noted as understating the speed of recent products. Do not extrapolate the steep middle of the curve: test announced capacity against a demand peak, not against the current growth rate. Once replacements dominate unit sales, forecast the replacement cycle, not penetration. Where cost decline drives adoption, project unit cost from cumulative output with a floor set by input costs, not as a line through time. For a new technology for new customers, run two or three adoption scenarios with probabilities that sum to 100, each weight taken from the analog products and labelled judgment. Done when the stage, the capacity check and the scenarios are stated.

5. **Real exposure.** Compute exposure from segment and geographic revenue: theme revenue share = theme-related segment revenue / total revenue, with the segment's growth and, where disclosed, its margin. Where segments do not isolate the theme, use the company's own disclosure and label it; otherwise write "not disclosed" and do not estimate a share from the narrative. Geographic revenue shows exposure to the countries where policy or demand concentrates. Separate companies with material exposure from those with the theme in the name only, and state the threshold used and why. Order the list by theme revenue share; it carries no weights. For a subject company, add its line even when its exposure is below the threshold. Done when the exposure table has a share, a basis and a source for every candidate and the subject company.

6. **What the prices imply.** From `references/expectations.md`, for the three to eight most exposed companies: forward P/E against the steady-state P/E (formula 1), the NOPAT growth the enterprise value implies (formula 2, with ROIIC as a three-year rolling figure, the most five annual periods allow) against consensus, and the share of value resting on future value creation, with the cost of capital set as its inputs table says. Translate into the theme: if the price needs growth g and the theme is s percent of revenue, state the growth the theme segment must deliver with the rest of the company held at consensus (derived). Then a cross-check that is this skill's construction, not a method from the sources: add up the theme revenue the exposed companies' prices imply in the horizon year and set it against the top of the addressable-market range. Done when each company has its implied bar and the aggregate check is stated.

7. **Base rates for the growth the theme assumes.** From `references/base-rates.md`: the revenue CAGR the market range and the prices imply, placed in the size-matched reference class (table 2, the column nearest the horizon) with the share of companies that achieved that rate or more, read from the share-above-threshold columns rather than a z-score, because growth rates are skewed and the published shares are the evidence. Give the sample label and the real-to-nominal conversion. Done when every growth figure in the note has its base-rate sentence.

8. **Signposts.** Four to eight observable, dated items that would confirm or break the theme: adoption data, prices and unit costs, capex and capacity announcements, policy decisions, the exposed companies' reports. Each with the threshold that changes the reading. Done when every signpost has a date or window and a threshold.

## Write

Follow `references/output-standard.md`.

```
# <Theme>: theme note, <date>
Data as of: prices <date>; estimates <date>; statements <latest period>; newest document <date>.
Scope: <mechanism, links covered, horizon, geography>.

## The view
Four to eight sentences: the mechanism, where the profit stays along the chain, the market range,
what the most exposed prices already assume, and the signpost that matters most. No rating word.

## How the theme works
Mechanism, the chain, adoption stage.

## The chain: beneficiaries and losers
| Link | Companies | Mechanism | Barriers to entry | Does volume become returns? | Basis | Source |

## Addressable market
| Route | Definition | Low | High | Key assumptions | Basis | Source |
Funnel table; price sensitivity; the limits; the S-curve stage and capacity check; adoption
scenarios with probabilities and their analogs.

## Exposure
| Company | Link | Theme revenue share | Segment growth | Segment margin | Geographic exposure | Basis | Source |
Ordered by theme revenue share, no weights. The threshold used; names with the theme in the name only.
<Subject company> exposure: theme revenue share, the link it sits on, what the theme does to it, against the most exposed peers.

## What the prices imply
| Company | Forward P/E | Steady-state P/E | Implied growth | Consensus growth | Implied theme-segment growth | Basis | Source |
The aggregate check against the market range.

## Base rates
The sentences for the market's growth and the leaders' consensus growth.

## Signposts
| Signpost | Threshold | Date or window | What it would change | Source |

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages. A narrow question (one link, one company's exposure, the market size) gets that step's table with its sources and the footer.

## Checks before sending

1. The theme's boundary, horizon, geography and the markets screened are stated under the title and held to.
2. Losers are named as well as beneficiaries, each with a mechanism.
3. Each link has an entry-barrier verdict before any claim that volume growth becomes profit.
4. The addressable market is a range from two routes, with the definition of each, and the S-curve warning is applied to any capacity or growth extrapolation.
5. Every exposure share comes from segment or geographic revenue or a company disclosure, labelled, or reads "not disclosed".
6. "What the prices imply" covers the most exposed names with assumed costs of capital stated once.
7. Every growth figure has a base-rate sentence with its sample, period and share above threshold; no z-score.
8. Scenario probabilities sum to 100 and name their analogs.
9. The exposure list is ordered by theme revenue share and carries no weights; no buy list, basket weights, rating or "how to play it" language; a named subject company has its exposure line.
10. Every figure has a Basis label and a source number or the Data line.

## Hand-offs

- One sector's economics: `bigdata-sector`. One exposed company in depth: `bigdata-deep-dive`. More companies that fit criteria: `bigdata-screen`.
- The user wants dated events for the exposed names: `bigdata-catalysts`.
- After delivering, make one offer: save the exposed companies as a Bigdata.com watchlist, or a monitor on the signposts. Act only on a clear yes.
