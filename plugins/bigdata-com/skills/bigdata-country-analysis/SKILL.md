---
name: bigdata-country-analysis
description: >
  Produce a deep country economic analysis using Bigdata.com data — GDP, inflation, monetary
  policy, labor markets, debt mechanics, and investment implications. Goes beyond a
  point-in-time snapshot: structural and historical context (sector transformation, labor
  productivity), debt composition and servicing, tax-to-GDP and public financial management, a
  substantive macro-and-micro labor section, market implications across equities, rates,
  currency and FDI, and a dedicated sourced policy-recommendations section. Suits institutional,
  multilateral, and academic audiences. Triggers: "economic outlook for X", "analyze X's
  economy", "country analysis of X", "how is X's economy doing", "X GDP inflation outlook",
  "X fiscal position", "X monetary policy outlook".
---

# Bigdata Country Analysis

Analytical country economic profile with policy depth. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the subject is one country's economy. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Several regions or blocs compared | Regional comparison |
| The G7 specifically | G7 comparison |
| A sector inside a country | Country-sector analysis |
| A cross-border macro theme | Thematic research |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_country_tearsheet` | Economic data, calendar, comparisons | None |
| `bigdata_search` | Indicators, policy, structural context, market implications | None |

If `bigdata_country_tearsheet` is unavailable or fails, complete the whole analysis with `bigdata_search` using the targeted queries below. Search **each indicator separately** rather than in one broad query.

## Workflow

### Step 1 — Core economic indicators

- "[Country] GDP growth economic outlook 2026"
- "[Country] inflation CPI consumer prices trends"
- "[Country] central bank interest rates monetary policy"
- "[Country] unemployment rate labor market"
- "[Country] fiscal policy government budget"

### Step 2 — Monetary policy

- "[Country] central bank rate decision outlook"
- "[Country] monetary policy inflation target"
- "Fed / ECB / BOJ / PBOC policy rate path expectations"

### Step 3 — Economic calendar and events

- "[Country] economic data releases calendar"
- "[Country] central bank meeting schedule"
- "[Country] GDP CPI employment report dates"

### Step 4 — Structural and historical context (required for depth)

A point-in-time-only report fails this deliverable's bar.

- "[Country] sector transformation structural change agriculture industry services"
- "[Country] labor productivity by sector comparison"
- "[Country] economic structure evolution [time range, e.g. 1990 2020]"
- "[Country] sectoral GDP share history"
- "[Country] employment by sector productivity growth"

### Step 5 — Debt composition, tax-to-GDP, and PFM (required for depth)

- "[Country] public debt composition domestic external"
- "[Country] debt servicing interest cost weighted average rate"
- "[Country] debt crowding out private sector"
- "[Country] public financial management PFM reform budget execution"
- "[Country] tax revenue GDP fiscal consolidation"
- "[Country] tax to GDP ratio tax burden comparison"

### Step 6 — Labor market in depth

Never leave the labor section as a one-line "macro good, micro bad".

- "[Country] labor market informality underemployment"
- "[Country] youth unemployment sectoral employment"
- "[Country] real wages productivity labor share"
- "[Country] employment growth by sector"

### Step 7 — Policy and reform context

Grounds the recommendations section — do not write recommendations without it.

- "[Country] fiscal consolidation tax reform recommendations"
- "[Country] debt management strategy IMF World Bank"
- "[Country] structural reform priorities"
- "[Country] demographic dividend youth bulge policy"

### Step 8 — Market implications and FDI

- "[Country] equity market outlook"
- "[Country] bond market yields spreads"
- "[Country] currency forex outlook"
- "[Country] FDI foreign direct investment inflows outflows"
- "[Country] FDI trajectory outlook greenfield M&A"

### Step 9 — Regional context (if applicable)

- "[Country] vs peers economic performance"
- "G7 economic comparison GDP inflation rates"
- "developed markets emerging markets outlook"

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

This deliverable is written for institutional, multilateral, and academic readers. Non-negotiables:

- **Structural and historical context** present — sector transformation over time, labor productivity by sector
- **Debt and PFM mechanics** quantified: composition, servicing burden, tax-to-GDP versus peers or IMF/OECD benchmarks
- **Labor market** covered at both macro and micro level (informality, underemployment, youth, real wages vs productivity)
- **Dedicated policy recommendations section**, structured by pillar — fiscal consolidation, debt management, monetary policy, structural reforms — with specific targets and mechanisms where available, each sourced
- No shallow, point-in-time-only narrative
