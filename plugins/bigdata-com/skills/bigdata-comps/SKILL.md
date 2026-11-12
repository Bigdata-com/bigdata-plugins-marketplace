---
name: bigdata-comps
description: >-
  Peer comparison: peers picked by value drivers, multiples on one basis, growth, margins and
  returns side by side. Use for comps, relative valuation, benchmark against competitors. Not
  intrinsic value: bigdata-valuation.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, multiples-and-peers, expectations, roic, valuation
  bigdata-sector-primer: auto
---

# Comps

Never calls a stock cheap or expensive, and the value the peer range implies is a range, never a target. A multiple is a cash-flow model with the forecast left implicit, so the work makes the forecast explicit: where the company should sit given its returns and growth, and what its multiple says the market expects. A company benchmarking itself against competitors asks a different question, how its operations compare: growth, margins, returns, cash conversion and total shareholder return come first, and multiples only as far as asked. Size the work to the question: "what is Micron's forward EV/EBITDA against peers" gets that multiple, the peer table behind it and the median, not the split of the multiple or the implied growth.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-comps"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **Peers by value drivers, the rule written before any multiple.** Candidates from the industry screen, the competitors block, the competitors named in the annual filing and past deal counterparties, then tested on growth, operating margin, ROIC and capital intensity, because a firm in another industry can be closer on drivers than one in the same industry, and a rule written after the multiples tends to pick high-multiple peers (`references/multiples-and-peers.md`, peer selection by value drivers). Each peer's reason is a clause where it first appears, and the obvious companies left out are named with why; how many candidates the test removed stays in the working. Peers the user names stay in, with a line if the drivers argue against one.
- **Enterprise value rebuilt on one basis.** Debt, cash, minorities, preferred, leases, pensions and equity stakes are taken from each company's latest filing the same way, and every multiple uses them. The inputs appear once on the page (each company's share count, the claims and stakes between equity value and enterprise value, and the net figure) so the reader can rebuild each multiple. An item missing for some peers is dropped for all or named (`references/multiples-and-peers.md`, building the multiple).
- **Claimants matched.** Equity multiples sit on equity value and enterprise multiples on enterprise value; P/E uses net income attributable to the parent and is used only where net debt to EBITDA sits in a narrow band across the set, because leverage moves P/E with no change in the business. The profit a multiple is applied to says whether it is before or after tax.
- **The metric cleaned on the same items for every company, or for none.** A "one-time" charge in two or more of the last five years is a cost and stays in; equity-accounted income comes out of EBITDA and the stake goes into the bridge from equity value to enterprise value (`references/multiples-and-peers.md`, building the multiple).
- **Multiple and base.** Forward, calendarized to the same twelve months, the sector primer's convention where it has one; EV/EBITA over EV/EBITDA where capital intensity or outsourcing differs; EV/EBITDA across IFRS and US GAAP companies only after the lease adjustment, because IFRS 16 moves lease costs out of EBITDA (`references/multiples-and-peers.md`, which multiple and which base).
- **Medians, not means, and the outlier's weight where it matters.** Peer sets are small and skewed, so where one company moves the median, the note says by how much. A comparison with the company's own history or the market holds only if returns, growth, rates and accounting are unchanged, and the note says whether they are.
- **Where it should sit, when the question is why the company trades where it does.** How much of the premium or discount to the median the ROIC spread and growth explain, at one stated cost of capital (the 10-year yield from the country data, the beta and the premium in a single clause, no regression statistics) with a one-point range. What is left is unexplained, and risk sits inside it. The split of the multiple into the part that needs no growth and the part paid for growth stays in the working unless the user asks what the multiple means (`references/multiples-and-peers.md`, what a multiple implies; `references/valuation.md`, cost of capital).
- **What the multiple implies, when the question is what the market expects.** The growth and return the multiple needs at the three-year rolling return on new investment, set beside consensus growth, and which path to that multiple the company is on, since the same P/E can mean fast growth on a thin spread or slow growth on a wide one (`references/expectations.md`, implied growth; `references/multiples-and-peers.md`, the warranted P/E; `references/roic.md`, ROIIC and the spread). Otherwise it stays in the working.
- **Special cases.** Banks and insurers on price to book against ROE; cyclicals on mid-cycle earnings; loss-making growth companies on forward EV/sales with the long-run margin stated; emerging-market listings checked against a cash-flow value; niche industries widened to global listings or adjacent sub-industries, and the note says so (`references/multiples-and-peers.md`, banks; errors).

## Where it goes wrong

- **The EV field used as given.** Its treatment of minorities, pensions, leases and the date of net debt is not documented, so it differs from a bridge built from the statements; rebuild it and say which one the note quotes.
- **FactSet ROIC mixed with a hand-built figure.** The two differ in tax rate, goodwill and leases; use one for every company, and never both in one comparison.
- **A mean, or a median that one company drives.**
- **A single year of return on new investment behind the implied growth.** One year can be operating leverage; five annual periods allow a three-year figure and nothing longer.
- **The peer-range value read as a target.** It is the median and quartile multiples applied to the company's metric, next to the price.
- **Peers pulled one tearsheet each.** The set comes in one batch.
- **Citations assembled at the end.** The link goes next to each cleaning item and filing figure when it is captured.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics per company, the limit; consensus for the next two fiscal years as a snapshot with its date and estimate count, no revision history. The current figures for a set of companies carry price, market cap, the daily move, surprise, targets and sentiment, but not growth, margins, ROIC or capital intensity, so the driver test needs annual statements, estimates and ratios for the candidate set, pulled as a set in one batch. Fiscal year-ends differ across peers, so periods are calendarized. Items to clean come from the latest annual and quarterly filings with the period fixed; when that is more searching than the request deserves, all figures stay as published and the note says so. The deal history that supplies past counterparties needs FactSet access. Total shareholder return over the standard windows comes from the overview plus dividends; any other window needs daily prices. There is no structured field for the cost of capital; build it once from the country data's yield. A private company has no market value, so the peers' multiples and operating metrics become a reference set, and the note calls them that. Sector multiples and accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Micron trades at a third below peers, and its returns explain most of it"). The opening gives the multiple against the peer median, how much of the gap returns and growth explain, and what the multiple implies about growth and returns, each where the question reaches that far. The body follows the question, the user's parts in the user's order, with the selection rule before any multiple. What would change the reading closes the note. Sub-headings state the finding ("Two peers carry the whole premium"), never the step.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- The selection rule precedes the multiples, and every peer has a source and a reason.
- The same EV basis, cleaning, multiple and calendarized period apply to every company, the items not adjusted for some peers are named, and every multiple can be rebuilt from the inputs stated once on the page.
- Every number in the opening agrees with its table, and the cost of capital is the same figure everywhere it is used.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
