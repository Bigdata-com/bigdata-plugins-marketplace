---
name: bigdata-risk
description: >-
  Downside analysis of a company: which value drivers could break and what each costs, balance
  sheet under stress, risks ranked, kill criteria. Use for what could go wrong, downside, risks to
  a holding or target. Not debt: bigdata-credit.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, downside-and-catalysts, expectations, valuation, credit, earnings-quality, forecasting-discipline
  bigdata-sector-primer: auto
---

# Risk

A note on how much could be lost, how likely each loss is, and the dated conditions that would end the case, for someone who will act on it. Never a buy, hold or sell call, a stop-loss or a position size. The reader's side decides which loss counts: a holder's loss is the shares falling; a short seller's is the shares rising, and the premortem then runs on the bullish outcome; a supplier, customer or lender asks whether the company keeps operating, paying and refinancing, which the balance-sheet stress answers before any per-share measure. With no side given, measure loss on the shares over twelve months and say so. Size the work to the question: "what is the floor under Intel?" gets the floor values per share against the price; "can the balance sheet take a downturn?" gets the stress and the maturities, not the ranked risk list.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-risk"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **Risk is permanent loss, not volatility or beta.** So the downside comes before anything that reads as upside. One line on what the price assumes, the growth and margin the enterprise value implies against consensus, lets the reader see what must go right (`references/expectations.md`, implied growth). The inputs behind the enterprise value appear once, from the latest filing: share count, cash, debt, leases, stakes outside the operating business and the net debt they give, so the reader can rebuild every per-share figure on the page; every later figure uses them. The cost of capital is one stated figure, with the yield, beta and premium in a single clause and no regression statistics; the 10-year yield comes from the country data (`references/valuation.md`, cost of capital).
- **When the question is which assumption the price hangs on, break one driver at a time.** Take the three to five drivers the price depends on (the user's thesis, or sales growth, margin, capital intensity, the balance sheet, the duration of excess returns); for each, the event that would break it, its evidence, and the value per share with only that driver moved to its broken level (growth at the bottom of its history, margin at the last cycle's trough) and the rest at consensus, at the three-year rolling ROIIC and on rebuilt earnings where the accounting work finds flags. Moving one driver alone is what shows which one carries the price (`references/expectations.md`, implied growth and which revision moves value).
- **When the question is how far it could fall, value the floors that fit the business and set the price against them.** The lower floor governs, and the distance between floors is part of the answer, because one margin-of-safety figure hides it. The candidates are net cash, net-net working capital, current-asset value, tangible book, a liquidation value, private-market value from dated comparable deals (calling out multiples paid on cheap debt or inflated stock) and the stressed cash-flow value for the whole company. Liquidation recoveries are historical and illustrative, not parameters. Software, platforms and services use the stressed cash-flow value and the cash runway; banks and insurers use book value, earnings quality and capital ratios; cyclicals use mid-cycle earnings (`references/downside-and-catalysts.md`, floor values, liquidation haircuts, margin of safety, and when the floors do not apply).
- **Permanent against temporary, as a sentence with its evidence.** For each event that would turn a price fall into a permanent loss (a need to raise capital, forced selling, a covenant breach, loss of market access), say in plain words whether the evidence shows it, rules it out or leaves it open, and give the evidence; never a label or a bolded category (`references/downside-and-catalysts.md`, permanent against temporary loss).
- **When the question reaches survival or the company's ability to pay, test the balance sheet on the agency ranges first.** FFO over adjusted debt and debt over EBITDA on the agency's published ranges, the rating medians as the cross-check, and say when they disagree. Use an EBIT shock at least as large as the worst year in the window or the sector's volatility, because a smaller one passes a balance sheet the record says can fail, and the refinancing stress on debt due within 24 months, alone and combined with the shock. For a holding company, name which legal entity owes each debt (`references/credit.md`, the claim and its obligor, coverage and leverage ratios, placing the company on the rating scales, coverage stress and refinancing stress, and liquidity and the maturity wall).
- **Accounting risk by severity, when the accounts raise a question.** The accrual ratio over the four years that five annual periods allow, recurring one-offs, reserve releases and the equity residual, with the severity described by what it does to the figures; where several flags point the same way or there is evidence of misstatement, name the figures not to rely on and use the rebuilt earnings for the broken-driver values (`references/earnings-quality.md`, accrual ratio and cash conversion, recurring one-offs, provisions, earnings-to-equity reconciliation, and severity).
- **When the question is what could go wrong, rank the risks by expected loss.** Each risk gets an integer probability over a stated window, starting from a reference class or the company's own record where one exists, a size per share from the broken-driver or floor work, whether the loss would be permanent, and the early signal that would show it first; the ranking states the probability-times-size sum it rests on, so the reader sees which two or three dominate. Written as sentences; a table only when more than four risks need comparing (`references/forecasting-discipline.md`, granular probabilities and expected value).
- **A premortem on the outcome this reader fears, when they hold or are about to take the position:** at least three reasons, each tied to a driver or a kill criterion. A reason reaches the page only where it changes the reading; otherwise it stays in the working (`references/forecasting-discipline.md`, premortem).
- **Kill criteria as driver, threshold and date,** because a price fall alone is not one; the case is re-tested on value (`references/downside-and-catalysts.md`, kill rule and sell logic).
- **Why it is cheap and who is selling,** when the stock has fallen, with the latest quarterly holder changes as the evidence and no reason found treated as a warning (`references/downside-and-catalysts.md`, why it is cheap and who is selling).
- **The disconfirming case searched by name:** bear research, short-seller reports, filings that contradict management, or the bull case for a short seller. Management claims, broker views and targets are opinions (`references/downside-and-catalysts.md`, facts and opinions).

## Where it goes wrong

- **A low P/E, a high dividend yield or a low price to book taken as proof of cheapness,** when each can mean the market expects earnings to fade.
- **The stressed cash-flow value used per driver.** It is the whole-company floor with every driver stressed at once; per-driver breaks change one driver only.
- **A margin of safety quoted as one number,** which hides how far apart the floors are.
- **A shock smaller than the worst year in the window,** which passes a balance sheet the record says can fail.
- **A long risk list that does not say which items impair value permanently,** or a "temporary" reason with no evidence.
- **Altman Z and Piotroski read against zones.** Quote them as the data set computes them, with no cut-offs.
- **Credit-news scores cited as spreads or ratios,** which they are not.
- **A risk-free rate taken from memory** when the country data has the yield.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, nothing older; segment and geographic revenue; consensus as a snapshot with its date and no revision history; the Altman Z and Piotroski fields as the data set computes them. The annual filing read in full gives the risk factors and what changed from the prior year, the debt note (maturities, covenants, facilities, fixed and floating split, hedges), pensions, leases, contingent liabilities, guarantees, deconsolidated entities, related parties and the auditor's report; events since come from later filings and releases. Institutional holder changes are quarterly 13F filings with a lag, so they show who sold over a quarter, not on a day. The credit tools give news-catalyst scores with direction, not bond prices, yields, spreads or ratios. Bond yields, short interest and option prices have no structured field; news and research often carry them, so search before stating a gap. The corporate calendar carries earnings dates, conferences, IPOs and delistings only, so maturities, covenant test dates, court and regulatory dates and votes come from filings and news. The risk-free rate is in the country data. Listing status comes from the entity lookup; a private company has no price to measure loss against, so it gets the floors and the balance-sheet stress only. Sector accounting traps and valuation conventions are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Intel's floor is tangible book at $18; the balance sheet, not the fabs, sets it"). The opening gives what the price assumes, the downside range and the floors against the price, whether the balance sheet survives the stress, the two or three risks that dominate expected loss, and the earliest dated signal, in plain sentences the reader can act on. The body follows the question, downside before anything that reads as upside. The kill criteria with their dates close the note. Sub-headings state the finding, never the step that produced it.

## Before sending

- Every number in the opening agrees with the figure it came from, and the net debt or enterprise value used anywhere matches the inputs stated once.
- Where drivers are broken, each is valued alone; the stressed cash-flow value appears once as the whole-company floor; every floor is per share with the price set against it.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Where risks are ranked, each has a probability with its window, a size per share and an early signal, and every kill criterion has a driver, a threshold and a date.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
