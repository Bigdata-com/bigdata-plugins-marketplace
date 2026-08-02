# Bigdata Cross-Sector Comparison

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **cross-sector comparison** — relative valuations, earnings growth, cycle positioning, and rotation recommendations — powered by **Bigdata.com MCP**.

---

## What It Produces

- Side-by-side sector metrics: valuation, growth, sentiment
- Bellwether-level fundamentals per sector
- Economic-cycle positioning: cyclical vs defensive, rate sensitivity
- Profitability and ROIC spread vs history — peak, mid-cycle, or trough earnings power
- Rotation recommendation with overweight / underweight calls
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:cross-sector

---

## Structure

    bigdata-cross-sector/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── porter-five-forces.md

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
