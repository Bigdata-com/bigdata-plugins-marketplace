---
name: bigdata-deal-analysis
description: Analysis of an announced or rumoured merger, acquisition or divestiture from Bigdata.com filings, news, research and tearsheets: strategic logic, price against value, synergies against base rates, value at risk for the acquirer, financing, the regulatory path, and what each side's shareholders get. Use when the user asks about a takeover, a merger, an acquisition, a bid, or whether a deal makes sense. Not for merger arbitrage arithmetic, which bigdata-special-situations covers.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, capital-allocation, valuation, multiples-and-peers, special-situations-arithmetic, credit
  bigdata-sector-primer: auto
---

# Deal analysis

This skill writes the note a portfolio manager reads when a deal lands on a name they own or follow: what was agreed and when it closes, why the buyer wants the target and how often deals of that kind work, what the price is against what the target is worth on its own, whether the synergies cover the premium once they are discounted the way history says they should be, how much of the acquirer's value is at stake, what the balance sheet looks like afterwards, what the regulators must approve, and what each side's shareholders end up with. The merits come first; the arbitrage spread, the implied completion probability and the annualised return belong to `bigdata-special-situations`. The note sizes to the question: "what premium is X paying?" gets the terms table and the premium line. It gives no call on either stock.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Do not answer from memory or the web instead: an unsourced answer looks like Bigdata.com data and is not.
- Pass `plugin_slug: "bigdata-deal-analysis"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the deal needs it. A bolt-on worth 2 percent of the buyer's value needs the terms and the synergy test, not a regulatory study.

## Scope the request

Establish before gathering: the parties, each resolved with `find_securities` (whether each is public or private comes from the lookup); the deal's status (rumoured, announced, agreed, contested, pending approval); its type (acquisition for cash, for stock or mixed, merger of equals, divestiture, carve-out); and the side the user cares about, if any. Assume the user wants both sides when they do not say.

For a rumoured deal the terms are reports, not facts: say so in the header, use the reported terms as assumed, and run the analysis as "if the deal is struck at these terms". For a private target there is no market price: the premium is replaced by the price against the target's reported financials and against listed peers, and the note says so. For a divestiture the seller's question is different: whether the buyer pays more than the unit is worth to the seller (step 3 below covers it).

Ask one question only if the deal cannot be identified (two live bids, or a name that matches several transactions). Otherwise state the assumptions and proceed.

## Gather

1. **Both tearsheets.** `bigdata_company_tearsheet` for the acquirer and the target with `sections` set to `company_overview, price_performance, analyst_data, events_calendar`, then `fundamentals, estimates`, then `mergers_acquisitions` for the acquirer. Done when market caps, enterprise values, net debt, five periods of statements, consensus to the furthest year, and the acquirer's deal history are in hand for each listed party.
2. **The deal documents.** `bigdata_search` for the announcement release and the investor presentation, then for the merger agreement (an 8-K exhibit or equivalent), the proxy or registration statement, the tender offer documents, and for a divestiture the sale agreement or Form 10. `bigdata_fetch_document` on each one found. Done when the price per share, the consideration mix and exchange ratio (with any collar), the total equity and enterprise value, the financing, the conditions, the termination fees each way, the outside date, the expected close, the synergy claim with its cost and revenue split, phasing and integration cost, and the background-of-the-merger section (other bidders, the process) are quoted with sources. Fairness opinions in the proxy carry the bankers' valuation ranges; record them as opinions.
3. **The unaffected price.** `bigdata_search` for the first report of talks or a leak, then `bigdata_computer` on the daily series for both stocks and the index from 60 trading days before that date through today. Done when the unaffected price and its date are fixed, and the one-, three- and five-day abnormal returns for both parties after the announcement are computed with the working shown.
4. **The regulatory path.** Two or three searches, one aspect each: antitrust filings and reviews in each jurisdiction named in the agreement (waiting periods, second requests, phase two opening, remedies offered); national security, foreign investment or sector regulators; political or public statements against the deal. Done when each approval has its agency, its stage and a date or an expected window, or the note says the filings have not been located.
5. **Financing and the credit view.** Search for commitment letters, bond or loan issuance tied to the deal, equity issuance, and rating agency comments since the announcement. Done when the sources of funds are listed with amounts and the rating actions are dated, or marked none found.
6. **Reaction and opposition.** Searches for sell-side and press reaction on each side, shareholder or activist opposition, a competing bid, and litigation. Done when each is listed with its date and source, or marked none found.
7. **Peers and precedent deals for the target.** `bigdata_screen_companies` on the target's industry and size, then `bigdata_portfolio_tearsheet` or tearsheets with `fundamentals, estimates` for four to eight peers; one search for the multiples paid in comparable transactions. Done when the peer table in the comps method can be filled and precedent multiples, if found, are listed with their dates.
8. **Sector primer.** Read the target's section in `references/sector-primers.md` for the sector's value drivers and its regulatory history.

## Analyse

1. **Terms and timeline.** The terms table from step 2 of Gather, the premium against the unaffected price (formula 8 in `references/capital-allocation.md`; use the price before rumours, not the day before announcement, when the stock ran up), and the deal multiples: offer EV over the target's last-twelve-month and forward EBITA and EBITDA, and offer P/E. Then the dated timeline from signing to the outside date. Done when the reader can see what is paid, in what form, at what premium, and when each step is due.

2. **Strategic logic.** From step 7 and the interpretation rules of `references/capital-allocation.md`: which of McKinsey's five archetypes the deal fits (improve the target, remove excess capacity, accelerate market access, buy skills or technology faster than building, pick winners early), or that it fits none, which makes value creation unlikely; the strategic category and its success rate from table 1 (Clark and Mills, in Mauboussin 2017; verify); the predictors of acquirer success (a strong operator, a low premium, a sole bidder) and whether each holds here; and the deal base rates in table 2 with their periods. Do not treat EPS accretion, relative P/E or relatedness as evidence for the deal; the sources find they do not predict success. Done when the logic is stated in the company's own words with a source and then placed in its category with the base rate.

3. **Price against value for the target.** From `references/valuation.md`: the target's stand-alone value as a range, from a DCF with three scenarios and probabilities when the deal is large enough to warrant it, or from the bankers' ranges in the proxy labelled as opinions when it is not. Cross-check with `references/multiples-and-peers.md`: the offer multiple against the peer median built on the same EV and metric definitions, and against the target's own undisturbed multiple; treat precedent-deal multiples as a check only, since exit multiples taken from deals are circular. Then the McKinsey identity: value created for the acquirer = (stand-alone value + value of improvements) - (market value + premium), and return on price paid = (target NOPAT + improvements) / price paid against the cost of capital (formula 11 in `references/capital-allocation.md`). For a divestiture, compare the price received with the unit's value to the seller, and list stranded costs, lost tax shield, tax on the gain and transitional service agreements; EPS dilution from the sale is irrelevant to value. Done when the price sits against a value range and the return on price paid is stated, each labelled with its basis.

4. **Synergies against the base rates.** From formula 9 and table 2 in `references/capital-allocation.md`: split management's synergy claim into cost and revenue, tax-effect each, capitalise at a stated cost of capital, discount for the phasing, and subtract the disclosed integration cost. Show two cases: management's figures, and a case that haircuts revenue synergies far more than cost synergies, using the realisation record (86 percent of 90 deals captured at least 70 percent of planned cost savings; almost half captured under 70 percent of revenue synergies and nearly a quarter under 30 percent; McKinsey ex. 21.8; verify) to set the haircut, labelled assumed. Size cost synergies against the combined cost base by function where disclosed, and note that integration cost often equals a year or more of savings and that savings not captured in the first full budget year may never be. Done when the present value of synergies in both cases sits next to the premium paid.

5. **Value at risk and the deal NPV.** From formulas 9 and 10 in `references/capital-allocation.md`: deal NPV = PV of synergies - premium, in both synergy cases; SVAR (premium over the buyer's market cap for cash, over the combined value plus the premium for stock); premium at risk for the target's holders in a stock deal; the acquirer move the NPV predicts against the actual one-, three- and five-day abnormal returns from step 3 of Gather, read with the payment-form evidence in table 2. The SVAR sample (126 US deals, 2015 to 2016, average 5.5 percent, median 3.2 percent; verify) says whether this deal is large for its buyer. Done when NPV, SVAR, premium at risk and the predicted against actual move are tabled.

6. **Financing and leverage after the deal.** From `references/credit.md`, run steps 3 to 6 on the pro forma balance sheet: combined debt including the acquisition debt, combined EBITDA with and without synergies, net debt over EBITDA, EBIT over interest, placement against the rating medians in table 1 (2011 to 2013 medians; verify), a stress test of the combined EBIT, and the maturity ladder of the acquisition debt. If either party is stressed, add step 9, the recovery view. Show EPS accretion or dilution only to say it is not a test of value, and set it next to return on price paid. Done when the pro forma leverage, coverage and implied rating bucket are shown with the rating agencies' stated actions.

7. **The regulatory path.** For each approval: the agency, the legal test it applies, the overlap or concern that matters (shares in overlapping products, vertical foreclosure, national security), the stage and the date, and the remedies offered or likely. The sources give no base rates for deal completion or for remedies; state the probability of clearance as judgment with the evidence behind it, and note the termination fees that fall due if the deal fails on regulation. Done when each approval has a stage, a date or window, and a judgment with its evidence.

8. **What each side's shareholders get.** Target holders: the premium against the unaffected price, the form of the consideration, the conservative value of any non-cash piece (step 5 of `references/special-situations-arithmetic.md`), their share of the synergies in a stock deal, and the alternative if the deal fails, the break price from step 3 of the same file, with its source and date. Acquirer holders: the NPV per share in both synergy cases, SVAR, the ownership dilution in a stock deal, the leverage they now carry, and the history of the market's first reaction persisting (Sirower and Sahni, 302 deals, in Mauboussin, A Long Look at Short-Termism, 2014: 34 percent first reactions positive, about half of those still positive a year later; 66 percent negative, two-thirds of those still negative; verify). Done when each side has its paragraph with the two or three numbers that decide it. The spread, the implied completion probability and the annualised return are for `bigdata-special-situations`; name it and stop there.

9. **Range for the acquirer.** From the cases above, three outcomes for the acquirer's value per share: the deal closes and management's synergies arrive, the deal closes with the haircut synergies, and the deal fails (with the termination fee if one is payable). Weight them from the category success rate in step 2 and the regulatory judgment in step 7, probabilities summing to 100, labelled judgment. Done when the three outcomes, their probabilities and the expected change in value per share are shown.

## Write

Follow `references/output-standard.md`.

```
# <Acquirer> (<ticker>) / <Target> (<ticker>): <deal type>, announced <date>
Data as of: prices <date>; unaffected price <date>; estimates <date>; newest document <date>.

## The deal in brief
Four to eight sentences: the terms and premium, the strategic logic and its base rate, price
against the target's value, synergies against the premium in both cases, SVAR, leverage after
the deal, the regulatory path, and what each side gets. No call on either stock.

## Terms and timeline
| Term | Value | Basis | Source |  (price, mix, exchange ratio, collar, equity and enterprise value,
premium vs unaffected, offer multiples, fees each way, conditions, outside date, expected close)
| Date | Step | Status | Source |

## Strategic logic
Archetype, category and success rate with label, predictors of success, management's rationale quoted.

## Price against value
Stand-alone value range and method; offer multiple vs peer median and undisturbed multiple;
value-created identity; return on price paid vs cost of capital.

## Synergies
| Synergy | Gross | Phasing | After tax | PV (management) | PV (haircut) | Basis | Source |
Integration cost; realisation base rates with labels.

## Value at risk and NPV
| Measure | Management case | Haircut case | Basis |  (PV synergies, premium, NPV, SVAR,
premium at risk, predicted vs actual acquirer move)

## Financing and leverage after the deal
| Measure | Acquirer today | Pro forma | Rating median (period) | Basis | Source |

## Regulatory path
| Approval | Agency | Test | Stage | Date or window | Judgment | Source |

## What each side's shareholders get
Target holders; acquirer holders. The arbitrage arithmetic is referred to bigdata-special-situations.

## Range for the acquirer
| Outcome | What must be true | Probability | Change in value per share | Basis |

## What would change this view
## Gaps
## Sources, then the Powered by Bigdata.com line and the disclaimer.
```

Length: four to eight pages for a material deal; two pages for a bolt-on where SVAR is small. A narrow question gets its step with the table and the sources, and keeps the footer.

## Checks before sending

1. The premium is measured against the unaffected price before rumours, with that date and its source.
2. Every term comes from a deal document or a dated report; rumoured terms are labelled assumed throughout.
3. Synergies are split into cost and revenue, tax-effected, phased, net of integration cost, and shown in both a management case and a haircut case.
4. SVAR uses the right denominator for the payment form, and the deal NPV is shown next to the premium.
5. Every base rate (category success rates, synergy realisation, SVAR sample, first-reaction persistence) carries its sample, period and "(verify)".
6. EPS accretion appears only next to return on price paid, never as evidence of value.
7. Pro forma leverage is placed against rating medians labelled with their period.
8. No spread, implied completion probability or annualised arbitrage return; those are referred to `bigdata-special-situations`.
9. No buy, sell, tender or vote recommendation; fairness opinions and broker views are labelled as opinions.
10. Every figure has a Basis label and a source number, or appears in the Gaps line.

## Hand-offs

- The user wants the spread, the break price, the implied completion probability or the return to closing: `bigdata-special-situations`.
- The user wants the acquirer's record on past deals, buybacks and capital discipline: `bigdata-capital-allocation`.
- The user wants a full valuation of the target or the acquirer: `bigdata-valuation`. The combined company's debt in depth: `bigdata-credit`.
- After delivering, make one offer: a monitor on the deal's regulatory filings, votes and competing bids until the expected close. Act only on a clear yes.
