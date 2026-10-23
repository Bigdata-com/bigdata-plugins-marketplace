# Alignment with the investing resources

Which sources informed each library file and skill, as reported by the agents that wrote them and checked by the reviewers. The source material is the set of papers and books in the investing-resources folder: Michael Mauboussin's Credit Suisse, Legg Mason and Counterpoint papers (2006 to 2017), Robinson and Weyns (UBS) on multiples and DCF (2017), Koller, Goedhart and Wessels, Valuation, fifth edition (McKinsey), Graham and Dodd, Security Analysis, sixth edition (with the modern commentaries by Klarman, Marks, Berkowitz, Greenwald, Merkin and Russo), Klarman, Margin of Safety (1991), and Damodaran, Return on Capital, Return on Invested Capital and Return on Equity (2007). Every figure in the library carries its source and period; where the sources were silent the file says "Not in the sources" and the skill states an assumption.

## Method files

| File | Sources | Assumptions where the sources were silent |
|---|---|---|
| expectations.md | Mauboussin, Expectations Investing (CFA, 2006, pp. 61-70); Mauboussin and Callahan, What Does a P/E Multiple Mean? (2014, pp. 2-13, Exhibits 5 and 6); UBS multiples paper (2017, pp. 47-49, 63-64); UBS DCF Episode II (2017, pp. 26-31) | Investment in the implied-CAP formula taken as next year's net investment held constant; no 80/20 rule stated because none is sourced |
| base-rates.md | The Base Rate Book (2016) and its sales growth, earnings growth and gross profitability editions (2015-2016); How to Model Reversion to the Mean (2013); What Makes for a Useful Statistic (2016) | Applying CFROI fade rates to the FactSet ROIC field is labelled judgment |
| forecasting-discipline.md | Sharpening Your Forecasting Skills; Methods to Improve Decisions; Cultivating Your Judgment Skills; IQ versus RQ; Expectations Investing pp. 61-69 | The premortem minimum of three reasons, the kill-criteria table and the catalyst-scoring table are the file's own constructions |
| after-a-price-move.md | Managing the Man Overboard Moment (2015, Exhibits 2, 3, 12, 13); Celebrating the Summit (2016, Exhibits 2-4); A Long Look at Short-Termism (2014, pp. 9-10); Klarman ch. 1 | The universe of the studies is not stated in the papers; the dispersion cells run 32.0 to 46.5 points |
| downside-and-catalysts.md | Klarman ch. 1-3, 6-10, 13; Security Analysis: Klarman preface, ch. 42-43, Greenberg, Greenwald, Russo | Cash runway for early-stage companies stated as an assumption |
| roic.md | Damodaran (2007, pp. 3-65); Calculating ROIC (2014); Estimating the Cost of Capital (2013); Economic Returns, Reversion to the Mean and TSR (2013); McKinsey ch. 2, 4, 6-11, 25, 27-29 | Two beta formulas appear in the sources; the file shows both and asks the model to say which it used |
| industry-structure.md | Measuring the Moat (2013, pp. 3-55); Profit Pools (2016); Total Addressable Market (2015); Corporate Longevity (2017); the Shrinking Universe (2017); How Well Do You Compare (2017); the Trancik cost-curve interview (2017); P/E paper p. 11 | Duration of advantage bounded by persistence figures and the market-implied 8-year CAP as a prior; the old skill's scoring weights and moat ratings were dropped as unsourced |
| operating-leverage-and-tam.md | Operating Leverage (2016, pp. 1-22); Total Addressable Market (2015, pp. 3-37); Profit Pools (2016); Expectations Investing p. 68; McKinsey ch. 9 | None beyond the papers' own |
| multiples-and-peers.md | UBS multiples paper (2017, pp. 7-70); P/E paper (2014); How Well Do You Compare (2017); McKinsey ch. 10, 14, 15, 33, 35, 36, Appendix E | No minimum peer count in the sources; peers tested with and without the closest and the most distant |
| valuation.md | McKinsey ch. 2-13, 19, 29, 30, 33-36; UBS DCF Episodes I and II (15-row error catalogue); Estimating the Cost of Capital (2013, pp. 7-26) | No WACC inputs in Bigdata.com; no RSU procedure; the emerging-market crisis probability is marked verify |
| earnings-quality.md | Security Analysis pp. 56, 90, 341-342, 409-486, 526-531, 545-547, 591-610, 656-663; McKinsey ch. 7, 12, 16, 24, 26-28, 35-36; Capital Allocation (2015, pp. 25-27); Klarman ch. 8 | The two-of-five-years rule for recurring charges and the severity scale are labelled assumed |
| capital-allocation.md | Capital Allocation (2015/2016, pp. 3-5, 20, 25-27, 33-43, 51); the buybacks paper (2014); To Buy or Not To Buy (2017); Operating Leverage exhibit 14; Cultivating Your Judgment Skills p. 5; McKinsey ch. 2, 8, 21-23; Security Analysis pp. 341-347, ch. 29, 44 | Cost of equity and intrinsic value are stated inputs |
| credit.md | Security Analysis: Marks pp. 128-140, pp. 85-88, 591-597, 688-690; Klarman ch. 4, 7, 12; McKinsey ch. 7, 8, 12, 23 (exhibits 23.3-23.6); Operating Leverage exhibit 14 | The stress-shock sizing rule and the 24-month maturity window |
| special-situations-arithmetic.md | Klarman ch. 6, 8-12; Security Analysis ch. 43, Merkin pp. 265-288, p. 441; McKinsey ch. 12, 22 | The implied-completion-probability formula is derived; the 1930s liquidation recovery table is illustrative |

## Sector primers

| Primer | Sources | Judgment ranges marked (verify) |
|---|---|---|
| technology-software, semiconductors-and-hardware, communication-services, healthcare-pharma | Base Rate Book sector tables (persistence, margins, CFROI, operating-margin beta); Profit Pools; Measuring the Moat; McKinsey ch. 26-28, 32, 34, 35; the Microsoft cash-versus-earnings example; Damodaran's R&D method; the old software and pharma primers rebuilt | Retention and payback ranges, chip spending ranges, telecom capex and churn, trial success rates; the pharma double-discounting in the old primer was corrected to McKinsey's decision-tree method |
| financials-banks, insurance, reits, utilities | McKinsey ch. 36 (equity cash flow, economic spread, parts), ch. 16, 4, 15, 7; Calculating ROIC p. 11; Security Analysis (Berkowitz on loss reserves, Marks on appraisals, Graham and Dodd on 1929 utility bonds); Klarman; the CFROI financials row; the old banks and REIT primers | Most of insurance; REIT and utility benchmark ranges; the primers say where enterprise multiples partly survive (implied cap rate, EV to regulated asset base) |
| industrials, consumer-retail, energy, materials | Base Rate Book sections 2.5-2.8; Operating Leverage (fixed-cost example, utilisation correlation, the Goodyear mix example); McKinsey ch. 35 (cyclicals), 27, 32; Measuring the Moat (HHI, airlines, mini-mills); UBS EV per unit of capacity (the cement example); the old industrials, consumer and energy primers | Book-to-bill and backlog thresholds, inventory turnover, the producer-to-services lag, mid-cycle price decks, cost-curve quartiles |

## Skills

| Skill | Sources behind the method (beyond its method files) |
|---|---|
| markets-today | A Long Look at Short-Termism; Methods to Improve Decisions; Outcome Bias and the Interpreter |
| watchlist | after-a-price-move rule 1; Expectations Investing (which revision matters); the old quick-take and company-brief |
| company-brief | the old company-brief's categories; Expectations Investing value triggers; the long-term outlook test |
| stock-move | Man Overboard and Celebrating the Summit; A Long Look at Short-Termism; Klarman ch. 1 |
| catalysts | the old catalyst-monitor schema; Klarman ch. 10; forecasting-discipline |
| quick-take | expectations (steady-state P/E, implied growth), base rates, downside-and-catalysts |
| deep-dive | all of roic, industry-structure, earnings-quality, capital-allocation, expectations, valuation, multiples, downside, forecasting |
| thesis | Expectations Investing 1.1-1.2; Methods to Improve Decisions and the premortem; Klarman ch. 9-10; the old variant-perception claim template |
| valuation | McKinsey as distilled in valuation.md and roic.md; the UBS error catalogue and sanity-check list |
| comps | UBS multiples pp. 24-27 (five steps); McKinsey ch. 14-15; the old peer-comparables exclusions |
| scenarios | Methods to Improve Decisions (no default split); base rates parts 1 and 3; UBS scenario manager |
| earnings-quality | earnings-quality.md steps 1-13; Security Analysis; McKinsey ch. 7, 24-28, 35-36; the old screen's flags |
| moat | Measuring the Moat steps; base-rates table 9; the roic transition and fade tables |
| capital-allocation | capital-allocation.md formulas 2-12 and tables; Capital Allocation pp. 49-52 on incentives |
| risk | downside-and-catalysts; credit steps 2-8; Klarman ch. 8 (private-market value); the old risk categories |
| credit | credit.md; Marks in Security Analysis; the rating medians; McKinsey ch. 23 |
| earnings-preview | expectations, base rates, operating leverage, forecasting; the old preview's order of sections |
| earnings-review | after-a-price-move rule 1 and tables; expectations formulas 1-2; the old digest and reaction (guidance table, thesis words) |
| deal-analysis | capital-allocation step 7 and formulas 8-11; McKinsey ch. 21-22; Sirower and Sahni via Cultivating Your Judgment Skills |
| special-situations | special-situations-arithmetic; Klarman ch. 9-12; Merkin in Security Analysis |
| sector | industry-structure steps 1-8; base-rates tables 6-10; the primers; the old sector skills |
| theme | TAM steps 1-7, the Bass model, the S-curve; the old thematic exposure check |
| country, macro-compare | forecasting-discipline (facts, opinions, expectations apart); the old country, regional and G7 skills |
| screen | base-rates table 6 (persistent metrics); roic; multiples step 7; the Freestyle Chess paper |
