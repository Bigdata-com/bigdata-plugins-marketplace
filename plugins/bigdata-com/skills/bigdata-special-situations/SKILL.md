---
name: bigdata-special-situations
description: >-
  Event-driven arithmetic from Bigdata.com filings, news and tearsheets: merger arbitrage spreads
  with break prices, spin-offs, rights issues, restructurings, liquidations and exchange offers,
  each as a probability-weighted payoff with the dates. Use when the user asks about a spin-off,
  an arbitrage spread, a rights issue, a restructuring, a tender offer, or an event-driven trade.
  Not for the strategic merits of a deal, which bigdata-deal-analysis covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, special-situations-arithmetic, downside-and-catalysts, credit
  bigdata-sector-primer: none
---

# Special situations

This skill works out the payoff of a security whose return comes from an event rather than from the market: a pending merger or tender, a spin-off, a rights issue, an exchange offer, a restructuring or bankruptcy, a liquidation. For each it lists what the holder receives in every outcome and when, what the current price already assumes about the odds, what is lost if the event fails, and why the price is where it is. The reader is an event-driven portfolio manager who wants the arithmetic shown and the terms sourced to the documents. The note sizes to the question: "what is the spread on the X deal?" gets the spread, the break price, the implied probability and the annualised return in a table with sources, not the full note. It gives no call on the security and no position size.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-special-situations"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the situation needs it. Each situation type below has its own steps; run only the type at hand.

## Scope the request

Establish before gathering: the situation type (merger arbitrage or tender, spin-off, rights issue, exchange offer, restructuring or bankruptcy, liquidation or breakup); the security the user is asking about (the target's stock, the parent, the spun entity, a bond, a right); the parties, each resolved with `find_securities`; and the event that realises value, who decides it, and its expected date. Assume the user asks from the perspective of a buyer at today's price when they do not say.

Ask one question only if the security is ambiguous: a bankruptcy with several debt classes and no class named, or a deal with two bidders. Otherwise state the assumption in the header and proceed.

The arithmetic depends on the documents. If the governing document (merger agreement, tender offer, Form 10, rights prospectus, plan of reorganisation, liquidation plan) cannot be found in Bigdata.com, say so, run the arithmetic on the terms reported in the news, and label every term assumed.

## Gather

1. **Prices and holders.** `bigdata_company_tearsheet` for each listed party with `sections` set to `company_overview, financial_statements, financial_ratios, key_metrics, dividends, earnings_calendar`, plus `fund_trends_history` and `revenue_segmentation` for a spin-off. Then `bigdata_computer` on the daily price series from before the first rumour or announcement through today. Done when the current price, the unaffected price with its date, dividends due during the hold, the share count, the balance sheet and, for a spin-off, the holder base and the segments are in hand.
2. **The governing document.** `bigdata_search` for the document that sets the terms, then `bigdata_fetch_document` on it: the merger agreement, proxy or tender offer; the Form 10 or information statement; the rights offering prospectus; the exchange offer memorandum; the plan of reorganisation and disclosure statement; the plan of liquidation. Done when the consideration and its pieces, conditions, termination fees, the outside or expiry date, proration and election terms, subscription ratio and price, the capitalisation of each entity, and the classes of claims are quoted with sources, as far as the situation has them.
3. **The dates.** `bigdata_events_calendar` for the parties, and the document's own timetable. Done when the vote, record, ex-date, expiry, regulatory deadline, court hearing, distribution or outside date that the payoff depends on is listed with its source.
4. **What could stop or delay it.** Searches, one aspect each: regulatory progress; financing; shareholder or creditor opposition and litigation; a competing bid; for a bankruptcy, the creditors' committee, objections to the plan and blocking positions. Done when each risk is dated with a source, or marked none found.
5. **Credit and the capital structure,** for exchange offers, restructurings, bankruptcies and leveraged spin-offs. `bigdata_get_credit_factor`, after reading what the tool returns, and the debt note from the latest filing. Done when every claim is listed by seniority with its face amount, and the note says whether Bigdata.com returned prices for any debt layer.
6. **Peers, when the break price or a stub value needs them.** Tearsheets or `bigdata_portfolio_tearsheet` for the target's or the spun entity's peers, and the index over the same period. Done when the peer move since the unaffected date is computed.

## Analyse

Load `references/special-situations-arithmetic.md` before step 1. It carries the formulas, the situation checks in table 1, the conservative values for non-cash consideration in table 2, the distress stages and process in table 3, and the spin-off and liquidation evidence.

1. **Classify.** Discount to breakup or liquidation value, rate-of-return situation with a known exit price, or asset conversion (Klarman ch. 9), with the event that realises value, the party that decides it, and the expected date. Done when the header line can be written.

2. **List every outcome.** Each outcome with its payoff per share or per unit of face and its date, always including the failure case and a delayed case. Event risks such as a regulatory decision go into the outcomes with probabilities, never into a higher discount rate. Done when the outcomes are exhaustive and each has a payoff, a date and a source for its terms.

3. **Merger arbitrage and tender offers.**
   - The consideration at close (F): each non-cash piece valued conservatively from its own terms and table 2 (notes near par, long debentures at half of face, preferred at a quarter of its liquidation preference, warrants at zero, per the Becor Western case; one case, not parameters), the exchange ratio applied to the acquirer's current price, and any collar applied.
   - The break price (B): the unaffected price adjusted for what peers and the index did since, with the adjustment shown; never the announcement-day price.
   - Formula 2: the gross spread, the implied completion probability p* = (P - B) / (F - B), and the downside-to-upside ratio, with P today's price.
   - Formula 1: the annualised return to the expected close and to one or two later dates, with dividends during the hold.
   - The analyst's probability next to p*, with the dated evidence that makes it different.
   - The merger arbitrage checks in table 1: friendly or contested, financing and regulatory conditions, crowding (spread compression and inflows signal lower future returns).

   For a tender offer, state the proration and back-end terms from the offer document; the sources give no method for proration beyond the terms themselves. Done when the spread table, p*, the analyst's probability with its reason, and the annualised returns are shown.

4. **Spin-offs.** The setup: the distribution ratio, the record and distribution dates, the capitalisation of the parent and the spun entity after the split (debt allocated to each, cash, the share count), the segment profit behind each, and management's options and ownership in the spun entity. If both trade, the implied value of the retained business per parent share (formula 6). Then the forced-selling logic, from the spin-off checks in table 1 and step 5 of `references/downside-and-catalysts.md`: the spun entity's size against typical institutional positions, whether it falls outside the parent's index or mandate, analyst coverage, a weak division masking profitable ones, option strikes set on early prices, insider buying, net-net working capital and tangible book against price. Quote the McKinsey evidence in table 4 (announcement returns, two-year returns for spun entities and parents, the focus split; verify) as a base rate, not a forecast. Done when the setup table is complete and each forced-selling check is marked yes, no or unknown with evidence.

5. **Rights issues.** Formula 3: the theoretical ex-rights price, TERP = (N x P + n x S) / (N + n), with N existing shares at price P and n new shares at subscription price S, the value of the right to buy one new share as TERP - S (derived), and the dilution suffered by a holder who does not subscribe. Show the effect of oversubscription privileges and of rights left unexercised, as in Klarman's worked case in the reference file. Run the rights-offering checks in table 1, including whether the prospectus has reached holders. Done when TERP, the value of a right, the dilution for non-subscribers and the dates (record, trading period, expiry) are shown.

6. **Exchange offers.** The package offered for each old security, valued conservatively piece by piece as in step 3; the value of the old security if the offer fails and the company files, from step 7 below; the minimum participation condition; and the hold-out problem: bondholders cannot be compelled to exchange, so a holder who refuses may be paid in full if enough others accept, which is why participation is a prisoner's dilemma (Klarman ch. 12). A prepackaged bankruptcy changes the arithmetic, because approval by a majority in number and two-thirds in amount of a class binds the rest. The sources give no base rates for participation; state the outcome as judgment. Done when the offered package and the hold-out outcome are valued side by side with the failure case.

7. **Restructurings and bankruptcies.** Follow the process under table 3:
   - Split the ongoing business from assets available for distribution (excess cash, assets held for sale, securities).
   - Value the business at two or more stated enterprise values by going-concern, liquidation and market methods, adjusted for the Chapter 11 distortions the file lists.
   - Add off-balance-sheet claims: pensions, tax and environmental claims, rejected leases and contracts.
   - List claims by seniority at face value, with post-petition interest only for oversecured claims, and compute recovery per layer at each enterprise value (formula 9 in `references/credit.md`).
   - Name the fulcrum security, the stage of the case (table 3) and any blocking position of one third of a class.

   The common stock of a bankrupt company is usually worth about zero in a reorganisation; say what would have to be true for it not to be. The sources give no recovery rates by seniority, so recoveries come from the stated enterprise values, never from an average. Done when the waterfall shows each layer's recovery in each scenario, the fulcrum is named, and the time to emergence is stated with its basis.

8. **Liquidations and breakups.** Formula 8: each asset at its recovery rate, less all liabilities at face, less the costs of liquidating (closure, severance, environmental), discounted for the time to each distribution. Table 5's recovery rates are 1930s industrial experience and illustrative only; use the company's own disclosures and asset sales where they exist, and label every haircut assumed. Done when the liquidation value per share is shown with a distribution timetable and the haircuts used.

9. **Why it is mispriced, and the downside.** From `references/downside-and-catalysts.md`: who is selling or cannot buy and why (steps 4 and 5), the catalyst's potency on the four tests in table 3 (certainty, timing, gap closed, decider alignment), and what happens if nothing happens. An identified institutional reason makes the outcome more predictable; an unexplained discount may hide a problem. Done when the reason is stated or stated as not found, and the catalyst has its potency with reasons.

10. **The probability-weighted payoff.** Formula 1 in `references/special-situations-arithmetic.md`: the expected return across all outcomes, with probabilities summing to 100, each with its reason and the dated evidence behind it, labelled judgment; the annualised expected return to the expected date and to a delayed date; and the failure outcome shown next to the success outcome, not folded into the expected value alone. The sources give no base rates for deal completion, typical spreads, time to close or break-price falls; say so rather than estimate them. Done when the payoff table and the expected return are complete.

11. **Kill conditions.** From table 4 in `references/downside-and-catalysts.md`: the dated conditions that would end the situation's case (a regulatory deadline passed, a financing condition failed, a plan vote lost, the value estimate falling below the price), each with a threshold and a date. Done when each condition is checkable.

## Write

Follow `references/output-standard.md`.

```
# <Security> (<ticker>): <situation type>, <date>
Data as of: price <date>; unaffected price <date>; governing document <name, date>; newest document <date>.

## The setup
Four to eight sentences: the event, who decides it and when, what the holder receives in success
and in failure, what the price implies about the odds, the expected return with its probabilities,
and why the price is where it is. No call on the security, no position size.

## Terms and dates
| Term | Value | Basis | Source |
| Date | Event | What it decides | Source |

## Outcomes and payoffs
| Outcome | Payoff per share | Date | Return | Annualised | Probability | Basis | Source |
Including the failure case and a delayed case.

## The arithmetic for this situation
Merger arbitrage: spread, break price and its adjustment, p*, downside-to-upside ratio.
Spin-off: setup table, stub value, forced-selling checks.
Rights issue: TERP, value of a right, dilution for non-subscribers.
Exchange offer: package against hold-out against failure.
Restructuring: waterfall | Layer | Claim at face | Recovery at EV A | Recovery at EV B |, fulcrum, stage.
Liquidation: | Asset | Book | Haircut (assumed) | Recovery | Timing |, costs, value per share.

## Why it is mispriced
The seller and the reason, the catalyst's potency, what happens if nothing happens.

## Expected return
The probability-weighted return and its annualised form, the loss case beside it.

## Kill conditions
| Condition | Threshold | Date |

## What would change this view
## Gaps
Completion base rates, spread history and recovery rates are not in the sources; bond prices if
not returned; any term not found in a governing document.

## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: two to four pages for a single merger, spin-off or rights issue; up to eight for a bankruptcy with several classes. A narrow question gets the relevant table and the sources, and keeps the footer.

## Checks before sending

1. Every term traces to the governing document with its date, or is labelled assumed with the news source it came from.
2. The break price is the unaffected price adjusted for the market and peers, with the adjustment shown; it is never the announcement-day price.
3. Non-cash consideration is valued piece by piece and conservatively, never at face.
4. The implied completion probability p* sits next to the analyst's probability with the dated reason for any difference.
5. Returns are annualised to the expected date and to at least one later date.
6. Probabilities sum to 100, the failure outcome is shown beside the success outcome, and the weights are labelled judgment.
7. Recoveries come from stated enterprise values and the claims at face, with the fulcrum security named.
8. Dated historical figures (Klarman's cases, the 1930s liquidation haircuts, McKinsey's spin-off returns) carry their period and "(verify)" and are not presented as current.
9. No buy, sell, tender, subscribe or vote recommendation and no position size.
10. Every figure has a Basis label and a source number, or appears in the Gaps line.

## Hand-offs

- The user wants the strategic merits of the deal, the synergies or what the acquirer's holders get: `bigdata-deal-analysis`.
- The user wants the issuer's credit outside a restructuring: `bigdata-credit`. The equity downside of the parent more broadly: `bigdata-risk`.
- After delivering, make one offer: a monitor on the situation's filings, court dockets and regulatory news until the deciding date. Act only on a clear yes.
