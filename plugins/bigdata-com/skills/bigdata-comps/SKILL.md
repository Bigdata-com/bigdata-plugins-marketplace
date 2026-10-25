---
name: bigdata-comps
description: >-
  Peer comparison: peers picked by value drivers, multiples on one basis, growth, margins and
  returns side by side. Use for comps, relative valuation, benchmark against competitors. Not
  intrinsic value: bigdata-valuation.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, multiples-and-peers, expectations, roic
  bigdata-sector-primer: auto
---

# Comps

This skill builds a comparables table a professional reader can trust: a peer set chosen by the economics that drive value, with the selection rule written down before any multiple is shown; every multiple built the same way, numerator and denominator on the same claimants, enterprise value on one basis, the metric cleaned of one-offs on the same items for every company; growth, margins, returns and cash conversion beside the multiples; medians rather than means; and then the two questions that matter, where the company should sit given its returns and growth, and what its multiple says the market expects. A multiple is a cash-flow model with the forecast left implicit, so this skill makes the forecast explicit. It never calls a stock cheap or expensive as a recommendation. "What is Micron's forward EV/EBITDA against peers?" gets that multiple, the peer table behind it and the median, not the full report.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-comps"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the target with `find_securities`, and every peer the user names in parallel, one call each. Establish the multiple the user cares about if they named one, the peers they want included (keep them, and say if the value drivers argue against one), and whether the question is relative value today or a peer set to reuse. Assume forward multiples on the next fiscal year unless the user says otherwise.

Establish the reader. An investor gets the report below. A corporate strategy, finance or investor-relations team benchmarking its own company against competitors gets corporate mode: the operating benchmark (growth, margins, returns, cash conversion and total shareholder return) as the first section, and the multiples as the second; write the implications for that reader.

Ask one question only when the answer changes the work: the target resolves to more than one listing, or the company has segments so different that the user must choose which business to compare. Otherwise state the assumptions under the header and proceed. Done when the target and named peers are resolved and the multiple, the base, the reader and the mode are stated.

If the target is Private, there is no market value to put in a multiple. Offer the peers' multiples and operating metrics as a reference set instead, labelled as such.

## Gather

Work through these in order. Each step says what it must produce.

1. **The target.** `bigdata_company_tearsheet` in three calls: `company_overview, revenue_segmentation`; `financial_statements, financial_ratios, key_metrics` with `interval` annual; `analyst_estimates`. Done when market cap, the EV field, debt, cash and securities, leases, pensions, minorities, preferred, equity-method investments, attributable net income, five annual periods of statements, consensus for the next two fiscal years with vintage and estimate counts, the segment mix and the competitors block in `company_overview` are in hand.
2. **Candidates.** `bigdata_screen_companies` on the target's industry, region and size (the classification route); the competitors block from step 1; the competitors named in the target's annual filing (one `bigdata_search` for the competition section); and the counterparties in the target's deal history where the account has `mergers_acquisitions`. Done when there are ten to twenty candidates, each tagged with where it came from.
3. **Driver figures for the selection.** The portfolio tearsheet does not carry growth, margin, ROIC or capital intensity, so the driver route needs the company tearsheet: for six to ten candidates, two calls each, `financial_ratios, key_metrics` and `financial_statements, analyst_estimates` with `interval` annual. When the user wants a quick set, start from the competitors block and one search for the rest, and say the driver test was not run. Done when each candidate tested has growth, EBITA margin, FactSet ROIC and capex over sales on the same fiscal basis, with fiscal year-ends noted so periods can be calendarized.
4. **Current prices.** `bigdata_portfolio_tearsheet` on the peers kept after Analyse step 1, for price and market cap only (do not request the surprise, target or sentiment columns, which the report does not use). Done when every peer has a price and market cap of the same date.
5. **Items to clean.** `bigdata_search` in fast mode on the latest annual and quarterly filings of the target and of every peer kept, for restructuring, impairment, write-down, integration costs, litigation and equity-accounted income, then `bigdata_fetch_document` where a table is needed. When that is more searching than the request deserves, compare reported figures for every company and say so. Done when each item has an amount, a year and a source for every company, or the report states that all figures are reported, uncleaned.
6. **Total shareholder return, corporate mode only.** Price change over the standard windows in `company_overview` plus dividends from the statements, or `bigdata_computer` on the daily series for another window, labelled derived. Done when every company has TSR over the same windows.
7. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the valuation-conventions and accounting-traps subsections. Done when the sector's multiple and traps are noted, or their absence is stated.

## Analyse

The five steps of a comparable company analysis (Robinson and Weyns, UBS, "How to analyse and talk the language of multiples", pp. 24-27) run through `references/multiples-and-peers.md`; each step below names its step there and ends in what it must produce.

1. **Pick the universe** (method step 7). Write the selection rule before showing any multiple, test the candidates on the drivers from Gather step 3, report how many classification-route peers survive, give each peer a one-line reason and name the obvious candidates excluded. The sources set no minimum count; state the number. Done when the peer table has a source and a reason for every name.

2. **Build enterprise value on one basis** (method steps 2 and 3). Start from the `key_metrics` EV for every company, then take debt, cash and minorities from each company's statements so all are built the same way. Add pensions, leases and options from the statements where present; where a peer's statements lack one, leave it out for every peer, or note which peers are not adjusted for it. Name the flavor (total, operating or core EV). Done when the bridge table shows every item for every company, and the items not adjusted are named.

3. **Match the claimants** (method step 1). Done when each multiple in the table is labelled equity or enterprise, and P/E uses net income attributable to the parent.

4. **Clean the metric** (method step 4), on the same items for the target and every peer, or on none, as Gather step 5 decided. A charge that appears in two or more of the last five years is a cost and stays in. Done when reported and cleaned metrics sit side by side with the items removed and their sources, or the report says all figures are reported.

5. **Choose the multiple and the base** (method step 5 and its table), using the sector primer's convention where it has one. Before comparing EBITDA multiples, check the accounting standard of each company: IFRS 16 moves operating lease costs out of EBITDA, US GAAP keeps most of them in, so compare EV/EBITDA across the two only after the lease adjustment, or use EV/EBITA. Use P/E only after checking that leverage is similar (net debt over EBITDA within a narrow band), because leverage moves P/E without any change in the business. Calendarize to the same twelve months for every company. Done when the multiple, the base, the period and the standards check are stated once and applied to every company.

6. **Put the operating metrics beside the multiples** (method step 6). For each company: consensus sales growth for the next two years and the three-year history, EBITA margin, ROIC, free cash flow over NOPAT, net debt over EBITDA, and capex over sales. Use the FactSet ROIC field for every company, and state under the table that its goodwill and lease treatment is not documented (`references/roic.md`); never mix it with a hand-built figure. Done when the operating table is complete or each gap is marked.

7. **Medians and position** (method step 8). Done when the line "the company trades at X against a peer median of Y (range A to B), a Z percent premium; without [outlier] the median is W" is written, and the report says whether a comparison with history or with the market is valid.

8. **Where the company should sit and why** (method step 9), at a stated cost of capital (assumed, with a range of plus and minus 1 point; `references/expectations.md` inputs table). Split the actual multiple into the steady-state part and the turns paid for value creation. Then say how much of the premium or discount the ROIC spread and growth explain through the justified multiple; the rest is the unexplained remainder. Risk has no separate measure here, so it sits inside that remainder with anything else the drivers miss, and the report says so. Done when the gap between actual and justified multiple is stated in turns, split into the part the spread and growth explain and the remainder.

9. **What the multiple implies about growth and returns.** `references/expectations.md` steps 1 to 5 on the target, at the three-year rolling ROIIC from `references/roic.md` (labelled; a single year is never evidence). Place the forward P/E on the warranted P/E grid (table 1, rerun at the assumed cost of equity) and state which of the three paths to the same multiple the company is on. Compare the implied competitive advantage period with the market-implied average of about 8 years (1976 to 2007, historical, not current). Done when the report states what growth and return the multiple assumes next to consensus growth and the company's ROIIC.

10. **The value the peer range implies** (five-step 5). Apply the peer median and the quartiles to the target's metric, then bridge core EV to equity per share. Present it as a range labelled derived, not as a target. Done when the range per share sits next to the price.

A narrow question gets steps 1 to 7 for the multiple asked about, with the peer table and the median.

Special cases: banks and insurers, cyclicals, loss-making high growth, emerging markets, multi-business companies and niche industries each have a rule in the "Interpretation and limits" of `references/multiples-and-peers.md`; apply the matching one, and hand a sum of the parts to `bigdata-valuation`. Done when the rule applied is named, or none applies.

## Write

Follow `references/output-standard.md`. The report has these sections in this order. In corporate mode, "Operating benchmark" comes straight after "Where it sits" and before "The peer set", with a TSR column.

```
# <Company> (<ticker>) comparables, <date>
Data as of: prices <date>; estimates <date>; statements <period>; newest document <date>.

## Where it sits
Four to six sentences: the multiple against the peer median, how much of the gap the returns and
growth explain, what the multiple implies about growth and returns, and what would change the
reading. No rating.

## The peer set
Selection rule, stated first.
| Peer | Ticker | Found by | Reason | Fiscal year-end | Standard | Source |
Excluded candidates, each with the reason.

## Enterprise value
| Company | Market cap | Debt | Minorities, preferred | Leases, pensions, options | Cash, non-core | EV |
Basis and sources note under the table; items not adjusted for some peers named.

## Cleaned metric
| Company | Reported EBITA | Items removed | Cleaned EBITA | Years with one-time charges (of 5) | Basis | Source |

## Multiples
| Company | Chosen multiple (fwd) | Second multiple | Equity or enterprise | Basis | Source |
Median, interquartile range, median without the outlier, target premium or discount.

## Operating metrics (Operating benchmark in corporate mode, with TSR)
| Company | Sales growth FY1, FY2 | 3-yr history | EBITA margin | ROIC (FactSet) | FCF / NOPAT | Net debt / EBITDA | Capex / sales |
Basis and sources note; ROIC definition line under the table.

## Where it should sit and why
Justified multiple for the target and the peer median at the stated cost of capital; steady-state
and value-creation turns; the gap split into what spread and growth explain and the remainder.

## What the multiple implies
Implied growth at the three-year ROIIC, position on the P/E grid, implied advantage period, against
consensus and history.

## Value from the peer range
| Multiple | Lower quartile | Median | Upper quartile | Equity value per share | Basis | Source |

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. Offer the peer table as a spreadsheet when the host can create files. For a narrow question, answer it in the method's terms with the peer table and the sources, and keep the footer.

## Checks before sending

1. The selection rule appears before the multiples, every peer has a source and a reason, and the excluded candidates are named.
2. Every multiple is labelled equity or enterprise, and P/E uses net income attributable to the parent and passed the leverage check.
3. EV is built on one basis for every company, and the items not adjusted for some peers are named.
4. The target and every peer are cleaned on the same items, or all figures are reported and the report says so.
5. The same multiple, base and calendarized period apply to every company, and EBITDA multiples passed the IFRS 16 and US GAAP check.
6. Medians, not means, with the median recomputed without the outlier.
7. ROIC is the FactSet field for every company, with the goodwill treatment stated as unknown.
8. The gap to the justified multiple is split into what spread and growth explain and an unexplained remainder that carries risk.
9. The implied growth and return are stated at the three-year ROIIC, with the cost of capital as an assumption with its range.
10. No table passes eight columns. No cheap, expensive, buy, sell or rating language used as a call; the value from the peer range is labelled derived and is not a target.

## Hand-offs

- The user wants an intrinsic value or a DCF: `bigdata-valuation`. New names that fit a profile: `bigdata-screen`. The economics of the whole industry: `bigdata-sector`.
- After delivering, make one offer: save the peer set as a Bigdata.com watchlist so later comps and checks start from it. Act only on a clear yes.
