# Bigdata Regional Comparison

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **regional comparison** — economic indicators, market performance, and allocation recommendations across regions — powered by **Bigdata.com MCP**.

---

## What It Produces

- Economic data by region: growth, inflation, policy, labor
- Comparative analysis across developed and emerging markets
- Regional equity valuations and market performance
- Cross-asset views: fixed income and currency per region
- Allocation recommendation with rationale
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:regional-comparison

---

## Structure

    bigdata-regional-comparison/
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
