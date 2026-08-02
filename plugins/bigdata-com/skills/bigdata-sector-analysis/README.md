# Bigdata Sector Analysis

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **sector analysis** — performance, valuations, themes, sub-industries, and upcoming catalysts — powered by **Bigdata.com MCP**.

---

## What It Produces

- Sector performance and valuation metrics vs the broad market
- Sector-specific KPI lens mapped to the GICS sector, not generic P/E only
- Cycle and profitability positioning: early / mid / late vs history
- Analyst sentiment distribution
- Tailwinds and headwinds with named beneficiaries and exposures
- Sub-industry breakdown and a 30-day earnings calendar
- Positioning call with top picks and areas to avoid
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:sector-analysis

---

## Structure

    bigdata-sector-analysis/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── porter-five-forces.md
    │   └── sector-routing.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `bigdata_search`, `bigdata_country_tearsheet`, `find_securities`, `bigdata_company_tearsheet`, `bigdata_events_calendar`.

---

## Related Skills

- **Sector analysis**
- **Country analysis**
- **Cross-sector comparison**
- **Regional comparison**
- **Thematic research**

---

## License

See the root `LICENSE` file of the plugin repository for details.
