# Bigdata Post-IPO Day 179

Part of the **Bigdata.com** plugin.

A focused skill that produces a balanced **day-179 post-IPO note** on the 180-day lock-up expiry and the supply overhang it releases — powered by **Bigdata.com MCP**.

---

## What It Produces

- Lock-up terms from the filing: expiry date, covered holders, share count, early-release provisions
- Float and overhang math: post-expiry float and days-to-trade
- Selling-intention signals: secondary filings, 10b5-1 plans, prior insider sales
- Positioning into the event: short interest, borrow, options skew
- Historical lock-up-expiry effect with recent analogs
- Two-sided read and dated watch points
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:post-ipo-day179

---

## Structure

    bigdata-post-ipo-day179/
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
