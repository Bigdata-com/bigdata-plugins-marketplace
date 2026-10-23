# Spec: Special situations arithmetic

## 1. Purpose
This method answers: in an event-driven situation (merger, spin-off, rights offering, bankruptcy, liquidation, conversion), what is the payoff in each outcome, what does the price already assume about the probability of each outcome, and what is lost if the event does not happen. Klarman groups these as situations with known exit prices and approximate time frames, and asset conversions, where the return comes from the event and not from the market (Margin of Safety, Ch.9). Jobs that use it: special situations, deal analysis, thesis, risk. The skill reports arithmetic and evidence. It does not give buy, hold or sell calls or position sizes.

## 2. Inputs
| Input | Bigdata.com source | Evidence label |
|---|---|---|
| Deal terms: consideration, mix, conditions, expected close, regulatory steps, termination fee | Search over filings and news; fetch the merger or Form 10 document | reported |
| Current price, unaffected price before the announcement | Tearsheet price fields; bigdata_computer for the price series | reported |
| Dividends and interest during the hold | Filings, tearsheet | reported |
| Spin-off: capitalisation, segment profit, management ownership and option terms, holder base | Form 10 and filings via search; tearsheet segments; 13F holders | reported |
| Capital structure by seniority, cash, assets for sale, off-balance-sheet claims (bankruptcy, liquidation) | Filings via search; tearsheet balance sheet | reported |
| Dates of votes, hearings, record dates, rights expiry | Events calendar, filings | reported |
| Bond prices for distressed layers | GAP: not in the field list for this project; verify whether the credit factor tools return them | not available |
| Break price, outcome probabilities, financing cost, resolution dates | Chosen by the analyst and stated | assumed |

## 3. Procedure
1. Classify the situation: discount to breakup or liquidation value, rate-of-return situation with a known exit price, or asset conversion such as distress, recapitalisation or exchange offer (Klarman, Ch.9). Done when the note names the type and the event that realises value.
2. List the outcomes with a payoff and a date for each, including the break case. Company-specific event risks such as regulatory approval belong in scenarios with probabilities, not in a discount rate (McKinsey, Valuation, 5th ed., the addendum on risk to chapters 1 and 2 in mckinsey-part1.md). Done when payoffs sum to a complete set of outcomes.
3. State the break price: where the stock trades if the event fails. For a deal, Klarman's downside is reversion to the previous trading level. Done when the break price comes from the unaffected price or a stated value, and the source is shown.
4. Compute the return in each outcome, the annualised return, the expected return (formula 4.1) and the completion probability the price implies (formula 4.2). Done when the note compares the implied probability with the analyst's stated probability.
5. Apply the situation checks in section 5.1 to the specific case. Done when each check is marked yes, no or unknown with evidence.
6. Test the value of any non-cash consideration conservatively (section 5.2). Done when each piece has a stated value and the floor value of the package is shown.
7. State what is not in the notes: completion base rates, typical spreads and typical timing (section 6). Done when the note names the missing statistic and does not supply one.

## 4. Formulas
4.1 Expected return = sum over outcomes i of p_i x (V_i / P - 1), where P is the price paid, V_i the value received in outcome i (including dividends and interest) and p_i the probability, with sum of p_i equal to 1. Always include the break outcome with its stated price. Annualise each outcome (derived): (V_i / P)^(365 / d_i) - 1, where d_i is days to resolution. Report annualised returns for a range of resolution dates, as Klarman does (Texaco 11.875% debentures at 90 in Nov 1987: 44.1%, 25.4% and 19.5% annualised if paid in full after one, two and three years; the notes do not give the inputs behind those figures). Show that a further price fall only improves the entry if value is unchanged.
4.2 Spread = (F - P) / P, where F is the consideration at close. Implied completion probability p* = (P - B) / (F - B), where B is the break price. If the analyst's probability exceeds p*, the price pays for more risk than the analyst sees, and the reverse. Downside to upside ratio = (P - B) / (F - P). (Derived arithmetic, not stated in the notes.)
4.3 Rights offering. Shares N at net asset value or price P; rights let holders buy n new shares at subscription price S. Post-offering value per share = (N x P + n x S) / (N + n). Klarman's example: 1,000,000 shares at 25, rights to buy another share at 15, all subscribe, value 20; if 50,000 rights are not used, value is 20.13 and non-subscribers lose almost 20%. An oversubscription privilege can pay: 50,000 shares bought at 15 and worth 20 gains 250,000.
4.4 Thrift or financial conversion. Pro forma book value per share = (pre-conversion net worth + net proceeds) / total shares after conversion. Example: net worth 10 million plus 10 million raised, 1 million shares, book value 20 per share. In an ordinary IPO with insiders buying 1 million shares at 1 and the public paying 11, book value is 6 and the public is diluted by 5 per share (Klarman, Ch.11). Buyback accretion from excess capital: book value per share after = (E - B) / (N - B / P), with E equity, B cash spent, P the buyback price, N shares. JSB Financial: buying back at two-thirds of book lifted pro forma book value from 21.12 to 25.00, up 18%.
4.5 Spin-off pair value: implied price of the retained business = parent price - value of the spun-entity shares received per parent share (derived). Klarman's Burlington Northern case bought the parent and sold the spun entity short to lock in an implied price of about 19 for the railroad (illustration only).
4.6 Distressed equity as an option: equity = max(EV_s - total claims, 0), weighted by scenario probability (McKinsey, ch.12). A fully covered unsecured claim behaves like a zero-coupon bond, so annualised return falls as the case lasts longer (Klarman, Ch.12).

## 5. Reference tables
### 5.1 Situation checks (Klarman, Ch.9 to 12; Security Analysis, Ch.43 and Merkin)
| Situation | Where the return comes from | Checks |
|---|---|---|
| Merger arbitrage | Spread between price and consideration | Break price; value of each piece of non-cash consideration; contested or friendly deal; crowding, where spread compression and fund inflows signal lower future returns; best entries come when uncertainty is high |
| Spin-off | Forced and uninformed selling by the parent's holders | Size of the position for institutions (200,000 shares worth 2.2 million against a 40 million average position in the InterTAN case); index funds selling regardless of price; no analyst coverage; management options struck on early low prices; one loss-making division hiding profits; net-net working capital and tangible book against price; insider purchases; data lag of two to three months in 1991 |
| Rights offering | Mispricing around the subscription terms | Dilution for non-subscribers; oversubscription terms; prospectus availability, since rights traded far below worth before the prospectus reached holders |
| Liquidation | Distribution of value in cash | Piece-by-piece value at highest use; fire sale against orderly; hidden assets; contingent liabilities; timing; reasons for the discount (disappointed holders, flipping, sub-minimum price, delisting) |
| Bankruptcy and distress | Reorganisation; emergence as a liquefying event | See 5.3 |
| Thrift or financial conversion | Existing capital obtained at the offer price | Positive pre-conversion business value; no exotic or distant lending, junk bonds or IO and PO securities; adjust book up for understated assets and down for intangibles and bad loans; normalise earnings for securities gains and branch sales; recurring spread against fees |

### 5.2 Valuing non-cash consideration conservatively (Klarman, Ch.10, Becor Western, Dec 1987)
Notes at near par; long debentures at 50% of face; preferred at 25% of liquidation preference; warrants at zero. Show the floor value of the package. In that case the stock traded below 10 against nearly 10 of cash per share, conservative value of the pieces was at least 14, and the outcome was about 14.25. Treat the percentages as one case from 1987 (verify), not parameters.

### 5.3 Distress: three stages (Michael Price, in Klarman, Ch.12)
| Stage | Timing | Character |
|---|---|---|
| 1. Immediately after filing | Days to weeks | Greatest uncertainty and best prices |
| 2. Plan negotiation | Months to years | More information, plan unresolved |
| 3. Final plan to emergence | 3 months to 1 year | Resembles merger arbitrage; lowest but most predictable return |
Process (Klarman, Ch.12): (1) separate assets of the ongoing business from assets available for distribution; (2) value the ongoing business by all three methods and adjust for Chapter 11 distortions (interest income on cash ends, interest on reinstated debt returns, professional costs of several percent or more end); (3) add off-balance-sheet assets and liabilities (pensions, tax and environmental claims, rejected lease and contract claims); (4) list claims by seniority, oversecured creditors receiving post-petition interest to the extent of oversecurity; (5) classify the holding as senior, fulcrum (class partly covered, most sensitive to value) or junior (option-like); common stock of bankrupt companies usually has value near zero in reorganisation; (6) note blocking positions (one third of a class). Filing effects: interest on unsecured debt stops, leases can be rejected, cash builds. Lowest-risk cases are overleveraged capital-intensive near-monopolies; highest-risk are fashion or competitive businesses and financials that depend on confidence.

### 5.4 Spin-off and divestiture evidence (McKinsey, Valuation, 5th ed., ch.22, Ex. 22.2 and 22.4, pp.471 to 486; verify)
Announcement return for spin-offs +4.5% market-adjusted (all divestitures +3.0% mean). Two-year market-adjusted return: spun entities +13.1%, parents +3.1%. Spin-offs that improve focus: median +8.6%; those that do not: -1.9%. Parent-controlled carve-outs with free float below 75%: median -32%.

## 6. Interpretation rules
6.1 Dated material. Every case in Klarman is from the 1980s to early 1991 (Becor Western, InterTAN, Texaco, City Investing, JSB) and every Security Analysis case is from the 1930s. Use them as method illustrations, not market facts. Tax rules, the 1990s Chapter 11 mechanics, and the data lags have changed.
6.2 GAP: the notes contain no base rates for deal completion, break prices, typical spreads or time to close, no recovery rates by seniority, and no current spin-off statistics beyond the McKinsey ch.22 figures. State the missing statistic; do not estimate it.
6.3 Illiquid markets reward trading skill as much as analysis (Klarman, Ch.12). Quote the price source and its date, and say when no bond price is available.
6.4 A flat expected return can hide a wide spread of outcomes. Always show the break outcome next to the success outcome, not the average only.
6.5 The method does not apply to a deal whose consideration cannot be valued from the filings, to securities the analyst cannot value (decline them, Klarman, Ch.6), or to companies with questionable accounting, which Graham and Dodd say to avoid and not adjust (Security Analysis, p.441).
6.6 Errors: using the announcement price as the break price; valuing warrants or preferred at face; ignoring time in the annualisation; treating the spread as risk-free; assuming the common stock of a bankrupt company recovers.

## 7. Output lines
- "Situation: [type]. Event: [description], expected [date], decided by [party]." (reported)
- "Price [P]; consideration at close [F] (components valued at [..], assumed); spread [x]%, annualised [y]% to [date]." (derived; component values assumed)
- "Break price [B] ([source]); downside to break [z]%; downside to upside ratio [r]." (derived)
- "Price implies a completion probability of [p*]%. Analyst probability [p]% because [reason, date]." (derived, judgment)
- "Expected return [e]% (annualised [a]%) with outcomes [list: probability, payoff, date]." (derived; probabilities assumed)
- "Spin-off checks: [constraint-driven selling yes/no; coverage; segment profit; insider buying; net-net working capital and tangible book against price]." (reported, derived)
- "Capital structure: [layer, claim, recovery in scenario A and B]; fulcrum security [name]." (reported, derived)
- "Not established: [completion base rate, spread history, recovery rates]." (judgment)

## 8. Sources
Notes: klarman.md (Ch.9 to 12, sections 3 to 6), security-analysis.md (Ch.43, Merkin, Section 4), mckinsey-part2.md (ch.22), mckinsey-part1.md (ch.12 and the risk addendum on company-specific scenarios), capital-allocation.md (divestiture and spin-off evidence). Books: Klarman, Margin of Safety (1991); Graham and Dodd, Security Analysis, 6th ed. (2009); McKinsey, Valuation, 5th ed. (2010).
