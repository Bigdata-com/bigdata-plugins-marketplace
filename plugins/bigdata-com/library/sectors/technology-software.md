# Technology: software

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
- **Acquisitions.** Use EBITA and show ROIC with and without goodwill (McKinsey ch.26).
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
8. Which competitors appear in lost deals, and is any entrant pricing below you?

## What to watch at the macro level

- Enterprise IT budgets and hiring: seat-based pricing tracks customer employment.
- Interest rates: long-duration cash flows make value sensitive to the discount rate (judgment).
- Currency: use constant-currency growth for vendors with foreign revenue.
- Cloud and AI compute costs: an input cost for vendors that host or run models.
- Regulation: privacy, data residency, antitrust on bundling, AI rules (verify per market).
- Sales growth tracks GDP only moderately (r 0.55, 1950-2014), so macro-driven forecasts are weaker here than for industrials (Operating Leverage, 2016).
