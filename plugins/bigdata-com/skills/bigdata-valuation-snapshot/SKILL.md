---
name: bigdata-valuation-snapshot
description: >
  Answer what a public company is worth and whether it is cheap or expensive, using Bigdata.com
  data (tearsheet multiples, estimates, margins, peer context). Produces a multiples cross-check
  against the company's own history and peer median, an implied-expectations read on what the
  current price already embeds (reverse-DCF reasoning, no model build required), the 2-3 value
  drivers that dominate, and a cheap / fair / rich verdict. Triggers: "what is X worth", "is X
  expensive", "valuation snapshot for X", "what's priced in for X", "is X cheap vs peers",
  "how is X valued", "fair value for X".
---

# Bigdata Valuation Snapshot

The lightweight answer path for "what is it worth" — no full memo, no standalone model build. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants a valuation read without a full thesis. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Full thesis with recommendation and conviction | Investment memo |
| Explicit bull/base/bear with probabilities and EV | Scenario analysis |
| Detailed peer table across many metrics | Peer comparables |
| Valuation in the context of an upcoming print | Earnings preview |
| Built DCF or sum-of-parts model output | Investment memo (with scripts) |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Current and historical multiples, estimates, margins, FCF, segments | `find_securities` |
| `bigdata_search` | Peer valuation context, analyst views, valuation debates | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Pull valuation inputs

Call `bigdata_company_tearsheet` for current and historical multiples, consensus estimates, margins, FCF where shown, and segment context.

### Step 3 — Peer and history context

- Use the tearsheet peer set, or search: "[Company] valuation vs peers EV EBITDA PE comparison"
- Note **current** vs **~5-year range** or trailing average where the data allows. If only spot data exists, say so and approximate rather than inventing a range.
- Pick the multiples that fit the business — a bank on P/TBV, a REIT on P/AFFO, a pre-profit grower on EV/Revenue. Framework: [references/multiples-framework.md](./references/multiples-framework.md).

### Step 4 — Implied expectations (reverse-DCF mindset)

Without building a model, articulate **what has to go right** at the current price:

- Revenue growth the multiple embeds vs consensus
- Margin level or trajectory embedded vs recent trend
- Reinvestment needs and the risk premium implied
- Whether the market is pricing a re-rating or a de-rating vs fundamentals

Methodology: [references/reverse-dcf.md](./references/reverse-dcf.md). Full DCF mechanics if the user wants depth: [references/dcf-methodology.md](./references/dcf-methodology.md). Run [scripts/reverse_dcf.py](./scripts/reverse_dcf.py) or [scripts/dcf_model.py](./scripts/dcf_model.py) only when the user explicitly asks for scripted or spreadsheet-style output.

### Step 5 — Synthesize

Combine the **multiples cross-check**, the **implied expectations**, and the **2–3 value drivers** that actually move fair value. State plainly whether the stock screens **cheap, fair, or rich** relative to embedded expectations — and name what would change that.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations as superscript-style numbers `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version at the end if useful.

## Quality bar

Pass the PM test before delivering: **What's different?** **What matters (2–3 drivers)?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing).

Non-negotiables in every snapshot:

- Multiples chosen for the **business type**, not generic P/E on everything
- Current level always framed against **history and peers**, or the gap stated explicitly
- A plain-English statement of what the price embeds — this is the point of the deliverable
- Cheap / fair / rich verdict given, not hedged into nothing
- Tearsheet and search preferred over model builds; scripts only on request
- Facts separated from analysis and implications
