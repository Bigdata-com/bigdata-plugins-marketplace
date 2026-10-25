# Credit analysis for an equity or a credit view

This method answers three questions: can the company meet its obligations through a downturn and a refinancing, what does each layer of the capital structure recover if it cannot, and do the equity and debt prices tell the same story? Credit risk is leverage times the instability of cash flow (Marks, Security Analysis p. 132), so the method judges the stability of the business before it computes any ratio. Gains on a bond are capped at the promised yield while losses can be total, so the work is to find what can go wrong (p. 131). The method states the balance of evidence and what would change it; it gives no rating of its own and no call on the securities.

## When a skill loads this file

bigdata-credit runs the whole method; bigdata-risk runs steps 2 to 8 and the distress signals; bigdata-deal-analysis runs steps 3 to 6 on the pro forma balance sheet and step 9 when a party is stressed. A narrow question ("can the company refinance its notes due next year?") gets step 6 and the coverage line.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Short- and long-term debt, notes payable, leases where reported, cash, current assets and liabilities, inventory, receivables, goodwill, PP&E, equity | `bigdata_company_tearsheet`, `financial_statements`, `interval` annual, five fiscal years | reported |
| EBIT, EBITDA, interest expense, CFO, capex, depreciation, FCF, dividends, buybacks | `financial_statements` | reported |
| Net debt, EV, market cap; Altman Z and Piotroski as FactSet computes them | `key_metrics` and `financial_ratios` | reported |
| Forward EBIT and EBITDA | `analyst_estimates`, to FY+4 | reported |
| Rent expense, maturity schedule, credit agreement and covenants, rating actions, pension deficit, contingent liabilities, deconsolidated entities, related-party loans | `bigdata_search` over filings and news, then `bigdata_fetch_document` | reported |
| Credit news signals | `bigdata_get_credit_factor`: the strongest positive and negative credit-news catalysts for the company (event type, score, direction) over a daily, weekly or monthly horizon; `bigdata_screen_credit_factor` ranks many companies the same way. Neither returns prices, yields, spreads or ratios | reported |
| Bond prices, yields, spreads, rating-agency commentary, fixed-floating split, hedges | Not in a Bigdata.com data set. Quoted figures from news, research and the filing's debt note via `bigdata_search` and `bigdata_fetch_document`; otherwise state the gap | reported or not available |
| Cost of debt, size of the stress shock, scenario enterprise values | Chosen and stated | assumed |

## Procedure

1. **Fix the claim.** Name the security (senior secured, senior unsecured, subordinated, preferred, common) and the legal entity that owes it. Holding-company debt can default while operating subsidiaries carry on, and debt at the operating subsidiary causes more disruption (Klarman, Margin of Safety, ch. 12). From the filing's debt and guarantor notes, record which subsidiaries guarantee the claim, what share of EBITDA and assets sits outside the guarantor group, the collateral, and any covenant baskets that let assets or collateral move away from existing lenders (drop-down and non-pro-rata uptier transactions; not in the sources, standard practice since 2016). Done when the obligor, the claim's rank, the guarantor coverage and the baskets are named.
2. **Judge the stability of the business.** A stable record is not proof of a stable business: Studebaker preferred with dividend coverage of 26 times was less safe than First National Stores at 6 times, because grocery demand, many locations and fast inventory turns made the grocer's earnings dependable (Security Analysis p. 86-88). Done when the five-year EBITDA range, the sector volatility from table 3 and a judgment on what drives the variability are written.
3. **Compute leverage and coverage** with formulas 1 to 5, all on the same period. Use total interest, never cash interest only. Done when each ratio shows numerator, denominator and period.
4. **Place the company against the rating tables.** Read coverage and debt / capital against table 1 and the McKinsey coverage rule in table 2. Done when the implied rating bucket is stated, labelled derived, next to the actual rating if a source gives it.
5. **Stress the coverage.** Cut EBIT by an assumed shock and recompute (formula 6). Use a shock at least as large as the worst year in the window or the sector volatility in table 3 (assumed rule); McKinsey's example uses 20%. Done when coverage after the shock is shown against the level the claim needs.
6. **Liquidity and the maturity wall.** From the filings, list debt due within 24 months with amounts and dates, short-term bank loans and notes payable, cash, undrawn facilities and covenant terms with current headroom. Financial difficulty is almost always preceded by short-term bank debt, and large debt maturing soon is a frequent cause of insolvency (Security Analysis p. 594-597). Done when each maturity has an amount, a date and a funding source, and the note says whether repayment depends on market access.
7. **Claims outside the debt line.** Leases, unfunded pensions (after tax), contingent liabilities, guarantees, deconsolidated entities, securitised receivables and related-party loans. Run the WorldCom balance-sheet checks: goodwill share of equity, PP&E growth against revenue growth, a shift from short- to long-term debt, deconsolidations (Greenwald, Security Analysis p. 545-547). Done when each item is marked present with an amount, absent, or unknown.
8. **Cash flow.** Compute formula 7 over five periods and compare capex with depreciation. EBITDA is not cash flow; capex below depreciation for long is gradual liquidation (Klarman ch. 4). Done when free cash flow, capex against depreciation, and dividends and buybacks against free cash flow are shown per year.
9. **Recovery view, for stressed cases.** Split assets into the ongoing business and assets available for distribution, list claims by seniority, value the business in at least two scenarios with stated enterprise values, and compute recovery per layer (formula 9). Classify the claim as senior (covered), fulcrum (partly covered, most sensitive to value) or junior (option-like) (Klarman ch. 12). Done when recovery per layer is shown for each scenario.
10. **Compare layers.** Test whether the bond and equity prices imply the same enterprise value (formula 10); one security of a company can be dear while another is cheap (Klarman ch. 12, Bank of New England, Jan 1990). Done when the implied values are shown, or the missing bond prices are named in the Gaps line.

## Formulas

1. Coverage = EBIT / total interest expense. Variants: EBITA / interest, EBITDA / interest, and EBITDAR / (interest + rent) for lessees such as retailers (McKinsey, Valuation, ch. 8, p. 182-184; ch. 23, p. 500). Klarman uses pretax earnings over total interest and calls EBITDA over cash interest "meaningless" (ch. 4); state whether the numerator is before or after interest.
2. Net debt / EBITDA, with net debt = debt + capitalised leases - excess cash, and excess cash = cash above working cash of about 2% of revenue (McKinsey ch. 7, p. 145; find the industry's own minimum where possible). Prefer this ratio when low-coupon convertibles or cheap short-term debt will reprice, because coverage would fall at refinancing (McKinsey p. 500).
3. FCF / total debt (derived).
4. Market-adjusted debt ratio = market value of common stock / funded debt, a leading margin-of-safety test (Marks, Security Analysis p. 138). Debt / tangible assets above 1 is a warning (Klarman ch. 4). Book solvency ratios such as debt / book equity are the least useful measure (McKinsey p. 500).
5. Leverage identity: ROE = ROIC + (D / E) x [ROIC - (1 - T) x kd]. More debt raises ROE and its sensitivity to ROIC, which is risk (McKinsey ch. 8, p. 182-184).
6. Stressed coverage = EBIT x (1 - s) / interest, with s the assumed shock. In McKinsey's example a single-A target needed EBIT / interest of about 9.5 and coverage had to stay at or above 7.5 after a 20% EBIT drop (ch. 23, p. 510-517; illustrative).
6a. Refinancing stress (not in the sources; standard agency practice): re-price every maturity within 24 months, and the floating-rate share of the rest, at the current yield for the rating (a quoted figure from news or research, labelled assumed when none is quoted); recompute interest, coverage and FCF / debt with the new interest bill, alone and combined with the EBIT shock in formula 6. State the fixed-floating split and the hedges from the debt note.
7. Free cash flow = after-tax earnings + depreciation and amortisation - capex (Klarman ch. 4), or CFO - capex - SBC.
8. Current ratio = current assets / current liabilities; quick ratio = (current assets - inventory) / current liabilities.
9. Recovery of layer i in scenario s: R_i = min(1, max(0, (EV_s - claims senior to i) / claim_i)). Equity_s = max(EV_s - total claims, 0); probability-weight across scenarios. With EV of 1,500 or 900 at 50/50 and debt of 1,200, equity is worth 150 (McKinsey ch. 12, p. 282-290). Use face value of debt, not the market value of distressed debt.
10. Enterprise value implied by layer i trading at price q_i (fraction of face), with everything junior worth zero: EV_i = claims senior to i + q_i x claim_i (derived). If the equity has market value while EV_i is below total claims, the two markets disagree.
11. Bond price and holding return diverge: a 5-year 10% bond at par, semiannual coupons, is worth 121.88 if rates fall to 5%, with a hold-to-maturity return of 9.10%; at 15% it is worth 82.84 with a hold-to-maturity return of 10.99% (Klarman ch. 7).

## Reference tables

**Table 1. S&P rating medians** (Mauboussin, Operating Leverage, Credit Suisse, 14 Jun 2016, ex. 14, p. 16; US companies, medians of three-year averages 2011-2013; default rates are median one-year global rates for 2014; verify)

| Rating | AAA | AA | A | BBB | BB | B |
|---|---|---|---|---|---|---|
| Operating income / revenue (%) | 28.0 | 26.9 | 22.7 | 21.3 | 17.9 | 19.2 |
| EBIT / interest (x) | 40.8 | 17.3 | 10.3 | 5.5 | 3.2 | 1.3 |
| Debt / total capital (%) | 2.8 | 17.2 | 30.7 | 41.1 | 50.4 | 72.7 |
| Return on capital (%) | 30.6 | 21.6 | 22.2 | 14.2 | 11.1 | 7.1 |
| One-year median default (%) | 0.00 | 0.00 | 0.00 | 0.12 | 0.71 | 3.46 |
| Companies in sample | 4 | 15 | 94 | 233 | 253 | 266 |

**Table 2. Five-year default probability and coverage rules** (McKinsey, Valuation, 5th ed., ch. 23, ex. 23.4, p. 499; S&P, defaults within five years, 1981-2003; an older cohort, quoted for the order of magnitude: later S&P studies show lower cumulative rates for BB and B; verify against the latest S&P annual default study before quoting)

| Rating | AAA | AA | A | BBB | BB | B | CCC |
|---|---|---|---|---|---|---|---|
| Five-year default (%) | 0.12 | 0.33 | 0.75 | 3.84 | 14.45 | 33.02 | 61.35 |

- EBITA / interest of about 5 to 11 corresponds to A+ to BBB-, where 72% of large US and European companies sat (p. 494-497).
- Coverage alone explains about 45% of rating differences (R-squared 0.45, ex. 23.5, p. 501). Size matters at the extremes: every AAA company had a market cap above $50 billion (p. 500).
- Enterprise value barely changes with coverage except below 2, and too much debt costs far more than too little (ex. 23.3).

**Table 3. Rating-agency cash-flow and leverage ranges** (S&P Global Ratings, Corporate Methodology, 19 Nov 2013, cash flow/leverage assessment, standard-volatility table; not in the resources folder; these are the agency's core ratios since 2013 and the ones a credit analyst quotes; verify against the current criteria)

| Assessment | FFO / debt (%) | Debt / EBITDA (x) |
|---|---|---|
| Minimal | above 60 | below 1.5 |
| Modest | 45 to 60 | 1.5 to 2 |
| Intermediate | 30 to 45 | 2 to 3 |
| Significant | 20 to 30 | 3 to 4 |
| Aggressive | 12 to 20 | 4 to 5 |
| Highly leveraged | below 12 | above 5 |

FFO = EBITDA - cash interest - cash taxes (derived from the statements). Debt is adjusted: reported debt + lease liabilities + unfunded pensions - surplus cash. Place the company on table 3 first, then on table 1 as the cross-check, and say when the two disagree.
- Spreads jump below BBB- because many institutions cannot hold sub-investment-grade debt (p. 502-503).
- Home Depot 2008 EBITA / interest 7.0 times against Lowe's 11.8 times, rated BBB+ and A+ (ch. 8, p. 182-184).

**Table 3. EBITDA volatility, median of the 25 largest companies per sector** (McKinsey ex. 23.6, p. 502; dated): semiconductors 41.2%, computer hardware 29.8%, steel 26.5%, retail 13.5%, chemicals 11.4%, telecom 10.4%. A sector with volatile EBITDA needs higher coverage for the same rating.

**Table 4. Graham and Dodd and Klarman thresholds** (dated; use the logic, verify any number before quoting)

| Test | Figure | Source and caveat |
|---|---|---|
| Current and quick ratio | 2:1 and 1:1 | 1930s industrial norms; Graham and Dodd proposed no better figure and allowed industry exceptions (Security Analysis p. 591-594) |
| Coverage judgment | Earnings about 3 times interest on average over seven years, a level not to fall far below, not a forecast | Security Analysis p. 85 |
| Bond buyer's three conditions | Rising profit trend, good current showing, margin over interest in every year; if one fails, require average coverage well above the minimum | Marks, Security Analysis p. 136 |
| Deterioration in new junk issues | Coverage below 1.0 by 1988; debt above tangible assets | Klarman ch. 4 |
| Unseasoned industrial bonds and preferreds | Speculative unless priced below 70 | Security Analysis p. 688-690 |

## Interpretation rules

- **Distress signals.** Short-term bank loans and notes payable rising; large maturities within 24 months; coverage below 1.0; debt above tangible assets; inventories and receivables building while cash falls (Klarman preface, Security Analysis p. xxviii); dividends held while free cash flow is weak, since stressed companies are almost always late to cut (Berkowitz p. 346); PIK, zero-coupon or interest-reset features, which postpone default and raise ultimate risk; a new yield measure replacing the standard one, such as "yield to reset" (Klarman ch. 4); an equity collapse raising market leverage while cash flow is thin (KPN and France Telecom, 2001; McKinsey p. 500); related-party and off-balance-sheet loans (Adelphia: debt 11 times market cap against 1.28 for Comcast; Merkin p. 274); interim reporting dropped as results weaken (p. 90). Avoid fixed income in a fast-deteriorating business with negative operating cash flow before interest (Klarman ch. 12).
- **Altman Z and Piotroski** are reported flags only. Verify the FactSet definition before reading anything into the level.
- **Safety margin.** A bond well below par offers more upside and less downside than one near par of the same credit (Klarman ch. 4). A high coupon does not pay for substantial risk to principal, and the test is the likelihood of payment, not the label on the security (Marks p. 128-129).
- **Ratings and default statistics can mislead.** Issuer-paid ratings and appraisals misled in the 1920s and in 2007 (Marks p. 140). Default rates look low when issuance is growing fast, when issuers prefunded interest, or when exchange offers impair holders without a default; group defaults by year of issue (Klarman ch. 4).
- **Size and coupon.** The biggest company may be the weakest if its bonded debt is disproportionately large (Marks p. 133). Coverage achieved only through a low coupon is not safety (Security Analysis p. 508-512).
- **Review** a credit view at least quarterly (Marks p. 133).
- **Does not apply** as written to banks and insurers: interest is an operating item and there is no net debt, so use capital ratios and equity measures (McKinsey ch. 36). Cyclicals: use mid-cycle EBITDA and the sector volatility row. Loss-making companies: coverage on a deficit is meaningless (Security Analysis p. 480-481). High inflation: use EBITDA / interest (McKinsey p. 610-611).

## Output lines

- "Claim: [security] of [entity], rank [position]. Net debt [x]; net debt / EBITDA [y] times; EBIT / interest [z] times; EBITDAR / (interest + rent) [w] times ([period])." [reported, derived]
- "Implied rating bucket from 2011-2013 medians (verify): [bucket] on coverage, [bucket] on debt / capital; reported rating [r, source] or not available." [derived]
- "After an assumed [s] percent EBIT decline, coverage falls to [x] times against [y] needed for [bucket]." [derived; shock assumed]
- "Debt due within 24 months: [amounts, dates, funding source]. Repayment [does / does not] depend on market access. Covenant headroom [x]." [reported; judgment]
- "Claims outside the debt line: leases [x], after-tax pension deficit [y], contingent [z], other [..]." [reported]
- "Free cash flow FY-4 to FY0 [..]; capex [above / below] depreciation in [n] of 5 years." [derived]
- "Recovery at EV [a]: senior [r1] percent, subordinated [r2] percent, equity [r3]; at EV [b]: [..]. Fulcrum security: [name]." [derived; EVs assumed]
- "Bond and equity prices imply EV of [a] and [b]" [derived], or "Bond prices not available in Bigdata.com."
- "Would change the view: [dated, checkable item]." [judgment]

## Not in the sources

- Not in the sources: an Altman Z method or cutoffs; quote the FactSet field as reported.
- Not in the sources: net debt / EBITDA medians by rating from the folder's own texts; table 3 carries the agency's published ranges from outside the folder, and the skill says so when it quotes them.
- Not in the sources: recovery rates by seniority; state scenario enterprise values instead.
- Not in the sources: a maturity-wall standard beyond "debt due soon"; the 24-month window is a skill choice.
- Not in the sources: Graham and Dodd's minimum coverage by type of security (those chapters are on the book's CD, not in the text).
- Not in the sources: a cash-runway method for loss-making companies.
- Not in the sources: methods for REITs, project finance and securitisations.
- Not in the sources: bond prices, yields and spreads in Bigdata.com; verify what the credit-factor tools return.

## Sources

- Notes: Graham and Dodd, Security Analysis, 6th ed. (Marks, Lowenstein, Klarman preface, Berkowitz, Greenwald, Merkin; ch. 2, 37, 40, 45, 51); Klarman, Margin of Safety (ch. 4, 7, 12); McKinsey, Valuation, 5th ed. (ch. 7, 8, 12); McKinsey, Valuation, 5th ed. (ch. 23, 29, 36); Mauboussin, Total Addressable Market (2015), Operating Leverage (2016) and Global Industry Profit Pools (2016) (section 2.6); base-rates.md (section 2.8).
- Graham and Dodd, Security Analysis, 6th ed. (2009): p. xxviii, 85-88, 90, 128-140, 274, 346, 480-481, 508-512, 545-547, 591-597, 688-690.
- Klarman, Margin of Safety (1991): ch. 4, 7, 12.
- McKinsey, Valuation, 5th ed. (2010): ch. 7 p. 145; ch. 8 p. 182-184; ch. 12 p. 282-290; ch. 23 p. 489-524; ch. 29 p. 610-611; ch. 36.
- Mauboussin, Operating Leverage, Credit Suisse, 14 Jun 2016, ex. 14, p. 16.

<!-- Followed the notes over the spec: excess cash uses McKinsey's working cash of about 2% of revenue (the spec's 2% to 4% heuristic is not in the notes); the B one-year default of 3.46% is not in the notes and is taken from the Operating Leverage raw text, ex. 14; the Studebaker 26x figure is preferred-dividend coverage, not interest coverage. -->
