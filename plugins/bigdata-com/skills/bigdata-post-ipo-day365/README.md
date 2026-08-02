# Bigdata Post-IPO Day 365

Part of the **Bigdata.com** plugin.

A focused skill that produces a balanced **day-365 post-IPO note** on the 366-day founder/investor lock-up expiry and float expansion toward 15-20% — powered by **Bigdata.com MCP**.

---

## What It Produces

- Staggered lock-up structure from the filing, including dual-class voting
- Float expansion math and days-to-trade ceiling
- Offsetting float-adjusted index reweight demand, math shown and netted against supply
- Realistic supply assessment: gradual founder diversification vs VC distribution
- Governance angle: voting control retained after economic sell-down
- Two-sided read and dated watch points
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:post-ipo-day365

---

## Structure

    bigdata-post-ipo-day365/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── post-ipo-common.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`, `bigdata_events_calendar`, plus web search for market data and index methodology.

---

## Related Skills

- **Pre-IPO analysis**
- **Post-IPO day 1**
- **Post-IPO day 14**
- **Post-IPO day 179**
- **Post-IPO day 365**

---

## License

See the root `LICENSE` file of the plugin repository for details.
