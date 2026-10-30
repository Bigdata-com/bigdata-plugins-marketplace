# Requests for the Bigdata.com MCP tool descriptions (26 Oct 2026)

The skills now describe what data a step needs and let the tool descriptions decide the call. That only works if the descriptions carry the facts the skills used to hardcode. Each item below was a source of wrong calls or wrong claims in the 25 Oct audit or the 26 Oct quality evals. Wording is a suggestion; the fact is the request.

## bigdata_company_tearsheet

1. State the period rule in the first paragraph: "`financial_statements` returns five periods; `interval` is `quarter` by default or `annual`; there is no offset, so older periods are not available." Agents asking for "five years" without the argument got five quarters in eight skills.
2. Say that `analyst_estimates` is a current snapshot with a vintage date and no revision history, and that `analyst_ratings` carries no past targets. Seven skills asked for 30-day consensus changes the tool cannot give.
3. Say that `latest_earnings` covers one quarter, and that earlier quarters' surprises are in the actuals of `analyst_estimates` where present.
4. State the response size: a multi-section pull can exceed 100,000 characters (the full tearsheet reached 524,000 in one run), and recommend two or three sections per call for a step-by-step job. The current text says to omit `sections` for general requests, which conflicts with that.
5. Say that `fund_trends_history` includes institutional options activity (positioning), and that the tool carries no option prices, implied volatility, short interest, bond prices or spreads.
6. Say that the FactSet ROIC in `financial_ratios` uses FactSet's definition (cash in capital), so it is not comparable with a hand-built ROIC.

## bigdata_market_tearsheet

7. State what the change columns measure: the 5D, 1M and other columns run from the tool's refresh time, not from a Friday close, so they are not a calendar week. Both arms of the markets-wrap eval found the S&P 500 "5D" at -1.7% against an actual Friday-to-Friday -0.5% and rebuilt the week from daily series.
8. State that the Yields table's change columns are percent changes of the yield, not basis points.

## bigdata_sentiment_tearsheet

9. Say that no window can be set and what period the narrative covers.

## bigdata_events_calendar

10. State that the corporate calendar carries earnings, conferences, IPOs and delistings only (no deal votes, court dates, regulatory deadlines or product events), and that an unfiltered country pull is paginated and large.
11. The economic calendar's `period` field for quarterly GDP releases reads 2025-07-01 for Q3 2026 releases in two runs; check the field.

## bigdata_get_credit_factor and bigdata_screen_credit_factor

12. Say in the first sentence that they return credit-news catalysts and scores, not prices, yields, spreads or ratios. Two skills used them to look for bond prices.

## bigdata_computer

13. Say which series it holds: securities and ETFs, but not index levels, Treasury yields, currency pairs, the VIX or futures. Agents discovered this by trial. Say that it is the route for a defined price window, a beta or an abnormal return, and for batch pulls across a peer set (statements, estimates, ratios), which saves one large tearsheet per peer.
14. Say what happens when a user's account does not include it, so a skill can fall back (the skills now say: standard-window performance from the overview and dated reports).

## bigdata_search

15. Keep the one-aspect-per-call rule prominent; it holds. Add that a fast-mode search filtered to one filing can return zero chunks even when the filters are right, and that fetching the document is the fallback (seen on a 10-Q three times in one run).
16. Say that smart searches resolving to an entity id can pick the wrong entity for ambiguous names (TSMC resolved wrong once) and that the audit block shows which id was used.

## All tools

17. Make `plugin_slug` visible in every description that accepts it, with the sentence that it identifies the running skill for usage counting.
