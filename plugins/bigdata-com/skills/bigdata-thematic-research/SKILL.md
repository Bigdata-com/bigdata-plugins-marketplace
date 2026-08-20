---
name: bigdata-thematic-research
description: >
  Research a macro investment theme using Bigdata.com data — scope and sub-themes, investment
  implications, sector impact, named beneficiaries and vulnerable losers with tearsheet
  fundamentals, the policy and regulatory dimension, geographic impact, and concrete
  implementation ideas. Covers themes such as AI, energy transition, inflation and rates,
  deglobalization and reshoring, demographics, geopolitical risk, and fiscal policy. Triggers:
  "research the X theme", "X investment implications", "who benefits from X", "how do I play
  X", "AI / energy transition / deglobalization theme", "thematic view on X".
---

# Bigdata Thematic Research

Cross-sector research on one macro theme, ending in implementable ideas. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the subject is a theme that cuts across sectors or borders. Not this skill when:

| Request | Use instead |
|---------|-------------|
| One sector's performance and outlook | Sector analysis |
| Sectors ranked against each other | Cross-sector comparison |
| One country's economy | Country analysis |
| One company exposed to the theme | Company brief / investment memo |

Common themes: AI and technology transformation, energy transition and clean tech, inflation and interest rates, deglobalization and reshoring, demographic shifts, geopolitical risk, fiscal policy and government spending.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Theme coverage, implications, policy, market impact | None |
| `find_securities` | Entity ids for the most exposed companies | None |
| `bigdata_company_tearsheet` | Fundamentals and exposure of beneficiaries and losers | `find_securities` |
| `bigdata_country_tearsheet` | Geographic impact where available | None |

**Required on every call:** pass `plugin_slug: "bigdata-thematic-research"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-thematic-research`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Define the theme scope

State the boundaries and the sub-themes explicitly before searching. An unbounded theme produces an unbounded report — this step is what keeps the deliverable usable.

### Step 2 — Search the theme (5–10 queries)

- "[Theme] investment implications outlook"
- "[Theme] winners beneficiaries stocks"
- "[Theme] risks losers vulnerable"
- "[Theme] policy government regulation"
- "[Theme] market impact analysis"
- "[Theme] sector exposure"

### Step 3 — Beneficiaries and casualties

Use `find_securities` and `bigdata_company_tearsheet` for the most exposed companies on **both** sides. A theme note that names only winners is a pitch, not research — quantify the exposure where the data allows (revenue share, capex tied to the theme, contract backlog).

### Step 4 — Geographic impact

Use `bigdata_country_tearsheet` (or search) for the countries most affected, positively and negatively.

### Step 5 — Implementation

Turn the analysis into concrete ways to express the theme: direct beneficiaries, second-order plays, avoided exposures, and what would invalidate the theme.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables:

- Theme scope and sub-themes stated up front and held to
- **Both** beneficiaries and losers named, with exposure quantified where possible
- Policy dimension addressed — most macro themes are policy-driven
- Implementation section present: how to express the theme, and what would invalidate it
- Every claim from a source carries an inline citation and appears in the Sources table
