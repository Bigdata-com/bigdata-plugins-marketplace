# Industry structure and moat (Measuring the Moat sequence)

Purpose: decide whether a company's excess return over its cost of capital is likely to last, by testing the structure of its industry first and the company's own advantage second. Used by moat, company, thesis, sector and theme jobs. The output is a balance of evidence and what would change it, never a rating.

Source tags (Mauboussin and Callahan unless noted): [MM] Measuring the Moat 2013; [PP] Global Industry Profit Pools 2016; [CL] Corporate Longevity 2017; [SU] Shrinking Universe 2017; [T15] Total Addressable Market 2015; [OL] Operating Leverage 2016; [MC14] Calculating ROIC 2014.

## 1. Inputs
- Reported, tearsheet: ROIC, margins, revenue, invested capital, revenue segments (5 years, product and geography) for the company and each peer; peers from a screen or the M&A history. Industry totals are not in the tearsheet.
- Search evidence: section 3, one aspect and one period per call.
- Assumed: WACC (see roic.md).

## 2. Procedure
1. Set the unit of analysis: the business unit, not the conglomerate; analyze each and aggregate [MM p.9]. Place it in a life-cycle phase (innovation, fading, mature, subpar) and give the reason [MM p.4]. Class the industry (fragmented, emerging, mature, declining, international, network, hypercompetitive) [MM p.17].
2. Draw the industry map: suppliers, customers, complementors, regulators and other external parties, and potential entrants; firms in order of dominance; payment terms and incentives between them [MM p.11].
3. Build the profit pool: width = firm's share of industry invested capital, height = ROIC minus WACC, area = economic profit. Use three to five year cycle averages, for today, five and ten years ago [MM p.13; PP p.1-2]. Add the four-firm revenue ratio and the top-10 share of capital. Done: who holds width, who holds spread, who gained or lost.
4. Run the market share stability test (formulas below). Done: one number and a verdict.
5. Run the pricing power test: 5-year price trend of the product, split any margin change into price, mix and volume [MM p.16; OL p.8-10]. Stable or rising prices go with a stable industry; falling prices with a fast-cycle one.
6. Test rivalry: HHI, concentration versus profits, similarity of firms' goals and ownership, asset specificity (keeps firms in), demand variability with high fixed costs, industry growth [MM p.25-27].
7. Test entry and exit with the base rates and the barrier list below. Done: named barriers with evidence, and recent entrants.
8. Apply Porter's forces as root-cause tests, not as an attractiveness label [MM p.18-27]. Supplier: more concentrated than the industry, no substitutes, high switching cost, industry small in supplier sales. Buyer: concentration, switching cost, information, substitutes. Substitutes: ceiling on price. Can the industry pass on supplier increases?
9. Map the value chain by discrete activity (R&D, supply chain, operations, marketing and sales, service) and compare with peers; a chain like peers' implies competition to be best and price wars [MM p.33]. Value created = willingness to pay minus opportunity cost [MM p.32].
10. Identify the source of advantage and test it against the numbers. Production: process (indivisibility, complexity, learning, protection, unique resources) and scale (distribution, purchasing, R&D, advertising); signature is low gross margin and high turnover. Consumer: habit, switching cost, network effects; signature is high gross margin. External: subsidy, tariff, regulation [MM p.34-41]. Scale is mostly local [T15 p.16]. A brand counts only if it raises willingness to pay; two of ten owners of the top ten brands missed their cost of capital [MM p.46-47]. Done: ROIC split into margin and turnover over 5 to 10 years matches the claimed source.
11. Run the disruption test: sustaining, low-end or new-market innovation; has innovation overshot customer needs; is competition moving to speed and convenience; are components modularizing [MM p.27-31].
12. Conclude on magnitude and duration (section 6).

## 3. Evidence to gather from Bigdata.com searches
| Step | Search for | Document type |
|---|---|---|
| 2, 8 | named suppliers, customers, regulators, complementors, contract terms, customer concentration | filings (business, risk factors), transcripts |
| 3, 4 | industry size, shares, peer results | broker research, filings, news |
| 5 | price increases taken, volume response, discounting, mix | transcripts, news |
| 6, 7 | capacity additions, entrants, exits, M&A, price wars | news, transcripts, M&A history |
| 8 | supplier or buyer concentration, switching costs, contract length | filings, broker research |
| 10 | customer retention, lock-in, scale economics, patents and expiries | filings, transcripts |
| 11 | new entrants on low price, new-market products | news, broker research, job postings |

## 4. Formulas
- Share stability = (1/N) x sum over competitors of |share(t) minus share(t-5)|, in percentage points, N = number of competitors [MM p.15-16].
- HHI = 10,000 x sum of squared market shares of the 50 largest firms. Shares 40, 30, 20, 10 give 3,000 [MM p.25-26].
- Four-firm ratio = revenue share of the four largest firms [PP p.1].
- Economic profit = invested capital x (ROIC minus WACC) [MM p.13].
- Unit cost after cumulative output doubles: about 0.8 x prior unit cost, for the median product [MM p.19-25].

## 5. Reference tables (all dated; verify)
| Item | Threshold or base rate | Source |
|---|---|---|
| Share stability | 2.0 points or less over five years is stable; 2007-2012: carbonated drinks 2, PCs 3, storage 4, smartphones 9 | [MM p.15-16] |
| Price trend, 2006-11, per year | ammunition +9.5%, pet food +5.8%, caskets +5.7%; semiconductors -8.6%, audio/video -1.9%, fiber optic -1.7% | [MM p.16] |
| Price elasticity | 1% price change gives 1.76% demand change on average (370 goods, 1998) | [OL p.8-10] |
| HHI | above 1,800 suggests reduced rivalry; 2007: breakfast cereal 2,425, snack food 1,984, tire 1,540 | [MM p.25-26] |
| Four-firm ratio | below 40% is competitive; automobiles 46.4%, metals and mining 8.2% (2015) | [PP p.1-2] |
| Public-firm HHI, US | 1,392 (1976), 812 (1996), 1,180 (2016) | [SU p.8-9] |
| Entry and exit | per 100 firms per year, about 11 enter and 10 leave (1977-2010); small firms 12 to 14 and 10 to 12 | [MM p.19-25; CL p.3] |
| Survival | establishments 75% at 1 year, 45% to 50% at 5 years; under 50% of public firms reach 10 years | [MM p.19-25] |
| Entrants | about one third of incumbent size; about 80% exit within 10 years | [MM p.19-25] |
| Deterrence used often | advertising 62%, R&D and patents 56%, reputation 27%, learning curve 26%, excess capacity 22% | [MM Exh.17] |
| Variance of abnormal profit, sustaining high performers | industry 44%, corporate parent 19%, segment 34%; low performers: segment 99% | [MM p.10, 1981-94] |
| Listed-firm survival | half-life about 10 years; S&P 500 implied 24 years; Fortune 500 16 years | [CL p.2] |

Barrier checklist [MM p.19-25]: asset specificity, minimum efficient scale against market size, excess capacity, incumbent reputation, precommitment contracts, licenses and patents (time-limited), learning curve, network effects (leaders in consumer products rarely exceed 40% share; with strong network effects above 50% [T15 p.17-19]), exit barriers.

## 6. Interpretation rules
- Two tests for advantage: ROIC above cost of capital, and above peers, over a full cycle [MM p.4]. Both magnitude (spread x capital) and duration (competitive advantage period) are required.
- Industry is not destiny. The best industries contain value destroyers and the worst contain creators [MM p.8; PP p.2]. For below-average firms, own factors explain 90% or more of profit variance [MM p.10].
- Duration is a judgment bounded by base rates: persistence of CFROI over four years by sector (staples 0.78, energy 0.35, see roic.md) and survival statistics above. GAP: the notes give no numeric competitive advantage period in years by industry; the skill states its assumed years and the evidence.
- Excess return fades faster at high returns and heavy reinvestment [MM p.5]. Slow cycles: staples, health care; fast: technology, energy [MC14 p.14-15].
- Concentration needs care: public-firm peer sets are older, larger and survivor-biased [SU], and private rivals are missing. GAP: industry totals and private-firm shares are not in the tearsheet; use broker research or filings, and say when shares cover listed firms only.
- Not applicable or weak for: banks and insurers (ROIC), cyclicals judged on one year (use 3 to 5 year averages [PP p.1]), early-stage and emerging industries (shares unstable), single-executive businesses. Success lists mislead: only 12% of 699 companies named in 19 success books qualified as superior beyond luck [MM p.48-49].
- Never accept a moat from brand, size or share alone.

## 7. Output lines
The skill states, with labels:
1. Unit, life-cycle phase, industry class. Judgment.
2. Industry map table. Reported.
3. ROIC minus WACC over a full cycle, against the company and peers. Derived; WACC assumed.
4. Profit pool today, 5 and 10 years ago; four-firm ratio. Derived.
5. Share stability number and verdict. Derived.
6. Price trend and pricing power evidence. Reported.
7. HHI or four-firm ratio and coverage limits. Derived.
8. Entry and exit evidence, named barriers. Reported, judgment.
9. Five forces verdicts with evidence. Judgment.
10. Source of advantage and the margin-turnover split that supports it. Derived.
11. Disruption verdict. Judgment.
12. Duration assumed, in years, with the evidence and the fade endpoint. Assumed.
13. What the price assumes (reverse DCF) and what would change the view. Derived, judgment.

## 8. Sources
Notes: roic-moat.md (paper E, steps 1 to 6, checklists), tam-leverage-profit-pools.md (sections 1, 2.3, 3 to 5), base-rates.md (2.7). Papers: the seven Mauboussin and Callahan reports tagged above.
