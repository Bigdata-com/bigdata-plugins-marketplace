# Output standard

Every Bigdata.com skill writes to this standard, so a reader who has seen one report knows where to look in the next. The reader is a professional who will act on it: a portfolio manager or analyst, or a corporate strategy, finance or investor-relations team reading about their own company, a competitor, a customer, a supplier or a target. All of them want the evidence, the arithmetic behind it and what would change the reading, in plain language. When the user's role is clear, write the implications for that reader; the evidence and the arithmetic are the same. Follow the user's own structure, length or format when they gave one, and keep the citations, the Gaps line and the footer in every case.

## The frame

1. **Header.** The title names the subject, the ticker and the job ("Micron (MU) earnings preview: Q1 FY2027, reports 17 Dec 2026 after market"). Under it, one line: "Data as of:" with the date of the price used, the vintage of the estimates, the latest fiscal period in the statements and the date of the newest document read.
2. **The answer first.** Four to eight sentences in prose that say what the evidence shows, what the price implies where that applies, and what would change the reading. No heading called "Executive summary"; call it what it is ("The setup", "The view", "What happened").
3. **The body** in the sections the skill defines, in its order.
4. **What would change this reading.** Two to five conditions, each observable and dated where possible. In a report that gives no view of its own (a brief, a watchlist check, a market wrap) call the section "What to watch".
5. **Gaps.** What Bigdata.com could not answer, in one or two lines. Never fill a gap from memory or the open web without saying so in this line.
6. **Sources** (optional, see Citations) and the **Data** line, then the footer, verbatim.

## Numbers

- Every figure carries its unit, currency and period, and consensus figures carry their vintage and the number of estimates when the tearsheet gives it.
- Tables have a **Basis** column and a **Source** column, or, when that would take a table past eight columns, one Basis and Source note under the table that covers every row. Keep tables at eight columns or fewer; split a wider one. Basis is one of four words: *reported* (taken from a document or a data set, with a citation), *derived* (computed from reported figures; name the formula or the fields once, in a note under the table or in the Data line), *assumed* (an input the analyst chose, with its basis), *judgment*.
- In prose, mark a derived or assumed figure the first time it appears ("implied growth of 4.5 percent a year, derived at an assumed 9 percent cost of capital"). Reported figures need only their citation.
- Assumptions appear once, in a table or an Assumptions line, with the reason for each value and a sensitivity where the result depends on it.
- Historical base rates are labelled with their sample and period ("top 1,000 global companies by market cap, 1950 to 2015, inflation-adjusted") and never presented as current facts. Dated figures from the method files are quoted with their source and period and the words "historical, not current"; the "(verify)" marks inside the method files are a working note for the analyst and do not appear in the deliverable.
- Ranges, not points, for forecasts and values. Probabilities sum to 100 and say where the weights came from.
- Compute with the host's code execution or Bigdata.com's computing tool when the arithmetic has more than a few steps, and show the working for anything a reader would want to check.
- Before finishing, re-read every number in the opening section and in prose against the table it came from. They must agree, to the same rounding. A summary that says "third" when the table says second, or 2.39 points when the table gives 2.45, is the commonest error in these reports and the easiest to catch.

## Citations

- **Attach the source when you write the sentence, not at the end.** The moment a fact is taken from a search result, a document or a data set, its link travels with it into the notes and then into the report. Citation numbers assigned afterwards, from memory of thirty excerpts, land on the wrong document; a link carried from the excerpt does not.
- Cite inline, right after the claim, as a link with the source name and date: "guided to $9.6bn at the midpoint ([Micron Q4 FY2026 call, 24 Sep 2026](url))". The URL is the attribution URL the tool result gave, never invented. A source cited several times can be given a short name after its first full citation ("[the Q4 call](url)").
- Prefer the primary document (the filing, the transcript, the release, the rating action) to the article that quotes it, and cite one document per fact. Fewer, better sources: a report that leans on twenty documents has fewer wrong citations than one that leans on sixty.
- A **Sources** section at the end is optional. When used, it is the list of the inline links, each once, in the server's link format, and it adds no source that the body does not cite.
- Figures computed from Bigdata.com data sets that have no document behind them (prices, estimates, statements, screens) are covered by one **Data** line at the end: "Data: Bigdata.com company tearsheet for Micron, FactSet fundamentals and consensus estimates, retrieved Oct 23, 2026."
- A claim with no source and no Basis label does not go in the report. This applies to numbers inside sentences as much as to tables: a figure in prose carries its link or its basis word (derived, assumed) in the same sentence.
- Last pass before sending: read each citation next to the claim it supports and ask whether that document can contain that fact. A debt figure cited to a market-wrap article, or a reporting date cited to an unrelated story, is the sign that a number was assigned from memory; find the excerpt it came from or drop the claim.

## No recommendation

The report describes the balance of evidence and what would change it. It never gives a buy, hold, sell, overweight, underweight, accumulate, avoid or similar call, a rating, a stance line, a price target of its own, or a position size. When a user asks "is it a buy", answer with what the price assumes, what the evidence says about that, and what would change the reading. The disclaimer below promises this, and a call would contradict it. A corporate user asking about their own decision (buy back or raise the dividend, which deal structure, whether to refinance) gets the arithmetic and the trade-offs of each option laid side by side; that is analysis of a corporate choice, not a call on a security.

## Size

Length follows the ask, not a page count. The skills' sections are guidance for what a complete answer covers; a report that needs more pages to cover them takes more pages, and a narrow question ("did they beat") gets the relevant table, the sources and the footer. What keeps a long report cheap for the reader is the frame above: the answer and the decision table first, so the rest can be read or skipped. As a rough guide, a quick take is a page, a brief or a wrap one to three, a single-method report (preview, review, valuation, credit) three to six, and a deep dive, sector, theme or country note six to ten.

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
