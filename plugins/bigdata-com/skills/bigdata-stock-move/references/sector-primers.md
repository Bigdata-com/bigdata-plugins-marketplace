# Sector primers

Read the section for the company's sector before analysing; skip the rest. Every figure is a range with its source and a (verify) mark, never a current fact.

- Technology: software (`technology-software`)
- Technology: semiconductors and hardware (`semiconductors-and-hardware`)
- Financials: banks (`financials-banks`)
- Industrials (`industrials`)
- Consumer and retail (`consumer-retail`)
- Energy (`energy`)
- Materials (`materials`)
- Communication services (`communication-services`)

## Technology: software

Scope: application and infrastructure software sold as subscriptions, licenses, usage or transactions. Hardware and semiconductors have their own primer; consumer internet platforms sit in communication services. A figure marked "(verify)" is a judgment or dated: check it against the peer set and period before use.

## How the sector makes money and the value drivers

Software is a knowledge business in Mauboussin's terms: high upfront cost, low cost per extra unit, no direct link between sales and costs, and an advantage that is hard to protect without lock-in or network effects (Total Addressable Market, 2015, pp.20, 23). The value drivers:

- Recurring revenue growth = new customers + expansion within existing customers + price, minus contraction and churn.
- Gross margin: hosting, support and services costs. Subscription gross margin is commonly 70 to 85 percent (verify); services run near break-even.
- Operating margin at scale: sales and marketing and R&D are the real investment, and both are expensed.
- Reinvestment: little tangible capital, so growth is funded through the income statement, not the balance sheet.
- Duration of advantage: switching costs (data, integration, training), network effects and de facto standards. These are the conditions under which returns can rise with scale rather than fade (roic-moat notes, Mauboussin 2014, pp.14-15).

## The metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| ARR | Annualized value of active recurring contracts, excluding services and uncommitted usage | Base for growth and efficiency ratios; definitions differ by company |
| Net revenue retention (NRR) | (Starting ARR + expansion - contraction - churn) / starting ARR, over 12 months, same cohort | Growth from the installed base; above 100 percent means the base grows without new logos |
| Gross revenue retention (GRR) | (Starting ARR - contraction - churn) / starting ARR | Stickiness with expansion removed; the cleaner test of switching costs |
| Remaining performance obligations (RPO, cRPO) | Contracted revenue not yet recognized; current portion due within 12 months | Leads revenue; length of contracts changes it |
| Billings | Revenue + change in deferred revenue | Demand signal, distorted by billing terms |
| CAC payback | Sales and marketing cost to win a customer / (new ARR x gross margin), in months | Speed at which growth spending is recovered in cash |
| Rule of 40 | Revenue growth percent + FCF margin percent | Practitioner heuristic; not in the sources |
| SBC / revenue | Stock-based compensation as a share of revenue | A real cost that adjusted margins exclude |

Practitioner ranges (judgment, not in the sources, verify): NRR of about 100 to 120 percent for established enterprise vendors, above 120 percent for the best cohorts; GRR of about 85 to 95 percent for enterprise, lower for small-business products; CAC payback of about 12 to 36 months; SBC of about 5 to 30 percent of revenue, highest at early stages.

Prefer metrics that are persistent and predictive over popular ones (What Makes for a Useful Statistic, 2016): gross profitability and operating margin persist year to year; one-year sales growth does not (base-rates.md 2.5, 2.6).

## What the statements do differently and the accounting traps

- **Expensed investment overstates ROIC.** R&D and customer acquisition are expensed, so invested capital is understated. McKinsey's Adobe example: ROIC excluding goodwill with R&D expensed ranged from 221 to 12,708 percent; with R&D capitalized it was about 40 percent and stable (Valuation, 5th ed., 2010, ch.28). Capitalize R&D with a short life (Damodaran: software short; judgment 3 to 5 years, verify) before comparing returns. Free cash flow does not change.
- **Negative invested capital.** Deferred revenue is an operating liability netted against operating assets. In a subscription business it can push invested capital below zero and make ROIC infinite and meaningless (McKinsey ch.34). Say so and use economic profit or cash returns instead.
- **Cash runs ahead of earnings.** Microsoft FY2005: net income $12.25bn against cash flow $15.59bn, from unearned revenue, SBC and taxes (Expectations Investing, pp.63-64). Upfront billing growth flatters cash flow; a slowdown reverses it.
- **Stock-based compensation.** Past awards add shares; future awards belong in the forecast. Do not count one award both as an expense and in the share count (UBS DCF2, 2017, p.17). Show margins and FCF with and without SBC.
- **Billing terms.** Moving from monthly to annual billing raises deferred revenue with no change in economics; multi-year prepaid deals inflate RPO.
- **Revenue recognition.** Upfront term licenses make quarters lumpy; gross versus net reporting changes EV/Sales (multiples notes 2.4).
- **Excess cash and capitalized development.** Surplus cash left in capital depresses ROIC (use an operating cash allowance of about 2 to 5 percent of sales, roic-moat notes); a rising capitalized share of development cost flatters margin.
- **Acquisitions.** Serial acquirers: use EBITA and show ROIC with and without goodwill (McKinsey ch.26).
- **Tax.** US tax amortization of R&D (from 2022) changes cash taxes; not in the sources, verify the current rule.

## Profit pool and competitive dynamics

HOLT's profit-pool study (data June 2016, verify) counted 770 listed software firms with a four-firm revenue ratio of 39.3 percent, just under the 40 percent line that marks a competitive industry. The top ten's share of industry invested capital rose from 49 percent (2005) to 55 percent (2010) and 61 percent (2015); in internet software and services it rose from 47 to 71 percent. IT consulting moved the other way (44 to 35 percent). Value has been migrating to the leaders.

The dynamics behind that:

- **Network effects and standards.** In consumer products the leader rarely exceeds 40 percent share; with strong network effects it is generally above 50 percent and often near 90 percent (TAM 2015, pp.17-19). Only networks where users interact qualify, and most never tip.
- **Minimum efficient scale.** Microsoft spent about $6bn on Vista, then sold copies at near-zero marginal cost (Measuring the Moat, 2013); high fixed development cost deters entry.
- **Switching costs** are procedural (training, data migration, integration) more than contractual. GRR and contract length are the evidence.
- **Overshoot and disruption.** Signs: customers use a fraction of the features and refuse to pay for new ones; competition shifts to speed and convenience. A platform shift (on-premise to cloud, possibly AI agents, judgment) can act as low-end or new-market disruption.
- **Industry is not destiny.** Every industry holds value creators and destroyers (Profit Pools 2016, p.2). Explain the dispersion inside the peer set.
- **Peer sets are survivor-biased.** Growth companies stay private longer and acquired names drop out of screens (Shrinking Universe, 2017). Build the map and pool with `references/industry-structure.md`.

## Persistence and fade

Historical base rates, not current facts (verify against current data). The sample pools software with hardware and semiconductors under "Information technology"; software-only rates are not in the sources.

| Measure | Information technology | All sectors | Sample |
|---|---|---|---|
| Gross profitability, 5-yr r; median | 0.63; 0.39 | staples 0.86, energy 0.61 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Operating margin, 5-yr r; median; mean | 0.62; 13%; 15% | all sectors 1-yr 0.91, 5-yr 0.72 | Same, 1950-2015 |
| CFROI, 4-yr r; median; mean | 0.50; 8.5%; 9.0% | staples 0.78, energy 0.35 | Global, market cap about $250M plus, 1983-2015 |
| CFROI, older cut, 4-yr r; mean | 0.38; 7.7% | | HOLT, r 1986-2012, means 1990-2012 |
| Operating margin beta, 1-yr / 3-yr | 0.173 / 0.158 | about 0.11 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Sales growth correlation with US real GDP | 0.55 | | Top 1,000 global, 1950-2014 |

Reading: at a four-year r near 0.5, about half of a company's excess CFROI over the sector mean is gone after four to five years, faster than in consumer and health care (Base Rate Book, 2016). The high operating margin beta means larger forecast misses, so widen ranges. McKinsey lists software among industries with high, persistent median ROIC (ch.4, 1965-2007, verify): the mean is high even as individual spreads fade. For any growth claim, place it in the size-and-horizon class from `references/base-rates.md`: for companies with $4.5 to 7bn of sales, a 10-year real sales CAGR of 15 percent or more occurred in 4.2 percent of cases (1950-2015).

## Valuation conventions and their pitfalls

- **High growth** (organic growth above 15 percent a year): use a scenario DCF that starts from a steady state 10 to 15 years out. Size the addressable market at returns above the cost of capital, cap share with a saturated early market, take long-run margins from mature analogues (medians, not means), work back to today and weight the scenarios with base rates (McKinsey ch.34; `references/valuation.md`).
- **EV/Sales or EV/ARR** only when profits are negative or unrepresentative. Since EV/Sales = EV/EBITA x EBITA margin, state the long-run margin the multiple implies.
- **EV/EBIT or EV/NOPAT** once margins are representative; P/E only with similar leverage and accounting. Treat SBC as a cost in any FCF yield.
- **PEG** ignores ROIC and makes growth that adds no value look cheap (multiples notes 2.4).
- Rule-of-40 premiums and EV/ARR bands by growth rate have no source; if used, build them from a live regression on the current peer set.
- Check that the implied terminal multiple is below today's; reverse-engineer the price to the implied growth and competitive advantage period with `references/expectations.md` before stating a view.

## Questions a specialist asks on the earnings call

1. What were NRR and GRR, and did the cohort definition change?
2. How much of net new ARR came from price increases, seat growth, usage and new logos?
3. Did sales cycles lengthen, and where (segment, region, deal size)?
4. How did RPO duration and billing terms change, and what would billings be on constant terms?
5. What is SBC as a share of revenue, and what is the net share count path after buybacks?
6. How much R&D and software development was capitalized this period against last year?
7. Where is gross margin heading as hosting and AI inference costs rise, and who bears them?
8. Which competitors appear in lost deals, and are any new entrants pricing below you?

## What to watch at the macro level

- Enterprise IT budgets and hiring: seat-based pricing tracks customer employment.
- Interest rates: long-duration cash flows make value sensitive to the discount rate (judgment).
- Currency: use constant-currency growth for vendors with foreign revenue.
- Cloud and AI compute costs: an input cost for vendors that host or run models.
- Regulation: privacy, data residency, antitrust on bundling, AI rules (verify per market).
- Sales growth tracks GDP only moderately (r 0.55, 1950-2014), so macro-driven forecasts are weaker here than for industrials (Operating Leverage, 2016).

## Technology: semiconductors and hardware

Scope: chip designers (fabless), integrated manufacturers, foundries, memory, semiconductor equipment and materials, and hardware makers (computers, storage, networking and communications equipment, devices). A figure marked "(verify)" is a judgment or dated: check it against the peer set and period before use.

## How the sector makes money and the value drivers

These are physical businesses with heavy preproduction cost: fabs, process development and chip design are paid before the first unit ships. Value comes from:

- **Volume x price x mix.** Unit demand from end markets (PCs, phones, data centers, autos, industrial), average selling price, and the mix of leading-edge against mature products.
- **Price declines and the learning curve.** Prices for a given level of performance fall every year. Measuring the Moat (2013) shows semiconductor prices falling about 8.6 percent a year in 2006-2011, the steepest of the fast-cycle examples quoted (verify). Profit depends on moving down the cost curve faster than price: the median product cuts unit cost about 20 percent for each doubling of cumulative output.
- **Utilization.** With most costs fixed, gross margin follows fab or factory loading. Changes in capacity utilization correlate about 0.60 with changes in operating margin across large companies (1967-2015).
- **Capital intensity and reinvestment.** Leading-edge capacity and tools are expensive and arrive in large blocks; fabless designers carry R&D but little fixed capital.
- **Product cycles and design wins.** A win in a customer's platform sets revenue for its life; a missed node or generation is hard to recover.

## The metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| Book-to-bill | Orders / shipments in the period (equipment, some components) | Leads revenue by one to several quarters |
| Inventory days, company and channel | Inventory / cost of goods sold x 365; distributor and customer weeks of supply | Rising days ahead of a slowdown signal a correction |
| Utilization | Output / capacity | Drives gross margin through fixed-cost absorption |
| Gross margin | (Revenue - COGS) / revenue | Mix, pricing and utilization in one number |
| Capex / revenue | Capital spending intensity | Separates foundry and memory from fabless; peaks come with oversupply risk |
| R&D / revenue | Design and process spending | The real investment for fabless and equipment companies |
| ASP and bit or unit growth (memory) | Price per bit and bits shipped | Memory profit is set by supply growth against demand growth |
| Customer concentration | Largest customers' share of revenue | One platform loss can remove a large share of sales |
| Sell-in against sell-through | Shipments to distributors against their sales to end users | Gap shows channel filling |

Typical ranges (judgment, not in the sources, verify): R&D at about 10 to 25 percent of revenue for designers and equipment makers; capex above 30 percent of revenue for leading foundries and memory makers in heavy years; gross margin from about 30 to 40 percent for hardware assemblers to above 60 percent for leading designers.

## What the statements do differently and the accounting traps

- **Inventory.** Write-downs reverse into margin when written-down units sell; check reserve releases in recovery quarters. Rising inventory with flat sales is the first warning.
- **Depreciation lives.** Fab equipment lives (judgment, about 5 to 7 years, verify) set reported margin; a change in useful life moves earnings with no cash effect. Compare depreciation with capex.
- **Underutilization charges.** Some companies expense idle capacity outside COGS or call it one-time; count how often it recurs.
- **Expensed R&D** overstates ROIC for designers. Capitalize it to compare designers with manufacturers on the same basis (McKinsey ch.28; Damodaran's research-asset method in roic-moat notes).
- **Customer prepayments, take-or-pay deals and government grants** reduce reported capex or appear as liabilities; read the cash flow statement and notes (subsidy programs vary by country, verify).
- **Revenue recognition for systems.** Equipment revenue may be split between shipment and acceptance; hardware bundles with services or software defer part of the price.
- **Acquisitions.** The industry consolidates through large deals; use EBITA, show ROIC with and without goodwill, and haircut revenue synergies (nearly half of acquirers realize under 70 percent of target, McKinsey ch.21, verify).

## Profit pool and competitive dynamics

- **Cyclical returns.** McKinsey lists semiconductors among cyclical industries, with chemicals, oil and gas and metals (ch.4, median ROIC 1965-2007, verify). Supply drives the cycle: capacity is added when returns are high and arrives in large blocks, and utilization and returns fall about two years later (the commodity chemicals pattern, McKinsey ch.35). Memory is the clearest case.
- **Capacity races.** Each firm gains from adding capacity alone; when all add, the payoff is lowest (a prisoner's dilemma, Measuring the Moat). Watch announced capex across the whole industry, not one firm.
- **S-curve overshoot.** Color TV makers built 14 million units of capacity against peak sales of 6 million because they extrapolated mid-curve growth (TAM 2015). Apply the same check to any new end market.
- **Replacement cycles.** Once replacements dominate unit demand (within 5 to 12 years for most products), forecast the replacement cycle, not penetration. A one-year lengthening of the cycle cut cumulative 15-year units 17 percent in the paper's example. In 2015 PCs were in the replacement stage and smartphones in transition (verify current stages).
- **Share stability.** Average five-year absolute share change of 2 points or less marks a stable industry; 2007-2012 readings were PCs 3, storage 4, smartphones 9 (Measuring the Moat, verify).
- **Concentration** (HOLT profit pools, data June 2016, verify): computers and peripherals, 275 firms, four-firm ratio 42.4 percent, top ten's share of invested capital 64 / 60 / 72 percent (2005 / 2010 / 2015); communications equipment, 366 firms, 48.2 percent, 67 / 68 / 64. Semiconductors were not broken out in the notes.
- **Sources of advantage.** Production advantages (process know-how, scale in fabs and tools, learning curve) show as lower gross margin and high asset turnover; design and ecosystem advantages (software stacks, standards, switching costs for developers) show as high gross margin (Measuring the Moat, pp.34-41).
- **Modularization.** When components standardize, the industry shifts from integrated to horizontal and value moves to the bottleneck layer (computers 1980 against 1995).

## Persistence and fade

Historical base rates, not current facts (verify against current data). Semiconductors and hardware are pooled with software under "Information technology"; sub-industry rates are not in the sources.

| Measure | Information technology | Comparison | Sample |
|---|---|---|---|
| Gross profitability, 5-yr r; median | 0.63; 0.39 | staples 0.86 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Operating margin, 5-yr r; median; SD of sector mean | 0.62; 13%; 3 points | staples 0.89 | Same, 1950-2015 |
| CFROI, 4-yr r; median | 0.50; 8.5% | energy 0.35, staples 0.78 | Global, market cap about $250M plus, 1983-2015 |
| CFROI, older cut, 4-yr r | 0.38 | | HOLT, 1986-2012 |
| Operating margin beta, 1-yr / 3-yr | 0.173 / 0.158 | materials 0.193 / 0.155; all about 0.11 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Sales growth correlation with US real GDP | 0.55 | industrials 0.74 | Top 1,000 global, 1950-2014 |

Reading: technology returns fade fast, and the operating margin beta is close to materials, so a small sales miss becomes a large earnings miss. Analyst errors are largest in high-beta industries and at peaks and troughs of industrial production (Operating Leverage, 2016). Use the multi-year r, not the one-year, to fade returns, and fade to the sector mean over a full cycle, not to a peak-year figure. Load `references/base-rates.md`.

## Valuation conventions and their pitfalls

- **Normalize to mid-cycle.** Value on mid-cycle revenue, margin and ROIC, "a point on the long-term trend line, not a peak or trough." Weight a normal-cycle scenario against a new-trend scenario and give each an economic reason (demand growth, entry and exit, technology, capacity) (McKinsey ch.35; `references/valuation.md`).
- **Consensus ignores the cycle.** Forecasts for cyclicals trend upward through peaks and troughs, so a forward P/E looks cheap at the peak and expensive at the trough. Market prices behaved like a 50/50 blend of perfect and zero foresight in McKinsey's sample (1985-1997, verify).
- **EV/EBITDA across business models is invalid.** Higher capital intensity gives a lower EV/EBITDA; compare foundries and memory with each other, and use EV/EBIT or EV/NOPAT when fabless and manufacturing peers are mixed (multiples notes 2.4).
- **P/B and EV/invested capital** for memory and capital-heavy names, read next to ROIC (EV/IC = EV/NOPLAT x ROIC).
- **High growth** in a new end market (AI accelerators, judgment): treat with the high-growth method (steady state 10 to 15 years out, addressable market at acceptable returns, scenarios), and test the S-curve and capacity against demand.
- **Operating leverage arithmetic.** In the paper's example a business with 75 percent fixed costs moves from a 20 percent margin to about -40 percent when sales halve and to nearly 60 percent when they rise 2.5 times (Operating Leverage, 2016). Show downside and upside cases with different incremental margins; load `references/operating-leverage-and-tam.md`.

## Questions a specialist asks on the earnings call

1. What are utilization rates by node or factory, and what does each point of utilization do to gross margin?
2. How many weeks of inventory sit at distributors and at the largest customers, and how did that change?
3. How much of the quarter's revenue is price against units, and what is the pricing outlook by product line?
4. What share of orders are pull-ins, cancellations or pushouts?
5. What is the capex plan, how much is committed, and what triggers a cut?
6. How concentrated is revenue, and which design wins start or end in the next four quarters?
7. Were there inventory reserve releases or underutilization charges, and are they in the adjusted figures?
8. What are export controls and tariffs doing to orders by region (verify the current rules)?
9. Where does the company sit on the next process node or product generation against named competitors?

## What to watch at the macro level

- Industrial production and global GDP: sales correlate with both, and forecast errors cluster at turning points.
- End-market unit data: PC, smartphone, server and auto builds; hyperscaler capex for data-center demand (judgment).
- Industry-wide capex announcements and equipment book-to-bill, two years ahead of supply.
- Trade policy: export controls, tariffs, local-content rules and subsidies (verify current rules by country).
- Currency: much production is in Asia and sales are in dollars; read constant-currency figures.
- Interest rates matter less to demand than to the cost of financing large fabs (judgment).

## Financials: banks

This primer covers deposit-taking banks, including their trading and fee businesses. Insurers have their own primer. Asset managers, exchanges and payment networks carry little balance-sheet risk; value them with the standard enterprise methods. Every figure below is historical, illustrative or judgment, never a current fact; check each "(verify)" before use.

## How banks make money and what drives value

A bank earns three kinds of income (McKinsey, Valuation 5th ed., ch. 36, pp. 766-767):

- Net interest income (NII): interest earned on loans and securities minus interest paid on deposits and borrowings. In the 2010 text it was about half of net revenue for retail-focused banks (verify the current mix by bank).
- Fees and commissions: advisory, underwriting, asset management, payments, brokerage. About half of net revenue for investment banks in the same text (verify). Underwriting and advisory fees are cyclical.
- Trading income: volatile; several years of gains can be lost in one year.

Value depends on return on equity (ROE) against the cost of equity, growth of the equity base, and the capital ratio regulators and depositors require (McKinsey ch. 36, p. 782). Leverage magnifies everything: in McKinsey's ABC Bank example (equity 8% of assets), a one-point change in the loan rate moved ROE by about 12 points (p. 780). Funding rests on confidence that "can disappear overnight" (p. 766). For these reasons, value a bank with scenarios, not a point estimate.

Not all NII creates value. A bank that funds long-term loans with short-term deposits earns a maturity-mismatch income that pays for interest-rate risk, not for a lending advantage (pp. 785-789).

## The metrics that matter

| Metric | Definition | Why it matters | Indicative range, large developed-market banks (judgment, verify) |
|---|---|---|---|
| Net interest margin (NIM) | NII / average earning assets | Spread on the balance sheet | about 1.5% to 3.5%; US banks usually above euro-area and Japanese banks |
| Pre-provision net revenue (PPNR) | NII + noninterest income - noninterest expense | Earning power before credit costs | compare across the cycle, not as a level |
| Efficiency ratio | noninterest expense / (NII + noninterest income) | Cost discipline and scale | about 50% to 70% |
| Provision ratio | provision for credit losses / average loans | Management's forward loss estimate | read against charge-offs |
| Net charge-off (NCO) ratio | (gross charge-offs - recoveries) / average loans | Realised losses | through-cycle about 0.3% to 1.0% for a diversified book; cards higher |
| NPL ratio and coverage | NPLs / loans; allowance / NPLs | Asset quality, reserve cushion | trend matters more than level |
| CET1 ratio | common equity tier 1 / risk-weighted assets (RWA) | Binding capital constraint; sets growth and payout capacity | Basel minimum 4.5% plus buffers; large banks often run about 10% to 14% |
| ROTCE | net income to common / average tangible common equity | The return that drives price to tangible book | about 8% to 18% across a cycle |
| Loan-to-deposit ratio | loans / deposits | Funding stability | above about 100% means reliance on wholesale funding |
| Deposit beta | change in deposit cost / change in policy rate | How much of a rate move the bank keeps | rises late in a hiking cycle |

Most of these sit in the earnings release, supplement and capital disclosures, not the tearsheet ratios; get them with `bigdata_search` and `bigdata_fetch_document`.

## What the statements do differently, and the traps

- Interest expense is the cost of goods: EBIT and EBITDA mean nothing, and there is no "net debt" (McKinsey ch. 36, p. 765).
- The cash flow statement mixes loan originations, deposit flows and securities purchases; industrial free cash flow has no meaning. Use the equity cash flow below.
- Provisions are estimates. Expected-loss accounting (CECL in the US, IFRS 9 elsewhere; verify which applies and when it was adopted) front-loads losses. Compare provisions with net charge-offs over several quarters: rising charge-offs with flat provisions point to under-reserving, and reserve releases lift earnings without cash. Under-provisioning reduces equity value because the deficit must be funded; do not deduct the provision a second time in a DCF (McKinsey ch. 36).
- Gains on securities are not earning power (Graham and Dodd, Security Analysis, pp. 417-418). Watch loss reserves and marks on thin-market instruments (Berkowitz, Security Analysis 6th ed., pp. 341-342).
- Securities held to maturity carry unrealised losses outside equity; available-for-sale losses sit in other comprehensive income and, for some banks, outside regulatory capital (verify current rules). This mattered in the 2023 US regional bank failures, which the sources do not cover.
- Banks are opaque: true returns and risks are hard to see from outside (McKinsey ch. 16). The accrual, EBITA and working-capital tests in `earnings-quality.md` do not apply; reconcile earnings to the change in equity.
- Use tangible equity for returns and multiples; acquirers carry goodwill.

## Profit pool and competition

Banks are fragmented when measured globally: 1,114 listed firms, a four-firm revenue concentration of 15.6%, and a top-10 share of industry invested capital that rose from 23% to 32% between 2005 and 2015 (Mauboussin and HOLT, Global Industry Profit Pools, July 2016; verify). National markets are usually far more concentrated (judgment, verify). In that study, the economic spread of commercial banks fell from 0.7 to 0.1 points between 2010 and 2015, while thrifts and mortgage finance recovered from -14.2 to 6.2 points (p. 4). The pool is close to zero on average with wide dispersion, so explain who earns the spread and why.

Banks compete on a low-cost, stable deposit base, scale in technology and payments, underwriting discipline and regulatory capital as a barrier; nonbank lenders and private credit compete for loans (judgment, verify). Regulation limits capital allocation choices: understand the capital rules before judging buybacks or growth (Mauboussin, Capital Allocation, 2015, p. 45). European banks shifted from interest income toward fees and trading between 1988 and 2007, which made ROE and price to book more cyclical (McKinsey Ex. 36.1-36.2).

## Persistence and fade

- The gross profitability, operating margin and operating leverage tables in `base-rates.md` exclude financials and utilities (Base Rate Book, 2016, sections 2.5, 2.6, 2.8). Do not apply them to a bank.
- The CFROI table includes financials, measured by HOLT on cash flow return on equity: four-year r 0.43, median 7.5%, mean 8.3% (global, live and dead, 1983-2015); the older cut gives r 0.43 and mean 6.8% (1986-2012). About 43% of a financial's excess return over the median is left after four years, a faster fade than consumer staples (r 0.78). The financials group in those samples also holds insurers and, before the 2016 GICS change, REITs (judgment, verify).
- The sales and earnings growth tables cover all sectors. Bank "sales" is usually total revenue (NII plus noninterest income; verify the field), and earnings swing with provisions, so state the growth basis.

## Valuation conventions and pitfalls

**Why enterprise multiples and the ROIC build do not apply.** Enterprise value, WACC and ROIC all depend on separating operating assets from financing. A bank's interest income and expense are its operations, so the split cannot be made: EV/EBITDA and an enterprise DCF have no consistent numerator or denominator (McKinsey ch. 36, pp. 765, 777). The return measure is ROE on adjusted net income against the cost of equity: "ROE is to financials as ROIC is to industrials" (Mauboussin and Callahan, Calculating ROIC, 2014, p. 11).

**The alternative, in McKinsey's three parts (ch. 36):**

1. Equity DCF. Cash flow to equity: CFE = net income - increase in book equity + other comprehensive income, which equals dividends + buybacks - issuance. Growth consumes equity: required equity = target capital ratio x RWA. Continuing value: CV = NI(t+1) x (1 - g / RONE) / (ke - g), where RONE is the return on new equity. If RONE equals ROE, value = book equity x (ROE - g) / (ke - g). McKinsey's illustration (ROE 12.8%, ke 10.85%, g 3.5%) gives price to book 1.3 and forward P/E 10.2; use it as a template only.
2. Economic spread, to see where value is created. After-tax spread on loans: SAT = L x (rL - kL) x (1 - T) - TP, with tax penalty TP = T x L x [kL - (1 - eL) x kD], where kL and kD are the matched-maturity market rates for loans and deposits and eL the equity required per unit of loans. In the ABC example only about half of after-tax NII was value created; the rest paid for maturity mismatch and for the required return on equity (pp. 785-789). Forecast margins from forward rates implied by the yield curve, smoothed (pp. 790-791).
3. Multibusiness banks: value lending (spread plus equity DCF), trading (on VaR and return on VaR, cycle-averaged) and fee businesses (assets under management x fee rate) separately, then triangulate with multiples (pp. 794-797).

**Multiples.** Price to tangible book against ROTCE: justified P/B = (ROE - g) / (ke - g); justified P/E = (1 - g / ROE) / (ke - g). At an assumed ke of 10% and g of 3%, ROE of 8%, 10%, 12% and 15% justify about 0.7x, 1.0x, 1.3x and 1.7x book (derived). A premium to book needs ROE above the cost of equity.

**Pitfalls.** Capitalising a peak-cycle ROE: normalise credit costs to through-cycle loss rates by loan category (cards highest, mortgages lowest, correlated with GDP; McKinsey ch. 36). Holding the cost of equity fixed while the capital ratio or asset mix changes (p. 784). Ignoring the tax cost of holding equity (equity x tax rate). Not valuing capital above the target ratio separately. Reading a high NIM as quality when it reflects credit risk or a duration gap.

## Questions a specialist asks on the call

- What deposit beta is assumed in NII guidance, and how has the deposit mix (noninterest-bearing share) moved?
- How much of NII comes from the securities book and swaps repricing, and what is the sensitivity to a parallel and a non-parallel rate shift?
- Why did provisions differ from charge-offs this quarter, and what macro scenario weights sit behind the allowance?
- Which books (commercial real estate, cards, leveraged loans) show rising delinquencies?
- What CET1 target, including management buffer, governs buybacks, and what do pending capital rule changes do to RWA?
- What would marking held-to-maturity securities do to tangible book?

## What to watch at the macro level

The level and slope of the yield curve and the policy-rate path; deposit competition and money-market yields; the credit cycle (unemployment, GDP, commercial property values); capital and stress-test rules (Basel III implementation and national variants; verify the current status); funding confidence after any bank failure; and, for international banks, currency and sovereign exposure. Before extrapolating ROE, check sector profits against GDP: by 2006, financials, energy, utilities and materials made up 51% of S&P 500 earnings, up from 41% (McKinsey ch. 16; verify).

## Sources

McKinsey, Valuation 5th ed. (2010), ch. 16 and 36; Mauboussin and Callahan, Calculating ROIC (2014); Mauboussin, Base Rate Book (2016), Reversion to the Mean (2013), Capital Allocation (2015); Mauboussin and HOLT, Global Industry Profit Pools (2016); Graham and Dodd, Security Analysis 6th ed. (2009). The metric ranges are judgment.

## Industrials

Capital goods (aerospace and defense, machinery, electrical equipment, building products, construction and engineering), transportation (rail, trucking, air freight, airlines, marine) and commercial and professional services. Most of the sector is cyclical: sales follow capital spending, construction, freight volumes and government budgets. Services, defense and aftermarket-heavy businesses are the exceptions.

## How the sector makes money

- Original equipment is sold against orders, often with long lead times; the order book sets revenue one to several years ahead. Price is set at order, cost is incurred at delivery, so inflation between the two compresses margin unless contracts carry escalators.
- The installed base generates aftermarket revenue (parts, service, upgrades) that is less cyclical and usually carries a higher margin than original equipment; a margin gap of roughly 15 to 30 points is a judgment range (verify against segment disclosure).
- Transport earns on volume times yield over a largely fixed network; incremental margins are high when volume returns to a network built for it.
- Value drivers: volume through the cycle, price and mix, aftermarket share of sales, operating leverage on a fixed plant, working capital intensity, and capital intensity. Median real sales growth of industrials correlated about 0.74 with US real GDP growth (top 1,000 global companies, 1950-2014; Mauboussin, Operating Leverage, 2016) (verify), so a macro view is a reasonable starting point for the top line, unlike energy or staples.

## Metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| Orders and book-to-bill | Orders received / revenue recognised in the period | Leads revenue. Readings persistently above 1.0 point to growth, below 1.0 to decline; a single quarter is noise (judgment, verify). Check for pull-forward ahead of price increases. |
| Backlog and backlog / revenue | Unfilled firm orders; backlog / trailing revenue | Visibility; from under one year (short-cycle machinery) to several years (aerospace, defense) (judgment, verify). Read cancellation terms. |
| Organic growth split | Volume, price, mix, ex currency and M&A | Price-only growth with falling volume is weaker than it looks. |
| Aftermarket share of sales | Service and parts revenue / total | Higher share means a less volatile margin. |
| Capacity utilisation | Output / practical capacity | The main link from volume to margin (see operating leverage below). |
| Incremental (decremental) margin | Change in operating profit / change in sales | Tests whether operating leverage is behaving as guided; compare with the contribution margin. |
| Free cash flow conversion | Free cash flow / net income | Countercyclical: working capital absorbs cash in upturns and releases it in downturns. |
| ROIC, with and without goodwill | NOPAT / invested capital | Many industrials are serial acquirers; the two figures can differ widely (load `references/roic.md`). |

Most are not tearsheet fields: take them from filings and transcripts through `bigdata_search`, or state them as assumptions.

## Operating leverage and capacity utilisation

- Split every past margin change into volume, price and mix, operating leverage, economies of scale and cost efficiencies (Mauboussin, Operating Leverage, 2016). Operating leverage is spreading fixed preproduction cost over more units; economies of scale lower unit cost as the firm grows. Mistaking one for the other leads to forecasting falling unit costs while the company is adding capacity.
- Changes in capacity utilisation correlated about 0.6 with changes in operating margin (US, 1967-2015; Base Rate Book, 2016) (verify). Ask for utilisation on calls; if it is not disclosed, infer it from output against stated capacity.
- Fixed-cost arithmetic: in the paper's example, two firms at a 20 percent margin on $10M of sales, one with 75 percent fixed costs and one with 25 percent, reach margins of about 56 and 32 percent at $25M of sales and about -40 and 0 percent at $5M (Operating Leverage, 2016, Exhibit 2). Operating leverage is symmetric: forecast a downside and an upside with different incremental margins, never a linear margin path.
- Debt, leases and pension deficits add financial leverage on top. Flag firms with both high operating and high financial leverage as the highest earnings risk.
- S-curve warning: capacity built by extrapolating the steep middle of a demand curve overshoots (colour TV capacity reached 14 million units against peak sales of 6 million; Operating Leverage, 2016). Test any announced capacity build-out against a demand peak, not the current growth rate.

## Mid-cycle normalisation

Normalise margins and returns to mid-cycle before any multiple or terminal value. Mid-cycle is a point on the long-run trend line, not a peak or a trough (McKinsey, Valuation, 5th ed., 2010, ch. 35).

1. Take operating margin and ROIC over at least one full cycle, covering a trough and a peak; the profit-pool work uses three to five years as a minimum (Global Industry Profit Pools, 2016), and seven to ten years is safer for long-cycle businesses (judgment, verify).
2. Adjust for structural change: divestments, acquisitions, aftermarket mix, restructuring that has lowered the fixed-cost base.
3. Cross-check the result against the sector mean in the fade tables below.
4. Build two scenarios: a normal-cycle case with continuing value on mid-cycle profit and ROIC, and a new-trend case extrapolating recent performance, each with its economic rationale (demand, capacity, entrants, technology). Weight them with probabilities that sum to 100.

The reason: with perfect foresight, DCF values of cyclicals are nearly flat while cash flows swing widely, and consensus EPS for cyclicals has historically trended upward through peaks and troughs (36 US cyclicals, 1985-1997; McKinsey ch. 35) (verify). A forward P/E at the peak looks cheap and at the trough looks expensive.

## Financial statements and accounting traps

- Percentage-of-completion and program accounting (aerospace, defense, engineering): margins rest on estimates of total program cost. Read cumulative catch-up adjustments; repeated negative catch-ups or forward-loss provisions show estimation bias.
- Customer advances and progress payments fund working capital. They lower invested capital and raise ROIC, which is part of why aerospace and defense ROIC trended up (McKinsey, ch. 2-4, 1965-2007 data) (verify). A fall in advances is a cash outflow that can look like a working capital problem.
- Pensions: replace reported pension cost with service cost only and remove the expected return on plan assets from operating profit; treat the unfunded deficit after tax as debt (McKinsey ch. 27). Legacy industrials can carry large deficits.
- Restructuring charges that recur in most years are operating costs. Count how many of the last five years carry one.
- Acquired-intangible amortisation: compare acquisitive firms on EBITA, and report ROIC with and without goodwill.
- Model working capital as a share of incremental revenue; it outgrows revenue in upturns.

## Profit pool and competitive dynamics

- Machinery and construction and engineering are fragmented: four-firm revenue concentration of about 13.6 and 13.8 percent, more than 1,100 and about 800 listed firms; aerospace and defense sat near the 40 percent line at 38.2 percent; air freight and couriers (53.8 percent) and industrial conglomerates (51.9 percent) were concentrated (Global Industry Profit Pools, HOLT, data to June 2016) (verify).
- Top-10 share of industry invested capital fell in electrical equipment (47 to 34 percent), trading companies and distributors (52 to 41) and industrial conglomerates (58 to 42), and rose in airlines (34 to 47), over 2005-2015 (same source) (verify).
- Machinery's economic spread fell from about 1.7 to 1.0 points over 2010-2015 (same source) (verify). Airlines destroyed value in aggregate, on the order of $19bn a year over 2002-2009 (Measuring the Moat, 2013) (verify).
- Rivalry rises when demand is volatile and fixed costs are high: capacity is added at the peak and fought over in the trough (Measuring the Moat, 2013). Build the profit pool for the subindustry, not the sector (load `references/industry-structure.md`).

## Persistence and fade

Label: historical base rate, top 1,000 global companies ex-financials and utilities, 1950-2015 (CFROI: global, about $250M market cap and above, 1983-2015). Not a forecast and not a current fact (Base Rate Book, 2016) (verify). Tables in `references/base-rates.md` (Tables 7 to 10).

| Measure | Industrials | All-sector context |
|---|---|---|
| Operating margin, 5-yr r; median; mean | 0.72; 9%; 11% | r ranges 0.62 (energy, materials, IT) to 0.89 (staples) |
| Gross profitability, 5-yr r; median | 0.79; 0.28 | |
| CFROI, 4-yr r; median; mean | 0.62; 6.7%; 7.6% | Middle of the ranking; older cut 0.52, 1986-2012 |
| Operating margin beta, 1-yr / 3-yr | 0.083 / 0.076 | Low; materials highest at 0.19 / 0.16 |

Read: about 62 percent of an industrial's excess CFROI over the sector mean has historically remained after four years. Fade with expected = mean + r x (current - mean), using the horizon-matched r and the mid-cycle mean. The low margin beta is an average across subsectors; short-cycle machinery and transport run well above it, so compute the company's own beta over five to ten years.

## Valuation conventions and pitfalls

- EV/EBITDA works only across peers with similar capital intensity; use EV/EBIT where depreciation burdens differ (UBS, multiples, 2017). Apply any multiple to mid-cycle, cleaned earnings.
- Compare a multiple with the company's own history only at a comparable point of the cycle.
- For capital-intensive subsectors without a strong franchise, a terminal spread near zero is the default; a positive terminal spread needs moat evidence (UBS, 2017).
- Sum-of-the-parts for conglomerates: value each segment on its own drivers; state the evidence for any spin-off or separation before crediting the gap.
- Credit a backlog or aftermarket premium only with evidence of lower margin volatility or higher cash conversion.
- Load `references/valuation.md` and `references/multiples-and-peers.md` for the method.

## Questions for the earnings call

1. What were orders and book-to-bill by segment, and how much was pull-forward ahead of price increases?
2. How much of organic growth was price, and how much volume? What is the price-cost spread now and next year?
3. What is capacity utilisation, and at what level do you add capacity?
4. What incremental margin should volume growth carry, and what decremental margin if volume falls?
5. What share of backlog is fixed price, and how are escalators and cancellation terms written?
6. What were the cumulative catch-up adjustments on long-term programs?
7. How much of the restructuring charge recurs next year?
8. How are aftermarket volumes trending against the installed base?

## What to watch at the macro level

Industrial production and purchasing-manager surveys, capital-goods orders, nonresidential construction, freight volumes and rates, defense outlays (not authorisations), air traffic, metal input costs, interest rates and currency. Analyst forecast errors have historically been largest at peaks and troughs of industrial production (Operating Leverage, 2016) (verify), so widen ranges at turning points.

## Consumer and retail

Retailers (broadline, specialty, grocery, off-price, e-commerce), restaurants, branded consumer goods (apparel, durables, food, beverages, household and personal products) and consumer services. The sector spans two GICS sectors with different behaviour: consumer discretionary sales track the economy closely, consumer staples barely do. Say which one a company belongs to before using any base rate.

## How the sector makes money

- Retailers earn a thin margin on fast-turning inventory and a large, mostly leased store or fulfilment base. Brands earn a wide gross margin and spend heavily on advertising, promotion and distribution.
- ROIC = NOPAT / sales x sales / invested capital. A low-cost retailer can earn 20 percent at a 4 percent margin with 5x capital turnover; a luxury seller earns the same at 20 percent and 1x (Mauboussin and Callahan, Calculating ROIC, 2014; illustrative). Cost leadership shows up in turnover, differentiation in margin. Know which one the company claims before judging a margin change.
- Revenue = revenue per store x stores. Comparable-store growth needs little capital and lifts ROIC; new-store growth needs capex and creates value only if the new stores earn above the cost of capital (McKinsey, Valuation, 5th ed., 2010, ch. 8). Lowe's held revenue flat in 2008 by opening 115 stores while revenue per store fell (verify).
- For a low-ROIC retailer, one point of ROIC was worth about 15 percent of value against about 5 percent for one point of growth; for a high-ROIC consumer-goods company the order reverses (McKinsey ch. 2, stylised, 2010) (verify). Returns matter more than growth for most retailers.
- Value drivers: traffic, ticket and mix; gross margin net of markdowns and shrink; occupancy and labour leverage; inventory turnover; store or unit economics; brand pricing power.

## Metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| Comparable sales | Sales growth at stores or channels open a full year, under the company's own definition | Isolates organic demand. Check the definition (e-commerce included or not, closure treatment, 53rd week). |
| Traffic and ticket | Transactions; average transaction value | Ticket-driven comps with falling traffic often mask share loss; traffic-driven comps are stronger. |
| Price, volume and mix (brands) | Organic growth split | Price-led growth with volume decline tests elasticity. The average price elasticity across about 370 goods was about 1.76 (Tellis meta-analysis, 1998) (verify); staples are usually less elastic, discretionary categories more. |
| Gross margin and markdowns | Gross profit / sales; clearance activity | Inventory growing faster than sales for two or more quarters has often preceded markdowns (judgment, verify). |
| Inventory turnover, GMROI | COGS / average inventory; gross margin / average inventory at cost | Turnover ranges from more than 10x in grocery to under 3x in furniture and luxury (judgment, verify); compare within format only. |
| Sales per square foot, unit volumes | Sales / selling area; average unit volume for restaurants | Productivity of the fixed base; falling productivity alongside unit growth suggests over-expansion. |
| New-unit economics | Cash-on-cash return or payback per new store | Tests whether unit growth creates value; new units often open below mature productivity and cannibalise (judgment, verify). |
| Channel economics | Margin by store, e-commerce, wholesale, direct-to-consumer | Direct-to-consumer gross margin is higher than wholesale, but fulfilment, returns and paid acquisition can leave operating margin lower (judgment, verify). |

Most are not tearsheet fields: take them from filings, transcripts and investor-day material through `bigdata_search`.

## Financial statements and accounting traps

- Leases. Under IFRS 16 and ASC 842 most store leases sit on the balance sheet, but EBITDA under IFRS excludes rent while US GAAP operating-lease cost stays in operating expense. Make EV and the earnings measure consistent (both include lease liabilities and exclude rent, or neither). In older data, capitalising leases cut US retail ROIC from about 19.7 to 11.0 percent and restaurants from about 14.6 to 10.6 percent (Damodaran, 2007, US 2006 data) (verify), and Starbucks' ROIC spread from about 15.1 to 5.4 points. The "8 times rent" shortcut works only near a 6 percent cost of debt and a 15-year life (McKinsey ch. 27).
- Coverage: use EBITDAR / (interest + rent) for retailers (McKinsey ch. 8).
- Vendor allowances, supplier-finance programs and extended payables flatter working capital and gross margin; check the payables days trend.
- Gift cards and loyalty programs create deferred revenue; breakage income can be a material and adjustable source of profit.
- Inventory method: LIFO reserves, retail-method write-downs and reserve releases move margin; compare peers on the same basis (Security Analysis, 6th ed., 2009, ch. 32: U.S. Rubber against Goodyear) (verify).
- Calendar: 53-week years, shifted holidays and fiscal year-ends in late January distort year-on-year comparisons.
- Franchise models: system sales are not revenue; refranchising lifts margin and ROIC while shrinking revenue.

## Profit pool and competitive dynamics

- Household products (four-firm revenue concentration about 65.5 percent), personal products (56.3) and tobacco (71.8) were concentrated; textiles and apparel (18.9), hotels, restaurants and leisure (15.5), food products (20.0) and auto components (18.0) were fragmented; internet and catalog retail was near the 40 percent line at 38.5, with the top-10 share of invested capital rising from 58 to 72 percent over 2005-2015 (Global Industry Profit Pools, HOLT, data to June 2016) (verify).
- Concentration measured by HHI: breakfast cereal about 2,425, snack food 1,984, tires 1,540, apparel 44 (Measuring the Moat, 2013, 2007 Census data) (verify). Readings above 1,800 suggest reduced rivalry.
- Department stores had a low median ROIC (about 9 percent, US, 1965-2007) and persistently low growth; household and personal products and beverages had persistently high ROIC (McKinsey ch. 4) (verify).
- Mix can outweigh volume: Goodyear's sales fell 28 percent and volume 8 percent over 2011-2015, yet operating income rose almost 50 percent and margin about 6 points from a shift to premium tires (Operating Leverage, 2016) (verify). Split every margin change into price, mix and volume.
- Scale economies are distinct from operating leverage: Home Depot's gross margin rose from 27.7 to 29.9 percent over FY1996-FY2001 on better supplier terms (Operating Leverage, 2016) (verify).
- Retailers whose business rests on image can be damaged irreversibly in distress (Klarman, Margin of Safety); weigh balance-sheet risk more heavily here than in capital-intensive sectors.

## Persistence and fade

Label: historical base rate, top 1,000 global companies ex-financials and utilities, 1950-2015 (CFROI: global, about $250M market cap and above, 1983-2015). Not a forecast and not a current fact (Base Rate Book, 2016) (verify). Tables in `references/base-rates.md` (Tables 7 to 10).

| Measure | Consumer staples | Consumer discretionary |
|---|---|---|
| Operating margin, 5-yr r; median; mean | 0.89; 9%; 11% | 0.73; 10%; 11% |
| Gross profitability, 5-yr r; median | 0.86; 0.49 | 0.77; 0.35 |
| CFROI, 4-yr r; median; mean | 0.78; 8.1%; 9.3% | 0.67; 8.0%; 9.1% |
| Operating margin beta, 1-yr / 3-yr | 0.075 / 0.071 | 0.081 / 0.074 |
| Sales growth correlation with US real GDP (1950-2014) | 0.37 | 0.77 |

Read: staples fade slowest of all sectors (78 percent of the excess CFROI spread has remained after four years), discretionary next. Sector means have small dispersion, so fade toward the sector mean rather than a mid-cycle estimate (Base Rate Book, Part 3). Discretionary sales are the most GDP-sensitive of any sector; for housing-linked, durable and big-ticket categories, normalise sales and margin to a mid-cycle level before applying a multiple.

## Valuation conventions and pitfalls

- P/E for staples and mature brands with comparable capital structures; EV/EBIT or lease-consistent EV/EBITDA (or EV/EBITDAR with leases in EV) across retailers with different lease intensity (UBS, multiples, 2017).
- Pair every multiple with ROIC and growth; a cheap-looking retailer often has low ROIC after leases. State how peers were chosen and show the multiple with and without high-multiple outliers (How Well Do You Compare, 2017).
- Price unit growth through store-level returns, not through a growth premium.
- Owned real estate is a separate asset: value it outside the operating multiple and remove the rent it would carry.
- Do not apply e-commerce or direct-to-consumer multiples without segment-level profitability.
- Load `references/valuation.md` and `references/multiples-and-peers.md`.

## Questions for the earnings call

1. How did comparable sales split between traffic and ticket, and between price and mix?
2. How much of gross margin change came from markdowns, freight, shrink and mix?
3. Is inventory per store growing faster than sales, and how much is aged?
4. What are payback and productivity of the last two years' new stores against the mature base?
5. What is the operating margin of the e-commerce or direct-to-consumer channel after fulfilment and returns?
6. How did price elasticity respond to the last price increase, and how is private label share moving?
7. How much of the year's margin depends on supplier terms or vendor funding?

## What to watch at the macro level

Real disposable income and wage growth, consumer credit and delinquency, savings rate, consumer confidence, housing turnover (for durables and home), gasoline prices, tariffs and freight costs for importers, input commodities (grains, cotton, packaging), and currency. Staples respond more to input costs and pricing than to GDP; discretionary responds to GDP and credit.

## Energy

Upstream exploration and production (E&P), integrated oil and gas, oilfield services and equipment (OFS), midstream pipelines, processing and storage, refining and marketing, and coal. Renewable developers and utilities-like power producers often sit elsewhere in GICS, but the transition questions below apply to them. Energy is the most cyclical sector by return persistence: earnings follow commodity prices that no company controls.

## How the sector makes money

- Upstream: revenue = production x realised price. Cost is lifting cost plus the capital to replace declining production. Value comes from the reserve base, its cost position and the reinvestment needed to hold output flat.
- OFS: revenue = activity (rigs, wells, fleet days) x pricing; activity follows producers' capital budgets with a lag of roughly two to four quarters (judgment, verify).
- Midstream: fee or cost-of-service income on volumes; commodity exposure depends on contract type (fee-based, percent-of-proceeds, keep-whole).
- Refining: margin = product prices minus crude cost (the crack spread) x throughput x capture rate.
- Value drivers: the commodity price deck, production growth and decline, unit cost and its position on the industry cost curve, reinvestment rate, reserve life and replacement, and capital discipline through the cycle.
- Median real sales growth of energy companies correlated only about 0.12 with US real GDP growth (top 1,000 global, 1950-2014; Operating Leverage, 2016) (verify). Price, not GDP, drives the top line; a macro sales model is weak here.

## Metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| Production and decline rate | Output per day; base decline without new wells | Sets maintenance capex. Shale wells decline faster than conventional fields (verify by basin). |
| Realised price and differentials | Price received against the benchmark | Basis and quality discounts move margin independent of the headline price. |
| Unit costs | Lifting, transport, G&A per unit; full-cycle cost including finding and development | Cost-curve position decides who earns a return at mid-cycle prices. |
| Reserve replacement and reserve life | Reserves added / production; proved reserves / annual production | Below 100 percent replacement for several years means the base is shrinking. |
| Reinvestment rate | Capex / operating cash flow | Separates growth from maintenance. |
| Breakeven price | Price at which free cash flow, or the dividend, is covered | Company-defined; check what it includes. |
| Crack spread and capture rate | Benchmark refining margin; realised / benchmark | Refining earnings are a spread business. |
| Utilisation | Refinery throughput / capacity; OFS fleet or rig utilisation | The volume-to-margin link (below). |
| Contract mix and tenor (midstream) | Fee-based share; weighted remaining term | Determines how much of the cycle reaches cash flow. |
| Distribution or dividend coverage | Distributable cash flow / payouts | Payout sustainability through a trough. |

Most are not tearsheet fields: take them from filings, reserve reports and transcripts through `bigdata_search`.

## Operating leverage and capacity utilisation

- Energy has the highest fixed-asset intensity of any sector (Damodaran data, global, January 2015; Operating Leverage, 2016) (verify). Operating margin beta was 0.134 at one year and 0.103 at three (Base Rate Book, 2016) (verify), and analyst forecast errors are largest where beta is high (Operating Leverage, 2016).
- Changes in capacity utilisation correlated about 0.6 with changes in operating margin (US, 1967-2015; Base Rate Book, 2016) (verify). In refining and OFS, utilisation and pricing move together: a tight fleet raises day rates and margins at the same time, which is why OFS margins swing more than producers'.
- Split every margin change into price, volume, mix and cost. A margin recovery from price alone reverses with the price.
- Supply drives the cycle: capacity is added at high returns, arrives in large increments, and returns fall about two years later (commodity chemicals case, McKinsey, Valuation, 5th ed., 2010, ch. 35) (verify). In energy, watch sanctioned projects and rig counts for the same pattern.
- S-curve warning: capacity built on mid-curve demand growth overshoots (colour TV capacity 14 million units against peak sales of 6 million; Operating Leverage, 2016). Apply it to LNG, refining and transition build-outs.

## Mid-cycle normalisation

Normalise margins and returns to mid-cycle before any multiple or terminal value. A mid-cycle commodity price is a judgment: anchor it on the cost curve (the full-cycle cost of the marginal supplier), the futures strip beyond the first two years, and a long-run real average, and state the deck used (judgment, verify).

1. Rebuild earnings at the mid-cycle price deck and mid-cycle crack spread, not the spot.
2. Check the resulting ROIC against the sector mean below.
3. Build a normal-cycle case on mid-cycle profit and ROIC and a new-trend case that assumes the current price persists, each with its supply and demand reasoning, and weight them with probabilities that sum to 100 (McKinsey ch. 35).
4. Show sensitivity of value to the commodity price in a table; one price is not a forecast.

The reason: consensus EPS for cyclicals has historically trended upward and ignored the cycle at peaks and troughs (36 US cyclicals, 1985-1997; McKinsey ch. 35) (verify). Market prices of cyclicals were best matched by a 50/50 blend of perfect and zero foresight, so prices anchor on current earnings more than they should.

## Financial statements and accounting traps

- Successful-efforts against full-cost accounting: full-cost capitalises dry holes and smooths earnings; compare peers on cash flow or restate (general knowledge, verify the method in each filing).
- Impairments and ceiling tests follow the price deck; a write-down lowers future depreciation and flatters later margins (Security Analysis, 6th ed., 2009, ch. 34: write-downs used to cut depreciation).
- Reserves are estimates under regulatory price rules (US SEC: trailing average prices); standardized-measure values move with price, not only with geology (verify current rules).
- Hedging gains and losses can sit in or out of operating income; separate realised from unrealised.
- Asset retirement obligations are debt-like; include them in the equity bridge.
- Inventory holding gains in a rising price market inflate refining and marketing earnings; FIFO against LIFO matters (Security Analysis: boom-year inventory profits are low quality).
- EBITDAX excludes exploration expense; treat recurring exploration as an operating cost.
- Check depletion life against reserve life (Security Analysis: Alaska Juneau depletion implied 85 years against 25 claimed).

## Profit pool and competitive dynamics

- Top-10 share of oil and gas invested capital fell from about 47 to 37 percent over 2005-2015 (Global Industry Profit Pools, HOLT, data to June 2016) (verify): the industry fragmented in the shale era.
- Oil and gas sits with chemicals, semiconductors and metals in the cyclical ROIC group; commodity businesses had a median ROIC of about 5.8 percent (US, 1965-2007; McKinsey ch. 4) (verify).
- Industry does not define destiny: low-cost producers earn a positive spread at mid-cycle prices while high-cost producers destroy value (Profit Pools, 2016). Map who holds the low-cost reserves.
- National oil companies and cartel policy set much of marginal supply; treat their decisions as a scenario variable, not a forecast.
- Transition: unit costs of solar and batteries have fallen with cumulative production (Wright's law), with a floor set by material costs and with policy-driven demand behind much of the volume (Coming Clean with Energy Cost Curves, 2017) (verify). Project cost from cumulative deployment with a range and a floor.

## Persistence and fade

Label: historical base rate, top 1,000 global companies ex-financials and utilities, 1950-2015 (CFROI: global, about $250M market cap and above, 1983-2015). Not a forecast and not a current fact (Base Rate Book, 2016) (verify). Tables in `references/base-rates.md` (Tables 7 to 10).

| Measure | Energy | Context |
|---|---|---|
| CFROI, 4-yr r; median; mean; CoV | 0.35; 5.0%; 4.9%; 0.34 | Fastest fade and most unstable mean of all sectors; older cut r 0.36, 1986-2012 |
| Operating margin, 5-yr r; median; mean; CoV | 0.62; 14%; 17%; 0.24 | Among the least persistent |
| Gross profitability, 5-yr r; median | 0.61; 0.22 | 68 percent band for r about 0.43 to 0.79 |
| Operating margin beta, 1-yr / 3-yr | 0.134 / 0.103 | Above the 0.11 all-sector average |

Read: only about 35 percent of excess CFROI has historically remained after four years. Because the sector mean itself is volatile, fade toward a mid-cycle mean, not the latest year's sector average (Base Rate Book, Part 3).

## Valuation conventions and pitfalls

- E&P: net asset value from risked reserves (proved developed producing, then undeveloped and probable at higher risk discounts), with the price deck and risking stated; EV/EBITDAX and EV per flowing barrel as cross-checks (judgment, verify).
- Undeveloped reserves and staged projects carry option value; use a decision tree with judgmental inputs. Short-term volatility misleads for long-dated options on mean-reverting commodities such as oil (McKinsey ch. 32).
- Midstream: EV/EBITDA and distributable cash flow yield, adjusted for contract quality and leverage.
- Refining and OFS: mid-cycle EV/EBITDA; never peak.
- EV per unit of capacity against replacement cost is a useful cross-check (rigs: replacement value about $35 against a price of $15 in one case, Security Analysis, 6th ed.) (verify), but it says nothing about profitability. Fair value per unit = sustainable NOPLAT per unit x (1 - g / ROIC) / (WACC - g) (UBS, multiples, 2017).
- For capital-intensive commodity producers, a terminal spread near zero is the default; steady-state P/E = 1 / cost of equity (UBS, 2017).
- Load `references/valuation.md` and `references/multiples-and-peers.md`.

## Questions for the earnings call

1. What price deck underlies the capital budget and the reserve report?
2. What is the base decline rate and the maintenance capex to hold production flat?
3. How did unit costs move, separated into inflation, efficiency and mix?
4. What share of production is hedged, at what prices, for how long?
5. What is the free cash flow and dividend breakeven, and what does it include?
6. (OFS) What are utilisation and net pricing, and what do customers' budgets imply for next year?
7. (Refining) What was the capture rate against the benchmark crack, and why?
8. (Midstream) What share of cash flow is fee-based, and which contracts reprice in the next two years?

## What to watch at the macro level

Oil and gas balances (inventories, spare capacity, producer-group policy), the futures curve, rig and frac counts, refinery utilisation and product inventories, regional gas and LNG prices, the US dollar, interest rates for capital-heavy projects, and energy policy and subsidies. Treat any current price as a scenario input, never as a forecast.

## Materials

Chemicals (commodity and specialty), metals and mining (steel, aluminium, copper, iron ore, precious metals), construction materials (cement, aggregates), containers and packaging, and paper and forest products. Commodity producers are price takers whose returns follow industry capacity; specialty and local-market businesses (specialty chemicals, aggregates, some packaging) behave more like industrials. Classify the company on that axis first.

## How the sector makes money

- Commodity producers: margin = market price minus unit cash cost, times volume. Position on the industry cost curve decides who earns a return at mid-cycle prices; the lowest-cost quartile earns through the cycle, the highest-cost quartile only near the peak (judgment, verify against a cost curve).
- Specialty producers: margin from formulation, service and switching costs; price is set against customer value, not raw-material cost, and passes through input changes with a lag.
- Local-market businesses: cement and aggregates are heavy and costly to transport, so competition is regional; a quarry or plant near a growing market can hold price.
- Value drivers: the price deck, cost-curve position, volume and utilisation, input costs (energy, feedstock, ore), reserve life and grade (mining), capital discipline and the timing of capacity additions.
- Median real sales growth of materials companies correlated about 0.53 with US real GDP growth (top 1,000 global, 1950-2014; Operating Leverage, 2016) (verify). Industrial production and China construction usually explain more than headline GDP (judgment, verify).

## Metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| Realised price against benchmark | Price received / index price | Grade, quality and contract lags move margin. |
| Unit cash cost and cost-curve position | Cash cost per tonne or unit; quartile on the industry curve | Determines survival at trough prices. |
| Spread | Product price minus feedstock cost (for example, ethylene against ethane or naphtha) | Commodity chemical earnings are a spread business. |
| Utilisation | Output / nameplate capacity, company and industry | The volume-to-margin link (below). |
| Volume, price, mix split | Organic change decomposed | Price-led margin gains reverse with price. |
| Reserve life, grade, strip ratio (mining) | Reserves / annual output; metal content; waste moved per tonne | Grade decline raises unit cost even at constant output. |
| Sustaining against growth capex | Capex to hold capacity / capex to add it | Separates free cash flow from reinvestment. |
| Energy intensity | Energy cost / total cost | Aluminium, cement, fertiliser and chlor-alkali are exposed to power and gas prices. |

Most are not tearsheet fields: take them from filings, reserve statements and transcripts through `bigdata_search`.

## Operating leverage and capacity utilisation

- Materials had the highest operating margin beta of any sector: 0.193 at one year and 0.155 at three, against 0.11 for all sectors (Base Rate Book, 2016) (verify). Analyst forecast errors are larger where beta is high, metals against food in the paper's own comparison (Operating Leverage, 2016). Widen ranges accordingly.
- Changes in capacity utilisation correlated about 0.6 with changes in operating margin (US, 1967-2015; Base Rate Book, 2016) (verify). Ask for utilisation and industry operating rates on every call.
- Fixed-cost arithmetic: in the paper's example, a firm with 75 percent fixed costs at a 20 percent margin reaches about 56 percent at 2.5x the sales and about -40 percent at half (Operating Leverage, 2016, Exhibit 2). Forecast downside and upside with different incremental margins.
- Supply drives the cycle: commodity chemical producers invest when ROIC is high, capacity arrives in large increments, and utilisation and ROIC fall about two years later (McKinsey, Valuation, 5th ed., 2010, ch. 35) (verify). In the book's simulation the IRR was about 4 percent for typical spending, 9 percent for optimally timed capex and 34 percent for optimally timed asset purchases (verify). Capital timing matters more than operations in this sector.
- S-curve warning: capacity built on mid-curve demand growth overshoots (colour TV capacity 14 million units against peak sales of 6 million; Operating Leverage, 2016). Test announced capacity against a demand peak.

## Mid-cycle normalisation

Normalise margins and returns to mid-cycle before any multiple or terminal value (McKinsey ch. 35). Mid-cycle is a point on the long-run trend line, not a peak or a trough.

1. Set a mid-cycle price deck from the cost curve (the cash cost of the marginal producer plus a return on sustaining capital), the long-dated futures where they exist, and a long-run real average; state it (judgment, verify).
2. Rebuild margin and ROIC at that deck and at mid-cycle utilisation, after structural changes (closures, mix toward specialty).
3. Cross-check against the sector mean below and the company's own returns over decades: U.S. Steel's return on average capital was 8.1, 9.6 and 5.2 percent in successive decades (Security Analysis, 6th ed., 2009) (verify), and a ten-year average was a better guide than any single year.
4. Weight a normal-cycle case against a new-trend case, each with supply and demand reasoning, with probabilities that sum to 100.

The reason: consensus EPS for cyclicals has historically trended upward through peaks and troughs (36 US cyclicals, 1985-1997, including primary metals; McKinsey ch. 35) (verify), so a peak-earnings P/E looks cheap.

## Financial statements and accounting traps

- Inventory holding gains and LIFO against FIFO: in rising price markets, inventory profits inflate earnings and are low quality (Security Analysis: 1919-20 industrials) (verify). Compare peers on the same inventory basis.
- Impairments reset the asset base and lower future depreciation; write-downs used to cut depreciation flatter later returns (Security Analysis, ch. 34). Report ROIC before and after.
- Depreciation and depletion adequacy: compare depreciation to the property base and to sales across peers; check depletion life against reserve life.
- Pensions: remove expected return on plan assets from operating profit. DuPont's 2007 adjustment cut EBITA by $455M and margin from 14.3 to 12.8 percent (McKinsey ch. 27) (verify).
- Environmental, reclamation and asset retirement obligations are debt-like.
- Provisional pricing in copper and other concentrates marks revenue to later prices; separate it from operating performance.
- Equity-accounted joint ventures are common in mining and chemicals; value them outside the operating multiple (UBS, multiples, 2017).

## Profit pool and competitive dynamics

- Metals and mining (1,481 listed firms, four-firm revenue concentration about 8.2 percent) and chemicals (1,048 firms, 14.3 percent) were among the most fragmented industries; the top-10 share of chemicals invested capital was about 23 percent (Global Industry Profit Pools, HOLT, data to June 2016) (verify).
- Commodities had a median ROIC of about 5.8 percent and paper and forest products a persistently low one; chemicals and metals and mining were classed as cyclical (US, 1965-2007; McKinsey ch. 4) (verify).
- Industry does not define destiny: low-cost producers earn a positive spread through the cycle while others destroy value (Profit Pools, 2016). Build the profit pool for the subindustry over three to five years at least.
- Resource uniqueness is a real advantage (Alcoa's bauxite) and so is local scale (aggregates); a moat claim for a commodity producer needs one of these (Measuring the Moat, 2013).
- Low-end disruption: mini-mills displaced integrated steel mills from the bottom of the market (Measuring the Moat, 2013).
- Replacement cost limits returns: when market values implied aluminium fabricating capacity above its replacement cost of about $1,000 per tonne a year, overbuilding followed (Security Analysis, 6th ed., Greenwald essay) (verify).

## Persistence and fade

Label: historical base rate, top 1,000 global companies ex-financials and utilities, 1950-2015 (CFROI: global, about $250M market cap and above, 1983-2015). Not a forecast and not a current fact (Base Rate Book, 2016) (verify). Tables in `references/base-rates.md` (Tables 7 to 10).

| Measure | Materials | Context |
|---|---|---|
| CFROI, 4-yr r; median; mean | 0.41; 4.6%; 4.7% | Second-fastest fade after energy; older cut r 0.44, mean 4.1%, 1986-2012 |
| Operating margin, 5-yr r; median; mean; CoV | 0.62; 11%; 13%; 0.25 | Highest CoV of sector mean margins |
| Gross profitability, 5-yr r; median | 0.76; 0.25 | |
| Operating margin beta, 1-yr / 3-yr | 0.193 / 0.155 | Highest of all sectors |

Read: about 41 percent of excess CFROI has historically remained after four years. The sector mean is cyclical, so fade toward a mid-cycle mean rather than the latest sector average (Base Rate Book, Part 3).

## Valuation conventions and pitfalls

- EV/EBITDA on mid-cycle EBITDA within peers of similar capital intensity; EV/EBIT where depreciation burdens differ (UBS, 2017).
- Mining: net asset value from mine-by-mine DCF at a stated price deck, with price sensitivity. Undeveloped deposits carry option value: in McKinsey's mining example a project with standard NPV of -9.1 had a real-option value of 19.5 (ch. 32) (verify). Use option methods only where value and volatility of the underlying are reliable.
- EV per unit of capacity against replacement cost: fair value per unit = sustainable NOPLAT per unit x (1 - g / ROIC) / (WACC - g). Cement example: $10 a tonne of NOPLAT, 12 percent return on capital, 3 percent growth and a 10 percent required return give up to about $107 a tonne (UBS, multiples, 2017) (verify). The multiple alone says nothing about profitability.
- For commodity producers without a cost or resource advantage, a terminal spread near zero is the default; steady-state P/E = 1 / cost of equity (UBS, 2017).
- P/B is useful only next to ROE, and book value after impairments is not replacement cost.
- Load `references/valuation.md` and `references/multiples-and-peers.md`.

## Questions for the earnings call

1. What were utilisation and industry operating rates, and what capacity is coming on across the industry in the next two years?
2. How did margin change split between price, volume, mix, input costs and efficiency?
3. Where does the company sit on the cost curve, and what moved unit cost?
4. What is sustaining capex, and what returns are expected on growth projects at a mid-cycle deck?
5. How much of the price change passes through to customers, and with what lag?
6. (Mining) How are grade, strip ratio and reserve life trending?
7. What would the company do with capital at the trough: buy assets, buy back stock, or cut?

## What to watch at the macro level

Industrial production and construction activity, especially China property and infrastructure; global steel, aluminium and chemical capacity additions and closures; energy and feedstock prices; freight; the US dollar; trade policy and tariffs on metals; and environmental regulation that raises cost or closes capacity. Treat any current price as a scenario input, never as a forecast.

## Communication services

Scope: telecom carriers (wireless, fixed line, cable and fiber), towers and other network infrastructure owned by carriers, media and entertainment (content, broadcasting, publishing, games), and interactive media (search, social, online advertising platforms). These businesses share little beyond the GICS label: carriers are capital-heavy utilities with competition, media are content portfolios, and interactive media are high-margin network businesses. Analyze the company by its own model. A figure marked "(verify)" is a judgment or dated: check it against the peer set and period before use.

## How the sector makes money and the value drivers

- **Carriers:** subscribers x revenue per user (ARPU), minus churn, on a network whose cost is mostly fixed. Value comes from pricing discipline in a concentrated market, network quality, the cost of spectrum and capex, and leverage. Growth tracks population and price; few carriers grow faster than nominal GDP for long (judgment, verify).
- **Media:** content spending (an investment, often expensed or amortized fast) earns advertising, subscription, licensing and box-office revenue over several years. Value comes from the hit rate, the library's reuse value and distribution reach.
- **Interactive media:** users x engagement x monetization per unit of engagement (ad load, price per ad). Network effects, data and low marginal cost drive returns; the main costs are engineering, data centers and payments to traffic partners.

## The metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| ARPU (carriers), ARPU or revenue per user (platforms) | Service revenue / average users or lines | Price and mix; separate price rises from mix shifts |
| Churn | Users or lines lost in the period / average base | Cost of standing still; small changes compound |
| Net adds | Gross adds - disconnections | Share gain or loss |
| Capex intensity | Capex / revenue | Separates cash generation from EBITDA |
| EBITDA - capex (operating FCF) | EBITDA less capex, before interest and tax | The cash a carrier can pay out or use to reduce debt |
| Net debt / EBITDA | Leverage, including leases where relevant | Dividend safety and rating headroom |
| Content cash spend against amortization | Cash paid for content / content amortization in the P&L | A ratio above 1 means earnings run ahead of cash |
| Daily or monthly active users, engagement | Unique users and time spent | Leading indicator for ad revenue |
| Traffic acquisition cost (TAC) | Payments to partners for traffic / ad revenue | A cost of distribution that can rise with partner bargaining power |

Practitioner ranges (judgment, not in the sources, verify): carrier capex at about 12 to 20 percent of revenue, higher during network builds; carrier net debt of about 2 to 3.5 times EBITDA; monthly postpaid phone churn under about 1 percent in concentrated markets.

## What the statements do differently and the accounting traps

- **Spectrum licenses** are often carried as indefinite-lived intangibles and not amortized under US GAAP (verify by jurisdiction), so EBIT omits the cost of the asset. Include spectrum purchases in capital spending when testing cash generation.
- **Leases.** Tower and site leases sit on the balance sheet under IFRS 16 and ASC 842, but EBITDA differs: IFRS puts lease cost below EBITDA, US GAAP mostly within it. Compare carriers across standards only after aligning this (McKinsey ch.27 for the method; standards verify).
- **Handset subsidies and contract assets.** Device installment plans and bundled discounts shift revenue between service and equipment under ASC 606 / IFRS 15; read service revenue separately.
- **Content accounting.** Accelerated amortization, capitalized production and impairments make media earnings lumpy. Compare cash content spend with amortization over several years.
- **Advertising reported gross or net** of partner payments changes revenue and margins; EV/Sales comparisons need the same basis (multiples notes 2.4).
- **Expensed investment in platforms.** Engineering and marketing are expensed, so reported ROIC overstates the return on capital; capitalize R&D before comparing (McKinsey ch.28). Amazon expensed $742m of marketing and $1.1bn of technology in 1999-2003; early ROIC overstated returns for new entrants (McKinsey ch.34).
- **Stock-based compensation** at platforms: show margins and FCF with and without it, and roll the share count forward.
- **Recurring one-time items.** Restructuring and impairments recur at carriers and legacy media; count how many of the last five years carried them.

## Profit pool and competitive dynamics

- **Carriers are a few-player game.** HOLT's profit pools (data June 2016, verify) put wireless telecom at 87 firms, a four-firm revenue ratio of 37.0 percent globally, and a top-ten share of invested capital of 59 / 53 / 69 percent (2005 / 2010 / 2015). National markets are far more concentrated than the global ratio. With high fixed costs, a new entrant or a price war resets returns; rational pricing in a repeated game sustains them (Measuring the Moat, pp.42-45).
- **Media are fragmented**: 748 firms and a four-firm ratio of 19.7 percent in the same study (verify). Returns depend on the library and the hit rate more than on structure.
- **Interactive media have strong network effects.** Where users interact, leaders hold well above 50 percent share and often near 90 percent; Google held about 70 percent of global search and about 90 percent on mobile in 2015 (TAM 2015, pp.17-19, verify current shares). Most networks never tip, and leaders can still fade (AOL, MySpace, Friendster).
- **Who captures value.** Carriers carry most of the capital; platforms and content owners earn higher spreads on less of it. Map the pool across carriers, platforms, content owners and device makers before calling any part attractive (`references/industry-structure.md`).
- **Substitutes and disruption.** Streaming against linear TV, messaging against voice, fixed wireless against cable: each is a new-market or low-end disruption to test.

## Persistence and fade

Historical base rates, not current facts (verify against current data). The base-rate sample uses the pre-2018 GICS sector "Telecom services". Media and internet companies were then classified in consumer discretionary and information technology, so the telecom row describes carriers only; use the IT row from the software primer for platforms.

| Measure | Telecom services | Comparison | Sample |
|---|---|---|---|
| Gross profitability, 5-yr r; median; CoV | 0.59; 0.24; 0.26 | staples 0.86; 0.49 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Operating margin, 5-yr r; median | 0.63; 22% | staples 0.89; 9% | Same, 1950-2015 |
| CFROI, 4-yr r; median; CoV | 0.55; 5.7%; 0.27 | staples 0.78; 8.1% | Global, market cap about $250M plus, 1983-2015 |
| CFROI, older cut, 4-yr r; mean | 0.47; 4.6% | | HOLT, r 1986-2012, means 1990-2012 |
| Operating margin beta, 1-yr / 3-yr | 0.174 / 0.184 | all about 0.11 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Sales growth correlation with US real GDP | 0.51 | | Top 1,000 global, 1950-2014 |

Reading: carriers combine the highest median operating margin with a low median CFROI, because the margin is earned on a large asset base (telecom ranks third for fixed assets to total assets after energy and materials, Damodaran data January 2015). The sector's coefficient of variation for CFROI is among the highest, and the persistence correlation itself moves a lot over time (SD of the gross profitability r about 0.24), so state a wide range. The high operating margin beta means a revenue shortfall hits profit hard.

## Valuation conventions and their pitfalls

- **Carriers:** EV/EBITDA is the convention, but it ignores capex, so compare it only among carriers with similar capital intensity and add EV/(EBITDA - capex) and FCF yield after leases and spectrum (multiples notes 2.4). Dividend yield is a floor value, not a valuation, and needs a check of payout against FCF and net debt. Sum of parts (towers, fiber, spectrum, the operating company) is valid only with peers of similar performance (`references/valuation.md`).
- **EV per subscriber** says nothing about profitability; it is fair only as sustainable NOPLAT per subscriber (multiples notes 2.4). Late-1990s internet valuations per customer (Yahoo $2,038, Amazon $1,400) show how such metrics lose meaning (McKinsey ch.14).
- **Leverage:** high operating and high financial leverage together carry the highest earnings risk (Operating Leverage, 2016); carriers often have both. Use coverage and rating thresholds, not debt to equity.
- **Media:** EV/EBITDA misleads when content cash spend exceeds amortization; use FCF over several years. Value a library on the cash it will earn, not on cost.
- **Interactive media:** EV/EBIT, P/E and FCF yield once margins are representative; the high-growth method for younger platforms. Check what growth and competitive advantage period the price implies (`references/expectations.md`).

## Questions a specialist asks on the earnings call

1. How much of ARPU growth came from price rises, mix and promotions rolling off?
2. What were gross adds, churn and net adds by segment, and who gained share?
3. What is the capex plan for the next three years, and what is the spectrum commitment?
4. What is leverage including leases and the spectrum payments due, and what is the target?
5. How did content cash spend compare with amortization, and what is the plan?
6. How did ad revenue split between volume and price, and how did traffic acquisition costs move?
7. How did engagement and users change by region and product?
8. What regulatory decisions (spectrum auctions, mergers, platform rules) are pending (verify)?

## What to watch at the macro level

- Interest rates: carriers carry high debt and pay large dividends, so refinancing costs move value (judgment).
- Advertising spending follows the business cycle; McKinsey lists advertising among industries with a falling median ROIC trend (ch.4, 1965-2007, verify).
- Consumer spending and price sensitivity for subscriptions.
- Regulation: spectrum auctions, merger review, net neutrality, platform and privacy rules, digital services taxes (verify current rules by market).
- Currency: emerging-market carriers report in local currency; use constant-currency growth.
- Sales growth correlates only moderately with GDP (r 0.51, 1950-2014).
