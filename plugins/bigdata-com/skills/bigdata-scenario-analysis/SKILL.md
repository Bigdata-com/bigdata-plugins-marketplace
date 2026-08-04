---
name: bigdata-scenario-analysis
description: >
  Build bull, base, and bear cases for a public company using Bigdata.com data — with explicit
  line-item assumptions, justified probability weights summing to 100%, a value or price per
  scenario with the bridge shown, a probability-weighted expected value and expected return
  versus spot, the upside/downside skew and risk-reward ratio, and what would move probability
  between the cases. Triggers: "scenario analysis for X", "bull base bear for X", "what's the
  upside and downside on X", "expected value for X", "probability-weighted view on X",
  "risk reward on X", "model out the cases for X".
---

# Bigdata Scenario Analysis

Three cases, honest probabilities, and the arithmetic. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants outcomes weighted, not a single point estimate. Not this skill when:

| Request | Use instead |
|---------|-------------|
| A single valuation read | Valuation snapshot |
| Full thesis with recommendation | Investment memo |
| Risks rated by likelihood and impact, not valued | Risk assessment |
| Scenarios specifically around a print | Earnings preview |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Financials, consensus estimates, multiples, spot price | `find_securities` |
| `bigdata_search` | The live debate, bull and bear arguments, analyst ranges | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company and baseline

Resolve the entity and pull the tearsheet: current financials, consensus estimates, current multiples, and **spot price** — every scenario is measured against it.

### Step 2 — Find the swing variables

Scenarios are only useful if they turn on the **2–3 variables that actually decide the outcome** — not on twenty inputs nudged in the same direction. Search the live debate:

- "[Company] bull case bear case debate"
- "[Company] key drivers revenue growth margin outlook"
- "[Company] analyst price target range high low"

Pick the swing variables and hold everything else roughly constant across cases. This is what makes the scenarios interpretable.

### Step 3 — Build the three cases

For each of **bull / base / bear**, state assumptions at the line-item level:

| Assumption | Bear | Base | Bull |
|------------|------|------|------|
| Revenue growth | | | |
| Operating margin | | | |
| [Swing variable 3] | | | |
| Exit multiple or terminal assumption | | | |

The **base case should be roughly consensus** — if it isn't, say so explicitly and explain why, because that gap is itself the finding.

### Step 4 — Value each scenario

Derive a value or price per case and **show the bridge** — the multiple applied to which earnings, or the DCF assumptions changed. Methodology: [references/dcf-methodology.md](./references/dcf-methodology.md), [references/reverse-dcf.md](./references/reverse-dcf.md).

### Step 5 — Assign and justify probabilities

Weights must sum to ~100%, and each needs a **one-line justification** grounded in evidence. Guard against the usual failure: a comfortable 25/50/25 that was never really thought about. If the distribution is skewed, say so. Methodology: [references/thesis-construction.md](./references/thesis-construction.md).

### Step 6 — Expected value and skew

- **EV** = Σ (probability × value). Show the arithmetic.
- **Expected return** versus spot, in %.
- **Upside/downside ratio** = (bull − spot) / (spot − bear).
- Note whether the distribution is symmetric or skewed, and what that means for the setup.

Run [scripts/scenario_probability.py](./scripts/scenario_probability.py) or [scripts/dcf_model.py](./scripts/dcf_model.py) only when the user explicitly asks for scripted math.

### Step 7 — What moves probability

For each case, name the **specific, observable** developments that would raise or lower its weight. Scenarios without triggers are static and go stale within a quarter.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) version if useful.

## Quality bar

Non-negotiables:

- 2–3 **swing variables** identified; everything else held roughly constant
- Assumptions at line-item level per case, not narrative adjectives
- Probabilities sum to ~100% and each is **justified**, not defaulted
- Base case tied to consensus, or the divergence stated explicitly
- Value bridge shown per scenario — no unexplained price targets
- EV arithmetic written out, plus expected return versus spot and the skew
- Probability triggers named and observable
