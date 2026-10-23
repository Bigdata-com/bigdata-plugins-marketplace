# Working with Bigdata.com

Guidance for using the Bigdata.com tools well. It describes approaches, not arguments: each tool's own description is the authority on what it takes and returns, so read it before the first call. Tool names below are the base names; a host may add a prefix to them.

Use judgment. A one-line question needs one or two calls. A research task needs a plan, several calls, and a second look when the first results leave a gap.

## Which data answers which question

| The question is about | Start with | Notes |
|---|---|---|
| What happened, what was said, why something moved | `bigdata_search` | News, filings, transcripts, broker research, podcasts, expert interviews and the user's own documents. Returns cited excerpts. |
| One company's numbers: financials, estimates, ratings, price targets, ownership | `bigdata_company_tearsheet` | Needs the company resolved first. Works for private companies too, with different content. |
| How the media sees a company, and why | `bigdata_sentiment_tearsheet` | Score, attention and a cited narrative. |
| Several companies at a glance: price, daily move, earnings surprise, targets, sentiment | `bigdata_portfolio_tearsheet` | One row per company. Then write a short read of the movers. |
| News across a list of companies | `bigdata_watchlist_search` | Gives every name its share of results. A plain search lets the most-covered names crowd out the rest. |
| Markets today: indexes, sectors, commodities, rates, currencies, crypto, factors | `bigdata_market_tearsheet` | One call covers all of it. |
| One country's economy | `bigdata_country_tearsheet` | Growth, inflation, rates, indices, currency, and a G7 comparison. |
| An ETF | `bigdata_etf_tearsheet` | Needs the ETF resolved first. |
| What is coming up: earnings dates, conferences, IPOs, economic releases | `bigdata_events_calendar` | Company events and economic releases are two different calendars. |
| Companies that match criteria the user describes | `bigdata_screen_companies` | Then use the portfolio tearsheet for current figures. |
| Credit risk signals | `bigdata_get_credit_factor`, `bigdata_screen_credit_factor` | One company, or a ranking across many. |
| A calculation, a series, a chart | `bigdata_computer` | Compute rather than doing arithmetic by hand. |
| The user's own documents and feeds | `bigdata_list_connectors`, `bigdata_list_tags`, `bigdata_list_documents` | Discover what they have, then search or read it. |
| Which publications Bigdata.com covers | `bigdata_find_sources` | For "do you cover the FT?" and for source filters. |
| The user's subscription and data packages | `bigdata_help` | |

Most tasks combine two or three of these: numbers from a tearsheet, the story behind them from search, the next event from the calendar.

## Resolve the company first

- Resolve every company, ticker, ETF or fund to its Bigdata.com entity before calling a tool that needs an entity id: tearsheets, the calendar, watchlists, fast searches with entity filters. Use `find_securities` for names and tickers, `get_securities` for ISIN, CUSIP, SEDOL or exchange listings, and `find_entities` for people, places, products and organizations that are not companies.
- Resolve several names in parallel, one call each.
- Take whether a company is public or private from the lookup result, never from training knowledge.
- If the top match is not clearly the company the user meant, look at the other matches, then ask.
- Resolve once. Reuse ids already confirmed in the conversation.
- A smart search resolves company names itself, so a lookup only to prepare a search is not needed.

## Search well

- **One topic, one period, one group of companies per search.** A combined query shares a fixed number of excerpts across everything it asks, so each part comes back thin. "Nvidia earnings and partnerships in 2024 and 2025" is four searches.
- **Write the query as a sentence,** not a list of keywords: "What did Nike say about inventory on its latest earnings call?"
- **Keep the user's time words.** "Last quarter", "yesterday", "FY2024" go into the query as said. Do not add dates the user or the results did not give.
- **List the angles first.** For a broad question, plan one search per angle. One relevant-looking result is not a reason to stop.
- **Pass a scope hint only when the user gave one:** their own files, a source, a tag, a broker.
- **The open web is a last resort,** for things outside Bigdata.com's content (a product page, a blog), and the user is told when an answer comes from it. News is not one of them.

## When a smart search comes back weak

Smart search reports how it read the query: the entity, period, source type and document type it chose, and how many excerpts matched. Read that report before retrying.

- **It read the query wrong** (wrong company, wrong period, wrong document type): run another smart search with a clearer query.
- **It read the query right, but the excerpts are empty, thin or off-topic:** retry in fast mode with the filters the report gives, and change only the query text. Simplify the wording, or phrase it the way the document would ("guidance" rather than "fiscal Q1 2026 outlook"). This keeps the retry on the right company, period and source instead of drifting.
- Prefer this smart-to-fast retry over a second smart search whenever the report already has the right filters.

## When to read the full document

A search returns ranked excerpts, not whole documents. Fetch the full document, with an id a search returned, when:

- the user asks for a document itself ("summarize the 10-K", "what did the CFO say in Q&A"),
- the answer depends on context the excerpts cut off (a table, a guidance range, a risk factor's full wording),
- one document carries the task (an earnings call for a digest, a filing for a risk review).

Do not fetch documents to answer what excerpts already answer. Never invent a document id or a URL.

## Lists of companies

When the user names companies they own or follow, resolve them all, then use the portfolio tearsheet for numbers and the watchlist search for news. When they refer to a saved list ("my watchlist", "my holdings"), load it rather than asking them to name the companies again.

## Saving to the user's Bigdata.com account

Saving changes the user's account, so offer it in one line and act only on a clear yes. Each fits a different moment:

- **A watchlist,** when the user named companies they own or follow. Later runs can start from it instead of the user listing the names again.
- **A monitor,** when the user wants to hear when something changes on a subject. Offer a test run on past data before turning it on.
- **The deliverable,** after a substantial one (a memo, brief, preview, comparison or screen), so later searches can find it. Not after a quick answer. Tell the user it becomes searchable once processed, not at once.

## When a tool returns an error

Read it. Most errors name the argument that was wrong; fix it and retry once. If it fails again, tell the user what could not be retrieved.

## The company tearsheet in detail

The company tearsheet is large. Ask for the sections the task needs with the tool's `sections` argument (its values are listed below), and split a full pull into two or three calls so no response is too big to use. The `interval` argument chooses five quarters (the default) or five fiscal years of statements; there is no period offset, so ten years of statements is not available from this tool.

| Section value | What it carries |
|---|---|
| `company_overview` | Profile, description, the real-time quote and price performance (52-week range, moving averages, price changes over standard windows) |
| `c_level_leadership` | Executives, board composition, management stats (needs FactSet access) |
| `financial_statements` | FactSet income statement, balance sheet and cash flow for five periods, with stock-based compensation split out, gross and net PP&E, goodwill and intangibles, invested capital, capex, buybacks, dividends |
| `financial_ratios` | Gross margin, P/E, P/B, debt ratios, ROIC, ROE, cash conversion cycle, Altman Z, Piotroski (trailing twelve months) |
| `key_metrics` | Market cap, enterprise value, EV/EBITDA, free cash flow yield, net debt (trailing twelve months) |
| `analyst_estimates` | Consensus for sales, EBIT, EBITDA, EPS, free cash flow, capex and long-term growth, with the actual where reported, the surprise in percent, and the company's guidance (low, mid, high) where the company gives it |
| `analyst_ratings` | Rating counts and price targets (consensus, median, high, low) |
| `latest_earnings` | The last reported quarter against consensus |
| `earnings_calendar` | The next earnings date |
| `revenue_segmentation` | Revenue by product and by geography |
| `fund_trends_history` | 13F holders, top buyers and sellers, position changes, options activity |
| `dividends`, `esg_performance`, `hiring_trends`, `mergers_acquisitions` | As named; M&A needs FactSet access |

The tool's own description says to omit `sections` for a general tearsheet request. A skill that needs three sections for a specific step is such a request: pass them.

Rules that follow from the data:

- Five periods come back per call, quarterly or annual by `interval`. For a ten-year view, use the annual statements and say in the Gaps line that the series stops at five years.
- The FactSet ROIC field and a hand-built ROIC differ by definition (tax rate, goodwill, leases). Say which one the report quotes and never mix them in one table.
- Not in Bigdata.com: a cost of capital or WACC, short interest, options data, intraday prices. State the cost of capital as an assumption with its basis and show a sensitivity. Say in the Gaps line when positioning data would have mattered.
- Consensus has a vintage: the date in the estimates section. Quote it next to any consensus figure, with the number of estimates when given.
- Price series and anything that needs more than a few steps of arithmetic go through `bigdata_computer`.

## Transcripts and guidance

- Guidance for the next quarter is given on the call for the quarter just reported. To read the guidance for Q1 FY2027, fetch the Q4 FY2026 call, never a later one. A smart search that resolves to a call that has not happened yet has read the period wrong; retry in fast mode with the reporting period filter set to the quarter of the call you need (fiscal year and quarter).
- Quote guidance verbatim with its range and the date of the call, then the consensus next to it.
- Research notes and news carry sell-side reactions (target changes, rating changes, the reasons). Until broker research is available in the account, search for those when a skill needs the Street's view, and label them as press or research summaries.
- Use `reporting_periods` (fiscal year and fiscal quarter) with a `document_type` of TRANSCRIPT and subtype EARNINGS_CALL on fast searches, so the period is fixed rather than inferred; the `sections` filter picks the prepared remarks (MANAGEMENT-DISCUSSION) or the Q&A (QUESTION-ANSWER).

## The skill slug

Pass `plugin_slug` with the skill's name on every Bigdata.com call that accepts it. It tells Bigdata.com which skill is running, which is how usage per skill is counted. The value is the skill's `name` field, for example `bigdata-earnings-preview`.
