# Bigdata Pre-IPO Analysis

Part of the **Bigdata.com** plugin.

A focused skill that produces a balanced **pre-IPO research note** on an upcoming listing — deal structure, financials, valuation framing, and bull/bear debates, with no buy/avoid call — powered by **Bigdata.com MCP**.

---

## What It Produces

- Deal structure from the S-1/F-1: price range, shares, greenshoe, implied valuation, underwriters, lock-ups, share classes
- Two fiscal years plus latest interim financials
- Business model, segments, customers, funding history and last private round
- TAM, competitive set, and 3-6 listed comparables
- IPO window conditions and recent sector debuts' aftermarket performance
- Sentiment over the last 90 days
- Balanced bull/bear debates and watch points — no recommendation
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:pre-ipo-analysis

---

## Structure

    bigdata-pre-ipo-analysis/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_search`, `bigdata_company_tearsheet`, plus web search for filings and comparables.

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
