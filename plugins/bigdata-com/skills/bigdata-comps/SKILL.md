---
name: bigdata-comps
description: >-
  Peer comparison from Bigdata.com data: peers picked by value drivers rather than sector label,
  multiples built on the same claimant basis at market values, growth, margins, returns and cash
  conversion side by side, medians, and where the company should sit and why. Use when the user
  asks for comps, peer comparables, how a company compares with its peers, or a relative
  valuation. Not for an intrinsic value, which bigdata-valuation covers.metadata:
  bigdata-refs: working-with-bigdata, output-standard, multiples-and-peers, expectations, roic
  bigdata-sector-primer: auto
---

# Comps

This skill builds the comparables table a portfolio manager trusts: a peer set chosen by the economics that drive value, with the selection rule written down before any multiple is shown; every multiple built the same way, numerator and denominator on the same claimants, enterprise value at market values, the metric cleaned of one-offs; growth, margins, returns and cash conversion beside the multiples; medians rather than means; and then the two questions that matter, where the company should sit given its returns, growth and risk, and what its multiple says the market expects. A multiple is a cash-flow model with the forecast left implicit, so this skill makes the forecast explicit. It never calls a stock cheap or expensive as a recommendation. "What is Micron's forward EV/EBITDA against peers?" gets that multiple, the peer table behind it and the median, not the full report.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-comps"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the target with `find_securities`, and every peer the user names in parallel, one call each. Establish the multiple the user cares about if they named one, the peers they want included (keep them, and say if the value drivers argue against one), and whether the question is relative value today or a peer set to reuse. Assume forward multiples on the next fiscal year unless the user says otherwise.

Ask one question only when the answer changes the work: the target resolves to more than one listing, or the company has segments so different that the user must choose which business to compare. Otherwise state the assumptions under the header and proceed.

If the target is Private, there is no market value to put in a multiple. Offer the peers' multiples and operating metrics as a reference set instead, labelled as such.

## Gather

Work through these in order. Each step says what it must produce.

1. **The target.** `bigdata_company_tearsheet` with `sections` set to `company_overview, price_performance, analyst_data`, then `fundamentals, estimates`, then `revenue_segmentation`. Done when market cap, the EV field, debt, cash and securities, leases, pensions, minorities, preferred, equity-method investments, attributable net income, five periods of statements, consensus for the next two fiscal years with vintage and estimate counts, and the segment mix are in hand.
2. **Candidates by two routes.** First `bigdata_screen_companies` on the target's industry, region and size (the classification route). Then a second screen on the value drivers, across industries: growth, EBITA margin, ROIC and capital intensity in ranges around the target's (the driver route). Add the competitors named in the target's annual filing (one `bigdata_search` for the competition section) and the counterparties in `mergers_acquisitions`. Done when there are ten to twenty candidates, each tagged with the route that found it.
3. **Peer figures.** `bigdata_portfolio_tearsheet` on the candidates for current price and market cap, then `bigdata_company_tearsheet` with `sections` set to `fundamentals, estimates` for each peer kept after Analyse step 1. Done when every peer has the same fields for the same fiscal basis, and fiscal year-ends are noted so periods can be calendarized.
4. **Items to clean.** `bigdata_search` in fast mode on the target's latest annual and quarterly filings for restructuring, impairment, write-down, integration costs, litigation and equity-accounted income, then `bigdata_fetch_document` where a table is needed. Repeat for any peer whose reported margin moves more than the others without an operating reason. Done when each item has an amount, a year and a source, and the count of years in the last five with a "one-time" charge is known for the target.
5. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read its valuation conventions: which multiple the sector uses and the traps in its statements.

## Analyse

The five steps of a comparable company analysis (Robinson and Weyns, UBS, "How to analyse and talk the language of multiples", pp. 24-27) run through `references/multiples-and-peers.md`; each step below names the file it loads and ends in what it must produce.

1. **Pick the universe** (five-step 1; `references/multiples-and-peers.md` step 7). Write the selection rule before showing any multiple, because analysts tend to pick high-multiple peers when arguing a stock is cheap. Match on the drivers of value: cash generation and conversion, risk, value-adding growth, then size, product mix, geography, business model, life-cycle stage, and organic against acquired growth. Compare business models, not lines of business. Report how many classification-route peers survive the driver test, give each peer a one-line reason, and name the obvious candidates excluded with the reason. The sources set no minimum count; state the number and test the median with and without the closest and the most distant peer. Done when the peer table has a route and a reason for every name.

2. **Build enterprise value the same way for every company** (`references/multiples-and-peers.md` steps 2 and 3). EV = market cap + debt at fair value if yields have moved + preferred + minorities + unfunded pensions + leases + options - non-operating assets at market value (excess cash, equity stakes, excess real estate), with average or seasonally adjusted net debt. If the metric is before rent, EV includes leases; if after rent, it excludes them. Name the flavor (total, operating or core EV) and match the metric to it. Rebuild EV from the balance sheet rather than trusting the tearsheet field, whose construction is not documented, and say which one the table quotes. Done when the bridge table shows every item for every company.

3. **Match the claimants** (`references/multiples-and-peers.md` step 1). Equity multiples (P/E, P/B) set parent-shareholder value against a metric after debt, minorities and preferred, with net income attributable to the parent; enterprise multiples put every claimant in the numerator. Done when each multiple in the table is labelled equity or enterprise.

4. **Clean the metric** (five-step 4; `references/multiples-and-peers.md` step 4). Add back non-recurring expenses and deduct non-recurring income; remove equity-accounted income from EBITDA and value the stake separately in the bridge; put the present value of an unpaid cash cost in the bridge. A charge that appears in most of the last five years is a cost and stays in. Done when reported and cleaned metrics sit side by side with the items removed and their sources.

5. **Choose the multiple and the base** (five-step 3; `references/multiples-and-peers.md` step 5 and its table). Prefer forward multiples: historical E/P had 1.6 times the dispersion of forward E/P in McKinsey's sample. Prefer EV/EBITA to EV/EBIT, and to EV/EBITDA where capital intensity or outsourcing differs. Use the sector primer's convention where it has one. Calendarize to the same twelve months for every company. Done when the multiple, the base and the period are stated once and applied to every company.

6. **Put the operating metrics beside the multiples** (five-step 2; `references/multiples-and-peers.md` step 6). For each company: consensus sales growth for the next two years and the three-year history, EBITA margin, ROIC, free cash flow over NOPAT, net debt over EBITDA, and capex over sales. ROIC follows `references/roic.md`: one definition for every company, stated in a line under the table, either the FactSet field for all or a hand-built figure for all, never mixed, and without goodwill as the basis for peer comparison. Done when the operating table is complete or each gap is marked.

7. **Medians and position** (`references/multiples-and-peers.md` step 8). Show the median, the interquartile range and the median without the outlier, then the target's premium or discount to the median. A comparison with the company's own history or with the market is valid only if returns, growth, rates, the risk premium, tax and accounting are unchanged, or at a comparable point in the cycle; say which holds. Done when the line "the company trades at X against a peer median of Y (range A to B), a Z percent premium; without [outlier] the median is W" is written.

8. **Where the company should sit and why** (`references/multiples-and-peers.md` step 9). Compute the justified multiple from the returns form, EV / EBITA = (1 - T) x (1 - g / ROIC) / (WACC - g), at a stated cost of capital (assumed, with a range of plus and minus 1 point), for the target and the peer median. Split the actual multiple into the steady-state part (1 / WACC for EV/NOPAT, 1 / cost of equity for P/E) and the turns paid for value creation. Then decompose the premium or discount into the part explained by the ROIC spread, by growth and by risk, and the part left unexplained. Compare multiples against ROIC, never against growth on a straight line. Done when the gap between actual and justified multiple is stated in turns with the driver that explains it, and the unexplained remainder is named.

9. **What the multiple implies about growth and returns.** Load `references/expectations.md` and run steps 1 to 5 on the target. Solve the implied perpetual NOPAT growth g = (EV x WACC - NOPAT1) / (EV - NOPAT1 / ROIIC) at the company's ROIIC from `references/roic.md`; place the forward P/E on the warranted P/E grid (table 1, rerun at the assumed cost of equity); state which of the three paths to the same multiple the company is on (fast growth on a thin spread, or slow growth on a wide one); and compare the implied competitive advantage period with the historical market-implied average of about 8 years, 1976 to 2007 (verify). Done when the report states what growth and return the multiple assumes next to consensus growth and the company's ROIIC.

10. **The value the peer range implies** (five-step 5). Apply the peer median and the quartiles to the target's cleaned metric, then bridge core EV to equity per share, adding non-core stakes and deducting the present value of non-recurring cash costs. Present it as a range labelled derived, not as a target: a multiple is a check on a forecast, never a substitute. Done when the range per share sits next to the price.

A narrow question gets steps 1 to 7 for the multiple asked about, with the peer table and the median.

Special cases, from `references/multiples-and-peers.md`:

- **Banks and insurers.** No EV multiples. Compare P/B against ROE; P/B = (ROE - g) / (ke - g), so a premium to book needs ROE above the cost of equity.
- **Cyclicals.** Normalize to mid-cycle earnings first; a forward P/E looks low at the peak and high at the trough, and consensus tends to ignore the cycle.
- **Loss-making high growth.** Forward EV/Sales with the long-run margin stated as an assumption.
- **Emerging markets.** Prices are weaker anchors; triangulate with a second multiple and widen the range.
- **Multi-business companies.** Compare each segment with its own peers; a blended multiple matches none of the units. Hand the sum of the parts to `bigdata-valuation`.
- **Niche industries.** Listed peer sets are smaller, older and survivor-biased; widen to global listings or adjacent sub-industries and say so.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) comparables, <date>
Data as of: prices <date>; estimates <date>; statements <period>.

## Where it sits
Four to six sentences: the multiple against the peer median, how much of the gap the returns,
growth and risk explain, what the multiple implies about growth and returns, and what would
change the reading. No rating.

## The peer set
Selection rule, stated first.
| Peer | Ticker | Route (classification, drivers, both) | Reason | Fiscal year-end | Source |
Excluded candidates, each with the reason.

## Enterprise value
| Company | Market cap | Debt | Leases | Pensions | Minorities | Preferred | Excess cash | Non-core | EV | Basis | Source |
Which EV is quoted (rebuilt or tearsheet field).

## Cleaned metric
| Company | Reported EBITA | Items removed | Cleaned EBITA | Years with one-time charges (of 5) | Basis | Source |

## Multiples
| Company | Chosen multiple (fwd) | Second multiple | Equity or enterprise | Basis | Source |
Median, interquartile range, median without the outlier, target premium or discount.

## Operating metrics
| Company | Sales growth FY1, FY2 | 3-yr history | EBITA margin | ROIC | FCF / NOPAT | Net debt / EBITDA | Capex / sales | Basis | Source |
ROIC definition line under the table.

## Where it should sit and why
Justified multiple for the target and the peer median at the stated cost of capital; steady-state
and value-creation turns; the premium decomposed into spread, growth, risk and unexplained.

## What the multiple implies
Implied growth at the stated ROIIC, position on the P/E grid, implied advantage period, against
consensus and history.

## Value from the peer range
| Multiple | Lower quartile | Median | Upper quartile | Equity value per share | Basis |

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: two to four pages. Offer the peer table as a spreadsheet when the host can create files. For a narrow question, answer it in the method's terms with the peer table and the sources, and keep the footer.

## Checks before sending

1. The selection rule appears before the multiples, every peer has a route and a reason, and the excluded candidates are named.
2. Every multiple is labelled equity or enterprise, and P/E uses net income attributable to the parent.
3. EV is built with the same items for every company, and the report says whether it is rebuilt or the tearsheet field.
4. The target's metric is cleaned, with the items removed, their sources and the recurrence count shown.
5. The same multiple, base and calendarized period apply to every company.
6. Medians, not means, with the median recomputed without the outlier.
7. One ROIC definition across the table; FactSet and hand-built figures are never mixed.
8. The premium or discount is decomposed into what returns, growth and risk explain and what is left unexplained.
9. The implied growth and return are stated with the cost of capital as an assumption with its range.
10. No cheap, expensive, buy, sell or rating language used as a call; the value from the peer range is labelled derived and is not a target.

## Hand-offs

- The user wants an intrinsic value or a DCF: `bigdata-valuation`. New names that fit a profile: `bigdata-screen`. The economics of the whole industry: `bigdata-sector`.
- After delivering, make one offer: save the peer set as a Bigdata.com watchlist so later comps and checks start from it. Act only on a clear yes.
