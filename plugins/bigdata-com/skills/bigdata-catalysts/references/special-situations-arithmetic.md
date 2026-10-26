# Special situations arithmetic

This method works out the payoff of an event-driven situation: a merger or tender, a spin-off, a rights offering, a liquidation, a bankruptcy or restructuring, a conversion. For each it asks what the holder receives in each outcome and when, what the current price already assumes about the probability of each outcome, and what is lost if the event does not happen. Klarman groups these as rate-of-return situations with known exit prices and approximate time frames, and asset conversions, where the return comes from the event rather than from the market (Margin of Safety, ch. 9). The skill reports the arithmetic and the evidence; it gives no call on the security and no position size.

## When a skill loads this file

bigdata-special-situations runs the whole method. bigdata-deal-analysis uses steps 2 to 5 and formulas 1 and 2 for the target's side of an announced deal. For a stressed capital structure, load credit.md as well for the recovery formula and the coverage tests. A narrow question ("what does the price of the target imply about the deal closing?") gets formulas 1 and 2 with the break price and its source.

## Inputs

| Input | Bigdata.com source | Basis |
|---|---|---|
| Deal terms: consideration and mix, conditions, expected close, regulatory steps, termination fee, financing | a search over filings and news; the full merger agreement, proxy, tender offer or Form 10 | reported |
| Current price and the unaffected price before rumours and the announcement | the tearsheet overview (quote and standard-window performance); the computing tool for the daily series | reported |
| Dividends and interest during the hold | `financial_statements`, `dividends`; filings | reported |
| Spin-off: capitalisation, segment profit, management ownership and option terms, holder base | Form 10 and filings via search; `revenue_segmentation`; `fund_trends_history` | reported |
| Capital structure by seniority, cash, assets for sale, off-balance-sheet claims | Filings via search; `financial_statements`, `key_metrics` | reported |
| Vote, hearing, record, expiry and regulatory dates | The proxy, merger agreement, tender documents and 8-Ks via search and the full document; the corporate calendar carries earnings, conferences, IPOs and delistings only | reported |
| Prices of distressed bonds or other layers | Not in a Bigdata.com data set (the credit-factor tool returns credit-news catalysts, not prices); quoted prices from news and research via a search when a document carries them, else state the gap | reported or not available |
| Break price, outcome probabilities, resolution dates, financing cost | Chosen and stated with the reason | assumed |

## Procedure

1. **Classify the situation.** Discount to breakup or liquidation value; rate-of-return situation with a known exit price (merger arbitrage, tender, complex security); or asset conversion (distress, bankruptcy, recapitalisation, exchange offer) (Klarman ch. 9). Done when the type, the event that realises value, the party that decides it and the expected date are named.
2. **List the outcomes.** Write every outcome with its payoff and its date, including the break case and a delayed case. Company-specific event risks such as regulatory approval go into scenarios with probabilities, not into a higher discount rate (McKinsey, Valuation, addendum to ch. 1-2: an all-or-nothing project is worth +8,000 or -2,000, never its 4,000 expected value). Done when the outcomes are exhaustive and each has a payoff, a date and a source for its terms.
3. **State the break price.** Where the stock trades if the event fails. For a deal, the downside is reversion to the previous trading level (Klarman ch. 10); adjust that level for what has happened to peers and the market since, and say how. Done when the break price comes from the unaffected price or a stated value, with its source and date.
4. **Compute the returns.** For each outcome the return and the annualised return over a range of resolution dates; the gross and annualised spread; the expected return (formula 1); and the completion probability the price implies (formula 2). Done when the implied probability sits next to the analyst's stated probability with the reason for the difference.
5. **Value non-cash consideration conservatively.** Assign a floor value to each piece (notes, debentures, preferred, warrants, contingent value rights, stock of the buyer) using table 2 as a guide and the security's own terms, and show the floor value of the package. Done when each piece has a value and a basis, and the floor is compared with the price.
6. **Run the situation checks** in table 1 for the type at hand. Done when each check is marked yes, no or unknown with evidence and a source.
7. **Why it is mispriced.** Name who is selling or unable to buy and why: index deletion, mandate limits, position too small to matter, minimum price rules, no analyst coverage, disappointed holders. A clearly identified reason such as an institutional constraint makes the outcome more predictable; an unexplained discount may hide a problem (Klarman ch. 9). Done when the reason is stated, or stated as not found.
8. **For distress, build the waterfall.** Follow the process under table 3, compute recovery per layer at two or more enterprise values (credit.md formula 9) and name the stage of the case. Done when each layer has a recovery per scenario and the fulcrum security is named.
9. **Name what is missing.** Say which statistics the sources do not provide (see "Not in the sources") and do not supply one from memory. Done when the Gaps line lists them.

## Formulas

1. Expected return = sum over outcomes i of p_i x (V_i / P - 1), with P the price paid, V_i the value received in outcome i including dividends and interest, and p_i its probability; the p_i sum to 1 and always include the break outcome. Annualised return for outcome i = (V_i / P)^(365 / d_i) - 1, with d_i the days to resolution (derived). Report it for several resolution dates, as Klarman does for Texaco 11.875% debentures bought at 90 in November 1987: 44.1%, 25.4% and 19.5% a year if paid in full after one, two or three years (ch. 6; the inputs behind these figures are not in the notes). If value is unchanged, a further price fall only improves the entry.
2. Gross spread = (F - P) / P, with F the consideration at close. Implied completion probability p* = (P - B) / (F - B), with B the break price. Downside-to-upside ratio = (P - B) / (F - P). If the analyst's probability is below p*, the price assumes more confidence than the analyst has; if above, less (derived arithmetic, not stated in the notes). Carry and the hedge (not in the sources; standard risk-arbitrage practice): the cost of holding to close = financing rate x days to close / 365, plus dividends the target pays less dividends paid on any short leg; net it from the spread before reading p*, so p* = (P + carry - B) / (F - B). For a stock-for-stock deal, F = exchange ratio x the acquirer's current price, the position is long the target and short the exchange ratio of acquirer shares, and the break loss includes the short leg. Report the annualised net spread next to the risk-free rate; a spread below it says the market sees the deal as done (Klarman annualises returns by holding period in ch. 12 and hedges the Burlington Northern spin-off pair in ch. 10).
3. Rights offering: post-offering value per share = (N x P + n x S) / (N + n), with N shares before at value or price P, and n new shares subscribed at price S. Klarman's example: 1,000,000 shares at 25 and rights to buy one more share at 15; if all subscribe, value is 20; if rights for 50,000 shares go unused, value is 20.13 and non-subscribers lose almost 20%. An oversubscription privilege can pay: 50,000 extra shares bought at 15 and worth 20 gain 250,000 (ch. 10).
4. Conversion of a mutual financial company: pro forma book value per share = (pre-conversion net worth + net proceeds) / shares after conversion. Net worth of 10 million plus 10 million raised on 1 million shares gives 20 per share: buyers get the existing capital at no cost. In an ordinary IPO where insiders bought 1 million shares at 1 and the public pays 11 for 1 million, book value is 6 and the public is diluted by 5 per share (Klarman ch. 11).
5. Buyback accretion from excess capital: book value per share after = (E - B) / (N - B / P), with E equity, B cash spent, P the buyback price and N shares before. JSB Financial (1990): buying back at two-thirds of book would lift pro forma book value from 21.12 to 25.00, up 18% (Klarman ch. 11).
6. Spin-off pair: implied value of the retained business per parent share = parent price - (spun shares per parent share x spun price) (derived). Klarman's Burlington Northern case bought the parent and sold the spun entity short to lock in about 19 a share for the railroad (ch. 10; illustration only).
7. Distressed equity: equity_s = max(EV_s - total claims, 0), probability-weighted across scenarios (McKinsey ch. 12, p. 282-290). A fully covered unsecured claim behaves like a zero-coupon bond, so its annualised return falls the longer the case lasts (Klarman ch. 12).
8. Liquidation value = sum of each asset at its recovery rate - all liabilities at face - costs of liquidation (plant closing, environmental, severance), discounted for time to distribution (derived; Security Analysis p. 560; Klarman ch. 8).

## Reference tables

**Table 1. Situation checks** (Klarman ch. 9 to 12; Security Analysis ch. 43 and Merkin p. 265-288)

| Situation | Return comes from | Checks |
|---|---|---|
| Merger arbitrage, tender | Spread between price and consideration | Break price; value of each non-cash piece; friendly or contested; financing and regulatory conditions; crowding (spread compression and fund inflows signal lower future returns); the best entries come when uncertainty is high |
| Spin-off | Indifferent or forced selling by the parent's holders | Position too small for institutions (InterTAN: 200,000 shares worth 2.2 million against a 40 million average position); index funds selling regardless of price; no analyst coverage; management options struck on early low prices; a loss-making division hiding profitable ones; net-net working capital and tangible book against price; insider purchases; screening databases that lag the listing |
| Rights offering | Mispricing around the subscription terms | Dilution for non-subscribers; oversubscription terms; whether the prospectus has reached holders (rights traded far below worth before it did) |
| Liquidation, breakup | Distribution of value in cash | Each piece at its highest use; fire sale against orderly; hidden assets; contingent liabilities; timing; why the discount exists (disappointed holders, flippers, sub-minimum price, delisting) |
| Bankruptcy, distress | Reorganisation; emergence as a liquefying event | Table 3 |
| Mutual conversion | Existing capital bought at the offer price | Positive business value before conversion; no exotic or distant lending or hard-to-value securities; book adjusted up for understated assets and down for intangibles and bad loans; earnings normalised for securities gains and branch sales |

**Table 2. Conservative values for non-cash consideration** (Klarman ch. 10, Becor Western, December 1987; one case, not parameters)

Notes near par; long debentures at 50% of face; preferred at 25% of liquidation preference; warrants at zero. The stock traded below 10 against nearly 10 of cash per share; the conservative value of the package was at least 14; holders received about 14.25.

**Table 3. Distress stages** (Michael Price, in Klarman ch. 12)

| Stage | Timing | Character |
|---|---|---|
| 1. Just after filing | Days to weeks | Greatest uncertainty, best prices |
| 2. Plan negotiation | Months to years | More information, plan unresolved |
| 3. Final plan to emergence | Three months to a year | Resembles merger arbitrage; lowest but most predictable return |

Process (Klarman ch. 12): (1) separate the ongoing business from assets available for distribution (excess cash, assets held for sale, securities); (2) value the business by going-concern, liquidation and market methods, adjusting for Chapter 11 distortions: interest income on accumulated cash ends, interest on reinstated debt returns, and professional costs of several percent or more of the estate stop; (3) add off-balance-sheet assets and liabilities (pensions, tax and environmental claims, rejected lease and contract claims); (4) list claims by seniority, with oversecured creditors receiving post-petition interest to the extent of the oversecurity; (5) classify the holding as senior, fulcrum or junior; common stock of a bankrupt company is usually worth about zero in reorganisation; (6) note blocking positions, one third of a class. On filing, interest on unsecured debt stops, leases can be rejected and cash builds. Lowest-risk cases are overleveraged, capital-intensive near-monopolies; highest-risk are fashion or competitive businesses and financial firms that depend on confidence.

**Table 4. Spin-off and divestiture evidence** (McKinsey, Valuation, 5th ed., ch. 22, ex. 22.2 and 22.4, p. 471-486; verify)

| Measure | Figure |
|---|---|
| Announcement return, market-adjusted | Spin-offs +4.5%; all divestitures +3.0% mean, +1.8% median |
| Two-year return, market-adjusted | Spun entities +13.1%; parents +3.1% |
| Spin-offs that sharpen focus / that do not | Median +8.6% / -1.9% |
| Parent-controlled carve-outs with free float below 75% | Median -32% |
| Spun-off units' margins | Up about one third in the three years after |

**Table 5. Liquidation recovery rates** (Security Analysis ch. 43, p. 560; 1930s industrial experience, illustrative only): cash 100% of book; receivables 75-90% (about 80%); inventories at lower of cost or market 50-75% (about 67%); fixed and other assets 1-50% (about 15%); liabilities at face. Not parameters for software, services or financials.

**Catalyst strength** (Klarman ch. 10): an orderly sale or liquidation realises the whole value; spin-offs, buybacks, recapitalisations and large asset sales realise part of it; emergence from bankruptcy realises value for creditors.

## Interpretation rules

- Every Klarman case dates from the 1980s to early 1991 and every Security Analysis case from the 1930s. They illustrate the method; they are not market facts. Tax rules, Chapter 11 practice and data lags have changed since.
- Show the break outcome next to the success outcome, not the expected value alone: a flat expected return can hide a wide spread of results.
- A seller's price rarely moves the full premium on announcement because of time and regulatory risk; that gap is the spread (Mauboussin, To Buy or Not To Buy, 2017).
- In illiquid markets trading skill matters as much as analysis (Klarman ch. 12). Quote the price source and its date, and say when no bond price is available.
- The method does not apply to consideration that cannot be valued from the filings, to securities the analyst cannot value (decline them; Klarman ch. 6), or to companies with questionable accounting, which Graham and Dodd say to avoid rather than adjust (Security Analysis p. 441).
- Common errors: using the announcement price as the break price; valuing warrants or preferred at face; ignoring time in the annualisation; treating the spread as risk-free; assuming the common stock of a bankrupt company recovers.

## Output lines

- "Situation: [type]. Event: [description], expected [date], decided by [party]." [reported]
- "Price [P]; consideration at close [F] (pieces valued at [..]); spread [x] percent, annualised [y] percent to [date], [z] percent if delayed to [date]." [derived; piece values assumed]
- "Break price [B] ([source, date]); downside to break [d] percent; downside-to-upside ratio [r]." [derived; B assumed]
- "The price implies a completion probability of [p*] percent; the analyst's estimate is [p] percent because [reason, dated evidence]." [derived; judgment]
- "Expected return [e] percent, annualised [a] percent, from outcomes [probability, payoff, date for each]." [derived; probabilities assumed]
- "Spin-off checks: [constraint-driven selling, coverage, segment profit, insider buying, net-net working capital and tangible book against price]." [reported, derived]
- "Capital structure: [layer, claim, recovery in scenarios A and B]; fulcrum security [name]; stage [1, 2 or 3]." [reported, derived]
- "Not established: [completion base rate, spread history, recovery rates]." [judgment]

## Not in the sources

- Not in the sources: base rates for deal completion, typical break-price falls, typical spreads or time to close; state them as unknown rather than estimate them.
- Not in the sources: recovery rates by seniority; use scenario enterprise values.
- Not in the sources: spin-off statistics more recent than McKinsey ch. 22.
- Not in the sources: prices of distressed bonds in Bigdata.com; verify what the credit-factor tools return.
- Not in the sources: the inputs behind Klarman's Texaco annualised returns.

## Sources

- Notes: Klarman, Margin of Safety (ch. 6 to 12, sections 3 to 6); Graham and Dodd, Security Analysis, 6th ed. (ch. 43, Merkin, section 4); McKinsey, Valuation, 5th ed. (ch. 21, 22); McKinsey, Valuation, 5th ed. (ch. 12 and the addendum to ch. 1-2); capital-allocation.md (sections 1.3 and 3.2).
- Klarman, Margin of Safety (1991): ch. 6, 8, 9, 10, 11, 12.
- Graham and Dodd, Security Analysis, 6th ed. (2009): Merkin introduction p. 265-288; ch. 43 p. 559-574; p. 441.
- McKinsey, Valuation, 5th ed. (2010): ch. 12 p. 282-290; ch. 22 p. 469-488; addendum to ch. 1-2.
- Mauboussin, To Buy or Not To Buy, Credit Suisse, 27 Feb 2017.

<!-- Spec and notes agree. Texaco figures are cited to Klarman ch. 6 (where the notes place them) rather than the spec's general reference; table 5, the catalyst-strength line and formula 8 were added from the same notes (Security Analysis p. 560; Klarman ch. 8 and 10). -->
