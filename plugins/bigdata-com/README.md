# Bigdata.com plugin

Financial research for Claude, ChatGPT and Microsoft 365 Copilot, built by [RavenPack](https://www.ravenpack.com/). The plugin connects the host to the [Bigdata.com](https://bigdata.com/) MCP server and adds 24 skills that turn its tools into finished analyst work, grounded in licensed news, filings, transcripts, broker research and estimates, plus files you upload. Every report cites its sources and gives no buy, hold or sell call.

## Requirements

A Bigdata.com account. [Sign up](https://app.bigdata.com/) if you don't have one.

## Install

In Claude and Claude Desktop, install the plugin from the Claude directory and sign in to Bigdata.com when asked. Team and Enterprise admins can enable it for the organization under **Organization settings**.

In Claude Code, run `/plugin marketplace add Bigdata-com/bigdata-plugins-marketplace`, then `/plugin install bigdata-com@bigdata-plugins-marketplace`. The plugin's `.mcp.json` connects to `https://mcp.bigdata.com`, and you sign in with OAuth when Claude asks. To use an API key from [platform.bigdata.com/api-keys](https://platform.bigdata.com/api-keys) instead:

```bash
claude mcp add --transport http bigdata_com https://mcp.bigdata.com/ --header "x-api-key: YOUR_API_KEY"
```

Then ask something like "Prepare an earnings preview for Broadcom".

## Skills

Start with `bigdata` for any Bigdata.com question. It asks what you need when the request is vague, and hands off to a job skill when one fits. You can also type `/` and pick a skill by name, or describe the task and the host picks one from its description.

| Group | Skills |
|---|---|
| Keep up with names and markets | `bigdata-markets-today`, `bigdata-watchlist`, `bigdata-company-brief`, `bigdata-stock-move`, `bigdata-catalysts`, `bigdata-quick-take` |
| One company in depth | `bigdata-deep-dive`, `bigdata-investment-thesis`, `bigdata-valuation`, `bigdata-comps`, `bigdata-earnings-quality`, `bigdata-moat`, `bigdata-capital-allocation`, `bigdata-risk`, `bigdata-credit` |
| Earnings and events | `bigdata-earnings-preview`, `bigdata-earnings-recap`, `bigdata-deal-analysis`, `bigdata-special-situations` |
| Sectors, themes and macro | `bigdata-sector`, `bigdata-theme`, `bigdata-country-analysis`, `bigdata-screen` |

## Data handling

Queries go to the Bigdata.com MCP server at `https://mcp.bigdata.com` and are answered from licensed content under your account's entitlements. See the [privacy policy](https://bigdata.com/privacy-policy) and [terms and conditions](https://bigdata.com/terms-and-conditions).

## Development

Each skill is a folder with a `SKILL.md`, the reference files it loads, and an `agents/openai.yaml` for ChatGPT and Codex.

`library/` holds what the skills share: `output-standard.md` (the rules every report follows), `working-with-bigdata.md` (which data answers which question), the method files under `methods/` and the sector primers under `sectors/`. A skill lists the files it needs in its frontmatter (`bigdata-refs`, `bigdata-sector-primer`), and `packaging/bigdata-com/scripts/sync_library.py` copies them into its `references/` folder, because claude.ai and Microsoft Cowork only load files inside the skill folder. Edit the library, run the sync, and commit both.

`packaging/bigdata-com/scripts/check_skills.py` validates every skill against the Claude, OpenAI and Microsoft limits. The `build-*.sh` scripts in the same folder build the ChatGPT package, the Microsoft 365 Copilot Cowork package (the 19 skills listed in `packaging/bigdata-com/microsoft/manifest.json`), standalone skill archives, and a development zip for trying a branch in claude.ai.

## Documentation and support

- [Plugin documentation](https://docs.bigdata.com/mcp-reference/plugins/bigdata-com)
- [MCP reference](https://docs.bigdata.com/mcp-reference/introduction)
- [Support](https://docs.bigdata.com/support) or [support@bigdata.com](mailto:support@bigdata.com)

## License

See [LICENSE](LICENSE), or contact legal@ravenpack.com.
