---
name: bigdata-earnings-quality-screen
description: >
  Screen a public company's reported earnings for quality and accounting red flags using
  Bigdata.com data and filings. Covers cash conversion (OCF/NI, FCF/NI across periods), accruals
  and the balance-sheet accrual ratio, working-capital signals (DSO, DIO, DPO versus revenue
  growth), revenue-recognition and capitalization flags, the GAAP versus non-GAAP gap and the
  nature of the add-backs, and an optional Beneish M-Score with inputs shown — closing with a
  verdict on how far the reported numbers can be trusted. Triggers: "earnings quality screen
  for X", "are X's earnings real", "accounting red flags at X", "is X manipulating earnings",
  "cash conversion at X", "check X's accruals", "quality of earnings on X".
---

# Bigdata Earnings Quality Screen

Forensic check on whether reported earnings are backed by cash. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the question is whether the numbers can be trusted. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Full breakdown of a reported quarter | Earnings digest |
| All risk categories, rated | Risk assessment |
| Valuation of the business | Valuation snapshot |
| Full thesis with recommendation | Investment memo |

A quality screen is **diagnostic, not accusatory**. Aggressive accounting is common and often legal; the deliverable is a graded read on reliability, with the evidence shown, not an allegation.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Income statement, cash flow, balance sheet across periods | `find_securities` |
| `bigdata_search` | Filings, reconciliations, restatements, auditor and short-seller commentary | None |

**Required on every call:** pass `plugin_slug: "bigdata-earnings-quality-screen"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-earnings-quality-screen`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Pull multi-period data

Call `bigdata_company_tearsheet`. **Trend is the signal** — a single period tells you almost nothing. Get at least 4–8 quarters, or 3 years, of net income, operating cash flow, free cash flow, receivables, inventory, payables, revenue, and total assets.

### Step 3 — Cash conversion

| Check | Healthy | Investigate |
|-------|---------|-------------|
| OCF / Net income | >0.8 sustained | <0.6, or a widening gap over time |
| FCF / Net income | Positive and stable | Persistently negative while NI is positive |

A company that reports profits but does not generate cash is the single most common quality problem. Chart the trend, don't just take the latest ratio.

### Step 4 — Accruals

- **Accrual ratio (balance sheet)** = (net operating assets end − net operating assets start) / average net operating assets
- **Accrual ratio (cash flow)** = (net income − OCF − investing cash flow) / average total assets

High and rising accruals mean earnings are increasingly made of estimates rather than cash. Show the inputs.

### Step 5 — Working capital signals

| Signal | Red flag |
|--------|----------|
| DSO vs revenue growth | Receivables growing faster than revenue → recognition or collection risk |
| DIO / inventory | Inventory building ahead of sales → demand weakness or write-down risk |
| DPO | Stretching payables → liquidity strain dressed as cash flow |

### Step 6 — Revenue recognition and capitalization

Search for the specifics:

- "[Company] revenue recognition policy change"
- "[Company] capitalized software development costs"
- "[Company] restatement auditor change material weakness"
- "[Company] related party transactions revenue"

Look for: recognition timing changes, capitalizing what peers expense, revenue from related parties, channel stuffing signals, and unusual "other income".

### Step 7 — GAAP versus non-GAAP

Size the gap and — more importantly — characterize the add-backs. Recurring "one-time" restructuring, perpetual stock-comp exclusion, and adjustments that only ever go one direction are the tell. Search: "[Company] non-GAAP reconciliation adjusted EBITDA add-backs".

### Step 8 — Optional Beneish M-Score

When several signals above are flashing, compute the Beneish M-Score and show the eight inputs (DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA). Flag data gaps rather than guessing inputs. Run [scripts/earnings_quality.py](./scripts/earnings_quality.py) only if the user wants scripted output; otherwise compute in the table.

Frameworks: [references/quality-of-earnings.md](./references/quality-of-earnings.md), [references/red-flags-checklist.md](./references/red-flags-checklist.md).

### Step 9 — Verdict

Grade the overall quality — **High / Adequate / Questionable / Poor** — and state the specific evidence behind the grade, plus what would confirm or clear each concern in the next print.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) version if useful.

## Quality bar

Non-negotiables:

- **Multi-period trends**, not single-period ratios
- Every flag carries the arithmetic or the source that produced it
- Data gaps stated explicitly — never fill a missing input with a guess
- Add-backs characterized, not just totalled
- A graded verdict given, with what would clear each concern
- Diagnostic language throughout — evidence and probability, not accusation
