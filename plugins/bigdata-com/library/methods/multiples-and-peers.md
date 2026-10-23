# Multiples and peers

This method answers three questions about a valuation multiple: is it built consistently and comparable across peers, what does it say about the market's expectations, and what multiple do the company's own returns, growth and risk justify. A multiple is shorthand for a cash-flow model; investors who rely on multiples are "burying" the forecast of cash flows and discount rates, not avoiding it (Mauboussin and Callahan, Cost of Capital, 2013, pp. 2-3). So the method builds every multiple the same way, explains it by value drivers, and reads it as a statement of expectations. It never calls a stock cheap or expensive as a recommendation.

## When a skill loads this file

Comps and peer comparison, valuation snapshots and full valuations (as the cross-check on the DCF), earnings previews and reviews (what is priced in), memos and sector work. Load `references/roic.md` for the returns each peer earns and `references/valuation.md` when a DCF is built. A narrow question ("what is the forward EV/EBITDA against peers") gets steps 1 to 8 for that multiple, with the peer table.

## Inputs

| Input | Where in Bigdata.com | Basis |
|---|---|---|
| Market cap, EV, EV/EBITDA, P/E, FCF yield, net debt | `bigdata_company_tearsheet`, `fundamentals` (key metrics), per peer | reported |
| Statements: debt, cash and securities, minorities, leases, pensions, equity-method investments, attributable net income | `fundamentals` | reported |
| ROIC, ROE, margins, cash conversion | `fundamentals` (ratios) | reported |
| Consensus sales, EBITDA, EBIT, EPS, FCF, long-term growth, with vintage | `estimates` | reported |
| Peer candidates | `bigdata_screen_companies` on sector, size, growth, margin and return; peers named in filings | reported |
| Current figures for a peer set | `bigdata_portfolio_tearsheet` | reported |
| Non-recurring items, JV income, option and share tables, segment profit | `bigdata_search` and `bigdata_fetch_document` on filings | reported |
| Cost of capital | Not in Bigdata.com; see `references/roic.md` | assumed |

Not in the sources: how the tearsheet's enterprise value is built (minorities, pensions, leases, period-end or average net debt) and whether its EBITDA is cleaned. Rebuild EV from the balance sheet for the target and each peer, and say which one is quoted.

## Procedure

1. **Match claimants.** Equity multiples (P/E, P/B) set parent-shareholder value against a metric after debt, minorities and preferred; P/E uses net income attributable to the parent. Price 5,600 over consolidated net income of 468 gives 12.0x; over attributable income of 298 it gives 18.8x (Robinson and Weyns, Multiples, 2017, p. 12). Enterprise multiples (EV/EBITDA, EV/EBITA, EV/Sales) put every claimant in the numerator. Done when each multiple is labelled equity or enterprise.
2. **Build EV at market values.** Market cap plus debt (at fair value if yields have moved), preferred, minorities, unfunded pensions, leases and options, less non-operating assets at market value (excess cash, equity stakes, excess real estate). Use average or seasonally adjusted net debt, adjusted for changes in the group (p. 9). If the metric is before rent, EV includes leases; if after rent, it excludes them. Example with EBITA of 100 and core value of 900: a company with 100 of excess cash and a 200 equity stake has debt plus equity of 1,200; the right multiple is (1,200 - 300) / 100 = 9.0x, against 12x on debt plus equity and 11x on debt plus equity less cash (McKinsey ch. 14). Done when the EV bridge is shown, built the same way for every peer.
3. **Pick the EV flavor and match the metric.** Total EV (all activities), operating EV (less non-operating assets), core EV (less non-core assets, with a core metric) (p. 7). Done when the flavor is stated.
4. **Clean the metric.** Remove non-recurring and non-core items or the multiple capitalizes them: a 1,707 restructuring charge left in EBITDA at 12x understates EV by about 20,500 (12 x 1,707) (pp. 15-20). Add back non-recurring expenses, deduct non-recurring income. If the cash cost is unpaid, put its present value in the equity bridge. Remove equity-accounted JV income from EBITDA, value the stake separately and add it in the bridge: an EV/EBITDA of 12.1x became 14.0x when JV value was left in (pp. 25-26). Find items on the face of the income statement, in other income and expense, the operating-profit notes, the earnings-to-cash-flow reconciliation, and by text search for restructuring, impairment, write-down and integration. Count how many of the last five years carry a "one-time" charge; recurring ones are costs. Done when reported and cleaned metrics sit side by side.
5. **Choose the multiple and the base** from the table below. Bases: historical (average price over past profit, for trading ranges), current (price over trailing and one or two forecast years), forward (price x (1 + cost of capital) - investor cash flow), partial-forward (current equity value with forecast net debt) (p. 62). Prefer forward multiples: historical E/P had 1.6 times the dispersion of forward E/P (6.0 against 3.7 percent), and IPO pricing error fell from 55.0 percent on historical to 28.5 percent on two-year forward earnings (McKinsey ch. 14). Prefer EV/EBITA to EV/EBIT (acquired-intangible amortization is an accounting artifact) and to EV/EBITDA where capital intensity or outsourcing differs. Done when the multiple and base are stated, the same for all peers.
6. **Compute operating metrics for every peer** on the same basis: growth, ROIC, margin, cash conversion, leverage. Done when the table is complete.
7. **Select peers by value drivers.** Two routes: industry classification, and the fundamentals that drive value (growth, margin, ROIC, turnover, leverage, capital intensity). Build both and report how many classification peers survive; a firm in another industry can be closer on drivers than one in the same industry (How Well Do You Compare, 2017, pp. 7, 10-12). Match cash generation, risk, value-added growth, size, product mix, geography, business model, life-cycle stage, organic against acquired growth (Multiples, pp. 24-27). Compare business models, not lines of business: Apple and Edison International both traded at 12.8x earnings in 2013 with CFROI of 25 and 5 percent (Mauboussin and Callahan, P/E, 2014, pp. 2, 14). State the selection rule before showing multiples, because analysts tend to pick high-multiple peers when arguing a stock is cheap (Compare, p. 7). Done when each peer has a reason.
8. **Summarize with the median**, not the mean, and show the result with and without any outlier (Multiples, p. 45; Compare, p. 7). A relative multiple (company over market or sector) or a comparison with the company's own history is valid only if returns, growth, rates, risk premium, tax and accounting are unchanged, or measured at a comparable point in the cycle (P/E, p. 11; Multiples, p. 24). Done when median, range and the target's premium or discount are shown.
9. **Explain the multiple.** Compare the target and peers on ROIC minus WACC, growth and risk; compute the justified multiple from the formulas below and split the actual multiple into a steady-state part (1/cost of equity for P/E, 1/WACC for EV/NOPAT) and the part paid for value creation, in turns. Done when the gap between actual and justified multiple is stated in turns with the driver that explains it.
10. **Cross-check with the DCF.** Back out the multiples the DCF implies, static and rolling; the implied terminal multiple should be below today's (Multiples, pp. 47-49). Done when both are reported.

## Formulas

- Returns form: EV / NOPAT = (1 - g / ROIC) / (WACC - g); EV / EBITA = (1 - T) x (1 - g / ROIC) / (WACC - g), T = operating tax rate (McKinsey ch. 14). At ROIC = WACC growth adds nothing.
- One-stage cash form: EV / EBITDA = [FCFF x (1 + g) / (WACC - g)] / EBITDA, which separates cash conversion, risk and growth (Multiples, pp. 21-22).
- Linking identities: EV / IC = EV / NOPAT x ROIC; P/B = P/E x ROE; EV / Sales = EV / EBITA x EBITA margin; value / earnings = value / capital x 1 / ROIC (McKinsey ch. 15).
- Single-stage P/E = (ROE - g) / [ROE x (COE - g)], COE = cost of equity. ROE = COE gives 1 / COE whatever the growth; ROE 12 percent, g 5 percent, COE 10 percent gives 11.7x. Single-stage forms overstate; prefer two stages (Multiples, pp. 66-67).
- Two-stage EV = NOPAT x (1 - gA / RONIC-A) / (WACC - gA) x [1 - ((1 + gA) / (1 + WACC))^N] + NOPAT x (1 + gA)^N x (1 - gB / RONIC-B) / [(WACC - gB) x (1 + WACC)^N], value-adding growth gA for N years, then gB below WACC (McKinsey ch. 10).
- Steady-state P/E = 1 / COE. Declining business: steady-state value = NOPAT x (1 + g) / (cost of capital - g), g negative; NOPAT 100, cost of capital 10 percent, decline 10 percent a year gives 450, a 4.5x multiple (P/E, pp. 4, 8).
- Warranted forward P/E = sum over t = 1 to N of (1 + g)^(t-1) x (1 - g / ROIIC) / (1 + k)^t, plus (1 + g)^N / k / (1 + k)^N, with k = cost of capital, N = 15 years, year-one earnings of 1 (reconstruction verified against P/E paper Exhibit 5).
- Adjusted PEG = EV multiple / (100 x expected EBITA growth) (McKinsey ch. 14).
- Banks: P/B = (ROE - g) / (ke - g); P/E = (1 - g / ROE) / (ke - g) (McKinsey ch. 36, 15).

## Reference tables

Which multiple (Multiples, pp. 50-62):

| Multiple | Use when | Watch for |
|---|---|---|
| EV/Sales | losses; restructuring candidates | margin differences; revenue recognition |
| EV/EBITDA | peers with similar capital intensity | ignores capex; invalid across sectors |
| EV/EBIT or EV/EBITA | capital intensity differs | depreciation policy; acquired amortization (use EBITA) |
| EV/NOPAT | a degeared P/E; tax differences | subjective adjustments |
| EV/FCF | smoothed, normalized FCF | lumpy cash flow |
| P/B, EV/IC | asset-heavy businesses and banks, always beside ROE or ROIC | historical-cost book values |
| P/E | clean earnings, similar leverage | negative earnings; leverage |
| PEG | within a sector, similar returns | ignores ROIC; growth without a spread looks cheap |
| EV per unit of capacity or subscriber | same-industry checks against replacement cost | says nothing about profitability |

Warranted forward P/E at an 8 percent cost of capital, 15-year horizon (Mauboussin and Callahan, P/E, 2014, Exhibit 5):

| Earnings growth | ROIIC 4% | 8% | 16% | 24% |
|---|---|---|---|---|
| 4% | 7.1x | 12.5x | 15.2x | 16.1x |
| 6% | 3.3x | 12.5x | 17.1x | 18.6x |
| 8% | NM | 12.5x | 19.4x | 21.8x |
| 10% | NM | 12.5x | 22.4x | 25.7x |

The same 15.0x can mean 12 percent growth at an 8.8 percent ROIIC, 6 percent at 11.0, or 3 percent at 23.0 (Exhibit 6).

Dated benchmarks (verify; recompute from the current risk-free rate and implied equity risk premium):

| Item | Figure | Source |
|---|---|---|
| Steady-state P/E | 12.5x at an 8 percent cost of equity (Jan 2014); 1961-2013 average 10.4x, standard deviation 2.7 | P/E paper, p. 4 |
| Forward EV/EBITA, S&P 500 non-financials | most between 7x and 11x (Dec 2009) | McKinsey ch. 14 |
| EV/EBITA by peer type | low growth, low margin 7x; low growth, high margin 9x; high growth, high margin 11x to 13x | McKinsey ch. 14, Exhibit 14.8 |
| Value and returns | 4 percent growth at ROIC 15 percent: 2.5x capital, 10.6x EBITA; at ROIC 10 percent: 1.5x capital, 9.6x EBITA | McKinsey ch. 15, Exhibit 15.4 |

## Interpretation and limits

- A P/E below 1 / COE, or EV/NOPAT below 1 / WACC, means the market prices no value creation or expects earnings to fade; it does not by itself mean a bargain (P/E, pp. 4, 12).
- Earnings multiples hide ROIC differences, especially at low growth (the 2.5x against 1.5x capital example is only 10.6x against 9.6x EBITA); show value to invested capital beside earnings multiples (McKinsey ch. 15).
- Do not chart multiples against growth linearly; use multiples against ROIC or ROE (Multiples, p. 45).
- Leverage: when the unlevered P/E is below 1 / cost of debt, P/E falls as leverage rises (McKinsey App. E). Use EV multiples when leverage differs.
- EBITDA multiples mislead across outsourcing: identical businesses traded at 6.0x and 8.6x EBITDA and both at 10x EBITA (McKinsey ch. 14). A high multiple on depressed earnings is not overvaluation: Home Depot was 13.0x forward EBITA, 8.0x at 2005 margins.
- PEG has no standard growth window, assumes value is linear in growth with a zero intercept, and ignores ROIC; use it only within a sector.
- Listed peer sets are smaller, older and survivor-biased; for niche industries widen to global listings or adjacent sub-industries and say so (Shrinking Universe, 2017, as interpreted in the TAM and profit pools note).
- Banks: no EV multiples; compare P/B against ROE, and a premium to book needs ROE above the cost of equity. Cyclicals: normalize to mid-cycle earnings first; consensus for cyclicals tends to ignore the cycle, so a forward P/E looks low at the peak and high at the trough (McKinsey ch. 35). High growth with losses: forward EV/Sales with the long-run margin stated. Emerging markets: share prices are weaker anchors; triangulate (McKinsey ch. 33).
- A multiple is a check on a forecast, never a substitute (McKinsey ch. 14).
- Not in the sources: a minimum number of peers. State the count and test the median with and without the closest and most distant peer.

## Output lines

- Multiple, base and definition for the target and each peer, labelled equity or enterprise. Basis: derived from reported.
- EV bridge, every item, the same for each peer. Basis: reported and derived.
- Reported and cleaned metric with the items removed and their source. Basis: reported, derived.
- Peer table: multiple, growth, ROIC, margin, leverage, selection reason. Basis: derived; reason judgment.
- "The company trades at X against a peer median of Y (range A to B), a Z percent premium; without [outlier] the median is W." Basis: derived.
- "At an assumed cost of capital of k, a steady-state multiple is S; the remaining T turns price in value creation." Basis: assumed and derived.
- "The company's ROIC, growth and risk justify about J; the gap of G turns is explained by [driver]." Basis: assumed inputs, derived output.
- "The DCF implies a terminal multiple of M against N today." Basis: derived.

## Sources

- Notes: expectations-multiples-dcf.md (sections 1.3, 2.1 to 2.7, 5, 6); mckinsey-part1.md (chapters 10, 14, 15); mckinsey-part2.md (chapters 33, 35, 36, Appendix E); skill-market-structure.md (How Well Do You Compare); tam-leverage-profit-pools.md (5.3).
- Robinson, D. and Weyns, G., "How to analyse and talk the language of multiples", UBS, 16 Mar 2017, pp. 7-70 (cited as Multiples).
- Mauboussin, M. and Callahan, D., "What Does a Price-Earnings Multiple Mean?", Credit Suisse, 29 Jan 2014, pp. 2-21 (cited as P/E).
- Mauboussin, M. and Callahan, D., "Estimating the Cost of Capital", Credit Suisse, 2013, pp. 2-3.
- Mauboussin, M., "How Well Do You Compare?", BlueMountain, Dec 2017, pp. 3-12.
- Mauboussin, M. et al., "The Incredible Shrinking Universe of Stocks", Credit Suisse, Mar 2017.
- Koller, T., Goedhart, M. and Wessels, D., Valuation, 5th ed., McKinsey, 2010, chapters 10, 14, 15, 33, 35, 36 and Appendix E.

<!-- Spec vs notes: 12 x 1,707 is 20,484; the UBS source and the spec print 20,490 from unrounded inputs, so the file says "about 20,500". The spec's worked check from Multiples Figure 60 (9.9x and 12.8x) is omitted because the note does not carry the EBITDA behind it. -->
