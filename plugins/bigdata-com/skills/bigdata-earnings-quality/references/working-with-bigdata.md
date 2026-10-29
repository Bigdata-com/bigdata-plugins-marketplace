# Working with Bigdata.com

The skills state what a step needs in data terms; this file maps those needs to the Bigdata.com tools and records what the data cannot do. Each tool's own description decides the arguments, so read it before the first call. Tool names below are base names; a host may add a prefix, and an account may not carry every tool. Carry the attribution URL with every fact as you take it, so the report can cite inline.

## Which data answers which question

| The question is about | Start with | Data fact |
|---|---|---|
| What happened, what was said, why something moved | `bigdata_search` | Cited excerpts from news, filings, transcripts, research and the user's documents |
| One company's numbers: financials, estimates, ratings, targets, ownership | `bigdata_company_tearsheet` | Needs the company resolved first |
| How the media sees a company | `bigdata_sentiment_tearsheet` | No window can be set; say which period it covers |
| Several companies at a glance | `bigdata_portfolio_tearsheet` | One row per company |
| News across a list of companies | `bigdata_watchlist_search` | Every name gets its share of results |
| Markets today: indexes, sectors, commodities, rates, currencies, crypto, factors | `bigdata_market_tearsheet` | One call covers all of it |
| One country's economy | `bigdata_country_tearsheet` | Growth, inflation, rates, indices, currency, G7 comparison |
| An ETF | `bigdata_etf_tearsheet` | Needs the ETF resolved first |
| Upcoming earnings, conferences, IPOs, delistings, economic releases | `bigdata_events_calendar` | Four corporate event types only; deal votes, court dates, regulatory deadlines and product events come from filings and news |
| Companies matching criteria | `bigdata_screen_companies` | Then the portfolio tearsheet for current figures |
| Credit news signals | `bigdata_get_credit_factor`, `bigdata_screen_credit_factor` | Scores and catalysts, not prices, yields, spreads or ratios |
| A calculation, a series, a chart | `bigdata_computer` | It does the arithmetic |
| The user's own documents and feeds | `bigdata_list_connectors`, `bigdata_list_tags`, `bigdata_list_documents` | Discover, then search or read |
| Which publications are covered | `bigdata_find_sources` | |
| The user's subscription and data packages | `bigdata_help` | |

## Data needs the skills ask for, and how to meet them

| A skill step asks for | Route | Data fact |
|---|---|---|
| The company resolved, public or private | `find_securities`; `get_securities` for ISIN, CUSIP, SEDOL | Listing status comes from the lookup, never from memory |
| Five fiscal years of statements | Company tearsheet, financial statements | Five periods per pull; the default is quarters, so ask for annual when years are wanted; nothing older exists |
| Latest quarter against consensus | Company tearsheet, latest-earnings section | One quarter; earlier surprises are in the estimates actuals or search |
| Consensus, guidance fields, targets, ratings | Company tearsheet, estimates and ratings | A snapshot with its vintage, quoted next to any consensus figure; no revision history, so "what changed" comes from dated research and news, labelled as such |
| A transcript or release for a named quarter | Search with fiscal year, quarter and document type fixed, then fetch | The call for the quarter just reported carries next quarter's guidance; quote guidance verbatim with its range and date |
| The Street's revisions and reactions since a date | Search, one aspect per call | Until broker research is in the account, these come from research notes and news, labelled as such |
| Daily prices over a window, a beta, an abnormal return | The computing tool on the stock and its index | The overview has standard windows only; if the tool is missing, use those and dated reports and say so |
| Several companies' current figures | Portfolio tearsheet, one call | One row per company |
| Statements or ratios for a peer set | The computing tool over the set in one batch | Per-peer tearsheets are large |
| ROIC | Company tearsheet financial ratios | FactSet ROIC and a hand-built ROIC differ by definition; say which, never mix them |
| Price-implied growth, a DCF, a sensitivity grid | The computing tool or the host's code execution | Show the working |
| Market moves across indexes, rates, currencies | Market tearsheet for levels; the computing tool for a defined window | Multi-day columns run from its refresh time, not a Friday close; yield changes are percent of the yield, not basis points |
| Risk-free rate, inflation, policy rates | Country tearsheet | Take them from the data while the tool is there; an assumed yield is a Gaps item |
| Institutional positioning | Company tearsheet, fund-trends section | The 13F and options data is positioning, not prices |
| A cost of capital, short interest, an options-implied move, intraday prices, bond prices or spreads | No structured field. Search news and research documents, which often quote them with a date, and cite the document | A figure found nowhere is a Gaps item, not an assumption |
| The user's own documents | Connectors, tags, listing, then search or fetch | |

When a tool a step wants is missing, use the nearest route and name the substitution in the Gaps line. Never give a figure from memory or the open web without saying so. The tool names in this file are for the working; the report names documents and data sets, never tools.

## Large responses

Ask for two or three tearsheet sections per call; a saved response is read with a parser.

## Resolve the company first

- Resolve every name, ticker, ETF or fund before calling a tool that needs an entity id, in parallel, once; reuse confirmed ids. `find_entities` covers people, places and products.
- Listing status comes from the lookup, never from memory.
- If the top match is not clearly the company, ask.
- A smart search resolves names itself.
- A saved list ("my watchlist") is loaded, not re-asked.

## Search well

- One topic, one period, one group of companies per search, because excerpts are shared.
- Write a sentence, not keywords.
- Keep the user's time words as said; invent no dates.
- Plan one search per angle.
- Pass a scope hint only when the user gave one.
- The open web is a last resort, and the user is told.
- Fetch the full document only when the excerpts cut off what the work needs; never invent an id.
- Keep the link with the fact.

## The skill slug

Every call that accepts `plugin_slug` takes the running skill's `name` field, for example `bigdata-earnings-preview`.
Each skill states it once under "Before starting".
