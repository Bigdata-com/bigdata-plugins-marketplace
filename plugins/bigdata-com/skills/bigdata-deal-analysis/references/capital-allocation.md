# Capital allocation as tests

This method judges whether management turns cash into growth in long-term value per share. The goal is value per share, not growth, earnings per share or the share price (Mauboussin, Capital Allocation, 2015, p. 3-5). It tabulates five years of sources and uses of cash, runs one numeric test per use (organic reinvestment, acquisitions, divestitures, dividends, buybacks, debt) and reads what the proxy pays management for. Most actions are sound at one price and unsound at another, so every test compares what was paid with what was received.

## When a skill loads this file

bigdata-capital-allocation runs the whole method; bigdata-deal-analysis runs step 7 and the deal tables; bigdata-deep-dive reports the sources-and-uses table, the buyback, deal and incentive lines; bigdata-moat uses steps 4 and 10. A narrow question ("was the buyback a good use of cash?") gets step 5 alone.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| CFO, capex, depreciation, acquisitions, divestitures, working capital, dividends, buybacks, issuance, SBC, debt, gross and net PP&E, invested capital, ROIC, cash conversion cycle, market cap, EV | the company tearsheet: statements, ratios and key metrics | reported |
| Deal history | the tearsheet's M&A section; a search for each announcement (price, premium, synergies, payment form, integration cost) | reported |
| Price series around announcements and over the buyback years | the tearsheet overview (quote and standard-window performance); the computing tool for daily series | reported, derived |
| Repurchase actuals, proxy statement (incentive metrics, performance period, clawback), insider sales | a search over filings, then the full document | reported |
| Executives and CEO changes | `c_level_leadership` section | reported |
| Cost of equity and of capital, intrinsic value per share by year | Not in Bigdata.com; stated with basis and sensitivity | assumed |

## Procedure

1. **Sources and uses.** Tabulate five years. Sources: CFO, net debt issued, equity issued, divestiture proceeds. Uses: capex, acquisitions, increase in working capital, dividends, buybacks, debt repaid, change in cash. Show R&D as a memo line, since it is expensed inside CFO. Done when the table ties to the change in cash each year.
2. **Spending pattern.** Compute cents invested per dollar of sales change for working capital, net fixed capital and net M&A (formula 2) over at least three and preferably five to ten years. Mark inflection points and CEO changes, which often shift the mix. Done when the mix and any shift are stated.
3. **Order of the tests.** Each dollar should go to the use with the highest expected return above the cost of capital. Test organic reinvestment first, then deals, then payouts (dividends as a commitment, buybacks only below value with no better use), then debt repayment (Mauboussin golden rule; McKinsey ch. 23). This is an order of testing, not a fixed ranking. Done when each use in the table has a verdict in step 11.
4. **Organic reinvestment.** Compute ROIC, three-year rolling ROIIC (the longest window five annual periods allow), growth capex (capex minus depreciation) as a share of capex, asset life and age, and asset growth. Compare actual growth with ROE x (1 - payout): growth well below it means cash beyond what the business can use (Mauboussin FAQ, 2014, p. 2). Check what retained earnings added to earning power (Security Analysis p. 381-392). Done when level, direction and the retention test are stated.
5. **Buybacks.** For each year: amount repurchased (actuals, not authorisations), average price, intrinsic value at the time, the buyback return against the cost of equity (formula 4), shares issued in the same year, and the net share count change. Lay the record against the valuation path: did buying rise when the stock was dear and stop when it was cheap? Name the funding source and the school management follows: fair value, intrinsic value or accounting-motivated (Mauboussin FAQ p. 9). Note insider selling during buybacks. Done when each year has a price-to-value return and a net issuance figure.
6. **Dividends.** Compute coverage by free cash flow after SBC and after maintenance and growth needs, and name the funding source: free cash flow, debt, offshore cash, or new equity, which is a false signal (Berkowitz, Security Analysis p. 345-347). Use total and net shareholder yield, not dividend yield. Done when coverage and funding source are stated for each year.
7. **Acquisitions.** For each deal in the last five years: premium, PV of cost and revenue synergies, deal NPV, predicted buyer move against the actual one-, three- and five-day move, SVAR and premium at risk, payment form, category and base rate (table 1), fit with McKinsey's five archetypes, and return on price paid against the cost of capital. Then the later record: goodwill impairments and disposals of acquired units reveal overpayment. Done when each deal has its row in the deal table.
8. **Divestitures and spin-offs.** List disposals and spin-offs, the price against the unit's value to the company, and whether units earning below the cost of capital remain. Sellers do better than buyers on average (Mauboussin 2015, p. 35). Done when each disposal is listed with its rationale and price.
9. **Balance sheet.** Compute EBIT / interest and debt / total capital and place them against table 6; check whether payouts were financed by borrowing (reinvestment rate above 1 with a high payout, McKinsey ch. 8). Load credit.md for a full credit view. Done when coverage and leverage are placed against the table.
10. **Incentives.** From the proxy, classify each long-term plan metric (absolute or relative TSR, EPS, ROIC or capital efficiency, revenue, cash flow), the performance period, option expense, clawbacks, option repricing and related-party dealings. Ask which way the CEO would go if the plan and value per share conflict (Mauboussin 2015, p. 5). Done when each metric is classified and the conflict question is answered.
11. **Verdict per use.** For each use, one line: value created, value neutral, value destroyed or not determinable, with the test that decides it. No composite score. Done when every use has a line and a basis label.

## Formulas

1. FCF = NOPAT - Investment; Investment = change in net working capital + (capex - depreciation) + (acquisitions - divestitures).
2. Incremental rates = each investment component / change in sales (for example ($130 - $70) / $100 = 60% fixed capital rate).
3. ROIC = NOPAT / average invested capital. ROIIC = (NOPAT_t - NOPAT_t-1) / (IC_t-1 - IC_t-2), three-year rolling. Implied growth = reinvestment rate x ROIIC (derived). Growth without outside funding = ROE x (1 - payout).
4. Buyback return = k_e / (P / IV), with k_e the cost of equity (assumed), P the price paid and IV intrinsic value per share at the time (assumed). At k_e 8% and P / IV of two-thirds the return is about 12%.
5. Value per share after a buyback = (V - C) / (N - C / P), with V the value of the firm before, C the cash spent, N shares before. Firm value 100,000, 1,000 shares, 20,000 spent at 200 gives 88.89 per share; at 50 it gives 133.33 (Mauboussin 2015, ex. 37).
6. EPS breakeven P/E = 1 / [r x (1 - t)], with r the pre-tax yield on the cash used or the pre-tax cost of the debt raised and t the tax rate. Cash at 3% and 33% tax gives 50; debt at 6% gives 25. A buyback below that P/E raises EPS; this says nothing about value.
7. Net shareholder yield = (dividends + buybacks - issuance) / average market cap. Net equity issuance ratio = issuance / purchases - 1.
8. Premium = (offer - undisturbed price) / undisturbed price, using the price before rumours.
9. PV synergies = gross synergy x (1 - t) / cost of capital, discounted for phasing and less disclosed integration cost. Deal NPV = PV synergies - premium paid. Predicted buyer move (cash deal) = NPV / buyer market cap.
10. SVAR, cash deal = premium / buyer market cap; stock deal = premium / (buyer cap + seller cap + premium). Premium at risk (stock deal) = share of the premium the seller would not receive if no synergies arrive.
11. Return on price paid = (target NOPAT + improvements) / total price paid; it should exceed the cost of capital (McKinsey ch. 21, ex. 21.10).
12. Asset life = gross PP&E / depreciation; asset age = life x (1 - net PP&E / gross PP&E).
13. Total shareholder return = g + (1 + g) x d, assuming full reinvestment of dividends d at price growth g.

## Reference tables

All figures are historical samples; quote them with their period and "(historical; quote with source and period)".

**Table 1. Deal success rate by strategic category** (Clark and Mills, in Mauboussin, To Buy or Not To Buy, 27 Feb 2017, ex. 12)

| Category | Success rate |
|---|---|
| Opportunistic bottom-trawl (a dying competitor exits) | 87-92% |
| Bolt-on filling a gap | 80-85% |
| Line extension | 65-70% |
| Consolidation of a mature industry | 55-60% |
| Multiple core-related complements | 40-45% |
| Consolidation of an emerging industry | 37-42% |
| Single core-related complement | 30-35% |
| Lynchpin strategic | 20-25% |
| Speculative strategic | 15-20% |

**Table 2. Deal base rates**

| Statistic | Figure | Source |
|---|---|---|
| Deals that fail to create value for the acquirer | About 60% | Sirower and Sahni 2006, in Mauboussin, Cultivating Your Judgment Skills, 7 May 2013, p. 5 |
| Deals where the buyer beat the market | 38% (1997-2009); 50-51% (2010-2015/16); 42% 20-year average | Mauboussin 2017, p. 3; Capital Allocation 2016 |
| Value created for acquirer | One third yes, one third no, one third inconclusive (1,415 deals, 1997-2009) | McKinsey ch. 21 |
| Average premium | 47% (2014), 43% (2016); McKinsey's typical figure about 30% | Mauboussin 2015 p. 20, 2017 p. 10; McKinsey ch. 21 |
| Premium by lasting market reaction | Persistent positive 25.8%, persistent negative 40.5% | Mauboussin 2017, ex. 4 |
| Buyer 5-day return by payment | Cash +0.7%, stock -3.9%, mixed -4.1% | Mauboussin 2017, p. 13 |
| EPS accretion | 86% of 95 deals accretive; 27% of those created value | Mauboussin 2017, p. 8-9 |
| Cost synergies | 86% of 90 deals captured at least 70% of planned savings | McKinsey ex. 21.8 |
| Revenue synergies | Almost half captured under 70%, nearly a quarter under 30% | McKinsey ex. 21.8 |
| Integration cost | Often a year or more of savings; savings not captured in the first full budget year may never be | McKinsey ch. 21, p. 459-460 |
| SVAR in 126 US deals, 2015-2016 | Average 5.5%, median 3.2% | Mauboussin 2017, p. 8 |

**Table 3. Value created per $1 of added revenue by growth type** (consumer goods, illustrative; ranks matter more than levels; McKinsey ex. 2.6): new products 1.75-2.00; expanding the market 0.30-0.75; share gain in a growing market 0.10-0.50; share gain in a stable market -0.25 to 0.40; acquisitions 0-0.20.

**Table 4. Announcement reactions** (McKinsey ch. 23, p. 505-510): dividend cut or omission about -9%; dividend increase about +2%; seasoned equity offering about -3%; open-market buyback +2% to +3%; tender-offer buyback about +16%.

**Table 5. Spending-pattern examples** (Mauboussin 2015, FY2010-2015; cents per dollar of sales change): Walmart working capital 9.4, fixed capital 28.5, M&A 0.6; Emerson 44.3, 18.4, 78.4.

**Table 6. S&P rating medians** (Mauboussin, Operating Leverage, 14 Jun 2016, ex. 14, p. 16; US three-year medians 2011-2013; five-year default probability from McKinsey ex. 23.4, S&P 1981-2003). Full table in credit.md.

| | AAA | AA | A | BBB | BB | B |
|---|---|---|---|---|---|---|
| EBIT / interest (x) | 40.8 | 17.3 | 10.3 | 5.5 | 3.2 | 1.3 |
| Debt / total capital (%) | 2.8 | 17.2 | 30.7 | 41.1 | 50.4 | 72.7 |
| 5-year default probability (%) | 0.12 | 0.33 | 0.75 | 3.84 | 14.45 | 33.02 |

EBITA / interest of about 5 to 11 corresponds to A+ to BBB-, and value barely changes with leverage except below coverage of 2; too much debt costs more than too little (McKinsey ch. 23).

**Table 7. Long-term incentive metrics** (Frederic W. Cook 2014, 250 largest S&P 500 companies, in Mauboussin 2015, p. 51): TSR 58%, profit 50%, capital efficiency 41%, revenue 21%, cash flow 13%.

## Interpretation rules

- **Organic.** Judge value creation on growth capex only, and do not benchmark capex against peers (Mauboussin 2015, p. 25-26). High asset growth predicts low later returns in developed markets and only weakly in emerging ones (Cooper, Gulen and Schill 2008). ROIIC is not an economic return and is not compared with the cost of capital; use it for direction, and test the hurdle with ROIC on new projects or RONIC against WACC.
- **Buybacks.** Repurchase creates value for continuing holders only below intrinsic value and with no better use. A buyback above value transfers value to sellers (formula 5). A later price fall does not prove an error; judge price to value at the time of purchase. EPS accretion is not value. Buying back shares to offset SBC is not value creation. S&P 500 buybacks fell more than 75% in 2007-2009 while dividends fell 20%, so companies tend to buy high (Mauboussin FAQ, 2014, p. 7). Issuance lowered US shareholder yield by 140 bp on average, range 70 to 310 bp (Mauboussin 2015, p. 43).
- **Dividends.** Managers treat dividends as a commitment and buybacks as residual. A dividend paid from debt or new equity is a false signal; stressed companies are almost always late to cut (Berkowitz, Security Analysis p. 346).
- **Acquisitions.** Credit cost synergies with a haircut and revenue synergies with a large one. Predictors of buyer success are a strong operator, a low premium and a sole bidder; EPS accretion, relative P/E and relatedness do not predict (McKinsey ch. 21, p. 449-450). A deal that fits none of the five archetypes (improve the target, remove excess capacity, accelerate market access, buy skills faster than building, pick winners early) is unlikely to create value. Serial acquirers and late-cycle deals do worse.
- **Does not apply** as written to banks and insurers (capital set by regulation), utilities (allowed returns), early-stage companies (ROIIC unstable) and many emerging markets (payout driven by ownership structure and buyback rules; use the home-region base rates in Mauboussin, Capital Allocation Outside the U.S., 2016).

## Output lines

- Five-year sources-and-uses table. [reported]
- "Cents per dollar of sales change, FY-4 to FY0: working capital a, fixed capital b, M&A c." [derived]
- "ROIC x; ROIIC three-year rolling y; growth capex g percent of capex." [derived]
- "Buybacks of X at average price P against estimated value V: return r against cost of equity k; issuance Y; net share count change n percent." [derived; V and k assumed]
- "Dividends covered c times by free cash flow after SBC; funded from ..." [derived, reported]
- Deal table: Deal, Date, Premium, PV synergies (cost / revenue), NPV, SVAR, Payment, Category, Base rate, Market reaction, Later impairment. [reported, derived; synergies as stated by management]
- "Long-term plan pays on [metrics], [relative / absolute] TSR, [n]-year period; the plan [does / does not] reward value per share." [reported; judgment]
- "Verdict by use: ..." [judgment]

## Not in the sources

- Not in the sources: industry ranges for the incremental investment rates; compare with the company's own history and named peers.
- Not in the sources: a dividend coverage threshold.
- Not in the sources: a numeric threshold for incentive alignment.
- Not in the sources: leverage thresholds beyond the coverage table, and net debt / EBITDA medians by rating.
- Not in the sources: a current cost of equity or WACC; state it as an assumption with a sensitivity.

## Sources

- Notes: capital-allocation.md (sections 1-4, 6, 9); Graham and Dodd, Security Analysis, 6th ed. (Berkowitz, Ch. 29, 44); McKinsey, Valuation, 5th ed. (ch. 2, 8); McKinsey, Valuation, 5th ed. (ch. 21-23); Mauboussin, Total Addressable Market (2015), Operating Leverage (2016) and Global Industry Profit Pools (2016) (section 2.6); Mauboussin, Man Overboard (2015) and Celebrating the Summit (2016) (JD).
- Mauboussin (Credit Suisse): Capital Allocation, 2 Jun 2015 and 19 Oct 2016; Capital Allocation Outside the U.S., 15 Nov 2016; Disbursing Cash to Shareholders, 6 May 2014; To Buy or Not To Buy, 27 Feb 2017; Operating Leverage, 14 Jun 2016; Cultivating Your Judgment Skills, 7 May 2013.
- McKinsey, Valuation, 5th ed. (2010): ch. 2 p. 17-44; ch. 8 p. 165-186; ch. 21 p. 445-468; ch. 22 p. 469-488; ch. 23 p. 489-524.
- Graham and Dodd, Security Analysis, 6th ed. (2009): Berkowitz p. 341-347; ch. 29 p. 376-392; ch. 44 p. 575-590.

<!-- Spec and notes agree. Kept from the earlier moat skill: impairments and disposals of acquired units, debt-funded buybacks, insider selling, clawbacks, option repricing; dropped its scorecard, ownership multiples and sizing links. -->
