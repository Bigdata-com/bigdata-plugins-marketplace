# Industry structure and moat

This method decides whether a company's return above its cost of capital is likely to last, by testing the structure of its industry first and the company's own advantage second, in the sequence of Mauboussin and Callahan's "Measuring the Moat" (2013). A moat has two dimensions: magnitude (the spread over the cost of capital times the capital that can earn it) and duration (how long the spread lasts). Advantage needs two tests passed over a full cycle: a return above the cost of capital, and a return above competitors (pp. 3-4). The output is a balance of evidence, an assumed duration in years and what would change it. It is never a moat rating or score.

## When a skill loads this file

Moat, deep dive, thesis, sector and theme work, and any valuation that sets a competitive advantage period or a fade. Load `references/roic.md` with it: the spread and the margin and turnover split come from there. A narrow question ("does the company have pricing power") gets the relevant step with its evidence, not the full sequence.

## Inputs

| Input | Where in Bigdata.com | Basis |
|---|---|---|
| ROIC, margins, revenue, invested capital for the company and each peer | `bigdata_company_tearsheet`, `financial_statements, financial_ratios, key_metrics` | reported |
| Revenue by product and geography, five years | `revenue_segmentation` | reported |
| Peer candidates | `bigdata_screen_companies`, peers named in filings, `mergers_acquisitions` | reported |
| Industry size and shares, supplier and customer concentration, contract terms, price changes, capacity, entrants and exits | `bigdata_search` (one aspect and one period per call; see the evidence table) | reported |
| Hiring by rivals and entrants | `hiring_trends` section, news | reported |
| Cost of capital | Not in Bigdata.com; see `references/roic.md` | assumed |

Not in the sources and not in the tearsheet: industry totals and private-company shares. Take them from filings or research and say when shares cover listed companies only.

## Procedure

1. **Set the unit and the stage.** Analyze the business unit, not the conglomerate, and aggregate (p. 9). Place it in a life-cycle phase: innovation (rising returns, heavy reinvestment), fading (excess but declining), mature (returns near the cost of capital), subpar (below it), with a reason (p. 4). Class the industry: fragmented, emerging, mature, declining, international, network or hypercompetitive (p. 17, after Barney). Done when the unit, phase and class are stated.
2. **Draw the industry map.** Suppliers, customers, complementors, regulators and potential entrants; firms in order of dominance; payment terms and incentives between them; labor and regulation (p. 11). Done when the map table names each party and how it touches profit.
3. **Build the profit pool.** Width = each firm's share of industry invested capital, height = ROIC minus WACC, area = economic profit. Use three to five year averages, for today and five and ten years ago (p. 13; Profit Pools 2016, pp. 1-2). Add the four-firm revenue ratio and the top-ten share of capital. Read it as: is the pool positive on average, who holds the width, are high-spread firms gaining width or only spread, which wide firms destroy value. Done when the table shows who gained or lost width and spread.
4. **Test share stability** (formula below). Done when one number and a verdict are stated.
5. **Test pricing power.** Five-year price trend of the product; split each margin change into price, mix and volume (p. 16; Operating Leverage 2016, pp. 8-10). Stable or rising prices go with a stable, slow-cycle industry, falling prices with a fast-cycle one. Ask whether the industry passed on supplier cost increases. Done when the price evidence is dated and cited.
6. **Test rivalry.** HHI or four-firm ratio; similarity of goals and ownership (public, private, private equity); asset specificity, which keeps firms in; demand variability with high fixed costs, which brings capacity at the peak and price wars in the trough; industry growth, since slow growth makes share gains zero-sum (pp. 25-27). Done when each item has evidence or a gap.
7. **Test entry and exit first among the forces.** Threat of entry is the most important force (pp. 19-25), so test barriers before the rest: where they are low, entry pushes returns toward the cost of capital whatever the other forces show. Use the base rates and the barrier list below. An entrant weighs the incumbent's likely reaction (asset specificity, scale, excess capacity, reputation) and its own payoff (precommitment contracts, patents, learning curve, network effects). Done when barriers are named with evidence and recent entrants and exits are listed.
8. **Run the remaining forces as root-cause tests**, not as an attractiveness label (p. 18):
   - Suppliers: more concentrated than the industry; no substitutes; high switching cost; the industry is a small share of their sales; the input is critical; credible forward integration.
   - Buyers: concentration against sellers; the product's share of the buyer's cost; differentiation; switching cost; information; credible backward integration; price sensitivity of end users.
   - Substitutes: other ways to do the same job, their price and performance, switching cost and how fast they are improving. Substitutes set a ceiling on price.
   Done when each force has a one-line verdict with its evidence.
9. **Map the value chain** by discrete activity (R&D, supply chain, operations, marketing and sales, service) and compare with peers. A chain that looks like the peers' means competition to be the best, and price wars (p. 33). Value created = willingness to pay minus opportunity cost (p. 32). Done when the activities that differ from peers are named.
10. **Identify the source of advantage and test it against the numbers** (pp. 34-41):
    - Production: process (indivisibility, complexity, rate of cost decline, legal protection, unique resources) and scale (distribution, purchasing, R&D, advertising). Signature: lower gross margin, high asset turnover. Scale is mostly local or regional (Total Addressable Market 2015, p. 16).
    - Consumer: habit, experience goods, switching costs and lock-in, network effects. Signature: high gross margin. Switching costs are financial (fees, implementation), procedural (training, data migration, integration) and relational; gather retention, churn and contract length where disclosed.
    - External: subsidies, tariffs, quotas, licenses, regulation.
    - Efficient scale: a market that supports only a few profitable firms at minimum efficient scale; the advantage belongs to whoever holds the position.
    A brand counts only if it raises willingness to pay or lowers supplier cost; two of the ten owners of the top ten brands missed their cost of capital (pp. 46-47). Done when ROIC split into margin and turnover over five to ten years matches the claimed source.
11. **Test interaction and disruption.** Capacity and price behavior of rivals: a repeated game with clear signals is stable, a single-play capacity race is not (pp. 42-45). Classify innovation as sustaining, low-end disruptive or new-market disruptive; ask whether products overshoot customer needs, whether competition is shifting to speed and convenience, and whether components are modularizing (pp. 27-31). Done when one verdict is written.
12. **Conclude on magnitude and duration** with the rules below. Done when the duration in years, its evidence, the fade endpoint and what would change the view are stated.

Evidence to search, one aspect per call:

| Step | Search for | Documents |
|---|---|---|
| 2, 8 | named suppliers, customers, regulators; customer concentration; contract terms | filings (business, risk factors), transcripts |
| 3, 4 | industry size, shares, peer results | research, filings, news |
| 5 | price increases, volume response, discounting, mix | transcripts, news |
| 6, 7 | capacity additions, entrants, exits, deals, price wars | news, transcripts, M&A history |
| 10 | retention, lock-in, scale economics, patents and expiries | filings, transcripts |
| 11 | low-price entrants, new-market products | news, research, job postings |

## Formulas

- Share stability = (1/N) x sum over competitors of |share(t) - share(t-5)|, in percentage points, N = number of competitors (pp. 15-16).
- HHI = 10,000 x sum of squared market shares (as fractions) of the 50 largest firms. Shares of 40, 30, 20 and 10 percent give 3,000 (pp. 25-26).
- Four-firm ratio = revenue share of the four largest firms (Profit Pools, p. 1).
- Economic profit = invested capital x (ROIC - WACC); a $200m capital base at a 5-point spread is $10m (p. 13).
- Learning curve: unit cost falls by a fixed share each time cumulative output doubles; about 20 percent for the median product (pp. 19-25). Project cost from cumulative production, not from time, and state a floor set by input costs (Trancik interview, 2017, pp. 4-5).

## Reference tables

All dated; quote with the period and "(verify)".

| Item | Threshold or base rate | Source |
|---|---|---|
| Share stability | 2.0 points or less over five years is stable; carbonated drinks 2, PCs 3, storage 4, smartphones 9 (2007-2012) | Moat, pp. 15-16 |
| Price trend, per year, 2006-2011 | ammunition +9.5%, pet food +5.8%, caskets +5.7%; semiconductors -8.6%, audio and video -1.9%, fiber optic -1.7% | Moat, p. 16 |
| Price elasticity | 1% price change, 1.76% demand change on average (about 370 goods) | Operating Leverage, pp. 8-10, citing Tellis 1998 |
| HHI | above 1,800 suggests reduced rivalry; breakfast cereal 2,425, snack food 1,984, tires 1,540 (2007 Census) | Moat, pp. 25-26 |
| HHI, US public companies | 1,392 (1976), 812 (1996), 1,180 (2016) | Shrinking Universe 2017, pp. 8-9 |
| Four-firm ratio | below 40% competitive; tobacco 71.8%, household products 65.5%, automobiles 46.4%, software 39.3%, banks 15.6%, chemicals 14.3%, metals and mining 8.2% (global listed, 2015) | Profit Pools 2016 |
| Entry and exit | per 100 US firms a year, about 11 enter and 10 leave (1977-2010); small firms 12 to 14 enter and 10 to 12 leave | Moat, pp. 19-25; Longevity 2017, p. 3 |
| Survival | establishments: 75% at one year, 45 to 50% at five; under half of public companies reach ten years | Moat, pp. 19-25; Longevity, p. 2 |
| Entrants | about one third of incumbent size; about 80% exit within ten years; survivors more than double relative size | Moat, pp. 19-25 |
| Listed-company life | half-life about 10 years (1975-2009); implied S&P 500 tenure 24 years (1958-2016); Fortune 500, 16 years | Longevity, p. 2 |
| Deterrence used frequently, new products | advertising 62%, R&D and patents 56%, reputation 27%, learning curve 26%, excess capacity 22%, limit pricing 8% | Moat, Exhibit 17 |
| Market share with and without network effects | consumer-product leaders rarely above 40%; strong network effects generally above 50% | Total Addressable Market, pp. 17-19 |
| Market-implied competitive advantage period | about 8 years on average, about 5 in very competitive industries to about 15 in stable ones (1976-2007) | P/E paper 2014, p. 11, citing Olsen |

Share of abnormal-profit variance explained, US businesses 1981-1994, about 58,000 firm-years (McGahan and Porter, in Moat, p. 10):

| Factor | Sustaining, high performers | Sustaining, low performers | Emerging, high | Emerging, low |
|---|---|---|---|---|
| Year | 3% | -7% | 2% | -5% |
| Industry | 44% | 12% | 37% | 13% |
| Corporate parent | 19% | -4% | 18% | 2% |
| Segment-specific | 34% | 99% | 43% | 90% |

Barrier checklist (pp. 19-25): asset specificity; minimum efficient scale against market size; excess capacity; incumbent reputation; precommitment contracts; licenses and patents (time-limited); learning curve; network effects (real only where users interact, as in payments or marketplaces; hub-and-spoke networks such as airlines are weak; Total Addressable Market, pp. 17-19); exit barriers.

## Interpretation and limits

- Industry is not destiny: the best industries contain value destroyers and the worst contain creators (p. 8; Profit Pools, p. 2). Industry is the largest single factor in sustaining high profits (44 percent of the variance); for below-average firms, segment-specific factors explain 90 percent or more. Show the dispersion inside the industry.
- Duration is a judgment bounded by base rates: the sector's four-year CFROI persistence in `references/roic.md` (staples 0.78 slowest, energy 0.35 fastest), listed-company half-life of about 10 years, and the market-implied period of about 8 years. A claim of a longer period needs moat evidence from steps 7 to 11.
- Excess returns fade faster at high return levels and heavy reinvestment, and the average period of excess returns has been shrinking (p. 5). Slow-fade sectors: staples, health care; fast: technology, energy (Calculating ROIC 2014, pp. 14-15).
- Never accept a moat from brand, size or market share alone. Require the spread over a full cycle and against peers, the margin and turnover signature, barrier evidence and the duration assumed.
- Warning signs of erosion: loss of pricing power (costs not passed through), share lost to entrants in core segments, rising customer concentration, ROIC falling while revenue grows, rivals copying faster, staff leaving for competitors, suppliers or distributors integrating.
- Check analogies. For any "this is the next X" claim, search beyond the first example, name the condition that made the analogy work and test whether it holds here (Boeing 787 outsourcing copied computing, where modularity existed; How Well Do You Compare 2017, pp. 3-4). Take base rates from the relevant regime, not one long average (Triple Crown 2015, p. 2).
- Peer sets of listed companies are older, larger and survivor-biased, and private rivals are missing (Shrinking Universe 2017); state the coverage of any concentration figure.
- Success lists mislead: of 699 companies named in 19 success books, 12 percent qualified as superior beyond luck (Moat, pp. 48-49). A moat that depends on one executive is not a moat (Buffett, cited p. 51).
- Weak or not applicable: banks and insurers (judge ROE against the cost of equity), cyclicals judged on one year (use three to five year averages), emerging industries where shares are unstable.
- Not in the sources: a numeric competitive advantage period by industry. State the assumed years and the evidence.
- Not in the sources: a minimum sample for a valid share-stability or HHI reading. Say how many firms and what share of the market the figure covers.

## Output lines

1. "Unit: [segment]; life-cycle phase: [phase], because [reason]; industry class: [class]." Basis: judgment.
2. Industry map table: party, role, concentration, terms, source. Basis: reported.
3. "ROIC minus WACC over [years] averaged S points for the company against P for the peer median." Basis: derived, WACC assumed.
4. Profit pool table for today, five and ten years ago; four-firm ratio. Basis: derived.
5. "Average absolute share change over five years: X points, [stable or unstable] against the 2.0-point rule (Measuring the Moat, 2007-2012 data)." Basis: derived.
6. "Prices [rose or fell] X percent a year over [period]; the margin change split into price A, mix B and volume C points." Basis: reported and derived.
7. "HHI of H (or four-firm ratio R), covering [listed firms only or the full market]." Basis: derived.
8. Entry and exit: entrants and exits in five years, barriers named with evidence. Basis: reported, judgment.
9. Five forces table: force, verdict, evidence, source. Basis: judgment.
10. "Source of advantage: [type]; supported by margin M and turnover T against peers." Basis: derived.
11. "Disruption: [sustaining, low-end or new-market], evidence [ ]." Basis: judgment.
12. "Assumed duration: N years, fading to [sector median or WACC], because [evidence]; base rates: [sector r], listed half-life about 10 years." Basis: assumed.
13. What the price assumes (from `references/expectations.md`) and what would change the view. Basis: derived, judgment.

## Sources

- Notes: roic-moat.md (paper E, steps 1 to 6 and the checklist); tam-leverage-profit-pools.md (sections 1.5, 2.3, 3, 4, 5); skill-market-structure.md (How Well Do You Compare, Triple Crown, energy cost curves); expectations-multiples-dcf.md (1.1, market-implied CAP); old skill bigdata-moat-governance-review references porter-five-forces.md and moat-taxonomy.md.
- Mauboussin, M. and Callahan, D., "Measuring the Moat: Assessing the Magnitude and Sustainability of Value Creation", Credit Suisse, 22 July 2013, pp. 3-55 (page references without a title are to this paper).
- Mauboussin, M. and Callahan, D., "Calculating Return on Invested Capital", Credit Suisse, 2014, pp. 12-15.
- Mauboussin, M. et al., "Global Industry Profit Pools", Credit Suisse HOLT, July 2016; "Total Addressable Market", Sep 2015; "Operating Leverage", June 2016; "Corporate Longevity", Feb 2017; "The Incredible Shrinking Universe of Stocks", Mar 2017.
- Mauboussin, M. and Callahan, D., "What Does a Price-Earnings Multiple Mean?", Credit Suisse, Jan 2014, p. 11.
- Mauboussin, M., "How Well Do You Compare?", BlueMountain, Dec 2017; "Triple Crown Teachings", 2015; "Coming Clean with Energy Cost Curves" (Trancik interview), Jan 2017.
- Kept from the previous moat skill's five-forces and moat-taxonomy references: the per-force diagnostic questions, the entry-first ordering, the switching-cost categories, efficient scale and the erosion signs. Its scoring weights, moat ratings and competitive-advantage-period tables were dropped because no source supports them.

<!-- Spec vs notes: the spec lists the four-firm ratio rule with automobiles and metals only; the Profit Pools note gives more industries, added here. No numeric conflicts found. The market-implied CAP of about 8 years (P/E paper, in the expectations note) partly answers the spec's duration GAP; the GAP is kept for industry-specific periods. -->
