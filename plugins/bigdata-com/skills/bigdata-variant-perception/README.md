# Bigdata Variant Perception

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **variant perception** — an explicit, falsifiable statement of where your view differs from consensus, framed on fundamentals, valuation, and sentiment — powered by **Bigdata.com MCP**.

---

## What It Produces

- Consensus baseline established from estimates and sell-side posture
- EPIC filter applied to candidate differentiators
- FaVeS framing: fundamentals, valuation, sentiment
- The variant view stated as a specific, falsifiable claim with a time horizon
- What the market is missing and why it persists
- Evidence for the view and what would disprove it
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:variant-perception

---

## Structure

    bigdata-variant-perception/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── epic-framework.md
    │   └── faves-framework.md
    │   └── reverse-dcf.md
    │   └── thesis-construction.md
    └── scripts/
        └── reverse_dcf.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Investment memo**
- **Valuation snapshot**
- **Scenario analysis**
- **Quick take**

---

## License

See the root `LICENSE` file of the plugin repository for details.
