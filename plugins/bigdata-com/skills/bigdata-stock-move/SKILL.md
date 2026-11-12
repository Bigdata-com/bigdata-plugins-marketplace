---
name: bigdata-stock-move
description: >-
  Why a stock moved: the trigger, headline vs change in the long-term outlook, revisions, base
  rates for what follows a move that size. Use for why is X down, why did our stock drop, what
  moved it. Not the quarter: bigdata-earnings-recap.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, after-a-price-move, expectations, valuation, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Stock move

A note on why a stock moved, whether the move reflects a change in the company's long-term outlook or a one-quarter headline, what the people who set the price did next, and, for a large one-day move, what history says follows a move like it. Never a view on whether to buy the dip, add or trim. A company asking why its own stock dropped asks a different question: what investors changed their mind about, what they will ask next, and what the company can still show them, ahead of the investor measures. Size to the question: "what happened to Deckers today" gets the trigger with its source, what the market changed its mind about and what the estimate-setters did, with the history in one sentence when the move qualifies.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-stock-move"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts come first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply only where the question reaches them. A note that answers the question with fewer tables and fewer pieces is the better note.
- **The size of the move is measured before it is explained.** From the daily series for the stock and its index over the exact window, never from the user's figure, stated close to close, or with the time when a pre-market or after-hours price is used. One pre-event price is fixed from the series and every percentage is computed from it. With no window named, take the largest one-day move in the last five trading days.
- **Pin down what kind of move it was before explaining it.** The move against the index, simple or beta-adjusted with the one used stated, whether it came on earnings, over one day or several, and the part the peers shared over the same window, so the company-specific part is what gets explained. A cause is easy to invent for any move, so this comes before the story, written as a plain sentence with its figures, never as a label or a bolded category (`references/after-a-price-move.md`, classifying the event, abnormal return).
- **Headline or long-term outlook.** The price capitalises years of cash flow, so a large move is the market revising growth, margins, returns, the period of excess returns or the per-share claim. Say in a sentence, with its evidence, which the trigger changed and by how much, from consensus for the second year out and beyond, guidance and cash flow, or that it changed none and what the move then implies; never a label such as "long-term" or "headline" (`references/after-a-price-move.md`, long-term outlook test). Where the move is large enough to matter for value and the question is what the market now assumes, compare the growth the enterprise value implied before the move with the growth it implies after (`references/expectations.md`, implied growth); otherwise it stays in the working. When it is shown, the inputs appear once, from the latest filing: share count, cash, debt, leases, stakes outside the operating business and the net debt they give, the tax rate on the profit figure, and the discounting convention, so the reader can rebuild both figures; the before and after figures use the same inputs. The cost of capital is one stated figure, with the yield, beta and premium behind it in one clause and no regression statistics; the 10-year yield comes from the country data (`references/valuation.md`, cost of capital).
- **Price and estimates read together.** Price down with estimates down reads as a fundamental revision; with estimates flat as a multiple or positioning move; with estimates up as unusual, and the note says so. A miss or beat is given on revenue and on EPS, each against consensus with its source.
- **What followed similar moves, only for a one-day move of 10 percent or more against the index.** Start at the row for the event type and the momentum going in, and step down to valuation and quality only while the row holds about 50 events or more. One sentence carries the population and period (US large caps with one-day moves of 10 percent or more against the S&P 500, 1990 to 2014 for drops and to 2015 for gains), how many events the row holds, the drift at 30, 60 and 90 trading days, and how widely outcomes spread around it, because the median sits below the mean and the spread is wide. A smaller move or a move over several days gets no drift figures; a non-US stock or a recent date says in the same sentence that the history is of US stocks before 2016 (`references/after-a-price-move.md`, drift after one-day drops, drift after one-day gains, drift in the branches with the sharpest contrasts, dispersion of drift, reading the drift tables).
- **Momentum, valuation and quality as they stood before the event**, when the drift row is stepped down. They choose the row; the page carries the row and the standing that put the stock in it, in a sentence. Valuation is re-based to the pre-event price so a stock is never scored cheap because it just fell; momentum uses the 13-week revisions from dated documents; quality uses the data set's ROIC against peers and its spread over the stated cost of capital (`references/after-a-price-move.md`, momentum, valuation and quality before the event).
- **Who is selling and the next date.** Forced sellers (an index change, a downgrade, holders who owned it for what just broke) from filings and news, because selling that is not about value tends to reverse; the next dated event that resolves the question the move raised. When the stock fell and the reader is weighing how far it could go, the floors that apply (net cash, asset value, a private-market value only where a dated transaction gives one) (`references/downside-and-catalysts.md`, why it is cheap and who is selling, floor values, catalysts).
- **No trigger found is an answer.** When the searches find nothing company-specific and the peers do not explain it, the note says the trigger was not found and gives the measured move, the estimates and, for a qualifying move, the history, without a story.

## Where it goes wrong

- **Only half the miss quantified.** Revenue and EPS both, each against consensus with its source.
- **Before and after figures on different measures.** Take before and after targets and estimates from the same provider and measure, or say the change cannot be measured.
- **Prices that do not reconcile.** Every percentage comes from the one pre-event price fixed from the series.
- **A record claim resting on one quote** ("the first miss in five years"). Check it against the surprise history, or attribute it.
- **Citations assembled at the end** land on the wrong document. The link goes next to the fact when the fact is captured.
- **A drift row with few events quoted as a finding.** Below about 50 events, the parent row is the figure.

## What the data has, and does not

The quote carries standard windows only; the move over the exact window, the index over the same days, the pre-event price and the peers' moves over several days need the daily series; the peers' one-day move comes from the current figures for the set in one pull. Consensus is a snapshot with its date and no history, so the before figures come from research and news dated in the 13 weeks before the event, each with its source and date. The snapshot's target and rating counts can come from a provider that has not caught the day's cuts, so after-event figures come from dated documents with the provider named. The transcript for the latest quarter is fetched with its period fixed. Five fiscal periods per pull. 13F holder and options data is quarterly and filed with a lag: it shows who sold over the quarter, not on the day. There is no structured field for short interest, option prices or intraday flows; news and research often carry them, so search before stating a gap. Sentiment has no window: say which period its narrative covers. `references/sector-primers.md` gives the sector's drivers and accounting traps.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Deckers fell 12 percent on a guide cut, not on the quarter"), and the move against the index over the stated window sits in the first sentence. The opening gives the trigger with its source and time, what the market changed its mind about, what the estimate-setters did, and, for a qualifying move, what history says about the next three months. The body follows the question, and the note closes on who is selling, the floor where one applies, and the next date that settles the question. Sub-headings state the finding, never the step.

## Before sending

- The move, the index move and the peer move cover the same window from the price series, and every percentage comes from one pre-event price.
- Every before-the-event consensus or target figure names its dated document and matches the after figure's provider and measure.
- Drift figures appear only for a one-day move of 10 percent or more against the index, with population and period in the sentence; the net debt used anywhere matches the inputs stated once.
- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with its table, and every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure carries a tag saying how it was obtained; no sentence describes how the note was made.
