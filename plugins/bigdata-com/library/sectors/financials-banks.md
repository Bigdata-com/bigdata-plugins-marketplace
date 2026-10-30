# Financials: banks

This primer covers deposit-taking banks, including their trading and fee businesses. Insurers have their own primer. Asset managers, exchanges and payment networks carry little balance-sheet risk; value them with the standard enterprise methods. Every figure below is historical, illustrative or a rough range, never a current fact.

## How the sector makes money and what drives value

A bank earns three kinds of income:

- Net interest income (NII): interest earned on loans and securities minus interest paid on deposits and borrowings. It was about half of net revenue for retail-focused banks around 2010.
- Fees and commissions: advisory, underwriting, asset management, payments, brokerage. About half of net revenue for investment banks over the same period. Underwriting and advisory fees are cyclical.
- Trading income: volatile; several years of gains can be lost in one year.

Value depends on return on equity (ROE) against the cost of equity, growth of the equity base, and the capital ratio regulators and depositors require. Leverage magnifies everything. Funding rests on confidence that can disappear overnight. For these reasons, value a bank with scenarios, not a point estimate.

Not all NII creates value. A bank that funds long-term loans with short-term deposits earns a maturity-mismatch income that pays for interest-rate risk, not for a lending advantage.

## Metrics that matter

| Metric | Definition | Why it matters | Rough range, large developed-market banks |
|---|---|---|---|
| Net interest margin (NIM) | NII / average earning assets | Spread on the balance sheet | about 1.5% to 3.5% for US and most European banks; Japanese megabanks run below 1%, so compare within a market |
| Pre-provision net revenue (PPNR) | NII + noninterest income - noninterest expense | Earning power before credit costs | compare across the cycle, not as a level |
| Efficiency ratio | noninterest expense / (NII + noninterest income) | Cost discipline and scale | about 50% to 70% |
| Provision ratio | provision for credit losses / average loans | Management's forward loss estimate | read against charge-offs |
| Net charge-off (NCO) ratio | (gross charge-offs - recoveries) / average loans | Realised losses | through-cycle about 0.3% to 1.0% for a diversified book; cards higher |
| NPL ratio and coverage | NPLs / loans; allowance / NPLs | Asset quality, reserve cushion | trend matters more than level |
| CET1 ratio | common equity tier 1 / risk-weighted assets (RWA) | Binding capital constraint; sets growth and payout capacity | Basel minimum 4.5% plus buffers; large banks often run about 10% to 14% |
| ROTCE | net income to common / average tangible common equity | The return that drives price to tangible book | about 8% to 18% across a cycle |
| Loan-to-deposit ratio | loans / deposits | Funding stability | above about 100% means reliance on wholesale funding |
| Deposit beta | change in deposit cost / change in policy rate | How much of a rate move the bank keeps | rises late in a hiking cycle |
| Uninsured deposit share | deposits above the insurance limit / total deposits | Run risk: uninsured balances leave first (the 2023 US regional failures ran above 80%) | above about 50% needs a liquidity story |
| Liquidity coverage ratio (LCR) and net stable funding ratio (NSFR) | high-quality liquid assets / 30-day net outflows; available / required stable funding | Regulatory liquidity floors; a thin cushion limits balance-sheet growth and payouts | both at least 100% where required; large banks usually report 110% to 140% LCR |
| Unrealised securities losses / CET1 | AOCI and held-to-maturity marks against tangible common equity | Capital that disappears if securities must be sold | above about 30% of CET1 was the 2023 warning level |
| CRE concentration | commercial real estate loans / total risk-based capital | Concentration the US supervisors screen for | US supervisory screen: above 300%, or 100% for construction, draws scrutiny |

Most of these sit in the earnings release, supplement and capital disclosures, not the tearsheet ratios; search for them and read the full document.

## Financial statements and accounting traps

- Interest expense is the cost of goods: EBIT and EBITDA mean nothing, and there is no "net debt".
- The cash flow statement mixes loan originations, deposit flows and securities purchases; industrial free cash flow has no meaning. Use the equity cash flow below.
- Provisions are estimates. Expected-loss accounting (CECL in the US, IFRS 9 elsewhere) front-loads losses. Compare provisions with net charge-offs over several quarters: rising charge-offs with flat provisions point to under-reserving, and reserve releases lift earnings without cash. Under-provisioning reduces equity value because the deficit must be funded; do not deduct the provision a second time in a DCF.
- Gains on securities are not earning power. Watch loss reserves and marks on thin-market instruments.
- Securities held to maturity carry unrealised losses outside equity; available-for-sale losses sit in other comprehensive income and, for some banks, outside regulatory capital. This mattered in the 2023 US regional bank failures.
- Banks are opaque: true returns and risks are hard to see from outside. The accrual, EBITA and working-capital tests in `earnings-quality.md` do not apply; reconcile earnings to the change in equity.
- Use tangible equity for returns and multiples; acquirers carry goodwill.

## Profit pool and competitive dynamics

Banks are fragmented when measured globally: 1,114 listed firms, a four-firm revenue concentration of 15.6%, and a top-10 share of industry invested capital that rose from 23% to 32% between 2005 and 2015 (profit-pool data to July 2016). National markets are usually far more concentrated. Over that period the economic spread of commercial banks fell from 0.7 to 0.1 points between 2010 and 2015, while thrifts and mortgage finance recovered from -14.2 to 6.2 points. The pool is close to zero on average with wide dispersion, so explain who earns the spread and why.

Banks compete on a low-cost, stable deposit base, scale in technology and payments, underwriting discipline and regulatory capital as a barrier; nonbank lenders and private credit compete for loans. Regulation limits capital allocation choices: understand the capital rules before judging buybacks or growth. European banks shifted from interest income toward fees and trading between 1988 and 2007, which made ROE and price to book more cyclical.

## Persistence and fade

- The gross profitability, operating margin and operating leverage tables in `base-rates.md` exclude financials and utilities. Do not apply them to a bank.
- The CFROI table includes financials, measured on cash flow return on equity: four-year r 0.43, median 7.5%, mean 8.3% (global, live and dead, 1983-2015); the older cut gives r 0.43 and mean 6.8% (1986-2012). About 43% of a financial's excess return over the median is left after four years, a faster fade than consumer staples (r 0.78). The financials group in those samples also holds insurers and, before the 2016 GICS change, REITs.
- The sales and earnings growth tables cover all sectors. Bank "sales" is usually total revenue (NII plus noninterest income), and earnings swing with provisions, so state the growth basis.

## Valuation conventions and pitfalls

**Why enterprise multiples and the ROIC build do not apply.** Enterprise value, WACC and ROIC all depend on separating operating assets from financing. A bank's interest income and expense are its operations, so the split cannot be made: EV/EBITDA and an enterprise DCF have no consistent numerator or denominator. The return measure is ROE on adjusted net income against the cost of equity: "ROE is to financials as ROIC is to industrials".

**The alternative, in three parts:**

1. Equity DCF. Cash flow to equity: CFE = net income - increase in book equity + other comprehensive income, which equals dividends + buybacks - issuance. Growth consumes equity: required equity = target capital ratio x RWA. Continuing value: CV = NI(t+1) x (1 - g / RONE) / (ke - g), where RONE is the return on new equity. If RONE equals ROE, value = book equity x (ROE - g) / (ke - g).
2. Economic spread, to see where value is created. After-tax spread on loans: SAT = L x (rL - kL) x (1 - T) - TP, with tax penalty TP = T x L x [kL - (1 - eL) x kD], where kL and kD are the matched-maturity market rates for loans and deposits and eL the equity required per unit of loans. Forecast margins from forward rates implied by the yield curve, smoothed.
3. Multibusiness banks: value lending (spread plus equity DCF), trading (on VaR and return on VaR, cycle-averaged) and fee businesses (assets under management x fee rate) separately, then triangulate with multiples.

**Multiples.** Price to tangible book against ROTCE: justified P/B = (ROE - g) / (ke - g); justified P/E = (1 - g / ROE) / (ke - g). At an assumed ke of 10% and g of 3%, ROE of 8%, 10%, 12% and 15% justify about 0.7x, 1.0x, 1.3x and 1.7x book (derived from those formulas). A premium to book needs ROE above the cost of equity.

**Pitfalls.** Capitalising a peak-cycle ROE: normalise credit costs to through-cycle loss rates by loan category (cards highest, mortgages lowest, correlated with GDP). Holding the cost of equity fixed while the capital ratio or asset mix. Ignoring the tax cost of holding equity (equity x tax rate). Not valuing capital above the target ratio separately. Reading a high NIM as quality when it reflects credit risk or a duration gap.

## Questions for the earnings call

- What deposit beta is assumed in NII guidance, and how has the deposit mix (noninterest-bearing share) moved?
- How much of NII comes from the securities book and swaps repricing, and what is the sensitivity to a parallel and a non-parallel rate shift?
- Why did provisions differ from charge-offs this quarter, and what macro scenario weights sit behind the allowance?
- Which books (commercial real estate, cards, leveraged loans) show rising delinquencies?
- What CET1 target, including management buffer, governs buybacks, and what do pending capital rule changes do to RWA?
- What would marking held-to-maturity securities do to tangible book?

## What to watch at the macro level

The level and slope of the yield curve and the policy-rate path; deposit competition and money-market yields; the credit cycle (unemployment, GDP, commercial property values); capital and stress-test rules (Basel III implementation and national variants); funding confidence after any bank failure; and, for international banks, currency and sovereign exposure. Before extrapolating ROE, check sector profits against GDP: by 2006, financials, energy, utilities and materials made up 51% of S&P 500 earnings, up from 41%.
