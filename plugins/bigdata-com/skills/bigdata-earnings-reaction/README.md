# Bigdata Earnings Reaction

Part of the **Bigdata.com** plugin.

A focused skill that produces a tight **post-earnings reaction note** — results versus expectations, guidance changes, thesis status, and the revised view — powered by **Bigdata.com MCP**.

---

## What It Produces

- Headline numbers versus consensus with beat/miss magnitude
- What mattered: positive and negative surprises
- Guidance update table, prior versus new
- Thesis check: Intact / Strengthened / Weakened / Broken with evidence
- Estimate revisions needed, including price target
- Valuation update, pre- versus post-earnings
- Quality signals for the quarter
- Action and next key date
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:earnings-reaction

---

## Structure

    bigdata-earnings-reaction/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── quality-of-earnings.md
    └── scripts/
        └── scenario_probability.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_events_calendar`, `bigdata_search`.

---

## Related Skills

- **Earnings digest**
- **Earnings preview**
- **Quick take**
- **Investment memo**

---

## License

See the root `LICENSE` file of the plugin repository for details.
