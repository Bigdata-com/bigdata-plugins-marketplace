---
name: bigdata-sector
description: >-
  How an industry works: structure and profit pool, drivers and metrics, what is priced in, where
  a named company sits. Use for a sector or industry outlook, our industry, which sectors look
  interesting. Not a theme: bigdata-theme.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, industry-structure, operating-leverage-and-tam, base-rates, expectations, multiples-and-peers, valuation
  bigdata-sector-primer: auto
---

# Sector

A note on how an industry makes money, who keeps the profit, where it sits in its cycle, what its leaders' prices already assume, and which companies matter for what reason. Never a picks list and never an overweight or underweight call. A company reading about its own industry asks where it stands: its share, margin, returns and multiple against the sub-industry median and range come first, with what that position means for it as competitor, customer, supplier or buyer. Size the work to the question: "how do banks make money" gets the economics with current figures for two or three banks, not the full note; "which sectors look interesting" is a triage on a stated measure, then the full method for the three or four that stand out.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-sector"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** A question in four parts gets four answers, in the user's order, each in full and findable by its name; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **The primer first, at the sub-industry level.** Read the sector's section of `references/sector-primers.md` before any data pull, and analyse by sub-industry, because a sector average hides who earns the return: "tech" spans software, semiconductors and internet platforms, each with its own economics. A sector with no primer section is analysed from the filings and research alone.
- **The profit pool, when the question is who keeps the sector's profit or whether that is shifting.** Show each company's share of the sub-industry's invested capital against its ROIC minus the cost of capital, latest year against the earliest of the five annual periods, so the note can say who gained or lost capital share or spread; banks and insurers use equity and ROE minus the cost of equity. The cost of capital is one stated figure, with the yield, beta and premium behind it in one clause, and the 10-year yield comes from the country data (`references/valuation.md`, cost of capital); where the ordering is close, say whether it holds at one point either side. Concentration and share stability go on the page only when the question turns on whether the structure will hold; otherwise they stay in the working (`references/industry-structure.md`, profit pool, concentration and HHI, share stability).
- **Entry first, when the question is whether returns will last.** Low barriers push returns toward the cost of capital whatever the other forces show, so entry is tested first. Another force enters only where it explains a return the reader asks about, with its evidence, never as a walk through all five or an attractiveness rating; otherwise the forces stay in the working (`references/industry-structure.md`, entry and exit, bargaining power).
- **Mid-cycle, when the question rests on a cyclical sector's earnings or valuation.** A forward P/E on peak earnings looks low and on trough earnings high, so the latest and consensus margins sit beside a mid-cycle margin from the primer's guidance and the long-run trend, its basis stated once in plain words; ranges widen at turning points. Where a sub-industry sits in its cycle is a plain sentence with its evidence, never a label such as early, mid or late cycle.
- **Sales to profit through the sector's operating margin beta, when the question turns on a change in demand**: what a stated change in sector sales does to operating profit, and where the companies' own cost structures differ from the sector's (`references/operating-leverage-and-tam.md`, cost structure and operating margin beta).
- **Margin fade, only when the note says where margins will be in some years and the fade changes the reading.** The leaders' expected margin is the sector mean plus the persistence factor times today's gap, with the population and period of the history in the same sentence; the historical sector names differ from the screener's, so map them (`references/base-rates.md`, regression to the mean, operating margin by sector, persistence of growth, margins and returns). Otherwise it stays in the working.
- **What the price assumes, when the question asks what is priced in.** For the leaders the question turns on, the NOPAT growth the enterprise value implies at a three-year rolling return on new investment, set against consensus (`references/expectations.md`, implied growth). The inputs appear once on the page (share count, net debt, tax rate, cost of capital and the year the cash flows start) so the reader can rebuild each figure. A base rate for a multi-year growth rate belongs only where a leader's case rests on that rate and the frequency changes the reading, with population and period in the sentence (`references/base-rates.md`, real sales growth by starting size). A median multiple is compared with its own history only at a similar point in the cycle and with ROIC beside it; banks use price to book against ROE (`references/multiples-and-peers.md`, what a multiple implies, banks). The note then says in two sentences whether the bar is high or low.
- **Companies by the role they play, when the question asks which companies matter.** Each is a sentence with the number behind it: holds the widest part of the profit pool at a positive spread, gaining capital share or spread, large and earning below its cost of capital, the marginal producer that sets price, the entrant, the company whose next report settles a live debate. This is a map of the industry, not a list of picks.
- **A live debate, where one bears on the question**: both sides, where consensus and the price-implied bar sit, and the dated evidence that would settle it.
- **Several sectors on the same measures and periods**, chosen from what the question turns on, ordered by a measure the user chose or by the spread, and never ranked by attractiveness.
- **A sector inside a country.** Exposure confirmed from geographic revenue, because a listing there is not business there; the policy that shapes returns (subsidies, tariffs, ownership rules, regulated returns); multiples and returns against global peers in the same sub-industry so a country premium or discount shows.

## Where it goes wrong

- **The method filled while the question goes unanswered.** Forces, profit pool, fade and base rates written out in full while the user's parts are not answered in order; the parts come first and a method piece appears only where it changes the answer.
- **A price-implied figure the reader cannot rebuild.** The inputs behind it are stated once on the page.
- **Prose that contradicts its own table.** Read every ordering and rank in the text off the table.
- **Growth figures side by side with different windows.** Each growth figure carries its window, and a one-year and a three-year figure are not set beside each other without saying so.
- **A profit pool built on unlike figures.** Same metric, period and scope for every company.
- **ROIC missing for much of the depth set.** Pull the depth set's statements and ratios as one batch.
- **Citations assembled at the end** land on documents that cannot hold the claim. The link goes next to the fact when the fact is captured.
- **A sector multiple compared with its history at a different point in the cycle**, which calls a peak cheap.
- **A risk-free rate taken from memory** when the country data has the current yield.

## What the data has, and does not

The screener covers primary listings on NASDAQ, NYSE, NYSE American and Toronto unless a country or exchange is given, so a global scope needs a screen per major market and the note names the markets screened; its sector labels are its own list; market caps are in listing currency and not converted. The current-figures grid takes up to 3,000 names with price and market cap, 100 once surprise, target or sentiment columns are added. Five fiscal years of annual statements and ratios, nothing older, which may not span a full cycle; the note says so where a mid-cycle figure depends on it. Segment and geographic revenue are available; the data set's ROIC field differs from a hand-built one, so one definition is used throughout. Consensus is a snapshot with its date and no revision history. The market overview gives sector performance over standard windows only. Industry size, market shares, pricing and capacity have no structured field; research, news and filings often carry them, so search before stating a gap. The corporate calendar carries earnings dates and conferences; the economic calendar carries the macro releases the primer names. The risk-free rate and a country's backdrop come from the country data. Peer sets are pulled in one batch, not one tearsheet each.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Equipment keeps the profit; memory carries the cycle"), not the sector's name alone. The opening answers the question first: of how the sector makes money and who keeps it, where it sits in the cycle, the drivers that matter now, whether the price-implied bar is high or low, and where a named company sits, the ones the question asks. The body follows the question, the user's parts in the user's order under their names; the primer's accounting traps go in where they bear on a figure, and several sectors share one comparison table, with one line per sector set aside in a triage and the figure that set it aside. Where a live debate bears on the question, the note closes on it and what would settle it. Sub-headings state the finding, never the step.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- Every price-implied figure can be rebuilt from inputs stated once on the page.
- Where a profit pool appears, it is per sub-industry on one ROIC definition and one stated cost of capital.
- Every ordering or rank in the text matches its table, and every number in the opening agrees with its table.
- Where the note rests on a cyclical sector's margin, the mid-cycle margin sits beside the latest and consensus margins, and every historical figure carries its population and period in the sentence.
- No cycle position, role or judgment appears as a label or a bolded category; each is a sentence with its evidence.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
