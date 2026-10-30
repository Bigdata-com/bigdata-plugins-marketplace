# Spec: Base rates and reversion

## 1. Purpose
This method answers: how does a forecast of growth, margin or return on capital compare with what happened to similar large companies, and how fast should an unusual level move back toward its sector mean. It starts from the history of a reference class (the outside view) and moves away only with evidence, instead of extrapolating company specifics (the inside view). Jobs: earnings preview (is consensus plausible), valuation (growth and fade), thesis, company view, sector comparison. Sources: Mauboussin and co-author Base Rate Book papers (Credit Suisse, 2013 to 2016). Every number is a historical base rate for large, mostly listed companies, not a forecast or a current fact.

Label rule: every table in the finished file carries the label for its sample, as written above each table in section 4. Main label: "Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact."

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Prior-year sales (size class), sales and net income history | Tearsheet income statement, 5 fiscal periods | reported |
| Gross profitability = (revenue - cost of goods sold) / total assets | Tearsheet income statement and balance sheet | derived |
| Operating margin, ROIC | Tearsheet ratios and income statement | reported or derived |
| Sector, size class | Tearsheet company profile | reported |
| Consensus growth, margin, EPS to FY+4, long-term growth | Tearsheet estimates | reported |
| Expected inflation | GAP: not in the Bigdata.com fields; use an explicit assumption and state it | assumed |
| Sector mean and persistence r | Tables in section 4 | reported (historical) |

## 3. Procedure
1. State the quantity (real or nominal growth, margin, return on capital) and the horizon. Done when both are written.
2. Choose the reference class: size class by prior-year sales for growth; sector for margins, profitability and returns; the above-$50B class for mega caps. Large enough to be robust, narrow enough to be relevant (Base Rate Book, 26 Sep 2016, "A"). Done when class and N are stated.
3. Assess the distribution, not only the average; it is right-skewed and the median is below the mean. Done when median, mean, dispersion and tail shares are quoted.
4. Place the forecast: "this needs a 10-year real sales CAGR of X percent, which Y percent of companies in the $A to $B class achieved (sample label)". The notes give shares at fixed thresholds only; interpolate and say so. GAP: no full percentile tables.
5. Convert real to nominal before comparing with consensus (5.4).
6. Blend by persistence (5.1): beyond 3 years, majority weight on the class median for growth; start from the latest level for margins and gross profitability; apply the horizon-matched r to returns on capital. Done when the blend and weights are shown.
7. Set a range at least as wide as history and include a decline case (5.5).
8. Ask which assumption must hold for the price to be right (expectations.md) and whether it sits in a rare part of the distribution. Claim an exception only with a specific, evidenced reason.

## 4. Reference tables

### 4.1 Sales growth, all sizes
Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact. (Base Rate Book 2016, "A"; N = 53,266 for 3-year, 49,874 for 5-year, 41,645 for 10-year; real CAGR.)
| Stat | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 5.8% | 5.4% | 5.2% | 4.9% |
| Mean | 14.8% | 8.1% | 6.9% | 5.8% |
| Standard deviation | 275% | 18.7% | 12.3% | 8.0% |
| Share with CAGR >= 10% | 35.5% | 30.9% | 27.1% | 20.6% |
| Share >= 15% | 24.1% | 18.6% | 14.5% | 9.0% |
| Share >= 20% | 17.3% | 11.9% | 8.5% | 4.5% |
| Share >= 25% | 12.8% | 8.0% | 5.4% | 2.5% |
| Share >= 45% | 5.5% | 2.5% | 1.3% | 0.3% |
| Share negative | 26.2% | 22.6% | 20.0% | 16.9% |
Use the 3-, 5- and 10-year columns; the 1-year column is noisy. Includes companies that later disappeared; modest survivorship bias remains.

### 4.2 Sales growth by starting size (prior-year sales, 2015 dollars)
Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact. (Base Rate Book 2016, "A". Columns are 3-yr / 5-yr / 10-yr, real CAGR. The ">$50B" row is a subset of ">$25B".)
| Prior-year sales | Median | Mean 10-yr | SD 10-yr | Share >=15% | Share >=20% | Share <0 |
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
Reading: median and dispersion fall with size. Above $25B, 35.5 percent had negative 10-year real CAGR. For the $4.5-7B class, no company grew 45 percent or more for 10 years. Share columns were derived by the note author from published bins.

### 4.3 Sales growth, alternate sample
Historical base rate, S&P 1500 constituents, 1994-2014, inflation-adjusted (2014 dollars), followed after index exit. Not a forecast and not a current fact. (Base Rate Book Sales Growth, 4 May 2015, "C"; N: 3-yr 23,914, 5-yr 19,288, 10-yr 10,681, 20-yr 1,136.)
| Stat | 1-yr | 3-yr | 5-yr | 10-yr | 20-yr |
|---|---|---|---|---|---|
| Median | 5.2% | 4.5% | 4.2% | 4.1% | 4.2% |
| Mean | 8.8% | 6.2% | 5.3% | 4.6% | 4.9% |
| SD | 50.3% | 16.4% | 13.1% | 9.6% | 6.7% |
Negative real sales CAGR: 31 percent of companies at 3 years, 30 percent at 5. Ten-year medians by sales class: $0-250M 8.8%; $250-450M 6.1%; $450-700M 5.4%; $700M-1B 5.0%; $1-1.5B 4.7%; $1.5-2.25B 3.6%; $2.25-3.5B 3.3%; $3.5-6B 3.0%; $6-13B 2.9%; above $13B 2.7%; above $50B 2.0%.

### 4.4 Net income growth, all sizes
Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact. (Base Rate Book 2016, "A"; net income before extraordinary items, real CAGR; CAGR needs positive beginning and ending earnings; N: 1-yr 52,901, 3-yr 48,472, 5-yr 44,874, 10-yr 37,305.)
| Stat | 1-yr | 3-yr | 5-yr | 10-yr |
|---|---|---|---|---|
| Median | 9.2% | 6.8% | 5.9% | 5.2% |
| Mean | 88.8% | 10.3% | 7.3% | 5.8% |
| SD | 7,842% | 34.6% | 20.2% | 11.0% |
| Share >= 10% | 48.4% | 41.5% | 36.6% | 28.0% |
| Share >= 20% | 33.4% | 23.1% | 16.3% | 7.5% |
| Share >= 30% | 24.4% | 13.6% | 7.5% | 2.4% |
| Share with lower net income | 33.0% | 31.6% | 29.3% | 24.3% |

### 4.5 Net income growth by starting size (prior-year sales)
Historical base rate, top 1,000 global companies by market cap, 1950-2015, inflation-adjusted. Not a forecast and not a current fact. (Base Rate Book 2016, "A". Columns are 3-yr / 5-yr / 10-yr.)
| Prior-year sales | Median | Share >=20% | Share >=30% | Share with decline |
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
Reading: the median falls with size but dispersion barely does (3-year SD 33 to 38 percent in every class). A 10-year CAGR of 20 percent or more is rare (4 to 8 percent of any class). Of the 200 highest-net-income companies in 1990, 162 survived to 2000; 14 (under 9 percent) grew net income 15 percent or more a year over 1990-1999; none sustained it for the decade to 2009.

### 4.6 Persistence (correlation between a metric now and the same metric earlier)
Historical base rate, top 1,000 global companies by market cap; sample as listed in the last column. Not a forecast and not a current fact.
| Metric | 1-yr r | 3-yr r | 5-yr r | Sample and source |
|---|---|---|---|---|
| Sales growth | 0.30 | 0.17 | 0.19 | 1950-2015, "A" |
| Net income growth | -0.05 | -0.23 | -0.24 | 1950-2015, "A" |
| Gross profitability | 0.95 | 0.89 | 0.82 | 1950-2015, ex-financials and utilities, "A", "E" |
| Operating margin | 0.91 | 0.79 | 0.72 | 1950-2015, ex-financials and utilities, "A" |
| CFROI | 0.78 | n/a | n/a | global, 1983-2015, ex-financials and utilities, "A"; the 4-year r is 0.56 |
Net income growth predicts total shareholder return (correlation 0.39 at 3 years, 0.40 at 5, 1985-2015) but is not persistent. Sales growth is weakly predictive (0.20, 0.25, 0.28 at 1, 3, 5 years). Prefer metrics that are persistent, predictive, or both ("G", What Makes for a Useful Statistic, 5 Apr 2016).

### 4.7 Gross profitability by sector
Historical base rate, top 1,000 global companies by market cap ex-financials and utilities, 1950-2015, ratio, no inflation adjustment. Not a forecast and not a current fact. (Base Rate Book 2016, "A". Gross profit / total assets; r is the 5-year correlation; SD and CoV are of the annual sector mean.)
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
A value of 0.33 or higher is generally attractive (Novy-Marx, cited in "E"). Profitability and P/E can give opposite signals (Amazon 2015: 0.54 with trailing P/E near 540).

### 4.8 Operating margin by sector
Historical base rate, top 1,000 global companies by market cap ex-financials and utilities, 1950-2015, ratio, no inflation adjustment. Not a forecast and not a current fact. (Base Rate Book 2016, "A". Operating income / sales.)
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
The aggregate margin rise since the mid-1980s is almost all in the top quintile (21 percent in 1985 to 31 percent in 2015); the bottom three quintiles were roughly flat. Use the sector figure, not the aggregate.

### 4.9 CFROI by sector
Historical base rate, global companies, live and dead, market cap about $250M and above, 1983-2015, inflation-adjusted cash flow return on investment (Credit Suisse HOLT measure), including financials and utilities. Not a forecast and not a current fact. (Base Rate Book 2016, "A"; r is the 4-year correlation; SD and CoV are of the annual sector mean; winsorized 1st and 99th percentile.)
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
Consumer-oriented sectors fade slowest; commodity and technology fastest. GAP: CFROI is a HOLT measure and the tearsheet has ROIC; the notes do not say how closely they track. State that r is applied to ROIC as an approximation (judgment).

### 4.10 Operating margin beta by sector
Historical base rate, top 1,000 global companies by market cap ex-financials and utilities, 1950-2015, ratio, no inflation adjustment. Not a forecast and not a current fact. (Base Rate Book 2016, "A". Slope of the change in operating profit on the change in sales: $ of operating profit per $1.00 of sales change.)
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
Use: operating profit change is roughly beta x change in sales; financial leverage amplifies it. Analyst errors are larger where beta is high.

## 5. Formulas and conventions
### 5.1 Regression to the mean and shrinkage
- Expected outcome = mean + r x (current outcome - mean). With r = 1 the best estimate is the last value; with r = 0 it is the mean (Mauboussin, "How to Model Reversion to the Mean", 17 Sep 2013, "F").
- Shrinkage form: estimated true level = grand average + c x (observed - grand average), c between 0 and 1, with r between successive periods as the proxy for c. Worked source example: grand average 8 percent, observed 12 percent, c = 0.10 gives 8.4 percent.
- Source example: Microsoft CFROI 16.1 percent, IT mean 9.0 percent, 4-year r 0.50 gives 12.6 percent in four years.
- The more luck in the outcome, the more weight on the base rate; the more skill, the more on the inside view.
- Use the horizon-matched r. The 4-year r exceeds the 1-year r compounded: for staples with CFROI 10 points above the sector mean, 0.89 applied four times leaves 6.3 points; the 4-year r of 0.78 leaves 7.8 points (paper "F" with its 2013 data: 6.0 versus 7.3). The one-year r overstates the speed of fading.
- Interpolating between years with r^(t/4) is an approximation by the note author, not a method in the papers.

### 5.2 Fade convention (HOLT, paper "F" endnote 1)
Explicit fade for 5 years set by life-cycle position; then 10 percent of the spread over the long-run average is eliminated each year (a spread of 10 points becomes 9); then the return equals the cost of capital in the terminal period. State it as a convention, not an empirical law.

### 5.3 Threshold margin (value test for growth)
Incremental threshold margin = (incremental fixed capital rate + incremental working capital rate) x cost of capital / [(1 + cost of capital) x (1 - tax rate)]. Source example: (0.35 + 0.25) x 0.10 / (1.10 x 0.65) = 8.4 percent; growth at that margin is value-neutral. Growth below it destroys value.

### 5.4 Real versus nominal
The tables are real. Consensus is nominal. Nominal growth is approximately real growth plus expected inflation; exactly, (1 + nominal) = (1 + real) x (1 + inflation) (derived identity). Convert before comparing, and state the inflation assumed.

### 5.5 Analyst overconfidence
Historical snapshots, verify, not current. Real growth, largest companies.
| Item | Consensus | History | Source |
|---|---|---|---|
| SD of 3-year sales growth | 8.3% (Sept 2016) | 18.7% | "A" |
| SD of 3-year sales growth | 12.2% (Feb 2016) | 18.4% | Base Rate Book Sales Growth v2, 23 Feb 2016, "B" |
| SD of 3-year net income growth | 19.2% (Sept 2016) | 34.6% | "A" |
| Mean net income growth, S&P 1500 | 13.3% a year (Dec 2015) | 10.4% | Base Rate Book Earnings Growth, 16 Dec 2015, "D" |
Consensus dispersion is about half of the historical dispersion. Few analysts forecast declines, yet 23 percent of companies had negative 3-year real sales CAGR and 31 percent had lower net income after 3 years (table 4.1 and 4.4 samples).

## 6. Interpretation rules
- Reversion is not proof of competition and does not mean dispersion shrinks. It occurs whenever r is below 1 and also works backward in time (Secrist error, "F"). Check dispersion first.
- Where the sector mean is unstable (energy, materials, IT, telecom) shade to mid-cycle ("F"; judgment).
- Base rates are not destiny: Apple 1981-1990 was under 0.5 percent of similar-size companies. Claim an exception only with a specific, evidenced reason.
- Samples are large caps, mostly pre-2016, with modest survivorship bias; small caps, private companies and recent years are not covered. Not applicable without adjustment to banks (CFROE and P/B logic), early-stage companies (GAP: no base rate for small companies with negative earnings) and emerging markets (GAP: no region split).
- A margin trend is not structural change when the gain sits in the top quintile or sector mix.
- Last year's growth says little about next year's: sales growth r is 0.30 at one year, high teens at 3 to 5; net income growth r is negative.

## 7. How-to-use checklist (from the notes)
1. Name quantity and horizon. 2. Pick the reference class. 3. Report the forecast's position in the distribution. 4. Weight by persistence. 5. Use the sector mean if its SD is small (staples, discretionary), mid-cycle if volatile. 6. Range: history SD is about twice consensus SD. 7. Convert real to nominal. 8. Ask what must be true for the price to be right.

## 8. Output lines
- "Consensus needs a 10-year real sales CAGR of X percent. Y percent of companies in the $A to $B class achieved this (reported, historical base rate, sample label)."
- "Blended with the class median at W percent weight, the forecast is Z percent (judgment; weights and inflation assumed)."
- "Operating margin is X percent against a sector mean of Y percent and 5-year r of R. Expected margin in 5 years is Y + R x (X - Y) (derived)."
- "A sales miss of S percent implies an operating profit change of about beta x S (derived, historical beta)."
- "Consensus SD is X against historical SD Y (reported, historical)."

## 9. Sources
Notes: base-rates.md (Parts 1 to 3, 5, 6). Papers (Mauboussin and co-authors, Credit Suisse): "A" The Base Rate Book (26 Sep 2016); "B" Sales Growth v2 (23 Feb 2016); "C" Sales Growth (4 May 2015); "D" Earnings Growth (16 Dec 2015); "E" Gross Profitability (25 Apr 2016); "F" How to Model Reversion to the Mean (17 Sep 2013); "G" What Makes for a Useful Statistic (5 Apr 2016).
