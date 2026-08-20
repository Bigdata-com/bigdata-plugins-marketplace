---
name: bigdata-regional-comparison
description: >
  Compare regions or blocs using Bigdata.com data — economic indicators, market performance,
  and cross-asset views — and turn that into an allocation recommendation. Covers growth,
  inflation, policy and labor per region, comparative developed-versus-emerging analysis,
  regional equity valuations, and fixed income and currency views for each. Triggers:
  "compare US vs Europe vs Asia", "which regions look attractive", "regional allocation",
  "developed vs emerging markets", "Europe vs US equities", "global allocation view".
---

# Bigdata Regional Comparison

Cross-region economic and market comparison with an allocation call. Use Bigdata.com plugin tools for every fact.

**Use this skill when** two or more regions or blocs are being weighed. Not this skill when:

| Request | Use instead |
|---------|-------------|
| One country in depth | Country analysis |
| The G7 specifically | G7 comparison |
| Sectors rather than regions | Cross-sector comparison |
| A sector inside one region | Country-sector analysis |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_country_tearsheet` | Economic data and comparisons where available | None |
| `bigdata_search` | Regional indicators, comparative analysis, cross-asset views | None |

**Required on every call:** pass `plugin_slug: "bigdata-regional-comparison"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-regional-comparison`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If `bigdata_country_tearsheet` is unavailable or fails, complete the analysis with `bigdata_search` alone.

## Workflow

### Step 1 — Economic data for each region

Search each region separately, indicator by indicator.

**US:** "United States GDP growth economic outlook 2026" · "US inflation Federal Reserve interest rates" · "US unemployment labor market"

**Europe:** "Eurozone GDP growth economic outlook 2026" · "ECB interest rates inflation monetary policy" · "Europe unemployment economic data"

**Asia:** "Japan GDP growth BOJ monetary policy" · "China economic outlook GDP growth" · "India economic growth outlook"

Extend or substitute regions to match what the user asked for.

### Step 2 — Comparative analysis

- "G7 economic comparison GDP growth rates"
- "US Europe Asia economic outlook comparison"
- "developed vs emerging markets allocation"
- "global economic outlook regional comparison"

### Step 3 — Regional market implications

- "regional equity valuations US Europe Asia"
- "currency outlook major currencies USD EUR JPY"
- "global fixed income yields comparison"

### Step 4 — Cross-asset views

Build the fixed income and currency view for **each** region in scope, not just for equities. Regional allocation decisions are usually made across assets.

### Step 5 — Allocation call

Rank the regions and state the allocation explicitly, with the reason per region and the key risk that would break the call.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables:

- Every region covered on the **same** indicators, so the comparison is like-for-like
- Policy divergence addressed explicitly — it usually drives currency and relative returns
- Cross-asset (equity, rates, FX) view per region, not equity-only
- An allocation call actually made, with the risk that would break it
- Every claim from a source carries an inline citation and appears in the Sources table
