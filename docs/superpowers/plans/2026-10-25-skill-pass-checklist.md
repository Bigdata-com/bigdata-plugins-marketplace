# Per-skill pass: checklist for the implementers

Scope: edit only `plugins/bigdata-com/skills/<skill>/SKILL.md` for the skills in your group. Do not edit anything under `references/` or `library/` (the library was fixed already and is synced into every skill; read it, do not write it). Do not touch the frontmatter `description` (rewritten already) or `name`. You may edit `metadata.bigdata-refs` only to add a library file a body now needs (then say so in your report; the sync will copy it).

Read first, in this order: `plugins/bigdata-com/library/working-with-bigdata.md` (tool realities, corrected), `plugins/bigdata-com/library/output-standard.md` (reader, section names, table width), and for each skill the method files its body cites (they live in the skill's `references/`).

Finance rules now in the library that the bodies must match (do not re-derive them; cite the file):

- Steady-state value = normalised NOPAT / cost of capital; excess cash is added once, in the equity bridge (expectations.md formula block 1).
- Capex = change in net PP&E + depreciation; net investment = change in net PP&E (valuation.md step 6).
- Stock compensation is already inside net income; never deduct it again and never add it back (earnings-quality.md formula 8).
- ROIIC: the value-trigger test uses a three-year rolling ROIIC, labelled; a single year is never evidence; drop any "never compare ROIIC with the cost of capital" wording and any "ROIIC over five years" (five annual periods allow three-year rolling at most) (roic.md, expectations.md block 4).
- Operating cash allowance: 2 percent of sales, 5 percent for less predictable companies (roic.md step 6). Remove "2 to 4 percent" and "2 to 5 percent".
- Credit: place the company on table 3 of credit.md (FFO/debt, debt/EBITDA) first, table 1 as cross-check, table 2 as order of magnitude; refinancing stress is formula 6a.
- Cost of capital: the WACC from valuation.md when loaded; otherwise cost of equity = government yield + beta x equity risk premium, WACC with after-tax cost of debt (expectations.md inputs table).

Generic checklist, every skill:

1. "Before starting": replace the three-way prohibition sentence pair ("Do not answer from memory or the web instead ... do not fall back to web search." or the skill's variant) with one sentence: "Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data." Keep the other bullets.
2. Tearsheet calls: `interval` annual wherever fiscal years are wanted; split a pull into calls of two or three sections; never request `company_overview` twice; drop a section the Analyse steps never use (for example `analyst_ratings`, `latest_earnings`, `hiring_trends` where unused). The tearsheet returns five periods at most: delete every "ten years", "five and ten years ago", "eight quarters", "ROIIC over five years", and size the step to what five annual periods allow (three-year rolling ROIIC, four accrual years). Where the step needs older history, say the series stops at five years in Gaps; do not add filing-fetch steps.
3. No consensus or target history exists in the tearsheet. Every "30-day change", "before and after", "13-week revisions", "90-day change" step uses one route: a `bigdata_search` of research and news for the period that quotes the figure, with the document's date, labelled "press or research summary", or the step marks it not found. Write that route into the step and into the table's Basis.
4. `latest_earnings` is one quarter. For a beat or guidance record, use the actuals in `analyst_estimates` where given, else a search for the prior two to four prints, and say how many quarters were found.
5. `bigdata_sentiment_tearsheet` takes no window: delete "for the last 30 days", "90 days" and similar; say which period its narrative covers.
6. `bigdata_events_calendar` (corporate) carries earnings, conferences, IPOs and delistings only. Deal votes, court dates, regulatory deadlines, product events come from filings and news via search. Fix any step that expects the calendar to give them.
7. `bigdata_get_credit_factor` and `bigdata_screen_credit_factor` return credit-news catalysts (event type, score, direction), never prices, yields, spreads or ratios. Fix any step that uses them otherwise.
8. `fund_trends_history`: 13F holders and options activity, quarterly and lagged; it cannot name who sold on a given day. Options prices and short interest are not in Bigdata.com; say so where positioning matters.
9. `bigdata_portfolio_tearsheet`: request surprise, targets and sentiment columns only when the template uses them (they cap the grid at 100 names).
10. A move over a specific window (an event day, the week before a print) comes from `bigdata_computer` on the daily series, for the stock and the index; `company_overview` gives standard windows only.
11. Output standard: rename "## What would change this view" to "## What would change this reading", or to "## What to watch" in a report that states it gives no view (brief, watchlist, market wrap). Cap every template table at eight columns: where Basis and Source columns push past eight, replace them with one "Basis and sources" note line under the table. Remove any instruction to print "(verify)" in the deliverable; dated figures are quoted with source and period and called historical.
12. Duplication: where the body restates a formula, a list or a step that a reference file already carries word for word, replace the restatement with the step or formula number in that file plus the body's own done condition. Keep the body's order, scope, gather steps, done conditions and anything that exists only in the body.
13. Reader: `output-standard.md` now names corporate strategy, finance and IR readers. Where the skill's subject can be the user's own company, a competitor, a customer, a supplier or a target, add one sentence in "Scope the request" that says so and tells the model to write the implications for that reader; keep the no-call rule. Where a template section only makes sense for a holder ("the holding has lost badly", "assume a long holder", "before committing capital"), reword it for any reader.
14. Sector primer: wherever `references/sector-primers.md` is cited, use this form: "Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) and read <the named subsections>."
15. Hand-offs: keep; add a hand-off where the per-skill list below names one.
16. Done conditions: every step ends on a checkable condition; sharpen the ones the list below names.

Per-skill items (apply all unless you can show one is wrong; if you skip one, say which and why):

## Group A

bigdata (entry skill)
- `references/skill-builder.md` and `README.md` point at `assets/report-template.md`, which does not exist. Change both pointers to `references/output-standard.md` (its frame and footer are the template); remove the README's listing of the missing file and add `references/output-standard.md` to it.
- Line about "broker research ... with citations" in the capabilities answer: say "research notes and news that quote sell-side views, and broker research where the account has it".
- Interview goal options: add "benchmark our company against competitors", "prepare for investors (IR)" and "diligence on a company or a target" to the goal list, so a corporate user is not forced into an investor framing.
- "read that skill and follow its method": change to "load that skill through the host; if the host cannot, follow this skill's own method and say so".

bigdata-company-brief
- Items 3 and 10 of the generic list (revision history, event-window move via `bigdata_computer` and the market tearsheet for the index).
- Formula 4 of expectations.md is defined on ROIIC: use the three-year rolling ROIIC where five annual periods allow it, else say the FactSet average ROIC is a proxy, labelled.
- Replace the fixed "10 percent against the index" materiality flag with: a one-day move outside the stock's own typical range (derived from the daily series) or 10 percent against the index, whichever is smaller for that stock; the 10 percent threshold stays only as the base-rate table boundary.
- "What would change this view" becomes "What to watch" (the brief gives no view). Events table to eight columns.
- Scope: the subject may be a competitor, customer, supplier or the user's own company; write the implications for that reader.

bigdata-watchlist
- Items 3, 5, 9, 11 of the generic list. The revision drill-down uses the search route or is marked not found.
- The incremental-return test is too heavy for a daily check: drop it; for a flagged name, fetch `financial_ratios, key_metrics` only if the user asks for the fundamentals.
- Flag threshold: scale to each stock's own daily range from the portfolio tearsheet's move and the index, not a fixed 10 percent.
- `bigdata_watchlist_search` asks not to render its documents as a numbered list under Sources: cite its items inline in the news column with the tool's own link format, and keep the report's Sources section for the other documents; say so in the Write section.
- Table to eight columns; "What to watch".
- Scope: a peer group or competitor set is a valid list; say so.

bigdata-markets-today
- Breadth: the market tearsheet has no equal-weight index or advance-decline data. Replace the breadth step with: the share of sectors up versus down, the dispersion between the best and worst sector, and the Russell 2000 against the S&P 500 as a size read (say it is size, not breadth); drop the Dow.
- Factor ETF rows are relative to the S&P 500: say so in the step and in the table.
- Rates: the tearsheet carries US Treasuries only; non-US yields come from search or go in Gaps.
- Past dates: the tearsheet is a snapshot; "how did markets do last Tuesday" uses `bigdata_computer` on the index series and search for the news, and the skill says so.
- VIX change in points is derived; label it.
- "What to watch" instead of "What would change this view".

bigdata-catalysts
- Item 3 (revisions).
- Merger-spread probability: point at `references/special-situations-arithmetic.md` formula 2 (now with carry) or hand off to bigdata-special-situations; do not keep the bare formula.
- "the sector's own event types from the sector section": point at the primer's "What to watch at the macro level" and "Questions for the earnings call" subsections with the grep form.
- Ranked table to eight columns; the twelve-column version becomes a table plus a note.

bigdata-quick-take
- Add one relative-valuation line: forward P/E and EV/EBITDA against the peers in `company_overview`'s competitors block (one `bigdata_portfolio_tearsheet` call), so "what the price implies" is not only the steady-state P/E; allow a fifth call when the user asks for a peer angle.
- Say that implied growth rests on the assumed incremental return, in the table's Basis.
- Items 3 and 5 (revisions, sentiment); split the tearsheet pull in two.
- Use the downside line and the next catalyst from `references/downside-and-catalysts.md` as that file's own guidance for quick-take says.
- The base-rate sentence uses the three-year class, not the one-year column.

bigdata-earnings-preview
- Items 2, 3, 4 (quarters of history via actuals or search, say how many found).
- Add the walk-down logic to the probabilities step: most companies beat a consensus that was cut into the print, so the reaction turns on the size of the beat against the typical beat and on the guide against next-period consensus, not on beat or miss alone; cite the company's own record where found.
- Reorder "The setup": the bar for the quarter first (consensus against the guide, the revisions found, the run into the print), then the reverse-DCF figures.
- Add the typical earnings-day move: `bigdata_computer` on the daily series around the last four print dates found in search.
- Base rates: the three-year class, not one-year; do not make a base rate mandatory for every growth figure.
- Positioning: request `fund_trends_history` and say options prices and short interest are not available.
- "Questions for the call" points at the primer's "Questions for the earnings call" subsection.

bigdata-earnings-review
- Items 2, 3, 4.
- Surprise decomposition only from disclosed segments or the company's own bridge; otherwise state that the split is not available, never estimate it.
- Add a "Peer read-across" section: what the print says for competitors, suppliers and customers, and what they said about it, from search.
- Thesis check: when the user holds no thesis (a corporate or IR reader, a competitor's print), run "how the Street received it" (revisions found, target changes, rating changes) in its place.
- Table the before-and-after consensus once, not twice.
- Short form: reaction note keeps "What happened", "Results", "Guidance", "Market reaction", "Next date" and sources.
- Compare the language with the prior call (both transcripts are fetched): metrics dropped, claims dropped, tone in the Q&A.

## Group B

bigdata-deep-dive
- Item 2 throughout (five annual periods; three-year ROIIC; four accrual years; delete the ten-year check and the ten-year done condition).
- Capital allocation step: the statements carry buybacks, dividends and issuance by year; use them with the year-average price from `bigdata_computer` for the buyback test, and point at bigdata-capital-allocation for the full treatment; drop "what the proxy pays management for" unless a proxy search is added.
- Catalysts: add a `bigdata_events_calendar` call and a search for dated non-calendar events.
- Add a premortem (forecasting-discipline.md rule 3) before the kill criteria.
- Private companies: accept them (the tearsheet works with different content); say which figures are missing; remove the refusal.
- Scope: a competitor profile or a due-diligence read is a valid use; write for that reader; remove the "long idea, short idea" framing as the only options.
- "The answer first" prose length: match output-standard (four to eight sentences).
- Drop the duplicate `company_overview` request; add a search fallback for `c_level_leadership` and `mergers_acquisitions` (FactSet-only); drop `hiring_trends` unless a step uses it.
- Sharpen "Done when the controversies are listed" and "Done when a reader can see where the profit comes from".
- Hand-offs: add comps, scenarios, earnings-quality, capital-allocation, risk, credit.

bigdata-thesis
- Value per share needs the equity bridge: add `valuation` to `bigdata-refs` and bridge from EV with net debt, minorities, pensions, leases and options as valuation.md step 10 sets out.
- Template order: "Downside first" before the claims table, as the check demands.
- ROIIC wording per the library rule.
- Item 3 (revisions). 13F: `fund_trends_history` position changes are quarterly; label.
- Private names: deep-dive now accepts them; keep the route.
- Forecast record and Brier scale: move out of the deliverable into the monitor offer (optional for the user).
- Scope: "what is the bull and bear case on us" from an IR reader is a valid request; write for that reader.

bigdata-valuation
- Net capex wording; steady-state wording; operating cash 2 or 5 percent; ROIIC three-year.
- Reorder: build the WACC (current step 3) and ROIIC (step 2) before the reverse DCF (step 1), so one discount rate runs through the report.
- Horizon by maturity and visibility (valuation.md step 4); do not bound it with the market-implied advantage period (circular); quote the implied period as a comparison only.
- Peer cross-check runs the multiples steps including selection (step 7).
- Length: "two to four pages" cannot hold eleven sections; either cut the template to the sections the user needs or state four to six pages.
- Dedupe (item 12): steps 3, 6, 8, 9, 10 and the special cases restate valuation.md; point at its step numbers.
- Hand-off to bigdata-deal-analysis when the subject is a target.

bigdata-comps
- Peer EV: `key_metrics` EV plus the statements for debt, cash, minorities; pensions, leases and options from the statements where present, else noted as not adjusted for peers; one basis for all.
- Clean the target and every peer on the same items, or compare reported figures for all and say so.
- Driver test: the portfolio tearsheet does not carry growth, margin, ROIC and capital intensity; use `financial_ratios, key_metrics` per peer for six to ten peers (two calls each) or the competitors block plus one search for the rest.
- ROIC basis: FactSet for all, with the goodwill treatment stated as unknown.
- Add an IFRS 16 versus US GAAP check before comparing EBITDA multiples; P/E only with a leverage check.
- ROIIC three-year rolling in the implied-growth step.
- The risk component of the premium decomposition is the unexplained remainder; say so.
- Corporate mode: when the user is IR or strategy, deliver the operating benchmark table (growth, margins, returns, cash conversion, total shareholder return) with the multiples as a second section.
- Dedupe (item 12) the passages restating multiples-and-peers.md; drop `analyst_ratings` if unused; header carries the newest-document date.

bigdata-scenarios
- Default horizon: explicit years to the company's maturity (five to seven, valuation.md step 4), fading after, not three; fix the "beyond year three" blend line.
- Data window five annual periods.
- The price-implied downside weight: hold the base-to-upside ratio fixed and solve for the downside weight; say so.
- ROIIC rule; the narrow route uses the user's own shock size; drop the hazard-window sentence.
- Dedupe the special cases.

bigdata-earnings-quality
- Step on steady-state free cash flow: match formula 8 (no SBC deduction; say SBC stays inside net income).
- Accrual series over four years; LTM from a second call with quarterly `interval`, not a 10-Q fetch.
- Severity scale: rename level 4 to "evidence of misstatement" so the check that bans "manipulation" holds, or allow the word only in the scale definition.
- Tax test: the rate reconciliation and cash against book tax, not only expense over statutory rate.
- Clarify per-flag levels against the company state in table 3; drop unused `latest_earnings` and `earnings_calendar`.
- Dedupe (item 12): steps 2 to 10, the flag list and step 12 restate earnings-quality.md; point at its step and formula numbers; keep step 14 and the done conditions.

bigdata-moat
- Profit-pool history over five annual periods for the company and the peers (interval annual), not ten.
- Duration: convert the persistence correlation to a half-life (half-life = period x ln 0.5 / ln r) and state the rule for combining the bounds (take the shortest well-supported one); the market-implied period is a comparison, never a bound on the fundamental estimate.
- Peer hiring: request `hiring_trends` for rivals if the step uses it, else drop the step.
- Dedupe (item 12) the passages restating industry-structure.md.
- Sharpen "Done when one verdict is written with its evidence".

bigdata-capital-allocation
- ROIIC: three-year rolling for the trigger; remove the self-contradiction with the checklist line.
- Value at each buyback date: use the steady-state value plus future value creation with the competitive advantage period stated as an assumption, or compare the price paid with the valuation range available at the time; label the method; never claim an observed advantage period.
- ROIIC five-year becomes three-year in the table.
- Peers: resolve two to four from the competitors block and pull `key_metrics, financial_statements` for payout, yield and leverage; the comparison table then has a peer median.
- Corporate decision: a user asking "buy back or raise the dividend" gets the arithmetic for each option side by side (output-standard allows it).
- Ratings: table 3 first, then table 1.
- Add the utilities special case the body promises; add a search fallback for FactSet-only sections; drop `analyst_estimates` if unused.
- Dedupe (item 12) the passages restating capital-allocation.md.

bigdata-risk
- Value each broken driver alone in the value-driver formula; keep the stressed cash-flow value as the floor for the whole company, not as the per-driver method.
- Add `bigdata_events_calendar` to Gather for the kill-criteria dates.
- Reader: any reader (holder, supplier, acquirer, lender); remove "assume a long holder" and "the holding has lost badly".
- Ratings: table 3 first.
- Dedupe the passages restating downside-and-catalysts.md and credit.md; drop `analyst_ratings` if unused.

## Group C

bigdata-deal-analysis
- Scope: add a hypothetical deal ("what would it cost us to buy X") and a third-party reading ("what does X buying Y mean for us as a rival, customer or supplier"), each with its own short template section.
- Regulatory step: compute combined share and the HHI change from `references/industry-structure.md` (now in the skill's references) with the 2023 US merger guideline presumptions quoted as thresholds (HHI above 1,800 with a change above 100, or combined share above 30 percent), labelled.
- Break price: compute it here from `references/special-situations-arithmetic.md` formula 2 and hand off the spread trade to bigdata-special-situations; remove the contradiction.
- Separate the probability that synergies are realised from the probability the deal completes (regulatory, vote, financing, topping bid), and weight outcomes with both.
- Precedent transactions stay a primary cross-check; the circularity warning applies to DCF exit multiples only.
- Add the tax structure to the terms list (stock or asset purchase, tax-free reorganisation, step-up).
- Stock deals: the predicted acquirer move uses the acquirer's price change times shares issued, not the cash formula alone.
- Archetypes: cite the 5th edition's five and note that the 7th edition adds a sixth.
- `interval` annual.

bigdata-screen
- Rank on the user's criteria; the gross-profitability, ROIC and margin ranking is the default only when the user names none, and sector-specific metrics from the primer replace it for REITs (FFO, AFFO), utilities (allowed return, rate base growth), producers (reserves, breakeven), banks and insurers.
- Corporate scopes: acquisition targets, competitors, suppliers; say up front that the screener covers listed companies on the exchanges it lists and that private names come from `find_securities` and search.
- Use the tearsheet's competitors block for "companies like X" before the screener.
- Request the grid's surprise, target and sentiment columns only when the template uses them.
- Second stage: "the 20 to 40 nearest the criteria" becomes the top N on the user's primary criterion, N stated; two calls per name with `interval` annual.
- Note that base-rate sector names differ from the screener's and map them explicitly.

bigdata-sector
- Scope: a subject-company slot ("my company", "where does X sit") and a template section "Where <company> sits" (share, margin, return and multiple against the sub-industry).
- "Which sectors look interesting": use the market tearsheet sector rows and one screener aggregate per sector to rank three or four sectors by the drivers, then run the primer for those only; never twelve deep runs.
- Geography: default to the user's market or global, with the screener's exchange coverage stated; align with bigdata-theme.
- Profit pool over five annual periods (interval annual), not ten; delete "where the tool allows".
- Banks: profit-pool width in equity, not invested capital.
- Grid columns only when used.
- Boundary with bigdata-moat in the "Not for" sense of the body: moat is one company, sector is the industry.

bigdata-theme
- Scope: a subject-company slot ("how exposed are we", "how exposed is X") and an exposure line for it in the template.
- Screener coverage (its listed exchanges) stated; non-US names added through `find_securities` and search; ETF holdings are top ten only, say so.
- Rarity: share above threshold from the base-rate tables, not a z-score.
- Calls split, `interval` annual for segment history; grid columns only when used.
- Deliver an exposure list with no weights; make Check 9 and the template agree.

bigdata-country
- Add a compact macro method inside the body (no library file carries one): real policy rate (policy rate less inflation) against a stated neutral range; debt dynamics (interest rate less growth, the primary balance that stabilises debt); external position (current account, reserves in months of imports and against short-term external debt); a country risk premium route (sovereign spread or rating-based default spread, scaled by the equity-to-bond volatility ratio, Damodaran's approach, labelled assumed); every figure's source is the tearsheet or a dated search result.
- Separate nominal from real in every rates and growth row.
- Probabilities: judgment with named historical analogues from the tearsheet and news; no invented base rates; say the loaded reference classes are equity ones.
- Corporate scope: market entry, FX exposure, supply-chain exposure to a country are valid requests; write for that reader.
- Merge the tagging section into the body's tags (one place).

bigdata-macro-compare
- Add real rates (policy and 10-year less inflation), net debt and interest to revenue where available, and the r minus g debt dynamics to the comparison; fiscal ratios from search when the tearsheet lacks them, dated.
- Same-moment rule: non-US yields come from search at mixed dates; flag it.
- Exposure to the common shock: trade openness, commodity balance and external financing need from search, with figures.
- Probabilities as judgment with analogues.
- Corporate scope: where to expand, source or hedge.
