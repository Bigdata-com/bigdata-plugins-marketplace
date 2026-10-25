# After a large price move

This method answers two questions after a stock moves sharply in one day: what happened next, historically, to stocks in the same situation, and does the news change the company's long-term cash flows or only the near-term accounting line. It produces a reference-class prior with its sample size, dates and dispersion, then sets the facts of the case against it. The base rates come from two Credit Suisse papers, "Managing the Man Overboard Moment" (2015, drops) and "Celebrating the Summit" (2016, gains). They condition a view; they never produce a buy, hold or sell call, a price target or a position size, and the note says so. The order is fixed because people invent a cause for any effect: classify the event and quote the base rate before explaining it (Outcome Bias and the Interpreter, 2013).

## When a skill loads this file

Load it for a stock-move note, an earnings review when the print moved the stock 10 percent or more against the index, a company brief after a gap, and risk triage of a drop or a gain. For a narrow question ("is this drop unusual?") give the classification, the matching row with N and period, and the long-term outlook test in a few lines.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Event date, stock and index returns, 60 monthly returns for beta, daily returns for the windows | `bigdata_computer` on price series; the tearsheet carries performance fields only. Index: the S&P 500 as in the papers, or the home-market index (state which) | reported, then derived |
| Event type: scheduled earnings release or not | `bigdata_events_calendar`; `bigdata_search` over filings and news for the event date | reported |
| Cause stated by the company or the press | `bigdata_search` over news, filings and transcripts for the event date | reported |
| Momentum proxies | `company_overview` (52-week relative performance, excluding the event); `analyst_estimates` (13-week change in consensus EPS and EBIT); `analyst_ratings` (target and rating changes) | derived |
| Valuation proxies | `key_metrics` and `financial_ratios`, re-based to the pre-event price (formula 4): EV/EBITDA, P/E, FCF yield, price to book, dividend yield, against sector peers | derived |
| Quality proxies | `financial_ratios` (FactSet ROIC) and five fiscal periods of margins and invested capital | derived |
| Change in the long-term outlook | `analyst_estimates` for FY+2 to FY+4 and long-term growth before and after the event; guidance; cash flow statement | reported, then derived |
| Cost of capital for the quality spread | Not in Bigdata.com. Choose it and state it | assumed |

The tearsheet carries no history of consensus estimates or targets (its estimates section is a current snapshot). Take the 13-week revisions and the pre-event target from research and news searches covering the 13 weeks before the event, quote the document and its date, and label them as press or research summaries.

## Procedure

1. **Classify the event.** Earnings or non-earnings (scheduled items such as same-store-sales updates and unscheduled items such as management changes or earnings warnings count as non-earnings); one day or several; the move relative to the index; and whether announced M&A is involved (the gain sample excludes M&A). The papers cover one-day moves of 10 percent or more against the S&P 500. Not in the sources: whether the 10 percent trigger uses the simple excess return or the beta-adjusted figure; compute both and state which one is used. Done when the note says "a one-day move of X percent against the index, Y percent beta-adjusted, earnings-driven" or its equivalent.
2. **Measure the abnormal return and the record going in** (formulas 1 to 3). Done when the event-day abnormal return and the 30-trading-day pre-event cumulative abnormal return (CAR) are stated.
3. **Score momentum, valuation and quality as they stood before the event,** against sector peers, with the proxies in table 5. Bucket each into the top third (strong, cheap, high), the middle third (neutral) and the bottom third (weak, expensive, low). The papers cut a 0 to 100 sector percentile at 66 or higher and 33 or lower in Man Overboard, and at 67 or higher and 33 or lower in Summit. Scores are measured before the price move. Done when each factor shows its bucket, the numbers behind it and the peer set, and the note says the proxies are not HOLT scores. Valuation proxies are re-based to the pre-event price: pre-event price = current price / (1 + the stock's return since the close before the event), and market cap, EV, P/E, EV/EBITDA, FCF yield and price to book are scaled to it before bucketing, so a stock that just fell is not scored as cheap because it fell (formula 4, derived).
4. **Read the reference class** (tables 1 to 3). Start at the row for the event type and momentum, then step down to valuation and quality only while N stays at about 50 or more. Done when the note shows the branch, N, the sample period, the mean CAR at +30, +60 and +90 trading days, and the parent branch beside it.
5. **State the dispersion** (table 4). Done when the note says the median is below the mean in most cells and the standard deviation of outcomes is 32 to 47 points in the published cells.
6. **Run the long-term outlook test** (rule 1). Done when the note states what changed in expected cash flows beyond the next year, with before and after figures, and whether the size of the move matches that change.
7. **List what is unknown.** Done when the note names the facts missing for a cause and offers no narrative the data cannot support.
8. **Close with what would change the read,** dated where possible: next earnings date, guidance update, filing. Done when each item is checkable.

## Formulas

**1. Beta.** Slope of the regression of the stock's monthly total returns on the index's monthly total returns over the 60 months ending before the event. Examples in the papers: about 0.8 for Symantec (60 months to Feb 2014) and 2.2 for Harman (60 months to Jul 2013). With fewer than 60 months of history, state the shorter window (assumed).

**2. Abnormal return** on day t: AR(t) = R(stock, t) - beta x R(index, t). The market model has no intercept (Man Overboard p.8).

**3. Cumulative abnormal return:** CAR(a, b) = sum of AR(t) for trading days t from a to b. Windows: -30 to -1 before the event, the event day alone, and +1 to +30, +60 and +90 after. CAR resets to zero at the close of the event day. Worked example from Man Overboard: stock +10.3 percent over 30 trading days, index +1.2 percent, beta 0.8, so CAR = 10.3 - 0.8 x 1.2 = 9.3 percent.

## Reference tables

All figures are mean CARs in percent, measured from the close of the event day in trading days. They are historical reference-class averages, not forecasts; verify before presenting anything as current. Data source in the papers: Credit Suisse HOLT. Universe: not stated explicitly in Man Overboard; the Summit exhibit is labelled "for the S&P 500", and abnormal returns are measured against the S&P 500. Treat the sample as US large caps.

**Table 1. One-day drops of 10 percent or more against the index.** Man Overboard, Exhibits 2 and 3. Sample: January 1990 to June 2014, more than 5,400 events, about 40 percent in the dot-com and 2008-2009 periods, about one quarter earnings releases.

| Event type | Momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.6 | -14.9 | 408 | -1.5 | -1.9 | -0.6 |
| Earnings | Neutral | -2.8 | -14.7 | 434 | 0.8 | 2.4 | 4.0 |
| Earnings | Weak | -1.0 | -14.9 | 600 | 2.7 | 5.1 | 8.4 |
| Non-earnings | Strong | -4.6 | -13.8 | 1,041 | 3.7 | 4.9 | 6.2 |
| Non-earnings | Neutral | -5.9 | -14.4 | 1,067 | 4.7 | 9.4 | 11.3 |
| Non-earnings | Weak | -6.2 | -14.2 | 1,867 | 11.1 | 17.0 | 18.8 |

**Table 2. One-day gains of 10 percent or more against the index.** Summit, Exhibits 2 to 4. Sample: January 1990 to July 2015, 6,797 events excluding announced M&A, 36 percent in bubble periods, 1,505 earnings and 5,292 non-earnings. Full sample: -30d -5.9, event day 13.8, +30/+60/+90 of 3.5/6.1/7.0. Earnings 2.7/3.7/4.1; non-earnings 3.8/6.8/7.9.

| Event type | Momentum | -30d | Event day | N | +30d | +60d | +90d |
|---|---|---|---|---|---|---|---|
| Earnings | Strong | -1.3 | 13.9 | 411 | 1.1 | 1.9 | 2.3 |
| Earnings | Neutral | -1.6 | 14.1 | 429 | 2.1 | 3.9 | 4.2 |
| Earnings | Weak | -5.7 | 15.2 | 665 | 4.1 | 4.7 | 5.2 |
| Non-earnings | Strong | -7.5 | 12.7 | 1,137 | 1.2 | 1.5 | 1.7 |
| Non-earnings | Neutral | -7.5 | 13.5 | 1,383 | 2.8 | 6.2 | 7.1 |
| Non-earnings | Weak | -5.8 | 14.0 | 2,772 | 5.3 | 9.1 | 10.8 |

**Table 3. Branches with the strongest contrasts.** Drops use the 1990 to June 2014 sample, gains the 1990 to July 2015 sample. N falls with each split, so N is shown.

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

Ex-bubble subsample (dot-com and 2008-2009 removed; Man Overboard Exhibits 12 and 13): the direction matches the full sample in over 80 percent of earnings branches and close to 90 percent of non-earnings branches. Earnings drops, strong and expensive: N 129, -2.2/-3.8/-3.3. Non-earnings drops, strong, expensive, high quality: N 153, -0.1/-7.6/-8.0. Non-earnings drops, weak and cheap: N 473, 6.2/9.3/8.1.

**Table 4. Dispersion** (Man Overboard p.4, p.11; Summit p.5). Mean / median / standard deviation, percent.

| Reference class | N | +30d | +60d | +90d |
|---|---|---|---|---|
| Drops, non-earnings, weak, cheap, high quality | 282 | 10.4 / 7.6 / 34.7 | 14.9 / 10.0 / 40.4 | 23.0 / 18.2 / 46.0 |
| Drops, non-earnings, weak momentum | 1,867 | 11.1 / 7.0 / 33.7 | 17.0 / 12.2 / 40.6 | 18.8 / 13.7 / 46.5 |
| Gains, non-earnings, weak, cheap, low quality | 455 | 7.6 / 6.1 / 32.0 | 11.0 / 7.5 / 38.8 | 12.0 / 8.0 / 46.1 |

Two worked cases show the spread. Symantec (CEO fired, -12.9 percent on 21 Mar 2014, non-earnings, weak, cheap, high): reference class N 282 at +10.4/+14.9/+23.0; actual +9.3/+15.4/+24.2. Tenet Healthcare (-36.7 percent on 4 Nov 2008, earnings, strong, expensive, low): reference class N 56 at -2.9/-6.3/-1.4; actual -60.9/-54.4/-51.2.

**Table 5. Factor proxies.** The right-hand column is an adaptation for Bigdata.com data, not a method from the papers.

| Factor | Paper definition (HOLT, percentile within sector) | Bigdata.com proxy |
|---|---|---|
| Momentum | 60% change in expected CFROI after 13 weeks of EPS revisions; 30% 52-week price change; 10% liquidity | 13-week change in consensus EPS and EBIT; analyst target and rating changes; 52-week price performance relative to the sector, excluding the event |
| Valuation | 50% HOLT warranted value against price; 30% economic P/E; 10% value-to-cost ratio; 10% dividend yield | EV/EBITDA, P/E, FCF yield and price to book against sector peers; upside to a reverse-DCF or scenario value if the report has one; dividend yield |
| Quality | 50% CFROI last fiscal year; 30% (CFROI - discount rate) x gross investment; 20% change in that spread | FactSet ROIC against peers; (ROIC - assumed cost of capital) x invested capital; change in that spread over five fiscal periods; margin history |

## Interpretation rules

**1. Long-term outlook test.** The market reacts to changes in expected long-term cash flows, not to the headline. Prices respond to short-term earnings only as signals of long-term earnings potential, and the market follows cash when earnings and cash diverge ("A Long Look at Short-Termism", 2014, pp.9-10). Ask five questions:
- (a) Did consensus for FY+2 and beyond, long-term growth or guidance change, and by how much?
- (b) Do the drivers recur (price, volume, margin structure) or are they one-time?
- (c) Does cash flow agree with the earnings line?
- (d) Which revision matters for this company? Where ROIC is near the cost of capital, the return on new investment moves value and growth does not; where ROIC is high, sales growth moves value (Expectations Investing, p.66; `references/expectations.md`).
- (e) Is the information diagnostic, meaning it changes the probability of the thesis, or does it only look causal, such as an EPS dilution headline on an acquisition whose synergies exceed the premium ("Cultivating Your Judgment Skills", 2013, p.10)?

Classify the move as long-term, short-term or unclear.

**2. Decompose the move** into fundamental news, a change in the multiple, and flows such as index changes, mandate constraints or tax selling. Most day-to-day moves are supply and demand. A price is an offer, not evidence of value (Klarman, Margin of Safety, 1991, Ch.1).

**3. What the tables say.** After large drops and gains, mean CARs are positive when momentum going in was weak, and larger for non-earnings events than for earnings events. They are flat to negative when momentum was strong and valuation expensive. A higher mean does not make a gain likely: the median sits below the mean and the standard deviation is 32 to 47 points in the published cells. Means are positive in most cells after both drops and gains, which can reflect the sample or the method (no intercept, survivorship treatment not described). Use the difference between branches and the sign relative to the full-sample row, not the absolute level.

**4. Limits.** US stocks, 1990 to mid-2014 or mid-2015, a period with two bubble-and-bust episodes. The papers do not use the size of the surprise, guidance or the stated reason for the move, and present the result as a complement to fundamental analysis, not a replacement. Banks, cyclicals and early-stage companies are not separated; state the sector and widen the range.

Not in the sources: base rates for multi-day moves, moves under 10 percent, non-US stocks, the years after publication, or the size of the earnings surprise. Say so when the event falls outside the sample.

**5. Errors to avoid.**
- A narrative before the classification.
- A leaf row with N under about 50 quoted as a finding: earnings drops with weak momentum, neutral valuation and high quality show -2.5 at +30 days against +2.7 for the weak-momentum parent.
- Judging a prior call by the result.
- Reading the sign of an average as a forecast.

## Output lines

- Event: "[Ticker] [fell/rose] X percent on [date] against [index] Y percent, a relative move of Z percent (W percent beta-adjusted, beta B over N months). Classified as [earnings / non-earnings], [one day / multi-day]." (derived)
- Cause: "[Stated cause], [source, date]." (reported). If none: "No cause is established in the sources reviewed." (judgment)
- Going in: "Momentum [strong/neutral/weak]: 52-week relative performance X percent, 13-week EPS revision Y percent. Valuation [cheap/neutral/expensive]: [multiples against peers]. Quality [high/neutral/low]: ROIC R percent, [trend]. These are proxies, not HOLT scores." (derived; cost of capital assumed)
- Reference class: "From [sample period], N stocks in the [branch] showed a mean CAR of a, b and c percent at 30, 60 and 90 trading days; median m and standard deviation s where published. Parent branch: N, a, b, c. Historical average, not a forecast." (reported, historical base rate)
- Outlook test: "Consensus FY+2 [EPS/EBIT] moved from X to Y; guidance [changed/unchanged]; [one-time/recurring] items: [list]. The move is [consistent/inconsistent] with the change in long-term cash flow." (derived, judgment)
- Unknowns: "Not established: [items]. The base rates do not cover [multi-day moves, non-US stocks, surprise size]." (judgment)
- What would change the read: "[Dated, checkable item]." (judgment)
- Close with: "This note conditions the view; it does not recommend a trade."

## Sources

- Notes: Mauboussin, Man Overboard (2015) and Celebrating the Summit (2016) (Part 1 sections 1, 2, 8 and 11; Parts 3 to 5); base-rates.md (section 2.9 and Part 6); Klarman, Margin of Safety (Ch.1); Mauboussin, Expectations Investing; Robinson and Weyns, UBS multiples and DCF papers (2017) (section 1.2).
- Credit Suisse Global Financial Strategies (Mauboussin and co-authors): "Managing the Man Overboard Moment" (15 Jan 2015); "Celebrating the Summit" (11 Jan 2016); "A Long Look at Short-Termism" (18 Nov 2014); "Cultivating Your Judgment Skills" (7 May 2013); "Outcome Bias and the Interpreter" (15 Oct 2013).
- Mauboussin, "Expectations Investing", CFA Institute Conference Proceedings Quarterly, Sept 2006.
- Klarman, Margin of Safety (1991), Ch.1.

<!-- Note vs spec: the spec gives "US stocks" as the universe and an SD range of 30 to 46 points; the notes say the universe is not stated (Summit labels its exhibit "for the S&P 500"), the papers say about 35 to 45 (drops) and 30 to 45 (gains), and the published cells run 32.0 to 46.5, so this file follows the notes. -->
