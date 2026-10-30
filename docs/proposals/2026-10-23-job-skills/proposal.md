# Bigdata.com job skills: proposal for the rewrite

Date: 2026-10-23. Author: Marko Kangrga with Claude. Status: proposal written in the morning; built in the afternoon on the local branch `skills-proposal-2026-10-23` (all 26 skills, the library, the scripts, the three packages, the trigger suite and the live cases). Nothing merged, pushed or published to a host.

## 1. Summary

A skill is a folder with a `SKILL.md` file that tells the model how to do one job, and the Bigdata.com plugin ships a set of them to Claude, ChatGPT and Microsoft Copilot next to the connector. Today the plugin has 28 skills: 27 job skills and the `bigdata` entry skill. We replace the 27 with 25 new job skills and keep the entry skill, so the plugin ships 26, built on a shared method library of 14 method files and 12 sector primers. The set follows what users ask Bigdata.com for (monitoring first, then company work, earnings, views, sectors and macro) and the methods come from Michael Mauboussin's research papers, the McKinsey valuation text, Graham and Dodd's Security Analysis and Klarman's Margin of Safety, rewritten as checkable procedures with the numbers labelled by source and date. Every skill produces a report a portfolio manager at a multi-strategy fund would accept as the first draft of their own work: expectations stated before the view, numbers tied to a source or a shown calculation, ranges rather than points, and no buy, hold or sell call.

The same skill folders ship to Claude (chat, Cowork, Claude Code), ChatGPT and Codex, and Microsoft 365 Copilot Cowork. The differences between hosts are handled in the build scripts and in a few per-host files, so one SKILL.md serves all three. The Anthropic directory holds a plugin for review above 512 files, so the shared library is copied into each skill only where the skill lists it, which keeps the plugin under 300 files (the build came to 287: each skill carries its SKILL.md, the OpenAI listing file, the icon, the two shared files, its method files and one primer bundle).

Before we narrow the set, we run three layers of evaluation: build-time checks, trigger tests with all 26 descriptions loaded at once, and end-to-end runs against the live connector graded by a judge against a per-skill checklist. Usage after release decides which skills stay in the 20-skill Microsoft package and which get merged.

Sections 2 to 9 give the reasoning and the detail. Appendix A has the description for every skill, Appendix B has four complete SKILL.md drafts, Appendix C has the specification of each method file, and Appendix D lists the sources.

## 2. What users ask for

Two data sets drove the job list. The first is the Mixpanel count of skill runs between 10 September and 13 October 2026. Only 2.6 percent of all Bigdata.com tool calls carry a skill slug, so these counts are floors. In the same period ChatGPT ran the skills about four times as often as Claude. The second is the [topic model](https://claude.ai/artifact/GdxjEuzkc2A2iVx3MFU6ER) a colleague built on 568,383 production searches between 22 September and 22 October 2026, clustered into 338 topics under 16 use cases. Unclassified means the model could not assign the search to a use case. Share with empty results is the share of searches in that use case that returned nothing.

| Current skill | Runs, 10 Sep to 13 Oct |
|---|---|
| quick-take | 1,404 |
| catalyst-monitor | 729 |
| investment-memo | 700 |
| company-brief | 585 |
| thematic-research | 479 |
| valuation-snapshot | 367 |
| peer-comparables | 239 |
| country-analysis | 204 |
| cross-sector, sector, regional, scenario | 166 to 189 each |
| earnings-preview, earnings-digest | 183, 164 |
| risk, earnings-reaction, country-sector | 87 to 110 |
| moat, quality, variant, playbook, pre-IPO | 32 to 57 |
| post-IPO day 1, 14, 179, 365 | 13 or fewer |

| Topic-model use case | Share of searches | Empty results |
|---|---|---|
| Company news monitoring | 26% | 18% |
| Unclassified | 17% | |
| Sector and theme | 12% | |
| Market wraps | 10% | |
| Earnings | 6% | 27% |
| Macro | 6% | |
| Commodities | 5% | |
| Why a stock moved | 4% | |
| Filings | 3% | 29% |
| Crypto, deals, geopolitics | 3% each | |
| Analyst views | 2% | 67% |
| Ownership | 1% | 38% |

Three things follow. Monitoring is the largest job by a wide margin and we have no skill for the two biggest pieces of it, a market wrap and a watchlist check. Explaining a price move is 4 percent of all searches and has no skill. Analyst views are asked for often and come back empty two thirds of the time, which the new skills handle by using the tearsheet's analyst targets, ratings and estimate revisions plus the sell-side reactions that research notes and news carry, until broker research arrives. The IPO skills had 13 or fewer runs each and go.

In the topic model, 71 percent of searches name a time window, which is why every skill states its data vintage and why the monitoring skills take a window as their main input.

## 3. Rules every skill follows

1. The agent picks the skill. Users rarely type a skill name, so the description decides whether a skill fires and the hand-off lines decide which neighbour fires instead. Descriptions are third person, lead with the job in the first 120 characters, give the phrasings users say, and name the adjacent job they do not cover. Target 500 characters, hard limit 1,024.
2. Skills are guidelines, not scripts. Each skill says what a finished answer must establish and how to get there, and tells the model to skip steps that do not apply and to go further where the task needs it. A narrow question gets a direct answer in the skill's method, not the full report.
3. The reader is a seasoned portfolio manager. Rigour first, plain language, buy-side vocabulary where it is the natural word. The user can ask for a simpler version.
4. Expectations before the view. Any skill that forms a view on a stock states what the price implies before saying what the analyst thinks, using the expectations method file.
5. Every number can be checked. A fact from a document carries a link with the source and date next to it. An assumption a conclusion rests on is stated once, in plain words, where it matters. Nothing else is labelled. (Revised 28 October: the four basis words and the Basis column were retired after they reached the reports as residue.)
6. Ranges, not points. Valuation and forecasts come as base, downside and upside with probabilities that sum to 100 percent and weights taken from the reference class, never a default 25/50/25.
7. A base rate where a multi-year growth or margin claim carries the conclusion, written into that sentence with how often companies of that size achieved it and the population and period, and nowhere else. (Revised 28 October: the earlier rule, a base rate next to every claim labelled with sample and period, produced paragraphs that named the source book.)
8. No recommendation. The output describes the balance of evidence and what would change it. It carries no rating, stance line, position size or Kelly fraction.
9. Facts apart from analysis. What the data shows, then what it means, then what would change the view, then the gaps Bigdata.com could not fill.
10. The same footer everywhere: Sources, the Powered by Bigdata.com line and the disclaimer, verbatim.
11. Nothing hard-coded that goes stale: no fixed years, no fixed query lists, no historical figure quoted as a current fact. A historical figure carries its population and period. (Revised 28 October: the "(verify)" convention was retired; verification notes live in the method specs under docs, never in shipped files.)
12. No scripts in version one. Computation goes through the Bigdata.com `bigdata_computer` tool or the host's code execution with the working shown; the method files carry the formulas. We revisit bundled scripts if the evals show arithmetic errors.

These replace the EPIC driver table and the FaVeS variant-perception scoring used in the current skills, the Kelly position-sizing formula, the star ratings, the Buy/Hold/Sell lines, the "Prepared with Claude" footer and the five Python scripts.

## 4. The skill set

Twenty-five job skills plus the entry skill. Names keep the `bigdata-` prefix because the ChatGPT package namespaces skills under a 36-character app id with a 64-character cap on `plugin:skill`, and because the usage pipeline keys on the prefix. The longest name below is 26 characters.

### 4.1 Keep up with names and markets

| Skill | Job | Why it is in the set |
|---|---|---|
| bigdata-markets-today | What moved across indexes, sectors, rates, FX, commodities and crypto over a window, and why, from the market tearsheet and news | Market wraps are 10 percent of searches and had no skill |
| bigdata-watchlist | For a list of names: price, move, news, earnings versus estimates, targets and sentiment side by side over a window, then an offer to save the list | Company news monitoring is 26 percent of searches; most prompts carry several names |
| bigdata-company-brief | What happened at one company over a window and what it means for the drivers | 585 runs; the most used monitoring skill |
| bigdata-stock-move | Why a stock moved, what changed in the long-term outlook, and the base rates for what follows a move of that kind | 4 percent of searches, no skill today; method from two Credit Suisse studies of large one-day moves (Man Overboard, 2015, and Celebrating the Summit, 2016) |
| bigdata-catalysts | Upcoming events for a name or list, each with date, mechanism, direction, size and certainty | 729 runs; the catalyst schema from the current skill is kept |
| bigdata-quick-take | One page: the view, what is priced in, the three drivers, the risks and what would change the view, the next catalyst | 1,404 runs, the most used skill |

### 4.2 One company in depth

| Skill | Job | Why it is in the set |
|---|---|---|
| bigdata-deep-dive | An initiation-style report: business, industry structure, economics, expectations, valuation range, risks, catalysts, what to watch | The long form of investment-memo (700 runs) |
| bigdata-thesis | A thesis with the variant view stated as testable claims, the evidence for and against each, kill criteria with dates, and the catalyst path | investment-memo and variant-perception merged around the claim template |
| bigdata-valuation | What the company is worth: price-implied expectations first, then a reinvestment-consistent DCF with the terminal value and bridge checks, as a range | 367 runs; the current skill lacks the checks a PM would run |
| bigdata-comps | Peers chosen by value drivers, consistent multiples at market values, medians, and where the company should sit and why | 239 runs |
| bigdata-scenarios | Base, downside and upside cases run through the drivers with reference-class weights and an expected value | 180 runs |
| bigdata-earnings-quality | Accrual, EBITA rebuild, recurring one-offs, provisions, revenue recognition, earnings-to-equity reconciliation, red flags with severity | 55 runs, but the method is used inside deep-dive, thesis and earnings-recap |
| bigdata-moat | Industry map, profit pool, share stability, pricing power, concentration, entry and exit, five forces, source of advantage, disruption test | 57 runs; the Measuring the Moat sequence replaces the current taxonomy |
| bigdata-capital-allocation | Five-year sources and uses, buyback and dividend tests, deal tests, reinvestment returns, leverage, incentives | New; the governance half of moat-governance plus the capital-allocation methods |
| bigdata-risk | Downside first: what breaks the thesis, how much is at risk, liquidation and private-market floors, the risks ranked by probability and size | 110 runs |
| bigdata-credit | Leverage, coverage, maturities, covenants, rating medians, distress signals, for an equity holder or a credit view | New; asked for by credit desks, thin method file until broker research arrives |

### 4.3 Earnings and events

| Skill | Job | Why it is in the set |
|---|---|---|
| bigdata-earnings-preview | Drivers, what is priced in, consensus against base rates and guidance, scenarios with watch-fors, the sales-to-margin linkage | 183 runs; the current order of sections is kept |
| bigdata-earnings-recap | After the print: results versus consensus and guidance, what changed in the long-term outlook, thesis check, estimate and valuation refresh, quality signals, next date | earnings-digest and earnings-reaction merged; the long and short forms are one skill sized to the question |
| bigdata-deal-analysis | For an announced or rumoured deal: strategic logic, price versus value, synergies against base rates, SVAR, financing, regulatory path, what each side's shareholders get | New; deals are 3 percent of searches |
| bigdata-special-situations | Spin-offs, merger arbitrage, rights issues, restructurings, liquidations: the arithmetic of the payoff with a break price and probabilities | New; replaces the five IPO skills for event work |

### 4.4 Sectors, themes and macro

| Skill | Job | Why it is in the set |
|---|---|---|
| bigdata-sector | One sector or several compared: structure, profit pool, cycle position, the names that matter, what is priced in, with the sector primer loaded | sector-analysis, sector-playbook and cross-sector merged |
| bigdata-theme | A theme: the chain of beneficiaries and losers, TAM with checks, the names with real exposure (geographic and segment revenue), what is priced in | 479 runs |
| bigdata-country | A country or region: growth, inflation, rates, currency, politics, markets, with the country tearsheet | 204 runs |
| bigdata-macro-compare | Countries, regions or blocs compared on the same indicators with the differences explained | regional, G7 and country-sector merged |
| bigdata-screen | Find candidates: screen by size, sector, geography, valuation and fundamentals, then rank and explain the shortlist | New; "find new ideas" is the fourth interview option in the entry skill and had no skill |

### 4.5 The entry skill

`bigdata` stays as the entry point: the interview for vague requests, the hand-off table to the job skills, the "what Bigdata.com has" answer, and the skill builder. The first rewrite session already wrote it (branch `worktree-bigdata-any-prompt`); its body gains the routing table for the new names.

### 4.6 Fold-in candidates, decided after evals

Comps and scenarios could fold into valuation, capital-allocation into moat, credit into risk, and macro-compare into country. We ship them separate so the trigger evals can show whether the specific phrasings route better to a focused description, and merge after four weeks of usage. The Microsoft Cowork package takes 20 skills, so six are left out of that package from day one; section 7.3 names them.

## 5. The shared method library

The current skills copy 23 reference files between them, several of which (EPIC, FaVeS, the routing file, the post-IPO file) go. The new library lives once in the repo at `plugins/bigdata-com/library/` and is copied into each skill's `references/` folder at build time, because claude.ai copies only the skill folder into its sandbox and Cowork rejects any `../` path. A skill lists the files it needs in its frontmatter `metadata` block, and a build check fails if a copied file differs from the library.

### 5.1 Method files (14)

| File | What it carries | Loaded by |
|---|---|---|
| expectations.md | Steady-state value, implied growth and competitive-advantage period solved from the price, the warranted P/E grid, which revision matters, implied multiples from a DCF | quick-take, deep-dive, thesis, valuation, earnings-preview, earnings-recap, scenarios, theme, sector |
| base-rates.md | Sales and earnings growth distributions by size and horizon, margin and profitability persistence by sector, fade formula with horizon-matched r, operating-margin beta, threshold margin, consensus overconfidence | valuation, scenarios, earnings-preview, thesis, deep-dive, theme, screen |
| roic.md | NOPAT and invested capital built both ways, with and without goodwill, leases, capitalised R&D, excess cash, ROIIC, margin times turnover, spread over cost of capital, the FactSet field as a cross-check | deep-dive, valuation, moat, capital-allocation, comps, earnings-quality |
| valuation.md | Value-driver formula, horizon by competitive advantage, continuing value with RONIC fading to WACC, terminal-value share and implied terminal multiple, reinvestment consistency, tax on EBIT, the equity bridge per share, cost of capital as an assumption with a sensitivity table, scenarios, special cases for banks, cyclicals, high growth, emerging markets, conglomerates | valuation, deep-dive, scenarios, deal-analysis |
| multiples-and-peers.md | Consistent numerator and denominator, EV at market values, cleaning the metric, which multiple for which business, peers by value drivers, medians, what drives a multiple, target multiple formulas, implied multiples | comps, valuation, quick-take, sector, screen |
| earnings-quality.md | One accrual definition, EBITA rebuild, recurring one-offs counted, provisions, pensions, leases, stock compensation, revenue recognition, earnings-to-equity reconciliation, Graham and Dodd normalisation, red flags with severity | earnings-quality, earnings-recap, deep-dive, thesis, risk |
| capital-allocation.md | Sources and uses, buyback return and EPS breakeven, dividend tests, deal NPV and SVAR, synergy base rates, reinvestment returns, leverage, incentives | capital-allocation, deal-analysis, deep-dive, moat |
| industry-structure.md | Industry map, profit pool, share stability, pricing power, HHI, entry and exit, five forces, value chain, sources of advantage, disruption, lifecycle and CAP | moat, deep-dive, sector, theme, thesis |
| operating-leverage-and-tam.md | Fixed and variable cost response, scale versus leverage, threshold margin, TAM built bottom-up and top-down, S-curve warning, profit pools and value migration | earnings-preview, theme, deep-dive, scenarios |
| after-a-price-move.md | Event classification, the Man Overboard and Celebrating the Summit tables, momentum, valuation and quality proxies from tearsheet fields, the long-term-outlook test | stock-move, earnings-recap, watchlist |
| downside-and-catalysts.md | Margin of safety, downside first, why it is cheap and who sells, liquidation and private-market floors, catalyst taxonomy and potency, kill rule, sell logic, facts versus opinions | risk, thesis, catalysts, quick-take, deep-dive |
| forecasting-discipline.md | Granular probabilities, scenario weights from the reference class, premortem, kill criteria with dates, disconfirming evidence, expected value and magnitude over frequency | scenarios, thesis, earnings-preview, earnings-recap |
| credit.md | Coverage and leverage tests, safety margins for senior securities, rating medians, maturities, distress signals | credit, risk, deal-analysis |
| special-situations-arithmetic.md | Merger arbitrage spread and break price, spin-off logic, rights issues, restructurings, liquidations, probability-weighted payoff | special-situations, deal-analysis |

Appendix C specifies each file: inputs mapped to Bigdata.com fields, the procedure with a done condition per step, formulas with variables defined, reference tables with source and period, interpretation rules, and the output lines the skill must produce. The specs were written from the extraction notes of the source papers, and every figure carries its source and period. Where the papers lack a number the spec says so with a GAP line rather than inventing one; there are about ten such lines, mostly on cost-of-capital inputs and current base rates that the writer must source elsewhere or leave as assumptions.

### 5.2 Sector primers (12)

The seven current primers (software, banks, pharma, REITs, industrials, consumer and retail, energy) are rewritten so that every number is a range with its population and period (revised 28 October: sources and "(verify)" marks were removed from shipped files), and five are added: semiconductors and hardware (split from software), materials, communication services, utilities, insurance. Each primer carries the sector's value drivers, the metrics that matter and why, the structure of the profit pool, the accounting traps, where the sector sits in the persistence and fade tables, and the questions a specialist asks on an earnings call. The sector skill loads the primer for the sector in question; the company skills load it when the company is in one of the eleven sectors.

### 5.3 The two files every skill loads

`working-with-bigdata.md` (written in the first rewrite session, extended here) carries the data rules: resolve every entity first, which tool answers which question, how to search well and when to retry in fast mode with the audit's filters, the tearsheet sections to request so the response stays small, five periods per call so ten years takes two calls, how estimates carry actuals, surprise and guidance, the rule that guidance for the next quarter is on the current quarter's call, and when to offer to save a watchlist, a monitor or a report. `output-standard.md` carries the report conventions in section 6.3.

## 6. How a skill is built

### 6.1 The folder

```
skills/bigdata-earnings-preview/
  SKILL.md                      the method and the output structure, under 400 lines
  references/                   copied from library/ at build, listed in SKILL.md metadata
    working-with-bigdata.md
    output-standard.md
    expectations.md
    base-rates.md
    operating-leverage-and-tam.md
    forecasting-discipline.md
    sectors/technology-saas.md  only when the skill is sector-aware
  agents/openai.yaml            ChatGPT and Codex listing and policy
  assets/bigdata-icon-black.svg the icon ChatGPT shows
```

No report template file. The output structure lives in SKILL.md so it is in context whenever the skill fires, and the body stays under 400 lines by pushing method detail to the references.

### 6.2 The SKILL.md skeleton

Every job skill has the same eight parts, in this order. The headings are fixed so the evals can check them and so the model finds the same thing in the same place.

1. Frontmatter: `name`, `description`, `metadata` with the list of library files to copy.
2. One paragraph on what the skill produces and for whom.
3. Before starting: the connector check (say so and stop if Bigdata.com is not connected, never answer from memory or the web instead), pass `plugin_slug` on every call, read `working-with-bigdata.md`, treat the skill as guidelines.
4. Scope the request: what must be known before data gathering starts, what to assume and state when it is not, and the one question worth asking when the answer would change the work materially. At most one question.
5. Gather: the data plan as a list of tool calls in order, with what each must establish and the done condition for the step.
6. Analyse: the method as numbered steps, each naming the reference file to load and when, each ending in what the step must produce.
7. Write: what the opening gives, that the body follows the question, what closes the note, and how to size down for a narrow question (revised 28 October: no section skeleton and no Basis column; sub-headings state findings, not steps).
8. Checks before sending: the list a portfolio manager would run on this report, five to ten items, specific to the skill.
9. Hand-offs: when to switch to a neighbouring skill, and the single offer to make after delivery (save a watchlist, a monitor or a report, or build a skill).

Appendix B shows four complete drafts in this shape.

### 6.3 The output standard

Each report has the same frame so that a user who reads three of them knows where to look.

- Header: title, the company or subject with its ticker, the date, and "Data as of" with the latest fiscal period in the tearsheet and the newest document used.
- The answer first, in prose, four to eight sentences: what the evidence shows, what the price implies, what would change the reading. No rating word.
- The body sections the skill defines, in its order.
- A fact from a document carries an inline link with source and date; an assumption a conclusion rests on is stated once in plain words where it matters; no Basis column and no citation numbers (revised 28 October). Every figure has a unit, a currency and a period. Consensus figures carry their vintage and the number of estimates when the tearsheet gives it.
- A "What would change this view" section with two to five conditions, each observable and dated where possible.
- A "Gaps" line naming what Bigdata.com could not answer. Nothing is filled from memory or the web without saying so.
- Sources: numbered, with source name, title, date and the attribution link from the tool result. Derived figures that have no document cite the data set in a Data line.
- The footer: the Powered by Bigdata.com line and the disclaimer, verbatim.
- Length. One page for quick-take. One to two pages for company-brief, stock-move, catalysts, watchlist and markets-today. Two to four pages for earnings-preview, earnings-recap, valuation, comps, scenarios, earnings-quality, moat, capital-allocation, risk and credit. Four to eight pages for deep-dive, thesis, sector, theme, country and deal-analysis. A narrow question gets a direct answer that still cites and still carries the footer.
- Plain language, active verbs, no hype adjectives. Buy-side vocabulary is fine; an uncommon term is defined on first use.

Citation format is one of the open decisions in section 10. The proposal uses numbered references with the server's link format inside each Sources entry, which works in markdown, in Word export and in every host, and asks the MCP team to align the server instruction's inline format with it.

### 6.4 The description template

```
<What it produces> for <subject> from Bigdata.com data: <three or four contents in
the order they appear>. Use when the user asks <phrasing 1>, <phrasing 2>,
<phrasing 3>, or <phrasing 4>. Not for <adjacent job>, which bigdata-<other>
covers, or <adjacent job 2>, which bigdata-<other 2> covers.
```

Third person throughout. The first clause names the job so a host that shortens descriptions (Codex at 2 percent of context, Claude Code at 1 percent) still matches on it. The phrasings are the ones users say, taken from the topic model's query examples, not synonyms of each other. The "Not for" clause names at most two neighbours. Target 500 characters.

Claude Code's listing budget is the reason for the target: at 1 percent of the context window, 26 descriptions of 1,000 characters would overflow it and Claude Code would drop the descriptions of the least-used skills, leaving names only. At 500 characters the set fits in most sessions, and the entry skill's routing table covers the case where it does not, because names are always listed.

### 6.5 Implicit invocation

All 26 skills are model-invoked on every host. OpenAI's own finance plugin uses one implicit router and 22 explicit-only specialists, which stops accidental firing but also stops the specialists from catching untagged questions. Our usage shows the job skills firing on their own at four times the Claude rate on ChatGPT, so switching them to explicit-only would cost the runs we have. The trigger evals in section 8.2 test the 26 descriptions together; if they show misfires that the "Not for" clauses do not fix, the fallback is OpenAI's pattern for the ChatGPT package only, since `allow_implicit_invocation` is a per-host file.

## 7. Packaging per host

The facts below were checked against the official pages on 2026-10-23; the few that rest on our own tests rather than documentation are marked.

### 7.1 Claude: chat, Cowork and Claude Code

The plugin repo stays the package. `plugins/bigdata-com/` holds `.claude-plugin/plugin.json`, `.mcp.json` with the remote server, and `skills/`. A plugin installed from the directory on claude.ai loads its skills in chat on web, desktop and mobile, in Cowork, and in Claude Code as a synced plugin from version 2.1.273.

Limits that shape the files:

| Limit | Value | Source |
|---|---|---|
| Skill description | 1,024 characters, no XML tags | [Agent Skills spec](https://agentskills.io/specification), [Claude skills how-to](https://claude.com/docs/skills/how-to) |
| Skill name | 64 characters, lowercase, digits, hyphens, equal to the folder name, must not contain "claude" or "anthropic" | [Skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) |
| SKILL.md body | under 500 lines recommended | [Agent Skills spec](https://agentskills.io/specification) |
| Claude Code listing | description plus when_to_use cut at 1,536 characters per skill; whole listing budget 1 percent of context, least-used descriptions dropped first; names always listed | [Claude Code skills page](https://code.claude.com/docs/en/skills) |
| Directory review | held for a reviewer above 512 files per plugin, or any text file above 256 KiB; every file under 5 MiB; repo under 50 MiB; README of 40 words or more; a license | [Pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist) |
| Plugin upload | 5,000 files, 200 MB | [Plugin platform support](https://claude.com/docs/plugins/platform-support) |
| MCP server instructions | delivered in Claude Code up to 4,096 characters; dropped in claude.ai chat and desktop (our canary test and GitHub issue 93, not documented by Anthropic) | [Claude Code MCP page](https://code.claude.com/docs/en/mcp), [claude-ai-mcp issue 93](https://github.com/anthropics/claude-ai-mcp/issues/93) |
| Directory policy 2F | a plugin must not direct Claude to pull behavioural instructions from external sources | [Directory policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) |

Consequences. The library is copied per skill rather than referenced across folders, and only the files a skill lists, which keeps the plugin under 300 files including the 26 icons. Descriptions target 500 characters. Nothing in a skill fetches instructions from a URL. The `agents/openai.yaml` file inside each skill folder is ignored by Claude and is harmless, but the Claude directory build can strip it to stay well inside the file limit.

Claude Code also honours `disable-model-invocation`, `allowed-tools`, `model` and `context` in frontmatter; we use none of them, so one frontmatter serves every host.

The development loop stays as the first rewrite session built it: `build-claude-dev-zip.sh` makes a zip of the branch for upload as a custom plugin on claude.ai under a different name, so the branch runs next to the released plugin.

### 7.2 ChatGPT and Codex

The OpenAI package is a zip with `plugin.json`, `mcp.json`, `assets/` and `skills/`, built by `build-openai-plugin-zip.sh` from the same skill folders. The limits come from OpenAI's [skills](https://developers.openai.com/plugins/build/skills), [MCP server](https://developers.openai.com/plugins/build/mcp-server), [submission](https://developers.openai.com/plugins/deploy/submission) and [submission errors](https://developers.openai.com/plugins/deploy/submission-errors) pages and the [Codex skills page](https://learn.chatgpt.com/docs/build-skills). Each skill carries `agents/openai.yaml` with `interface.display_name`, `interface.short_description`, `interface.default_prompt`, the icons, and `policy.allow_implicit_invocation`.

| Limit | Value |
|---|---|
| Skills per plugin | no cap in the ZIP route; the MCP import route is capped at 5 and is not used |
| `plugin-name:skill-name` | 64 characters; our app id is 36, so skill names up to 27 |
| Skill description | 1,024 characters |
| Plugin short description | 240 characters at validation, 30 at final submission |
| Starter prompts | 3, each 128 characters, no @mention |
| ZIP | 100 MB compressed, 5,000 entries, 512 MiB extracted |
| Review | every skill change needs a new ZIP, scans take up to 2 hours, then a review |
| Codex listing | 2 percent of context for all skill descriptions, descriptions shortened first, key use case must lead |

Two additions. First, `extensions.com.openai.onboardingSkill` points at `./skills/bigdata/SKILL.md`, so the Setup action on the plugin page runs the entry skill's interview. Second, the three starter prompts are rewritten to match three of the new skills (a market wrap, a watchlist check, an earnings preview), since those are the jobs the topic model shows.

The open question for ChatGPT is whether a plain finance question with no @mention reaches a Bigdata.com skill or goes to web search. The implicit-pick test from the ChatGPT research (ten finance prompts sent without an @mention, with and without the plugin installed) measures it after release; the fallback is in section 6.5.

### 7.3 Microsoft 365 Copilot Cowork

The Cowork package is a zip with `manifest.json`, the two icons and `skills/`, built by `build-microsoft-plugin-zip.sh`, which already enforces the limits below and fails the build on any breach. The limits come from Microsoft's [Cowork plugin development](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development) and [declarative agent skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-skills) pages.

| Limit | Value |
|---|---|
| Skills per package | 20 (ASKILL-M002) |
| Companion files per skill | 20, each 5 MB or less, 10 MB per skill in total |
| Companion file types | an allowlist: .md, .json, .pdf, .py, .sh among others; .svg is rejected |
| Paths | relative, no `../`, no hidden files, folder path 256 characters or less |
| Name | 1 to 64 characters, kebab-case, equal to the folder name |
| Description | 1 to 1,024 characters |
| Body | target under 5,000 tokens |
| Companion download | all companions within 15 seconds |

With 26 skills the package leaves six out. The proposed first cut, by expected demand and by overlap with skills that stay: bigdata-credit, bigdata-special-situations, bigdata-capital-allocation, bigdata-macro-compare, bigdata-screen and bigdata-comps (valuation loads the same multiples file). The build prints the skills left out so the list is visible on every build, and usage after four weeks revises it.

Microsoft also has a declarative-agent route for Copilot Chat with at most 8 skills and 20,000 characters of instructions per agent. If a Copilot Chat agent is wanted later, it takes the six monitoring skills plus earnings-preview and earnings-recap; this proposal does not build it.

### 7.4 Other hosts

Grok has no way for a publisher to ship skills into grok.com chat; the connector works there and users can save their own skills. Perplexity accepts a plugin zip with `plugin.json` at the root on plans that include Perplexity Computer, which is the same layout as the OpenAI zip, so that zip can be tried there without changes. Gemini takes a user-uploaded skill file. None of these needs work in the rewrite beyond a short guide page, and the entry skill's body is the one file worth offering as a single-file skill to users on those hosts.

Serving skills from the MCP server itself (a tool that returns a skill's text, as Daloopa, Figma and Datadog do) would reach connector-only users on every host. It is outside this rewrite and listed as an open question.

### 7.5 Build and check

One script, `packaging/bigdata-com/scripts/sync-library.sh`, copies the listed library files into each skill's `references/` and fails if a copied file differs from the library or a listed file is missing. The three existing build scripts run after it. A `check-skills.py` step validates every skill against the union of the three hosts' rules (name, description length, body lines, file count, file size, file types, no `../`, links resolve, the eight headings present, no rating words, no "Prepared with Claude", no hard-coded year) and runs the writing linter over the SKILL.md prose. These replace the per-skill validation in `build-skill.sh`, which checks for a template file that no longer exists.

## 8. Evaluation

Three layers, cheapest first, and all three must pass before a skill ships. The runner from the first rewrite session (`evals/run_evals.py`) is the base for layer three; `claude plugin eval` is the base for layer two.

### 8.1 Build-time checks

The `check-skills.py` step in section 7.5, run on every commit. Zero cost, catches the structural failures (the current plugin has a routing file that points at files that do not exist, and a script that mixes gross and net PP&E in the Beneish calculation).

### 8.2 Trigger tests

`claude plugin eval` runs each case with the whole plugin loaded and, by default, once more without it, in a clean configuration with no user skills, and never starts the real MCP server unless asked. Each case is a folder with a `prompt.md` and graders; the grader `tool_used: Skill` with the skill name checks that the right skill fired. Mocks for the Bigdata.com tools live in `evals/mocks/` so trigger runs cost nothing on the connector.

Per skill, six prompts:

| Kind | Example for bigdata-stock-move | Expected |
|---|---|---|
| Direct | "Why is Micron down 8 percent today?" | the skill fires |
| Indirect, ticker only | "MU just dropped, what happened" | the skill fires |
| Window phrasing | "What drove ASML this week?" | the skill fires |
| Near miss, neighbour | "What happened at Micron last month?" | bigdata-company-brief fires, not stock-move |
| Near miss, neighbour | "Micron reported last night, how did it do?" | bigdata-earnings-recap fires |
| Should not fire | "Why do stocks drop after earnings in general?" | no Bigdata.com skill, or the entry skill at most |

Twenty-six skills times six prompts is 156; with the baseline run it is 312 model calls on Sonnet, in the tens of dollars per pass at current Sonnet prices. The pass rule is that each skill fires on its three positives and on none of its three negatives in at least two of three runs. The whole set runs together, which is the coexistence test the onboarding plan asked for. The skill-creator plugin's description tuner runs on any skill that fails, with the same six prompts as its should-fire and should-not-fire sets.

### 8.3 End-to-end runs against the live connector

The first session's runner, extended with a `skill` field per case so one cases file covers all skills. It loads the branch's plugin, switches every other plugin off, limits tools to the production connector and the read tools, blocks the account-changing tools, lets Haiku play the user when a skill asks a question, and grades with a Sonnet judge. Four fixtures cover the cases a method must survive:

| Fixture | Why |
|---|---|
| Micron | a cyclical with guidance on the call, large consensus growth outside the base-rate class, a price that implies no growth: tests expectations, base rates, mid-cycle normalisation |
| JPMorgan | a bank: tests the equity-DCF and P/B against ROE paths, the primer, and that EV multiples are not used |
| ASML or Toyota | a non-US name: tests entity resolution, currency, reporting conventions, geographic revenue |
| a $2 billion US industrial | a small cap: thin news and estimates, tests the Gaps line and that nothing is filled from memory |

Per skill, three to four cases: the fixture that stresses its method, a narrow question that must get a direct answer rather than the full report, a connector-off case that must stop and explain, and for the company skills a private company that `find_securities` returns as Private, which must be handled from documents only. Counted checks: questions asked before the first result (at most one), Bigdata.com calls within a range, the expected skill used, no account-changing call, every number with a citation or a Basis label (a regex over the report), no rating word. Judge checks: the per-skill checklist from section 8.4. A full pass is about 90 runs on Opus with a Sonnet judge, in the low hundreds of dollars at current prices.

### 8.4 The method-quality rubric

The judge grades each report against a checklist specific to the skill, written from the "what a top analyst checks" lists in the method specs. Examples:

- earnings-preview. States what the price implies before the drivers. Places consensus sales and EPS growth in the size-and-horizon class with the share that achieved it. Quotes the company's guidance for the quarter from the previous call, verbatim with a citation. Gives the sales-to-margin sensitivity with the sector's operating-margin beta. Scenarios carry probabilities summing to 100 and a watch-for each. No rating.
- valuation. Expectations first. A reinvestment-consistent terminal value with RONIC fading to WACC. The terminal-value share of EV reported against the guidance band, and the implied terminal multiple below today's. The bridge per share with every item. A WACC and growth sensitivity table. A range rather than a point. The special case applied when the company is a bank, a cyclical or high growth.
- stock-move. The event classified as earnings or not, with its size relative to the index. The base-rate row stated with its population and period. Momentum, valuation and quality proxied from tearsheet fields and named derived. The long-term-outlook test answered. No buy or sell call.
- quick-take. Fits on one page. The steady-state P/E check is there. Three drivers with evidence, the next dated catalyst, and what would change the view.

Each item scores pass or fail with a one-sentence reason. A skill ships at 80 percent of items passing across its runs, a starting bar to raise as the skills mature, and any failed item on "no rating", "no memory fill" or "citation on every number" blocks regardless. The judge grades against the checklist item by item, so its own taste plays a small part.

### 8.5 Manual host runs

After layers one to three, each skill is run once by hand on claude.ai web with the custom-plugin zip, once in Cowork, once in ChatGPT web, and once in Microsoft Cowork, with the transcript and a screenshot saved under `skills-tracker/evidence/`. These catch what headless cannot: the host's question widget, the slash menu entries, where ChatGPT shows the starter prompts, and whether an untagged finance question reaches the plugin.

### 8.6 After release

Every call carries `plugin_slug`, the server-side allowlist gets the new names and keeps the old ones for a transition, and the Mixpanel skill-run report is read weekly. At four weeks we take the fold-in decisions in section 4.6 and revise the Microsoft 20.

## 9. Migration and release

| Current skill | Becomes |
|---|---|
| quick-take | bigdata-quick-take |
| catalyst-monitor | bigdata-catalysts |
| investment-memo | bigdata-deep-dive (long form) and bigdata-thesis (the claims) |
| company-brief | bigdata-company-brief |
| thematic-research | bigdata-theme |
| valuation-snapshot | bigdata-valuation |
| peer-comparables | bigdata-comps |
| country-analysis | bigdata-country |
| cross-sector, sector-analysis, sector-playbook | bigdata-sector |
| regional-comparison, g7-comparison, country-sector-analysis | bigdata-macro-compare (country-sector questions route to bigdata-sector with a country scope) |
| earnings-preview | bigdata-earnings-preview |
| earnings-digest, earnings-reaction | bigdata-earnings-recap |
| scenario-analysis | bigdata-scenarios |
| risk-assessment | bigdata-risk |
| moat-governance-review | bigdata-moat (structure) and bigdata-capital-allocation (governance and incentives) |
| earnings-quality-screen | bigdata-earnings-quality |
| variant-perception | bigdata-thesis |
| pre-ipo-analysis, post-ipo day 1, 14, 179, 365 | dropped; IPO questions go to the entry skill, and event arithmetic to bigdata-special-situations |
| none | new: bigdata-markets-today, bigdata-watchlist, bigdata-stock-move, bigdata-capital-allocation, bigdata-credit, bigdata-deal-analysis, bigdata-special-situations, bigdata-screen |

Release in one batch, as the onboarding plan of 21 October decided, because the entry skill's routing table, the descriptions' "Not for" clauses and the usage allowlist all reference the full set. The sequence: library and specs first, then the four flagship skills in Appendix B to the eval bar, then the remaining 21 written to the same skeleton, then the three packages. Each package carries the version from the plugin manifest, and `plugin_slug` carries the version too, as the ticket for versioned plugin slugs (AX-198) asks.

## 10. Decisions for Marko

These are the points where a different answer changes what gets built; Marko decides them before the library build starts. Everything else in this document is a call made in the research and will change on request.

| Decision | Proposal | Alternative |
|---|---|---|
| Citation format | Numbered references `[1]` in the text and a Sources list whose entries use the server's link format; the MCP server instruction and the skills then say the same thing | Inline `[Source - date](url)` as the server instruction says today; it reads worse in long reports |
| ChatGPT invocation | All 26 skills stay model-invoked, measured by the trigger evals and the ChatGPT implicit-pick test (finance prompts with no @mention) | OpenAI's pattern for the ChatGPT package: one implicit router skill and explicit-only specialists, kept as the fallback |
| The six skills left out of the 20-skill Microsoft Cowork package | credit, special-situations, capital-allocation, macro-compare, screen and comps, revised after four weeks of usage | Two Cowork packages, or a different six |
| The four skills written first | earnings-preview, stock-move, deep-dive and quick-take: the most used skill, the most demanded new job, the flagship long form and the method-heaviest short form | Another four, for example the six monitoring skills first |
| Cost of capital | The skills state it as an assumption with its basis (risk-free rate plus a premium, or a stated sector range) and always show a sensitivity, since Bigdata.com has no WACC field | Ask the platform team to add a WACC estimate to the tearsheet |
| A skill-serving MCP tool | Outside this rewrite; worth a ticket for a `bigdata_get_skill` tool that returns a skill's text, so connector-only users on every host get the methods | Leave connector-only users with the tool descriptions |
| Sector primers | Twelve: the seven current ones rewritten, semiconductors split from software, plus materials, communication services, utilities and insurance | Split transport from industrials if the sector skill's evals show the primer is too broad |
