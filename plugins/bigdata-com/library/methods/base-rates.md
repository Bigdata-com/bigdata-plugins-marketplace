# Base rates and reversion to the mean

This method answers: how does a forecast of growth, margin or return on capital compare with what actually happened to similar large companies, and how fast should an unusual level move back toward its sector mean. It starts from the history of a reference class (the outside view) and moves away from it only with evidence, instead of extrapolating the company's own story (the inside view). The inside view is usually too optimistic and its ranges too narrow (Base Rate Book, 2016). Every number in this file is a historical base rate for large, mostly listed companies. None is a forecast or a current fact.

## When a skill loads this file

Load it next to any growth, margin or return claim: earnings preview, valuation, thesis, deep dive, moat, scenarios, sector work. For a narrow question ("how often do companies this size grow 20 percent a year?") quote the relevant row with its label and stop.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Prior-year sales (sets the size class), sales and net income history | `bigdata_company_tearsheet`, `fundamentals`, five fiscal periods | reported |
| Gross profitability = (revenue - cost of goods sold) / total assets | `fundamentals` income statement and balance sheet | derived |
| Operating margin, ROIC | `fundamentals` ratios and statements | reported or derived |
| Sector | `company_overview` | reported |
| Consensus growth, margin, EPS to FY+4, long-term growth | `estimates`, with vintage | reported |
| Expected inflation | Not in Bigdata.com company fields; state it as an assumption with its basis | assumed |
| Sector mean and persistence r | Tables below | reported (historical base rate) |

## Procedure

1. **State the quantity and the horizon.** Real or nominal growth, margin or return on capital, over how many years. Done when both are written.
2. **Choose the reference class.** Size class by prior-year sales for growth; sector for margins, gross profitability and returns on capital; the above-$50B class for mega caps. The class must be large enough to be robust and narrow enough to be relevant. Done when the class, its N and its label are stated. If the company differs in a way that matters, say which feature differs and still show the base rate.
3. **Read the distribution, not only the average.** Growth distributions are right-skewed: the median sits below the mean. Done when median, mean, dispersion and the relevant tail shares are quoted.
4. **Place the forecast in the distribution.** "Consensus needs a 10-year real sales CAGR of X percent, which Y percent of companies in the $A to $B class achieved." The tables give shares at fixed thresholds only; interpolate between them and say so. Not in the sources: full percentile tables.
5. **Convert real to nominal** before comparing with consensus (formula 4). Done when the inflation assumption is stated.
6. **Blend by persistence** (formula 1). Beyond three years, put the majority of the weight on the class median for sales and earnings growth. For margins and gross profitability, start from the latest level and fade toward the sector mean. For returns on capital, apply the horizon-matched r. Done when the blend, the weights and the r used are shown.
7. **Set a range at least as wide as history** and include a decline case (table 12). Done when the bear case includes shrinking real sales or lower net income.
8. **Ask what must be true for the price** (`references/expectations.md`) and whether that assumption sits in a rare part of the distribution. Claim an exception only with a specific, evidenced reason. Done when the note says how rare the implied path is.

## Formulas

**1. Regression to the mean and shrinkage** (Mauboussin, "How to Model Reversion to the Mean", 2013, "F"; Base Rate Book, 2016, "A")

- Expected outcome = mean + r x (current outcome - mean), where r is the correlation between the metric now and the same metric earlier. With r = 1 the best estimate is the last value; with r = 0 it is the mean.
- Shrinkage form: estimated true level = grand average + c x (observed - grand average), c between 0 and 1, with r as the proxy for c. Source example: grand average 8 percent, observed 12 percent, c = 0.10 gives 8.4 percent.
- Source example: Microsoft CFROI 16.1 percent, IT sector mean 9.0 percent, four-year r 0.50 gives 12.6 percent in four years.
- The more luck in the outcome, the more weight on the base rate; the more skill, the more on the inside view.
- Use the r that matches the horizon. The four-year r is higher than the one-year r compounded. For staples with CFROI 10 points above the sector mean, 0.89 applied four times leaves 6.3 points of excess; the four-year r of 0.78 leaves 7.8 points (paper F with its 2013 data: 6.0 against 7.3). The one-year r overstates the speed of fading.
- Interpolating between years with r^(t/4) is an approximation by the note author, not a method in the papers; paper F says the single-r equation is meant for one-time adjustments.

**2. Fade convention** (HOLT, paper F, endnote 1)

An explicit fade period of 5 years set by life-cycle position; then 10 percent of the spread over the long-run average is eliminated each year (a spread of 10 points becomes 9); then the return equals the cost of capital in the terminal period. State it as a convention, not an empirical law.

**3. Threshold margin** (A)

Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 - tax rate)]. Source example: (0.35 + 0.25) x 0.10 / (1.10 x 0.65) = 8.4 percent. Growth at that margin is value-neutral; growth below it destroys value.

**4. Real versus nominal**

The tables are real (inflation-adjusted). Consensus is nominal. (1 + nominal) = (1 + real) x (1 + inflation); nominal is approximately real plus inflation.

**5. Operating profit sensitivity** (A)

Change in operating profit is approximately operating margin beta x change in sales (table 10). Financial leverage amplifies the effect on net income.

## Reference tables

Main label, carried by every table unless the table names another: **Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact.** The sample includes companies that later disappeared; modest survivorship bias remains, because a 10-year observation needs 10 years of survival.

**Table 1. Real sales growth, all sizes** (A; N = 53,266 at 3 years, 49,874 at 5, 41,645 at 10; real CAGR)

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 5.8% | 5.4% | 5.2% | 4.9% |
| Mean | 14.8% | 8.1% | 6.9% | 5.8% |
| Standard deviation | 275% | 18.7% | 12.3% | 8.0% |
| Share with CAGR >= 10% | 35.5% | 30.9% | 27.1% | 20.6% |
| Share >= 15% | 24.1% | 18.6% | 14.5% | 9.0% |
| Share >= 20% | 17.3% | 11.9% | 8.5% | 4.5% |
| Share >= 25% | 12.8% | 8.0% | 5.4% | 2.5% |
| Share above 45% (the ">45" bin) | 5.5% | 2.5% | 1.3% | 0.3% |
| Share negative | 26.2% | 22.6% | 20.0% | 16.9% |

Use the 3-, 5- and 10-year columns; the 1-year column is noisy.

**Table 2. Real sales growth by starting size, prior-year sales in 2015 dollars** (A; each cell is 3-yr / 5-yr / 10-yr real CAGR unless the column says 10-yr; the >$50B row is a subset of >$25B; share columns were derived by the note author by summing the published bins)

| Prior-year sales | Median | Mean 10-yr | SD 10-yr | Share >= 15% | Share >= 20% | Share < 0 |
|---|---|---|---|---|---|---|
| $0-325M | 11.7 / 11.2 / 9.8 | 12.6 | 12.0 | 40.7 / 36.9 / 28.6 | 30.3 / 26.8 / 18.1 | 9.7 / 6.8 / 4.9 |
| $325-700M | 7.5 / 7.3 / 6.7 | 7.4 | 7.0 | 21.5 / 17.1 / 9.9 | 14.1 / 9.9 / 4.7 | 12.1 / 9.8 / 8.0 |
| $700M-1.25B | 6.8 / 6.4 / 5.7 | 6.2 | 7.0 | 21.9 / 17.1 / 8.4 | 13.7 / 9.8 / 3.5 | 16.3 / 14.4 / 12.7 |
| $1.25-2B | 6.2 / 5.7 / 5.1 | 5.7 | 6.6 | 19.4 / 14.3 / 7.0 | 12.4 / 8.1 / 3.0 | 17.8 / 15.4 / 12.8 |
| $2-3B | 5.4 / 5.1 / 4.5 | 5.1 | 6.0 | 17.2 / 11.8 / 6.3 | 10.7 / 6.4 / 2.2 | 20.4 / 17.3 / 15.3 |
| $3-4.5B | 5.0 / 4.7 / 4.1 | 4.4 | 5.7 | 15.5 / 10.4 / 4.4 | 8.5 / 5.2 / 1.2 | 23.0 / 20.9 / 18.4 |
| $4.5-7B | 4.4 / 4.1 / 3.7 | 3.9 | 6.0 | 14.7 / 10.3 / 4.2 | 8.5 / 4.7 / 1.5 | 25.3 / 23.0 / 20.8 |
| $7-12B | 3.7 / 3.5 / 3.2 | 3.3 | 6.0 | 12.4 / 7.6 / 3.2 | 7.0 / 3.6 / 1.1 | 29.2 / 27.6 / 24.6 |
| $12-25B | 3.0 / 2.9 / 2.7 | 2.9 | 6.1 | 10.3 / 6.8 / 3.4 | 5.9 / 3.2 / 0.9 | 33.4 / 30.7 / 27.9 |
| >$25B | 2.2 / 2.0 / 1.8 | 1.7 | 6.1 | 8.9 / 5.2 / 1.5 | 4.6 / 2.0 / 0.2 | 37.0 / 35.6 / 35.5 |
| >$50B | 1.5 / 1.5 / 1.1 | 0.8 | 5.8 | 6.0 / 3.3 / 0.9 | 2.8 / 1.0 / 0.0 | 41.4 / 38.9 / 41.1 |

Median and dispersion both fall with size. Above $25B, 35.5 percent had a negative 10-year real CAGR: large companies shrink about as often as they grow over a decade. In the $4.5-7B class no company grew 45 percent or more a year for 10 years, and 30 to 35 percent a year was about 0.2 percent of the class.

**Table 3. Real sales growth, alternate sample.** Label: historical base rate, S&P 1500 constituents followed after index exit, 1994-2014, inflation-adjusted (2014 dollars). Not a forecast and not a current fact. (Base Rate Book Sales Growth, 2015, "C"; N = 23,914 at 3 years, 19,288 at 5, 10,681 at 10, 1,136 at 20.)

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr | 20-yr |
|---|---|---|---|---|---|
| Median | 5.2% | 4.5% | 4.2% | 4.1% | 4.2% |
| Mean | 8.8% | 6.2% | 5.3% | 4.6% | 4.9% |
| SD | 50.3% | 16.4% | 13.1% | 9.6% | 6.7% |

Negative real sales CAGR: 31 percent of companies at 3 years, 30 percent at 5. Ten-year medians by sales class: $0-250M 8.8%; $250-450M 6.1%; $450-700M 5.4%; $700M-1B 5.0%; $1-1.5B 4.7%; $1.5-2.25B 3.6%; $2.25-3.5B 3.3%; $3.5-6B 3.0%; $6-13B 2.9%; above $13B 2.7%; above $50B 2.0%.

**Table 4. Real net income growth, all sizes** (A; net income before extraordinary items; a CAGR needs positive beginning and ending earnings; N = 52,901 at 1 year, 48,472 at 3, 44,874 at 5, 37,305 at 10)

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 9.2% | 6.8% | 5.9% | 5.2% |
| Mean | 88.8% | 10.3% | 7.3% | 5.8% |
| SD | 7,842% | 34.6% | 20.2% | 11.0% |
| Share >= 10% | 48.4% | 41.5% | 36.6% | 28.0% |
| Share >= 20% | 33.4% | 23.1% | 16.3% | 7.5% |
| Share >= 30% | 24.4% | 13.6% | 7.5% | 2.4% |
| Share with lower net income | 33.0% | 31.6% | 29.3% | 24.3% |

**Table 5. Real net income growth by starting size, prior-year sales** (A; each cell is 3-yr / 5-yr / 10-yr)

| Prior-year sales | Median | Share >= 20% | Share >= 30% | Share with decline |
|---|---|---|---|---|
| $0-325M | 11.1 / 10.1 / 8.5 | 33.6 / 26.9 / 17.2 | 21.6 / 14.6 / 7.0 | 22.2 / 18.7 / 13.8 |
| $325-700M | 7.7 / 6.8 / 6.0 | 22.0 / 15.5 / 6.5 | 12.4 / 6.4 / 1.9 | 24.6 / 22.0 / 16.5 |
| $700M-1.25B | 7.2 / 6.4 / 5.3 | 22.2 / 15.0 / 6.0 | 12.6 / 7.0 / 1.3 | 28.8 / 26.2 / 22.3 |
| $1.25-2B | 6.9 / 5.9 / 5.0 | 22.1 / 15.1 / 4.8 | 12.5 / 6.0 / 1.1 | 30.9 / 27.5 / 23.7 |
| $2-3B | 6.6 / 5.3 / 4.2 | 21.4 / 14.5 / 4.6 | 12.5 / 6.0 / 1.2 | 30.9 / 29.9 / 27.6 |
| $3-4.5B | 6.2 / 4.7 / 4.3 | 21.3 / 13.0 / 4.4 | 11.9 / 5.4 / 1.4 | 33.5 / 32.8 / 26.9 |
| $4.5-7B | 6.0 / 4.8 / 4.3 | 20.8 / 13.3 / 5.5 | 11.8 / 6.2 / 1.6 | 34.1 / 32.9 / 29.9 |
| $7-12B | 5.5 / 4.9 / 4.4 | 21.9 / 14.9 / 6.5 | 12.9 / 6.9 / 1.9 | 35.2 / 32.4 / 27.9 |
| $12-25B | 5.2 / 4.4 / 4.3 | 21.5 / 15.0 / 7.1 | 13.3 / 6.8 / 2.6 | 36.8 / 36.1 / 30.3 |
| >$25B | 4.7 / 4.0 / 4.1 | 22.1 / 15.5 / 7.3 | 13.5 / 7.5 / 2.0 | 39.6 / 38.6 / 32.5 |
| >$50B | 3.6 / 2.5 / 3.3 | 21.0 / 13.9 / 8.3 | 13.5 / 7.9 / 2.2 | 42.6 / 41.7 / 35.9 |

The median falls with size but the dispersion barely does (3-year SD 33 to 38 percent in every class). A 10-year CAGR of 20 percent or more is rare (4 to 8 percent of any class). Of the 200 highest-net-income companies in 1990, 162 survived to 2000; 14 of them (under 9 percent) grew net income 15 percent or more a year over 1990-1999, and none sustained it for the decade to 2009.

**Table 6. Persistence: correlation between a metric now and the same metric earlier** (A unless stated; sample as listed)

| Metric | 1-yr r | 3-yr r | 5-yr r | Sample |
|---|---|---|---|---|
| Sales growth | 0.30 | 0.17 | 0.19 | 1950-2015 |
| Net income growth | -0.05 | -0.23 | -0.24 | 1950-2015 |
| Gross profitability | 0.95 | 0.89 | 0.82 | 1950-2015, ex-financials and utilities (A, E) |
| Operating margin | 0.91 | 0.79 | 0.72 | 1950-2015, ex-financials and utilities |
| CFROI | 0.78 | n/a | n/a | Global, 1983-2015, ex-financials and utilities; the 4-year r is 0.56 |

Net income growth predicts total shareholder return (correlation 0.20, 0.39 and 0.40 at 1, 3 and 5 years, 1985-2015) but is not persistent. Sales growth is weakly predictive (0.20, 0.25, 0.28). Prefer metrics that are persistent, predictive or both ("What Makes for a Useful Statistic", 2016, "G").

**Table 7. Gross profitability by sector.** Label: top 1,000 global companies ex-financials and utilities, 1950-2015, ratio, no inflation adjustment. Not a forecast and not a current fact. (A; gross profit / total assets; r is the 5-year correlation; SD and CoV are of the annual sector mean.)

| Sector | r (5-yr) | Median | Mean | SD | CoV |
|---|---|---|---|---|---|
| Consumer staples | 0.86 | 0.49 | 0.54 | 0.08 | 0.14 |
| Industrials | 0.79 | 0.28 | 0.30 | 0.07 | 0.23 |
| Health care | 0.77 | 0.47 | 0.49 | 0.09 | 0.18 |
| Consumer discretionary | 0.77 | 0.35 | 0.39 | 0.05 | 0.12 |
| Materials | 0.76 | 0.25 | 0.28 | 0.04 | 0.14 |
| Information technology | 0.63 | 0.39 | 0.42 | 0.06 | 0.14 |
| Energy | 0.61 | 0.22 | 0.24 | 0.04 | 0.18 |
| Telecom services | 0.59 | 0.24 | 0.27 | 0.07 | 0.26 |

A value of 0.33 or higher is generally attractive (Novy-Marx, cited in "E"). Profitability and P/E can give opposite signals (Amazon 2015: 0.54 with a trailing P/E near 540).

**Table 8. Operating margin by sector.** Label: top 1,000 global companies ex-financials and utilities, 1950-2015, ratio, no inflation adjustment. Not a forecast and not a current fact. (A; operating income / sales.)

| Sector | r (5-yr) | Median | Mean | SD | CoV |
|---|---|---|---|---|---|
| Consumer staples | 0.89 | 0.09 | 0.11 | 0.02 | 0.21 |
| Health care | 0.74 | 0.16 | 0.17 | 0.02 | 0.14 |
| Consumer discretionary | 0.73 | 0.10 | 0.11 | 0.01 | 0.13 |
| Industrials | 0.72 | 0.09 | 0.11 | 0.02 | 0.16 |
| Telecom services | 0.63 | 0.22 | 0.22 | 0.04 | 0.19 |
| Materials | 0.62 | 0.11 | 0.13 | 0.03 | 0.25 |
| Information technology | 0.62 | 0.13 | 0.15 | 0.03 | 0.23 |
| Energy | 0.62 | 0.14 | 0.17 | 0.04 | 0.24 |

The rise in the aggregate margin since the mid-1980s is almost all in the top quintile (21 percent in 1985 to 31 percent in 2015); the bottom three quintiles were roughly flat. Use the sector figure, not the aggregate.

**Table 9. CFROI by sector.** Label: global companies, live and dead, market cap about $250M and above, 1983-2015, inflation-adjusted cash flow return on investment (Credit Suisse HOLT), including financials and utilities. Not a forecast and not a current fact. (A; r is the 4-year correlation; SD and CoV are of the annual sector mean; winsorized at the 1st and 99th percentiles.)

| Sector | 4-yr r | Median % | Mean % | SD % | CoV |
|---|---|---|---|---|---|
| Consumer staples | 0.78 | 8.1 | 9.3 | 0.6 | 0.07 |
| Consumer discretionary | 0.67 | 8.0 | 9.1 | 0.6 | 0.07 |
| Health care | 0.64 | 8.3 | 7.6 | 1.1 | 0.15 |
| Industrials | 0.62 | 6.7 | 7.6 | 1.0 | 0.12 |
| Utilities | 0.57 | 3.5 | 4.1 | 0.8 | 0.20 |
| Telecom services | 0.55 | 5.7 | 5.3 | 1.4 | 0.27 |
| Information technology | 0.50 | 8.5 | 9.0 | 1.6 | 0.18 |
| Financials | 0.43 | 7.5 | 8.3 | 1.5 | 0.18 |
| Materials | 0.41 | 4.6 | 4.7 | 0.9 | 0.19 |
| Energy | 0.35 | 5.0 | 4.9 | 1.7 | 0.34 |

Consumer-oriented sectors fade slowest; commodity and technology sectors fastest. Not in the sources: how closely CFROI tracks the FactSet ROIC in the tearsheet. Applying these r values to ROIC is an approximation; label it judgment.

**Table 10. Operating margin beta by sector** (A; ex-financials and utilities; dollars of operating profit change per $1.00 of sales change)

| Sector | 1-yr | 3-yr |
|---|---|---|
| All sectors | 0.115 | about 0.11 |
| Materials | 0.193 | 0.155 |
| Telecom services | 0.174 | 0.184 |
| Information technology | 0.173 | 0.158 |
| Energy | 0.134 | 0.103 |
| Health care | 0.115 | 0.111 |
| Industrials | 0.083 | 0.076 |
| Consumer discretionary | 0.081 | 0.074 |
| Consumer staples | 0.075 | 0.071 |

Analyst forecast errors are larger where beta is high.

**Table 11. Analyst overconfidence** (historical snapshots; verify, not current; real growth, largest companies)

| Item | Consensus | History | Source |
|---|---|---|---|
| SD of 3-year sales growth | 8.3% (Sept 2016) | 18.7% | A |
| SD of 3-year sales growth | 12.2% (Feb 2016) | 18.4% | Base Rate Book Sales Growth v2, 2016, "B" |
| SD of 3-year net income growth | 19.2% (Sept 2016) | 34.6% | A |
| Mean net income growth, S&P 1500 | 13.3% a year (Dec 2015) | 10.4% | Base Rate Book Earnings Growth, 2015, "D" |

Consensus dispersion is about half of historical dispersion, and few analysts forecast declines.

**Table 12. How often companies shrink** (from tables 1, 2 and 4)

| Outcome | Share of companies |
|---|---|
| Negative real sales CAGR over 3 years, all sizes | 22.6% |
| Negative real sales CAGR over 10 years, by size class | 4.9% ($0-325M) to 41.1% (>$50B) |
| Lower net income after 3 years, all sizes | 31.6% |
| Lower net income after 10 years, all sizes | 24.3% |

## Interpretation and limits

- Reversion is not proof of competition and does not mean dispersion shrinks. It occurs whenever r is below 1, works backward in time too, and the population distribution stays about the same (the Secrist error, paper F). Check dispersion before writing "everything converges".
- Where the sector mean is itself unstable (energy, materials, IT, telecom), do not fade to the long-run average blindly; shade it to mid-cycle and say where the sector is in its cycle (paper F; judgment).
- Base rates are not destiny: Apple's growth over 1981-1990 was achieved by under 0.5 percent of similar-size companies. Claim an exception only with a specific, evidenced reason, and never by citing one analogy.
- A margin trend is not structural change when the gain sits in the top quintile or comes from sector mix.
- Samples are large caps, mostly before 2016, with modest survivorship bias. Small caps, private companies and recent years are not covered.
- Banks and insurers: use returns on equity and price to book logic; the margin and gross profitability tables exclude financials.
- Not in the sources: base rates for small companies with negative earnings, or a split by region or for emerging markets. Say so and widen the range.

## Output lines

- "Consensus needs a 10-year real sales CAGR of X percent (derived, after Y percent assumed inflation). Z percent of companies in the $A to $B class achieved this (reported, historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted)."
- "Blended with the class median at W percent weight, the forecast is V percent (judgment; weights and inflation assumed)."
- "Operating margin is X percent against a sector mean of Y percent and a 5-year r of R. The expected margin in 5 years is Y + R x (X - Y) = M percent (derived)."
- "A sales miss of S percent implies an operating profit change of about beta x S (derived, historical sector beta)."
- "Consensus dispersion is X against historical dispersion of Y (reported, historical)."

## Sources

- Note: base-rates.md, Parts 1 to 3, 5 and 6.
- Mauboussin, Callahan and co-authors, Credit Suisse Global Financial Strategies: "A" The Base Rate Book (26 Sep 2016); "B" Base Rate Book: Sales Growth v2 (23 Feb 2016); "C" Base Rate Book: Sales Growth (4 May 2015); "D" Base Rate Book: Earnings Growth (16 Dec 2015); "E" Base Rate Book: Gross Profitability (25 Apr 2016); "F" How to Model Reversion to the Mean (17 Sep 2013); "G" What Makes for a Useful Statistic (5 Apr 2016).
