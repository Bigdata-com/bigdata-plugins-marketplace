---
name: bigdata-deep-dive
description: >-
  Full company research: economics, moat, earnings quality, capital allocation, what the price
  implies, valuation range, risks, catalysts. Use for a deep dive, initiation, investment memo,
  due diligence. Not one page: bigdata-quick-take.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, roic, valuation, industry-structure, earnings-quality, capital-allocation, expectations, base-rates, forecasting-discipline, multiples-and-peers, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Deep dive

The full research report on one company, for someone who will act on it: how it makes money and how well, what protects that, whether the earnings in the accounts are the real earnings, what management does with the cash, what the price assumes, what the company is worth across cases, what breaks it and what to watch. Never a rating, a target or a point value. Due diligence on a partner, customer or supplier asks a different question, so the contract terms and counterparty risks the evidence points to come first there. Size the work to the question: "what is the ROIC trend at Danaher?" gets the ROIC series built from the statements, its margin and turnover split, the three-year ROIIC and the links, not the full report; a company with one segment and no acquisitions needs no sum of the parts and no deal history.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-deep-dive"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a report that answers it with fewer tables and pieces is the better report.
- **Returns built from the statements, when the question reaches the economics.** NOPAT at the operating tax rate and invested capital from both sides of the balance sheet, with and without goodwill, split into margin and turnover where the split explains the trend. The three-year rolling ROIIC sits beside it when the question is the next five years, because the trend in returns on new capital says more about them than the level does. A vendor ROIC field is compared in one line and never mixed into the same table (`references/roic.md`, NOPAT, invested capital, ROIC decomposition, and ROIIC and the spread).
- **One cost of capital and one share count through everything.** The cost of capital is built once, with the beta checked against peer and sector betas and the cost of equity inside the market's range, and used in the economics, in what the price implies and in the valuation. On the page it is one stated figure, with the yield, beta and premium in a single clause and no regression statistics; the 10-year yield in the cash-flow currency comes from the country data (`references/valuation.md`, cost of capital). One share count, from the filings, runs through price, enterprise value and value per share.
- **Inputs stated once.** Where the report uses an enterprise value, a bridge to equity or a sum of the parts, its inputs appear once, from the latest filing: the share count, net debt with leases and stakes outside the operating business, the tax rate and the discount convention, so the reader can rebuild every later figure (`references/valuation.md`, equity bridge). The profit a multiple is applied to says whether it is before or after tax.
- **The moat tested, not asserted, when the question is how long returns last.** Entry and exit come first, because low barriers push returns toward the cost of capital whatever the other forces show; the claimed source of advantage has to show its signature in gross margin and turnover against peers over a cycle; brand, size or share alone is never a moat. How long excess returns last is bounded by the sector's return persistence and the listed-company half-life, which reach the page only as the bound they set; the period the price implies is a comparison, never a bound (`references/industry-structure.md`, entry and exit, moat tests, and competitive advantage period).
- **Earnings quality from cash and recurrence, when the accounts raise a question or the value rests on an adjusted figure.** The accrual ratio in its cash-flow form, and EBITA rebuilt beside published operating profit, because the gap between them is where the published number overstates the business. A "one-time" charge that recurs is an operating cost and goes in the forecast. Stock compensation is a cost inside net income: past awards sit in the share count, future awards in the forecast, never added back and never deducted twice. Piotroski and Altman Z are quoted as the data set computes them, with no zones of their own, and only where they change the reading (`references/earnings-quality.md`, accrual ratio and cash conversion, rebuilding EBITA, recurring one-offs, and pensions, leases, R&D, stock compensation, sold receivables).
- **Capital allocation judged at the price paid.** The buyback return at the year-average price paid, net of issuance, against value at the time; a deal's synergies after tax against the premium; EPS accretion is not value (`references/capital-allocation.md`, buybacks, acquisitions, and verdict per use).
- **What the price implies comes before the valuation,** because the reader needs the bar before the range: how much of the price the current business supports and how much rests on future value creation, and the growth and competitive advantage period the price needs at the same cost of capital (`references/expectations.md`, implied growth and implied competitive advantage period). When the bar rests on a multi-year growth or margin path and the history changes how it reads, the sentence carries how often companies of this size achieved it, with population and period (`references/base-rates.md`, real sales growth by starting size); otherwise the history stays in the working, as do the steady-state multiple and the share of the price paid for growth unless the user asks what the multiple means.
- **Cases that partition the outcomes, when the value turns on drivers that could go either way.** Two or three swing drivers carried through the whole model with their second-order effects on reinvestment and margin. Each driver has one cut-off across the whole note, so every value falls in exactly one case. Probabilities start from the share of a stated reference class that reached each case's driver value, or from the company's own record, never a default split. Each case's value shows the figures it rests on; continuing value states the return on new capital it assumes; the probability-weighted value is stated and reconciles with those figures. One central case and one range cover the sensitivity (`references/valuation.md`, continuing value and sensitivity and cases; `references/forecasting-discipline.md`, scenario weights from a reference class and expected value). Banks, cyclicals, high growth, multi-business and distressed companies each change the method (`references/valuation.md`, special cases).
- **Peers chosen by value drivers, when a multiple carries the reading,** with the selection rule stated before the multiple and the median given with and without any outlier, because a peer set chosen by industry code imports companies with different returns and growth (`references/multiples-and-peers.md`, peer selection by value drivers).
- **Downside before upside, and a premortem before the risk list,** because a list written first collects generic risks. Assume the reading has proved badly wrong a year from now and give three reasons, each tied to a driver. The floor values that apply, whether a loss would be permanent or temporary, and why the price is where it is and who is selling follow where they change the reading; kill criteria each carry a driver, a threshold and a date (`references/forecasting-discipline.md`, premortem and kill criteria with dates; `references/downside-and-catalysts.md`, floor values, permanent against temporary loss, and why it is cheap and who is selling).
- **Facts kept apart from opinions and from what is priced,** and the market treated as right unless there is a specific, evidenced reason it is not, which the report names (`references/forecasting-discipline.md`, facts, opinions and expectations).

## Where it goes wrong

- **Two share counts.** Market value on basic shares and value per share on diluted shares put the comparison on two bases. One count, from the filings.
- **A raw regression beta.** An unchecked beta can produce a cost of capital at which no case reaches the price. Check it against peers before using it.
- **A risk-free rate taken from memory** when the country data has the yield.
- **Shares of a total that leave out a loss.** Shares of segment profit are computed on the total including loss-making segments, or the note says what is excluded.
- **A loose annualisation.** State the number of days and compute; "about six weeks" is not a basis for an annual figure.
- **Width.** A table past eight columns is split, or its sources move to a note under it.
- **Citations assembled at the end.** The link goes next to the fact when the fact is captured.
- **The note mirrors the method.** A figure that does not change the reading stays in the working, and the working itself never reaches the page.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, the limit, so the profit pool is compared over five years, not ten, and the report says so. Industry shares and concentration figures are often partial; state the coverage of any that are used. The executive team and the deal history need FactSet access; when they come back empty, they come from search. A newly listed company may have a registration statement rather than an annual report; say which document stands in. The last three earnings calls, each with its period fixed; the call for the latest quarter carries next quarter's guidance. Consensus is a snapshot with its date and no revision history. The corporate calendar carries earnings dates, conferences, IPOs and delistings only, so shareholder votes, court and regulatory dates, debt maturities, product launches and lock-up expiries come from filings and news. Institutional holder data is quarterly and lagged. Short interest, option prices and a cost of capital have no structured field; news, research and filings often carry the first two, and the cost of capital is built. The risk-free rate and inflation for the cash-flow currency are in the country data. Peers are pulled as a set in one batch, not one tearsheet each. A private company has no price or consensus, so what the price implies, market multiples and positioning do not run, and the header says so. `references/sector-primers.md` has the sector's metrics, accounting traps and valuation conventions.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line, not the company's name alone. The opening gives what the business is, how good its economics are and what protects them, what the price implies against the range of values, and the main risk, in plain sentences the reader can act on. The body follows the question. Kill criteria with their dates and the catalysts to watch close the note. Sub-headings state the finding ("Returns on new capital have halved since the 2021 deal"), never the step that produced it.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with the body, and the net debt or enterprise value used anywhere equals the inputs stated once.
- One cost of capital and one share count run through the economics, what the price implies and the valuation.
- Where there are cases, each driver has one cut-off across them, the probabilities sum to 100 and rest on a stated reference class or record, and the probability-weighted value reconciles with the figures.
- Every code name or internal term is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
