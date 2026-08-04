# Bigdata Peer Comparables

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **peer comparables analysis** — how a company screens against its peer set on valuation, growth, profitability, and sentiment — powered by **Bigdata.com MCP**.

---

## What It Produces

- Peer set construction with an explicit rationale for inclusion and exclusion
- Comparables table: valuation multiples, growth, margins, returns, leverage
- Peer median and quartile positioning per metric
- Premium / discount decomposition — is it justified by fundamentals?
- Sentiment and sell-side posture across the peer set
- Relative attractiveness verdict with the specific drivers
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:peer-comparables

---

## Structure

    bigdata-peer-comparables/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── multiples-framework.md
    │   └── sector-routing.md
    └── scripts/
        └── peer_comparables.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Valuation snapshot**
- **Sector analysis**
- **Investment memo**
- **Variant perception**

---

## License

See the root `LICENSE` file of the plugin repository for details.
