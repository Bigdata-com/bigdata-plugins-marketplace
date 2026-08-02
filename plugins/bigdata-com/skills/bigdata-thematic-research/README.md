# Bigdata Thematic Research

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **thematic research note** — a macro investment theme, its sector impact, beneficiaries, and implementation ideas — powered by **Bigdata.com MCP**.

---

## What It Produces

- Theme scope and sub-themes, explicitly bounded
- Investment implications, winners, and vulnerable losers
- Most-exposed companies with tearsheet fundamentals
- Policy and regulatory dimension
- Geographic impact
- Implementation ideas and how to express the theme
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:thematic-research

---

## Structure

    bigdata-thematic-research/
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
