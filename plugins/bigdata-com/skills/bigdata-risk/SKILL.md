---
name: bigdata-risk
description: >-
  Downside analysis of a company: which value drivers could break and what each costs, balance
  sheet under stress, risks ranked, kill criteria. Use for what could go wrong, downside, risks to
  a holding or target. Not debt: bigdata-credit.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, downside-and-catalysts, forecasting-discipline, earnings-quality, credit, expectations
  bigdata-sector-primer: auto
---

# Risk

This skill answers "what could go wrong and how much could be lost" the way Klarman and Graham and Dodd define risk: the probability and amount of permanent loss at today's price, not volatility or beta. So it works downside first: what breaks each value driver and what the company is worth then, what the floors are, whether the balance sheet survives stress, which risks matter most by probability and size, how the reading fails in a premortem, and the dated conditions that would end it. It never gives a buy, hold or sell call, a stop-loss or a position size. A narrow question ("what is the floor under Intel?") gets the floor values per share against the price and stops.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-risk"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Establish the reader and the side they stand on, because it decides which loss counts. A holder's downside is the shares falling; a short seller's is the shares rising, and the premortem then runs on the bullish outcome; a lender reads the balance-sheet stress first; a supplier, customer or acquirer reads whether the company keeps operating, paying and investing. Write the implications for that reader. When the user does not say, measure loss on the shares over twelve months and state that choice. If the user has a thesis, take its drivers; otherwise name the three to five drivers the price depends on (sales growth, margin, capital intensity, the balance sheet, the duration of excess returns).

Ask one question only if the answer changes the work: the user says "my thesis" without stating it and the drivers cannot be inferred, or the name is ambiguous. Otherwise proceed. Done when the company, the reader's side, the horizon and the drivers are stated.

Narrow questions map to steps in the Analyse section:
- "What is the floor?" or "how much could be lost?": steps 1 to 3.
- "Can the balance sheet take a downturn?": step 4, with the maturity table.
- "What are the biggest risks?": step 6, with the ranked table and early signals, drawing on steps 2 to 5 only as far as the ranking needs.
- "What would end the thesis?": steps 8 and 9, stated as conditions, never as a call.

If the company is Private, say there is no price to measure loss against and give the floors and the balance-sheet stress only. For a bank or an insurer, test book value and earnings quality in place of liquidation value and use capital ratios in place of net debt (`references/downside-and-catalysts.md` rule 5 and `references/credit.md`, interpretation rules).

## Gather

1. **The company's numbers.** Profile and quote, consensus estimates with their vintage, and revenue by segment and geography; five fiscal years of annual statements, ratios and key metrics; the institutional holders with their latest changes. Done when the price, market cap, EV, net debt, share count, five annual periods of statements and the balance sheet line by line, segment revenue, consensus with its vintage, the FactSet Altman Z and Piotroski fields, and the latest quarterly 13F position changes (filed with a lag, so they show who sold over a quarter, not on a given day) are in hand.
2. **The annual filing.** Search and fetch the latest annual report and read the risk factors (and what changed from the prior year's), the debt note (maturities, covenants, facilities, fixed and floating split, hedges), pensions, leases, contingent liabilities and guarantees, deconsolidated entities, related parties, and the auditor's report. Done when each is noted with its section, or marked not disclosed.
3. **Material events since the annual filing.** Search the company's filings and releases since then (8-K or local equivalent: guidance changes, financing, management changes, litigation, rating actions). Done when each event is listed with its date.
4. **Credit-news signals.** The credit-news signals for the company: the strongest positive and negative credit-news catalysts (event type, score, direction), with no bond prices, yields, spreads or ratios. Done when the catalysts are recorded with their dates, or the coverage gap is named.
5. **Risks by category.** One search each, recent window: regulatory and legal (investigations, litigation, antitrust, policy changes); competitive (share loss, price cuts, entrants, customer losses); operational (supply chain, key people, technology and cyber, execution); macro exposure (cycle, rates, currency, commodities, geopolitics); management and governance (departures, related parties, insider selling, activists). Done when each category has dated evidence or the searches found none.
6. **The disconfirming case.** Searches for bear-case research, short-seller reports, and filings that contradict management's statements. When the reader is short, search for the bull case instead. Done when the strongest opposing argument is quoted with its source, or the searches found none.
7. **Private-market comparables.** Searches for recent acquisitions of comparable businesses and the multiples paid. Done when two or more transactions have a multiple, a date, the buyer, and how the deal was financed, or the comparables are named as not available.
8. **Dated events for the kill criteria.** The corporate calendar for the next earnings dates and conferences over the horizon; then searches of filings and news for debt maturities, covenant test dates, court and regulatory dates and shareholder votes, which the calendar does not carry. Done when every driver has at least one dated checkpoint, or the gap is named.
9. **Management's account.** Search and fetch the last earnings call. Done when management's statements on the drivers, the balance sheet and the risks analysts pressed on are quoted.
10. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read the accounting-traps, valuation-conventions and macro subsections. Done when the sector's traps and conventions are noted, or their absence is stated.

## Analyse

Load `references/downside-and-catalysts.md` before step 1, `references/credit.md` before step 4, `references/earnings-quality.md` before step 5 and `references/forecasting-discipline.md` before step 6. Where a step names a method step, run it there; the line keeps what this skill adds and the done condition.

1. **What the price already assumes** (downside method step 1). Place the forward P/E against one over an assumed cost of equity (`references/expectations.md` formula 1, with the cost of capital from its inputs table), and note consensus growth and margin for the next two years. Done when one line says what must go right for the current price to hold. The full implied-growth arithmetic belongs to `bigdata-valuation`.

2. **What breaks each driver, and by how much.** For each driver: the event that breaks it, with the evidence that it could happen, and the driver's value if broken (revenue growth at the bottom of the reference class, margin back to the trough of the last cycle, a higher capital intensity). Value each break alone: hold the other drivers at consensus, change only the broken one, and recompute EV with the value-driver formula (`references/expectations.md` formula 2 run forward: EV = NOPAT1 x (1 - g / ROIIC) / (WACC - g), at the three-year rolling ROIIC and the step 1 cost of capital), then take net debt and other claims off and divide by the share count. Use rebuilt earnings where step 5 finds flags. Done when every driver has a break event, a value per share with only that driver changed, and the loss from today's price, each labelled.

3. **The floors** (downside method step 2, formulas 1 to 4 and 7, table 1 haircuts quoted as 1930s industrial and retail experience, illustrative only). The stressed cash-flow value from method step 2 is the floor for the whole company, with every driver at its stressed level at once; it is not the per-driver method of step 2 above. Add private-market value from the Gather step 7 multiples (Klarman, Margin of Safety, ch. 8) as one input, not the arbiter, and flag multiples paid with cheap debt or inflated stock. Apply the method's rule 5 for software, platforms, services and cyclicals. Done when each floor is shown per share with the price as a percentage of it, the downside range is stated low to high, and the margin of safety against the lower value is computed.

4. **The balance sheet and liquidity under stress** (credit method steps 2 to 8). Place the company on table 3 of `references/credit.md` first (FFO / debt and debt / EBITDA on adjusted debt), then on table 1 as the cross-check, and say when the two disagree. Stress coverage with formula 6 at a shock at least as large as the worst year in the window or the sector volatility, and run the refinancing stress in formula 6a on the maturities within 24 months, alone and combined with the shock. Run the distress signals in the credit method's interpretation rules, and quote Altman Z and Piotroski as reported, with no cutoffs. Then mark each permanent-loss event from downside method step 3 present, absent or unknown. Done when coverage after the shock and after refinancing, the maturity table and the permanent-loss events are stated.

5. **Accounting risk.** `references/earnings-quality.md` steps 2, 4, 5, 10, 11 and 13: the accrual ratio over the four years five annual periods allow, recurring one-offs, reserve releases, the equity residual, the governance events, and the flags with a severity level from table 3 (a scale designed for these skills, labelled so). Done when the level and the flags behind it are stated; where the level is 3 or 4, the figures not to rely on are named and step 2 uses the rebuilt earnings.

6. **The risks ranked by probability and size.** List the risks from steps 2 to 5 and the category searches, merging duplicates. For each: the probability over a stated window as an integer percent, anchored to a reference class where one exists and labelled judgment (`references/forecasting-discipline.md` rule 2); the size as value per share lost, from step 2 or 3; whether the loss would be permanent or temporary; and the early signal that would show it first, with where to watch for it. Rank by expected loss (probability times size). Label management claims, broker views and targets as opinions. Done when every ranked risk has a probability, a size, a permanence mark and an early signal.

7. **Why it is cheap and who is selling**, when the stock has fallen (downside method steps 4 and 5), with the quarterly 13F changes as the holder evidence. Short interest and option prices are not in Bigdata.com; say so in Gaps. Done when the reason and the seller are named or marked unknown.

8. **The premortem** (`references/forecasting-discipline.md` rule 3). Assume that one year from now the outcome the reader fears has happened (for a holder, the shares have fallen hard; for a short seller, they have risen; for a lender or supplier, the company is in distress), and write why. Done when at least three reasons are written, each mapped to a driver or a kill criterion.

9. **Kill criteria with dates** (table 4 of the downside method and rule 4 of the forecasting method), with dates from Gather step 8. A price fall alone is not a kill condition: re-test the thesis on value. Done when each criterion has a driver, a checkable threshold and a date.

Special cases:
- Non-US listings and emerging markets: demand a wider margin for incomplete disclosure, restricted share classes and illiquidity, and compare local accounting with peers in other countries.
- Loss-making or early-stage companies: the sources give no cash-runway method; state the burn rate and the runway as derived and the funding assumption as assumed, and treat a need to raise capital as a permanent-loss event.
- Cyclicals: set the break cases and the floors on multi-year average earnings and mid-cycle EBITDA, not the latest year.
- Holding companies: name which legal entity owes each debt, since holding-company debt can default while operating subsidiaries carry on.

## Write

Follow `references/output-standard.md`. The report has these sections in this order.

```
# <Company> (<ticker>) downside and risks, <date>
Data as of: price <date>; estimates <date>; statements <period>; newest document <date>.
Reader and horizon: <holder, short seller, lender, supplier, acquirer>, <window>. Assumptions:
cost of equity, stressed discount rate, liquidation haircuts, EBIT shock, refinancing yield, each
with its basis.

## The downside
Four to eight sentences: what the price assumes, the downside range and floors against the price,
whether the balance sheet survives the stress case, the two or three risks that dominate expected
loss, and the earliest dated signal, written for the reader named above. No rating and no
recommendation.

## What the price assumes
One short table: price, EV, forward P/E, one over the assumed cost of equity, consensus growth
and margin, each with Basis and Source.

## What breaks each driver
| Driver | What breaks it | Evidence | Value per share if broken (alone) | Loss from price | Basis | Source |

## Floors
| Floor | Value per share | Price as % of floor | Method and haircuts | Basis | Source |
Rows: net cash, net-net working capital, current-asset value, tangible book, liquidation,
private-market value, stressed cash-flow value (whole company). Downside range; margin of safety
vs the lower value.

## Balance sheet and liquidity under stress
| Measure | Value | Agency range (table 3) | Rating median band (table 1) | Basis | Source |
Coverage after the assumed shock and after refinancing; maturities within 24 months (amount, date,
funding source); claims outside the debt line; distress signals; Altman Z and Piotroski as
reported; the permanent-loss events marked present, absent or unknown.

## Accounting risk
Severity level with its reason and the flags behind it.

## Risks ranked by probability and size
| Rank | Risk (category) | Probability (window) | Size per share | Expected loss | Permanent? | Early signal |
Basis and sources note under the table.

## Why it is cheap and who is selling
Only when the stock has fallen.

## Premortem
Three or more reasons, each mapped to a driver or kill criterion.

## Kill criteria
| Condition | Driver | Threshold | Date | Where the date comes from | Basis | Source |

## What would change this reading
## Gaps
## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. The cost of equity, the discount rate for the stressed case, the haircuts, the shock size, the refinancing yield and the probabilities appear once in an Assumptions line with their basis. For a narrow question, answer with the relevant step, its table and the sources, and keep the footer.

## Checks before sending

1. The downside and the floors come before anything that reads as upside.
2. Each broken driver is valued alone in the value-driver formula; the stressed cash-flow value appears once, as the whole-company floor.
3. Every floor is per share with the price as a percentage of it, and the liquidation haircuts are labelled illustrative 1930s figures, historical.
4. Private-market multiples name the deals, dates and financing, and inflated or debt-fuelled multiples are flagged.
5. The company is placed on the agency ranges before the rating medians; the stress shock is at least as large as the worst year in the window or the sector volatility; maturities within 24 months have amounts, dates and the refinancing stress.
6. Every ranked risk has an integer probability with a window, a size per share, a permanence mark and an early signal.
7. The premortem has at least three reasons, each mapped to a driver or a kill criterion.
8. Every kill criterion has a driver, a checkable threshold and a date; none is a price level alone.
9. Altman Z and Piotroski are quoted as reported, with no zones; credit-factor results are cited as news catalysts, never as spreads or ratios.
10. Facts and opinions are labelled apart, and the disconfirming search is shown with its result. No table passes eight columns.
11. No buy, hold, sell, stop-loss, position size or rating word.

## Hand-offs

- The user wants the credit of the company's bonds or loans: `bigdata-credit`. The accounting in depth: `bigdata-earnings-quality`.
- The user wants the upside case and the full thesis: `bigdata-thesis`. Probability-weighted cases with an expected value: `bigdata-scenarios`.
- The user wants the dated events that could close or widen the gap: `bigdata-catalysts`.
- After delivering, make one offer: a monitor on the early signals and kill criteria (filings, rating actions, guidance changes, the named risks) until the last kill date. Act only on a clear yes.
