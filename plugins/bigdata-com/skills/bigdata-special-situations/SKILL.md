---
name: bigdata-special-situations
description: >-
  Event-driven payoffs with dates: merger arbitrage spreads with break price, spin-offs, rights
  issues, bankruptcy recovery by layer. Use for arb spreads, a rights issue or spin-off payoff,
  Chapter 11. Not deal merits: bigdata-deal-analysis.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, special-situations-arithmetic, downside-and-catalysts, credit
  bigdata-sector-primer: none
---

# Special situations

A note that works out what the holder receives in every outcome and when, what the current price already assumes about the odds, what is lost if the event fails, and why the price is where it is, with the arithmetic shown and every term traced to the governing document. Never a call on the security, a recommendation to buy, sell, tender, subscribe or vote, or a position size. With no side given, take a buyer at today's price. Size the work to the question: "what is the spread on the X deal?" gets the spread, the break price, the implied completion probability and the annualised return in one table with sources; a bankruptcy with several classes gets the full waterfall.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-special-situations"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them and the situation is of their kind. A note that answers the question with fewer tables and fewer pieces is the better note.
- **Every outcome, with the failure and a delay.** Each outcome has a payoff per share or per unit of face, a date and a source for its terms, including a topping bid or bump where the situation allows one. The outcomes partition what can happen: each value of a deciding variable (a regulatory ruling, a vote, a plan value) falls in exactly one case, with one cut-off across the note. Event risk such as a regulatory decision goes into the outcomes with probabilities, never into a higher discount rate, because an all-or-nothing event is worth one of its outcomes, not their average (`references/special-situations-arithmetic.md`, outcomes and the break price).
- **The break price is the unaffected price moved with the market.** Take the price before the first rumour and adjust it for what the peers and the index did since, with the adjustment shown and the peer move computed over the same window (`references/special-situations-arithmetic.md`, outcomes and the break price).
- **The implied probability net of carry.** Gross spread, then carry to the expected close (financing cost and dividends on both legs), then the completion probability the price implies and the downside-to-upside ratio. For a stock-for-stock deal the consideration is the exchange ratio times the acquirer's current price with any collar applied, and the position is long the target and short the ratio, so the break loss includes the short leg (`references/special-situations-arithmetic.md`, merger arbitrage spread).
- **Probabilities start from what the price implies and move with dated evidence**: regulatory statements and timetables, vote commitments, financing, a competing bid. Never a default split. Where research gives a completion rate for comparable deals, it is stated with its population and period in the sentence. The probability-weighted return is stated and reconciles with the outcomes, and the failure outcome sits next to the success outcome rather than inside the average alone (`references/special-situations-arithmetic.md`, expected and annualised return).
- **Returns annualised to more than one date**, the expected close and one or two later dates, with dividends during the hold, next to the risk-free rate for the same horizon; a spread below it says the market treats the deal as done.
- **Non-cash consideration valued piece by piece**: at market where a warrant, CVR or note trades, otherwise at a conservative value from its own terms, with the value and its reason stated once. The conservative floor scheme is a guide, not a rule (`references/special-situations-arithmetic.md`, non-cash consideration).
- **Tender offers** take proration and back-end terms from the offer document.
- **Spin-offs through the forced-selling logic.** The terms come from the Form 10: the distribution ratio and dates, the tax status (a tax-free distribution under Section 355 or the local equivalent, the ruling relied on, the two-year restrictions), the capitalisation of each entity after the split, segment profit, and management's options and ownership in the spun entity. The question is whether holders will be forced or inclined to sell regardless of value, so the evidence that answers it reaches the page and the rest stays in the working: the spun entity's size against typical institutional positions, whether it falls outside the parent's index or mandate, analyst coverage, a weak division masking profitable ones, option strikes set on early prices, insider buying, net-net working capital and tangible book against price. If both trade and the question is what the retained business is worth, give its implied value per parent share with the share counts, distribution ratio and net debt stated once so the reader can rebuild it (`references/special-situations-arithmetic.md`, spin-offs; `references/downside-and-catalysts.md`, why it is cheap and who is selling). The historical spin-off returns appear only when the case rests on the spun entity outperforming, with their population and period in the sentence.
- **Rights issues.** When the question is what a holder should expect, the value per share after the offering, the value of a right against it, the dilution for a holder who does not subscribe, and the effect of oversubscription and unexercised rights (`references/special-situations-arithmetic.md`, rights offerings).
- **Exchange offers as a hold-out problem.** The package offered, valued piece by piece, against the old security's value if the offer fails and the company files. Holders cannot be compelled to exchange, so a refuser may be paid in full if enough others accept; a prepackaged plan binds a class at a majority in number and two-thirds in amount. With no participation history to start from, the probability is given with its reasons.
- **When the question is what a layer of a distressed capital structure recovers, the waterfall from stated enterprise values.** The claims are stated once, from the latest filing or the disclosure statement, together with the enterprise values and how each was reached, so the reader can rebuild every recovery; every recovery uses them. Separate the ongoing business from assets available for distribution; value it at two or more stated enterprise values; add off-balance-sheet claims; list claims at face from those ranking ahead of every pre-petition layer (DIP financing, administrative, priority tax and employee claims) down through secured, unsecured and subordinated, with post-petition interest only for oversecured claims; note any uptier or drop-down that moved collateral, since it changes who is fulcrum. Then say what each layer recovers at each value and which layer is the fulcrum, in sentences; the stage of the case, any blocking third of a class and the time to emergence with what it rests on belong where they change a recovery or its timing (`references/credit.md`, recovery by layer, comparing the layers; `references/special-situations-arithmetic.md`, bankruptcy and distress). The process is US Chapter 11; another regime is named with its class-voting and cram-down rules from the documents.
- **Liquidations** value each asset at its recovery rate less all liabilities at face and the costs of closing, discounted for the time to each distribution, from the company's own disclosures and asset sales where they exist (`references/special-situations-arithmetic.md`, liquidation).
- **Why it is mispriced.** Who is selling or cannot buy and why, because an identified institutional reason makes the outcome more predictable and an unexplained discount may hide a problem. Judge the catalyst in a sentence or two by how certain and how soon it is, how much of the gap it would close and whether the person who decides it gains from it, and say what happens if nothing happens; never as a scored list (`references/special-situations-arithmetic.md`, why it is mispriced; `references/downside-and-catalysts.md`, catalysts).
- **Kill conditions dated and checkable**: the date by which the event must happen, the ruling or vote that ends it, the price of the acquirer below which a collar breaks (`references/downside-and-catalysts.md`, kill rule and sell logic).

## Where it goes wrong

- **The announcement-day price as the break price**, which understates the downside because the stock had already moved.
- **Warrants or preferred valued at face**, which overstates the consideration.
- **Time left out of the annualisation**, or a single resolution date, which hides how fast the return falls when the close slips.
- **The spread treated as risk-free**, when it is the price of the failure outcome.
- **The common stock of a bankrupt company taken to recover.** It is usually worth about zero in a reorganisation; say what would have to be true for it not to be.
- **Recoveries taken from average rates by seniority** instead of from the stated enterprise values and the claims at face.
- **Historical figures quoted as current.** The liquidation recovery rates come from 1930s US industrial companies, and tax rules and Chapter 11 practice have changed since the spin-off and bankruptcy figures were measured.
- **Terms from news written as document terms.** When the governing document cannot be found, run the arithmetic on the terms in the news and say once that the document was not found.

## What the data has, and does not

The governing document (merger agreement, proxy, tender offer, Form 10 or information statement, rights prospectus, exchange memorandum, plan of reorganisation and disclosure statement, plan of liquidation) comes from search and is read in full, with the 8-Ks and releases that update its timetable. The corporate calendar carries earnings dates, conferences, IPOs and delistings only, so votes, record and ex-dates, expiries, regulatory deadlines, court hearings and distributions come from the documents and news. The overview has standard price windows only; the unaffected price, the peer move and any event window need the daily series. Five fiscal years of annual statements, and the dividends due during the hold, come from the statements and filings. Quarterly holder changes are 13F filings with a lag. There is no structured field for bond and loan prices, short interest, borrow cost, option prices, deal completion rates, typical spreads or time to close; news and research often carry them, so search before stating a gap, and the note says which layers have no quote. The credit tools give news-catalyst scores, not prices or spreads. The risk-free rate for the annualised comparison comes from the country data.

## Write

`references/output-standard.md` holds the rules. The title carries the setup in one line ("The spread prices a 70 percent chance the regulator clears the deal by June"), not the event's name. The opening gives the event, who decides it and when, what the holder receives in success and in failure, what the price implies about the odds and the expected return. The body follows the question and carries only the arithmetic for the situation at hand, with terms and dates traced to the governing document. The note closes on the dated kill conditions and the next dates to watch. Sub-headings state the finding, never the step.

## Before sending

- The break price is the unaffected price adjusted for the market and peers with the adjustment shown, and no non-cash piece is valued at face.
- Probabilities sum to 100, start from the implied probability with the dated evidence for any difference, and the probability-weighted return reconciles with the outcomes; returns are annualised to the expected and a later date, net of carry, next to the risk-free rate.
- Every number in the opening agrees with the figure it came from, and every recovery uses the claims and enterprise values stated once.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every code name, contract term or class designation is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
