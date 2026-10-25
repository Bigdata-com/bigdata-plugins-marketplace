---
name: bigdata-earnings-quality
description: >-
  Quality of earnings: accruals, cash conversion, EBITA rebuild, recurring one-offs, revenue
  recognition, flags by severity. Use for are earnings real, QoE, forensic accounting, red flags.
  Not one quarter: bigdata-earnings-review.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, earnings-quality, roic
  bigdata-sector-primer: auto
---

# Earnings quality

This skill tells a portfolio manager how much of a company's reported profit is backed by cash, how much of it will recur, whether it is fairly stated, and what earning power a valuation should therefore use. It rebuilds operating profit from the notes, tests profit against cash and against the change in equity, counts the "one-time" items that keep coming back, and ends in a flags table with a severity level and a line on what each flag changes in the valuation inputs. A flag is a question for the notes, not an accusation. It is sized to the question: "is cash conversion healthy at Nike?" gets the accrual series, CFO to net income and the working-capital lines, not the full report.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not. Stop there: give no view, drivers, risks, figures or dates from memory while the tools are missing, and do not fall back to web search.
- Pass `plugin_slug: "bigdata-earnings-quality"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company with `find_securities`. Establish three things: the window (five fiscal periods plus the last twelve months by default; five to ten years when the question is about normal earning power through a cycle), the user's concern if they named one (receivables, a short-seller report, a non-GAAP gap, a reserve release that carried a beat), and the peers the comparison will use. State the window and the peers in the header when the user did not give them.

Ask one question only if the answer changes the work: the name resolves to more than one listing, or the user refers to a specific allegation or document that a search does not find. Otherwise proceed.

If `find_securities` returns the company as Private, say that the tearsheet carries different content for private companies, use whatever statements and filings Bigdata.com holds, and name the tests that could not be run in the Gaps line. For a bank or an insurer, the accrual, EBITA and working-capital tests do not apply; say so and run the equity reconciliation, reserve adequacy and loan-loss provisioning instead (`references/earnings-quality.md`, interpretation rules).

## Gather

1. **Tearsheet.** `bigdata_company_tearsheet` with `sections` set to `company_overview, latest_earnings, earnings_calendar` first, then `financial_statements, financial_ratios, key_metrics`. Use `interval` annual for five fiscal years; there is no period offset, so a longer window is noted in the Gaps line. Done when revenue, operating income, net income, CFO, capex, depreciation, receivables, inventory, payables, deferred revenue, gross and net PP&E, goodwill and intangibles, total assets, equity, dividends, buybacks, issuance, SBC and leases are in hand for every period, with the FactSet Altman Z and Piotroski fields.
2. **The latest annual report and the one before it.** `bigdata_search` in fast mode for the annual filing with the reporting period filter, then `bigdata_fetch_document`. Read the notes this method needs: special items and restructuring, the provisions roll-forward, pensions, leases, the tax reconciliation, the revenue recognition policy, capitalised development, SBC, the statement of changes in equity and OCI, factoring or securitised receivables, related parties, and the auditor's report. Compare the revenue and capitalisation policies with the prior year's wording. Done when each note is recorded with its page or section, or marked not found.
3. **Year-to-date figures for the last twelve months.** Search and fetch the latest quarterly filing. Done when LTM revenue, operating profit, net income and CFO are computed with formula 9 of `references/earnings-quality.md`.
4. **Non-GAAP reconciliations.** One search per fiscal year for the company's adjusted earnings reconciliation in its results releases. Done when every adjustment type is listed by year, so recurrence can be counted.
5. **Management's explanations.** Search and fetch the last two earnings calls. Done when management's explanation of any working-capital swing, reserve movement, one-off or margin change is quoted, or marked as not discussed.
6. **Governance and disclosure events.** One search each, over the window: auditor resignation or dismissal; restatements or material weakness; late filings or regulatory inquiries into the accounts; related-party dealings; short-seller or forensic research on the company; KPIs, segments or interim data dropped. Done when each is marked present with a source, absent, or not found.
7. **Peers.** Three to six peers named in the filing or found with `bigdata_screen_companies` on industry and size, then `bigdata_company_tearsheet` with `financial_statements, financial_ratios, key_metrics` for each. Done when peer medians for the accrual ratio, CFO to net income, DSO, DIO, DPO, depreciation rate and goodwill to equity can be computed.
8. **Sector primer.** If the company's sector has a section in `references/sector-primers.md`, read its accounting-traps section before analysing. Done when the sector's traps are noted, or their absence is stated.

## Analyse

Load `references/earnings-quality.md` before step 1 and `references/roic.md` before step 12.

1. **Window and LTM.** Set the window and compute LTM with formula 9 (prior fiscal year plus current year-to-date minus prior year-to-date). Done when the window and LTM figures are stated.

2. **The accrual series.** Compute the accrual ratio for each of the five periods and LTM with the one definition the method uses, formula 1: (net income minus CFO) divided by average total assets. Positive means profit above cash. Do not substitute a balance-sheet accrual measure: acquisitions, disposals and currency distort balance-sheet changes. Add CFO to net income for each year and the peer median. The sources give no numeric cutoff, so read sign, trend and the peer median. Done when values, sign, trend and peer median sit in one table.

3. **The EBITA rebuild.** Start at reported operating profit and apply formula 2 (method step 3): add back amortisation of acquired intangibles only; remove impairments, write-offs, restructuring, litigation, asset-sale gains, acquired in-process R&D and pension gains, including any buried in cost of sales or SG&A; pair each gain with losses booked the same year or charged to equity; reverse the net movement in income-smoothing provisions; keep SBC as an expense. Done when every adjustment cites its note and reported operating profit sits beside adjusted EBITA for each year.

4. **One-offs counted by recurrence.** For each special-item type, count the years with a charge in the window and the average charge as a percent of revenue (method step 4). Treat a type that appears in two or more of five years as a recurring operating cost; this rule is the method's assumption, not a sourced threshold, and the report labels it so. Done when each type has its count, its average and its treatment.

5. **Provisions and reserves.** Classify each provision by table 1 of the method (ongoing operating, long-term operating, nonoperating, income-smoothing) and tabulate opening balance, charge, utilisation, release and closing balance (method step 5). Done when the contribution of releases to EBITA is stated in currency and as a percent of EBITA, and to any beat of consensus where one occurred.

6. **Pensions, leases, stock compensation, sold receivables.** Follow method step 6. Pensions: keep service cost and prior-service amortisation in operating cost, move the rest below EBITA, record the expected-return assumption, and treat the after-tax unfunded liability as debt. Leases: where rent is still an operating cost, capitalise it with formula 3 at an assumed cost of secured debt; where the liability is on the balance sheet, use it, and confirm the standard for each period. SBC: never add it back; subtract it from CFO in any free cash flow; show buybacks net of issuance. Factored or securitised receivables: add them back with matching debt and treat the fee as interest. Done when each item shows its effect on EBITA, free cash flow and debt.

7. **Revenue recognition and working capital.** Compute receivables growth minus revenue growth, DSO, inventory growth minus sales growth, DIO, DPO and working capital excluding inventory (formula 7, method step 7). For subscription businesses compare deferred revenue growth with revenue growth; for long-term contracts compare contract assets with revenue. Note that a rising DPO lifts CFO for a time and reverses later. Done when each ratio has a trend and a cause from the filing or the call, or is marked unexplained.

8. **Capitalisation and depreciation.** Compute PP&E growth minus revenue growth, depreciation over average gross PP&E, asset life (gross PP&E over depreciation; a longer life lowers the charge), goodwill and intangibles over equity, and capitalised development with its amortisation life (method step 8, formula 4). Flag only wide gaps against the company's own history and the peers. Done when each has a trend and a peer comparison.

9. **Taxes.** Compare tax-implied profit (formula 6: income tax expense over the statutory rate) with reported pretax profit, and cash taxes with the book charge. Done when the gap is stated and, if wide, explained from the tax note.

10. **The earnings-to-equity reconciliation.** Compute formula 5 over the window: the change in equity minus (net income plus OCI minus dividends plus issuance including the SBC credit minus buybacks). Charges taken straight to equity outside OCI show up in the residual. The sources give no threshold, so report the residual as a percent of cumulative net income. Done when the residual is explained from the equity statement or flagged.

11. **Normalised earning power.** Follow method step 12: over five to ten years spanning a cycle, remove nonrecurring items from the current-year view but keep them in the multi-year average; test whether results cluster around the average or are unrelated figures whose average is accidental; prefer the average to the trend unless the trend has a cause. Add steady-state free cash flow with formula 8 (net income plus D&A minus maintenance capex, proxied by depreciation, minus SBC). For a cyclical, normalise on mid-cycle margins. Done when reported, adjusted and normalised earnings, the window and the range are shown, with where the latest year sits.

12. **What it does to returns.** From `references/roic.md`: recompute NOPAT from adjusted EBITA at the operating tax rate and ROIC with and without goodwill, before and after the lease and capitalised R&D adjustments, and name which figure the FactSet ROIC field corresponds to, if any. Never put the FactSet field and the hand-built figure in one comparison. Flag a ROIC lifted by write-offs that shrink capital. Done when ROIC on reported and on adjusted profit sit side by side.

13. **Flags and severity.** Run the flags in table 2 of the method (profit above cash, receivables build, inventory build, payables stretch, receivables sold, capitalised cost, light depreciation, recurring special items, gains in operating profit, smoothing provisions, write-off then clean slate, pension credit, tax gap, equity bypass, goodwill load, EPS against revenue, non-GAAP drift, disclosure dropped, governance events). For each triggered flag give the number, the period, the source and the company's explanation with whether the numbers support it. Assign a level from table 3 (0 no flags to 4 evidence of manipulation): take the highest level triggered, and raise it one step when two flags sit at that level (an assumed rule). The scale was designed for these skills and the report says so. At level 4, say the figures cannot be adjusted and should not be relied on, as Graham and Dodd do. Done when every triggered flag has its row and the level has a one-line reason.

14. **What each flag means for the valuation inputs.** Map every flag at level 2 or above to the input it changes: recurring one-offs, pension credits, smoothing releases and gains change EBITA and NOPAT; capitalised costs, light depreciation, capitalised R&D and leases change invested capital and ROIC; SBC, payables stretch and sold receivables change free cash flow; unfunded pensions, leases and sold receivables add debt-like claims to the equity bridge; normalised earning power replaces the latest year as the earnings base for a multiple. Done when each input shows the reported and the adjusted figure and the flag behind the change.

Quote Piotroski and Altman Z from the tearsheet as FactSet reports them, with no zones or cutoffs attached, since the sources give none. Compute no Beneish M-score or other fitted manipulation score. For acquirers use organic and pro forma figures; for cross-border listings compare local accounting with foreign peers; for loss-making companies use CFO and cash burn.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) earnings quality, <date>
Data as of: statements <latest fiscal period and LTM>; newest document <date>; peers <names>.

## The reading
Four to eight sentences: how much of reported profit is backed by cash, the rebuilt EBITA against
reported operating profit, the flags that matter and the severity level with its reason, and what
it changes in the valuation inputs. Flags framed as questions with the company's explanation.

## Cash against profit
| Period | Net income | CFO | Average total assets | Accrual ratio | CFO / NI | Peer median | Basis | Source |

## EBITA rebuild
| Line | FY-4 ... FY0, LTM | Note | Basis | Source |
From reported operating profit to adjusted EBITA, one row per adjustment.

## One-offs that recur
| Charge type | Years with a charge (n of 5) | Average % of revenue | Treatment | Basis | Source |

## Provisions and reserves
| Provision | Type | Opening | Charge | Utilised | Released | Closing | Effect on EBITA | Basis | Source |

## Pensions, leases, stock compensation and sold receivables
| Item | Effect on EBITA | Effect on free cash flow | Effect on debt | Basis | Source |

## Revenue recognition, working capital and capitalisation
| Ratio | FY-4 ... FY0 | Peer median | Cause | Basis | Source |

## Taxes and the equity reconciliation
Tax-implied against reported profit; cash against book taxes; the equity residual as a percent of
cumulative net income, explained or flagged.

## Governance and disclosure
| Item | Present / absent / not found | Basis | Source |

## Normalised earning power
Reported, adjusted and normalised earnings per share with the window and range; steady-state FCF.
ROIC on reported and on adjusted profit, with the definition line.

## Flags and severity
| Flag | Value | Period | Company's explanation | Basis | Source |
Severity level n, with the reason and a note that the scale is this method's design.
Piotroski and Altman Z as reported by FactSet.

## What this means for the valuation inputs
| Input | Reported | Adjusted | Flag behind the change | Basis | Source |
Rows: EBITA and NOPAT, invested capital and ROIC, free cash flow, debt-like claims, earnings base.

## What would change this view
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. Every assumed input (cost of secured debt, recurrence rule, materiality threshold, R&D life) appears once in an Assumptions line with its basis. For a narrow question, answer it with the method's step for that question, its table and the sources, and keep the footer.

## Checks before sending

1. One accrual definition, formula 1, used for every period and every peer.
2. Every EBITA adjustment cites the note it came from, and SBC stays an expense throughout.
3. Each special-item type is counted by recurrence, and the two-of-five rule is labelled assumed.
4. Reserve releases are sized in currency and as a percent of EBITA.
5. The equity residual is shown and either explained or flagged.
6. Piotroski and Altman Z are quoted as reported with no zones; no Beneish or other fitted score appears.
7. The severity level has a reason and the scale is labelled as this method's design, not a sourced standard.
8. Each flag at level 2 or above maps to a valuation input with reported and adjusted figures.
9. The FactSet ROIC field and the hand-built ROIC are never in one comparison.
10. The language is diagnostic: no "fraud", "manipulation" or rating word unless a filing or regulator says it, and then with the citation.

## Hand-offs

- The user wants one quarter's results against consensus: `bigdata-earnings-review`.
- The flags point at the balance sheet or refinancing: `bigdata-credit`. The user wants the downside more broadly: `bigdata-risk`.
- The user wants the adjusted figures carried into a value range: `bigdata-valuation`.
- After delivering, make one offer: a monitor on the company's filings and news for auditor changes, restatements and reserve releases, or save the report to the user's Bigdata.com account. Act only on a clear yes.
