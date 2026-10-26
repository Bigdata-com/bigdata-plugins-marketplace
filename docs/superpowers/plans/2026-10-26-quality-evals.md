# Quality evals: with skill vs without, 26 October 2026

Ten skills from branch `skills-audit-fixes-2026-10-25`, one live prompt each, run twice by fresh opus agents (high effort): once reading the skill from the worktree and following it, once with no skill material at all. Both arms had the same Bigdata.com MCP tools and no web tools. Each report was graded by a sonnet agent against 11 to 13 fixed assertions (six generic: every fact sourced and dated, no unfinished-work markers, tables at most 8 columns, gaps stated, closes with what to watch, framed for the stated reader; the rest skill-specific). I read the credit, stock-move, valuation and deep-dive with-skill reports in full and used the graders' notes and the agents' run logs for the rest. Artefacts (gitignored): `plugins/bigdata-com/evals/quality-2026-10-26/`. Decisions D29 to D35 in `2026-10-25-decisions.md`.

## Prompts

Built from what Bigdata.com showed as live on 26 Oct 2026: Meta's negative free cash flow and the AI-debt scare, semis down 18% in three weeks, Brent at $115, the 10-year at 5%, JetBlue and Cable One credit stress, CoreWeave, data-centre power names, SpaceX reporting as a public company. Five in PM voice, five in corporate voice.

| Skill | Prompt (short) | Voice |
|---|---|---|
| company-brief | catch me up on CoreWeave, what it means for the stock | PM |
| stock-move | head of IR at Deckers: what drove the -7%, what the sell side says, brief the CEO | corporate |
| earnings-review | GM tier-1 supplier: review Q3 and the 2026 outlook, what to plan for | corporate |
| earnings-preview | Amazon reports Thursday: consensus vs guide, what is priced in, what to check first | PM |
| valuation | Nvidia after the sell-off: what the price implies, DCF, cheap or not | PM |
| credit | treasury counterparty check on Cable One after the B3 downgrade, 60-day terms | corporate |
| sector | semis after -18%: structure, profit pool, what is priced, where Lam sits | PM |
| theme | head of strategy at nVent: exposure vs peers, theme risk if capex slows | corporate |
| markets-today | last week's wrap across indexes, sectors, rates, currencies | PM |
| deep-dive | corporate venture team: due diligence on SpaceX before a connectivity contract | corporate |

Four prompts carried a false premise (Lam "cut guidance", GM "lowered" the 2026 outlook, Deckers "almost 7%", the 10-year "back near 5%"). Both arms corrected all four, up front.

## Scoreboard

| Skill | With skill | Without | Words with / without | Tokens (k) with / without | Minutes with / without |
|---|---|---|---|---|---|
| company-brief | 10/11 | 8/11 | 4,283 / 3,161 | 349 / 245 | 9.7 / 5.5 |
| stock-move | 11/12 | 10/12 | 3,354 / 4,330 | 338 / 232 | 10.2 / 8.2 |
| earnings-review | 11/11 | 10/11 | 5,053 / 4,324 | 364 / 265 | 10.6 / 6.2 |
| earnings-preview | 11/11 | 9/11 | 5,075 / 2,479 | 423 / 284 | 12.6 / 7.3 |
| valuation | 10/12 | 9/12 | 4,278 / 3,249 | 397 / 275 | 13.8 / 7.9 |
| credit | 13/13 | 12/13 | 5,238 / 4,360 | 322 / 265 | 10.5 / 9.1 |
| sector | 11/11 | 9/11 | 4,803 / 2,328 | 374 / 267 | 9.0 / 5.2 |
| theme | 11/11 | 7/11 | 4,740 / 3,195 | 490 / 294 | 11.4 / 5.1 |
| markets-today | 11/11 | 9/11 | 4,369 / 3,199 | 298 / 286 | 8.8 / 5.1 |
| deep-dive | 11/12 | 10/12 | 6,080 / 3,684 | 521 / 332 | 13.2 / 6.0 |
| **All** | **110/115 (96%)** | **93/115 (81%)** | **4,727 / 3,431** | **388 / 275** | **11.0 / 6.6** |

The skill arm won every pair. Tool calls: 64 per run with the skill, 37 without. Research tokens across the 20 runs: 6.6M (opus), plus 20 sonnet graders at about 90k each. Estimated cost from token counts, not billed: roughly $50 to $60.

What the baseline lost points on, consistently: facts without inline sources or dates (8 of 10), no Gaps section (5 of 10), no closing "what would change this" (2 of 10), valuation not anchored to the pre-move price (stock-move), no consensus-revision caveat (earnings-preview), weaker chain mechanism and no close (theme). The with-skill reports lost points on: company-brief items without an explicit bullish/bearish label, stock-move EPS consensus not quoted, valuation implied-growth arithmetic not shown and no positioning view, deep-dive tables of 9 columns.

## My read of the finance

- **credit (Cable One).** The rebuilt method shows: guarantor coverage and the missing-baskets note, instrument-by-instrument run-rate interest, a refinancing stress at 11% and 14% crossed with EBIT shocks, S&P's FFO/debt and debt/EBITDA buckets, recovery by layer at three enterprise values with the vendor's claim placed in the pool, preference-period and 20-day goods points, dated signposts. A credit analyst would accept it as a first-pass memo. One number does not reconcile (sources of $1.19bn against about $1.25bn from its own inputs). At 5,238 words it is long for a treasury team; the two-table answer at the top carries the decision.
- **stock-move (Deckers).** Valuation proxies measured at the pre-event $85.28, the large-drop studies labelled out of sample (the move was under 10%), its own miss sample built from peers, peers on the same day, before/after consensus with dates, a CEO briefing section. The reconciled rules from the 25 Oct rewrite held. Minor: EPS consensus not quoted, two small price inconsistencies.
- **valuation (Nvidia).** Formulas from the 25 Oct library fixes applied correctly (equity bridge adds excess cash once, capex = change in net PP&E + depreciation, three-year ROIIC labelled, continuing value with RONIC). The result is driven by a 13.9% WACC from a raw 60-month beta of 2.19, which puts even the bull case ($190) below the $211 price. The report shows the market-implied rate (9.2%) and a sensitivity grid, so the reader can see the lever, but a PM would reject the headline rate. The baseline made the opposite choice (beta 1.45, value $263) and was flagged for that too. The method file needs a beta sanity step.
- **deep-dive (SpaceX).** Listing status taken from find_securities, ROIC hand-built and reconciled to the financing side, segment economics, earnings-quality flags (related-party Boring Company gain, 90-day cancellable compute contracts, server lives, Valor sale-leaseback debt), three-case DCF with the high-growth special case, kill criteria with dates, and a contract checklist the partnerships team can use. Strong. It ran 6,080 words and three tables at 9 columns.
- **sector, theme, markets, earnings-preview, earnings-review, company-brief.** Passed on structure and sourcing. The graders' "suspicious" notes are mostly small arithmetic reconciliation slips (semis calls Lam third when its own table says second; markets says 2.39 points when the table gives 2.45; nVent leverage 2.7x against about 3.1x from its own inputs) and citation mismatches (below).

## Systematic flaws the runs exposed (fix candidates, not applied)

1. **Numbered citations drift.** In 6 of 10 with-skill reports a bracketed number points at a document whose title cannot support the claim (CoreWeave debt figure cited to an Ethereum-miners article; Microsoft's reporting date cited to an Anthropic S-1 piece; index closes cited to an analyst-calls round-up; DRAM price rises cited to a Redington note). The baseline, which mostly used inline links, had fewer wrong citations but more uncited claims. Fix in output-standard.md: either inline links next to the claim, or a final check step that every [n] used in the body is the document the fact came from.
2. **Cost of capital.** valuation.md asks for CAPM with the measured beta and nothing else. Add: Blume-adjust, compare with the peer median and a bottom-up beta, keep the cost of equity inside a stated range for the market, and show value at both the measured and the market-implied rate.
3. **Length.** Every with-skill report exceeded the skill's page target (mean 4,727 words against two to four pages). Either the targets are wrong or the output standard needs a hard cap with an appendix for tables.
4. **Arithmetic reconciliation.** Both arms carry small inconsistencies between text and tables. A one-line self-check in output-standard.md ("every number in the summary appears in a table with the same value") would catch most.
5. **Tool realities.** The market tearsheet's 5D column is not Friday-to-Friday (both arms found and worked around it); its yield "change" columns are percent of the yield, not basis points. Add both to working-with-bigdata.md. The company tearsheet is often 100k to 500k characters; agents saved it to a file and parsed it, which the skills do not anticipate.
6. **Cost.** The theme skill's three-tearsheet-calls-per-company design produced a 134-call, 490k-token run; agents in several skills batched peers through bigdata_computer instead and said so. Let the skills say that batching is the preferred route for peer sets.
7. **Table width.** The 8-column rule was broken in the deep-dive (9 columns, three tables). Minor.

## Gaps in this eval

One run per arm per prompt, so no variance estimate. The assertion grader rewards structure more than correctness; two of its own suspicions (Lam third vs second, the 2.39 points) are the kind of slip it cannot score. Prompts were written by me, not sampled from users. The Skill tool was blocked in both arms, so the eval does not test whether the installed plugin would have fired the right skill (the trigger suite covers that).
