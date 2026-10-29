# Capital allocation as tests

Whether management turns cash into long-term value per share, not into growth, earnings per share or a higher share price. Most actions are sound at one price and unsound at another, so every test compares what was paid with what was received.

## Inputs

| Input | Where it comes from |
|---|---|
| CFO, capex, depreciation, acquisitions, divestitures, working capital, dividends, buybacks, issuance, stock compensation, debt, gross and net PP&E, invested capital, ROIC, market cap, EV | Company statements, ratios and key metrics |
| Deal price, premium, synergies, payment form, integration cost | The tearsheet's M&A section, then a search for each announcement |
| Prices around announcements and over the buyback years | Tearsheet overview; daily series from the computing tool |
| Repurchase actuals, proxy incentive terms, insider sales | A search over filings, then the full document |
| CEO changes | Leadership section of the tearsheet |
| Cost of equity and of capital, value per share by year | Not in the data. State each once with a one-point sensitivity (valuation.md, cost of capital) |

## Sources and uses

Tabulate five years. Sources: CFO, net debt issued, equity issued, divestiture proceeds. Uses: capex, acquisitions, increase in working capital, dividends, buybacks, debt repaid, change in cash. Show R&D as a memo line; it sits inside CFO.

FCF = NOPAT - investment, where investment = change in net working capital + (capex - depreciation) + (acquisitions - divestitures).

## Spending pattern

Incremental rate = each investment component / change in sales, for working capital, net fixed capital and net M&A, over three and preferably five to ten years. Compare with the company's own history and named peers, and mark inflection points and CEO changes.

## Order of the tests

Each dollar belongs in the use with the highest expected return above the cost of capital. Test organic reinvestment first, then deals, then payouts, then debt repayment. This orders the tests; it does not rank the uses.

## Organic reinvestment

- ROIC = NOPAT / average invested capital.
- ROIIC = (NOPAT(t) - NOPAT(t-1)) / (IC(t-1) - IC(t-2)), as a three-year rolling figure, the longest window five annual periods allow (roic.md, ROIIC and the spread).
- Implied growth = reinvestment rate x ROIIC. Growth without outside funding = ROE x (1 - payout); actual growth well below it means cash the business cannot use.
- Growth capex = capex - depreciation, as a share of capex.
- Asset life = gross PP&E / depreciation; asset age = life x (1 - net PP&E / gross PP&E).

Compare the three-year rolling ROIIC with the cost of capital and read the result as expectations.md, which revision moves value, sets out; use the one-year series only for direction. Judge value creation on growth capex only, not on capex against peers. High asset growth predicts low later returns in developed markets, weakly in emerging ones.

## Buybacks

For each year: amount repurchased (actuals, not authorisations), average price, value per share at the time, shares issued in the same year and the net change in share count.

- Buyback return = ke / (P / IV), with ke the cost of equity, P the price paid and IV value per share at the time. At ke of 8 percent and P / IV of two-thirds, the return is about 12 percent.
- Value per share after a buyback = (V - C) / (N - C / P), with V firm value before, C cash spent and N shares before.
- EPS breakeven P/E = 1 / [r x (1 - t)], with r the pre-tax yield on the cash used or the pre-tax cost of debt raised and t the tax rate. Cash at 3 percent and 33 percent tax gives 50; debt at 6 percent gives 25. Buying below that P/E raises EPS, which says nothing about value.
- Net shareholder yield = (dividends + buybacks - issuance) / average market cap. Net equity issuance ratio = issuance / purchases - 1.

Lay the record against the valuation path: did buying rise when the stock was dear and stop when it was cheap? Name the funding source, the motive (fair value, below value, or an accounting effect) and any insider selling during buybacks.

A buyback creates value for continuing holders only below value and with no better use; above value it transfers value to sellers. Judge price against value at the time of purchase, not by the later price. Neither EPS accretion nor offsetting stock compensation is value creation. Companies tend to buy high: S&P 500 buybacks fell more than 75 percent from 2007 to 2009 while dividends fell 20 percent. Issuance has cut US shareholder yield by 140 basis points on average, range 70 to 310.

## Dividends

Compute coverage by free cash flow after stock compensation, maintenance and growth needs; judge it on trend and funding source (free cash flow, debt, offshore cash or new equity). A dividend paid from debt or new equity is a false signal, and stressed companies are almost always late to cut. Use total and net shareholder yield, not dividend yield.

Total shareholder return = g + (1 + g) x d, with price growth g and dividend yield d reinvested.

## Acquisitions

For each deal in the last five years:

- Premium = (offer - undisturbed price) / undisturbed price, using the price before rumours.
- PV synergies = gross synergy x (1 - t) / cost of capital, discounted for phasing, less disclosed integration cost.
- Deal NPV = PV synergies - premium paid. Predicted buyer move in a cash deal = NPV / buyer market cap; set it against the actual one-, three- and five-day move.
- Shareholder value at risk (SVAR): cash deal = premium / buyer market cap; stock deal = premium / (buyer cap + seller cap + premium). Premium at risk in a stock deal = the share of the premium the seller loses if no synergies arrive.
- Return on price paid = (target NOPAT + improvements) / total price paid; it should exceed the cost of capital.

Add the payment form, the strategic category with its success rate, and the fit with the five archetypes that create value: improve the target, remove excess capacity, accelerate market access, buy skills faster than building them, pick winners early. A deal that fits none rarely creates value. Later impairments and disposals of acquired units reveal overpayment.

Haircut cost synergies and cut revenue synergies far more. Integration often costs a year or more of savings; savings missed in the first full budget year may never come. A strong operator, a low premium and a sole bidder predict success; EPS accretion, relative P/E and relatedness do not. Serial acquirers and late-cycle deals do worse.

**Deal success rate by strategic category** (acquisitions classified by strategy, historical)

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

**Deal base rates**

| Statistic | Figure | Population and period |
|---|---|---|
| Deals that fail to create value for the acquirer | About 60% | 302 large US deals, 1995 to 2001 |
| Buyer beat the market | 38%; 50-51%; 42% | US deals 1997 to 2009; 2010 to 2016; 20-year average |
| Value created for the acquirer | A third yes, a third no, a third inconclusive | 1,415 deals, 1997 to 2009 |
| Average premium | 47%, 43%; about 30% typical | US public deals, 2014 and 2016; long-run studies |
| Premium by lasting market reaction | Positive 25.8%, negative 40.5% | US deals, studies to 2016 |
| Buyer 5-day return by payment | Cash +0.7%, stock -3.9%, mixed -4.1% | US deals, studies to 2016 |
| EPS accretion | 86% accretive; 27% of those created value | 95 US deals, studies to 2016 |
| Cost synergies | 86% captured at least 70% of plan | 90 deals |
| Revenue synergies | Almost half under 70% of plan, nearly a quarter under 30% | 90 deals |
| SVAR | Average 5.5%, median 3.2% | 126 US deals, 2015 to 2016 |

**Value per $1 of added revenue by growth type** (consumer goods companies; ranks matter more than levels): new products 1.75 to 2.00; expanding the market 0.30 to 0.75; share gain in a growing market 0.10 to 0.50; share gain in a stable market -0.25 to 0.40; acquisitions 0 to 0.20.

## Divestitures and spin-offs

Set each disposal's price against the unit's value to the company, and list units still earning below the cost of capital. Sellers do better than buyers on average.

## Balance sheet

Place EBIT / interest and debt / total capital on the rating medians below. A reinvestment rate above 1 with a high payout means payouts were financed by borrowing. For FFO to debt, net debt / EBITDA and a full credit view, use credit.md.

**S&P rating medians** (US companies, medians of three-year averages 2011 to 2013; five-year default probability from S&P defaults 1981 to 2003)

| | AAA | AA | A | BBB | BB | B |
|---|---|---|---|---|---|---|
| EBIT / interest (x) | 40.8 | 17.3 | 10.3 | 5.5 | 3.2 | 1.3 |
| Debt / total capital (%) | 2.8 | 17.2 | 30.7 | 41.1 | 50.4 | 72.7 |
| 5-year default probability (%) | 0.12 | 0.33 | 0.75 | 3.84 | 14.45 | 33.02 |

EBITA / interest of about 5 to 11 corresponds to A+ to BBB-. Value barely changes with leverage except below coverage of 2, and too much debt costs more than too little.

**Announcement reactions** (US companies): dividend cut or omission about -9 percent; dividend increase about +2; seasoned equity offering about -3; open-market buyback +2 to +3; tender-offer buyback about +16.

## Incentives

From the proxy, classify each long-term plan metric (absolute or relative TSR, EPS, ROIC, revenue, cash flow) and note the performance period, option expense, clawbacks, repricing and related-party dealings. Judge alignment by one question: which way would the CEO go if the plan and value per share conflict?

**Long-term incentive metrics in use** (250 largest S&P 500 companies, 2014): TSR 58 percent, profit 50, capital efficiency 41, revenue 21, cash flow 13.

## Verdict per use

One line per use: value created, neutral, destroyed or not determinable, with the test that decides it. No composite score.

## Special cases

- Banks and insurers: test payouts against regulatory capital and ROE against the cost of equity.
- Utilities: test rate-base growth against the allowed return.
- Early-stage companies: ROIIC is unstable; use cash burn and funding history.
- Outside the US: ownership and buyback rules drive payout; use home-region base rates.
