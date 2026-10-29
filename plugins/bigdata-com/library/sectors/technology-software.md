# Technology: software

Scope: application and infrastructure software sold as subscriptions, licenses, usage or transactions. Hardware and semiconductors have their own primer; consumer internet platforms sit in communication services.

## How the sector makes money and the value drivers

Software is a knowledge business: high upfront cost, low cost per extra unit, no direct link between sales and costs, and an advantage that is hard to protect without lock-in or network effects. The value drivers:

- Recurring revenue growth = new customers + expansion within existing customers + price, minus contraction and churn.
- Gross margin: hosting, support and services costs. Subscription gross margin is commonly 70 to 85 percent; services run near break-even.
- Operating margin at scale: sales and marketing and R&D are the real investment, and both are expensed.
- Reinvestment: little tangible capital, so growth is funded through the income statement, not the balance sheet.
- Duration of advantage: switching costs (data, integration, training), network effects and de facto standards. These are the conditions under which returns can rise with scale rather than fade.

## The metrics that matter

| Metric | Definition | Why it matters |
|---|---|---|
| ARR | Annualized value of active recurring contracts, excluding services and uncommitted usage | Base for growth and efficiency ratios; definitions differ by company |
| Net revenue retention (NRR) | (Starting ARR + expansion - contraction - churn) / starting ARR, over 12 months, same cohort | Growth from the installed base; above 100 percent means the base grows without new logos |
| Gross revenue retention (GRR) | (Starting ARR - contraction - churn) / starting ARR | Stickiness with expansion removed; the cleaner test of switching costs |
| Remaining performance obligations (RPO, cRPO) | Contracted revenue not yet recognized; current portion due within 12 months | Leads revenue; length of contracts changes it |
| Billings | Revenue + change in deferred revenue | Demand signal, distorted by billing terms |
| CAC payback | 12 x sales and marketing cost to win a customer / (new ARR x gross margin), giving months | Speed at which growth spending is recovered in cash |
| Rule of 40 | Revenue growth percent + FCF margin percent | Practitioner heuristic |
| SBC / revenue | Stock-based compensation as a share of revenue | A real cost that adjusted margins exclude |

Rough practitioner ranges: NRR of about 100 to 120 percent for established enterprise vendors, above 120 percent for the best cohorts; GRR of about 85 to 95 percent for enterprise, lower for small-business products; CAC payback of about 12 to 36 months; SBC of about 5 to 30 percent of revenue, highest at early stages.

Prefer metrics that are persistent and predictive over popular ones: gross profitability and operating margin persist year to year; one-year sales growth does not.

## What the statements do differently and the accounting traps

- **Expensed investment overstates ROIC.** R&D and customer acquisition are expensed, so invested capital is understated. Capitalize R&D over a short life, about 3 to 5 years for software, before comparing returns. Free cash flow does not change.
- **Negative invested capital.** Deferred revenue is an operating liability netted against operating assets. In a subscription business it can push invested capital below zero and make ROIC infinite and meaningless. Say so and use economic profit or cash returns instead.
- **Cash runs ahead of earnings.** Upfront billing growth flatters cash flow; a slowdown reverses it.
- **Stock-based compensation.** Past awards add shares; future awards belong in the forecast. Do not count one award both as an expense and in the share count. Show margins and FCF with and without SBC.
- **Billing terms.** Moving from monthly to annual billing raises deferred revenue with no change in economics; multi-year prepaid deals inflate RPO.
- **Revenue recognition.** Upfront term licenses make quarters lumpy; gross versus net reporting changes EV/Sales.
- **Excess cash and capitalized development.** Surplus cash left in capital depresses ROIC (use an operating cash allowance of 2 percent of sales, 5 percent for less predictable companies); a rising capitalized share of development cost flatters margin.
- **Acquisitions.** Use EBITA and show ROIC with and without goodwill.
- **Tax.** US tax treatment of R&D moved cash taxes twice: domestic R&D was amortised over five years for tax years 2022 to 2024, and the July 2025 tax act restored immediate expensing of domestic R&D from tax years beginning in 2025, with catch-up deductions for the unamortised balance; foreign R&D stays on 15-year amortisation. Read the company's cash-tax and deferred-tax notes for the year in question.

## Profit pool and competitive dynamics

A profit-pool study of 770 listed software firms (data to June 2016) found a four-firm revenue ratio of 39.3 percent, just under the 40 percent line that marks a competitive industry. The top ten's share of industry invested capital rose from 49 percent (2005) to 55 percent (2010) and 61 percent (2015); in internet software and services it rose from 47 to 71 percent. IT consulting moved the other way (44 to 35 percent). Value has been migrating to the leaders.

The dynamics behind that:

- **Network effects and standards.** In consumer products the leader rarely exceeds 40 percent share; with strong network effects it is generally above 50 percent and often near 90 percent. Only networks where users interact qualify, and most never tip.
- **Minimum efficient scale.** High fixed development cost deters entry.
- **Switching costs** are procedural (training, data migration, integration) more than contractual. GRR and contract length are the evidence.
- **Overshoot and disruption.** Signs: customers use a fraction of the features and refuse to pay for new ones; competition shifts to speed and convenience. A platform shift (on-premise to cloud, possibly AI agents) can act as low-end or new-market disruption.
- **Industry is not destiny.** Every industry holds value creators and destroyers. Explain the dispersion inside the peer set.
- **Peer sets are survivor-biased.** Growth companies stay private longer and acquired names drop out of screens. Build the map and pool with `references/industry-structure.md`.

## Persistence and fade

Historical base rates, not current facts. The sample pools software with hardware and semiconductors under "Information technology"; software-only rates are not separated.

| Measure | Information technology | All sectors | Population and period |
|---|---|---|---|
| Gross profitability, 5-yr r; median | 0.63; 0.39 | staples 0.86, energy 0.61 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Operating margin, 5-yr r; median; mean | 0.62; 13%; 15% | all sectors 1-yr 0.91, 5-yr 0.72 | Same, 1950-2015 |
| CFROI, 4-yr r; median; mean | 0.50; 8.5%; 9.0% | staples 0.78, energy 0.35 | Global, market cap about $250M plus, 1983-2015 |
| CFROI, older cut, 4-yr r; mean | 0.38; 7.7% | | Global, r 1986-2012, means 1990-2012 |
| Operating margin beta, 1-yr / 3-yr | 0.173 / 0.158 | about 0.11 | Top 1,000 global ex financials and utilities, 1950-2015 |
| Sales growth correlation with US real GDP | 0.55 | | Top 1,000 global, 1950-2014 |

Reading: at a four-year r near 0.5, about half of a company's excess CFROI over the sector mean is gone after four to five years, faster than in consumer and health care. The high operating margin beta means larger forecast misses, so widen ranges. Software has had high, persistent median returns on capital (1965 to 2007): the mean stays high even as individual spreads fade. Place any growth claim in its size-and-horizon class from `references/base-rates.md`: for companies with $4.5 to 7bn of sales, a 10-year real sales CAGR of 15 percent or more occurred in 4.2 percent of cases (1950-2015).

## Valuation conventions and their pitfalls

- **High growth** (organic growth above 15 percent a year): use a scenario DCF that starts from a steady state 10 to 15 years out. Size the addressable market at returns above the cost of capital, cap share with a saturated early market, take long-run margins from mature analogues (medians, not means), work back to today and weight the scenarios with base rates (`references/valuation.md`).
- **EV/Sales or EV/ARR** only when profits are negative or unrepresentative. Since EV/Sales = EV/EBITA x EBITA margin, state the long-run margin the multiple implies.
- **EV/EBIT or EV/NOPAT** once margins are representative; P/E only with similar leverage and accounting. Treat SBC as a cost in any FCF yield.
- **PEG** ignores ROIC and makes growth that adds no value look cheap.
- Rule-of-40 premiums and EV/ARR bands by growth rate have no stable standard; if used, build them from a live regression on the current peer set.
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
- Interest rates: long-duration cash flows make value sensitive to the discount rate.
- Currency: use constant-currency growth for vendors with foreign revenue.
- Cloud and AI compute costs: an input cost for vendors that host or run models.
- Regulation: privacy, data residency, antitrust on bundling, AI rules.
- Sales growth tracks GDP only moderately (r 0.55, 1950-2014), so macro-driven forecasts are weaker here than for industrials.
