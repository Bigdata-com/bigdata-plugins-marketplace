---
name: bigdata-capital-allocation
description: >-
  Capital allocation review: buybacks, dividends, reinvestment and acquisitions, and whether each
  created value. Use for payout policy, buyback vs dividend, M&A record, incentives. Not one
  announced deal: bigdata-deal-analysis.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, capital-allocation, roic, expectations, credit
  bigdata-sector-primer: auto
---

# Capital allocation

This skill judges whether management turns cash into long-term value per share, the goal set by Mauboussin's "Capital Allocation" (2015): not growth, not earnings per share, not the share price. It tabulates five years of sources and uses, runs one numeric test per use (organic reinvestment, acquisitions, divestitures, dividends, buybacks, debt), reads what the proxy pays management for, and says what each finding means for value per share. Most actions are sound at one price and unsound at another, so every test compares what was paid with what was received. It gives no composite score and no rating. A narrow question ("was Apple's buyback a good use of cash?") gets the buyback test alone.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-capital-allocation"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Fix the window: the five fiscal years the tearsheet returns. When the user asks about a decade of M&A or a long CEO tenure, extend the deal list by search and say in Gaps that the statements stop at five years. Note the CEO changes in the window, because a new CEO often shifts the mix. Fix which deals count as material: state the threshold used (for example, a share of the buyer's market cap), since the sources give none.

Establish the reader. An investor gets the review below. A corporate finance team or board asking about its own choice ("buy back shares or raise the dividend", "pay down debt or acquire") gets the same tests plus the arithmetic for each option laid side by side; `references/output-standard.md` treats that as analysis of a corporate choice, not a call on a security. A competitor's or a target's record is a valid subject too; write the implications for that reader.

Ask one question only if the answer changes the work: the user asks about "management" and the company has had several CEOs in the window, or the name is ambiguous. Otherwise state the window and threshold in the header and proceed. Done when the window, the threshold, the reader and any options to compare are stated.

Narrow questions map to steps in the Analyse section, with the sources-and-uses table as context:
- Buybacks: steps 4 and 5. Dividends: step 6. Leverage and how payouts were funded: step 9.
- The M&A track record: steps 7 and 8, over the window the user names.
- What management is paid for: step 10.

If the company is Private, say there is no share price for the buyback and deal-reaction tests and run the sources-and-uses, reinvestment and deal-price tests from whatever statements and filings Bigdata.com holds. The method does not apply as written to banks and insurers, utilities, early-stage companies and many emerging markets (`references/capital-allocation.md`, interpretation rules); follow the special cases at the end of the Analyse section and say which tests were adapted and why.

## Gather

1. **The company's numbers.** Profile and quote, the executive team and board, and the deal history; then five fiscal years of annual statements, ratios and key metrics; then the dividend history. The executive team and the deal history need FactSet access: if either comes back empty, search for the executive changes and for the acquisitions in the window instead. Done when every item in the method's inputs table is in hand for each of the five years, with the deal list, the executives and the competitors block from the company profile.
2. **Repurchase actuals.** Search and fetch the annual and quarterly filings for the issuer repurchase tables: shares bought and average price paid by period, authorisations, and shares issued under compensation plans. Done when each year has shares bought, the average price, the amount spent and shares issued, or the gap is named. Authorisations are not purchases.
3. **Price series.** Daily share prices over the window and around each material deal announcement, and the market index over the same days, computed, not estimated. Done when the average price in each buyback year and the buyer's one-, three- and five-day moves against the index around each announcement can be computed.
4. **Each material deal.** One search per deal for the announcement: price, form of payment, the target's undisturbed price, the synergies claimed by type and timing, the integration cost, and the stated rationale. Then a search for later goodwill impairments, write-downs or disposals of the acquired unit. Done when each deal has its announcement source and its later record, or the gap is named.
5. **Divestitures and spin-offs.** Searches for disposals and spin-offs in the window, with price and rationale. Done when each is listed with its source.
6. **The proxy statement.** Search and fetch the latest proxy (DEF 14A or the local equivalent), and the prior one if the plan changed, for the items in method step 10 plus the ownership and voting structure. Done when each item is recorded with its section.
7. **What management says it does.** Search for management's stated capital allocation priorities on calls and at investor days, and for insider sales during buyback periods. Done when the stated priorities are quoted with dates, to compare words with actions.
8. **Peers.** Resolve two to four peers from the competitors block, then five fiscal years of annual statements and key metrics for the peer set, pulled as a set rather than one company at a time where the account allows. Done when each peer has payout, net shareholder yield and leverage for the same years.
9. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the value-driver and valuation-conventions subsections for capital intensity. Done when the sector's capital-intensity and valuation conventions are noted, or their absence is stated.

## Analyse

Load `references/capital-allocation.md` before step 1, `references/roic.md` before step 3, `references/expectations.md` before step 4 and `references/credit.md` before step 9. Each step runs the method step named; the line keeps what this skill adds and the done condition.

1. **Sources and uses** (method step 1). Done when the table ties to the change in cash each year.

2. **Spending pattern** (method step 2, formula 2), with inflection points and CEO changes marked. Compare with the company's own history and the peers, since the sources give no industry ranges. Done when the mix and any shift are stated.

3. **Reinvestment returns against the cost of capital.** `references/roic.md` steps 1 to 11 and method step 4: ROIC with and without goodwill, the spread over a stated cost of capital (assumed, with its build), growth capex as a share of capex, asset life and age (formula 12), and the retention test. ROIIC is a three-year rolling figure, labelled; five annual periods allow no five-year window. The three-year figure is what the value-trigger test in `references/expectations.md` formula 4 compares with the cost of capital; a single year is never evidence, because a high reading can be operating leverage. Done when level, direction, the spread, the three-year ROIIC against the cost of capital and the retention test are stated.

4. **The buyback return test, net of issuance** (method step 5, formula 4). Value per share at each buyback date is an assumption; build it one of two ways and label which:
   - Model at the time: steady-state value from that year's normalised NOPAT over the cost of capital, plus future value creation (`references/expectations.md` formula 1) at the three-year ROIIC to that year and a competitive advantage period stated as an assumption, with a sensitivity of a few years either way. The period is chosen, never observed.
   - Range at the time: the valuation range published then in research or news, quoted with its date and labelled press or research summary.
   Lay the record against the valuation path: did buying rise when the stock was dear and stop when it was cheap? A later price fall does not prove an error. Buying back shares to offset stock compensation is not value creation. Done when each year has a price-to-value return with its method named and a net issuance figure.

5. **The EPS breakeven P/E** (formula 6). Done when the breakeven sits next to the P/E paid each year, with the sentence that EPS accretion is not value.

6. **Dividend tests** (method step 6, formula 7). Done when coverage, funding source and net shareholder yield are stated for each year, with the peer median beside them.

7. **The deal table** (method step 7, formulas 8 to 11, tables 1 and 2). Haircut cost synergies and haircut revenue synergies heavily, against the synergy base rates in table 2 quoted with their period as historical. Done when every material deal has its row, including the later record of impairments and disposals.

8. **Divestitures** (method step 8). Done when each disposal is listed with its price, rationale and whether units earning below the cost of capital remain.

9. **Leverage.** Place the company on table 3 of `references/credit.md` first (FFO / debt and debt / EBITDA, debt adjusted for leases and pensions), then on table 1 as the cross-check (EBIT / interest and debt / total capital), and say when the two disagree; check whether payouts were financed by borrowing (method step 9). Done when both placements are stated with their samples and periods; for a full credit view, hand off to `bigdata-credit`.

10. **The incentive review** (method step 10, table 7 quoted as historical). Absolute TSR is mostly luck; EPS and revenue targets can drive buybacks and deals that lift the metric without value. Note the ownership and voting structure, since it decides whom the plan serves. Done when each metric is classified and the conflict question (if the plan and value per share conflict, which way does the CEO go?) is answered.

11. **Verdict per use and what it means for value** (method step 11). Then what each finding means for value per share going forward: whether reinvestment at the current spread adds value (`references/expectations.md` formula 4 on the three-year ROIIC), the value transferred to sellers in buybacks above value or premiums above synergies, in currency per share, the net share count trend, and whether the incentive plan makes the pattern likely to continue. No composite score. Done when every use has its line and the forward implication is stated.

12. **The options side by side, corporate decision only.** For each option the user names (buy back, raise the dividend, pay down debt, acquire), the cash cost, the effect on value per share at the stated value per share (formula 5 for a buyback), the EPS effect, leverage after on table 3 of `references/credit.md`, and what it commits the company to (a dividend is treated as a commitment, a buyback as residual). Done when the options sit in one table with their arithmetic and trade-offs, and no option is recommended.

Compare words with actions throughout: the priorities management states on calls, what the incentive plan rewards, and what the sources-and-uses table shows it did. Where the three disagree, say so with the figures.

Special cases:
- Serial acquirers of many small deals: aggregate the tuck-ins by year and judge them through ROIC with goodwill and later impairments, since a deal-by-deal table would be mostly gaps.
- Banks and insurers: judge payouts and buybacks against regulatory capital and ROE against the cost of equity, not against free cash flow and ROIC.
- Utilities: returns are set by the regulator, so judge reinvestment by growth in the rate base and the allowed return on equity against the cost of equity, and judge payouts against the capital structure the regulator assumes; the buyback test rarely applies. Read the utilities primer for the allowed-return terms.
- Companies outside the US: use the home-region base rates for payout and M&A (Mauboussin, Capital Allocation Outside the U.S., 2016, historical), and note legal limits on buybacks and an ownership structure (family, state, cross-holdings) that sets the payout.
- Early-stage companies: ROIIC is unstable; report the cash burn and the funding history instead of the reinvestment tests.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) capital allocation, FY<first> to FY<last>, <date>
Data as of: statements <latest fiscal period>; price <date>; proxy <year>; newest document <date>.
Assumptions: cost of equity, cost of capital, value per share at each buyback date and its method,
material-deal threshold, synergy haircuts, each with its basis and a sensitivity.

## The reading
Four to eight sentences: where the cash went, which uses created or destroyed value and by how much
per share, what management is paid for, and what the pattern means for value per share from here.

## Sources and uses
| Line | FY-4 ... FY0 | Total | Basis | Source |
Then the cents-per-dollar-of-sales-change line, with CEO changes marked.

## Reinvestment returns
| Year | ROIC ex goodwill | ROIC incl goodwill | WACC (assumed) | Spread | ROIIC 3-yr | Growth capex share |
Basis and sources note under the table. The retention test in one line.

## Buybacks
| Year | Spent | Shares bought | Average price | Shares issued | Net share change | Basis | Source |
| Year | Value per share then (method) | Return vs cost of equity | EPS breakeven P/E | P/E paid | Basis | Source |

## Dividends
| Year | Dividends | FCF after SBC | Coverage | Funding source | Net shareholder yield | Basis | Source |

## Against peers
| Company | Payout ratio | Net shareholder yield | Net debt / EBITDA | Basis | Source |
Peer median row.

## Acquisitions and divestitures
| Deal | Date | Premium | PV synergies (cost / revenue) | NPV | SVAR | Payment | Return on price paid |
| Deal | Predicted vs actual buyer move | Category and base rate | Later impairment or disposal | Basis | Source |
Basis and sources note under the first table. Disposals and spin-offs below.

## Leverage
Placement on the agency ranges (FFO / debt, debt / EBITDA), then on the rating medians; payouts
financed by debt.

## Incentives and governance
| Plan element | Detail | Basis | Source |
The conflict question answered in one line.

## Verdict by use and what it means for value
| Use | Verdict | Deciding test | Value per share effect | Basis | Source |
Then the forward implication in two to four sentences.

## The options side by side (corporate decision only)
| Option | Cash cost | Value per share effect | EPS effect | Leverage after | Commitment | Basis |

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. The cost of equity, the cost of capital and value per share at each buyback date appear once in an Assumptions line with their basis and a sensitivity. For a narrow question, answer with the relevant test, its table and the sources, and keep the footer.

## Checks before sending

1. The sources-and-uses table ties to the change in cash each year.
2. Buybacks use actual repurchases and prices paid, not authorisations, and are shown net of issuance.
3. Value per share at each buyback date is labelled assumed with its method named; any competitive advantage period in it is stated as an assumption, never as observed.
4. The EPS breakeven P/E appears with the statement that accretion is not value.
5. ROIIC is the three-year rolling figure, labelled, and only that figure is compared with the cost of capital.
6. Every material deal has premium, synergies against base rates, SVAR and the later record, or a named gap.
7. Leverage is placed on the agency ranges first and the rating medians second, each with its sample and period.
8. Each incentive metric is classified from the proxy, with its source.
9. No composite score, rating or recommendation; each use has its own verdict and basis; a corporate decision gets the options side by side with none recommended.
10. Dated base rates carry their source and period and are called historical. No table passes eight columns.

## Hand-offs

- The user asks about one announced or rumoured deal: `bigdata-deal-analysis`.
- The user wants the moat or industry structure behind the returns: `bigdata-moat`. The debt and refinancing in depth: `bigdata-credit`.
- After delivering, make one offer: a monitor on the company's buyback, dividend and M&A announcements, or save the report to the user's Bigdata.com account. Act only on a clear yes.
