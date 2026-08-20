---
name: bigdata-variant-perception
description: >
  State explicitly where your view on a public company differs from consensus, using Bigdata.com
  data. Establishes the consensus baseline from estimates and sell-side posture, applies the
  EPIC filter to candidate differentiators, frames the view on FaVeS (fundamentals, valuation,
  sentiment), and states the variant view as a specific, falsifiable claim with a time horizon —
  plus what the market is missing, why the mispricing persists, the evidence for the view, and
  what would disprove it. Triggers: "variant perception on X", "where do I differ from
  consensus on X", "what is the market missing on X", "non-consensus view on X",
  "what's priced in versus reality for X", "contrarian case for X".
---

# Bigdata Variant Perception

The discipline of saying exactly where you differ from consensus — and how you'd know you were wrong. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the consensus gap *is* the deliverable. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Full thesis with recommendation and conviction | Investment memo |
| Absolute valuation | Valuation snapshot |
| Outcomes weighted by probability | Scenario analysis |
| A fast view with no consensus framing | Quick take |

**A variant perception is not a bull case.** Agreeing with consensus more enthusiastically is not a variant view. If you cannot name a specific number, timing, or outcome where you differ, the honest answer is that you have no variant perception on this name — say so.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Consensus estimates, multiples, sentiment, positioning | `find_securities` |
| `bigdata_search` | Sell-side posture, the live debate, evidence for and against | None |

**Required on every call:** pass `plugin_slug: "bigdata-variant-perception"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-variant-perception`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Establish the consensus baseline

You cannot differ from a consensus you have not written down. From the tearsheet and search, capture:

- Consensus revenue, EPS, and margin estimates for the next 1–2 years
- Mean price target and the high/low range
- Rating distribution and recent revision direction
- What the current multiple implies (reverse-DCF reasoning — [references/reverse-dcf.md](./references/reverse-dcf.md))

Search: "[Company] analyst estimates consensus outlook", "[Company] price target upgrades downgrades".

### Step 2 — Apply the EPIC filter

For each candidate differentiator, run all four tests:

| Test | Question | Pass criteria |
|------|----------|---------------|
| **E**ffect | Is it material? | ~10% change moves intrinsic value meaningfully |
| **P**redictability | Can you forecast it? | You have an analytical or informational edge, not a guess |
| **I**ndependence | Does consensus get it wrong? | The market systematically misjudges this |
| **C**onsensus gap | Is there a gap? | Your forecast differs meaningfully and specifically |

Only factors passing all four qualify. Detail: [references/epic-framework.md](./references/epic-framework.md).

### Step 3 — Frame on FaVeS

- **Fundamentals** — which 2–3 KPIs drive value, and where your forecast differs from the consensus line item
- **Valuation** — what multiple the quality and growth justify, versus what is being applied
- **Sentiment** — what is priced in behaviorally: positioning, flows, short interest, sell-side posture

Detail: [references/faves-framework.md](./references/faves-framework.md).

### Step 4 — State the variant view

Write it as a **specific, falsifiable claim with a time horizon**:

> "Consensus models [X]% [metric] in [period]; we expect [Y]% because [mechanism], which would imply [$Z] of [revenue/EBIT/value] versus the [$W] embedded in the current price."

Vague directional statements ("we're more optimistic than the street") fail this deliverable.

### Step 5 — Why the mispricing persists

A gap that anyone could see would already be closed. Name the structural reason it survives: disclosure gaps, time-horizon mismatch, index or mandate constraints, coverage gaps, complexity, recency bias after a shock, or a segment that reporting obscures. Methodology: [references/thesis-construction.md](./references/thesis-construction.md).

### Step 6 — Evidence and disconfirmation

- **Evidence for:** the specific data points, each cited
- **What would disprove it:** observable, dated, and specific — if nothing could disprove the view, it is not a research claim
- **Time horizon:** when the gap should close, and what closes it

Run [scripts/reverse_dcf.py](./scripts/reverse_dcf.py) only if the user explicitly wants scripted implied-growth math.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) version if useful.

## Quality bar

Non-negotiables:

- Consensus baseline **written down** with numbers before any differing view is stated
- EPIC run on each candidate; only all-four passes qualify
- The variant view is specific, quantified, and carries a time horizon
- A structural reason the mispricing persists — otherwise the gap probably isn't real
- Disconfirming evidence named and observable
- Honesty about the null result: if nothing passes EPIC, say there is no variant perception here
