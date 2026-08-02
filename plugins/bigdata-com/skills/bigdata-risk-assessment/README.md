# Bigdata Risk Assessment

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited, comprehensive **risk assessment** of a public company — six risk categories rated by likelihood and impact — powered by **Bigdata.com MCP**.

---

## What It Produces

- Financial health baseline and distress screen (Altman Z-style) when leverage is stretched
- Moat durability and erosion risk
- Official 10-K risk factors and recent 8-K material events
- Six rated risk categories: regulatory/legal, competitive, operational, financial, macro, management/governance
- Likelihood x impact priority matrix with mitigation status
- Scenario bridge tying the risk profile to value drivers
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:risk-assessment

---

## Structure

    bigdata-risk-assessment/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── capital-allocation.md
    │   └── moat-taxonomy.md
    │   └── red-flags-checklist.md
    │   └── thesis-construction.md
    └── scripts/
        └── earnings_quality.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Company brief**
- **Earnings quality screen**
- **Moat & governance review**
- **Investment memo**

---

## License

See the root `LICENSE` file of the plugin repository for details.
