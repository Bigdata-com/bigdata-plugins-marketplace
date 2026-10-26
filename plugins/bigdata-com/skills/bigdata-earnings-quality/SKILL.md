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

This skill tells a professional reader how much of a company's reported profit is backed by cash, how much of it will recur, whether it is fairly stated, and what earning power a valuation should therefore use. It rebuilds operating profit from the notes, tests profit against cash and against the change in equity, counts the "one-time" items that keep coming back, and ends in a flags table with a severity level and a line on what each flag changes in the valuation inputs. A flag is a question for the notes, not an accusation. It is sized to the question: "is cash conversion healthy at Nike?" gets the accrual series, CFO to net income and the working-capital lines, not the full report.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-earnings-quality"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Establish three things: the window (the five fiscal periods the tearsheet returns plus the last twelve months; when the question is about normal earning power through a cycle, say in Gaps that the series stops at five years), the user's concern if they named one (receivables, a short-seller report, a non-GAAP gap, a reserve release that carried a beat), and the peers the comparison will use. The subject may be the user's own company, a competitor, a customer or supplier whose accounts they rely on, or an acquisition target; write the implications for that reader. State the window and the peers in the header when the user did not give them.

Ask one question only if the answer changes the work: the name resolves to more than one listing, or the user refers to a specific allegation or document that a search does not find. Otherwise proceed. Done when the company, window, concern, reader and peers are stated.

If the lookup returns the company as Private, say that the tearsheet carries different content for private companies, use whatever statements and filings Bigdata.com holds, and name the tests that could not be run in the Gaps line. For a bank or an insurer, the accrual, EBITA and working-capital tests do not apply; say so and run the equity reconciliation, reserve adequacy and loan-loss provisioning instead (`references/earnings-quality.md`, interpretation rules).

## Gather

1. **Annual numbers.** Five fiscal years of annual statements, ratios and key metrics. Done when every input in the method's inputs table is in hand for the five fiscal years, with the FactSet Altman Z and Piotroski fields.
2. **Quarterly numbers.** Quarterly statements for the last five quarters, plus the company profile for the competitors block. Done when LTM revenue, operating profit, net income and CFO are computed as the sum of the last four quarters (the same result as formula 9 of `references/earnings-quality.md`), with the latest quarter's balance sheet.
3. **The latest annual report and the one before it.** Both annual filings in full, each with its fiscal year fixed rather than inferred. Read the notes the method's inputs table lists, plus the auditor's report. Compare the revenue and capitalisation policies with the prior year's wording. Done when each note is recorded with its page or section, or marked not found.
4. **Non-GAAP reconciliations.** One search per fiscal year for the company's adjusted earnings reconciliation in its results releases. Done when every adjustment type is listed by year, so recurrence can be counted.
5. **Management's explanations.** Search and fetch the last two earnings calls. Done when management's explanation of any working-capital swing, reserve movement, one-off or margin change is quoted, or marked as not discussed.
6. **Governance and disclosure events.** One search each, over the window, for the items in method step 11, plus short-seller or forensic research on the company. Done when each is marked present with a source, absent, or not found.
7. **Peers.** Three to six peers from the competitors block, the filing or a screen on industry and size, then five fiscal years of annual statements, ratios and key metrics for the peer set, pulled as a set rather than one company at a time where the account allows. Done when peer medians for the accrual ratio, CFO to net income, DSO, DIO, DPO, depreciation rate and goodwill to equity can be computed.
8. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read its accounting-traps subsection before analysing. Done when the sector's traps are noted, or their absence is stated.

## Analyse

Load `references/earnings-quality.md` before step 1 and `references/roic.md` before step 12. Steps 2 to 11 and 13 run the method's step of the same subject; read it there and keep the done condition below.

1. **Window and LTM.** Done when the window, the four accrual years it allows and the LTM figures are stated.

2. **The accrual series.** Method step 2, formula 1 only. Five annual periods give four accrual ratios, because each needs the prior year's total assets; add LTM. Done when values, sign, trend, CFO to net income and the peer median sit in one table.

3. **The EBITA rebuild.** Method step 3, formula 2. Done when every adjustment cites its note and reported operating profit sits beside adjusted EBITA for each year.

4. **One-offs counted by recurrence.** Method step 4. The two-of-five rule is the method's assumption, not a sourced threshold, and the report labels it so. Done when each type has its count, its average and its treatment.

5. **Provisions and reserves.** Method step 5 with table 1. Done when the contribution of releases to EBITA is stated in currency and as a percent of EBITA, and to any beat of consensus where one occurred.

6. **Pensions, leases, stock compensation, sold receivables.** Method step 6, with formula 3 for leases at an assumed cost of secured debt and the standard confirmed for each period. Done when each item shows its effect on EBITA, free cash flow and debt.

7. **Revenue recognition and working capital.** Method step 7, formula 7. Done when each ratio has a trend and a cause from the filing or the call, or is marked unexplained.

8. **Capitalisation and depreciation.** Method step 8, formula 4. Done when each has a trend and a peer comparison, and only wide gaps are flagged.

9. **Taxes.** Three tests: tax-implied profit against reported pretax profit (formula 6); the rate reconciliation in the tax note, item by item, for one-off benefits, a falling rate without an operating cause, and reconciling items that recur under a "one-time" label; and cash taxes against the book charge over the window, with the change in deferred tax that explains the gap. Done when each test has its figure and, where a gap is wide, the line of the tax note that explains it or a flag.

10. **The earnings-to-equity reconciliation.** Method step 10, formula 5. Report the residual as a percent of cumulative net income, since the sources give no threshold. Done when the residual is explained from the equity statement or flagged.

11. **Normalised earning power.** Method step 12, over the five annual periods (the method asks for five to ten; say in Gaps that the series stops at five). Add steady-state free cash flow with formula 8: net income plus D&A minus maintenance capex, proxied by depreciation. Stock compensation is already an expense inside net income, so it is neither deducted again nor added back; if the company's adjusted figures add it back, remove that add-back. For a cyclical, normalise on mid-cycle margins. Done when reported, adjusted and normalised earnings, the window and the range are shown, with where the latest year sits.

12. **What it does to returns.** `references/roic.md` steps 2 and 7 to 9 on adjusted EBITA: NOPAT at the operating tax rate, ROIC with and without goodwill, before and after the lease and capitalised R&D adjustments. Never put the FactSet field and the hand-built figure in one comparison, and flag a ROIC lifted by write-offs that shrink capital. Done when ROIC on reported and on adjusted profit sit side by side.

13. **Flags and severity.** Method step 13: run every flag in table 2, and for each triggered flag give the number, the period, the source and the company's explanation with whether the numbers support it. Then give each flag its own level by what it does, using the wording of table 3: 1 if it is minor and explained; 2 if it changes adjusted EBITA or free cash flow; 3 if it is one of several flags pointing the same way; 4 if it is evidence of misstatement (losses charged to equity, reserve-made profit). The company's level is the highest flag level, raised one step when two flags sit at that level (an assumed rule); the scale was designed for these skills and the report says so. Table 3 calls level 4 "evidence of manipulation"; the report writes "evidence of misstatement", which describes the figures rather than intent. At level 4, say the figures cannot be adjusted and should not be relied on, as Graham and Dodd do. Done when every triggered flag has its row and level, and the company level has a one-line reason.

14. **What each flag means for the valuation inputs.** Map every flag at level 2 or above to the input it changes: recurring one-offs, pension credits, smoothing releases and gains change EBITA and NOPAT; capitalised costs, light depreciation, capitalised R&D and leases change invested capital and ROIC; payables stretch and sold receivables change free cash flow; unfunded pensions, leases and sold receivables add debt-like claims to the equity bridge; normalised earning power replaces the latest year as the earnings base for a multiple. Done when each input shows the reported and the adjusted figure and the flag behind the change.

Quote Piotroski and Altman Z from the tearsheet as FactSet reports them, with no zones or cutoffs attached, since the sources give none. Compute no Beneish M-score or other fitted score. For acquirers use organic and pro forma figures; for cross-border listings compare local accounting with foreign peers; for loss-making companies use CFO and cash burn.

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
| Period | Net income | CFO | Average total assets | Accrual ratio | CFO / NI | Peer median |
Basis and sources note under the table.

## EBITA rebuild
| Line | FY-4 ... FY0, LTM | Note | Basis | Source |
From reported operating profit to adjusted EBITA, one row per adjustment.

## One-offs that recur
| Charge type | Years with a charge (n of 5) | Average % of revenue | Treatment | Basis | Source |

## Provisions and reserves
| Provision | Type | Opening | Charge | Utilised | Released | Closing | Effect on EBITA |
Basis and sources note under the table.

## Pensions, leases, stock compensation and sold receivables
| Item | Effect on EBITA | Effect on free cash flow | Effect on debt | Basis | Source |

## Revenue recognition, working capital and capitalisation
| Ratio | FY-4 ... FY0 | Peer median | Cause | Basis | Source |

## Taxes and the equity reconciliation
Tax-implied against reported profit; the rate reconciliation items; cash against book taxes; the
equity residual as a percent of cumulative net income, explained or flagged.

## Governance and disclosure
| Item | Present / absent / not found | Basis | Source |

## Normalised earning power
Reported, adjusted and normalised earnings per share with the window and range; steady-state FCF
(stock compensation left inside net income). ROIC on reported and on adjusted profit, with the
definition line.

## Flags and severity
| Flag | Value | Period | Company's explanation | Level | Basis | Source |
Company severity level n, with the reason and a note that the scale is this method's design.
Piotroski and Altman Z as reported by FactSet.

## What this means for the valuation inputs
| Input | Reported | Adjusted | Flag behind the change | Basis | Source |
Rows: EBITA and NOPAT, invested capital and ROIC, free cash flow, debt-like claims, earnings base.

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. Every assumed input (cost of secured debt, recurrence rule, materiality threshold, R&D life) appears once in an Assumptions line with its basis. For a narrow question, answer it with the method's step for that question, its table and the sources, and keep the footer.

## Checks before sending

1. One accrual definition, formula 1, used for every period and every peer; four annual accrual years plus LTM.
2. Every EBITA adjustment cites the note it came from, and stock compensation stays an expense throughout: never added back, never deducted a second time in steady-state free cash flow.
3. Each special-item type is counted by recurrence, and the two-of-five rule is labelled assumed.
4. Reserve releases are sized in currency and as a percent of EBITA.
5. The tax section covers the rate reconciliation and cash against book tax, not only the statutory-rate test.
6. The equity residual is shown and either explained or flagged.
7. Piotroski and Altman Z are quoted as reported with no zones; no Beneish or other fitted score appears.
8. Every triggered flag has its own level, the company level follows the stated rule, and the scale is labelled as this method's design, not a sourced standard.
9. Each flag at level 2 or above maps to a valuation input with reported and adjusted figures.
10. The FactSet ROIC field and the hand-built ROIC are never in one comparison. No table passes eight columns.
11. The language is diagnostic: no "fraud", "manipulation" or rating word unless a filing or regulator says it, and then with the citation; level 4 reads "evidence of misstatement".

## Hand-offs

- The user wants one quarter's results against consensus: `bigdata-earnings-review`.
- The flags point at the balance sheet or refinancing: `bigdata-credit`. The user wants the downside more broadly: `bigdata-risk`.
- The user wants the adjusted figures carried into a value range: `bigdata-valuation`.
- After delivering, make one offer: a monitor on the company's filings and news for auditor changes, restatements and reserve releases, or save the report to the user's Bigdata.com account. Act only on a clear yes.
