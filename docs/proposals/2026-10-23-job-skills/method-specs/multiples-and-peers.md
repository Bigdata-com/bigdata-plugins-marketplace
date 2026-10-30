# Multiples and comparable companies, done consistently

Purpose: answer "is this multiple comparable, what does it say about expectations, and what multiple do the company's own returns, growth and risk justify". Used by the valuation snapshot, peer comparison, memo and earnings jobs. A multiple is shorthand for a cash-flow model, so the method builds it consistently, explains it by value drivers, and reads it as a statement of expectations. It gives no recommendation.

## Inputs
- Reported (tearsheet per peer): market cap, EV, EV/EBITDA, P/E, net debt (key metrics); statements, minorities, leases, pensions where reported; ROIC, ROE, margins (ratios); revenue segments.
- Consensus (estimates): forward EBITDA, EBIT, EPS, sales, long-term growth.
- Peer list: screen_companies on sector, size, growth and margin, then narrow by value drivers (step 7). GAP: the notes give no minimum peer count.
- Filings (search, fetch_document): income-statement notes for non-recurring items, JV income, attributable net income, option tables.
- Assumed: cost of capital (no field exists; see valuation spec). GAP: the notes do not say how the key_metrics EV is built (minorities, pensions, leases, average or period-end net debt) or whether EBITDA is cleaned. Verify per ticker and rebuild EV from the balance sheet.

## Procedure
1. Match claimant groups. Equity multiples (P/E, P/B) use parent-shareholder price over a metric after debt, minorities and preferred: P/E must use net income attributable to the parent (MULT p.12 example: price 5,600 over consolidated income 468 gives 12.0x, over attributable income 298 gives 18.8x). Enterprise multiples (EV/EBITDA, EV/EBIT, EV/Sales) put all claimants in the numerator. Done: each multiple labelled equity or enterprise.
2. Build EV at market values: market cap, plus debt at fair value if yields moved, preferred, minorities, deemed debt (unfunded pensions, leases), options, less non-operating assets at market (excess cash, JV stakes, excess real estate). Use average or seasonally adjusted net debt, adjusted for group changes (MULT p.9; McKinsey ch.14). If the metric excludes lease cost (EBITDA before rent), EV must include leases, and the reverse. Done: EV bridge, same for target and every peer.
3. Pick the EV flavour and match the metric: total EV (all activities), operating EV (less non-operating assets), core EV (less non-core assets, with a core metric) (MULT p.7). Done: flavour stated.
4. Clean the metric. Remove non-recurring and non-core items; otherwise the multiple capitalises them (a 1,707 restructuring charge at 12x understates EV by 20,490). Add back non-recurring expenses, deduct non-recurring income. If the cash cost is unpaid, put its present value in the equity bridge. Remove equity-accounted JV income from EBITDA, value the stake separately, add it in the bridge (MULT pp.15-20, 25-26). Find items in the face of the income statement, other income and expense, operating-profit notes, the earnings-to-cash-flow reconciliation, and text for restructuring, impairment, write-down and integration. Count how many of the last five years carry a "one-time" charge (recurring ones are costs). Done: reported and cleaned metric side by side.
5. Choose the multiple from the table below, then the pricing base: historical (average-year price over history, for trading ranges), current (price over trailing and one or two forecast years), forward (price x (1 + cost of capital) - investor cash flow), or partial-forward (current equity value with forecast net debt, so weak cash flow is penalised) (MULT p.62). Prefer forward multiples: historical E/P had 1.6x the dispersion of forward E/P (6.0% against 3.7%) (McKinsey ch.14). Done: multiple and base stated, same base for all peers.
6. Compute operating metrics for every peer on the same basis: growth, ROIC, margin, cash conversion, leverage. Done: table.
7. Select peers by value drivers, not line of business: cash generation, risk, value-added growth, then size, product mix, geography, business model, life-cycle stage, organic against acquired growth (MULT pp.24-27; PE p.14). Apple and Edison International both traded at 12.8x P/E in 2013 with CFROI of 25% against 5% (PE p.2). Done: peer list with reason for each.
8. Summarise with the median, not the mean (MULT p.45). Express as relative multiple (company over market or sector) only against a stable-driver history or a comparable point in the cycle. Decide whether the target deserves a premium or discount from its drivers (step 9). Done: median, range, relative multiple.
9. Explain the multiple. Compare company and peers on ROIC less WACC, growth and risk. Compute the target multiple from the formulas below. Done: gap between actual and justified multiple stated in turns, with the driver that explains it.
10. Back out implied multiples from the DCF (static and rolling) and compare: the terminal multiple should be below today's (MULT pp.47-49). Done.

## Formulas
- One-stage: EV/EBITDA = [FCFF x (1 + g) / (WACC - g)] / EBITDA, which separates cash conversion, risk and growth (MULT pp.21-22).
- Returns form: EV = NOPAT x (1 - g/ROIC) / (WACC - g); EV/EBITA = (1 - T)(1 - g/ROIC)/(WACC - g), where T = operating tax rate (McKinsey ch.14). If ROIC = WACC, growth is irrelevant (MULT pp.63-64).
- Worked check: NOPAT 1,150, g 3%, ROIC 8%, WACC 8% gives EV/EBITDA 9.9x; NOPAT 1,250, g 3.5%, ROIC 9% gives 12.8x (MULT Figure 60).
- Linking identities: EV/IC = EV/NOPAT x ROIC; P/B = P/E x ROE; EV/Sales = EV/EBITA x EBITA margin. IC = invested capital.
- Single-stage P/E = (ROE - g) / [ROE x (COE - g)]; COE = cost of equity. ROE = COE gives 1/COE whatever g. ROE 12%, g 5%, COE 10% gives 11.7x (MULT p.67 prints 12x, an error).
- Two-stage EV: value-adding growth gA with return RONIC-A for N years, then gB (below WACC) with RONIC-B: EV = NOPAT(1 - gA/RONIC-A)/(WACC - gA) x [1 - ((1 + gA)/(1 + WACC))^N] + NOPAT(1 + gA)^N (1 - gB/RONIC-B) / [(WACC - gB)(1 + WACC)^N] (McKinsey ch.10). Single-stage formulas overstate; prefer two-stage (MULT p.66).
- Steady-state (commodity) P/E = 1/COE; declining business: NOPAT(1 + g)/(COE - g) with g negative (PE pp.4, 8).
- Warranted forward P/E = sum over t = 1 to N of (1 + g)^(t-1) (1 - g/ROIIC)/(1 + k)^t, plus (1 + g)^N / k / (1 + k)^N; k = 8%, N = 15, year-1 earnings 1 (PE Exhibit 5, reconstructed and verified in the notes). ROIIC = return on incremental invested capital = change in NOPAT / prior investment.
- PEG adjusted = EV multiple / (100 x expected growth).
- Banks: P/B = (ROE - g)/(ke - g); P/E = (1 - g/ROE)/(ke - g) (McKinsey ch.36, ch.15).

## Reference tables
| Multiple | Use when | Watch for (source MULT pp.50-62) |
|---|---|---|
| EV/Sales | losses; restructuring candidates | margin differences; revenue recognition |
| EV/EBITDA | similar capital intensity | ignores capex; invalid across sectors |
| EV/EBIT or EV/EBITA | capital intensity differs | depreciation policy |
| EV/NOPAT | degeared P/E; tax differences | subjective NOPAT adjustments |
| EV/FCF | normalised, smoothed FCF | lumpy cash flow |
| P/B, EV/IC | asset-heavy; banks, always beside ROE | historical-cost distortion |
| P/E | clean earnings, similar leverage | negative earnings; leverage |
| PEG | intra-sector, similar returns | ignores ROIC; growth with no spread looks cheap |

| Warranted P/E (PE Exhibit 5) | ROIIC 4% | 8% | 16% | 24% |
|---|---|---|---|---|
| g 4% | 7.1x | 12.5x | 15.2x | 16.1x |
| g 8% | NM | 12.5x | 19.4x | 21.8x |

Cost of capital 8% in that table. Dated figures (verify): 7x to 11x forward EV/EBITA for most S&P 500 non-financials in Dec 2009 (McKinsey ch.14); steady-state P/E 12.5x at 8% COE and a 1961 to 2013 average of 10.4x (PE p.4). Recompute from the current risk-free rate and implied equity risk premium.

## Interpretation rules
- A P/E below 1/COE, or EV/NOPAT below 1/WACC, means no priced value creation or fading earnings, not necessarily a bargain (PE pp.4, 12).
- Historical-average multiples are a target only if returns, growth, rates, risk premium, tax and accounting are unchanged (PE p.11).
- Leverage: if unlevered P/E is below 1/cost of debt, P/E falls as leverage rises (McKinsey App. E). Use EV multiples when leverage differs.
- Do not chart multiple against growth linearly. Use multiple against ROIC or ROE.
- PEG: no standard growth window, assumes value is linear in growth with a zero intercept (a zero-growth company has positive value), and ignores ROIC. Use only within a sector (McKinsey ch.14; MULT pp.43-44, 60).
- Banks: no EV multiples. Compare P/B against ROE across peers; a premium to book needs ROE above ke. Cyclicals: normalise to mid-cycle earnings first. High growth with losses: use EV/Sales on a forward base, with margin explained.
- A multiple is not a valuation: use it to test the DCF, not replace it (McKinsey ch.14).

## Output lines
- Multiple, base and definition for target and peers (derived from reported). EV bridge with each item (reported or derived).
- Reported against cleaned metric, with the items removed (reported, derived).
- Peer table: median, range, each peer's ROIC, growth, leverage (derived), selection reason (judgment).
- Target against peer median, premium or discount in percent (derived).
- Justified multiple from the stated drivers, and the gap in turns (assumed inputs, derived output).
- Implied terminal multiple against current (derived).
- "At this multiple the price implies ..." with its evidence label. No rating.

## Sources
Notes: expectations-multiples-dcf.md (MULT = Robinson and Weyns, UBS, 2017; PE = Mauboussin and Callahan, 2014), mckinsey-part1.md (ch.14, ch.10), mckinsey-part2.md (ch.36). Underlying: McKinsey, Valuation, 5th ed. (2010).
