# Brief for method-reference specs (Bigdata.com skills rewrite, 2026-10-23)

## What this is
Bigdata.com ships a plugin of financial research skills (SKILL.md folders) for Claude, ChatGPT and Microsoft Copilot. The skills call the Bigdata.com MCP tools (search over news, filings, transcripts, broker research; company tearsheets with FactSet fundamentals and estimates; events calendar; screens; watchlists). We are rewriting the skills. Each skill will load one or more shared "method reference" files when it needs a method. You are writing the SPEC for some of those method files: what the file must contain, in enough detail that a writer can produce the final file without re-reading the source papers.

## Quality bar
The reader of the finished skill output is a seasoned portfolio manager at a multi-strategy hedge fund. The method must be the one a top analyst would use, stated precisely, with formulas, definitions and reference tables. Rigorous first; the user can ask for a simpler version. No investment recommendations: skills describe the balance of evidence and what would change it, never Buy/Hold/Sell, never position sizing.

## Sources
Use ONLY the extraction notes in the folder given in your prompt (they summarise the Mauboussin papers, McKinsey Valuation 5th ed, Security Analysis 6th ed, Klarman Margin of Safety, Damodaran ROIC). Every number, table or threshold you include must carry its source (paper or book, year, and page or section if the note gives it). Do not add figures from memory. If the notes lack something the method needs, write "GAP:" and say what is missing.

## Bigdata.com data the method can draw on (so you can map inputs)
Company tearsheet (FactSet): 5 fiscal periods per call of income statement, balance sheet, cash flow (incl. stock-based comp split, PPE gross and net, goodwill and intangibles, invested capital, capex, buybacks, dividends, leases where reported); ratios (ROIC, ROE, margins, cash conversion cycle, Altman Z, Piotroski); key metrics (market cap, EV, EV/EBITDA, P/E, FCF yield, net debt); consensus estimates (about 100 metrics to FY+4: sales, EBIT, EBITDA, EPS, FCF, capex, long-term growth; with actuals, surprise %, and guidance where the company gives it); revenue segments (5 years, product and geography); analyst targets and ratings; price performance; 13F holders and fund trends; next earnings date; M&A history; executives; ESG; job postings. Not available: WACC, short interest, options data, intraday prices, daily price history beyond the tearsheet's performance fields (use bigdata_computer for price series and computations). Search returns cited chunks from news, filings, transcripts and broker research; full documents can be fetched.

## Format of each spec (markdown, 900 to 1,600 words per file)
1. Title and one-paragraph purpose: what question the method answers and which jobs use it.
2. Inputs: the data needed, mapped to the Bigdata.com fields above or to a search.
3. Procedure: numbered steps a model can follow and a reader can check. Each step ends with what "done" looks like.
4. Formulas: every formula written out with variables defined. Where a closed form exists, give it.
5. Reference tables: base rates, thresholds, typical ranges, with source and date. Mark time-sensitive figures "(verify)".
6. Interpretation rules: how to read the result, common errors, when the method does not apply (banks, cyclicals, early-stage, EM) and what to do instead.
7. Output lines: the specific sentences or table rows the skill should put in its report, with evidence type labelled as reported (from a document or dataset), derived (computed from reported data), assumed (an input the analyst chose) or judgment.
8. Sources: list of notes and the underlying papers or chapters used.

## Style rules
Plain prose, imperative mood for procedure steps, no emojis, no em dashes (use commas or "and"), no metaphors, no marketing adjectives. Say "verify" rather than inventing a current number. Use "the company" and "the ticker"; do not perform jargon. Do not write the skill itself; write the spec for the reference file.
