---
name: bigdata-investment-thesis
description: >-
  Investment thesis: where the view differs from consensus, evidence for and against, bull and
  bear case, catalysts, kill criteria. Use for a thesis, variant view, bull and bear case,
  stress-test my idea. Not a full report: bigdata-deep-dive.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, valuation, base-rates, forecasting-discipline, industry-structure, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Investment thesis

A thesis written so a professional reader can test it: what the price already implies, the two to four claims where the evidence points away from consensus, each provable or disprovable by a date, the evidence for and against, why the gap exists, the loss case before the upside, and kill criteria written now so they cannot drift later. Never a buy, hold or sell call, a target or a position size. A variant view is a well-founded view meaningfully different from consensus; agreeing with consensus more enthusiastically is not one, and when no claim survives, the thesis says there is no variant view on this name now. Size the work to the question: "what is the market missing on Nike?" gets what the price implies, the consensus line and the one or two claims that survive, each with its evidence, test and date.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-investment-thesis"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a thesis that makes its case with fewer tables and pieces is the better thesis.
- **The bar before the view,** because a claim means nothing until the reader knows what the price already holds: the growth, return on new capital and years of excess return the enterprise value needs at the stated cost of capital, and whether that bar is high or low and why (`references/expectations.md`, implied growth and implied competitive advantage period). The enterprise value's inputs appear once, from the latest filing (share count, net debt with leases and stakes outside the operating business, tax rate, discount convention), so the reader can rebuild it, and every later figure uses them. The cost of capital is one stated figure, with the yield, beta and premium in a single clause and no regression statistics; the 10-year yield in the cash-flow currency comes from the country data (`references/valuation.md`, cost of capital). When the bar rests on a multi-year growth rate and the history changes how it reads, the sentence carries how often companies of this size achieved it, with population and period (`references/base-rates.md`, placing a forecast in the distribution); otherwise the history stays in the working.
- **Consensus written down before any claim,** with its date, estimate counts and the 30 and 90-day revisions from dated documents. A view cannot differ from a consensus that has not been stated.
- **The user's claims stay the user's.** When the user brings an idea to stress-test, their claims are tested as given; a new claim is added only if the evidence turns up one that matters more, and the note says so. The direction the user leans is noted, because the premortem runs against it.
- **Claims chosen by what moves value.** Where returns on new capital sit near the cost of capital, the return on new investment moves value and growth does not; well above it, sales growth does. A claim is kept only if its effect on value per share is large enough to matter, and the effect is stated (`references/expectations.md`, which revision moves value). A claim about how long returns last is tested on entry, bargaining power and the source of advantage, and bounded by the sector's return persistence (`references/industry-structure.md`, entry and exit, bargaining power, moat tests, and competitive advantage period).
- **Each claim written so it can be scored,** because a claim no date can settle cannot be tested. In sentences, not a grid: what consensus models for the metric and period, what the evidence points to and through what mechanism, the value per share at stake against what the price holds, and what would prove or kill it, as an observable, a threshold and a date. The default horizon is twelve months, because forecast skill decays beyond about a year; a longer view is broken into dated questions inside it (`references/forecasting-discipline.md`, questions that can be scored).
- **The outside view where a claim is a multi-year growth, margin or return claim** and the history changes how it reads: where the claim sits in the distribution for its reference class, with the population and period in the sentence, and how far the history pulls it back toward the class; an exception only with a specific, evidenced reason (`references/base-rates.md`, choosing the reference class, placing a forecast in the distribution, and regression to the mean).
- **Facts kept apart from opinions and from what is priced,** a disconfirming search run by name for each claim with what it found stated in that claim's evidence, and evidence that only looks causal kept apart from evidence that changes the odds (`references/forecasting-discipline.md`, facts, opinions and expectations).
- **A probability per claim,** a granular integer with the date it applies to, starting from the reference class or the company's own record and moved by the evidence (`references/forecasting-discipline.md`, granular probabilities and updating on evidence).
- **Why the gap exists, and who is on the other side.** A forced seller, a mandate constraint or an index change, with the quarterly holder changes as evidence; for a short idea, who is forced to buy. A gap with no structural reason is a warning that the claim may be wrong, and the note says so (`references/downside-and-catalysts.md`, why it is cheap and who is selling).
- **The loss case before the upside.** The floors that apply, per share, and the conditions that would make a fall permanent come before any upside figure; where the floors do not apply (software and services, banks and insurers), their substitutes (`references/downside-and-catalysts.md`, floor values, permanent against temporary loss, and when the floors do not apply).
- **A catalyst for every claim,** dated, with who decides it and how much of the gap it would close, and what happens if nothing happens (`references/downside-and-catalysts.md`, catalysts).
- **Three cases that partition the outcomes, when the thesis rests on a value gap the reader will weigh.** The thesis case, the consensus case and a downside case, each solved forward at its growth and return on new capital and bridged to equity per share item by item on the inputs stated once. Each driver has one cut-off across the whole note. Weights start from the reference class or the company's record, never a default split, and are integers summing to 100; each case's value shows the figures it rests on; the probability-weighted value is stated beside the price and reconciles with those figures, with the loss case beside the gain case. One central case and one range cover the sensitivity (`references/valuation.md`, equity bridge and sensitivity and cases; `references/forecasting-discipline.md`, scenario weights from a reference class and expected value).
- **A premortem against the lean.** Assume the thesis failed badly a year from now and give at least three reasons, each tied to a claim or a kill criterion; for a short or bearish thesis, run it on the bullish outcome (`references/forecasting-discipline.md`, premortem).
- **Kill criteria written now,** each with a driver, a checkable threshold and a date, and the date they were written (`references/forecasting-discipline.md`, kill criteria with dates; `references/downside-and-catalysts.md`, kill rule and sell logic).

## Where it goes wrong

- **A manufactured disagreement.** A claim that only agrees with consensus more strongly, or one with no evidence behind it, is not a variant view. When no claim survives the history and the disconfirming search, say so and what would have to change for one to form.
- **Value per share as enterprise value divided by shares.** It skips the claims between the two; bridge item by item, with one share count throughout.
- **A price level as a kill criterion.** A price fall is a prompt to re-test value, not evidence that the thesis broke.
- **The period of advantage the price implies used as a bound** on the fundamental estimate. It tests the price against itself; it is a comparison only.
- **A "temporary" reason for the discount with no evidence,** or an upside case with no loss case.
- **A risk-free rate taken from memory** when the country data has the yield.
- **Citations assembled at the end.** The link goes next to the fact when the fact is captured.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, the limit, which allows a three-year ROIIC and nothing longer. Consensus to four years out is a snapshot with its date and estimate counts and no revision history, so revisions and past targets come from research and news, quoted with their dates; where none is found, the note says so. The last two earnings calls, each with its period fixed; the call for the latest quarter carries next quarter's guidance. The corporate calendar carries earnings dates, conferences, IPOs and delistings only, so regulatory, contract, product and deal dates come from filings and news. Institutional holder changes are quarterly and filed with a lag. Short interest and option prices have no structured field; news and research often carry them, so search before stating a gap. The cost of capital is built, with the risk-free rate for the cash-flow currency from the country data. Sentiment has no window: say which period its narrative covers. A private company has no price to read expectations from: say so. `references/sector-primers.md` gives the sector's value drivers, metrics and accounting traps.

## Write

`references/output-standard.md` holds the rules. The title carries the variant view in one line ("The market prices Nike's margin recovery; the evidence says it is two years late"), or says there is none. The opening gives what the price implies, where the evidence differs from consensus and on which driver, how strong that evidence is, the loss case and the next date that tests the thesis, in plain sentences the reader can act on. What the price implies, consensus and the downside come before the first claim, because the claims carry value effects and the loss case has to be read first; then the body follows the question. The kill criteria, with the date they were written, close the note. Sub-headings state the finding, never the step that produced it.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with the body, and the net debt or enterprise value used anywhere equals the inputs stated once.
- Each claim has a probability with its date and a dated catalyst; where there are cases, each driver has one cut-off across them, and the weights sum to 100 and reconcile with the probability-weighted value.
- Every kill criterion has a driver, a threshold and a date, and none is a price level alone.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
