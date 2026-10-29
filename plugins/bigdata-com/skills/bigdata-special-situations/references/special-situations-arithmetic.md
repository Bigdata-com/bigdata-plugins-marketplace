# Special situations arithmetic

The payoff of an event-driven situation (merger or tender, spin-off, rights offering, liquidation, bankruptcy, conversion): what the holder receives in each outcome and when, what the price assumes about the odds, and what is lost if the event fails. The return comes from the event, not from the market. Report the arithmetic and the evidence; give no call and no position size.

## Inputs

| Input | Where it comes from |
|---|---|
| Deal terms: consideration and mix, conditions, expected close, regulatory steps, termination fee, financing | Filings and news, then the merger agreement, proxy, tender offer or Form 10 |
| Current price and the unaffected price before rumours and the announcement | Company overview; the computing tool for the daily series |
| Dividends and interest during the hold | Company statements and filings |
| Spin-off capitalisation, segment profit, management ownership and option terms, holder base | Form 10 and filings; revenue segments; fund holdings |
| Capital structure by seniority, cash, assets for sale, off-balance-sheet claims | Filings; company statements and key metrics |
| Vote, hearing, record, expiry and regulatory dates | Proxy, merger agreement, tender documents and current reports, not the corporate calendar |
| Prices of distressed bonds or other layers | Not in the data. Quoted prices from news and research; otherwise state the gap |
| Break price, outcome probabilities, resolution dates, financing cost | Not in the data. State each once, with the reason |

## Kinds of situation

- **Discount to breakup or liquidation value**: value distributed in cash or in parts.
- **Rate of return with a known exit price**: merger arbitrage, tenders, complex securities. The risk is that the event fails or slips.
- **Asset conversion**: distress, bankruptcy, recapitalisation, exchange offers.

An orderly sale or liquidation realises the whole value; spin-offs, buybacks, recapitalisations and large asset sales realise part of it; emergence from bankruptcy realises value for creditors.

## Outcomes and the break price

Write every outcome with its payoff and date, including the break case and a delayed case. Event risks such as regulatory approval go into scenarios with probabilities, not into a higher discount rate: an all-or-nothing project ends at +8,000 or -2,000, never at its expected 4,000.

The break price is where the stock trades if the event fails. For a deal it is the unaffected price, adjusted for what peers and the market have done since; say how. Using the announcement price as the break price is the commonest error.

## Expected and annualised return

- Expected return = sum over outcomes i of p_i x (V_i / P - 1), with P the price paid, V_i the value received in outcome i including dividends and interest, and p_i its probability. The p_i sum to 1 and always include the break.
- Annualised return for outcome i = (V_i / P)^(365 / d_i) - 1, with d_i the days to resolution. Report it for several resolution dates.
- Show the break outcome beside the success outcome; a flat expected return can hide a wide spread.
- If value is unchanged, a further price fall only improves the entry.

## Merger arbitrage spread

- Gross spread = (F - P) / P, with F the consideration at close.
- Implied completion probability p* = (P - B) / (F - B), with B the break price. If your probability is below p*, the price assumes more confidence than you have; above it, less.
- Downside-to-upside ratio = (P - B) / (F - P).
- Carry: the cost of holding to close = financing rate x days to close / 365, plus dividends the target pays, less dividends owed on any short leg. Net it from the spread before reading p*: p* = (P + carry - B) / (F - B).
- Stock-for-stock: F = exchange ratio x the acquirer's current price. The position is long the target and short the exchange ratio of acquirer shares, and the break loss includes the short leg.
- Compare the annualised net spread with the risk-free rate over the same period. A spread below it says the market treats the deal as done.
- A target rarely moves the full premium on announcement because of time and regulatory risk; that gap is the spread, and it is not risk-free.
- Check: friendly or contested; financing and regulatory conditions; crowding, since spread compression and fund inflows signal lower returns. The best entries come when uncertainty is high.

## Non-cash consideration

Give each piece (notes, debentures, preferred, warrants, contingent value rights, acquirer stock) a floor value from its own terms and show the package's floor. One conservative scheme: notes near par, long debentures at 50 percent of face, preferred at 25 percent of liquidation preference, warrants at zero. Valuing warrants or preferred at face is a common error.

## Spin-offs

Implied value of the retained business per parent share = parent price - (spun shares per parent share x spun price). Buying one side and shorting the other locks in that implied price.

The return comes from indifferent or forced selling by the parent's holders. Check: a position too small for institutions; index funds selling regardless of price; no analyst coverage; management options struck on early low prices; a loss-making division hiding profitable ones; net-net working capital and tangible book against price; insider purchases; screening databases that lag the listing.

**Spin-off and divestiture returns** (published studies of spin-offs and divestitures before 2010)

| Measure | Figure |
|---|---|
| Announcement return, market-adjusted | Spin-offs +4.5 percent; all divestitures +3.0 mean, +1.8 median |
| Two-year return, market-adjusted | Spun entities +13.1 percent; parents +3.1 |
| Spin-offs that sharpen focus / that do not | Median +8.6 / -1.9 percent |
| Parent-controlled carve-outs with free float below 75 percent | Median -32 percent |
| Spun-off units' margins | Up about one third in the three years after |

## Rights offerings

Value per share after the offering = (N x P + n x S) / (N + n), with N shares before at price P and n new shares subscribed at S. Non-subscribers are diluted; an oversubscription privilege can pay; rights can trade far below their worth until the prospectus reaches holders.

## Conversions and buybacks from excess capital

- Mutual conversion: pro forma book value per share = (pre-conversion net worth + net proceeds) / shares after conversion. Buyers get the existing capital at no cost. Check for positive business value before conversion and no exotic or distant lending or hard-to-value securities; adjust book up for understated assets and down for intangibles and bad loans; normalise earnings for securities gains and branch sales.
- Buyback from excess capital: book value per share after = (E - B) / (N - B / P), with E equity, B cash spent, P the buyback price and N shares before.

## Liquidation

Liquidation value = sum of each asset at its recovery rate - all liabilities at face - costs of liquidation (plant closing, environmental, severance), discounted for the time to distribution. Take each piece at its highest use, orderly rather than fire sale, and look for hidden assets and contingent liabilities.

**Liquidation recovery rates** (US industrial companies, 1930s; illustrative, not parameters for software, services or financials): cash 100 percent of book; receivables 75 to 90 (about 80); inventories at lower of cost or market 50 to 75 (about 67); fixed and other assets 1 to 50 (about 15); liabilities at face.

## Bankruptcy and distress

Distressed equity in scenario s = max(EV_s - total claims, 0), weighted across scenarios; recovery per layer at two or more enterprise values follows credit.md, recovery by layer. A fully covered unsecured claim behaves like a zero-coupon bond, so its annualised return falls the longer the case lasts.

The waterfall:

- Separate the ongoing business from assets available for distribution (excess cash, assets held for sale, securities).
- Value the business by going-concern, liquidation and market methods, adjusting for what ends at emergence: interest income on accumulated cash ends, interest on reinstated debt returns, and professional costs of several percent of the estate stop.
- Add off-balance-sheet assets and liabilities: pensions, tax and environmental claims, rejected lease and contract claims.
- List claims by seniority. Oversecured creditors receive post-petition interest to the extent of the oversecurity.
- Classify the holding as senior, fulcrum or junior. The common stock of a bankrupt company is usually worth about zero in a reorganisation.
- Note blocking positions: one third of a class.

On filing, unsecured interest stops, leases can be rejected and cash builds. The lowest-risk cases are overleveraged, capital-intensive near-monopolies; the highest-risk are fashion or competitive businesses and financial firms that depend on confidence.

**Stages of a bankruptcy case**

| Stage | Timing | Character |
|---|---|---|
| Just after filing | Days to weeks | Greatest uncertainty, best prices |
| Plan negotiation | Months to years | More information, plan unresolved |
| Final plan to emergence | Three months to a year | Resembles merger arbitrage; lowest but most predictable return |

## Why it is mispriced

Name who is selling or unable to buy and why: index deletion, mandate limits, a position too small to matter, minimum price rules, no coverage, disappointed holders. A clear institutional reason makes the outcome more predictable; an unexplained discount may hide a problem.

## Limits

- Tax rules, bankruptcy practice and data lags have changed since the historical figures here were measured.
- For deal completion rates, break-price falls, typical spreads or time to close, search documents; otherwise state them as unknown rather than estimate.
- Quote each price with its source and date, and say when no bond price is available.
- The arithmetic does not apply to consideration that cannot be valued from the filings, to securities you cannot value (decline them), or to companies with questionable accounting (avoid rather than adjust).
