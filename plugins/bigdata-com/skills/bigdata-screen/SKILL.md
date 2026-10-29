---
name: bigdata-screen
description: >-
  Find companies that fit criteria: size, sector, valuation, growth or quality, ranked on what the
  user asked for. Use for screen for stocks, find ideas, who else does what X does, acquisition
  targets. Not one name: bigdata-quick-take.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, base-rates, multiples-and-peers, expectations
  bigdata-sector-primer: auto
---

# Screen

A screen produces candidates for further work, never a buy list, a target or a weighting, and the note says why each one screens well and why it might be a trap. A company looking for acquisition targets, competitors, suppliers or customers asks a different question: the criteria are written in its terms (a size it could buy, overlap with its products, geography) and each name's reason and caution are fit and obstacles for a target, threat for a competitor, dependence for a supplier. Size the work to the question: "list US semiconductor companies above $10bn" gets the screened list with its as-of time and the Data line, without a ranking.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-screen"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **Criteria written as thresholds before the first pull.** Vague words ("small cap", "cheap", "quality", "growing", "low debt") become stated thresholds with the reason in a few words, so the reader can change them, and one criterion is named as the one the shortlist is ranked on first.
- **Two stages.** The screener filters what it can; valuation, growth, margins, ROIC, leverage and cash conversion are applied afterwards to the top N on the primary criterion, with N stated (20 to 30 works, all when fewer survive). Names that fail one criterion narrowly are worth naming when they would change what the reader does next, because screens that disagree are informative.
- **Rank on the user's criteria; a default only when they give none.** The default is gross profitability (gross profit over total assets), ROIC, and the level and stability of operating margin, because these persist from year to year while sales growth persists weakly and net income growth not at all (`references/base-rates.md`, persistence of growth, margins and returns). Each is measured against the sector median from the second-stage set, so a staples company and a software company are not compared on raw margins. One-year growth may be shown; it does not drive the default. When several metrics are combined into one rank, state the weights once and let the reader see where each name stands on each metric, because a composite hides which metric put a name on top.
- **Sector metrics replace the default where they apply**: REITs on FFO and AFFO per share and price over AFFO; utilities on allowed return and rate-base growth; oil and gas producers on reserve life, reserve replacement and breakeven price; banks on ROTCE against a stated cost of equity and price to tangible book; insurers on combined ratio and operating ROE against price to book. Banks and insurers are screened apart from industrial companies (`references/sector-primers.md`).
- **One ROIC definition for every name**: the data set's field, never mixed with a hand-built figure. A name without the field is left blank.
- **A multiple is read beside ROIC and growth.** When valuation is among the criteria, use the sector's conventional multiple, built the same way for every name, because a low multiple on a low return is not cheap and a cyclical's multiple on peak earnings looks cheaper than it is (`references/multiples-and-peers.md`, which multiple and which base).
- **What the price implies, when valuation is among the criteria and a name's case rests on growth.** The NOPAT growth the enterprise value implies at a three-year rolling return on new investment (`references/expectations.md`, implied growth), with the share count and net debt behind the enterprise value stated so the reader can rebuild it; and, where that growth rate carries the case, how often companies of its size achieved it, with the population and period in the same sentence (`references/base-rates.md`, real sales growth by starting size). Where neither changes the ranking or the cautions, it stays in the working.
- **Every top name earns its place in a sentence or two:** why it screens well, with dated evidence; how it could be a trap (a one-off gain, peak-cycle margins, leverage, an accounting choice the sector primer flags, a declining business at a low multiple); and the next check, because a screen hit alone is not a candidate. Then the list as a whole: if it is mostly one size, one sector or one cheap-valuation tilt, say that the screen is a factor bet rather than a set of company ideas.
- **"Companies like X" is a peer search.** Start from X's competitors in its profile, then compare the names that share X's industry classification with those closest to X on growth, margin, ROIC, turnover and capital intensity; the names on both are the strongest peers. Rank by distance from X rather than by quality, and state the selection rule before any multiple (`references/multiples-and-peers.md`, peer selection by value drivers).
- **Loss-making or early-stage names** have no meaningful gross profitability or ROIC when NOPAT or invested capital is negative; rank them, if at all, on gross margin and revenue growth against forward EV over sales, and say so.

## Where it goes wrong

- **The default ranking used when the user named criteria**, which answers a question they did not ask.
- **A peak-cycle margin read as persistent.** Show the five-year range beside the latest value and flag any name sitting at the top of it.
- **Market caps from several countries compared unconverted.** The screener does not convert; convert to one currency, with the rate and date stated, before applying a size threshold.
- **Historical sector names taken as the screener's.** Map them: consumer staples to Consumer Defensive, consumer discretionary to Consumer Cyclical, health care to Healthcare, information technology to Technology, materials to Basic Materials, telecom services to Communication Services (which also holds media), industrials and energy as named. Financial Services, Real Estate and Utilities have no historical sector row.
- **Estimate revisions applied to a long list.** They come from dated research per name, so they apply to the shortlist only, each with its source and date.
- **Peers fetched one company at a time.** Pull peer statements as a set in one batch.

## What the data has, and does not

The screener covers listed companies only. Without a country or exchange it covers primary listings on NASDAQ, NYSE, NYSE American and the Toronto Stock Exchange; other markets need a country or an exchange from its own list. It filters on market cap, share price, beta, daily volume, dividend per share, sector, industry, country, exchange, actively trading, and ETF or fund; its sector labels are its own list, not those of the entity lookup; values are in each listing's currency and are not converted; results are paged until complete. The current-figures grid takes up to 3,000 names with price and market cap, but only 100 once surprise, target or sentiment columns are added. Private companies are added by resolving named ones and through search, and the note says how they were found. Fundamentals are five fiscal years of annual statements, nothing older; consensus is a snapshot with its date and no revision history, so revisions come from dated research. Next report dates come from the corporate calendar. Each sector's metrics and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line (what the survivors have in common), not the criteria. The opening gives the criteria and coverage, how many companies passed, what the top names share, the main caution about the list and what would change the ranking. The body follows the question: usually the shortlist in the order of the primary criterion with each figure beside its sector median, then the top names' reasons and cautions; for a company screening for targets or competitors, each name's fit or threat comes before its valuation. A line under the shortlist says it is a list of candidates for further work, and the note closes on the next checks. Sub-headings state the finding ("Four of the top ten sit at five-year peak margins"), never the step.

## Before sending

- The ranking follows the user's criteria; the default ranking appears only when they named none, and sector metrics replace it where they apply.
- The note states how many names survived each stage, the N cut and its criterion, the as-of time and the coverage (exchanges, currency, private names added).
- Every number in the opening agrees with its table.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
