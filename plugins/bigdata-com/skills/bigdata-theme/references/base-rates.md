# Base rates and reversion to the mean

How a forecast of growth, margin or return on capital compares with what similar large companies achieved, and how fast an unusual level moves back toward its sector mean. Start from a reference class and move away from it only with evidence: a forecast built from the company's own story is usually too optimistic and too narrow. The tables are historical base rates for large, mostly listed companies, not forecasts or current facts.

## Inputs

| Input | Where it comes from |
|---|---|
| Prior-year sales (sets the size class), sales and net income history | Company tearsheet and annual statements, five fiscal years |
| Gross profitability | (Revenue - cost of goods sold) / total assets, from the income statement and balance sheet |
| Operating margin, ROIC | Financial ratios and statements |
| Sector | Company overview |
| Consensus growth, margin and EPS to four years out, long-term growth | Estimates, with their date |
| Expected inflation | Not in the company data. Take it from the country data, or state the figure used once |
| Sector mean and persistence r | The tables below |

## Choosing the reference class

State the quantity first: real or nominal, growth, margin or return on capital, and over how many years. Then pick the class:

- Sales and earnings growth: the size class by prior-year sales. For a mega cap, the above-$50B class.
- Margins, gross profitability and returns on capital: the sector.

The class must be large enough to be robust and narrow enough to be relevant. When the company differs in a way that matters, name the difference and still show the base rate.

## Placing a forecast in the distribution

Growth distributions are skewed to the right, so the median sits below the mean: quote the median and the threshold shares, not the mean alone. Place the forecast as a share of the class: "consensus needs a 10-year real sales CAGR of X percent, which Y percent of companies in the $A to $B class achieved." Between two thresholds, interpolate and say so.

Set the range at least as wide as history and include a decline case. The "share negative" and "share with decline" rows give its frequency: a negative 10-year real sales CAGR ran from 4.9 percent of the smallest class to 41.1 percent of the above-$50B class.

Then ask what must be true for the price (expectations.md, implied growth) and whether that bar sits in a rare part of the distribution. Claim an exception only with a specific, evidenced reason, never with one analogy.

## Real and nominal growth

The growth tables are real. Consensus is nominal. When comparing them, convert first: (1 + nominal) = (1 + real) x (1 + inflation); nominal is approximately real plus inflation.

## Regression to the mean

Expected outcome = mean + r x (current outcome - mean), where r is the correlation between the metric now and the same metric earlier. With r = 1 the best estimate is the last value; with r = 0 it is the mean. The same arithmetic in shrinkage form: estimated true level = grand average + c x (observed - grand average), c between 0 and 1, with r as the proxy for c.

- The more luck in the outcome, the more weight on the base rate.
- Sales and earnings growth beyond three years: put most of the weight on the class median. Their r is low (persistence table).
- Margins and gross profitability: start from the latest level and fade toward the sector mean at the sector's r.
- Returns on capital: apply the r that matches the horizon. The four-year r is higher than the one-year r compounded: a 10-point spread faded at a one-year r of 0.89 four times leaves 6.3 points, a four-year r of 0.78 leaves 7.8. Compounding overstates the speed of fading.
- Interpolating between years with r^(t/4) is an approximation; the single-r equation is meant for one adjustment over one horizon.

## Fade toward the cost of capital

A common valuation convention: an explicit fade period of about five years set by life-cycle position; then 10 percent of the spread over the long-run average eliminated each year (a spread of 10 points becomes 9); then a return equal to the cost of capital in the terminal period. Present it as a convention, not an empirical law.

## Threshold margin

Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 - tax rate)]. Growth at that margin is value-neutral; growth below it destroys value.

## Operating profit sensitivity

Change in operating profit is approximately the operating margin beta x change in sales (operating margin beta by sector). Financial leverage amplifies the effect on net income. Analyst forecast errors are larger where the beta is high, so widen the range there.

## Base-rate tables

Unless a table names another population: top 1,000 global companies by market cap, 1950 to 2015, inflation-adjusted. The sample includes companies that later disappeared, but a 10-year observation needs 10 years of survival, so modest survivorship bias remains.

### Real sales growth, all sizes

N = 53,266 at 3 years, 49,874 at 5, 41,645 at 10. Real CAGR. The 1-year column is noisy; use the 3-, 5- and 10-year columns.

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 5.8% | 5.4% | 5.2% | 4.9% |
| Mean | 14.8% | 8.1% | 6.9% | 5.8% |
| Standard deviation | 275% | 18.7% | 12.3% | 8.0% |
| Share >= 10% | 35.5% | 30.9% | 27.1% | 20.6% |
| Share >= 15% | 24.1% | 18.6% | 14.5% | 9.0% |
| Share >= 20% | 17.3% | 11.9% | 8.5% | 4.5% |
| Share >= 25% | 12.8% | 8.0% | 5.4% | 2.5% |
| Share above 45% | 5.5% | 2.5% | 1.3% | 0.3% |
| Share negative | 26.2% | 22.6% | 20.0% | 16.9% |

### Real sales growth by starting size

Prior-year sales in 2015 dollars. Each cell is 3-yr / 5-yr / 10-yr real CAGR unless the column says 10-yr. The above-$50B row is a subset of the above-$25B row.

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

The median and the dispersion both fall with size. Above $25B, large companies shrink in real terms about as often as they grow over a decade. In the $4.5-7B class no company grew 45 percent or more a year for 10 years, and 30 to 35 percent a year occurred in about 0.2 percent of the class.

### Real sales growth, S&P 1500 sample

S&P 1500 constituents, followed after they left the index, 1994 to 2014, inflation-adjusted to 2014 dollars. N = 23,914 at 3 years, 19,288 at 5, 10,681 at 10, 1,136 at 20.

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr | 20-yr |
|---|---|---|---|---|---|
| Median | 5.2% | 4.5% | 4.2% | 4.1% | 4.2% |
| Mean | 8.8% | 6.2% | 5.3% | 4.6% | 4.9% |
| SD | 50.3% | 16.4% | 13.1% | 9.6% | 6.7% |

Negative real sales CAGR: 31 percent of companies at 3 years, 30 percent at 5. Ten-year medians by sales class: $0-250M 8.8%; $250-450M 6.1%; $450-700M 5.4%; $700M-1B 5.0%; $1-1.5B 4.7%; $1.5-2.25B 3.6%; $2.25-3.5B 3.3%; $3.5-6B 3.0%; $6-13B 2.9%; above $13B 2.7%; above $50B 2.0%.

### Real net income growth, all sizes

Net income before extraordinary items. A CAGR needs positive beginning and ending earnings. N = 52,901 at 1 year, 48,472 at 3, 44,874 at 5, 37,305 at 10.

| Statistic | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 9.2% | 6.8% | 5.9% | 5.2% |
| Mean | 88.8% | 10.3% | 7.3% | 5.8% |
| SD | 7,842% | 34.6% | 20.2% | 11.0% |
| Share >= 10% | 48.4% | 41.5% | 36.6% | 28.0% |
| Share >= 20% | 33.4% | 23.1% | 16.3% | 7.5% |
| Share >= 30% | 24.4% | 13.6% | 7.5% | 2.4% |
| Share with lower net income | 33.0% | 31.6% | 29.3% | 24.3% |

### Real net income growth by starting size

Prior-year sales. Each cell is 3-yr / 5-yr / 10-yr.

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

The median falls with size but the dispersion barely does: the 3-year SD is 33 to 38 percent in every class. A 10-year CAGR of 20 percent or more occurred in 4 to 8 percent of any class.

### Persistence of growth, margins and returns

Correlation between a metric now and the same metric earlier.

| Metric | 1-yr r | 3-yr r | 5-yr r | Population |
|---|---|---|---|---|
| Sales growth | 0.30 | 0.17 | 0.19 | 1950-2015 |
| Net income growth | -0.05 | -0.23 | -0.24 | 1950-2015 |
| Gross profitability | 0.95 | 0.89 | 0.82 | 1950-2015, ex-financials and utilities |
| Operating margin | 0.91 | 0.79 | 0.72 | 1950-2015, ex-financials and utilities |
| CFROI | 0.78 | n/a | n/a | Global, 1983-2015, ex-financials and utilities; 4-yr r 0.56 |

Net income growth is not persistent but predicts total shareholder return (correlation 0.20, 0.39 and 0.40 at 1, 3 and 5 years, 1985 to 2015); sales growth predicts it weakly (0.20, 0.25, 0.28). Prefer metrics that are persistent, predictive or both.

### Gross profitability by sector

Gross profit / total assets. Top 1,000 global companies ex-financials and utilities, 1950 to 2015, no inflation adjustment. r is the 5-year correlation; SD and CoV are of the annual sector mean.

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

A value of 0.33 or higher is generally attractive. Gross profitability and P/E can point in opposite directions, so read them separately.

### Operating margin by sector

Operating income / sales. Top 1,000 global companies ex-financials and utilities, 1950 to 2015, no inflation adjustment.

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

### CFROI by sector

Cash flow return on investment, inflation-adjusted. Global companies, live and dead, market cap about $250M and above, 1983 to 2015, including financials and utilities. r is the 4-year correlation; SD and CoV are of the annual sector mean; winsorized at the 1st and 99th percentiles.

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

Consumer sectors fade slowest; commodity and technology sectors fastest. CFROI is a real cash return, so when applying these r values to a reported ROIC, treat the fade as an approximation and say the speed is a judgment.

### Operating margin beta by sector

Operating leverage: dollars of operating profit change per $1.00 of sales change. Ex-financials and utilities.

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

### Consensus dispersion against history

Real growth, largest companies. Consensus figures are snapshots from 2015 and 2016.

| Item | Consensus | History |
|---|---|---|
| SD of 3-year sales growth | 8.3% to 12.2% | 18.4% to 18.7% |
| SD of 3-year net income growth | 19.2% | 34.6% |
| Mean net income growth, S&P 1500 | 13.3% a year | 10.4% |

Consensus dispersion has run at about half of historical dispersion, and few analysts forecast declines. When a consensus range is narrower than the class, widen it to the class.

## Interpretation and limits

- When writing that levels converge, check the dispersion first. Reversion occurs whenever r is below 1, works backward in time too, and leaves the population distribution about the same; it is not proof of competition.
- When the sector mean is itself unstable (energy, materials, information technology, telecom), fade to a mid-cycle level rather than the long-run average, and say where the sector is in its cycle.
- When a margin gain sits in the top quintile or comes from sector mix, treat it as dispersion, not structural change.
- For banks and insurers, use return on equity and price to book; the margin, gross profitability and operating leverage tables exclude financials and utilities.
- The tables cover large caps, mostly before 2016. For a small company, a loss-making company, a private company or an emerging-market listing there is no matching class here: say so and widen the range beyond the nearest class.
