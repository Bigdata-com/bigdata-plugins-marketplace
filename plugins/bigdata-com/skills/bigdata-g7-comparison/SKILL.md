---
name: bigdata-g7-comparison
description: >
  Benchmark the seven G7 economies side by side using Bigdata.com data — the United States,
  Japan, Germany, the United Kingdom, France, Italy, and Canada. Produces a like-for-like
  indicator table (GDP, inflation, unemployment, policy rate, fiscal position), central bank
  stance and rate-path divergence across the Fed, BoJ, ECB, BoE and BoC, relative market
  positioning across equities, rates and currencies, the divergence and convergence themes
  running through the bloc, and a ranked allocation view — optionally focused on equities,
  rates, FX or credit. Triggers: "compare G7 economies", "G7 comparison", "G7 outlook",
  "how do the G7 economies compare", "G7 growth and inflation", "G7 central bank divergence".
---

# Bigdata G7 Comparison

Side-by-side benchmark of the seven G7 economies. Use Bigdata.com plugin tools for every fact.

**Members:** United States, Japan, Germany, United Kingdom, France, Italy, Canada. Note the euro-area members (Germany, France, Italy) share the ECB's policy rate — differentiate them on fiscal position, growth, and market pricing rather than on monetary policy.

**Use this skill when** the G7 is the frame. Not this skill when:

| Request | Use instead |
|---------|-------------|
| One G7 country in depth | Country analysis |
| Broader or different regions (EM, Asia ex-Japan) | Regional comparison |
| Sectors rather than economies | Cross-sector comparison |
| A macro theme across borders | Thematic research |

If the user supplied a focus (equities, rates, FX, credit), lead the market-implications section with it. Otherwise cover all four at a broad level.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_country_tearsheet` | Economic data and built-in G7 comparison where available | None |
| `bigdata_search` | Indicators, policy, market positioning per member | None |

If `bigdata_country_tearsheet` is unavailable or fails, complete the analysis with `bigdata_search` alone.

## Workflow

### Step 1 — Indicators for each member

Pull the **same** indicators for all seven so the table is like-for-like: GDP growth, CPI inflation, unemployment, policy rate, and fiscal position (deficit and debt/GDP).

- "[Country] GDP growth economic outlook 2026"
- "[Country] inflation CPI consumer prices"
- "[Country] unemployment labor market"
- "[Country] government deficit debt to GDP"

Where a figure is unavailable for one member, write "Not available" rather than leaving the comparison lopsided.

### Step 2 — Central bank stance and rate paths

- "Fed ECB BOJ BOE rate decision outlook"
- "[Country] central bank policy rate path expectations"
- "G7 monetary policy divergence"

Capture the last action, current guidance, and market-implied path for the **Fed, BoJ, ECB, BoE, and BoC**. Policy divergence across the bloc is usually the single most important driver of relative returns — treat it as a headline finding, not a footnote.

### Step 3 — Comparative economic analysis

- "G7 economic comparison GDP growth rates"
- "G7 inflation comparison"
- "G7 fiscal position debt sustainability"

Identify who is leading and lagging on growth, who is winning and losing the inflation fight, and whose fiscal position constrains policy.

### Step 4 — Market positioning

- "G7 equity market valuations comparison"
- "G7 sovereign bond yields comparison"
- "USD EUR JPY GBP CAD currency outlook"
- "credit spreads investment grade high yield [region]"

Cover equity valuations, 10-year yields and curve shape, currency levels and outlook, and credit where relevant.

### Step 5 — Divergence and convergence themes

Name the 2–3 themes running through the bloc — for example policy divergence, fiscal stress, energy exposure, demographics, or trade policy — and which members each helps or hurts.

### Step 6 — Ranked view

Rank the seven on relative attractiveness for the user's focus (or overall), with a one-line reason each and the key risk to the ranking.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables:

- All seven members present in the indicator table, on the **same** metrics, with gaps marked "Not available"
- Euro-area members differentiated on fiscal position, growth, and market pricing — not treated as one country
- Central bank divergence treated as a headline driver
- A ranked view delivered, with reasons and the key risk
- Every claim from a source carries an inline citation and appears in the Sources table
