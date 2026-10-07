# Bigdata.com plugin

Financial research and market intelligence for Claude, built by [RavenPack](https://www.ravenpack.com/). The plugin connects Claude to the [Bigdata.com](https://bigdata.com/) MCP server and adds 27 research skills that turn its tools into finished analyst work: company briefs, earnings previews and digests, valuation snapshots, peer comparables, investment memos, risk assessments, catalyst monitors, sector and macro analysis, and IPO reviews.

Every skill grounds its output in licensed sources with citations: premium news, regulatory filings, earnings call transcripts, broker research, financial statements and estimates, sentiment signals, macro data, and your own uploaded documents.

## Requirements

An active Bigdata.com account. [Sign up](https://app.bigdata.com/) if you do not have one.

## Install

**Claude.ai and Claude Desktop**: install the plugin from the Claude directory and sign in to Bigdata.com when prompted. Team and Enterprise admins can enable it for the organization under **Organization settings**.

**Claude Code**: run `/plugins`, add the `Bigdata-com/bigdata-plugins-marketplace` marketplace, and install `bigdata-com`. The bundled MCP server configuration in `.mcp.json` connects to `https://mcp.bigdata.com/`. Sign in with OAuth when Claude asks, or add the server with an API key from [platform.bigdata.com/api-keys](https://platform.bigdata.com/api-keys):

```bash
claude mcp add --transport http bigdata_com https://mcp.bigdata.com/ --header "x-api-key: YOUR_API_KEY"
```

Then ask something like:

```
Prepare an earnings preview for Broadcom with inline citations.
```

## Skills

Each skill is a workflow with a defined structure, sourcing rules and output format. Ask in plain language and Claude picks the matching skill.

**Company research**
- `bigdata-company-brief`: what happened at a company in the last 30 days and why it matters.
- `bigdata-quick-take`: a one-page PM-style view with drivers, risks and the next catalyst.
- `bigdata-investment-memo`: a full institutional memo with thesis, variant perception, valuation and recommendation.
- `bigdata-variant-perception`: where your view differs from consensus and why.
- `bigdata-valuation-snapshot`: current valuation by the method that fits the business, with a cross-check.
- `bigdata-peer-comparables`: a comps table against a justified peer set with premium or discount decomposition.
- `bigdata-scenario-analysis`: bull, base and bear cases with probability-weighted expected value.
- `bigdata-risk-assessment`: six-category risk review rated by likelihood and impact.
- `bigdata-moat-governance-review`: moat durability, capital allocation track record and governance.
- `bigdata-catalyst-monitor`: dated events that could move the stock over the next few quarters.

**Earnings**
- `bigdata-earnings-preview`: forward-looking setup ahead of the print.
- `bigdata-earnings-digest`: full post-print breakdown of results, guidance and surprises.
- `bigdata-earnings-reaction`: a tight note on whether the quarter changes the thesis.
- `bigdata-earnings-quality-screen`: cash conversion, accruals and accounting red flags.

**IPOs**
- `bigdata-pre-ipo-analysis`: balanced note on an upcoming listing from the S-1 or F-1.
- `bigdata-post-ipo-day1`, `bigdata-post-ipo-day14`, `bigdata-post-ipo-day179`, `bigdata-post-ipo-day365`: first-day reaction, index fast-track eligibility, and the 180-day and one-year lock-up expiries.

**Sectors, themes and macro**
- `bigdata-sector-analysis`: performance, valuations, themes and catalysts for one sector.
- `bigdata-sector-playbook`: the KPIs, valuation approach, live debates and what to own, avoid and watch in a sector.
- `bigdata-cross-sector`: relative value and rotation calls across sectors.
- `bigdata-thematic-research`: the companies, drivers and risks behind an investment theme.
- `bigdata-country-analysis`: deep economic analysis of one country.
- `bigdata-country-sector-analysis`: one sector inside one country or region.
- `bigdata-regional-comparison`: regions and blocs compared with an allocation view.
- `bigdata-g7-comparison`: the seven G7 economies side by side.

## Data handling

Queries are sent to the Bigdata.com MCP server at `https://mcp.bigdata.com/` and answered from licensed content under your account's entitlements. See the [privacy policy](https://bigdata.com/privacy-policy) and [terms and conditions](https://bigdata.com/terms-and-conditions).

## Documentation and support

- [Plugin documentation](https://docs.bigdata.com/mcp-reference/plugins/bigdata-com)
- [Skills reference](https://docs.bigdata.com/skills-reference/mcp-helpers/financial-research-analyst)
- [MCP reference](https://docs.bigdata.com/mcp-reference/introduction)
- [Support](https://docs.bigdata.com/support) or [support@bigdata.com](mailto:support@bigdata.com)

## License

See [LICENSE](LICENSE), or contact legal@ravenpack.com.
