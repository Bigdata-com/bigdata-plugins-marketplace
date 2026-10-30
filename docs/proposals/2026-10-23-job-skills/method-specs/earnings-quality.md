# Earnings quality and accounting red flags

Purpose: decide how much reported profit is cash-backed, recurring and fairly stated, and what earning power a valuation should use. Used by the earnings, valuation and memo jobs. The method rebuilds operating profit, tests profit against cash and equity, and normalises earnings over a cycle. It does not compute Beneish M-score or Piotroski score. The tearsheet's Piotroski and Altman Z fields are quoted as reported only.

## 1. Inputs

- Tearsheet (FactSet, 5 fiscal periods): income statement, receivables, inventory, deferred revenue where reported, gross and net PP&E, goodwill and intangibles, total assets, equity, cash from operations (CFO), dividends, buybacks, stock-based compensation (SBC), leases where reported, Altman Z, Piotroski.
- Filing search (footnotes, MD&A): special items, provisions, pension note, lease note, tax reconciliation, other comprehensive income (OCI), revenue policy, restatements. Graham and Dodd want 5 to 10 years; the tearsheet gives 5, so fetch older filings or state the shorter window.

## 2. Procedure

1. Accrual ratio. Compute it (section 3) for five years with CFO/net income. Done when values, sign and peer median show.
2. EBITA rebuild. Start at reported operating profit. Add back amortisation of acquired intangibles only. Remove nonoperating and non-recurring items: impairments, write-offs, restructuring, litigation, asset-sale gains, acquired in-process R&D, pension gains. Search notes for items inside cost of sales and SG&A. Pair each gain with losses booked the same year or charged to equity. Keep SBC as an expense. Done when each adjustment cites its note.
3. Recurring one-offs. For each special-item type count the years with a charge in the last five and the average charge as a percent of revenue. Treat it as a recurring operating cost if it appears in 2 or more years (assumed rule). Done when each type has both numbers.
4. Provisions. Classify each into the four types in section 4 and tabulate opening balance, charge, utilisation, release, closing balance. Flag build in strong years and release in weak years. Done when releases' contribution to EBITA is stated.
5. Pensions, leases, SBC. Pensions: replace net periodic pension cost in operating costs with service cost plus prior-service amortisation; interest cost, expected return and amortised losses go below EBITA; record the expected-return assumption; treat the after-tax unfunded liability as debt. Leases: capitalise (section 3) unless the filing is under IFRS 16 or ASC 842, then use the disclosed liability (verify standard). SBC: never add it back; subtract it from CFO in any free cash flow figure and show buybacks net of shares issued.
6. Revenue recognition. Compute receivables growth minus revenue growth and DSO = 365 x receivables / revenue. For subscription or contract businesses compare deferred revenue growth with revenue growth. For long-term contracts compare unbilled receivables or contract assets with revenue and check whether profit is booked before cash. Read the policy note for rule changes. Done when each ratio has a five-year trend and a cause from MD&A or the call.
7. Inventory and capitalisation. Compute inventory growth minus sales growth, working capital excluding inventory, PP&E growth minus revenue growth, depreciation / average gross PP&E, asset life = gross PP&E / depreciation (a rising life lowers expense), goodwill and intangibles as a percent of equity, and capitalised development cost with its amortisation life. Compare with own history and peers. Done when each has a trend.
8. Earnings-to-equity reconciliation (section 3). Done when the five-year residual is explained line by line or flagged.
9. Normalise earning power (Graham and Dodd). Use 5 to 10 years spanning a cycle. Remove nonrecurring items from the current-year view but keep them in the multi-year average. Test whether results cluster around the average (Kress, 2.80 to 5.92 around 4.36) or are unrelated figures (Hudson, -3.54 to +13.39 around 4.75; that average is accidental). Prefer the average to the trend and explain any trend by cause. A deficit has qualitative meaning only. Where history is unreliable build normal volume x unit margin less depreciation, interest and preferred. LTM = prior fiscal year + current YTD - prior YTD. Value each earnings stream at its own multiple. Done when reported, adjusted and normalised earnings, window and range are shown.
10. Flags and severity. Run section 4. Done when each triggered flag has a number and a source.

## 3. Formulas

- Accrual ratio_t = (NI_t - CFO_t) / ((TA_t + TA_t-1) / 2); NI and CFO as reported, TA total assets. One definition throughout. The cash-flow form is used because the tearsheet carries the cash flow statement, it matches Lowenstein's income-versus-cash test, and the balance-sheet form is distorted by acquisitions, disposals and currency (McKinsey ch. 7). Positive means profit above cash. GAP: no source gives a numeric cutoff; use sign, five-year trend and peer median.
- Adjusted EBITA = EBIT + acquired-intangible amortisation + nonoperating and non-recurring charges - such gains + (reported pension cost - service cost - prior-service amortisation) + lease interest + smoothing-provision movements.
- Lease asset_t-1 = Rent_t / (kd + 1 / Life); kd secured cost of debt; Life = PP&E / depreciation. Lease interest = kd x Lease asset_t-1, added to EBITA; the asset is added to invested capital and debt; ROIC falls.
- Capitalised R&D asset_t = asset_t-1 + R&D_t - amortisation_t; EBITA uses amortisation in place of R&D expense.
- Residual = (Equity_end - Equity_start) - (sum NI + sum OCI - sum dividends + sum share issuance including SBC credit - sum buybacks). Basis: CFE = NI - increase in book equity + OCI = dividends + buybacks - issuance (McKinsey ch. 36). Dirty surplus items sit in OCI or are charged directly to equity. GAP: no threshold; report as a percent of cumulative NI.
- Implied taxable profit = tax expense / statutory rate; compare with pretax profit (Graham p. 437).

## 4. Reference tables

Provision types (McKinsey ch. 26, p. 568): (1) ongoing operating (warranty): stays in EBITA. (2) Long-term operating (decommissioning): operating part in EBITA, interest part nonoperating, reserve is debt. (3) Restructuring: nonoperating, reserve is debt. (4) Income-smoothing "other provisions": undo in EBITA, reserve is equity.

| Flag | Test | Sign or threshold | Source |
|---|---|---|---|
| Profit above cash | Accrual ratio, CFO/NI | Positive and rising; GAP numeric | Lowenstein p. 56 |
| Receivables build | Receivables vs revenue growth | Receivables faster | Lowenstein p. 56 |
| Inventory build | Inventory vs sales growth | Faster, debt-funded | Graham p. 604-607 |
| Capitalised cost | PP&E vs revenue growth | Faster (WorldCom +27% vs +8%) | Greenwald p. 545-547 |
| Light depreciation | Depreciation / gross PP&E, life | Below own history or peers; wide gaps only | Graham p. 460, 663 |
| Recurring special items | Years with charge, of 5 | 2 or more (assumed); Kodak 4.0% of revenue | McKinsey ch. 26 |
| Gains in operating profit | Asset, securities, debt gains | Any, unpaired with losses | Graham p. 413-415 |
| Smoothing provisions | Other-provision movement | Build then release | McKinsey ex. 26.5 |
| Pension credit | Net periodic cost | Credit lifting EBITA; GAP threshold | McKinsey ch. 27 |
| Tax gap | Implied vs reported profit | "Very wide" | Graham p. 437 |
| Equity bypass | Residual | Negative | Graham p. 599 |
| Goodwill load | Goodwill / equity | Peers; WorldCom above 85% | Greenwald p. 545 |
| Disclosure | Dropped KPIs or interim data | Present | Graham p. 90 |
| EPS vs revenue | EPS growth far above revenue | Gap | McKinsey ch. 1 addendum |

Severity scale (skill design, not from the sources): Level 0 no flags. Level 1 one or two minor, explained flags; no adjustment. Level 2 flags that change adjusted EBITA or free cash flow; show reported and adjusted. Level 3 several flags in one direction; cut earning power and name the unusable figures. Level 4 evidence of manipulation (losses charged to equity, reserve-manufactured profit); Graham and Dodd say reject, not adjust (p. 441). Take the highest level triggered; two flags at one level raise it one step (assumed).

Dated (verify): Graham's 20x average earnings ceiling and 12-12.5x neutral multiple are 1940 figures; use the logic only. ASC 606, IFRS 15, IFRS 16 and ASC 842 postdate McKinsey. GAP: no materiality threshold for adjustments, no percentage-of-completion test, no Altman or Piotroski cutoffs; label any rule used as assumed.

## 5. Interpretation rules

- Do not adjust for a dishonest management; reject (Graham p. 441).
- Banks and insurers: accrual, EBITA and working capital tests do not apply; use equity reconciliation and reserve adequacy. Cyclicals: use mid-cycle (McKinsey ch. 35). Early-stage: use CFO. Emerging markets: compare local accounting with peers and widen the margin for disclosure gaps (Russo). Acquirers: use organic figures.

## 6. Output lines

- "Accrual ratio FY-4 to FY0: a, b, c, d, e; peer median m; CFO/NI x" [derived from reported].
- "Reported EBIT X; adjusted EBITA Y" [derived]; each adjustment [reported].
- "Charge type T in n of 5 years, average r% of revenue; treated as recurring" [derived; rule assumed].
- "Cumulative NI X, OCI Y, unexplained equity change Z" [derived].
- "Normalised earning power E per share, N-year window, range lo to hi" [derived; window assumed].
- "Altman Z a, Piotroski b, as reported" [reported].
- "Severity level n because ..." [judgment].

## 7. Sources

Notes: security-analysis.md, mckinsey-part1.md (ch. 7, 8, 16), mckinsey-part2.md (ch. 26-28, 35, 36), capital-allocation.md (asset life). Underlying: Graham and Dodd, Security Analysis 6th ed. (2009); McKinsey, Valuation 5th ed. (2010).
