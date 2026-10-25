# Output standard

Every Bigdata.com skill writes to this standard, so a reader who has seen one report knows where to look in the next. The reader is a professional who will act on it: a portfolio manager or analyst, or a corporate strategy, finance or investor-relations team reading about their own company, a competitor, a customer, a supplier or a target. All of them want the evidence, the arithmetic behind it and what would change the reading, in plain language. When the user's role is clear, write the implications for that reader; the evidence and the arithmetic are the same. Follow the user's own structure, length or format when they gave one, and keep the citations, the Gaps line and the footer in every case.

## The frame

1. **Header.** The title names the subject, the ticker and the job ("Micron (MU) earnings preview: Q1 FY2027, reports 17 Dec 2026 after market"). Under it, one line: "Data as of:" with the date of the price used, the vintage of the estimates, the latest fiscal period in the statements and the date of the newest document read.
2. **The answer first.** Four to eight sentences in prose that say what the evidence shows, what the price implies where that applies, and what would change the reading. No heading called "Executive summary"; call it what it is ("The setup", "The view", "What happened").
3. **The body** in the sections the skill defines, in its order.
4. **What would change this reading.** Two to five conditions, each observable and dated where possible. In a report that gives no view of its own (a brief, a watchlist check, a market wrap) call the section "What to watch".
5. **Gaps.** What Bigdata.com could not answer, in one or two lines. Never fill a gap from memory or the open web without saying so in this line.
6. **Sources**, then the footer, verbatim.

## Numbers

- Every figure carries its unit, currency and period, and consensus figures carry their vintage and the number of estimates when the tearsheet gives it.
- Tables have a **Basis** column and a **Source** column, or, when that would take a table past eight columns, one Basis and Source note under the table that covers every row. Keep tables at eight columns or fewer; split a wider one. Basis is one of four words: *reported* (taken from a document or a data set, with a citation), *derived* (computed from reported figures; name the formula or the fields once, in a note under the table or in the Data line), *assumed* (an input the analyst chose, with its basis), *judgment*.
- In prose, mark a derived or assumed figure the first time it appears ("implied growth of 4.5 percent a year, derived at an assumed 9 percent cost of capital"). Reported figures need only their citation.
- Assumptions appear once, in a table or an Assumptions line, with the reason for each value and a sensitivity where the result depends on it.
- Historical base rates are labelled with their sample and period ("top 1,000 global companies by market cap, 1950 to 2015, inflation-adjusted") and never presented as current facts. Dated figures from the method files are quoted with their source and period and the words "historical, not current"; the "(verify)" marks inside the method files are a working note for the analyst and do not appear in the deliverable.
- Ranges, not points, for forecasts and values. Probabilities sum to 100 and say where the weights came from.
- Compute with `bigdata_computer` or the host's code execution when the arithmetic has more than a few steps, and show the working for anything a reader would want to check.

## Citations

- Cite inline with numbers in square brackets right after the claim: "guided to $9.6bn at the midpoint [3]". One number per source; reuse the number for a source cited twice.
- The **Sources** section lists every number once, in the server's link format: `[3] [Micron Q4 FY2026 earnings call - Sep 24, 2026](url)`, with the attribution URL the tool result gave. Never invent a URL or a document id.
- Figures computed from Bigdata.com data sets that have no document behind them (prices, estimates, statements, screens) are covered by one **Data** line after the numbered sources: "Data: Bigdata.com company tearsheet for Micron, FactSet fundamentals and consensus estimates, retrieved Oct 23, 2026."
- A claim with no source and no Basis label does not go in the report. This applies to numbers inside sentences as much as to tables: a figure in prose carries its citation number or its basis word (derived, assumed) in the same sentence.

## No recommendation

The report describes the balance of evidence and what would change it. It never gives a buy, hold, sell, overweight, underweight, accumulate, avoid or similar call, a rating, a stance line, a price target of its own, or a position size. When a user asks "is it a buy", answer with what the price assumes, what the evidence says about that, and what would change the reading. The disclaimer below promises this, and a call would contradict it. A corporate user asking about their own decision (buy back or raise the dividend, which deal structure, whether to refinance) gets the arithmetic and the trade-offs of each option laid side by side; that is analysis of a corporate choice, not a call on a security.

## Size

| Skill | Length |
|---|---|
| quick-take | one page |
| company-brief, stock-move, catalysts, watchlist, markets-today | one to two pages |
| earnings-preview, earnings-review, valuation, comps, scenarios, earnings-quality, moat, capital-allocation, risk, credit, screen | two to four pages |
| deep-dive, thesis, sector, theme, country, macro-compare, deal-analysis, special-situations | four to eight pages |

A narrow question gets a direct answer in the skill's method with the relevant table and the sources, not the full report. The footer stays.

## Language

- Plain sentences, active verbs, the company and the ticker by name. Buy-side vocabulary is fine for this reader; define an uncommon term on first use.
- No hype adjectives, no "robust", "compelling", "significant" without a number, no exclamation marks, no emojis.
- Facts, then what they mean, then what would change the reading. Keep the three apart.
- Markdown by default: headings, tables for anything tabular, short paragraphs. Offer a Word document for a formal deliverable when the host can create files.

## Footer

Reproduce the two blocks below verbatim after Sources in every user-facing deliverable, including a one-line answer. The report ends on the disclaimer. The one offer a skill makes after delivery (save a watchlist, a monitor or the report; build a skill) is conversation, not report: put it in a separate short line after a blank line, so the deliverable itself still ends on the disclaimer.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
