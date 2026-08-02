# Bigdata Quick Take

Part of the **Bigdata.com** plugin.

A focused skill that produces a concise **PM-style quick take** — current view, key drivers, risks, and the near-term setup, in one page — powered by **Bigdata.com MCP**.

---

## What It Produces

- One-line current view
- The 2-3 drivers that actually matter right now
- Key risks and what would change the view
- Near-term setup and next catalyst
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:quick-take

---

## Structure

    bigdata-quick-take/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── epic-framework.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Company brief**
- **Investment memo**
- **Valuation snapshot**
- **Catalyst monitor**

---

## License

See the root `LICENSE` file of the plugin repository for details.
