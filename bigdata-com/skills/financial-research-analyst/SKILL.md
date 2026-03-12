---
name: bigdata-financial-research-analyst
description: Guide for creating financial workflows with the Bigdata MCP. Use when users need assistance to create company briefs, earnings previews, earnings digests, risk assessments, startup profiles, funding analysis, founder research, sector overviews, sector comparisons, country economic profiles, regional analysis, G7/G20 comparisons, economic calendar analysis, thematic macro research, sector rotation signals, or cross-asset implications
---

# Bigdata.com Financial Analysis Workflows

This skill provides several comprehensive financial analysis workflows powered by Bigdata.com data and tools.

### Identify the right company
If the user provides a company name, call `find_companies` first to find the entity_id. If the company name is ambiguous, respond with:

>  "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"


## Analysis Categories

This skill covers two main analysis categories. **Read the appropriate reference file based on the user's request:**

| Category | When to Use | Reference File |
|----------|-------------|----------------|
| **Public Company** | Public company analysis: company briefs, earnings previews, earnings digests, risk assessments, investment memos | Read [references/public_company/main.md](./references/public_company/main.md) |
| **Macro Economics** | Sector analysis, country economic profiles, regional comparisons, thematic research, sector rotation, cross-asset implications | Read [references/macro/main.md](./references/macro/main.md) |

### Routing Examples
- "Create an earnings preview for NVIDIA" → **Public Company**
- "Risk assessment for Tesla" → **Public Company**
- "What's happening with Apple?" → **Public Company**
- "Analyze the US technology sector" → **Macro Economics**
- "Economic outlook for Germany" → **Macro Economics**
- "Compare G7 economies" → **Macro Economics**
- "Macro analysis of financials in India" → **Macro Economics**




## Capabilities Overview

When a user says **"Can you help me with a financial report?"** or similar, respond with:

> I can help you automate your research workflows and create professional deliverables:
>
> **Public Company Analysis**
> - **Company Briefs** — 30-day development summaries with categorized news and investment implications
> - **Earnings Previews** — Pre-earnings analysis with bull/bear cases and key metrics to watch
> - **Earnings Digests** — Post-earnings breakdowns with surprises, guidance analysis, and analyst reactions
> - **Risk Assessments** — Comprehensive risk profiles with likelihood/impact ratings from SEC filings and news
>
> **Macro Economics Analysis**
> - **Sector Analysis** — Performance, valuations, themes, sub-industries, catalysts
> - **Country Profiles** — GDP, inflation, policy, calendar, market implications
> - **Regional Comparisons** — G7/G20 comparisons, currency, cross-asset views
> - **Thematic Research** — AI, energy transition, deglobalization, rates
>
> Just tell me what you need. For example: "Create an earnings preview for NVIDIA", or "Economic outlook for Germany."


## Universal Best Practices

- `bigdata_search` can be used directly without calling `find_companies` - just include company name in search query
- Use `bigdata_company_tearsheet` to establish financial baseline when detailed company data is needed
- Call `bigdata_search` multiple times with targeted queries for comprehensive coverage
- Separate objective facts from analysis/implications


## Output Formats

Adapt output to analyst needs:
- **Markdown** — Default for quick review. At the end of the response, ask whether the user wants to create a report

>  "Would you like to create a report with the above response?"

- **Word document (.docx)** — For formal memos and reports
- **Presentation content** — Structured for pitch decks