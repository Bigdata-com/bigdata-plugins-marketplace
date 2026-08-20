---
name: bigdata-investment-memo
description: >
  Write a full institutional investment memo on a public company using Bigdata.com data —
  thesis, variant perception versus consensus, valuation, risks, catalysts, and an explicit
  recommendation with conviction. Runs the complete workflow: EPIC-filtered primary drivers,
  FaVeS variant perception, earnings quality and moat assessment, valuation by the method that
  fits the business with a secondary cross-check, bull/base/bear scenarios with probabilities
  and a probability-weighted value, key risks and what would change the view. Triggers:
  "investment memo for X", "full analysis of X", "should I buy X", "build the bull case for X",
  "write up X as an investment", "deep dive on X", "thesis on X", "DCF thesis for X".
---

# Bigdata Investment Memo

The deepest company deliverable: a complete thesis with an explicit recommendation. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants the full write-up. Not this skill when:

| Request | Use instead |
|---------|-------------|
| A fast view, one page | Quick take |
| Just "what is it worth" | Valuation snapshot |
| Just the consensus gap | Variant perception |
| Just bull/base/bear with probabilities | Scenario analysis |
| Just risks, rated | Risk assessment |
| Recent developments | Company brief |

## Core philosophy

Anchor everything on three ideas:

1. **Intrinsic value** — estimate what the business is worth independent of the price
2. **Variant perception** — state clearly where your view differs from consensus
3. **Quality over quantity** — prioritize the few drivers that matter, do not weight twenty findings equally

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Financials, estimates, margins, sentiment, segments | `find_securities` |
| `bigdata_search` | News, filings, transcripts, analyst and competitive coverage | None |
| `bigdata_events_calendar` | Upcoming earnings and conferences | `find_securities` |

**Required on every call:** pass `plugin_slug: "bigdata-investment-memo"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-investment-memo`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Company and data

Resolve the entity, pull the tearsheet, and run focused searches for recent developments, competitive position, management commentary, and the current debate on the name. Establish the factual base before any analysis.

### Step 2 — What matters (EPIC)

Filter candidate drivers down to the **2–3 that pass all four tests**:

| Test | Question | Pass criteria |
|------|----------|---------------|
| **E**ffect | Is it material? | ~10% change moves intrinsic value meaningfully (e.g. >5%) |
| **P**redictability | Can you forecast it? | You have an analytical or informational edge |
| **I**ndependence | Does consensus get it wrong? | The market systematically misjudges this |
| **C**onsensus gap | Is there a gap? | Your forecast differs meaningfully |

Detail: [references/epic-framework.md](./references/epic-framework.md).

### Step 3 — Variant perception (FaVeS)

| Element | Key questions |
|---------|---------------|
| **Fundamentals** | Which 2–3 KPIs drive value? Where could estimates be wrong? |
| **Valuation** | What is intrinsic value? What multiple fits this quality and growth? |
| **Sentiment** | What is priced in (reverse DCF)? How are investors positioned? |

You **must** articulate where you differ from consensus. Detail: [references/faves-framework.md](./references/faves-framework.md), [references/reverse-dcf.md](./references/reverse-dcf.md).

### Step 4 — Quality and risk (before valuation)

- **Earnings quality:** OCF/NI (healthy typically >0.8; red flag <0.6 or diverging), accruals, DSO vs revenue trend — [references/quality-of-earnings.md](./references/quality-of-earnings.md)
- **Competitive position:** moat type and strength, ROIC vs WACC, competitive advantage period — [references/moat-taxonomy.md](./references/moat-taxonomy.md)
- **Management:** capital allocation, insider activity, guidance track record — [references/capital-allocation.md](./references/capital-allocation.md)

Valuing a business before checking whether its earnings are real is how memos go wrong. Do this step first.

### Step 5 — Value it

Pick the primary method by business type, and always run a secondary check:

| Company type | Primary | Secondary check |
|--------------|---------|-----------------|
| Stable, profitable | DCF (FCFF) | EV/EBITDA, P/E |
| High-growth, pre-profit | EV/Revenue; DCF with long CAP | Reverse DCF |
| Bank / insurer | P/TBV; dividend discount | P/E, residual income |
| REIT | NAV; P/AFFO | Implied cap rate |
| Conglomerate | Sum-of-parts | Holdco discount |
| Distressed | Liquidation / recovery | Asset coverage |

Methodology: [references/dcf-methodology.md](./references/dcf-methodology.md), [references/multiples-framework.md](./references/multiples-framework.md), [references/sum-of-parts.md](./references/sum-of-parts.md). Sector-specific lenses: [references/sector-routing.md](./references/sector-routing.md). Foundations: [references/graham-dodd-principles.md](./references/graham-dodd-principles.md).

### Step 6 — Scenarios

Build **bull / base / bear** with explicit assumptions, probability weights, and a value per scenario. Show the probability-weighted value and the arithmetic. Methodology: [references/thesis-construction.md](./references/thesis-construction.md).

### Step 7 — Risks, catalysts, recommendation

State the key risks and **what would change the view** (falsifiable, not decorative). List dated catalysts. Then give the recommendation and a conviction level — a memo that hedges everything has not done its job.

## Optional scripts

**Default:** work from tearsheet, search, and reasoning — including reverse-DCF reasoning — without running Python.

Use these only when the user explicitly wants spreadsheet-style model output:

| Script | Purpose |
|--------|---------|
| [scripts/dcf_model.py](./scripts/dcf_model.py) | DCF with scenarios |
| [scripts/reverse_dcf.py](./scripts/reverse_dcf.py) | Implied growth extraction |
| [scripts/earnings_quality.py](./scripts/earnings_quality.py) | Beneish M-Score, accruals |
| [scripts/peer_comparables.py](./scripts/peer_comparables.py) | Comp table |
| [scripts/scenario_probability.py](./scripts/scenario_probability.py) | Expected value across scenarios |

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer Word (.docx) for formal memos or a deck-ready structure.

## Quality bar

A memo must clear a concise institutional review. Non-negotiables:

1. Clear **recommendation** and **conviction** (e.g. 1–5)
2. **Explicit variant perception** versus consensus — stated, not implied
3. **Scenarios** with probabilities and price targets or ranges, math shown
4. **Key risks** and what would change the view
5. **Catalysts** with timing
6. Earnings quality and moat assessed **before** the valuation section
7. Facts separated from analysis and implications
