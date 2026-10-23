# Earnings quality and accounting red flags

This method decides how much of a company's reported profit is backed by cash, how much will recur and whether it is fairly stated, and from that what earning power a valuation should use. It rebuilds operating profit from the notes, tests profit against cash flow and against the change in equity, counts "one-time" items that keep coming back, and normalises earnings over a cycle as Graham and Dodd describe. It computes no Beneish M-score or other fitted manipulation score, since none is in the sources. The tearsheet's Piotroski and Altman Z fields are quoted as reported, with no zones attached.

## When a skill loads it

bigdata-earnings-quality runs the whole method. bigdata-earnings-review runs steps 2, 3, 5 and 7 on the quarter against the same quarter a year earlier and checks whether reserve releases, gains or accruals carried a beat. bigdata-deep-dive and bigdata-thesis report the flags table, the rebuilt EBITA and the normalised earning power. bigdata-risk uses the flags and severity. A narrow question ("is cash conversion healthy?") gets only the test it asks about: step 2 and the working-capital lines of step 7.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Five fiscal periods of statements: revenue, operating income, net income, receivables, inventory, payables, deferred revenue, gross and net PP&E, depreciation, goodwill and intangibles, total assets, equity, cash from operations (CFO), capex, dividends, buybacks, issuance, stock-based compensation (SBC), leases | `bigdata_company_tearsheet`, section `fundamentals` | reported |
| Altman Z, Piotroski | `fundamentals` ratios | reported |
| Special items, provisions roll-forward, pension, lease and tax notes, OCI, revenue policy, non-GAAP reconciliation, auditor changes, restatements, related parties | `bigdata_search` over filings and releases, then `bigdata_fetch_document` for the note | reported |
| Peer medians | Tearsheets of three to six peers | derived |
| Cost of secured debt, recurrence rule, severity level | Chosen and stated | assumed, judgment |

The tearsheet returns five periods per call; fetch older annual reports when the task needs the five to ten years Graham and Dodd ask for, or state the shorter window in the Gaps line.

## Procedure

1. **Set the window.** Five fiscal periods, more where the tool or older filings allow, plus the last twelve months (LTM). Done when the window and LTM figures are stated.
2. **Accrual ratio and cash conversion.** Compute formula 1 and CFO / net income for each year, with the peer median. Done when values, sign, trend and peer median are in one row.
3. **Rebuild EBITA.** Start at reported operating profit. Add back amortisation of acquired intangibles only. Remove impairments, write-offs, restructuring, litigation, asset-sale gains, acquired in-process R&D and pension gains, including any buried in cost of sales or SG&A. Pair each gain with losses booked the same year or charged to equity (Manhattan Electrical Supply, Security Analysis p. 415). Keep SBC as an expense. Done when each adjustment cites its note and reported operating profit sits beside adjusted EBITA.
4. **Count recurring one-offs.** For each special-item type, count the years with a charge and the average charge as a percent of revenue. Treat a type that appears in two or more of five years as a recurring operating cost (assumed rule). Done when each type has both numbers.
5. **Provisions.** Classify each provision by table 1 and tabulate opening balance, charge, utilisation, release and closing balance. Done when the contribution of releases to EBITA, and to any beat, is stated in currency and as a percent of EBITA.
6. **Pensions, leases, SBC, sold receivables.** Pensions: keep only service cost and prior-service amortisation in operating cost; move interest cost, expected return and amortised losses below EBITA; record the expected-return assumption; treat the after-tax unfunded liability as debt. Leases: where rent is still an operating cost, capitalise it with formula 3; where the liability is on the balance sheet, use it; verify the standard for each period. SBC: never add it back; subtract it from CFO in any free cash flow; show buybacks net of issuance; count future grants as cost and outstanding options as a claim, not both (McKinsey ch. 12). Securitised or factored receivables: add back with matching debt and treat the fee as interest (McKinsey ch. 27, p. 586). Done when each item shows its effect on EBITA, free cash flow and debt.
7. **Revenue recognition and working capital.** Compute receivables growth minus revenue growth, DSO, inventory growth minus sales growth, DIO, DPO and working capital excluding inventory. For subscription businesses compare deferred revenue growth with revenue growth; for long-term contracts compare contract assets with revenue. Read the revenue policy note for changes. Rising DPO lifts CFO for a time and reverses later. Done when each ratio has a trend and a cause from MD&A or the call, or is marked unexplained.
8. **Capitalisation and depreciation.** Compute PP&E growth minus revenue growth, depreciation / average gross PP&E, asset life (gross PP&E / depreciation; a longer life lowers the charge), goodwill and intangibles / equity, and capitalised development with its amortisation life. Compare with own history and peers and flag only wide gaps (Security Analysis p. 663). Done when each has a trend and a peer comparison.
9. **Taxes.** Compare tax-implied profit (formula 6) with reported pretax profit, and cash taxes with the book charge. Done when the gap is stated and, if wide, explained from the tax note.
10. **Earnings-to-equity reconciliation.** Compute formula 5 over the window. Done when the residual is explained from the equity statement or flagged.
11. **Governance and disclosure.** Search for auditor resignation or dismissal, restatements, material weaknesses, late filings, related-party dealings, and KPIs, segments or interim data dropped when results weakened (Security Analysis p. 90; McKinsey ch. 24, p. 536). Done when each is marked present, absent or not found.
12. **Normalise earning power.** Over five to ten years spanning a cycle, remove nonrecurring items from the current-year view but keep them in the multi-year average (Security Analysis p. 414). Test whether results cluster around the average (S.H. Kress, 2.80 to 5.92 around 4.36) or are unrelated figures whose average is accidental (Hudson Motors, -3.54 to +13.39 around 4.75) (p. 472-473). Prefer the average to the trend and explain any trend by cause. Where the history is unreliable, build normal volume x unit margin less depreciation, interest and preferred dividends (p. 475). Value contractual or investment income at its own multiple (p. 526-531). Done when reported, adjusted and normalised earnings, the window and the range are shown.
13. **Flags and severity.** Run table 2 and assign a level from table 3. Done when each triggered flag has a number, period and source, and the level has a one-line reason.

## Formulas

1. Accrual ratio_t = (NI_t - CFO_t) / ((TA_t + TA_t-1) / 2), with NI net income and CFO as reported and TA total assets. Positive means profit above cash. This is the only accrual definition used. The cash-flow form is chosen because the tearsheet carries the cash flow statement, because it is Lowenstein's income-versus-cash test (Security Analysis p. 56), and because balance-sheet changes are distorted by acquisitions, disposals and currency (McKinsey ch. 7).
2. Adjusted EBITA = EBIT + acquired-intangible amortisation + nonoperating and non-recurring charges - such gains + (reported pension cost - service cost - prior-service amortisation) + lease interest + net change in income-smoothing provisions (a build is added back, a release subtracted).
3. Lease asset_t-1 = Rent_t / (kd + 1 / Life), with kd the cost of secured debt (assumed) and Life = PP&E / annual depreciation. Lease interest = kd x Lease asset_t-1, added to EBITA; the asset goes into invested capital and debt, and ROIC usually falls (McKinsey ch. 27, p. 583).
4. Capitalised R&D asset_t = asset_t-1 + R&D_t - amortisation_t; adjusted EBITA uses amortisation in place of R&D expense (McKinsey ch. 28, p. 597).
5. Residual = (Equity_end - Equity_start) - (sum NI + sum OCI - sum dividends + sum issuance including the SBC credit - sum buybacks). It rests on cash flow to equity = NI - increase in book equity + OCI = dividends + buybacks - issuance (McKinsey ch. 36). Charges made straight to equity outside OCI show up here.
6. Tax-implied profit = income tax expense / statutory rate (Security Analysis p. 437).
7. DSO = 365 x receivables / revenue; DIO = 365 x inventory / COGS; DPO = 365 x payables / COGS.
8. Steady-state free cash flow = net income + D&A - maintenance capex - SBC, with pension assumptions corrected and expensed growth spending added back (Berkowitz, Security Analysis p. 341-342). Depreciation is the usual maintenance-capex proxy (Mauboussin, Capital Allocation, 2015, p. 25).
9. LTM = prior fiscal year + current year-to-date - prior year-to-date (Security Analysis p. 656).

## Reference tables

**Table 1. Provision types** (McKinsey, Valuation, 5th ed., ex. 26.4, p. 568)

| Type | Example | EBITA | Reserve treated as |
|---|---|---|---|
| Ongoing operating | Returns, warranties | Stays in | Operating |
| Long-term operating | Decommissioning | Operating part in, interest part out | Debt |
| Nonoperating | Restructuring | Out | Debt |
| Income-smoothing | "Other provisions" | Movement reversed | Equity |

**Table 2. Flags**

| Flag | Trigger | Source |
|---|---|---|
| Profit above cash | Accrual ratio positive and rising against history and peers; high-accrual earnings increases are followed by poor relative returns | Lowenstein p. 56; McKinsey ch. 16 (Chan et al.) |
| Receivables build | Receivables or DSO rising faster than revenue | Lowenstein p. 56 |
| Inventory build | Inventory faster than sales, funded by debt; working capital ex inventory falling | Security Analysis p. 604-607 |
| Payables stretch | DPO rising while CFO runs above NI | Earlier Bigdata.com screen |
| Receivables sold | Factoring or securitisation present and growing | McKinsey ch. 27, p. 586 |
| Capitalised cost | PP&E faster than revenue (WorldCom 2000: +27% vs +8%) | Greenwald, Security Analysis p. 545-547 |
| Light depreciation | Depreciation rate or asset life well off history or peers | Security Analysis p. 460, 663 |
| Recurring special items | Two or more of five years (assumed); Kodak 2001-2008 averaged 4.0% of revenue | McKinsey ch. 26, p. 566-567 |
| Gains in operating profit | Asset, securities or debt gains in operating lines, unpaired with losses | Security Analysis p. 413-415 |
| Smoothing provisions | Build in good years, release in weak ones | McKinsey ex. 26.5 |
| Write-off then clean slate | Post-write-down margin used as run rate; write-down that cuts future depreciation | Security Analysis p. 424-425, 455; Klarman ch. 8 |
| Pension credit | Credit lifting EBITA (DuPont 2007: adjustment cut EBITA $455m) | McKinsey ch. 27 |
| Tax gap | "Very wide" gap between tax-implied and reported profit | Security Analysis p. 437 |
| Equity bypass | Residual negative (U.S. Industrial Alcohol 1929-38: $8.85m charged to surplus) | Security Analysis p. 599 |
| Goodwill load | Goodwill and intangibles / equity high against peers; WorldCom above 85% | Greenwald p. 545 |
| EPS against revenue | EPS growth far above revenue growth | McKinsey addendum to ch. 1-2 |
| Non-GAAP drift | Same "non-recurring" item three years running; categories changing | McKinsey ch. 26; earlier screen |
| Disclosure dropped | KPIs, segments or interim data stopped | Security Analysis p. 90; McKinsey ch. 24 |
| Governance events | Auditor change, restatement, material weakness, related-party dealings | Merkin, Security Analysis p. 274 (Adelphia); earlier screen |

**Table 3. Severity** (designed for these skills, not from the sources)

| Level | Meaning | What the report does |
|---|---|---|
| 0 | No flags | States the tests run |
| 1 | One or two minor flags, explained | Notes them, no adjustment |
| 2 | Flags that change adjusted EBITA or free cash flow | Shows reported and adjusted side by side |
| 3 | Several flags in one direction | Cuts earning power, names figures not to rely on |
| 4 | Evidence of manipulation: losses charged to equity, reserve-made profit | Says the figures cannot be adjusted; Graham and Dodd reject rather than adjust (p. 441) |

Take the highest level triggered; two flags at one level raise it one step (assumed rule). All case figures above are dated illustrations; use the logic and verify any figure before quoting it.

## Interpretation rules

- A flag is a question for the notes, not a verdict; state the company's explanation and whether the numbers support it.
- Do not adjust for a dishonest management; say the figures cannot be used (Security Analysis p. 441).
- A "one-time" charge that recurs is an operating cost and goes in the forecast (McKinsey ch. 26). A write-down is not a clean slate (Klarman ch. 8).
- Average beats trend; a trend is an assumption until its cause is shown (Security Analysis p. 477-480). A deficit has qualitative meaning only (p. 480-481).
- Earnings volatility alone is not priced; cash-flow volatility is (McKinsey ch. 16). Do not mark down lumpy but cash-backed earnings.
- Banks and insurers: the accrual, EBITA and working-capital tests do not apply; use the equity reconciliation, reserve adequacy and loan-loss provisioning (McKinsey ch. 36).
- Cyclicals: normalise on mid-cycle margins (McKinsey ch. 35). Loss-making companies: use CFO and cash burn. Cross-border: compare local accounting with foreign peers and widen the margin for disclosure gaps (Russo, Security Analysis p. 711-724). Acquirers: use organic and pro forma figures (McKinsey ch. 8).

## Output lines

- "Accrual ratio FY-4 to FY0: a, b, c, d, e percent of average assets; peer median m; CFO / net income x." [derived]
- "Reported operating profit X; adjusted EBITA Y." [derived]; each adjustment [reported, with its note]
- "Charge type T in n of 5 years, average r percent of revenue; treated as recurring." [derived; rule assumed]
- "Reserve releases added Z to EBITA, p percent of EBITA." [derived]
- "Cumulative net income X, OCI Y, net distributions W; unexplained change in equity Z." [derived]
- "Normalised earning power E per share over N years, range lo to hi; the latest year sits near the top, middle or bottom." [derived; window assumed]
- "Altman Z a, Piotroski b, as reported by FactSet." [reported]
- "Severity level n because ..." [judgment]
- A flags table with columns Flag, Value, Period, Basis, Source.

## Not in the sources

- Not in the sources: a numeric cutoff for the accrual ratio or CFO / net income; read sign, trend and peer median.
- Not in the sources: a threshold for the equity residual; report it as a percent of cumulative net income.
- Not in the sources: a threshold for a pension credit or the expected-return assumption.
- Not in the sources: a materiality threshold for adjustments; state the one used.
- Not in the sources: a percentage-of-completion test beyond the contract-asset comparison.
- Not in the sources: Altman Z or Piotroski cutoffs; quote the fields without zones.
- Not in the sources: the two-of-five recurrence rule and the severity scale; both are labelled assumed.
- Not in the sources: bands for SBC / revenue, CFO / net income or non-GAAP adjustment size.

## Sources

- Notes: security-analysis.md; mckinsey-part1.md (ch. 7, 8, 12, 16, addendum to ch. 1-2); mckinsey-part2.md (ch. 24-28, 35, 36); capital-allocation.md; klarman.md (ch. 8).
- Graham and Dodd, Security Analysis, 6th ed. (2009): p. 56, 90, 341-342, 409-486, 526-531, 545-547, 591-610, 656-663, 711-724.
- McKinsey (Koller, Goedhart, Wessels), Valuation, 5th ed. (2010): ch. 7, 12, 16, 24, 26, 27, 28, 35, 36.
- Mauboussin and Callahan, Capital Allocation, Credit Suisse, 2 Jun 2015, p. 25-27. Klarman, Margin of Safety (1991), ch. 8.

<!-- Spec and notes agree; from the earlier screen the payables, factoring, non-GAAP and governance flags were kept and labelled, and its ratio bands, balance-sheet accrual formula, Beneish M-score and Altman cutoffs were dropped as not in the sources. -->
