# Capital allocation as tests

Purpose: judge whether management turns cash into growth in long-term value per share. The method tabulates sources and uses of cash over five years, then runs one numeric test per use: organic reinvestment, M&A, dividends, buybacks and debt, and reviews what the proxy pays for. Used by the moat, memo, valuation, earnings and M&A jobs. The goal is value per share, not growth, EPS or share price (Mauboussin, Capital Allocation, 2015-2016).

## 1. Inputs

- Tearsheet (5 fiscal periods): CFO, capex, D&A, acquisitions, divestitures, dividends, buybacks, share issuance, SBC, debt, gross and net PP&E, invested capital, ROIC, cash conversion cycle, market cap, EV, M&A history, executives, consensus estimates.
- Search: deal announcements (price, premium, synergies, payment form), repurchase actuals, proxy statement (incentive plan metrics), filings.
- Assumed inputs: cost of equity and cost of capital (WACC is not in Bigdata.com), and intrinsic value per share from the valuation job.

## 2. Procedure

1. Sources and uses. Tabulate five years: sources (CFO, net debt issued, equity issued, divestiture proceeds) and uses (capex, acquisitions, working capital, dividends, buybacks, debt repaid, change in cash). Show R&D as a memo, since it is expensed inside CFO. Done when the table ties to the change in cash.
2. Order of tests. The sources give an order of testing, not a fixed ranking: fund uses by expected return above the cost of capital. Test organic reinvestment first, then deals (NPV test), then payout (dividends as a commitment, buybacks only below value with no better use), then debt paydown last (Mauboussin golden rule; McKinsey ch. 23). Done when each use has a verdict.
3. Value drivers. For at least 3 and preferably 5 to 10 years compute incremental working capital rate, fixed capital rate and M&A rate per change in sales. Done when mix and shifts at CEO changes are stated.
4. Organic tests. Compute ROIC, ROIIC (rolling 3 and 5 years), growth capex, asset age, asset growth. Done when direction and level are stated.
5. Buyback tests. Done when each buyback has a price-to-value return and a net issuance figure.
6. Dividend tests. Done when coverage and funding source are stated.
7. M&A tests. Run for each deal in the last five years. Done when each has NPV, SVAR, category and base rate.
8. Balance sheet tests. Done when coverage and leverage are placed against the ratings table.
9. Incentive review. Done when each proxy metric is classified.

## 3. Formulas

- FCF = NOPAT - Investment; Investment = change in NWC + (capex - depreciation) + (acquisitions - divestitures). Value drivers = each component / change in sales.
- ROIC = NOPAT / invested capital. ROIIC = (NOPAT_t - NOPAT_t-1) / (IC_t-1 - IC_t-2). Implied growth = reinvestment rate x ROIIC (derived). Growth without outside funding = ROE x (1 - payout).
- Maintenance capex proxy = depreciation; growth capex = capex - depreciation. Asset life = gross PP&E / depreciation; age = life x (1 - net / gross PP&E).
- Buyback return = cost of equity / (price / intrinsic value). EPS breakeven P/E = 1 / [rate x (1 - tax)], rate = pre-tax yield on cash or pre-tax cost of debt. Net shareholder yield = (dividends + buybacks - issuance) / average market cap.
- Premium = (offer - undisturbed price) / undisturbed price. PV synergies = gross x (1 - tax) / cost of capital, discounted for phasing. Deal NPV = PV synergies - premium paid. Predicted buyer move (cash) = NPV / buyer market cap. SVAR cash = premium / buyer cap; stock = premium / (buyer cap + seller cap + premium). Return on price paid = (target NOPAT + improvements) / price paid, to exceed cost of capital (McKinsey ch. 21).
- Total return = g + (1 + g) x d, with full reinvestment.

## 4. Reference tables

Deal-type success rates (Clark and Mills, in Mauboussin, To Buy or Not to Buy, 27 Feb 2017, ex. 12): opportunistic bottom-trawl 87-92%; bolt-on 80-85%; line extension 65-70%; mature-industry consolidation 55-60%; multiple core-related complement 40-45%; emerging-industry consolidation 37-42%; single core-related complement 30-35%; lynchpin strategic 20-25%; speculative strategic 15-20%.

Failure base rates for deals (quote as a range, not a forecast): about 60% fail to create value for the acquirer (Sirower and Sahni 2006, cited in Mauboussin, Cultivating Your Judgment Skills, 7 May 2013, p. 5). Buyer-gain share 38% in 1997-2009 and 50-51% in 2010-2015 (Mauboussin 2017), so 49-62% did not gain. One third create value, one third do not, one third inconclusive (1,415 deals, McKinsey ch. 21). All verify.

Synergies: 86% of 90 deals captured at least 70% of cost savings; almost half captured under 70% of revenue gains and nearly a quarter under 30% (McKinsey ex. 21.8). Integration cost often equals a year or more of savings. Savings not captured in the first full budget year may never be.

Value per $1 of added revenue by growth type (consumer goods, illustrative; McKinsey ex. 2.6): new products 1.75-2.00; expand market 0.30-0.75; share gain in growing market 0.10-0.50; share gain in stable market -0.25 to 0.40; acquisitions 0-0.20.

Cents per dollar of sales examples (Mauboussin, FY2010-2015, dated): Walmart working capital 9.4%, fixed capital 28.5%, M&A 0.6%; Emerson 44.3%, 18.4%, 78.4%. GAP: no industry ranges.

Credit medians (S&P, 3-year medians 2011-2013, Mauboussin, Operating Leverage, 2016, p. 15-17; verify): AAA, AA, A, BBB, BB, B. EBIT coverage 40.8, 17.3, 10.3, 5.5, 3.2, 1.3. Debt/total capital 2.8, 17.2, 30.7, 41.1, 50.4, 72.7%. Return on capital 30.6, 21.6, 22.2, 14.2, 11.1, 7.1%. Five-year default probability (S&P 1981-2003, McKinsey ex. 23.4): 0.12, 0.33, 0.75, 3.84, 14.45, 33.02%. EBITA/interest of 5 to 11 corresponds to A+ to BBB-; leverage has little value effect except below coverage 2. GAP: no net debt/EBITDA medians by rating.

Announcement returns (McKinsey ch. 23, verify): dividend cut about -9%, increase +2%, open-market buyback +2% to +3%, tender about +16%. Buyer 5-day return by payment form: cash +0.7%, stock -3.9%, mixed -4.1% (Mauboussin 2017).

Incentives (Frederic W. Cook 2014, largest 250 S&P firms, verify): long-term plans use TSR 58%, profit 50%, capital efficiency 41%, revenue 21%, cash flow 13%. Read the proxy for: absolute versus relative TSR (absolute is mostly luck), ROIC or capital efficiency metric, EPS targets, option expense, performance period, long-term plan. HOLT deducts for no disclosure, no financial targets, substantial option expense, no long-term plan. Three agency conflicts: pay tied to size favours M&A, managers avoid risk, short horizons. In a survey of 400 CFOs, 80% would cut value-creating spending to hit an earnings target (McKinsey ch. 1). GAP: no numeric alignment threshold.

## 5. Interpretation rules

- Organic. Capex above depreciation is growth capex; judge value on that part only. Do not benchmark capex against peers. High asset growth predicts low later returns in developed markets and only weakly in emerging ones (Cooper, Gulen and Schill 2008). ROIIC is not an economic return and Mauboussin says not to compare it with the cost of capital; use it for direction, and test the hurdle with ROIC on new projects or McKinsey's RONIC above WACC.
- Buybacks. Repurchase only below intrinsic value with no better use. A buyback above value transfers value from continuing holders to sellers: at $200 against $100 of value, holders' value per share falls to 88.89 from 100 (Mauboussin ex. 37). A later price fall does not prove error; judge price to value at purchase. EPS accretion is not value, and issuance offsetting must be netted. Compare the repurchase record with the valuation path; S&P 500 buybacks fell over 75% in 2007-2009. Repurchasing to offset SBC dilution is not value creation. Worked breakeven: cash yielding 3% with 33% tax gives P/E 50; debt at 6% gives P/E 25. Issuance lowered US shareholder yield by 140 bp on average (range 70-310, dated).
- Dividends. Check coverage by FCF after SBC and after maintenance and growth needs, and the funding source: debt, offshore cash, or new equity (a false signal, Berkowitz). If actual growth is below ROE x (1 - payout), cash is in excess. Use total shareholder yield, not dividend yield. GAP: no coverage threshold in the sources.
- M&A. EPS accretion is not a test: 86% of 95 deals were accretive, 27% of those created value. Cost synergies are credible and revenue synergies are haircut. Predictors of buyer success: strong operator, low premium, sole bidder (McKinsey ch. 21).
- Leverage. Use coverage and the table; GAP: the sources give no other leverage thresholds. High payout with reinvestment above 1 means borrowing to pay (McKinsey ch. 8). Cost of overleverage exceeds cost of underleverage (McKinsey ch. 23).
- Not applicable: banks and insurers (capital set by regulation), utilities (allowed returns), early-stage firms (ROIIC unstable), emerging markets (payout driven by ownership and rules).

## 6. Output lines

- Five-year sources and uses table [reported].
- "Cents per $1 of sales change: working capital a, fixed capital b, M&A c" [derived].
- "ROIC x, ROIIC three-year y, five-year z; growth capex share g" [derived].
- "Buybacks of $X at average price P against value V: return r versus cost of equity k; net of issuance $Y" [derived; V and k assumed].
- "Deal D: premium p, NPV n, SVAR s, category c, base rate b" [derived; synergies as stated by management].
- "Incentive plan pays on [metrics]; relative or absolute TSR; aligned or not" [reported; alignment judgment]. Test: which way would the CEO go if the plan conflicts with value per share.

## 7. Sources

Notes: capital-allocation.md, security-analysis.md (Berkowitz), mckinsey-part1.md (ch. 2, 8), mckinsey-part2.md (ch. 21-23), tam-leverage-profit-pools.md (credit medians), decisions-price-moves.md (60% figure).
