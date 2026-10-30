# Spec: Downside first, why it is cheap, catalysts and the kill rule

## 1. Purpose
This method answers four questions in a fixed order: how much can be lost at this price and how permanent is that loss; why the price is what it is and who is on the other side; what event closes the gap between price and value, and by when; and which pre-stated facts or dates would end the thesis. Jobs that use it: thesis and investment memo, deep dive, quick take, catalyst work, special situations, risk. The method describes the balance of evidence and what would change it. It does not issue buy, hold or sell calls, price targets or position sizes.

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Cash, marketable securities, receivables, inventories, PPE gross and net, goodwill and intangibles, current and total liabilities, debt, leases (5 fiscal periods) | Tearsheet balance sheet | reported |
| Free cash flow, capex, depreciation, stock-based compensation | Tearsheet cash flow and income statement | reported |
| Market cap, EV, net debt, FCF yield, multiples | Tearsheet key_metrics | reported |
| Segment revenue and profit (5 years) | Tearsheet segments | reported |
| Holder base and recent changes (who sold, who bought) | Tearsheet 13F holders and fund trends | reported |
| Dated catalysts: next earnings, shareholder meeting, deal milestones | Events calendar, search over filings and news | reported |
| Buyback authorisations, spin-off or asset-sale announcements, activist stakes, covenants, pension and contingent liabilities, insider purchases | Search over filings, news, transcripts | reported |
| Past M&A, executives and insider ownership | Tearsheet M&A history and executives | reported |
| Liquidation haircuts, discount rate, probabilities | Chosen by the analyst and stated | assumed |

## 3. Procedure
1. Record the price, market cap and EV, and the growth and margin the price already assumes (see the expectations method). Done when one line says what must go right for the current price to hold. A stock priced for high growth falls sharply on a miss (Klarman, Ch.6, torpedo stocks).
2. Value the downside before the upside. Compute net-net working capital, current-asset value, tangible book per share, a liquidation value and a stressed cash-flow value (formulas 4.2 to 4.5; stressed case: capex equal to depreciation, no cash released from working capital, a conservative discount rate chosen for the cash flows). Done when the note shows each value per share, the price as a percentage of each, and the lowest and the highest of them. When methods diverge, use the lower unless the note justifies otherwise (Klarman, Ch.8).
3. Separate permanent from temporary loss. List the events that would turn a temporary price fall into permanent loss: a need to raise capital, forced selling, covenant breach, loss of market access, deflation turning hidden assets into hidden liabilities (Klarman, Ch.6 and Ch.8 on reflexivity). Done when each is marked present, absent or unknown with evidence.
4. Ask why it is cheap. Ask "what is wrong with it?" and test each candidate: broken business model, hidden liabilities, litigation, a competitor's product, management quality (Klarman, Ch.9; Security Analysis preface, p.xviii). A clearly identified, temporary reason such as an institutional constraint makes the case better because the outcome is more predictable. Done when the note lists the reason or states that none was found, which is itself a warning.
5. Identify the seller. Check each constraint: index deletion, minimum-price or mandate rules, downgrade below investment grade, spin-off selling, dividend omission, tax-loss selling, window dressing, position too small for institutions, no analyst coverage, dumping after a miss, margin calls. Compare 13F holders now and a year ago. For an expensive stock ask who is forced to buy. Done when each constraint is marked yes, no or unknown.
6. Search for disconfirming evidence by name (contingent liabilities, pension deficits, restatements, insider selling) and label every statement as fact or opinion (section 6.4). Done when the note shows at least one disconfirming item or states that the search found none.
7. List catalysts and score each (section 5.2). Done when each has type, decider, date or "open-ended", and potency.
8. State what happens if nothing happens: without a catalyst, value can erode or the gap can widen (Klarman, Ch.10). Done when the note gives the direction of the drift and the main cause.
9. Write the kill rule (section 5.3) and the sell logic (section 6.3) before any upside case. Done when every kill condition has a driver, a checkable threshold and a date.

## 4. Formulas
4.1 Margin of safety = 1 - P / V, where P is the price and V a conservative value (derived). The sources give no fixed percentage: it must be wide enough for error and bad luck, depends on the price paid, and should be wider for intangible-heavy or leveraged companies (Klarman, Ch.6). Stated practices, not rules: a 30% to 40% or larger discount to underlying value, or a FCF yield of 8% to 10% or more when the risk-free rate is 4% to 5% (Security Analysis, Klarman preface, p.xxxiii; verify rates).
4.2 Net-net working capital per share = (cash + marketable securities + receivables + inventories - current liabilities - all long-term liabilities) / shares (Graham and Dodd; Klarman, Ch.8). Valid only if working capital is not overstated and operations are not consuming cash quickly. Check pensions, off-balance-sheet and contingent liabilities, and liabilities that arise in liquidation (plant closing, environmental).
4.3 Current-asset value = current assets - all liabilities - senior claims. Cash-asset value = cash and equivalents (securities at market) - all liabilities - senior claims. Tangible book per share = (tangible assets - all liabilities - senior stock, preferred at effective par) / shares (Security Analysis, Ch.42, pp.548 to 554).
4.4 Liquidation value = 1.00 x cash + h_r x receivables + h_i x inventories + h_f x fixed and other assets - liabilities at face - liquidation costs. Graham and Dodd averages (Ch.43, p.560): h_r 0.75 to 0.90 (average 0.80), h_i 0.50 to 0.75 (average 0.667), h_f 0.01 to 0.50 (average about 0.15), retail instalment receivables 0.30 to 0.60. These are 1930s industrial and retail experience (verify), illustrative only, and not parameters for software, services or financials. Orderly liquidation approximates book; a fire sale discounts inventory steeply (Klarman, Ch.8).
4.5 Return sources (Klarman, Ch.1), used to attribute any base case: free cash flow generated, change in the multiple, narrowing of the gap between price and value.
4.6 Expected value with stated probabilities: E = sum of p_i x payoff_i, with p_i integers summing to 100, each tied to a reason and a date (assumed). Report the loss case next to the gain case (Buffett, quoted in "Thirty Years: Ten Attributes of Great Investors", 2016).
4.7 Earning power versus asset value (Greenwald, Security Analysis, pp.543 to 544): if asset value exceeds earnings value, assets are under-used and a catalyst such as a change of management is needed; if earnings power exceeds asset value, an identifiable moat is needed; if they are about equal, asset value checks the projections.

## 5. Reference tables
### 5.1 Catalyst types (Klarman, Ch.10, L5815 to 5881; Security Analysis, Ch.43, pp.564 to 567)
| Catalyst | Internal or external | Who decides | Potency |
|---|---|---|---|
| Orderly sale of the company or liquidation | Internal | Management and board | Total realisation of value |
| Breakup into parts | Internal | Management and board | Largely total |
| Spin-off, buyback, recapitalisation, large asset sale | Internal | Management and board | Partial; also signals a shareholder-oriented management |
| Accumulation toward voting control, takeover fear, proxy fight | External | Outside holders | Depends on outcome |
| Emergence from bankruptcy (creditors) | Court process | Court and creditors | Value realised in cash, new debt or more liquid equity |
| Industry improvement, change of management or policy, sale or merger at liquidation value, partial liquidation | Mixed | Varies | Cases in Security Analysis: Hamilton Woolen, White Motor, Mohawk Mining |

### 5.2 Potency scoring (derived framework, judgment; not a table in the sources)
| Test | High | Low |
|---|---|---|
| Certainty | Announced, board-approved, with a filed document | Hoped for or only rumoured |
| Timing | Dated or with a defined window | Open-ended |
| Size of the gap closed | Realises most of (V - P) | Realises a small part |
| Decider alignment | Decider gains from closing the gap (insider buying, incentives tied to share price) | Decider indifferent or conflicted |
GAP: the notes give no base rates for how often announced catalysts complete or how long gap closure takes, and no numeric weights.

### 5.3 Kill rule template
Each row is written when the thesis is written. Conditions come from Klarman, Ch.7 and Ch.13, Security Analysis, p.441, and the linchpin method in Credit Suisse, "Methods to Improve Decisions" (24 Feb 2014, pp.6 to 7). Question design follows "Sharpening Your Forecasting Skills" (28 Sep 2015, p.13): a checkable outcome, a time window, relevance to the decision.
| Condition | Driver | Threshold | Date |
|---|---|---|---|
| Value changes | Conservative value V | V falls below P, or P rises to V | Each quarterly filing |
| Management incompetent or corrupt, or accounting questionable | Restatement, related-party loans, repeated "one-time" charges | Any confirmed instance. Graham and Dodd: do not adjust and proceed, reject the company | On disclosure |
| Funding or covenant stress | Maturities, covenant headroom, access to markets | Stated ratio or date | Per filings |
| Catalyst fails | The listed catalysts | Not occurred by the stated date | A stated date |
| Better use of capital | Alternative with larger margin of safety | Stated comparison | Review date |
A price fall alone is not a kill condition: re-test the thesis on value, not price. If value is unchanged, a lower price raises the margin of safety. A stop-loss order treats the market as knowing more than the analyst (Klarman, Ch.13). Test: would the analyst buy more at the lower price? If not, the original purchase is in doubt.

## 6. Interpretation rules
6.1 Order matters. Downside value comes before upside, because risk is the probability and amount of permanent loss at the price paid, not volatility or beta (Klarman, Ch.7).
6.2 Bottom-up versus top-down. A bottom-up case needs four answers: what the business is worth, whether the value will endure, how likely the gap is to narrow, and the risk and reward at the price. A top-down case needs a correct macro call, sector implication, security choice and timing, so it has no margin of safety; macro views count only through their effect on valuation (Klarman, Ch.7).
6.3 Sell logic. State the conditions, not a call: the price reaches value, the thesis breaks (value changes, management proves incompetent or corrupt), or a better use of capital exists. There are no mechanical rules on P/E, percentage gain or targets. Stated practices to cite as practices: begin selling at a 10% to 20% discount to underlying value depending on liquidity, catalyst, management, leverage and confidence (Klarman preface, p.xxxvi); Greenberg required about a 15% implied FCF return to buy and sold when the modelled return fell to 10% (Security Analysis, p.398). Consider taxes, cash and liquidity.
6.4 Facts versus opinions. Mark facts (can be disproved) and opinions separately; when opinion outweighs fact, update (Credit Suisse, "Methods to Improve Decisions", p.7). Treat sell-side targets, issuer figures and sponsor figures as opinions: research skews to buy and issuers earn fees if the number is believed (Klarman, Ch.2).
6.5 When the floors do not apply. Software, platforms and services have little tangible value: use stressed cash flow and cash runway. Klarman's preference for tangible assets is a style choice. Banks and insurers: asset and liability values are hard to verify, so test book value and earnings quality instead. Cyclicals: use multi-year average earnings, not the latest year. Early-stage companies: GAP, the notes do not cover cash-runway methods. Emerging markets: demand a wider margin for incomplete disclosure and restricted share classes (Security Analysis, Russo essay).
6.6 Common errors: a low P/E, high dividend yield or low P/B accepted as proof of cheapness; a margin of safety quoted as one number; an upside case with no loss case; a "temporary" reason that has no evidence.

## 7. Output lines
- "Price [P] is [x]% of net-net working capital [a], [y]% of tangible book [b], [z]% of liquidation value [c] (haircuts: [list], assumed), [w]% of stressed cash-flow value [d]. Downside range [low] to [high] per share." (derived; haircuts assumed)
- "Margin of safety against the lower value: [x]%." (derived)
- "Reason for the discount: [reason, source]. Constraint-driven selling: [yes/no/unknown, evidence]. Largest holder changes over [period]: [list]." (reported; judgment on the reason)
- "Catalyst: [type], decided by [who], date [date or open-ended], potency [high/medium/low] because [certainty, timing, gap closed]." (reported, judgment)
- "If nothing happens: [erode / widen / hold], because [cause]." (judgment)
- "Kill conditions (written [date]): [driver, threshold, date] for each of [n]." (judgment, thresholds assumed)
- "Facts: [list]. Opinions: [list]. Disconfirming evidence found: [item or none]." (reported, judgment)
- "Sell logic: conditions only, no call: [price reaches value / thesis breaks / better use of capital]."

## 8. Sources
Notes: klarman.md (Ch.1, 2, 6 to 10, 13; sections 3 and 5), security-analysis.md (Klarman preface, Lowenstein, Ch.42 and 43, Ch.50, Greenwald, Greenberg, Section 5), decisions-price-moves.md (MI, FC, 30Y). Books and papers: Klarman, Margin of Safety (1991); Graham and Dodd, Security Analysis, 6th ed. (2009, text of the 1940 edition); Credit Suisse Global Financial Strategies, "Methods to Improve Decisions" (2014), "Sharpening Your Forecasting Skills" (2015), "Thirty Years: Ten Attributes of Great Investors" (2016).
