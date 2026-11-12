# Earnings quality and accounting red flags

How much of reported profit is backed by cash, how much will recur, whether it is fairly stated, and so what earning power a valuation should use. Compute no fitted manipulation score. Quote the tearsheet's Piotroski and Altman Z as reported, with no zones attached.

## Inputs

| Input | Where it comes from |
|---|---|
| Revenue, operating income, net income, receivables, inventory, payables, deferred revenue, gross and net PP&E, depreciation, goodwill and intangibles, total assets, equity, CFO, capex, dividends, buybacks, issuance, stock compensation, leases | Annual statements, five fiscal years |
| Altman Z, Piotroski | Financial ratios |
| Special items, provisions roll-forward, pension, lease and tax notes, OCI, revenue policy, non-GAAP reconciliation, auditor changes, restatements, related parties | A search over filings and releases, then the full document for the note |
| Peer medians | Tearsheets of three to six peers |
| Cost of secured debt, materiality threshold | Not in the data. State each once |

## Window

Five fiscal periods, more where older filings allow, plus the last twelve months. When fewer than five years are available, say so.

LTM = prior fiscal year + current year-to-date - prior year-to-date.

## Accrual ratio and cash conversion

Accrual ratio(t) = (NI(t) - CFO(t)) / ((TA(t) + TA(t-1)) / 2), with NI net income, CFO cash from operations as reported and TA total assets. Positive means profit above cash. Use this cash-flow form only: balance-sheet accruals are distorted by acquisitions, disposals and currency.

Compute it and CFO / net income for each year beside the peer median. Neither has a cutoff; read sign, trend and the peer median. High-accrual earnings increases are followed by poor relative returns.

## Rebuilding EBITA

Start at reported operating profit and add back amortisation of acquired intangibles only. Remove impairments, write-offs, restructuring, litigation, asset-sale gains, acquired in-process R&D and pension gains, including any buried in cost of sales or SG&A. Pair each gain with losses booked the same year or charged to equity. Keep stock compensation as an expense.

Adjusted EBITA = EBIT + acquired-intangible amortisation + nonoperating and nonrecurring charges - such gains + (reported pension cost - service cost - prior-service amortisation) + lease interest + net change in income-smoothing provisions (a build is added back, a release subtracted).

State the materiality threshold used for adjustments.

## Recurring one-offs

For each special-item type, count the years with a charge and the average charge as a percent of revenue. A type that appears in two or more of five years is a recurring operating cost and goes in the forecast.

## Provisions

Classify each provision and tabulate opening balance, charge, utilisation, release and closing balance.

**Provision types**

| Type | Example | EBITA | Reserve treated as |
|---|---|---|---|
| Ongoing operating | Returns, warranties | Stays in | Operating |
| Long-term operating | Decommissioning | Operating part in, interest part out | Debt |
| Nonoperating | Restructuring | Out | Debt |
| Income-smoothing | "Other provisions" | Movement reversed | Equity |

## Pensions, leases, R&D, stock compensation, sold receivables

- **Pensions.** Keep only service cost and prior-service amortisation in operating cost; move interest cost, expected return and amortised losses below EBITA. Record the expected-return assumption and the size of any credit against EBITA. Treat the after-tax unfunded liability as debt.
- **Leases.** Where the liability is on the balance sheet, use it. Where rent is still an operating cost, capitalise it: lease asset(t-1) = rent(t) / (kd + 1 / life), with kd the cost of secured debt and life = PP&E / annual depreciation. Lease interest = kd x lease asset(t-1), added to EBITA; the asset goes into invested capital and debt, and ROIC usually falls. Check which lease standard applies in each period.
- **R&D.** Capitalised R&D asset(t) = asset(t-1) + R&D(t) - amortisation(t); adjusted EBITA uses the amortisation in place of R&D expense.
- **Stock compensation.** Never add it back; subtract it from CFO in any free cash flow; show buybacks net of issuance. Count future grants as a cost and outstanding options as a claim, not both. Compare stock compensation / revenue with history and peers.
- **Securitised or factored receivables.** Add them back with matching debt and treat the fee as interest.

## Revenue recognition and working capital

- DSO = 365 x receivables / revenue; DIO = 365 x inventory / COGS; DPO = 365 x payables / COGS.
- Compute receivables growth minus revenue growth, inventory growth minus sales growth, and working capital excluding inventory.
- Subscription businesses: deferred revenue growth against revenue growth. Long-term contracts: contract assets against revenue; this is the test for percentage-of-completion accounting.
- Read the revenue policy note for changes. Rising DPO lifts CFO for a time and reverses later.

## Capitalisation and depreciation

Compute PP&E growth minus revenue growth, depreciation / average gross PP&E, asset life (gross PP&E / depreciation; a longer life lowers the charge), goodwill and intangibles / equity, and capitalised development with its amortisation life. Flag only wide gaps against history and peers.

## Taxes

Tax-implied profit = income tax expense / statutory rate. Compare it with reported pretax profit, and cash taxes with the book charge.

## Earnings-to-equity reconciliation

Residual = (equity at end - equity at start) - (sum of NI + sum of OCI - sum of dividends + sum of issuance including the stock-compensation credit - sum of buybacks), over the window.

It rests on cash flow to equity = NI - increase in book equity + OCI = dividends + buybacks - issuance. Charges made straight to equity outside OCI show up here. Report the residual as a percent of cumulative net income.

## Steady-state free cash flow

Steady-state FCF = net income + D&A - maintenance capex, with pension assumptions corrected and expensed growth spending added back. Depreciation is the usual proxy for maintenance capex. Stock compensation is already an expense inside net income under ASC 718 and IFRS 2, so it is neither added back nor deducted a second time; remove any add-back in the company's adjusted figures.

## Governance and disclosure

Search for auditor resignation or dismissal, restatements, material weaknesses, late filings, related-party dealings, and KPIs, segments or interim data dropped when results weakened. Compare the size of non-GAAP adjustments with history and peers.

## Normalised earning power

Over five years spanning a cycle, remove nonrecurring items from the current-year view but keep them in the multi-year average. Test whether results cluster around the average or are unrelated figures whose average is accidental. Prefer the average to the trend; a trend is an assumption until its cause is shown, and a deficit year has qualitative meaning only. Where the history is unreliable, build normal volume x unit margin less depreciation, interest and preferred dividends. Value contractual or investment income at its own multiple.

## Red flags

| Flag | Trigger |
|---|---|
| Profit above cash | Accrual ratio positive and rising against history and peers |
| Receivables build | Receivables or DSO rising faster than revenue |
| Inventory build | Inventory faster than sales, funded by debt; working capital excluding inventory falling |
| Payables stretch | DPO rising while CFO runs above NI |
| Receivables sold | Factoring or securitisation present and growing |
| Capitalised cost | PP&E faster than revenue (one large fraud showed PP&E up 27 percent on revenue up 8) |
| Light depreciation | Depreciation rate or asset life well off history or peers |
| Recurring special items | The same type in two or more of five years |
| Gains in operating profit | Asset, securities or debt gains in operating lines, unpaired with losses |
| Smoothing provisions | Build in good years, release in weak ones |
| Write-off then clean slate | Post-write-down margin used as the run rate; a write-down that cuts future depreciation |
| Pension credit | A credit lifting EBITA |
| Tax gap | A very wide gap between tax-implied and reported profit |
| Equity bypass | Residual negative |
| Goodwill load | Goodwill and intangibles / equity high against peers (the same fraud carried above 85 percent) |
| EPS against revenue | EPS growth far above revenue growth |
| Non-GAAP drift | The same "nonrecurring" item three years running; categories changing |
| Disclosure dropped | KPIs, segments or interim data stopped |
| Governance events | Auditor change, restatement, material weakness, related-party dealings |

## Severity

| Level | Meaning | What the report does |
|---|---|---|
| 0 | No flags | States the tests run |
| 1 | One or two minor flags, explained | Notes them, no adjustment |
| 2 | Flags that change adjusted EBITA or free cash flow | Shows reported and adjusted side by side |
| 3 | Several flags in one direction | Cuts earning power, names figures not to rely on |
| 4 | Evidence of misstatement: losses charged to equity, reserve-made profit | Says the figures cannot be adjusted or relied on |

Take the highest level triggered; two flags at one level raise it one step.

## Interpretation and limits

- A flag is a question for the notes, not a verdict. State the company's explanation and whether the numbers support it.
- When management is dishonest, do not adjust; say the figures cannot be used.
- A write-down is not a clean slate.
- Earnings volatility alone is not priced; cash-flow volatility is. Do not mark down lumpy but cash-backed earnings.
- Banks and insurers: the accrual, EBITA and working-capital tests do not apply; use the equity reconciliation, reserve adequacy and loan-loss provisioning.
- Cyclicals: normalise on mid-cycle margins.
- Loss-making companies: use CFO and cash burn.
- Cross-border listings: compare local accounting with foreign peers and widen the margin for disclosure gaps.
- Acquirers: use organic and pro forma figures.
