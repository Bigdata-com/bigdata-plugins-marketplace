# bigdata-com

Financial research for Claude, ChatGPT and Microsoft 365 Copilot, built by [RavenPack](https://www.ravenpack.com/). The plugin connects the host to the [Bigdata.com](https://bigdata.com/) MCP server and adds 24 research skills that turn its tools into finished analyst work. Every report cites its sources, labels each figure as reported, derived, assumed or judgment, states what the share price implies before giving a view, and gives no buy, hold or sell call.

## Install

Claude: Customize, Plugins, Discover, search for Bigdata.com, Add. Claude Code: `/plugin install bigdata-com@bigdata-plugins-marketplace`. The plugin's Connectors tab lists the Bigdata.com connector; add it and sign in. A Bigdata.com account is required.

## The skills

The entry skill `bigdata` handles any Bigdata.com question, interviews the user when the request is vague, and routes to a job skill when one fits.

| Group | Skills |
|---|---|
| Keep up with names and markets | `bigdata-markets-today`, `bigdata-watchlist`, `bigdata-company-brief`, `bigdata-stock-move`, `bigdata-catalysts`, `bigdata-quick-take` |
| One company in depth | `bigdata-deep-dive`, `bigdata-investment-thesis`, `bigdata-valuation`, `bigdata-comps`, `bigdata-earnings-quality`, `bigdata-moat`, `bigdata-capital-allocation`, `bigdata-risk`, `bigdata-credit` |
| Earnings and events | `bigdata-earnings-preview`, `bigdata-earnings-recap`, `bigdata-deal-analysis`, `bigdata-special-situations` |
| Sectors, themes and macro | `bigdata-sector`, `bigdata-theme`, `bigdata-country-analysis`, `bigdata-screen` |

Each skill is a folder with a `SKILL.md` (what a complete answer contains and where the work goes wrong), the reference files it loads, and an `agents/openai.yaml` for ChatGPT and Codex. Type `/` in Claude to pick one by name, or describe the task and the host picks the skill from its description.

## The library

`library/` holds the files the skills share: `output-standard.md` (the rules every report follows, and the footer), `working-with-bigdata.md` (which data answers which question, and what the data can and cannot do), fourteen method files under `methods/` (price-implied expectations, base rates, ROIC, valuation, multiples and peers, earnings quality, capital allocation, industry structure, operating leverage and TAM, after a price move, downside and catalysts, forecasting discipline, credit, special situations) and the sector primers under `sectors/`. The methods come from Michael Mauboussin's research, the McKinsey valuation text, Graham and Dodd, Klarman and Damodaran, with every figure labelled by source and period.

A skill names the files it needs in its frontmatter (`bigdata-refs`, `bigdata-sector-primer`). `packaging/bigdata-com/scripts/sync_library.py` copies them into the skill's `references/` folder, because claude.ai copies only the skill folder into its sandbox and Microsoft Cowork rejects paths outside it. Edit the library, run the sync, commit both.

## Checks and evals

`packaging/bigdata-com/scripts/check_skills.py` validates every skill against the Claude, OpenAI and Microsoft rules (names, description length, body length, links, companion file counts and sizes, rating words, non-ASCII characters). `evals/run_evals.py` runs cases against the live connector in Claude Code headless and grades them with a judge; see `evals/README.md`.

## Packaging

`packaging/bigdata-com/scripts/` builds the ChatGPT zip, the Microsoft 365 Copilot Cowork zip (19 skills, listed in `packaging/bigdata-com/microsoft/manifest.json`) and a development zip for claude.ai.

## License

MIT, see LICENSE.
