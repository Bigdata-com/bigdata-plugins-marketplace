# Bigdata Country-Sector Analysis

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **country-sector analysis** — a specific sector inside a specific country or region, combining economic backdrop, sector trends, and company fundamentals — powered by **Bigdata.com MCP**.

---

## What It Produces

- Country macroeconomic backdrop: GDP, inflation, rates, policy
- Country-specific sector trends, valuations, and investment flows
- Country-domiciled sector leaders with tearsheet fundamentals and geographic revenue confirmation
- Policy, regulation, subsidies, tariffs, and foreign-investment restrictions
- Valuation relative to global sector peers
- Upcoming earnings for the country's sector leaders
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:country-sector-analysis

---

## Structure

    bigdata-country-sector-analysis/
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
