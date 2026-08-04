# Bigdata G7 Comparison

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **G7 comparison** — growth, inflation, policy, market positioning, and investment implications across the seven economies — powered by **Bigdata.com MCP**.

---

## What It Produces

- Side-by-side G7 indicator table: GDP, inflation, unemployment, policy rate, fiscal position
- Central bank stance and rate-path divergence across the Fed, ECB, BoJ, BoE, BoC
- Relative market positioning: equity valuations, yields, currencies
- Divergence and convergence themes across the bloc
- Ranked attractiveness with an allocation view, optionally focused on equities, rates, FX, or credit
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:g7-comparison

---

## Structure

    bigdata-g7-comparison/
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
