---
name: bigdata-country-sector-analysis
description: >
  Analyze a specific sector inside a specific country or region using Bigdata.com data —
  combining the macroeconomic backdrop (GDP, inflation, rates, policy), country-specific sector
  trends and valuations, fundamentals of country-domiciled sector leaders confirmed by
  geographic revenue exposure, the policy and regulatory environment including subsidies,
  tariffs and foreign-investment rules, and valuation versus global sector peers. Use whenever
  a request names BOTH a sector AND a country or region. Triggers: "macro analysis of X in Y",
  "European financials outlook", "US technology sector view", "India consumer sector",
  "China EV sector", "Japanese semiconductor industry", "[sector] in [country]".
---

# Bigdata Country-Sector Analysis

Sector view anchored to one country or region. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the request combines **both** a sector and a country/region — "Technology investment in the USA", "European financials outlook", "India consumer sector", "China EV". Not this skill when:

| Request | Use instead |
|---------|-------------|
| A sector globally, with no country anchor | Sector analysis |
| A country's economy, with no sector anchor | Country analysis |
| Several sectors compared | Cross-sector comparison |
| Several regions compared | Regional comparison |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Country macro backdrop, country-sector trends, policy | None |
| `find_securities` | Entity ids for country-domiciled sector leaders | None |
| `bigdata_company_tearsheet` | Fundamentals and geographic revenue split | `find_securities` |
| `bigdata_events_calendar` | Upcoming earnings for those leaders | `find_securities` |
| `bigdata_country_tearsheet` | Economic data where available | None |

**Required on every call:** pass `plugin_slug: "bigdata-country-sector-analysis"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-country-sector-analysis`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Country economic context

- "[Country] economic outlook GDP growth 2026"
- "[Country] inflation interest rates monetary policy"
- "[Country] central bank rate decision outlook"

Extract GDP growth, inflation, interest rates, and the policy environment.

### Step 2 — Country-specific sector news

Query **country + sector** together:

- "[Country] [Sector] sector outlook 2026"
- "[Country] [Sector] industry trends performance"
- "[Country] [Sector] regulatory policy government"
- "[Country] [Sector] investment flows foreign domestic"
- "[Country] [Sector] earnings revenue growth"
- "[Country] [Sector] valuations multiples"
- "[Country] [Sector] headwinds risks challenges"
- "[Country] [Sector] tailwinds opportunities growth drivers"

### Step 3 — Country-domiciled sector leaders

Use `find_securities` for 5–10 companies **headquartered in** or **primarily operating in** that country, then `bigdata_company_tearsheet` for each:

- Revenue breakdown by geography — **confirm the country exposure is real**, not just a listing venue
- Financial metrics and performance
- Analyst estimates and sentiment
- Hiring trends as a workforce signal

### Step 4 — Events

Use `bigdata_events_calendar` for upcoming earnings across those leaders; filter by the country's exchange for a market-wide scan.

### Step 5 — Policy and regulation

- "[Country] [Sector] regulation policy 2026"
- "[Country] government [Sector] subsidies incentives"
- "[Country] [Sector] trade tariffs exports"
- "[Country] [Sector] foreign investment restrictions"

### Step 6 — Synthesize the macro-sector view

Combine the country backdrop, the country-specific sector trends, company fundamentals, the policy environment, and **valuation relative to global sector peers**. The value of this deliverable is the intersection — a generic sector view with a country label pasted on top does not pass.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables:

- Country macro backdrop **and** sector detail both present — neither alone is the deliverable
- Company selection justified by domicile or operations, with geographic revenue confirming it
- Policy, subsidies, tariffs, and foreign-investment rules addressed — these usually dominate country-sector outcomes
- Valuation framed against **global** sector peers, so the country premium or discount is visible
- Every claim from a source carries an inline citation and appears in the Sources table
