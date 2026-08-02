# Bigdata Investment Memo

Part of the **Bigdata.com** plugin.

A focused skill that produces a full **investment memo** — thesis, variant perception, valuation, risks, catalysts, and an explicit recommendation with conviction — powered by **Bigdata.com MCP**.

---

## What It Produces

- Recommendation and conviction level up front
- EPIC-filtered primary drivers
- Variant perception versus consensus (FaVeS: fundamentals, valuation, sentiment)
- Earnings quality and competitive-moat assessment
- Valuation by the method that fits the business, with a secondary cross-check
- Bull / base / bear scenarios with probabilities and a probability-weighted value
- Key risks, what would change the view, and dated catalysts
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:investment-memo

---

## Structure

    bigdata-investment-memo/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── capital-allocation.md
    │   └── dcf-methodology.md
    │   └── epic-framework.md
    │   └── faves-framework.md
    │   └── graham-dodd-principles.md
    │   └── moat-taxonomy.md
    │   └── multiples-framework.md
    │   └── quality-of-earnings.md
    │   └── reverse-dcf.md
    │   └── sector-routing.md
    │   └── sum-of-parts.md
    │   └── thesis-construction.md
    └── scripts/
        └── dcf_model.py
        └── earnings_quality.py
        └── peer_comparables.py
        └── reverse_dcf.py
        └── scenario_probability.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`, `bigdata_events_calendar`.

---

## Related Skills

- **Quick take**
- **Valuation snapshot**
- **Variant perception**
- **Scenario analysis**
- **Risk assessment**
- **Moat & governance review**

---

## License

See the root `LICENSE` file of the plugin repository for details.
