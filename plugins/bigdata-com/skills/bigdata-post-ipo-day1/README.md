# Bigdata Post-IPO Day 1

Part of the **Bigdata.com** plugin.

A focused skill that produces a balanced **first-trading-day post-IPO reaction note** — price discovery against the offer, demand and stabilization signals, and the aftermarket setup — powered by **Bigdata.com MCP**.

---

## What It Produces

- Deal anchor: offer price vs range, shares, greenshoe, implied market cap and EV
- Day-1 reconstruction: open, intraday range, close, volume, first-day return
- Demand and float mechanics, including stabilization activity
- Valuation reset at the close vs peers
- Sentiment and the quiet-period coverage gap
- Dated post-IPO timeline: initiations, index inclusion, lock-up expiries
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:post-ipo-day1

---

## Structure

    bigdata-post-ipo-day1/
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
