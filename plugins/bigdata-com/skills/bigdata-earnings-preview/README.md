# Bigdata Earnings Preview

Part of the **Bigdata.com** plugin.

A focused skill that produces an institutional-quality, forward-looking
**earnings preview** for a public company ahead of its next earnings
call — powered by **Bigdata.com MCP**.

---

## What It Produces

A cited, decision-ready preview containing:

- **EPIC driver table** — the 2–3 factors that actually matter this print,
  with material / forecastable / consensus-blind-spot / consensus-gap tests
- **Earnings quality quick screen** — OCF/NI, DSO, GAAP vs non-GAAP, each
  with a forward "watch for" note
- **Consensus estimates and recent performance context**
- **Sentiment & positioning table** — quantified sentiment, options,
  short interest, 13F changes, insider transactions, sell-side posture
- **Recent developments** including legal and regulatory items
- **Industry trends and sector dynamics**
- **What's priced in** plus a valuation cross-check vs history and peers
- **Variant perception (FaVeS)** — fundamentals, valuation, sentiment
- **Bull and bear cases** tied to specific consensus line items
- **Scenario analysis** — bull/base/bear with probabilities and a
  probability-weighted expected value, math shown
- **Key metrics to watch** and management guidance focus areas
- **Sources** with inline citations, plus the standard Bigdata.com footer
  and disclaimer

---

## Usage

Ask in natural language, for example:

    Create an earnings preview for NVIDIA
    Preview Alphabet's next quarter
    What should I watch when Apple reports?

Or, within the plugin, via the namespaced command:

    /bigdata-com:earnings-preview NVIDIA

---

## Structure

    bigdata-earnings-preview/
    ├── SKILL.md                     # Workflow, triggers, quality bar
    ├── agents/openai.yaml           # OpenAI interface manifest
    ├── assets/report-template.md    # Mandatory output structure + footer
    ├── references/                  # Optional analytical depth
    │   ├── epic-framework.md
    │   ├── faves-framework.md
    │   ├── quality-of-earnings.md
    │   ├── reverse-dcf.md
    │   └── thesis-construction.md
    └── scripts/scenario_probability.py   # Optional scripted EV math

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent
platform. The skill uses `find_securities`,
`bigdata_company_tearsheet`, `bigdata_events_calendar`, and
`bigdata_search`.

---

## Related Skills

- **Earnings digest / earnings reaction** — after results are reported
- **Company brief** — retrospective 30-day summary
- **Valuation snapshot** — "what is it worth" with no earnings event
- **Risk assessment** — comprehensive risk mapping

---

## License

See the root `LICENSE` file of the plugin repository for details.
