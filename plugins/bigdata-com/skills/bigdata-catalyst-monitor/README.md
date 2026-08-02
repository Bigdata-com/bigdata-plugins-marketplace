# Bigdata Catalyst Monitor

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **catalyst monitor** — the dated events that could move a company over the next few quarters, with likely market implications and watch points — powered by **Bigdata.com MCP**.

---

## What It Produces

- Dated catalyst calendar over the next 2-4 quarters
- Scheduled events: earnings, investor days, index reviews, lock-up and patent expiries
- Unscheduled but foreseeable catalysts: regulatory decisions, litigation milestones, product cycles
- Per catalyst: likely direction, magnitude, confidence, and what to watch
- Ranked by expected impact, not by date alone
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:catalyst-monitor

---

## Structure

    bigdata-catalyst-monitor/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── epic-framework.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_events_calendar`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Company brief**
- **Earnings preview**
- **Quick take**
- **Scenario analysis**

---

## License

See the root `LICENSE` file of the plugin repository for details.
