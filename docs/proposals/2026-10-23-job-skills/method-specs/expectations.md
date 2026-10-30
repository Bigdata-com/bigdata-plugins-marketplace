# Spec: Price-implied expectations

## 1. Purpose
This method answers: what must the company deliver, in growth, return on new investment and years of excess return, for the current price to be fair, and is that implied bar high or low against base rates. Jobs: reverse DCF, multiples, earnings preview, thesis, company view, sector comparison. Order of work: implied bar first, then the opportunity (will the company go over, under or meet the bar), then the view. Source: Mauboussin, "Expectations Investing", CFA Institute Conference Proceedings Quarterly, Sept 2006, p.61 ("EI").

## 2. Inputs
| Input | Bigdata.com source | Label |
|---|---|---|
| Market cap, EV, net debt | Tearsheet key_metrics. Add minorities, preferred, pension deficit and leases from the balance sheet if absent | reported |
| EBIT, tax, sales, capex, depreciation, working capital, invested capital | Tearsheet statements, 5 fiscal periods. Tax rate = income tax / pretax income, normalised | reported |
| Consensus sales and EBIT to FY+4, long-term growth | Tearsheet estimates | reported |
| NOPAT0, NOPAT1 | EBIT x (1 - tax rate); NOPAT1 uses consensus EBIT for next fiscal year | derived |
| ROIIC (return on incremental invested capital) | (NOPAT1 - NOPAT0) / Investment0; investment = change in working capital + capex net of depreciation + acquisitions; rolling averages if lumpy | derived |
| Cost of capital | No WACC field exists. Set from the current 10-year yield in the currency of the cash flows plus an equity risk premium; sensitivity of at least plus and minus 1 point | assumed |

## 3. Procedure
1. Collect consensus value drivers: sales growth, operating margin, incremental investment (EI p.66). Done when NOPAT1 and the investment rate are written with labels.
2. Fix the cost of capital as an input with a sensitivity; refining it adds little (EI p.64). Done when a base value and a range are stated.
3. Compute steady-state value and the ratio of P/E to steady-state P/E (4.1). Done when the share of EV paid for future value creation is stated.
4. Solve for the implied bar (4.2, 4.3): implied growth at a given ROIIC, or implied competitive advantage period (CAP, years of positive spread on new investment). Done when stated as "the price needs X percent growth at Y percent ROIIC for Z years".
5. Cross-check with the P/E grid (section 5) and the implied terminal multiple (4.5).
6. Compare the bar with base rates and industry CAP (section 6); label it above, in line with or below history.
7. Name the value trigger (4.4), then state where the analyst view differs. No Buy, Hold or Sell.

## 4. Formulas
### 4.1 Steady state and the Miller and Modigliani split (Mauboussin and Callahan, "What Does a Price-Earnings Multiple Mean?", Credit Suisse, 29 Jan 2014, pp.3-9; "PE")
- Firm value = steady-state value + future value creation.
- Steady-state value = (normalised NOPAT + excess cash) / cost of capital (current NOPAT lasts forever; new investment earns the cost of capital).
- Future value creation = Investment x (ROIIC - cost of capital) x CAP / [cost of capital x (1 + cost of capital)].
- Equity value = steady state + future value creation + excess cash - debt (cash net of repatriation tax; debt includes preferred).
- Steady-state P/E = 1 / cost of equity; 12.5x at 8 percent (verify: PE used 3 percent yield plus 5 percent premium on 1 Jan 2014).
- Ratio of P/E to steady-state P/E = P/E x cost of equity. At 1.0 the stock is valued as a commodity; above 1.0 the market pays for value creation; below 1.0 it expects none or expects earnings to fade (PE p.4).

### 4.2 Closed-form implied growth
Start from EV = NOPAT1 x (1 - g/ROIIC) / (WACC - g), where g is perpetual NOPAT growth and g/ROIIC the reinvestment rate (Robinson and Weyns, UBS, "How to analyse and talk the language of multiples", 16 Mar 2017, pp.63-64; "MULT").
1. EV x (WACC - g) = NOPAT1 - NOPAT1 x g / ROIIC
2. EV x WACC - NOPAT1 = g x (EV - NOPAT1 / ROIIC)
3. **g = (EV x WACC - NOPAT1) / (EV - NOPAT1 / ROIIC)**

Illustration, not a company: EV 2,000, NOPAT1 100, WACC 8 percent, ROIIC 15 percent gives g = 60 / 1,333.3 = 4.5 percent; substituting back returns EV 2,000 (checked). It also reproduces MULT example B (NOPAT 1,250, ROIC 9 percent, WACC 8 percent, g 3.5 percent). Validity: undefined when ROIIC equals WACC, because growth then does not affect EV; requires g below WACC. For negative g use 4.3.

### 4.3 Implied CAP and declining business
- Implied CAP (derived, rearranging 4.1): CAP = (EV - steady-state value) x cost of capital x (1 + cost of capital) / [Investment x (ROIIC - cost of capital)]. GAP: the notes give no worked implied-CAP example and do not say whether Investment is annual or cumulative; state the convention used. Alternative: find the N in the section 5 recipe that reproduces the market P/E.
- Declining business (PE p.8): value = NOPAT x (1 + g) / (cost of capital - g), g negative. Source example: NOPAT 100, cost of capital 10 percent, decline 10 percent gives 450, a 4.5x multiple.

### 4.4 Value triggers and which revision matters (EI pp.66-68)
Triggers: sales, operating costs, investments (drivers: sales growth, operating margin, incremental investment rate).
- Value-neutral business (ROIIC near cost of capital): incremental return matters, growth does not.
- Value-creating business (ROIIC far above): sales growth matters.
- Below cost of capital: faster growth destroys value (PE p.10).

### 4.5 Implied multiples from a DCF (MULT pp.47-49; Robinson and Weyns, "When DCF valuation goes rogue (Episode II)", 25 Sep 2017, pp.26-31; "DCF2")
Back out the implied EV/EBITDA or EV/NOPAT. Implied terminal multiple = terminal value / final-year EBITDA; it should fall below today's multiple as the company matures. At or above today's means a valuation problem or a very strong story (MULT p.48). Report terminal value share of EV; UBS rule of thumb is 70 to 80 percent for a 5-year explicit period, 50 to 60 percent for 10 years (DCF2 p.27; not a statistic, verify).

## 5. Reference table: warranted forward P/E
Source: PE Exhibit 5, p.10. All-equity firm, 8 percent cost of capital, 15-year forecast then zero spread. Rows are earnings growth, columns ROIIC.
| growth | 4% | 8% | 16% | 24% |
|---|---|---|---|---|
| 4% | 7.1x | 12.5x | 15.2x | 16.1x |
| 6% | 3.3x | 12.5x | 17.1x | 18.6x |
| 8% | NM | 12.5x | 19.4x | 21.8x |
| 10% | NM | 12.5x | 22.4x | 25.7x |
Recipe (reconstructed by the note author; I re-ran it and it matches all 16 cells): forward P/E = sum for t = 1 to N of (1+g)^(t-1) x (1 - g/ROIIC) / (1+k)^t + (1+g)^N / [k x (1+k)^N], with k the cost of equity, N = 15, year-1 earnings 1. Closed form of the sum: (1 - g/ROIIC) x (1 - q^N) / (k - g), q = (1+g)/(1+k); when g = k sum the terms directly. Negative cells are "NM".
Three paths to about 15.0x (PE Exhibit 6, checked): growth 12 percent with ROIIC 8.8 percent; 6 percent with 11.0 percent; 3 percent with 23.0 percent.

## 6. Other reference figures (historical, verify)
- Steady-state P/E averaged 10.4x (SD 2.7), 1961-2013 (PE p.4).
- Steady state explained about two-thirds of the S&P 500 since 1961, future value creation about one-third (PE p.5; the paper prints 74 and 24 percent, the arithmetic gives 76 and 24).
- Market-implied CAP averaged about 8 years, 1976-2007, from about 5 (competitive industries) to about 15 (stable) (PE p.11, citing Olsen). A prior, not a current figure.
- 80/20 rule on where expectations sit: GAP. None of the three notes has it; do not state it. The nearest sourced figure is the two-thirds and one-third split above, at index level only.

## 7. Interpretation rules
- A P/E below 1 / cost of equity is not automatically cheap; it means no value creation is priced or earnings are fading (PE p.12).
- Compare business models, not lines of business (PE p.2: two companies at 12.8x P/E in 2013 had CFROI of 25 and 5 percent). Use unlevered multiples when leverage differs (PE p.14).
- Past multiples are a target only if the drivers are stable (PE p.11).
- Does not apply directly to: banks (use P/B against ROE, MULT appendix); cyclicals (normalise to mid-cycle first; GAP: no normalisation procedure beyond the fade convention in base-rates.md); loss-making or early-stage companies (NOPAT1 not meaningful; MULT suggests EV/Sales or normalised earnings; GAP: no reverse-DCF procedure for them); emerging markets (match the risk-free rate to the currency of the cash flows; DCF1 pp.49-53).

## 8. Output lines
- "EV is Z from market cap X and net debt Y (reported); NOPAT1 is X from consensus EBIT at a Y percent tax rate (derived)."
- "At an assumed WACC of X percent (assumed, range Y to Z), the price implies NOPAT growth of g percent at ROIIC R percent (derived)."
- "Steady state explains X percent of EV; Y turns of the P/E pay for future value creation (derived)."
- "The price needs g percent growth for N years at ROIIC R percent; consensus is A; the historical base rate is B (reported, historical)."
- "The implied terminal multiple is X against Y today (derived)."
- "The value trigger is [incremental return | sales growth] because ROIIC is [near | above] cost of capital (judgment)."

## 9. Sources
Notes: expectations-multiples-dcf.md (sections 1 to 2.7, 6). Papers: EI (2006); PE (2014); MULT, DCF1 (Episode I, 6 Sep 2017), DCF2 (Robinson and Weyns, UBS, 2017).
