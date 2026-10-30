---
name: bigdata-company-brief
description: >-
  What happened at one company, each item with source, date and what it means. Use for what is
  happening at X, catch me up, latest news, a competitor update. Not a view: bigdata-quick-take;
  one day's move: bigdata-stock-move.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, expectations, after-a-price-move, downside-and-catalysts
  bigdata-sector-primer: auto
---

# Company brief

Never a view on the stock: no call, no target, no bullish or bearish verdict. What happened at one company over a window, and what each event changes in its value drivers, so the reader can tell what changed in the company and not only what was in the news. Size to the question: "any legal news on Pfizer this month?" gets the matching events, what each changes and the links in a few lines; a quiet month gets a short brief that says so, with the price against the index and the next date.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-company-brief"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for (operations, legal, the stock, a competitor) come first, in the user's order, each answered in full under its name; the choices below apply where the question reaches them, and a brief that answers the question with fewer tables and pieces is the better brief. The last part of the question (what it means for us, for the industry, for a counterparty) gets the same depth as the first, with the arithmetic that supports it on the page: a runway or coverage figure is computed, not asserted.
- **An event judged by what it moves in value.** A headline with a positive or negative tag tells the reader nothing about value, so each event that matters is a sentence saying which driver it moves (sales by volume or by price and mix, operating margin, the investment growth needs, how long returns stay above the cost of capital, the per-share claim through dilution, debt or a buyback), which way, and how much where the figures allow, such as a contract's annual value as a share of sales or a fine as a share of free cash flow; where no size can be inferred, the sentence gives the mechanism. A table of events only when there are more than four and the reader needs to compare them.
- **The driver that matters for this company, when events have to be weighed against each other.** Where the return on new investment is near the cost of capital, events that change that return move value and growth news does not; where it is well above, sales growth moves value. Judge it on a three-year rolling return on new investment from the five annual periods, never on a single year; when the statements do not allow it, use the FactSet ROIC field and say the reading rests on it. The figure goes on the page only when the reader needs it to follow the ordering; otherwise it stays in the working (`references/expectations.md`, which revision moves value).
- **Whether an event reaches beyond the next year.** The price capitalises many years of cash flow, so an event matters to value when it changes cash flow beyond the next year. For an event that matters, ask whether consensus or guidance two years out moved, whether the driver recurs, whether cash agrees with earnings, and whether the information changes the odds or only looks causal. The answer is a plain sentence with that evidence, never a label such as long-term, near-term or unclear; where the evidence does not settle it, the sentence says what would (`references/after-a-price-move.md`, long-term outlook test).
- **Facts kept apart from opinions.** A filed contract or a published figure is a fact; a management claim, a sell-side view or an unnamed-source report is an opinion and is written as the speaker's claim. The company's own document is cited before the press (`references/downside-and-catalysts.md`, facts and opinions).
- **Price and estimates read together, when the question reaches the stock.** Price down with estimates down reads as a fundamental revision; price down with estimates flat as a multiple or positioning move; a move with no event behind it is called unexplained, not given a story.
- **Ranked by effect, not coverage.** The two or three events that matter are ordered by the size of their effect on a long-term driver, then by certainty (filed over press, announced over rumoured), never by headline count.
- **Regulatory and legal searched on their own, and a long window searched month by month.** One search across a long span or a mixed topic returns thin coverage, and legal items get buried under earnings headlines.
- **A large one-day move is named, not explained here.** The line that makes a day's move worth naming is the smaller of twice the standard deviation of the stock's daily return against the index over the 60 trading days before the window and 10 percent against the index, because a quiet stock's 4 percent day can matter more than a volatile stock's 8 percent; the line itself stays in the working, and the page says only which days moved, by how much against the index, and on what news. Explaining the move is a stock-move note's work.
- **The sector's own drivers.** Banks and insurers are read through net interest margin, provisions, capital, the combined ratio and reserves rather than sales and operating margin; a conglomerate's event is sized against the segment it hits, not the group; a loss-making company's events mostly move cash runway, with the funding it rests on stated once. `references/sector-primers.md` has each sector's decisive metrics.

## Where it goes wrong

- **A part the user named, left out.** When the question asks for operations, the stock or a competitor, that part gets its own section by that name, and an event list does not stand in for it; operations means how the business ran over the window (volumes, pricing, margins, capacity, supply), not only what was announced.
- **Citations assembled at the end.** The link goes next to the fact when the fact is captured.
- **Unlike figures compared.** A new yield set against an old coupon misstates the change; compare a yield with a yield, a mean with a mean, and one provider with the same provider.
- **A target change measured across two providers.** Start and end figures come from the same source, or the note says the change cannot be measured.
- **A worst case presented as the size.** A size built on the worst rate for the whole amount is called an upper bound in the sentence.
- **An event with no direction.** An event that matters says which way it moves its driver, or what would settle the direction.
- **An unconfirmed date given as fixed.** A date the company has not confirmed is called provisional.
- **A gap declared too early.** Contract values, fines and maturities are often in filings and news even when no structured field carries them; search before stating a gap.

## What the data has, and does not

Consensus, targets and rating counts are a current snapshot with a date and no history, so the start-of-window figures come from research and news dated near the start of the window, quoted with that date; when none is found, the note says so. The quote carries standard windows only; a move over the exact window, the stock's typical daily range and the index over the same days need the daily series. Five fiscal periods per pull, annual when years are wanted, which allows a three-year figure for the return on new investment and nothing longer. The corporate calendar carries earnings dates, conferences, IPOs and delistings only, so pending rulings, deal votes and court dates come from filings and news. Sentiment has no window: say which period its narrative covers and whether it matches the brief's. A private company has no price, estimates or targets; listing status comes from the lookup, and the brief is written from documents and says so at the top.

## Write

`references/output-standard.md` holds the rules. The title carries the window and the finding in one line ("Pfizer, October: the patent ruling matters more than the guidance cut"). The opening gives the two or three events that matter and what each moves, whether they change the outlook beyond the next year, what the price and the estimates did over the window, and the next date. The body follows the question: the parts the user named come first, in the user's order, under their names. Where the question names no parts, a paragraph on each event that matters with what would confirm or contradict its effect; what the price, consensus and targets did over the window; and what peers, suppliers, customers or regulators did that bears on the company, with at least one source about a company other than the subject, because a brief built only from the company's own news misses what changes its position. Categories searched with nothing found go in one line. The next dates and what each decides close the note. Sub-headings state the finding ("The ruling removes the main generic threat until 2029"), never the step.

## Before sending

- The user's parts are answered in the user's order, each under its own name, and every table on the page is one the reader needed.
- Every event that matters says in a sentence what it moves, which way, and by how much or through what mechanism, and whether its effect reaches beyond the next year; no event carries a label or a bolded category.
- Start-of-window consensus and targets carry a document date and come from the same source as the end figure, or the note says none was found.
- Every number in the opening agrees with the figure in the body.
- Every code name or internal term (a drug code, a project name, a contract term) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
