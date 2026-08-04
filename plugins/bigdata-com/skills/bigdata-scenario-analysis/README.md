# Bigdata Scenario Analysis

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **scenario analysis** — bull, base, and bear cases with explicit assumptions, probabilities, and expected-value implications — powered by **Bigdata.com MCP**.

---

## What It Produces

- Driver identification: the 2-3 variables the scenarios actually turn on
- Per-scenario assumptions at the line-item level
- Probability weights with justification, summing to 100%
- Value or price per scenario with the bridge shown
- Probability-weighted expected value and expected return versus spot
- Upside/downside skew and risk-reward ratio
- What would move probabilities between scenarios
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:scenario-analysis

---

## Structure

    bigdata-scenario-analysis/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── dcf-methodology.md
    │   └── reverse-dcf.md
    │   └── thesis-construction.md
    └── scripts/
        └── dcf_model.py
        └── scenario_probability.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Valuation snapshot**
- **Investment memo**
- **Variant perception**
- **Risk assessment**

---

## License

See the root `LICENSE` file of the plugin repository for details.
