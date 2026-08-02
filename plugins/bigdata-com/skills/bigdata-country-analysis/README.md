# Bigdata Country Analysis

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **country economic analysis** — GDP, inflation, monetary policy, labor markets, debt mechanics, and investment implications — powered by **Bigdata.com MCP**.

---

## What It Produces

- Key indicators and an economic health assessment
- Structural and historical context: sector transformation and labor productivity
- Debt and fiscal mechanics: tax-to-GDP, debt composition, servicing burden, PFM
- Substantive labor market section covering macro and micro (informality, youth, real wages)
- Monetary policy stance and rate-path expectations
- Market implications across equity, fixed income, currency, and FDI
- A dedicated, sourced policy recommendations section
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:country-analysis

---

## Structure

    bigdata-country-analysis/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md

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
