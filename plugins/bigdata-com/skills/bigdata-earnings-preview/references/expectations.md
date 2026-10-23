# Price-implied expectations

This method answers one question before any view on a stock is formed: what must the company deliver, in growth, return on new investment and years of excess return, for today's price to be fair, and is that bar high or low against history. Mauboussin's order of work is fixed: measure the height of the bar first without judging it, then decide whether the company will go over, under or meet it, then state the view (Expectations Investing, p.65-66). The method keeps two things apart that most written research blends: knowledge of the fundamentals and the expectations embedded in the price. A good company is not a good stock unless the price misjudges what the fundamentals will deliver (EI p.61).

## When a skill loads this file

Load it wherever a view on a stock is formed: valuation and reverse DCF, multiples and comps, earnings preview, thesis and variant perception, deep dive, quick take, stock move (implied growth before and after the move) and sector comparison. For a narrow question ("what does the price imply?") run steps 1 to 4 and give the answer with the arithmetic; skip the rest.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Market cap, enterprise value, net debt | `bigdata_company_tearsheet`, `fundamentals` key metrics. Add minorities, preferred, pension deficit and leases from the balance sheet when the EV field leaves them out | reported |
| EBIT, income tax, pretax income, sales, capex, depreciation, working capital, invested capital | `fundamentals` statements, five fiscal periods | reported |
| Tax rate | Income tax / pretax income, normalised for one-off tax items | derived |
| Consensus sales, EBIT, EPS to FY+4, long-term growth | `estimates`, with the vintage date and the number of estimates | reported |
| NOPAT0, NOPAT1 | EBIT x (1 - tax rate); NOPAT1 uses consensus EBIT for the next fiscal year | derived |
| Investment | Change in working capital + capex net of depreciation + acquisitions (EI p.63) | derived |
| ROIIC | (NOPAT1 - NOPAT0) / Investment0; use rolling averages when investment is lumpy (PE p.9) | derived |
| Cost of capital | Not in Bigdata.com. Set from the current 10-year government yield in the currency of the cash flows plus an equity risk premium, and show a sensitivity of at least plus and minus 1 point | assumed |

Use free cash flow as "cash earnings minus investments", where cash earnings = sales x operating margin less cash taxes. Do not substitute cash from operations less capex (EI p.63). Treat large R&D as investment when judging returns (EI p.63-64).

## Procedure

1. **Collect the consensus value drivers.** Sales growth, operating margin and the incremental investment rate, from the estimates section (EI p.66). The sell-side consensus stands in for the market's view because it avoids imposing the analyst's own forecast. Done when NOPAT1, the investment rate and ROIIC are written with their Basis labels and the consensus vintage.
2. **Fix the cost of capital as an input.** Choose one economically sensible value and a range; effort spent refining it adds little (EI p.64). Done when a base value and a range are stated as assumed, with the yield and premium used.
3. **Split the value into steady state and future value creation** (formula 1). Done when the note states what share of EV the steady state explains and how many turns of the P/E pay for value creation.
4. **Solve for the implied bar** (formulas 2 and 3): implied perpetual growth at a stated ROIIC, or the implied competitive advantage period (CAP, the years during which new investment earns more than the cost of capital). Done when the note says "the price needs X percent NOPAT growth at Y percent ROIIC" or "the price needs Z years of positive spread on new investment".
5. **Cross-check with the P/E grid and the implied terminal multiple** (reference table 1, formula 5). Done when the market P/E has been placed on the grid and, where a DCF exists, the implied terminal multiple is compared with today's multiple.
6. **Compare the bar with base rates.** Use `references/base-rates.md` for growth and margin by size class and sector, and the CAP figures below. Done when the bar is labelled above, in line with or below history, with the sample and period.
7. **Name the value trigger** (formula 4), then state where the analyst's view differs and why. Done when the trigger is named and the difference is stated as a fact or a judgment. No buy, hold or sell.

## Formulas

**1. Steady state and future value creation** (Mauboussin and Callahan, "What Does a Price-Earnings Multiple Mean?", 2014, pp.3-9; "PE")

- Firm value = steady-state value + future value creation.
- Steady-state value = (normalised NOPAT + excess cash) / cost of capital. It assumes current NOPAT lasts forever and new investment earns exactly the cost of capital.
- Future value creation = Investment x (ROIIC - cost of capital) x CAP / [cost of capital x (1 + cost of capital)].
- Equity value = steady state + future value creation + excess cash - debt. Excess cash is net of any repatriation tax; debt includes preferred and other senior claims (PE p.4).
- Steady-state P/E = 1 / cost of equity. At an 8 percent cost of equity it is 12.5x (PE p.4, using a 3 percent 10-year yield plus a 5 percent premium on 1 Jan 2014; verify and recompute from today's inputs).
- Ratio of P/E to steady-state P/E = P/E x cost of equity. At 1.0 the stock is valued as a commodity business. Above 1.0 the market pays for value creation. Below 1.0 it expects none, or expects current earnings to fade (PE p.4, p.7).

Variables: NOPAT is net operating profit after tax; Investment is net new investment (working capital, capex net of depreciation, acquisitions); ROIIC is the return on that incremental investment; CAP is in years.

**2. Implied perpetual growth, closed form**

Start from the value-driver formula EV = NOPAT1 x (1 - g/ROIIC) / (WACC - g), where g is perpetual NOPAT growth and g/ROIIC is the reinvestment rate (Robinson and Weyns, UBS, "How to analyse and talk the language of multiples", 2017, pp.63-64; "MULT"). Solve for g:

- EV x (WACC - g) = NOPAT1 - NOPAT1 x g / ROIIC
- EV x WACC - NOPAT1 = g x (EV - NOPAT1 / ROIIC)
- **g = (EV x WACC - NOPAT1) / (EV - NOPAT1 / ROIIC)**

Illustration, not a company: EV 2,000, NOPAT1 100, WACC 8 percent, ROIIC 15 percent gives g = 60 / 1,333.3 = 4.5 percent; substituting back returns EV 2,000. The formula also reproduces MULT's example B (NOPAT 1,250, ROIC 9 percent, WACC 8 percent, g 3.5 percent). It is undefined when ROIIC equals WACC, because growth then does not change value, and it requires g below WACC. When EV x WACC is below NOPAT1 the price implies shrinking NOPAT: use formula 3b.

**3a. Implied CAP** (rearranging formula 1)

CAP = (EV - steady-state value) x cost of capital x (1 + cost of capital) / [Investment x (ROIIC - cost of capital)].

Not in the sources: a worked implied-CAP example, or whether Investment is one year's or cumulative. Use next year's expected net investment, held constant each year, and state that convention as assumed. As a check, find the forecast length N in the P/E grid recipe (reference table 1) that reproduces the market P/E at the stated growth and ROIIC.

**3b. Declining business** (PE p.8)

Value = NOPAT x (1 + g) / (cost of capital - g), with g negative. Source example: NOPAT 100, cost of capital 10 percent, decline 10 percent a year gives 100 x 0.90 / 0.20 = 450, a 4.5x multiple. A low multiple can be fair when the base earnings are fading.

**4. Value triggers and which revision matters** (EI pp.66-68; PE p.10)

The three triggers are sales, operating costs and investments; they move the three operating drivers: sales growth, operating margin and the incremental investment rate.

- ROIIC near the cost of capital (value-neutral business): the incremental return moves value; growth does not. EI's distributor example: changing growth did not move value, while 300 basis points more incremental return almost doubled it.
- ROIIC far above the cost of capital (value-creating business): sales growth moves value.
- ROIIC below the cost of capital: faster growth destroys value.

Run "if, then" cases on the trigger that matters: if consensus sales growth moves 2 points either way, what happens to margin, investment and value. Analysts consistently underestimate how changes in sales flow into margins, on the way up and on the way down (EI p.68).

**5. Implied multiples from a DCF** (MULT pp.47-49; Robinson and Weyns, "When DCF valuation goes rogue (Episode II)", 2017, pp.26-31; "DCF2")

- Implied terminal multiple = terminal value / final-year EBITDA (or NOPAT). It should be below today's multiple, because multiples fall as a company matures. At or above today's multiple, either the valuation has an error or it rests on a very strong story (MULT p.48).
- Terminal value share of EV: the UBS rule of thumb is 70 to 80 percent for a 5-year explicit period and 50 to 60 percent for a 10-year period (DCF2 p.27). It is a rule of thumb, not a statistic.

## Reference tables

**Table 1. Warranted forward P/E by earnings growth and ROIIC** (PE Exhibit 5, p.10). All-equity firm, 8 percent cost of capital, 15-year forecast, then new investment earns the cost of capital. Rows are earnings growth, columns are ROIIC.

| Growth | ROIIC 4% | 8% | 16% | 24% |
|---|---|---|---|---|
| 4% | 7.1x | 12.5x | 15.2x | 16.1x |
| 6% | 3.3x | 12.5x | 17.1x | 18.6x |
| 8% | NM | 12.5x | 19.4x | 21.8x |
| 10% | NM | 12.5x | 22.4x | 25.7x |

Recipe (reconstructed by the note author; it matches all 16 cells): forward P/E = sum for t = 1 to N of (1+g)^(t-1) x (1 - g/ROIIC) / (1+k)^t + (1+g)^N / [k x (1+k)^N], with k the cost of equity, N = 15 and year-1 earnings of 1. Closed form of the sum: (1 - g/ROIIC) x (1 - q^N) / (k - g), with q = (1+g)/(1+k); when g equals k, sum the terms directly. Negative cells are shown as NM. Rerun the recipe at the assumed cost of equity rather than reading the 8 percent grid as current.

Three paths to about 15.0x (PE Exhibit 6): growth 12 percent with ROIIC 8.8 percent; 6 percent with 11.0 percent; 3 percent with 23.0 percent. The same multiple can mean fast growth on a thin spread or slow growth on a wide one (PE p.13).

**Table 2. Historical reference figures** (verify; none is a current fact)

| Figure | Value | Sample and source |
|---|---|---|
| Steady-state P/E of the S&P 500 | Averaged 10.4x, standard deviation 2.7; low just over 5x in 1981, high teens in the early 1960s and late 1990s | 1961-2013, PE p.4 |
| Share of S&P 500 value explained by the steady state | About two-thirds on average; future value creation about one-third (about 15 to 20 percent in early 2014) | Since 1961, PE p.5 |
| Market-implied CAP | Averaged about 8 years; about 5 in very competitive industries, about 15 in stable ones | 1976-2007, PE p.11, citing Olsen |
| Reversion in returns on capital | Top quintile fell about 800 bp, bottom quintile rose about 700 bp | 615 industrial companies, 1991-2000, EI p.65 |
| Slow-fade and fast-fade sectors | Slow: consumer staples, health care. Fast: information technology, energy | PE p.11 |

Not in the sources: an "80/20" rule on where expectations sit in a share price. Do not state one. The nearest sourced figure is the index-level two-thirds and one-third split above.

## Interpretation and limits

- A P/E below 1 / cost of equity is not proof of cheapness. It means the market prices no value creation, or expects earnings to fade. It is attractive only if the base business is stable (PE p.12).
- The market is not short-term: the price capitalises many years of cash flow, so a near-term miss is not the same as a change in long-term value (EI p.62).
- Compare business models, not lines of business. Two companies at 12.8x P/E in 2013 had CFROI of 25 and 5 percent (PE p.2). Use unlevered multiples when leverage differs (PE p.14).
- A company's own past multiple is a target only when returns, growth, rates, the risk premium, tax and accounting are unchanged (PE p.11).
- CAPs cluster by business type, so set CAP for a group of related companies, not one company in isolation (EI p.65).
- Banks: use price to book against ROE (P/B = P/E x ROE), not EV-based formulas (MULT appendix).
- Cyclicals: normalise NOPAT to mid-cycle before solving. Not in the sources: a normalisation procedure beyond the fade convention in `references/base-rates.md`; state the mid-cycle margin used as assumed.
- Loss-making or early-stage companies: NOPAT1 is not meaningful. MULT suggests EV/Sales or normalised earnings. Not in the sources: a reverse-DCF procedure for these companies; state the margin path assumed and solve for the revenue the price needs.
- Non-US listings and emerging markets: take the risk-free rate in the currency of the cash flows, not the domicile, and adjust it if the government bond carries default risk (DCF1 pp.49-53).

## Output lines

- "EV is Z, from market cap X and net debt Y (reported). NOPAT1 is N from consensus EBIT of E [vintage] at a T percent tax rate (derived)."
- "At an assumed cost of capital of K percent (assumed; range K-1 to K+1), the price implies perpetual NOPAT growth of g percent at ROIIC of R percent (derived)."
- "The steady state explains S percent of EV; V turns of the P/E pay for future value creation (derived)."
- "The price needs g percent growth for N years at R percent ROIIC. Consensus is A. In the reference class, B percent of companies achieved this [sample and period] (reported, historical base rate)."
- "The implied terminal multiple is X against Y today (derived)."
- "The value trigger is [incremental return | sales growth] because ROIIC is [near | well above] the cost of capital (judgment)."

## Sources

- Note: expectations-multiples-dcf.md, sections 1.1 to 1.3, 2.6, 2.7, 3.1 (rows 2 and 9), 5 and 6.
- Mauboussin, "Expectations Investing: Reading Stock Prices for Better Returns", CFA Institute Conference Proceedings Quarterly, Sept 2006, pp.61-70 ("EI").
- Mauboussin and Callahan, "What Does a Price-Earnings Multiple Mean?", Credit Suisse, 29 Jan 2014, pp.2-21 ("PE").
- Robinson and Weyns, UBS, "How to analyse and talk the language of multiples", 16 Mar 2017 ("MULT").
- Robinson and Weyns, UBS, "When DCF valuation goes rogue", Episode I (6 Sep 2017, "DCF1") and Episode II (25 Sep 2017, "DCF2").
