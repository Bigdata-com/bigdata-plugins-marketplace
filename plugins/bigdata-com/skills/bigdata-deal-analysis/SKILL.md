---
name: bigdata-deal-analysis
description: >-
  Merger or acquisition analysis: strategic logic, price vs value, synergies vs base rates, value
  at risk, what each side gets. Use for takeovers, bids, deal rationale, a hypothetical deal. Not
  arb maths: bigdata-special-situations.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, capital-allocation, valuation, multiples-and-peers, special-situations-arithmetic, credit, roic, expectations, industry-structure
  bigdata-sector-primer: auto
---

# Deal analysis

This skill writes the note a portfolio manager, or a corporate strategy or finance team, needs when a deal touches a company they own, follow, compete with or want to buy: the terms and timing, why the buyer wants the target and how often such deals work, price against stand-alone value, whether discounted synergies cover the premium, the acquirer's value at stake, the balance sheet afterwards, the regulatory path, and what each side's shareholders get. The arbitrage spread, the implied completion probability and the annualised return belong to `bigdata-special-situations`. The note sizes to the question: "what premium is X paying?" gets the terms table and the premium line. It gives no call on either stock.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-deal-analysis"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the deal needs it. A bolt-on worth 2 percent of the buyer's value needs the terms and the synergy test, not a regulatory study.

## Scope the request

Establish before gathering: the parties, each resolved with `find_securities` (public or private comes from the lookup); the status (rumoured, announced, agreed, contested, pending approval, hypothetical); the type (cash, stock or mixed acquisition, merger of equals, divestiture, carve-out); and the side the user cares about. Assume both sides when they do not say.

Three framings change the note:

- **A hypothetical deal** ("what would it cost us to buy X"): the user's company is the acquirer and there are no terms. Price the target at its undisturbed price plus a range of assumed premiums (set from the premium rows of table 2 in `references/capital-allocation.md`, quoted as historical), assume the financing mix, and add the section "What it would cost".
- **A third-party reading** ("what does X buying Y mean for us" from a rival, customer or supplier): run the terms, logic, synergy and regulatory steps, then add "What it means for <company>": combined share and pricing power in the overlap, the integration window when customers and staff move, likely remedies and divested assets, and concentration as a customer or supplier.
- **A corporate choice** ("cash or stock", "at what premium"): lay the arithmetic for each option side by side, as `references/output-standard.md` allows, with no call.

For a rumoured deal the terms are reports: say so in the header and label them assumed. For a private target the premium is replaced by the price against its reported financials and listed peers. For a divestiture the question is whether the buyer pays more than the unit is worth to the seller (step 3 of Analyse).

Ask one question only if the deal cannot be identified (two live bids, or a name that matches several transactions). Otherwise state the assumptions and proceed.

## Gather

1. **Both tearsheets.** `bigdata_company_tearsheet` for the acquirer and the target in three calls each: `company_overview, key_metrics`; then `financial_statements, financial_ratios` with `interval` annual; then `analyst_estimates`. For the acquirer add `mergers_acquisitions`; it needs FactSet access, so when it comes back empty, search for the acquirer's deals over the five years instead. Done when market cap, EV, net debt, five fiscal years of statements, consensus with its vintage and the acquirer's deal history are in hand for each listed party, or the missing item is named.
2. **The deal documents.** `bigdata_search` for the announcement release, the investor presentation, the merger agreement, the proxy or registration statement, the tender offer documents, and for a divestiture the sale agreement or Form 10; `bigdata_fetch_document` on each one found. Done when these are quoted with sources: price per share; consideration mix and exchange ratio (with any collar); equity and enterprise value; tax structure (stock or asset purchase, tax-free reorganisation or taxable, any step-up in the target's asset basis); financing; conditions; termination fees each way; outside date and expected close; the synergy claim with its cost and revenue split, phasing and integration cost; and the background of the merger (other bidders, the process). Record the bankers' ranges in fairness opinions as opinions.
3. **The unaffected price.** `bigdata_search` for the first report of talks or a leak, then `bigdata_computer` on the daily series for both stocks and the index from 60 trading days before it to today. Done when the unaffected price and date are fixed and both parties' one-, three- and five-day abnormal returns after the announcement are computed with the working shown.
4. **The regulatory path.** Searches, one aspect each: antitrust reviews in each jurisdiction named in the agreement (waiting periods, second requests, phase two, remedies offered); market shares of the parties and their main rivals in each overlapping product and geography; national security, foreign investment or sector regulators; political opposition. Done when each approval has its agency, stage and date or window, and each overlap has shares with a source and date, or the note says they were not located.
5. **Financing and reaction.** Searches, one aspect each: commitment letters, debt or equity issuance tied to the deal, rating agency comments; sell-side and press reaction on each side, shareholder or activist opposition, a competing bid, litigation. Done when the sources of funds have amounts and each item has its date and source, or is marked none found.
6. **Peers and precedent deals.** `bigdata_screen_companies` on the target's industry and size, then `bigdata_portfolio_tearsheet` for current multiples and `financial_statements, financial_ratios` (`interval` annual) for four to eight peers; then searches for the multiples paid in comparable transactions. Done when the peer table in `references/multiples-and-peers.md` can be filled and each precedent deal has its date, multiple and source, or is marked none found.
7. **Sector primer.** Find the target's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read "How the sector makes money", "Profit pool and competitive dynamics" and "Valuation conventions and pitfalls". Done when the sector's value drivers and the valuation conventions that apply to the target are noted.

## Analyse

1. **Terms and timeline.** The terms from Gather, the premium against the unaffected price (formula 8 in `references/capital-allocation.md`; the price before rumours when the stock ran up), and offer EV over the target's trailing and forward EBITA and EBITDA, and offer P/E. Then the dated timeline from signing to the outside date. Done when the reader can see what is paid, in what form, with what tax structure, at what premium, and when each step is due.

2. **Strategic logic.** From step 7 of `references/capital-allocation.md` and its acquisitions rule, state four things:
   - Which of McKinsey's five archetypes the deal fits (5th edition, listed in the acquisitions rule of that file; the 7th edition adds a sixth, exploiting a business's industry-specific scalability), or that it fits none, which makes value creation unlikely. A consolidation that relies on changing competitors' pricing works only when the industry is down to three or four players and entry is blocked (McKinsey ch. 21).
   - The strategic category and its success rate from table 1 of that file.
   - Whether each predictor of acquirer success in that rule holds here.
   - The deal base rates in table 2, each with its sample and period.

   EPS accretion, relative P/E and relatedness do not predict success; do not use them as evidence. Done when the logic is stated in the company's own words with a source and then placed in its category with the base rate.

3. **Price against value for the target.** From `references/valuation.md`: the target's stand-alone value as a range, from a DCF with three scenarios when the deal is large enough to warrant it, or from the bankers' ranges labelled as opinions when it is not. Cross-check with `references/multiples-and-peers.md`: the offer multiple against the peer median on the same EV and metric definitions, the target's undisturbed multiple, and the precedent deals from Gather. Precedent deals are a primary cross-check, because they show what buyers paid for control; date each one. The circularity warning in `references/valuation.md` applies to exit multiples inside a DCF, not here. Take the target's ROIC with and without goodwill from `references/roic.md`, and the growth the undisturbed price implied from formula 2 in `references/expectations.md` (three-year rolling ROIIC), so improvements are measured against what holders already priced. Then value created for the acquirer = (stand-alone value + value of improvements) - (market value + premium) (McKinsey), and return on price paid against the cost of capital (formula 11 in `references/capital-allocation.md`; cost of capital per the inputs table of `references/expectations.md`). For a divestiture, compare the price with the unit's value to the seller, net of stranded costs, lost tax shield, tax on the gain and transitional services. Done when the price sits against a value range and the return on price paid is stated, each labelled with its basis.

4. **Synergies against the base rates.** Apply formula 9 of `references/capital-allocation.md` to management's claim, split into cost and revenue and net of the disclosed integration cost. Show two cases:
   - Management's figures, as disclosed, labelled reported.
   - A haircut case that cuts revenue synergies far more than cost synergies, set from the synergy rows of table 2 and labelled assumed. Revenue synergies are often negative at first, as customers and sales staff leave and prices are conceded (McKinsey ch. 21).

   Size cost synergies against the combined cost base where disclosed, and apply the integration-cost row of table 2. For a hypothetical deal, compute the run-rate pre-tax synergies that cover the premium: premium x cost of capital / (1 - tax rate) (derived from formula 9, before phasing). Done when the present value of synergies in both cases sits next to the premium.

5. **Value at risk and the deal NPV.** From formulas 9 and 10 in `references/capital-allocation.md`: deal NPV in both synergy cases, SVAR with the denominator for the payment form, and premium at risk in a stock deal. The predicted acquirer move for cash is formula 9. For stock or mixed consideration the price paid moves with the acquirer's stock, so predicted acquirer price = (acquirer market cap + target unaffected market cap + PV synergies - cash paid) / (acquirer shares + shares issued), and target holders receive the shares issued times that price plus the cash (derived; formula 9 covers cash only). Set the prediction against the actual abnormal returns from Gather, read with the payment-form row of table 2, and compare SVAR with the SVAR sample there. Done when NPV, SVAR, premium at risk and the predicted against actual move are tabled.

6. **Financing and leverage after the deal.** Run steps 3 to 6 of `references/credit.md` on the pro forma balance sheet, combined EBITDA with and without synergies: FFO over debt and debt over EBITDA on table 3 (agency cash-flow and leverage ranges) first, table 1 as the cross-check, table 2 for the order of magnitude of default risk; the EBIT stress of formula 6 and the refinancing stress of formula 6a on the acquisition debt. If either party is stressed, add step 9, the recovery view. Show EPS accretion only next to return on price paid, to say it is not a test of value. Done when pro forma leverage, coverage and the implied rating bucket are shown with the agencies' stated actions.

7. **The regulatory path.** For each overlap, compute the combined share and the HHI after the deal (formula in `references/industry-structure.md`); the change from merging two firms is 2 x share A x share B x 10,000, shares as fractions. Quote the 2023 US Merger Guidelines presumptions as thresholds, not outcomes: post-merger HHI above 1,800 with a change above 100, or a combined share above 30 percent with a change above 100; other jurisdictions apply their own tests. Say which firms the shares cover, since listed-company shares miss private rivals. For each approval: agency, legal test, the concern that matters (horizontal overlap, vertical foreclosure, national security), stage, date, and remedies offered or likely. The sources give no base rates for completion or remedies, so the probability of clearance is judgment with its evidence; note the fees due if the deal fails on regulation. Done when each overlap has a combined share and HHI change with its coverage, and each approval has a stage, a date or window, and a judgment with its evidence.

8. **What each side's shareholders get.**
   - Target holders: the premium, the consideration and its tax treatment, the conservative value of any non-cash piece (step 5 of `references/special-situations-arithmetic.md`), their share of the synergies in a stock deal, and the alternative if the deal fails: the break price, set by step 3 of the same file (B in its formula 2), with its source and date.
   - Acquirer holders: the NPV per share in both synergy cases, SVAR, the ownership dilution in a stock deal, the leverage they now carry, and how often a first reaction persists (Sirower and Sahni, 302 deals, in Mauboussin, A Long Look at Short-Termism, 2014: 34 percent of first reactions positive, about half still positive a year later; 66 percent negative, two-thirds still negative; historical).

   Done when each side has its paragraph with the two or three numbers that decide it. The spread, the implied completion probability and the annualised return are for `bigdata-special-situations`; name it and stop there.

9. **Range for the acquirer.** Keep two probabilities apart, because different evidence drives them: completion, from the regulatory judgment, the vote, the financing and the chance of a topping bid; and realisation of the synergies if it closes, from the category success rate and the synergy rows of table 2. Three outcomes for the acquirer's value per share: closes with management's synergies (completion x realisation), closes with the haircut synergies (completion x (1 - realisation)), fails (1 - completion, with any termination fee). Weights sum to 100, labelled judgment. Done when both input probabilities, the three outcomes, their weights and the expected change in value per share are shown.

## Write

Follow `references/output-standard.md`.

```
# <Acquirer> (<ticker>) / <Target> (<ticker>): <deal type>, announced <date>
Data as of: prices <date>; unaffected price <date>; estimates <date>; newest document <date>.

## The deal in brief
Four to eight sentences on terms, logic, price against value, synergies, SVAR, leverage,
regulation and what each side gets. No call on either stock.

## Terms and timeline
| Term | Value | Basis | Source |  (the terms listed in Gather step 2, premium, offer multiples)
| Date | Step | Status | Source |

## Strategic logic
## Price against value

## Synergies
| Synergy | Gross | Phasing | After tax | PV (management) | PV (haircut) | Basis | Source |

## Value at risk and NPV
| Measure | Management case | Haircut case | Basis |

## Financing and leverage after the deal
| Measure | Acquirer today | Pro forma | Agency range or rating median (period) | Basis | Source |

## Regulatory path
| Overlap | Share A | Share B | Combined | HHI after | HHI change | Basis |  (sources in a note)
| Approval | Agency | Test | Stage | Date or window | Judgment | Source |

## What each side's shareholders get
Target holders; acquirer holders. The arbitrage arithmetic is referred to bigdata-special-situations.

## What it would cost                      (hypothetical deal only)
| Premium (assumed) | Price per share | Equity value | EV / EBITDA | Synergies needed | SVAR | Pro forma debt / EBITDA | Basis |

## What it means for <company>            (third-party reading only)
Overlap, pricing power, integration window, remedies, concentration; each with its evidence.

## Range for the acquirer
| Outcome | What must be true | Probability | Change in value per share | Basis |

## What would change this reading
## Gaps
## Sources
Numbered sources, then the Data line, then the footer verbatim from references/output-standard.md.
```

Length: four to eight pages for a material deal; two for a bolt-on with a small SVAR. A narrow question gets its step, the table and the sources, and keeps the footer.

## Checks before sending

1. The premium is measured against the unaffected price before rumours, with that date and its source.
2. Rumoured terms and every input of a hypothetical deal are labelled assumed throughout.
3. Synergies appear in a management case and a haircut case; a stock deal's predicted acquirer move uses the shares issued.
4. Every base rate carries its sample and period and is called historical, not current; the HHI thresholds are labelled as guideline presumptions with the share coverage stated.
5. EPS accretion appears only next to return on price paid, never as evidence of value.
6. The completion probability and the synergy-realisation probability are stated separately before they are combined.
7. No spread, implied completion probability or annualised arbitrage return; no buy, sell, tender, vote or bid recommendation; fairness opinions and broker views are labelled as opinions.
8. Every figure has a Basis label and a source number, or appears in the Gaps line.

## Hand-offs

- The user wants the spread, the implied completion probability, the annualised return to closing or the trade around the break price: `bigdata-special-situations`. This note computes the break price itself.
- The acquirer's record on past deals and capital discipline: `bigdata-capital-allocation`.
- A full valuation of either party: `bigdata-valuation`. The combined company's debt in depth: `bigdata-credit`.
- The industry structure behind the overlap in depth: `bigdata-sector`.
- After delivering, make one offer: a monitor on the deal's regulatory filings, votes and competing bids until the expected close. Act only on a clear yes.
