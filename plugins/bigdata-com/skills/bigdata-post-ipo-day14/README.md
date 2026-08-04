# Bigdata Post-IPO Day 14

Part of the **Bigdata.com** plugin.

A focused skill that produces a balanced **day-14 post-IPO note** on potential NASDAQ-100 fast-track inclusion and the passive-flow demand it would create — powered by **Bigdata.com MCP**.

---

## What It Produces

- Two-week trading status: price vs offer and day-1 close, ADV, free float
- Eligibility check against Nasdaq's current published methodology (cited, not assumed)
- Float-adjusted index weight and implied passive demand, math shown
- Days-to-cover versus ADV — the index-effect magnitude
- Historical index-effect analogs and reversal risk
- Watch points: effective date, rebalance mechanics, lock-ups, first earnings
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:post-ipo-day14

---

## Structure

    bigdata-post-ipo-day14/
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
