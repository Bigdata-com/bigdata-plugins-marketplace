# Downside first, why it is cheap, catalysts and the kill rule

This method answers four questions in a fixed order: how much can be lost at this price and how permanent that loss would be; why the price is where it is and who is on the other side of the trade; what event closes the gap between price and value, and by when; and which facts or dates, written down in advance, would end the thesis. It follows Klarman (Margin of Safety, 1991) and Graham and Dodd (Security Analysis, 6th ed., 2009): risk is the probability and amount of permanent loss at the price paid, not volatility or beta, so the loss case comes before the upside case (Klarman, Ch.7). The method describes the balance of evidence and what would change it. It does not issue buy, hold or sell calls, price targets or position sizes.

## When a skill loads this file

Load it for a thesis or memo, deep dive, quick take (the downside line and the next catalyst only), catalyst calendar, special situations, risk, and a stock-move note (who is selling, what the floor is, what the next dated event is). For a narrow question ("what is the floor?") give the floor values per share against the price and stop.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Cash, marketable securities, receivables, inventories, PP&E gross and net, goodwill and intangibles, current and total liabilities, debt, leases | the company tearsheet, annual balance sheets (five fiscal years) | reported |
| Free cash flow, capex, depreciation, stock-based compensation | `financial_statements` cash flow and income statement | reported |
| Market cap, EV, net debt, FCF yield, multiples, share count | `key_metrics` | reported |
| Segment revenue and profit | `revenue_segmentation` | reported |
| Holders and changes (who sold, who bought) | `fund_trends_history`: 13F holders, top buyers and sellers, position changes, options activity; quarterly and filed with a lag, so it shows who was selling over the quarter, not who sold on a given day | reported |
| Dated catalysts: next earnings, shareholder meeting, deal milestones | the corporate calendar; a search over filings and news | reported |
| Buyback authorisations, spin-offs, asset sales, activist stakes, covenants, pension and contingent liabilities, insider purchases | a search over filings, news and transcripts | reported |
| M&A history, executives, insider ownership | `mergers_acquisitions`, `c_level_leadership` | reported |
| Liquidation haircuts, discount rate, probabilities | Chosen in the report, with reasons | assumed |

## Procedure

1. **Record what the price already assumes.** Price, market cap and EV, and the growth and margin the price implies (`references/expectations.md`). A stock priced for high growth falls sharply on a miss (Klarman, Ch.6, "torpedo stocks"). Done when one line says what must go right for the current price to hold.
2. **Value the downside before the upside.** Compute net-net working capital, current-asset value, tangible book per share, a liquidation value and a stressed cash-flow value (formulas 2 to 4). For the stressed case, set capex equal to depreciation, release no cash from working capital, and use a discount rate as conservative as the forecasts (Klarman, Ch.8, the Esco example). Done when each value is shown per share, with the price as a percentage of each and the lowest and highest values. When the methods diverge, use the lower unless the note justifies otherwise (Klarman, Ch.8).
3. **Separate permanent from temporary loss.** List the events that would turn a temporary price fall into a permanent loss: a need to raise capital, forced selling, a covenant breach, loss of market access, deflation turning hidden assets into hidden liabilities (Klarman, Ch.6 and Ch.8 on reflexivity). Done when each is marked present, absent or unknown, with evidence.
4. **Ask why it is cheap.** Ask "what is wrong with it?" and test each candidate: a broken business model, hidden liabilities, litigation, a competitor's product, management quality (Klarman, Ch.9; Security Analysis, Klarman preface, p.xviii). A clearly identified, temporary reason such as an institutional constraint makes the case better, because the outcome is more predictable. Done when the note names the reason or states that none was found, which is itself a warning.
5. **Identify the seller.** Check each constraint: index deletion, minimum-price or mandate rules, a downgrade below investment grade, spin-off selling, a dividend omission, tax-loss selling, window dressing, a position too small for institutions, no analyst coverage, dumping after a miss, margin calls (Klarman, Ch.3, 6, 9 and 10). Compare 13F holders now with a year ago. For an expensive stock ask the mirror question: who is forced to buy. Done when each constraint is marked yes, no or unknown.
6. **Search for disconfirming evidence by name:** contingent liabilities, pension deficits, restatements, insider selling, repeated "one-time" charges. Label every statement as fact or opinion (rule 4). Done when the note shows at least one disconfirming item or states that the searches found none.
7. **List and score the catalysts** (tables 2 and 3). Done when each has a type, a decider, a date or "open-ended", and a potency.
8. **State what happens if nothing happens.** Without a catalyst, value can erode or the gap can widen (Klarman, Ch.10). Done when the note gives the direction and the main cause.
9. **Write the kill rule and the sell logic before any upside case** (table 4, rule 3). Done when every kill condition has a driver, a checkable threshold and a date.

## Formulas

**1. Margin of safety** = 1 - P / V, where P is the price and V a conservative value (derived). The sources give no fixed percentage. It must be wide enough for error and bad luck, it depends on the price paid, and it should be wider for intangible-heavy or leveraged companies (Klarman, Ch.6). Stated practices, to be cited as practices and not rules: a discount of 30 to 40 percent or more to underlying value, or a FCF yield of 8 to 10 percent or more when the risk-free rate is 4 to 5 percent nominal (Security Analysis, Klarman preface, p.xxxiii; 2008 conditions, verify against current rates).

**2. Net-net working capital per share** = (cash + marketable securities + receivables + inventories - current liabilities - all long-term liabilities) / shares (Graham and Dodd; Klarman, Ch.8). Valid only if working capital is not overstated and operations are not consuming cash quickly. Check pensions, off-balance-sheet and contingent liabilities, and liabilities that arise in a liquidation (plant closing, environmental). Few stocks pass this test today, and managements can dissipate the assets (Security Analysis, Klarman preface, p.xvii footnote; Greenwald, p.541); use it as a floor check, not a screen.

**3. Asset values** (Security Analysis, Ch.42, pp.548-554)
- Current-asset value = current assets - all liabilities - senior claims.
- Cash-asset value = cash and equivalents (securities at market) - all liabilities - senior claims.
- Tangible book per share = (tangible assets - all liabilities - senior stock) / shares, with preferred stock at its effective par (par plus back dividends, or market, whichever is higher), not its stated value.

**4. Liquidation value** = 1.00 x cash + h_r x receivables + h_i x inventories + h_f x fixed and other assets - liabilities at face - liquidation costs. The haircuts h are the fractions of book value recovered (table 1). Orderly liquidation approximates book value; a fire sale discounts inventory steeply (Klarman, Ch.8).

**5. Sources of return** (Klarman, Ch.1): free cash flow generated, a change in the multiple, and narrowing of the gap between price and value. Attribute any base case to these three.

**6. Expected value:** E = sum of p_i x payoff_i, with integer p_i summing to 100, each tied to a reason and a date (assumed). Report the loss case next to the gain case (Buffett, quoted in "Thirty Years: Ten Attributes of Great Investors", Credit Suisse, 2016).

**7. Earning power against asset value** (Greenwald, Security Analysis, pp.543-544). If asset value exceeds earnings value, the assets are under-used and a catalyst such as a change of management is needed. If earnings power exceeds asset value, an identifiable moat is needed to sustain it, and the assets show what remains if the moat erodes. If they are about equal, asset value is the check on the projections. Add surplus cash after removing its interest income, to avoid counting it twice.

## Reference tables

**Table 1. Liquidation haircuts** (Security Analysis, Ch.43, p.560). Share of book value recovered. These are 1930s industrial and retail experience: illustrative only (verify), and not parameters for software, services or financials.

| Asset | Range | Average |
|---|---|---|
| Cash assets | 100% | 100% |
| Receivables, net of reserves | 75-90% | 80% |
| Retail instalment receivables | 30-60% | 50% |
| Inventories, at lower of cost or market | 50-75% | 66.7% |
| Fixed and other assets | 1-50% | about 15% |

**Table 2. Catalyst types** (Klarman, Ch.10; Security Analysis, Ch.43, pp.564-567)

| Catalyst | Internal or external | Who decides | Potency |
|---|---|---|---|
| Orderly sale of the company, or liquidation | Internal | Management and board | Total realisation of value |
| Breakup into parts | Internal | Management and board | Largely total |
| Spin-off, buyback, recapitalisation, large asset sale | Internal | Management and board | Partial; also signals a shareholder-oriented management |
| Accumulation toward voting control, takeover fear, proxy fight | External | Outside holders | Depends on the outcome |
| Emergence from bankruptcy | Court process | Court and creditors | Value realised in cash, new debt or more liquid equity |
| Industry improvement; change of management or policy; sale or merger at liquidation value; partial liquidation | Mixed | Varies | Cases in Security Analysis: Hamilton Woolen (policy change), White Motor (sale), Mohawk Mining (partial liquidation) |

**Table 3. Potency scoring.** A framework built for this file from the sources above; it is judgment, not a table in the sources.

| Test | High | Low |
|---|---|---|
| Certainty | Announced and board-approved, with a filed document | Hoped for or rumoured |
| Timing | Dated, or a defined window | Open-ended |
| Gap closed | Realises most of V - P | Realises a small part |
| Decider alignment | The decider gains from closing the gap (insider buying, pay tied to the share price) | Indifferent or conflicted |

Not in the sources: base rates for how often announced catalysts complete or how long gap closure takes, and numeric weights for the four tests.

**Table 4. Kill rule template.** Written when the thesis is written. Conditions from Klarman (Ch.7 and Ch.13), Security Analysis (p.441) and linchpin analysis ("Methods to Improve Decisions", Credit Suisse, 2014, pp.6-7); question design from "Sharpening Your Forecasting Skills" (2015, p.13): a checkable outcome, a time window, relevance to the decision.

| Condition | Driver | Threshold | Date |
|---|---|---|---|
| Value changes | Conservative value V | V falls below P, or P rises to V | Each quarterly filing |
| Management incompetent or corrupt, or accounting questionable | Restatement, related-party loans, repeated "one-time" charges | Any confirmed instance. Graham and Dodd: do not adjust and proceed; reject the company | On disclosure |
| Funding or covenant stress | Maturities, covenant headroom, market access | A stated ratio or date | Per filings |
| Catalyst fails | The listed catalysts | Not occurred by the stated date | A stated date |
| Better use of capital | An alternative with a larger margin of safety | A stated comparison | Review date |

A price fall alone is not a kill condition: re-test the thesis on value, not price. If value is unchanged, a lower price raises the margin of safety. A stop-loss treats the market as knowing more than the analyst (Klarman, Ch.13). Test: would the analyst buy more at the lower price? If not, the original case is in doubt.

Not in the sources: a kill-criteria template as such; table 4 is this file's construction from the sources cited above it.

## Interpretation rules

**1. Order matters.** Downside value comes before upside, because risk is the probability and amount of permanent loss at the price paid (Klarman, Ch.7).

**2. Bottom-up against top-down.** A bottom-up case needs four answers: what the business is worth, whether the value will endure, how likely the gap is to narrow, and the risk and reward at the price. A top-down case needs a correct macro call, its sector implication, the right security and early timing, so it carries no margin of safety; macro views count only through their effect on value (Klarman, Ch.7).

**3. Sell logic.** State conditions, not a call: the price reaches value, the thesis breaks (value changes, management proves incompetent or corrupt), or a better use of capital exists (Klarman, Ch.7 and Ch.13). There are no mechanical rules on P/E, percentage gain or targets. Stated practices, cited as practices: begin selling at a 10 to 20 percent discount to underlying value depending on liquidity, catalyst, management, leverage and confidence (Security Analysis, Klarman preface, p.xxxvi); Greenberg required about a 15 percent implied FCF return to buy and sold when the modelled return fell to 10 percent (Security Analysis, p.398). Consider taxes and the alternatives.

**4. Facts against opinions.** Mark facts (can be disproved) and opinions separately; when opinion outweighs fact, update ("Methods to Improve Decisions", p.7). Treat sell-side targets, issuer figures and sponsor figures as opinions: research leans to buy ratings, and issuers and underwriters earn fees if the number is believed (Klarman, Ch.2).

**5. When the floors do not apply.**
- Software, platforms and services have little tangible value: use the stressed cash-flow value and cash runway. Klarman's preference for tangible assets is a style choice, not a rule.
- Banks and insurers: asset and liability values are hard to verify, so test book value and earnings quality instead of liquidation value.
- Cyclicals: use multi-year average earnings, not the latest year (Security Analysis, Ch.37).
- Non-US listings and emerging markets: demand a wider margin for incomplete disclosure, restricted share classes and illiquidity, and compare local accounting with peers in other countries (Security Analysis, Russo essay, pp.711-724).
- Not in the sources: a cash-runway method for early-stage companies. State the burn rate and the runway as derived, and the funding assumption as assumed.

**6. Common errors.** A low P/E, a high dividend yield or a low price to book taken as proof of cheapness; a margin of safety quoted as one number; an upside case with no loss case; a "temporary" reason with no evidence; a ten-item risk list that does not say which items impair value permanently.

## Output lines

- "Price P is x percent of net-net working capital (a per share), y percent of tangible book (b), z percent of liquidation value (c; haircuts [list], assumed) and w percent of stressed cash-flow value (d). Downside range [low] to [high] per share." (derived; haircuts and discount rate assumed)
- "Margin of safety against the lower value: m percent." (derived)
- "Reason for the discount: [reason, source]. Constraint-driven selling: [yes/no/unknown, evidence]. Largest holder changes over [period]: [list]." (reported; judgment on the reason)
- "Catalyst: [type], decided by [who], [date or open-ended], potency [high/medium/low] because [certainty, timing, gap closed, alignment]." (reported, judgment)
- "If nothing happens: value [erodes / the gap widens / holds], because [cause]." (judgment)
- "Kill conditions, written [date]: [driver, threshold, date] for each." (judgment; thresholds assumed)
- "Facts: [list]. Opinions: [list]. Disconfirming evidence found: [item or none]." (reported, judgment)
- "Sell logic, conditions only: [price reaches value / thesis breaks / better use of capital]."

## Sources

- Notes: Klarman, Margin of Safety (sections 1 to 3 and 5: Ch.1, 2, 3, 6 to 10, 13); Graham and Dodd, Security Analysis, 6th ed. (Klarman preface, Ch.42 and 43, Greenwald, Greenberg, Russo, sections 3 to 5); Mauboussin, Man Overboard (2015) and Celebrating the Summit (2016) (MI, FC, 30Y).
- Klarman, Margin of Safety: Risk-Averse Value Investing Strategies for the Thoughtful Investor (1991).
- Graham and Dodd, Security Analysis, 6th ed. (2009; text of the 1940 edition, with essays by Klarman, Greenberg, Greenwald and Russo).
- Credit Suisse Global Financial Strategies: "Methods to Improve Decisions" (24 Feb 2014); "Sharpening Your Forecasting Skills" (28 Sep 2015); "Thirty Years: Ten Attributes of Great Investors" (4 Aug 2016).

<!-- Note vs spec: the spec ties the wider-margin rule to emerging markets; the Russo essay in the note covers non-US and cross-border investing generally, so this file says "non-US listings and emerging markets". -->
