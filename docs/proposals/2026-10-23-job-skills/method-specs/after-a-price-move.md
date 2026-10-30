# Spec: After a large price move

## 1. Purpose
This method answers: the ticker moved sharply in one day, what does the historical record say happens next to stocks in the same situation, and does the news change the company's long-term cash flows or only the short-term accounting line. Jobs that use it: stock-move note, earnings reaction (when the print caused a move of 10% or more against the index), company brief after a gap, risk (drop or gain triage). The method produces a reference-class prior with its sample size, dates and dispersion, then sets it against the facts of the case. The base rates condition a view. They never produce a buy, hold or sell call, a price target or a position size, and the skill must say so in the note.

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Event date, stock return, index return, 60 monthly returns for beta | bigdata_computer on price series (the tearsheet carries performance fields only). Index: S&P 500 as in the papers, or the home-market index (state which) | reported, then derived |
| Event type: scheduled earnings release or not | Events calendar, company filings and news search for the event date | reported |
| Cause stated by the company or press | Search over news, filings, transcripts for the event date | reported |
| Momentum proxies: relative price performance over 52 weeks excluding the event, estimate revisions over 13 weeks, analyst target and rating changes | Tearsheet price_performance, consensus estimates, analyst targets and ratings. GAP: verify whether the tearsheet exposes consensus history; if not, take revisions from broker-research and news search in the 13 weeks before the event | derived |
| Valuation proxies | Tearsheet key_metrics: EV/EBITDA, P/E, FCF yield, price to book, dividend yield, against sector peers | derived |
| Quality proxies | Tearsheet ratios (FactSet ROIC) and 5 fiscal periods of margins and invested capital | derived |
| Change in long-term outlook | Consensus for FY+2 to FY+4 and long-term growth before and after the event, guidance, cash flow statement | reported, then derived |
| Cost of capital for the spread proxy | Not available in Bigdata.com (no WACC). The analyst chooses it and states it | assumed |

## 3. Procedure
1. Classify the event. Done when the note states: earnings or non-earnings (scheduled items such as same-store-sales updates and unscheduled items such as management changes or earnings warnings both count as non-earnings); one day or several days; the relative move against the index; and whether an announced merger or acquisition is involved. The papers cover one-day moves of 10% or more against the S&P 500 and exclude M&A-related gains (Summit). GAP: the notes do not say whether the 10% trigger uses simple excess return or the beta-adjusted figure; compute both and state which is used.
2. Measure the abnormal return and the pre-event record (formulas 4.1 to 4.3). Done when the event-day abnormal return and the 30-trading-day pre-event cumulative abnormal return are stated.
3. Score the three factors as they stood before the event, against sector peers: momentum, valuation, quality. Use the proxies in section 5.3. Bucket each into top third (strong, cheap, high), middle third (neutral) and bottom third (weak, expensive, low). The papers cut at a 0 to 100 sector percentile of 66 or higher and 33 or lower (Summit: 67 and 34 to 66). Done when each factor shows its bucket, numbers and peer set, and the note says the proxy is not the HOLT score.
4. Read the reference class (section 5.1 and 5.2): start at the top-level row for the event type and momentum, then step down to valuation and quality only while N stays at about 50 or more. Done when the note shows the branch, N, sample period, mean cumulative abnormal return at +30, +60 and +90 trading days, and the parent branch beside it.
5. State the dispersion (section 5.4). Done when the note says the mean is above the median in most cells and the standard deviation is 30 to 46 points.
6. Run the long-term outlook test (section 6.1). Done when the note states what changed in expected cash flows beyond the next year, with the before and after figures, and whether the price move matches that change.
7. List what is unknown. Done when the note names the facts missing for a cause and supplies no narrative the data cannot support.
8. Close with what would change the read, dated where possible (next earnings date, guidance update, filing). Done when each item is checkable.

## 4. Formulas
4.1 Beta. Slope of the regression of the stock's monthly total returns on the index's monthly total returns over the prior 60 months, ending before the event. Examples in the papers: 0.8 (Symantec, 60 months to Feb 2014) and 2.2 (Harman, 60 months to Jul 2013). If fewer than 60 months exist, state the shorter window (assumed).
4.2 Abnormal return on day t: AR(t) = R(stock,t) - beta x R(index,t). There is no intercept (Man Overboard p.8).
4.3 Cumulative abnormal return: CAR(a,b) = sum of AR(t) for t from a to b in trading days. Windows: -30 to -1 before the event, the event day alone, and +1 to +30, +60, +90. CAR resets to zero at the close of the event day. Worked example from the paper: stock +10.3% over 30 days, index +1.2%, beta 0.8, so CAR = 10.3% - 0.8 x 1.2% = 9.3%.

## 5. Reference tables
All figures are mean cumulative abnormal returns in percent, historical reference-class averages, not forecasts. Source: Credit Suisse Global Financial Strategies, "Managing the Man Overboard Moment" (15 Jan 2015, Exhibits 2 and 3) and "Celebrating the Summit" (11 Jan 2016, Exhibits 2 to 4). Universe: US stocks, abnormal returns against the S&P 500; the notes do not describe survivorship treatment. Data source in the papers: Credit Suisse HOLT. Verify against current data before presenting as current.

### 5.1 Man Overboard: one-day drops of 10% or more against the index
Sample: January 1990 to June 2014; more than 5,400 events; about 40% fall in the dot-com and 2008 to 2009 periods; about one quarter are earnings releases.
| Event type | Prior momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.6 | -14.9 | 408 | -1.5 | -1.9 | -0.6 |
| Earnings | Neutral | -2.8 | -14.7 | 434 | 0.8 | 2.4 | 4.0 |
| Earnings | Weak | -1.0 | -14.9 | 600 | 2.7 | 5.1 | 8.4 |
| Non-earnings | Strong | -4.6 | -13.8 | 1,041 | 3.7 | 4.9 | 6.2 |
| Non-earnings | Neutral | -5.9 | -14.4 | 1,067 | 4.7 | 9.4 | 11.3 |
| Non-earnings | Weak | -6.2 | -14.2 | 1,867 | 11.1 | 17.0 | 18.8 |

### 5.2 Celebrating the Summit: one-day gains of 10% or more against the index
Sample: January 1990 to July 2015; 6,797 events excluding announced M&A; 36% in bubble periods; 1,505 earnings and 5,292 non-earnings. Full sample: -30d -5.9, event day 13.8, +30/+60/+90 of 3.5/6.1/7.0. Earnings 2.7/3.7/4.1; non-earnings 3.8/6.8/7.9.
| Event type | Prior momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.3 | 13.9 | 411 | 1.1 | 1.9 | 2.3 |
| Earnings | Neutral | -1.6 | 14.1 | 429 | 2.1 | 3.9 | 4.2 |
| Earnings | Weak | -5.7 | 15.2 | 665 | 4.1 | 4.7 | 5.2 |
| Non-earnings | Strong | -7.5 | 12.7 | 1,137 | 1.2 | 1.5 | 1.7 |
| Non-earnings | Neutral | -7.5 | 13.5 | 1,383 | 2.8 | 6.2 | 7.1 |
| Non-earnings | Weak | -5.8 | 14.0 | 2,772 | 5.3 | 9.1 | 10.8 |

### 5.3 Leaf rows to carry (strongest contrasts; N shown because it falls with each split)
Drops use the 1990 to Jun 2014 sample, gains the 1990 to Jul 2015 sample. Columns are N, then +30d, +60d, +90d.
| Sample | Event type | Branch (momentum, valuation, quality) | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|
| Drop | Earnings | Weak, cheap | 299 | 3.7 | 5.5 | 10.9 |
| Drop | Earnings | Weak, cheap, high quality | 79 | 5.5 | 7.7 | 14.1 |
| Drop | Earnings | Strong, expensive | 167 | -2.4 | -4.5 | -3.2 |
| Drop | Non-earnings | Weak, cheap | 1,008 | 13.9 | 19.1 | 22.1 |
| Drop | Non-earnings | Weak, cheap, high quality | 282 | 10.4 | 14.9 | 23.0 |
| Drop | Non-earnings | Strong, expensive | 472 | 2.2 | 0.8 | 0.4 |
| Drop | Non-earnings | Strong, expensive, high quality | 225 | 1.9 | -2.8 | -3.2 |
| Drop | Non-earnings | Neutral, expensive, high quality | 132 | -2.5 | -4.5 | -3.7 |
| Gain | Earnings | Weak, cheap | 304 | 5.9 | 3.7 | 5.2 |
| Gain | Earnings | Strong, expensive | 153 | -0.6 | -1.4 | -2.8 |
| Gain | Earnings | Strong, expensive, high quality | 65 | -2.3 | -1.7 | -6.0 |
| Gain | Non-earnings | Weak, cheap | 1,270 | 7.6 | 11.4 | 13.5 |
| Gain | Non-earnings | Strong, expensive | 456 | 0.0 | -4.5 | -6.2 |
| Gain | Non-earnings | Strong, expensive, high quality | 209 | 0.0 | -7.0 | -7.9 |
The full trees (momentum by valuation by quality, 36 rows per event type) are in decisions-price-moves.md, Parts 1.1 and 1.2. Ex-bubble subsample (dot-com and 2008 to 2009 removed; Man Overboard Exhibits 12 and 13), same direction in over 80% of earnings branches and close to 90% of non-earnings branches: earnings drops, strong and expensive N 129, -2.2/-3.8/-3.3; non-earnings drops, strong, expensive, high quality N 153, -0.1/-7.6/-8.0; non-earnings drops, weak and cheap N 473, 6.2/9.3/8.1.

### 5.4 Dispersion (Man Overboard p.4, p.11; Summit p.5)
| Reference class | N | +30d mean / median / SD | +60d | +90d |
|---|---|---|---|---|
| Drops, non-earnings, weak, cheap, high quality | 282 | 10.4 / 7.6 / 34.7 | 14.9 / 10.0 / 40.4 | 23.0 / 18.2 / 46.0 |
| Drops, non-earnings, weak momentum | 1,867 | 11.1 / 7.0 / 33.7 | 17.0 / 12.2 / 40.6 | 18.8 / 13.7 / 46.5 |
| Gains, non-earnings, weak, cheap, low quality | 455 | 7.6 / 6.1 / 32.0 | 11.0 / 7.5 / 38.8 | 12.0 / 8.0 / 46.1 |

### 5.5 Factor proxies (adaptation, not from the papers)
| Factor | Paper definition (HOLT, percentile within sector) | Bigdata.com proxy |
|---|---|---|
| Momentum | 60% change in expected CFROI after EPS revisions (13 weeks), 30% price change over 52 weeks, 10% liquidity | 13-week change in consensus EPS and EBIT, analyst target and rating changes, 52-week price performance relative to sector, excluding the event |
| Valuation | 50% HOLT warranted value against price, 30% economic P/E, 10% value-to-cost, 10% dividend yield | EV/EBITDA, P/E, FCF yield and price to book against sector peers; upside to the analyst's own reverse-DCF or scenario value if one exists; dividend yield |
| Quality | 50% CFROI last year, 30% (CFROI minus discount rate) x gross investment, 20% change in that spread | FactSet ROIC level against peers; (ROIC minus an assumed cost of capital) x invested capital; change in that spread over 5 fiscal periods; margin history |

## 6. Interpretation rules
6.1 Long-term outlook test. The market reacts to changes in expectations about long-term cash flows, not to the headline. Share prices respond to short-term earnings only as signals of long-term earnings potential, and the market follows cash when earnings and cash diverge (Credit Suisse, "A Long Look at Short-Termism", 18 Nov 2014, p.9 to 10). Ask five questions. (a) Did consensus for FY+2 and beyond, long-term growth, or guidance change, and by how much. (b) Is the change driven by items that recur (price, volume, margin structure) or by one-time items. (c) Does cash flow agree with the earnings line. (d) Which revision matters for this company: where ROIC is near the cost of capital, the return on new investment moves value and growth does not; where ROIC is high, sales growth moves value (Mauboussin, "Expectations Investing", p.66). (e) Is the information diagnostic, meaning it changes the probability of the thesis, or only looks causal, such as an EPS dilution headline on an acquisition whose synergies exceed the premium (Credit Suisse, "Cultivating Your Judgment Skills", 7 May 2013, p.10). Result: classify the move as long-term, short-term or unclear.
6.2 Decompose the move into fundamental news, change in the multiple, and flows such as index changes, mandate constraints or tax selling (Klarman, Margin of Safety, Ch.1). Most day-to-day moves are supply and demand. Price is an offer, not evidence of value.
6.3 What the tables say. After large drops and gains, average cumulative abnormal returns are positive when prior momentum was weak, larger for non-earnings events than for earnings events, and flat to negative when momentum was strong and valuation expensive. A higher average does not make a positive outcome likely: the median is below the mean and the standard deviation is 30 to 46 points. Averages are positive in most cells after both drops and gains, which can reflect sample or method (no intercept, unstated survivorship). Use differences between branches and the sign relative to the full-sample row, not the absolute level.
6.4 Limits. US stocks, 1990 to mid-2014 or mid-2015, including two bubble and bust episodes. GAP: the notes contain no base rates for multi-day moves, moves under 10%, non-US stocks, the years after publication, or the size of the earnings surprise. Banks, cyclicals and early-stage companies are not separated in the papers; state the sector and widen the range. The papers say the result complements fundamental analysis and does not replace it.
6.5 Errors to avoid: a narrative before classification; a leaf row with N under about 50 quoted as a finding (earnings drops with weak momentum, neutral valuation and high quality show -2.5 at +30 days against +2.7 for the weak-momentum parent); judging a prior call by the result; reading the sign of an average as a forecast.

## 7. Output lines
- Event: "[Ticker] [fell/rose] [x]% on [date] against [index] [y]%, a relative move of [z]% ([w]% beta-adjusted, beta [b] over [n] months). Classified as [earnings / non-earnings], [one day / multi-day]." (derived)
- Cause: "[Company-stated or reported cause], source [document, date]." (reported). If none: "No cause is established in the sources reviewed." (judgment)
- Going in: "Momentum [strong/neutral/weak]: 52-week relative performance [x]%, 13-week EPS revision [y]%. Valuation [cheap/neutral/expensive]: [multiples against peers]. Quality [high/neutral/low]: ROIC [r]%, [trend]. These are proxies, not HOLT scores." (derived; cost of capital, if used, assumed)
- Reference class: "In [sample period], [N] stocks with a [branch] move showed a mean cumulative abnormal return of [a], [b], [c]% at 30, 60 and 90 trading days; median [m], standard deviation [s] where published. Parent branch: [N], [a], [b], [c]. Historical average, not a forecast." (reported)
- Outlook test: "Consensus FY+2 [EPS/EBIT] moved from [x] to [y]; guidance [changed/unchanged]; [one-time/recurring] items [list]. The move is [consistent/inconsistent] with the change in long-term cash flow." (derived, judgment)
- Unknowns: "Not established: [items]. Base rates do not cover [multi-day, non-US, surprise size]." (judgment)
- What would change the read: "[Dated, checkable item]." (judgment)
- Facts and opinions kept separate, one line each. Close with: "This note conditions the view; it does not recommend a trade."

## 8. Sources
Notes: decisions-price-moves.md (Part 1 sections 1, 2, 11; Parts 3 and 5), base-rates.md (section 2.9, Part 6), klarman.md (Ch.1), expectations-multiples-dcf.md (section 1.2). Papers: Credit Suisse Global Financial Strategies, "Managing the Man Overboard Moment" (2015) and "Celebrating the Summit" (2016); "A Long Look at Short-Termism" (2014); "Cultivating Your Judgment Skills" (2013); Mauboussin, "Expectations Investing"; Klarman, Margin of Safety (1991).
