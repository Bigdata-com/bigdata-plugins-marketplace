# Bigdata Company Brief

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **30-day company brief** — what
happened at a public company over the past month, and why each item
matters — powered by **Bigdata.com MCP**.

---

## What It Produces

- **Executive summary** led by the ranked top 2–3 developments
- **Competitive context** — concentration, pricing power, disruption risk
- **Categorized developments**, each with date, facts, and a
  bullish/bearish/neutral implication tied to a value driver:
  - Financial results
  - Product / tech launches
  - M&A and partnerships
  - Regulatory and legal updates
  - Management changes
  - Other material events
- **Overall assessment** with net tilt, key risk, and next catalyst
- **Sources** with inline citations, plus the standard Bigdata.com footer
  and disclaimer

---

## Usage

Ask in natural language, for example:

    Create a company brief for NVIDIA
    What's happening with Alphabet?
    Catch me up on Apple

Or, within the plugin, via the namespaced command:

    /bigdata-com:company-brief NVIDIA

---

## Structure

    bigdata-company-brief/
    ├── SKILL.md                       # Workflow, triggers, quality bar
    ├── agents/openai.yaml             # OpenAI interface manifest
    ├── assets/report-template.md      # Output structure + footer
    └── references/
        └── porter-five-forces.md      # Industry-structure mental model

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent
platform. The skill uses `find_securities`,
`bigdata_company_tearsheet`, and `bigdata_search`.

---

## Related Skills

- **Earnings preview** — forward-looking, ahead of the print
- **Earnings digest / earnings reaction** — after results are reported
- **Valuation snapshot** — "what is it worth"
- **Risk assessment** — structured risk mapping
- **Investment memo** — full thesis and variant perception

---

## License

See the root `LICENSE` file of the plugin repository for details.
