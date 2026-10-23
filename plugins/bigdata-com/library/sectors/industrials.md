# Industrials

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
