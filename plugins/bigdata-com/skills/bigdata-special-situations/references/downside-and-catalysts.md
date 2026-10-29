# Downside first, why it is cheap, catalysts and the kill rule

Four questions, in this order: how much can be lost at this price and how permanently; why the price is where it is and who is on the other side; what event closes the gap between price and value, and by when; and which facts or dates, written down in advance, end the thesis. Risk is the probability and size of permanent loss at the price paid, not volatility or beta, so the loss case comes first. The method weighs evidence; it issues no call, price target or position size.

## Inputs

| Input | Where it comes from |
|---|---|
| Balance sheet items, free cash flow, capex, depreciation, stock-based compensation, segment profit | Annual statements and segments, five fiscal years |
| Market cap, EV, net debt, FCF yield, multiples, share count | Company key metrics |
| Holders and their changes | Fund holdings history: 13F holders, top buyers and sellers, options activity. Quarterly with a filing lag: who sold over the quarter, not on a day |
| Dated catalysts; buybacks, spin-offs, asset sales, activist stakes, covenants, pension and contingent liabilities, insider purchases | Corporate calendar; filings, news and transcripts |
| M&A history, executives, insider ownership | M&A and leadership data |
| Liquidation haircuts, discount rate, probabilities | Not in the data. Choose each and give the reason |

## What the price already assumes

Record the price, EV and the growth and margin the price implies (expectations.md, implied growth). A stock priced for high growth falls hard on a miss.

## Margin of safety

Margin of safety = 1 - P / V, where P is the price and V a conservative value. No fixed percentage applies: it must cover error and bad luck, and it should be wider for intangible-heavy or leveraged companies. Practices, not rules: a discount of 30 to 40 percent or more to underlying value, or a FCF yield of 8 to 10 percent or more when the risk-free rate is 4 to 5 percent nominal.

## Floor values

Compute each that applies, per share, against the price. When they diverge, use the lower unless the note gives a reason.

- **Net-net working capital** = (cash + marketable securities + receivables + inventories - current liabilities - all long-term liabilities) / shares. Valid only if working capital is not overstated and operations are not burning cash fast; check pensions, off-balance-sheet and contingent liabilities, and liabilities a liquidation creates (plant closing, environmental). Managements can dissipate the assets, so it is a floor check, not a screen.
- **Current-asset value** = current assets - all liabilities - senior claims.
- **Cash-asset value** = cash and equivalents, securities at market, - all liabilities - senior claims.
- **Tangible book per share** = (tangible assets - all liabilities - senior stock) / shares, with preferred stock at the higher of par plus unpaid dividends and market value.
- **Liquidation value** = 1.00 x cash + h_r x receivables + h_i x inventories + h_f x fixed and other assets - liabilities at face - liquidation costs, where each h is the share of book value recovered. An orderly liquidation approximates book value; a fire sale discounts inventory steeply.
- **Stressed cash-flow value:** capex equal to depreciation, no cash released from working capital, and a discount rate as conservative as the forecasts.

## Liquidation haircuts

Share of book value recovered in US industrial and retail liquidations, 1930s. Illustrative only; not parameters for software, services or financials.

| Asset | Range | Average |
|---|---|---|
| Cash assets | 100% | 100% |
| Receivables, net of reserves | 75-90% | 80% |
| Retail instalment receivables | 30-60% | 50% |
| Inventories, at lower of cost or market | 50-75% | 66.7% |
| Fixed and other assets | 1-50% | about 15% |

## Earning power against asset value

Asset value above earnings value means under-used assets, which need a catalyst such as a change of management. Earning power above asset value needs an identifiable moat, and the assets show what remains if it erodes. When the two are about equal, asset value checks the projections. Add surplus cash after removing its interest income, so it is not counted twice.

## Permanent against temporary loss

List the events that would turn a temporary price fall into a permanent loss: a need to raise capital, forced selling, a covenant breach, loss of market access, deflation turning hidden assets into hidden liabilities. Mark each present, absent or unknown with evidence.

## Why it is cheap and who is selling

Test each candidate for what is wrong: a broken business model, hidden liabilities, litigation, a competitor's product, management. An identified, temporary reason such as an institutional constraint makes the outcome more predictable; no reason found is a warning.

Forced sellers: index deletion, minimum-price or mandate rules, a downgrade below investment grade, spin-off selling, a dividend omission, tax-loss selling, window dressing, a position too small for institutions, no analyst coverage, dumping after a miss, margin calls. Compare 13F holders now with a year ago. For an expensive stock, ask who is forced to buy.

Search by name for contingent liabilities, pension deficits, restatements, insider selling and repeated "one-time" charges.

## Facts and opinions

Mark facts (statements that can be disproved) apart from opinions; when opinion outweighs fact, update. Sell-side targets and issuer and sponsor figures are opinions: research leans to buy ratings, and issuers and underwriters earn fees when the number is believed.

## Catalysts

Attribute any base case to its three sources of return: free cash flow generated, a change in the multiple, and the gap between price and value narrowing. Then name the event that closes the gap.

| Catalyst | Internal or external | Who decides | Potency |
|---|---|---|---|
| Orderly sale of the company, or liquidation | Internal | Management and board | Realises all of the value |
| Breakup into parts | Internal | Management and board | Largely all |
| Spin-off, buyback, recapitalisation, large asset sale | Internal | Management and board | Partial; signals a shareholder-oriented management |
| Accumulation toward voting control, takeover fear, proxy fight | External | Outside holders | Depends on the outcome |
| Emergence from bankruptcy | Court process | Court and creditors | Value realised in cash, new debt or more liquid equity |
| Industry improvement, change of management or policy, sale at liquidation value, partial liquidation | Mixed | Varies | Varies |

Score each catalyst's potency on four tests:

| Test | High | Low |
|---|---|---|
| Certainty | Announced and board-approved, with a filed document | Hoped for or rumoured |
| Timing | Dated, or a defined window | Open-ended |
| Gap closed | Realises most of V - P | Realises a small part |
| Decider alignment | The decider gains from closing the gap (insider buying, pay tied to the share price) | Indifferent or conflicted |

State what happens if nothing happens: without a catalyst, value can erode or the gap can widen.

## Expected value

E = sum of p_i x payoff_i, with whole-number p_i summing to 100, each tied to a reason and a date. Report the loss case next to the gain case.

## Kill rule and sell logic

Write the kill rule with the thesis, before any upside case: each condition checkable, with a time window, and relevant to the decision.

| Condition | Driver | Threshold | Date |
|---|---|---|---|
| Value changes | Conservative value V | V falls below P, or P rises to V | Each quarterly filing |
| Management incompetent or corrupt, or accounting questionable | Restatement, related-party loans, repeated "one-time" charges | Any confirmed instance: reject, do not adjust and proceed | On disclosure |
| Funding or covenant stress | Maturities, covenant headroom, market access | A stated ratio or date | Per filings |
| Catalyst fails | The listed catalysts | Not occurred by the stated date | A stated date |
| Better use of capital | An alternative with a larger margin of safety | A stated comparison | Review date |

A price fall alone is not a kill condition. Re-test on value: if value is unchanged, a lower price raises the margin of safety, and a stop-loss treats the market as knowing more than the analyst. If the analyst would not buy more at the lower price, the original case is in doubt.

Sell on conditions: the price reaches value, the thesis breaks, or a better use of capital exists, never on a mechanical P/E, gain or target. Practices: begin selling at a 10 to 20 percent discount to underlying value, depending on liquidity, catalyst, management, leverage and confidence; or buy at about a 15 percent implied FCF return and sell when the modelled return falls to 10 percent. Weigh taxes and the alternatives.

## Bottom-up against top-down

A bottom-up case needs four answers: what the business is worth, whether the value will endure, how likely the gap is to narrow, and the risk and reward at the price. A top-down case needs a correct macro call, its sector effect, the right security and early timing, so it carries no margin of safety; macro views count only through their effect on value.

## When the floors do not apply

- Software, platforms and services have little tangible value: use the stressed cash-flow value and the cash runway. A preference for tangible assets is a style choice, not a rule.
- Banks and insurers: asset and liability values cannot be checked from outside, so test book value and earnings quality instead of liquidation value.
- Cyclicals: use multi-year average earnings, not the latest year.
- Non-US listings and emerging markets: demand a wider margin for incomplete disclosure, restricted share classes and illiquidity, and compare local accounting with peers elsewhere.
- Early-stage companies: state the burn rate, the runway in months and the funding assumption.

## Common errors

A low P/E, a high dividend yield or a low price to book taken as proof of cheapness; a margin of safety quoted as one number; an upside case with no loss case; a "temporary" reason with no evidence; a ten-item risk list that does not say which items impair value permanently.
