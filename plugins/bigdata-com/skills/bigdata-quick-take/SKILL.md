---
name: bigdata-quick-take
description: >-
  One-page view on a stock or company: what the price implies, the drivers that matter now, risks,
  next catalyst. Use for quick take, a one-page read on X, thoughts on a ticker, is X interesting.
  Not a full thesis: bigdata-deep-dive.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, valuation, base-rates, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Quick take

One page that answers "what do you think of Micron" the way an analyst would in a morning meeting: what the price already assumes, the three things that decide whether it is right, the ways it goes wrong and the next date that tells. Never a rating, a target or "interesting at this price". Size the work to the question: "is Micron's multiple high?" gets the forward P/E against the steady-state P/E and the peer median, what the multiple means for growth, and the links, not the full page.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-quick-take"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a page that answers it with fewer tables and pieces is the better page.
- **What the price implies comes first,** because the page opens with the height of the bar rather than the story or the multiple: the growth the enterprise value implies at the stated cost of capital and return on new capital, set against consensus growth (`references/expectations.md`, implied growth). The enterprise value's inputs appear once (share count, net debt with leases and stakes outside the operating business, tax rate, discount convention), so the reader can rebuild it. The profit a multiple is applied to says whether it is before or after tax. The cost of capital is one stated figure, with the yield, beta and premium in a single clause and no regression statistics; the 10-year yield in the cash-flow currency comes from the country data (`references/valuation.md`, cost of capital). One central case and one range cover the sensitivity. The steady-state P/E and the share of the price paid for growth stay in the working unless the user asks what the multiple means (`references/expectations.md`, steady state and value creation).
- **Implied growth with its return on new capital beside it.** The growth the price implies changes with the return on new capital, so the three-year rolling ROIIC, or the figure used in its place, sits in the same sentence.
- **Consensus growth placed in its history, when it carries the reading.** When the conclusion rests on a multi-year growth rate and the history changes how it reads, one sentence gives how often companies of this size reached it over three years, with the population and period in the sentence; the one-year figures are too dispersed to mean anything for one company (`references/base-rates.md`, real sales growth by starting size).
- **A relative line beside the absolute one, when the read of the price would otherwise rest on one measure.** Forward P/E and EV/EBITDA against the median of two or three peers (up to five when the user asks for a peer angle).
- **Up to three drivers, chosen by what moves value.** Where returns on new capital sit near the cost of capital, the incremental return is the driver that matters; well above it, sales growth. Each driver gets a sentence with what consensus assumes, one dated piece of evidence and the direction the risk runs (`references/expectations.md`, which revision moves value).
- **Risks that would change the reading, each with its first observable sign.** Usually the one that breaks the drivers; a balance-sheet or accounting risk, or one from outside (a regulator, a customer, a technology), earns a line only when there is one, with how it would show up first.
- **A downside line, when a floor sits close enough to the price to matter.** The price per share against the floors that apply (net cash, tangible book, a stressed cash-flow value); for software and services the stressed cash-flow value, for banks book value and earnings quality (`references/downside-and-catalysts.md`, floor values and when the floors do not apply).
- **The next catalyst with who decides it.** The date, its type, who decides it and how much of the gap between price and value it could close (`references/downside-and-catalysts.md`, catalysts).
- **The price stands unless there is evidence against it.** Where the page's reading differs from what the price implies, it names the evidence.
- **Special cases.** A bank: price to book against return on equity. A cyclical: earnings normalised to a mid-cycle margin, stated. A loss-making company: the P/E is not meaningful; give the revenue the price needs at a stated margin path (`references/expectations.md`, special cases).

## Where it goes wrong

- **Running long.** A quick take that becomes three pages is a brief nobody asked for: cut each driver to a sentence before cutting a line of what the price implies.
- **A risk-free rate taken from memory** when the country data has the yield.
- **Implied growth with no return on new capital beside it.** It cannot be checked.
- **Peer multiples taken from the profile's competitors block,** which carries symbol, price and market cap only. Pull the peers' key metrics and next-year consensus EPS, and compute the forward P/E.
- **Citations assembled at the end.** The link goes next to the fact when the fact is captured.

## What the data has, and does not

Consensus is a snapshot with its date and no revision history, so a 30-day revision or target change comes from research and news dated in the window; where none is found, the note says so. The transcript for the last call is fetched with its period fixed; the call for the latest quarter carries next quarter's guidance. Five fiscal periods per pull, annual when years are wanted, which allows a three-year ROIIC and nothing longer. The several-company grid carries price, move, surprise, targets and sentiment but no multiples; peer metrics come as a set in one batch. Sentiment has no window: say which period its narrative covers. The cost of capital has no structured field and is built, with the risk-free rate from the country data. A private company has no price to read expectations from: say so and offer a summary from documents. `references/sector-primers.md` gives the sector's own drivers.

## Write

`references/output-standard.md` holds the rules. One page: about 450 words before the sources, and at most one table. The title carries the finding in one line ("Micron's price needs a memory upcycle longer than any since 2010"). The opening gives what the price implies, whether the evidence supports it, and what would change the reading, in prose. The body follows the question: the drivers, the risks with their early signs, the downside line where it applies. The next catalyst, with its date and what it decides, closes the page.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Within one page, and every number in the opening agrees with the body.
- The net debt or enterprise value used anywhere equals the inputs stated once, and implied growth has its return on new capital beside it.
- Each driver has a dated piece of evidence, and each risk has an early sign.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
