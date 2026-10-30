# After a large price move

Two questions after a stock moves sharply in one day: what happened next to stocks in the same situation, and does the news change long-term cash flows or only the near-term accounting line. Classify the event and read the matching drift before explaining the move, because a cause is easy to invent for any move. Drift figures condition a view; they never produce a call, a price target or a position size.

## Inputs

| Input | Where it comes from |
|---|---|
| Stock and index returns: 60 monthly for beta, daily for the windows | The price series through the computing tool; without it, the standard performance windows and dated reports, said so. Index: the S&P 500 to match the tables, or the home-market index, stated |
| Event type, earnings or not | Corporate calendar; filings and news for the event date |
| Cause stated by the company or the press | News, filings and transcripts for the event date |
| Momentum, valuation and quality proxies (listed under the factor scores below) | Company overview, estimates, analyst ratings, key metrics, financial ratios, five fiscal periods of statements |
| Change in the long-term outlook | Estimates for FY+2 to FY+4 and long-term growth, before and after the event; guidance; cash flow statement |
| Cost of capital for the quality spread | Not in the data. Choose it and state it |

Estimates are a current snapshot. Take the 13-week revisions and the pre-event target from research and news dated in the 13 weeks before the event.

## Classifying the event

- Earnings or non-earnings. Non-earnings covers scheduled items such as same-store-sales updates and unscheduled ones such as profit warnings.
- One day or several. The tables cover single-day moves.
- The move against the index, computed both as the simple excess return and beta-adjusted. State which one is used; a move that clears 10 percent on only one measure is a borderline member of the class.
- Announced M&A or not. The gain tables exclude announced M&A.

## Abnormal return

- **Beta:** slope of the stock's monthly total returns on the index's over the 60 months before the event, or the shorter window available, stated.
- **Abnormal return** on day t: AR(t) = R(stock, t) - beta x R(index, t), with no intercept.
- **Cumulative abnormal return:** CAR(a, b) = sum of AR(t) for trading days a to b. Windows: -30 to -1, the event day alone, and +1 to +30, +60 and +90. CAR resets to zero at the close of the event day.

## Momentum, valuation and quality before the event

Score each factor as it stood before the move, as a 0 to 100 percentile within the sector: top third (strong, cheap, high) at 67 or above, bottom third (weak, expensive, low) at 33 or below.

Re-base valuation so a stock is never scored cheap because it just fell: pre-event price = current price / (1 + return since the close before the event). Scale market cap, EV and the multiples to it before bucketing.

| Factor | Proxy |
|---|---|
| Momentum | 13-week change in consensus EPS and EBIT; target and rating changes; 52-week performance against the sector, excluding the event |
| Valuation | EV/EBITDA, P/E, FCF yield and price to book against peers; upside to a reverse-DCF or scenario value if the report has one; dividend yield |
| Quality | ROIC against peers; (ROIC - stated cost of capital) x invested capital; change in that spread over five fiscal periods; margin history |

Weight the proxies as the historical scores did: momentum 60 percent 13-week earnings revisions and 30 percent 52-week price change; valuation 50 percent model value against price and 30 percent economic P/E; quality 50 percent last year's cash return on investment, 30 percent its spread over the discount rate times invested capital, 20 percent the change in that spread.

## Drift after one-day drops

US large caps, one-day drops of 10 percent or more against the S&P 500, January 1990 to June 2014: more than 5,400 events, about 40 percent in the dot-com and 2008-2009 periods, about one quarter earnings releases. Mean CAR in percent, trading days from the close of the event day.

| Event type | Momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.6 | -14.9 | 408 | -1.5 | -1.9 | -0.6 |
| Earnings | Neutral | -2.8 | -14.7 | 434 | 0.8 | 2.4 | 4.0 |
| Earnings | Weak | -1.0 | -14.9 | 600 | 2.7 | 5.1 | 8.4 |
| Non-earnings | Strong | -4.6 | -13.8 | 1,041 | 3.7 | 4.9 | 6.2 |
| Non-earnings | Neutral | -5.9 | -14.4 | 1,067 | 4.7 | 9.4 | 11.3 |
| Non-earnings | Weak | -6.2 | -14.2 | 1,867 | 11.1 | 17.0 | 18.8 |

## Drift after one-day gains

US large caps, one-day gains of 10 percent or more against the S&P 500, excluding announced M&A, January 1990 to July 2015: 6,797 events, 36 percent in bubble periods, 1,505 earnings and 5,292 non-earnings. Full sample: -30d -5.9, event day 13.8, +30/+60/+90 of 3.5/6.1/7.0; earnings 2.7/3.7/4.1; non-earnings 3.8/6.8/7.9.

| Event type | Momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.3 | 13.9 | 411 | 1.1 | 1.9 | 2.3 |
| Earnings | Neutral | -1.6 | 14.1 | 429 | 2.1 | 3.9 | 4.2 |
| Earnings | Weak | -5.7 | 15.2 | 665 | 4.1 | 4.7 | 5.2 |
| Non-earnings | Strong | -7.5 | 12.7 | 1,137 | 1.2 | 1.5 | 1.7 |
| Non-earnings | Neutral | -7.5 | 13.5 | 1,383 | 2.8 | 6.2 | 7.1 |
| Non-earnings | Weak | -5.8 | 14.0 | 2,772 | 5.3 | 9.1 | 10.8 |

## Drift in the branches with the sharpest contrasts

Drops: the January 1990 to June 2014 population above; gains: the January 1990 to July 2015 population above. N falls with each split.

| Sample | Event type | Momentum, valuation, quality | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|
| Drop | Earnings | Weak, cheap | 299 | 3.7 | 5.5 | 10.9 |
| Drop | Earnings | Weak, cheap, high | 79 | 5.5 | 7.7 | 14.1 |
| Drop | Earnings | Strong, expensive | 167 | -2.4 | -4.5 | -3.2 |
| Drop | Non-earnings | Weak, cheap | 1,008 | 13.9 | 19.1 | 22.1 |
| Drop | Non-earnings | Weak, cheap, high | 282 | 10.4 | 14.9 | 23.0 |
| Drop | Non-earnings | Strong, expensive | 472 | 2.2 | 0.8 | 0.4 |
| Drop | Non-earnings | Strong, expensive, high | 225 | 1.9 | -2.8 | -3.2 |
| Drop | Non-earnings | Neutral, expensive, high | 132 | -2.5 | -4.5 | -3.7 |
| Gain | Earnings | Weak, cheap | 304 | 5.9 | 3.7 | 5.2 |
| Gain | Earnings | Strong, expensive | 153 | -0.6 | -1.4 | -2.8 |
| Gain | Earnings | Strong, expensive, high | 65 | -2.3 | -1.7 | -6.0 |
| Gain | Non-earnings | Weak, cheap | 1,270 | 7.6 | 11.4 | 13.5 |
| Gain | Non-earnings | Strong, expensive | 456 | 0.0 | -4.5 | -6.2 |
| Gain | Non-earnings | Strong, expensive, high | 209 | 0.0 | -7.0 | -7.9 |

With the dot-com and 2008-2009 periods removed from the drop population, the direction matches the full sample in over 80 percent of earnings branches and close to 90 percent of non-earnings branches. Earnings drops, strong and expensive: N 129, -2.2/-3.8/-3.3. Non-earnings drops, strong, expensive, high quality: N 153, -0.1/-7.6/-8.0. Non-earnings drops, weak and cheap: N 473, 6.2/9.3/8.1.

## Dispersion of drift

Mean / median / standard deviation of CAR, percent. Drops: January 1990 to June 2014; gains: January 1990 to July 2015; US large caps against the S&P 500.

| Reference class | N | +30d | +60d | +90d |
|---|---|---|---|---|
| Drops, non-earnings, weak, cheap, high quality | 282 | 10.4 / 7.6 / 34.7 | 14.9 / 10.0 / 40.4 | 23.0 / 18.2 / 46.0 |
| Drops, non-earnings, weak momentum | 1,867 | 11.1 / 7.0 / 33.7 | 17.0 / 12.2 / 40.6 | 18.8 / 13.7 / 46.5 |
| Gains, non-earnings, weak, cheap, low quality | 455 | 7.6 / 6.1 / 32.0 | 11.0 / 7.5 / 38.8 | 12.0 / 8.0 / 46.1 |

## Reading the drift tables

- Start at the row for the event type and momentum, then step down to valuation and quality only while N stays at about 50 or more. Quote N, the period and the parent row with any branch.
- After drops and gains alike, mean drift is positive when momentum going in was weak, and larger for non-earnings events than for earnings. It is flat to negative when momentum was strong and valuation expensive.
- A higher mean does not make a gain likely: the median sits below the mean and the standard deviation runs 32 to 47 points. State the dispersion with the mean.
- Means are positive in most cells, partly from the measurement (no intercept, survivorship not controlled). Read the difference between branches and the sign against the full-sample row, not the level.
- The tables ignore the size of the surprise, guidance and the stated reason, and do not separate banks, cyclicals or early-stage companies; for those, widen the range.
- A multi-day move, a move under 10 percent, a non-US stock or a date after mid-2015 is outside the population: quote the nearest row as context only and say so.

## Long-term outlook test

The price reacts to changes in expected long-term cash flows. Short-term earnings matter only as signals of long-term earning power, and when earnings and cash diverge the price follows cash. Ask:

- (a) Did consensus for FY+2 and beyond, long-term growth or guidance change, and by how much?
- (b) Do the drivers recur (price, volume, margin structure) or are they one-time?
- (c) Does cash flow agree with the earnings line?
- (d) Which revision matters for this company? Where ROIC is near the cost of capital, the return on new investment moves value and growth does not; where ROIC is high, sales growth moves value (expectations.md, which revision moves value).
- (e) Does the information change the probability of the thesis, or does it only look causal, such as an EPS dilution headline on an acquisition whose synergies exceed the premium?

Class the move long-term, short-term or unclear, with the evidence.

## Decomposing the move

Split the move into fundamental news, a change in the multiple, and flows such as index changes, mandate constraints or tax selling. Most day-to-day moves are supply and demand. A price is an offer, not evidence of value.

## Errors

- A narrative before the classification.
- A branch with N under about 50 quoted as a finding: earnings drops with weak momentum, neutral valuation and high quality show -2.5 at +30 days against +2.7 for the weak-momentum parent.
- Judging a prior call by its result.
- Reading the sign of an average as a forecast.
