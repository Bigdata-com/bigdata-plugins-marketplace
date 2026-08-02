# Bigdata Valuation Snapshot

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **valuation snapshot** — what a public company is worth and what the current price already embeds — powered by **Bigdata.com MCP**.

---

## What It Produces

- Current multiples vs ~5-year range and peer median
- Implied expectations at the current price (reverse-DCF mindset)
- 2-3 value drivers that dominate the valuation debate
- Cheap / fair / rich verdict against embedded expectations
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:valuation-snapshot

---

## Structure

    bigdata-valuation-snapshot/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── dcf-methodology.md
    │   └── multiples-framework.md
    │   └── reverse-dcf.md
    └── scripts/
        └── dcf_model.py
        └── reverse_dcf.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Peer comparables**
- **Scenario analysis**
- **Investment memo**
- **Variant perception**

---

## License

See the root `LICENSE` file of the plugin repository for details.
