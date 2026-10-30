# Spec: Credit analysis for an equity or credit view

## 1. Purpose
This method answers: can the company meet its obligations through a downturn and through refinancing, what does each layer of the capital structure recover if it cannot, and do the prices of the equity and the debt tell the same story. Jobs that use it: risk assessment, deep dive and thesis (leverage check on the equity), special situations (distressed), earnings quality (debt-related red flags). The method states the balance of evidence and what would change it. It does not give buy, hold or sell calls. The notes contain no Altman Z method, no net debt or FCF thresholds, no recovery rates and no maturity-wall standard; those are marked GAP.

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Debt (short-term, long-term), leases where reported, cash, current assets and liabilities, notes payable, goodwill, PPE | Tearsheet balance sheet, 5 fiscal periods | reported |
| EBIT, EBITDA, interest expense, rent expense | Tearsheet income statement; rent from filings via search | reported |
| Operating cash flow, capex, FCF, dividends, buybacks | Tearsheet cash flow | reported |
| Net debt, EV, market cap | Tearsheet key_metrics | reported |
| Altman Z and Piotroski, as reported by FactSet | Tearsheet ratios | reported |
| Forward EBITDA and EBIT | Tearsheet consensus estimates to FY+4 | reported |
| Debt maturities, covenants, ratings actions, credit agreements, pension deficits, contingent liabilities, deconsolidated entities | Search over filings and news; fetch the document | reported |
| Bond prices, yields, spreads, ratings | GAP: not in the field list for this project. Verify whether the bigdata_get_credit_factor and bigdata_screen_credit_factor tools return them | not available |
| Cost of debt, stress shock size | Chosen by the analyst and stated | assumed |

## 3. Procedure
1. Fix the claim. Name the security (senior secured, senior unsecured, subordinated, equity) and the legal entity that owes it. Holding-company debt can default while subsidiaries operate unimpaired, and debt at the operating subsidiary causes more disruption (Klarman, Ch.12). Done when the note names the obligor and the position in the capital structure.
2. Judge the stability of the business first. Credit risk is leverage times instability of cash flow, and a stable cash flow supports high leverage (Marks, in Security Analysis, p.132). A stable record is not proof of a stable business: a coverage of 26 times for an auto maker was less safe than 6 times for a grocery chain with stable demand (Security Analysis, pp.86 to 88). Done when the note shows the 5-year EBITDA range and the sector EBITDA volatility (section 5.3).
3. Compute leverage and coverage on the same period basis (formulas 4.1 to 4.5). Use total interest, not cash interest only. Done when each ratio has numerator, denominator and period shown.
4. Place the company against the rating tables (sections 5.1 and 5.2). Done when the note states the rating bucket the ratios imply, labelled derived, and the actual rating if a source gives it.
5. Stress the coverage. Reduce EBIT by an assumed shock (20% in the McKinsey example) and recompute. Done when the note shows coverage after the shock against the level the claim needs.
6. Test liquidity and the maturity wall. List debt due within 24 months from the filings, short-term bank loans and notes payable, cash, undrawn facilities and the covenant terms. Financial difficulty is almost always preceded by short-term bank debt, and large debt maturing soon is a frequent cause of insolvency (Security Analysis, Ch.45, pp.594 to 597). Done when each maturity has an amount, a date and a funding source, and the note states whether repayment depends on market access.
7. Look for claims outside the debt line: leases, unfunded pensions, contingent liabilities, deconsolidated entities, related-party loans. Run the balance-sheet checks from the WorldCom case: goodwill share of equity, PPE growth against revenue growth, a shift from short-term to long-term debt, deconsolidations (Security Analysis, pp.545 to 547). Done when each item is marked present, absent or unknown.
8. Check cash flow. Cash flow = after-tax earnings + depreciation and amortisation - capex. EBITDA is not cash flow. Capex below depreciation for long periods is gradual liquidation (Klarman, Ch.4). Done when FCF and capex against depreciation are shown over 5 periods.
9. Build the recovery view for stressed cases (formula 4.6). Split assets into the ongoing business and those available for distribution, list liabilities by seniority, and classify the claim as senior, fulcrum (partly covered) or junior (Klarman, Ch.12). Done when recovery per layer is shown for at least two scenarios with stated enterprise values. GAP: no recovery rates by seniority exist in the notes.
10. Compare layers. Test whether bond and equity prices imply the same enterprise value; one security of a company can be overvalued while another is cheap (Klarman, Ch.12, Bank of New England case). Done when the implied values are shown or the gap in bond price data is stated.

## 4. Formulas
4.1 Coverage = EBIT / total interest expense. Variants: EBITA / interest, EBITDA / interest, and EBITDAR / (interest + rent) for lessees such as retailers (McKinsey, Valuation, 5th ed., pp.182 to 184 and p.500). Klarman compares earnings to total interest, never EBITDA to cash interest, which he calls meaningless; his notes write the numerator as "pretax earnings", so state whether it is before or after interest.
4.2 Net debt / EBITDA, with net debt = debt + capitalised operating leases - excess cash. Excess cash excludes working cash of about 2% to 4% of revenue (a rating-agency heuristic quoted in the notes). Prefer this ratio when low-coupon convertibles or cheap short-term debt will reprice, because interest coverage would fall at refinancing (McKinsey, p.500).
4.3 FCF / total debt (derived). GAP: no threshold in the notes.
4.4 Market-adjusted debt ratio = market value of the common stock / funded debt, a leading margin-of-safety test (Security Analysis, Marks, p.138). Book solvency ratios (debt to assets, debt to book equity) are the least useful measure (McKinsey, p.500). Debt to tangible assets above 1 is a warning (Klarman, Ch.4).
4.5 Leverage identity: ROE = ROIC + (D/E) x [ROIC - (1 - T) x kd]. More debt raises ROE and its sensitivity to ROIC, which is risk (McKinsey, pp.182 to 184).
4.6 Recovery of layer i in a scenario: R_i = min(1, max(0, (EV_s - claims senior to i) / claim_i)). Equity = max(EV_s - total claims, 0), weighted by scenario probability (McKinsey, Ch.12, pp.282 to 290: with EV 1,500 or 900 at 50/50 and debt 1,200, equity is 150). Do not deduct the market value of distressed debt.
4.7 Bond arithmetic: a 5-year 10% bond at par, rates fall to 5%: price 121.88, hold-to-maturity return 9.10%; rates rise to 15%: price 82.84, hold-to-maturity return 10.99% (Klarman, Ch.7, footnote). Mark-to-market and long-term return diverge.

## 5. Reference tables
### 5.1 Credit-rating medians (Mauboussin, "Operating Leverage", Credit Suisse, 14 Jun 2016, pp.15 to 17; S&P three-year medians 2011 to 2013, defaults for 2014; verify)
| Rating | Operating margin % | EBIT coverage x | Debt / total capital % | Return on capital % | 1-year median default % |
|---|---|---|---|---|---|
| AAA | 28.0 | 40.8 | 2.8 | 30.6 | 0.00 |
| AA | 26.9 | 17.3 | 17.2 | 21.6 | 0.00 |
| A | 22.7 | 10.3 | 30.7 | 22.2 | 0.00 |
| BBB | 21.3 | 5.5 | 41.1 | 14.2 | 0.12 |
| BB | 17.9 | 3.2 | 50.4 | 11.1 | 0.71 |
| B | 19.2 | 1.3 | 72.7 | 7.1 | 3.46 |

### 5.2 Default probability and coverage rules (McKinsey, Valuation, 5th ed., Ex. 23.4 to 23.6, pp.494 to 504; S&P 1981 to 2003; verify)
| Rating | AAA | AA | A | BBB | BB | B | CCC |
|---|---|---|---|---|---|---|---|
| 5-year default probability % | 0.12 | 0.33 | 0.75 | 3.84 | 14.45 | 33.02 | 61.35 |
Rules: EBITA / interest of about 5 to 11 corresponds to A+ to BBB-, where 72% of large US and European companies sat. Coverage alone explains about 45% of rating differences. All AAA companies had market cap above $50 billion. Value barely changes with coverage except below 2, and overleverage costs far more than underleverage. Spreads jump below BBB- because many institutions cannot hold sub-investment-grade debt. Example in the book: Home Depot 7.0 times against Lowe's 11.8 times, rated BBB+ and A+ in 2008. A target single-A needed about 9.5, and coverage had to stay at or above 7.5 after a 20% EBIT drop (illustrative case).

### 5.3 EBITDA volatility, median of the 25 largest firms (McKinsey, Ex. 23.6)
Semiconductors 41.2%, computer hardware 29.8%, steel 26.5%, retail 13.5%, chemicals 11.4%, telecom 10.4%. Required coverage for a given rating is higher where EBITDA is volatile.

### 5.4 Graham and Dodd and Klarman thresholds (dated; use the logic, verify the numbers)
| Test | Figure | Source and caveat |
|---|---|---|
| Current ratio, quick ratio | 2:1 and 1:1 | 1930s industrial norms; no better figure proposed; industry exceptions (Security Analysis, pp.591 to 594) |
| Coverage judgment | Earnings at 3 times interest on average over seven years is a level not to fall far below, not a forecast | Security Analysis, p.85 |
| Bond buyer's three conditions | Rising profit trend, good current showing, margin over interest in every year; if one fails, require average coverage well above the minimum | Marks, p.136 |
| New junk issue standards | Coverage below 1.0 by 1988; debt above tangible assets | Klarman, Ch.4 |
| Unseasoned industrial bonds and preferreds | Buy only on speculative terms, price below 70 | Security Analysis, pp.688 to 690, 1930s |
GAP: Graham and Dodd's minimum coverage ratios by security type are in chapters held on a CD that the notes do not cover; only the illustrations above are available.

## 6. Interpretation rules
6.1 Distressed signals: short-term bank loans and notes payable rising; large maturities within 24 months; coverage below 1.0; debt above tangible assets; inventories and receivables building while cash falls; dividends held while FCF is weak, since stressed companies are almost always late to cut; non-cash-pay (PIK, zero-coupon) or interest-reset features, which postpone default and raise ultimate risk; a new yield measure replacing the standard one ("yield to reset"); equity collapse raising market leverage while cash flow is thin (KPN and France Telecom, 2001); related-party and off-balance-sheet loans (Adelphia: debt 11 times market cap against 1.28 for Comcast); interim reporting dropped when results weaken. Avoid fixed income in a rapidly deteriorating business with negative operating cash flow before interest (Klarman, Ch.12). Altman Z and Piotroski are reported flags only. GAP: the notes give no Altman Z method or cut-offs; verify the FactSet definition before reading a zone.
6.2 Safety margin for bonds. Bond gains are capped at the promised yield and losses can be total, so the work is to avoid losers (Marks, p.131). Bonds well below par offer more upside and less downside than bonds near par of the same credit quality (Klarman, Ch.4). A high coupon does not compensate for substantial risk of principal, and the test is the likelihood of payment, not the label on the security (Marks, p.128).
6.3 Ratings and default statistics can mislead. Issuer-paid ratings and appraisals misled in the 1920s and 2007 (Marks, p.140). Default rates look low when the issuer base is growing fast, prefunding delays defaults, and exchanges impair holders without a default; group by year of issue (Klarman, Ch.4).
6.4 When the method does not apply. Banks and insurers: interest is an operating item and there is no net debt, so use equity measures (McKinsey, ch.36). Cyclicals: use mid-cycle EBITDA and the sector volatility row. Early-stage or loss-making companies: coverage on a deficit is meaningless (Security Analysis, p.480); GAP: the notes have no cash-runway method. High inflation: use EBITDA / interest (McKinsey, pp.610 to 611). REITs, project finance and securitisations: GAP.
6.5 Review credit at least quarterly (Marks, p.133).

## 7. Output lines
- "Claim: [security] of [entity], rank [position]. Net debt [x], net debt / EBITDA [y]x, EBIT / interest [z]x, EBITDAR / (interest + rent) [w]x ([period])." (reported, derived)
- "Implied rating bucket from medians: [bucket] on coverage, [bucket] on debt / capital; reported rating [r, source or not available]. Medians are 2011 to 2013 (verify)." (derived)
- "After a [20]% EBIT decline, coverage falls to [x]x." (derived; shock assumed)
- "Debt due within 24 months: [amount, dates, funding source]. Repayment [depends/does not depend] on market access." (reported, judgment)
- "Claims outside the debt line: leases [x], pension deficit [y], contingent [z]." (reported)
- "Recovery, scenario [a] EV [x]: senior [r1]%, subordinated [r2]%, equity [r3]. Scenario [b]: [..]." (derived; EV assumed)
- "Bond and equity prices imply EV of [a] and [b]." (derived) or "Bond prices not available."
- "Would change the view: [dated, checkable item]."

## 8. Sources
Notes: security-analysis.md (Marks, Lowenstein, Ch.2, 40, 45, 51, Greenwald, Merkin, Section 4), klarman.md (Ch.4, 7, 12), mckinsey-part2.md (Ch.23), mckinsey-part1.md (sections 8.4 and 12), tam-leverage-profit-pools.md (section 2.6), base-rates.md (section 2.8), expectations-multiples-dcf.md (EV completeness). Books and papers: Graham and Dodd, Security Analysis, 6th ed. (2009); Klarman, Margin of Safety (1991); McKinsey, Valuation, 5th ed. (2010); Mauboussin, "Operating Leverage" (2016).
