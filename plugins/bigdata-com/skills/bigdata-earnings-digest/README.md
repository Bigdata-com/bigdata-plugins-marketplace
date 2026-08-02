# Bigdata Earnings Digest

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **post-earnings digest** — a deep
dive on a public company's latest reported quarter — powered by
**Bigdata.com MCP**.

---

## What It Produces

- **Executive summary** — headline result, what changed for the bull/bear
  debate, what's priced in next
- **Thesis check** — whether the quarter strengthened, weakened, or left
  unchanged each side of the debate (or Intact / Strengthened / Weakened /
  Broken against a thesis the user supplies)
- **Quality signals** — OCF vs NI, DSO, inventory, guidance credibility,
  each with a forward "watch for" note
- **Sentiment & positioning** — quantified sentiment, options/short,
  institutional flows, insider activity
- **Financial results** — headline numbers vs consensus, revenue and
  margin analysis, segments and operating KPIs
- **Management guidance and commentary** — forward guidance vs consensus,
  strategic priorities, market conditions
- **Cash flow and balance sheet** — OCF, FCF, leverage, capital allocation
- **Surprises vs expectations** — magnitude in % / bps and sigma, labelled
  sustainable vs one-time
- **Analyst reactions** — rating and price-target changes
- **Scenario refresh** — post-print bull/base/bear with a
  probability-weighted expected value, math shown
- **Valuation cross-check** — does the reaction fit the surprise and guidance?
- **Sources** with inline citations, plus the standard Bigdata.com footer
  and disclaimer

---

## Usage

Ask in natural language, for example:

    Analyze NVIDIA's earnings
    Create an earnings digest for Alphabet
    How did Apple do last quarter?
    Did Tesla beat or miss?

Or, within the plugin, via the namespaced command:

    /bigdata-com:earnings-digest NVIDIA

---

## Structure

    bigdata-earnings-digest/
    ├── SKILL.md                        # Workflow, triggers, quality bar
    ├── agents/openai.yaml              # OpenAI interface manifest
    ├── assets/report-template.md       # Mandatory output structure + footer
    ├── references/                     # Optional analytical depth
    │   ├── quality-of-earnings.md
    │   └── thesis-construction.md
    └── scripts/scenario_probability.py # Optional scripted EV math

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent
platform. The skill uses `find_securities`,
`bigdata_company_tearsheet`, `bigdata_events_calendar`, and
`bigdata_search`.

---

## Related Skills

- **Earnings preview** — forward-looking, ahead of the print
- **Earnings reaction** — short note against a stated thesis
- **Company brief** — 30 days of all developments
- **Valuation snapshot** — "what is it worth"
- **Risk assessment** — structured risk mapping

---

## License

See the root `LICENSE` file of the plugin repository for details.
