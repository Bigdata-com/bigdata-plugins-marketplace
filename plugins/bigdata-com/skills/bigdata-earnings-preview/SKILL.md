---
name: bigdata-earnings-preview
description: >
  Create a forward-looking earnings preview for a public company ahead of its next earnings
  call, using Bigdata.com data (estimates, tearsheet financials, news, filings, transcripts,
  events calendar). Produces an EPIC driver table, earnings quality screen with forward
  watch-fors, structured sentiment and positioning data, what's priced in plus valuation
  cross-check, FaVeS variant perception, bull and bear cases, bull/base/bear scenarios with
  probability-weighted expected value, and key metrics to watch — fully cited. Triggers:
  "earnings preview for X", "preview X earnings", "pre-earnings analysis", "Q3 preview",
  "what to expect before X reports", "what should I watch when X reports", "set up for X
  earnings", "bull and bear case into the print".
---

# Bigdata Earnings Preview

Forward-looking, pre-earnings research note on a public company. Use Bigdata.com plugin tools for every fact; apply the pre-synthesis filter below before writing.

**Use this skill when** the user wants analysis *before* a company reports. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Analysis of results already reported | Earnings digest / earnings reaction |
| Retrospective summary of recent news | Company brief |
| "What is it worth" with no earnings event | Valuation snapshot |
| Comprehensive risk mapping | Risk assessment |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Financials, estimates, margins, sentiment/positioning fields | `find_securities` |
| `bigdata_events_calendar` | Next earnings call date | `find_securities` |
| `bigdata_search` | News, filings, transcripts, analyst and regulatory coverage | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Before you synthesize — quality over quantity

Do this **after** gathering data and **before** writing the draft:

1. List candidate drivers from tearsheet + search.
2. Rank them and keep the top **2–3** as primary drivers. Do not give 20 findings equal weight.
3. Run the full **EPIC** filter on each primary driver:

| Test | Question |
|------|----------|
| **E**ffect (material) | Would getting this wrong move value or the debate on the name meaningfully? |
| **P**redictability | Can *you* form a view with evidence, not speculation? |
| **I**ndependence | Does consensus or price **systematically** under- or over-weight this factor? |
| **C**onsensus gap | Does **your** view differ from consensus in a specific, falsifiable way? |

4. Map each primary driver to an implication (bullish / bearish / neutral) with specific metrics.
5. Deprioritize template sections that are immaterial this period — say so in one line rather than padding.

Depth: [references/epic-framework.md](./references/epic-framework.md).

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Financial baseline

Call `bigdata_company_tearsheet` with the `entity_id` for:

- Recent quarterly performance trends and YoY comparisons
- Historical earnings surprises
- Analyst estimates for the upcoming quarter
- Key financial metrics and margins
- **Positioning / sentiment fields when exposed** — sentiment scores, news/social metrics, ownership concentration, insider summary, options or short interest. Capture whatever the tool returns; never substitute analyst headlines for systematic data when numbers exist.

### Step 3 — Earnings quality quick screen

Before building narratives, record a credibility table with a forward-looking **watch for** column (approximate if necessary; flag data gaps):

| Check | This period / trend | Red-flag threshold | **Watch for (next print)** |
|-------|---------------------|--------------------|----------------------------|
| OCF / Net income | | Healthy often >0.8 sustained; <0.6 or widening gap → dig | further OCF/NI divergence; one-time boosts rolling off |
| DSO vs revenue growth | | DSO rising faster than revenue → recognition risk | DSO days vs rev growth; channel inventory mentions |
| GAAP vs non-GAAP EPS gap | | Large or widening gap → quality question | stock comp, restructuring, "adjusted" add-backs |

If the tearsheet lacks a line, search: "[Company] operating cash flow vs net income non-GAAP reconciliation".

Depth: [references/quality-of-earnings.md](./references/quality-of-earnings.md).

### Step 4 — Earnings date

Call `bigdata_events_calendar` with the `entity_id` to find the next earnings call. If unknown, ask:

> "I don't have the exact earnings date yet. Shall I proceed with the preview based on recent developments and expectations?"

### Step 5 — Search: developments, legal/regulatory, positioning

Cast a **wide net** so material non-operational risks (court rulings, probes, tax disputes) are not missed. Use `bigdata_search` over the last **60–90 days** (extend if coverage is thin). Run **at least 8–10 targeted queries** across all three buckets, then merge redundant results.

**Core company & industry**
- "[Company] recent developments last 90 days"
- "[Company] product launches initiatives"
- "[Company] guidance commentary management"
- "[Company] analyst expectations earnings preview"
- "[Industry] trends headwinds tailwinds"

**Regulatory, legal, policy (mandatory)**
- "[Company] lawsuit litigation court ruling settlement regulatory investigation last 90 days"
- "[Company] SEC investigation DOJ antitrust fine penalty Europe"
- "[Company] tax dispute regulatory approval compliance"

**Market positioning & flows (mandatory — fills the structured table in the output)**
- "[Company] insider buying selling Form 4 transactions last 90 days"
- "[Company] institutional ownership 13F changes fund flows"
- "[Company] short interest options put call ratio open interest"
- "[Company] news sentiment score" (or closest available)

If news is sparse, ask:

> "There's been limited news recently. Would you like me to expand the search period or focus on industry trends?"

### Step 6 — Sentiment & positioning (structured, not anecdotes)

Build the output table from data, not from a single analyst note:

1. Pull every **numeric** sentiment / flow / positioning field from the tearsheet.
2. Use Step 5 results to fill gaps (insider trades, large holder moves, options/skew, quantified sentiment).
3. If a cell is unavailable, write **"Not available in data"** — the section still appears.

### Step 7 — What's priced in + valuation cross-check

**Before** writing bull/bear narratives, establish what the current price embeds for this quarter and the near-term trajectory. Use tearsheet multiples, consensus, and reverse-DCF-style reasoning (conceptual is fine — [references/reverse-dcf.md](./references/reverse-dcf.md)).

| Lens | Implied by market | Consensus | Your assessment |
|------|-------------------|-----------|-----------------|
| Growth (revenue / key volume) | | | |
| Margin level or expansion | | | |
| Beat magnitude / "whisper" vs published consensus | | | |

**Multiples sanity check:** current EV/EBITDA, P/E, FCF yield (or sector-standard multiples) vs ~5-year range or peer median where data allows. State whether valuation implies **optimism**, **consensus**, or **pessimism** relative to the setup.

### Step 8 — Variant perception (FaVeS) + scenarios

**FaVeS — mandatory structure in the output:**
- **Fundamentals** — the 2–3 KPIs that drive the quarter; where consensus could be wrong (link to bull/bear).
- **Valuation** — tie to the *What's priced in* table and valuation cross-check; cross-reference rather than repeat prose.
- **Sentiment** — tie to the *Sentiment & positioning* table; separate what is priced in **behaviorally** from **fundamentally**.

Depth: [references/faves-framework.md](./references/faves-framework.md).

**Scenario analysis — mandatory:** build Bull / Base / Bear with

- **Probability weights** summing to ~100% (e.g. 30/50/20), briefly justified
- **Key assumptions** per scenario (growth, margin, one-timers, legal outcomes)
- **Price level or range** per scenario (spot, consensus PT band, or a rough DCF/multiple bridge — show the assumptions)
- **Probability-weighted expected value** with the arithmetic shown (EV = Σ p×P; state expected upside/downside % vs spot)

Methodology: [references/thesis-construction.md](./references/thesis-construction.md). Compute in prose/table by default; run [scripts/scenario_probability.py](./scripts/scenario_probability.py) only if the user explicitly asks for scripted math.

### Step 9 — Synthesize

Lead with the 2–3 primary drivers and their EPIC documentation. Cover, in order of materiality only:

- **Recent developments** — launches, partnerships or M&A, operational shifts, geographic/share changes, plus material legal and regulatory items
- **Industry trends** — macro drivers, competitive landscape, supply chain and cost pressure, policy
- **Bull case** — each point specific, measurable, evidence-backed and resolvable over a sensible horizon; tie to consensus line items where possible ("consensus models X% growth in segment Y; channel evidence suggests Z%, ~$Nm revenue upside"); cite a source per claim
- **Bear case** — same discipline; quantify downside (margin bps, revenue %, one-time vs recurring)
- **Key metrics to watch** — the KPIs that matter *this* quarter, those that move the stock given what's priced in, and where surprise volatility is highest vs whisper/consensus

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, mandatory tables, sources, and footer.

- Add inline citations as superscript-style numbers `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version at the end if useful.

## Quality bar

Pass the PM test before delivering: **What's different?** **What matters (2–3 drivers)?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing). Would it survive a short, skeptical morning meeting without reading as a data dump?

Non-negotiables in every preview:

- EPIC table for each elevated driver — filled, not placeholder
- Scenario table with probabilities, prices, and **EV math shown**
- Sentiment & positioning as structured data — tearsheet first, then search
- Regulatory/legal queries run, and material items surfaced in developments and the bear case
- **Watch for** column on the quality screen — forward monitoring, not only backward checks
- *What's priced in* built before bull/bear, so both cases are relative to embedded expectations
- Facts separated from analysis and implications
