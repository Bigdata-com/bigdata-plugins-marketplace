# Bigdata Moat & Governance Review

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **moat and governance review** — how durable the competitive advantage is and whether management can be trusted with the capital — powered by **Bigdata.com MCP**.

---

## What It Produces

- Moat identification by type, with the evidence for each
- Moat strength and durability: ROIC versus WACC, pricing power, share trend
- Competitive advantage period estimate and erosion signals
- Industry structure context (five forces)
- Capital allocation track record: M&A, buybacks, dividends, reinvestment
- Governance: board independence, dual roles, compensation design, related-party exposure, insider activity
- Combined verdict on moat durability and management quality
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:moat-governance-review

---

## Structure

    bigdata-moat-governance-review/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── capital-allocation.md
    │   └── moat-taxonomy.md
    │   └── porter-five-forces.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Risk assessment**
- **Investment memo**
- **Sector playbook**
- **Valuation snapshot**

---

## License

See the root `LICENSE` file of the plugin repository for details.
