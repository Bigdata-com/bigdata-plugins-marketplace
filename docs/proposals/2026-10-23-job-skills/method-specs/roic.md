# Return on invested capital, built properly

Purpose: answer what the company earns on the capital its business uses, how that compares with its cost of capital, and where it is heading. Used by company, valuation, moat, quality of earnings, thesis and sector jobs. The skill must state every definitional choice, because ROIC moves by a factor of two or more on those choices (Procter and Gamble 2006: 10.6% with goodwill, 26.2% without [D07 p.43-45]).

Source tags: [D07] Damodaran 2007; [MC14] Mauboussin and Callahan, Calculating ROIC, 2014; [MC13] their Estimating the Cost of Capital, 2013; [V5] McKinsey, Valuation 5th ed.; [BR] base-rates note.

## 1. Inputs
- Reported, tearsheet income statement: EBIT, amortization of acquired intangibles, income tax expense, pretax income, interest, non-operating income, R&D, revenue. Five fiscal periods per call.
- Reported, tearsheet balance sheet: receivables, inventory, prepaid, payables, accruals, deferred revenue, PPE net, goodwill and intangibles, cash and securities, debt, lease liabilities (where reported), equity, minority interest, invested capital field.
- Reported, tearsheet ratios: ROIC field (FactSet).
- Search (filings): tax reconciliation note, lease note, R&D and restructuring disclosures.
- Assumed: WACC. Bigdata.com has no WACC field.

## 2. Procedure
1. State the definition in one line: tax method, average or opening capital, goodwill, leases, R&D, excess cash rule. Done: repeated under every ROIC table.
2. Build NOPAT = EBITA (EBIT plus acquired-intangible amortization) x (1 minus operating tax rate). Take the rate from the tax note (statutory plus state, plus recurring operating items). Do not use reported tax or the effective rate: it contains the interest tax shield, which WACC already counts [D07 p.8; V5 7.6]. Optional cash-tax variant: add the rise in operating net deferred tax liability [MC14 p.2-3]; show separately. Unusual charges: one-time (remove), periodic (spread), volatile (average), sign-flipping (ignore) [D07 p.37-39].
3. Build invested capital, operating side: operating working capital (receivables, inventory, prepaid, less payables, accruals, deferred revenue; no excess cash, no interest-bearing items) plus PPE net plus goodwill and acquired intangibles plus other net operating assets [V5 7.2]. Keep an item only if the company could not earn the same NOPAT without it [MC14 p.5].
4. Build it from the financing side: debt plus lease liabilities plus unfunded pensions plus equity plus minority interest, less excess cash and non-operating assets [V5 7.2]. The sides must reconcile; a gap is a missed item. Compare with the tearsheet invested capital field.
5. Compute ROIC with and without goodwill and acquired intangibles, side by side. Without measures the operating business; with measures the return on all capital raised, premiums included [MC14 p.7-8; V5 8.1]. Add back cumulative impairments [V5 7.2]. Judge deals by net present value, not ROIC [MC14 fn.12].
6. Strip excess cash. Operating cash allowance: 2% of sales for steady companies, 5% for less predictable or faster-growing ones [MC14 p.6-7; V5 7.3]. Remove the same amount from equity; keep interest on cash out of NOPAT.
7. Leases: state whether the feed capitalizes them (on balance sheet since ASC 842 and IFRS 16, 2019; verify). If capitalized, add implied interest (prior-year lease liability x pre-tax cost of debt) to EBITA [V5 7.8]. Before 2019, capitalize the present value of commitments at the pre-tax cost of debt [D07 p.30-37]. The WACC debt weight changes too. Show ROIC before and after.
8. Capitalize R&D when material, and advertising only with evidence of multi-year benefit [D07 p.28]. Research asset = sum over t = -(n-1) to 0 of R&D(t) x (n+t)/n, n = amortizable life (pharma about 10, software short). Adjusted EBIT = EBIT + R&D minus amortization; capital plus research asset [D07 p.20]. Say so if history is shorter than n.
9. Headline ROIC = NOPAT / average of opening and closing capital [V5 8.1]; show the opening-capital variant [D07 p.7].
10. Decompose: ROIC = (1 minus t) x EBITA/revenue x revenue/capital, over five to ten years, with working capital days. High margin points to a consumer advantage, high turnover to a production advantage [MC14 p.12-14]. Segment ROIC needs filing segment capital; tearsheet segments are revenue only.
11. Compute ROIIC, set WACC, the spread and the reversion path (sections 3 and 5). Run the checks (section 6).

## 3. Formulas
- ROIC = NOPAT / average invested capital. Economic profit = capital x (ROIC minus WACC) = NOPAT minus WACC x capital; use one capital definition for both [V5 6.7].
- g = ROIC x investment rate. FCF = NOPAT minus net investment. Value = NOPAT(t+1) x (1 minus g/RONIC) / (WACC minus g), RONIC = return on new invested capital [V5 2.2, 10.1].
- ROIIC (1-year) = (NOPAT(t) minus NOPAT(t-1)) / (IC(t-1) minus IC(t-2)) [MC14 p.10]. Rolling n-year form (derived): (NOPAT(t) minus NOPAT(t-n)) / (IC(t-1) minus IC(t-n-1)); use n = 3 and 5 for lumpy investment. Do not compare ROIIC with WACC; high values can be operating leverage [MC14 p.11].
- WACC = D/V x kd x (1 minus T) + E/V x ke, market weights; ke = rf + beta x ERP. beta_u = beta_L / [1 + (1 minus T)(D/E)]; adjusted beta = 0.67 x raw + 0.33 [MC13 p.7, 14-19].
- Expected ROIC in four years = sector mean + r x (current minus mean) [BR 1.4].

## 4. Worked table layout (one column per fiscal year)
| Row | Source | Label |
|---|---|---|
| EBIT, acquired-intangible amortization, EBITA | tearsheet income statement | reported, derived |
| Operating tax rate, operating taxes, NOPAT | filing tax note | assumed, derived |
| Working capital items, PPE net, goodwill and intangibles | tearsheet balance sheet | reported |
| Excess cash removed (cash minus 2% or 5% of sales) | tearsheet | derived |
| Invested capital: operating side, financing side, difference | | derived |
| Invested capital field | tearsheet | reported |
| ROIC with goodwill, without, lease-adjusted, R&D-adjusted | | derived |
| ROIC ratio field | FactSet | reported |
| Margin, turnover, ROIIC (1, 3, 5 year) | | derived |
| WACC, spread, economic profit | | assumed, derived |

The FactSet ROIC field and a hand-built ROIC will differ. GAP: the notes do not give FactSet's definition (tax rate, goodwill, leases, average or year-end capital). The output must name which one is quoted on each line, never mix them in one comparison, and explain gaps from the section 2 choices.

## 5. Reference tables
Cost of capital inputs (all assumed; fetch current values; verify all):
| Item | Range or rule | Source |
|---|---|---|
| Risk-free | 10-year government yield on valuation date, never a bill | [MC13 p.18; V5 11.2] |
| Equity risk premium | 4.5% to 5.5% (2009); Damodaran 5.7%, Credit Suisse 4.5% (Oct 2013); textbook 3% to 10% | [V5 11.2; MC13 p.12-13] |
| Cost of equity, large companies | 8% to 10%; median cost of capital about 8% (US, 1963-2008) | [V5 ch.1-2, 4.4] |
Show prevailing and normalized WACC, each labelled [MC13 p.22-25]. Check ke above kd, ERP above credit spread.

Four-year persistence r of CFROI (HOLT, global, 1983-2015) [BR 2.7]: staples 0.78, discretionary 0.67, health care 0.64, industrials 0.62, utilities 0.57, telecom 0.55, IT 0.50, financials 0.43, materials 0.41, energy 0.35. CFROI differs from ROIC; use r as a speed guide (higher r, slower reversion).

US non-financial ROIC without goodwill, 1963-2008: median about 10%; companies above 20% fall from a median 29% to 15% in 15 years, not to the median. Starting above 20%, 67% stay above 20% over ten years (1995-2005); starting below 10%, 57% stay below [V5 4.4]. Industry medians: pharma and biotech 23.5%, utilities 6.3% (verify).

Path by advantage and sector barriers [D07 p.59]: strong company advantage and strong barriers, company ROIC then sector average; strong advantage, weak barriers, then cost of capital; weak advantage and strong barriers, sector average; weak and weak, cost of capital. Convention: five-year fade, then 10% of the spread removed per year, then cost of capital [BR 1.4]. Rule of thumb: mature companies earn at most 2 to 3 points over cost of capital in perpetuity [D07 p.63].

## 6. Interpretation and checks
- Show ROIC, ROIIC and RONIC for every forecast year. Forecast ROIC should hold near current, trend to the sector median, or trend to WACC, with a reason [V5 9.6].
- Flag any turnover jump and any implied negative capex [V5 9.5].
- Check investment rate = g / ROIC. Terminal growth above the economy's, or terminal ROIC below WACC, is an error [D07 p.63; V5 9.1].
- Flag ROIC lifted by write-offs that shrink capital [D07 p.37-39]; buybacks lift ROE, not ROIC [D07 p.39-40].
- Does not apply to banks and insurers (use adjusted ROE [MC14 p.11]), captive finance arms (separate [V5 7.3]) or early-stage companies (negative NOPAT). For cyclicals use cycle-average NOPAT; for EM use local-currency yields less default spread [MC13 p.18].
- Starting ROIC is already priced; returns come from change against expectations [roic-moat.md, paper D].

## 7. Output lines
- "ROIC ([definition line]) is X% with goodwill and Y% without; the provider field shows Z%." Derived; reported.
- "NOPAT uses operating tax rate t%." Assumed.
- "Lease adjustment moves ROIC from X% to Y%." Derived.
- "WACC W% prevailing, V% normalized; rf, ERP, beta, weights stated." Assumed.
- "Spread S points; economic profit $E." Derived.
- "ROIIC over 3 and 5 years is A% and B%." Derived.
- "Reversion path: N years to M%, because [sector and moat evidence]." Judgment.

## 8. Sources
Notes: roic-moat.md, mckinsey-part1.md (ch. 2, 4, 6 to 11), base-rates.md (1.4, 2.7). Papers: Damodaran (2007); Mauboussin and Callahan (2013, 2014); McKinsey, Valuation, 5th ed.
