# Bigdata Sector Playbook

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **sector investment playbook** — the KPIs that matter, the live debates, valuation context, and an actionable setup for a sector — powered by **Bigdata.com MCP**.

---

## What It Produces

- Sector-specific KPI framework, not generic multiples
- How to value companies in this sector and why
- The live debates and where consensus sits on each
- Valuation context versus the sector's own history
- Sub-industry map and where in the cycle each sits
- Screening criteria and red flags specific to the sector
- Actionable setup: what to own, what to avoid, what to watch
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:sector-playbook

---

## Structure

    bigdata-sector-playbook/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── consumer-retail.md
    │   └── energy.md
    │   └── financials-banks.md
    │   └── healthcare-pharma.md
    │   └── industrials.md
    │   └── porter-five-forces.md
    │   └── reits.md
    │   └── sector-routing.md
    │   └── sector-selection-guide.md
    │   └── technology-saas.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `bigdata_search`, `find_securities`, `bigdata_company_tearsheet`, `bigdata_events_calendar`.

---

## Related Skills

- **Sector analysis**
- **Cross-sector comparison**
- **Peer comparables**
- **Investment memo**

---

## License

See the root `LICENSE` file of the plugin repository for details.
