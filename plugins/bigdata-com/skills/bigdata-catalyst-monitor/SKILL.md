---
name: bigdata-catalyst-monitor
description: >
  Map the dated events that could move a public company over the next few quarters, using
  Bigdata.com data (events calendar, filings, news, tearsheet). Covers scheduled catalysts —
  earnings, investor days, index reviews, lock-up and patent expiries, regulatory decision
  dates — and foreseeable unscheduled ones — litigation milestones, product cycles, contract
  renewals, refinancings. Each catalyst carries a date or window, likely direction, magnitude,
  confidence, and what to watch, ranked by expected impact rather than by date alone.
  Triggers: "catalyst monitor for X", "what's coming up for X", "upcoming catalysts for X",
  "what could move X", "key dates for X", "event calendar for X", "what should I watch on X".
---

# Bigdata Catalyst Monitor

Forward calendar of what could move the name, ranked by impact. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the question is "what's coming". Not this skill when:

| Request | Use instead |
|---------|-------------|
| What already happened over the past month | Company brief |
| Deep analysis of the next earnings print | Earnings preview |
| Probability-weighted outcomes and values | Scenario analysis |
| Risks rated by likelihood and impact | Risk assessment |

**Catalyst vs risk:** a catalyst is a **dated or datable event** that resolves something. A standing risk with no resolution date belongs in a risk assessment.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_events_calendar` | Scheduled earnings and conferences | `find_securities` |
| `bigdata_company_tearsheet` | Baseline financials, estimates, what the price embeds | `find_securities` |
| `bigdata_search` | Regulatory dates, litigation milestones, product cycles, filings | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Scheduled events

Call `bigdata_events_calendar` for earnings dates and conferences over the next 2–4 quarters. Note the fiscal calendar so quarter-ends and guidance updates land correctly.

### Step 3 — Baseline: what is already priced

Call `bigdata_company_tearsheet`. A catalyst only matters relative to expectations — capture consensus estimates, current multiples, and sentiment so each catalyst can be framed against what the market already assumes.

### Step 4 — Search for datable events

Run **6–8 targeted searches**:

- "[Company] upcoming product launch roadmap timeline"
- "[Company] regulatory decision approval date FDA / FTC / EU"
- "[Company] lawsuit trial date court ruling expected"
- "[Company] investor day capital markets day guidance update"
- "[Company] contract renewal expiry major customer"
- "[Company] debt maturity refinancing schedule"
- "[Company] patent expiry exclusivity loss"
- "[Company] index inclusion review lock-up expiry"

Include the industry-specific ones that apply — clinical readouts, license renewals, rate cases, spectrum auctions, model launches.

### Step 5 — Rate each catalyst

For every catalyst record:

- **Date or window** — exact where known, quarter where not; mark undated but expected items as such
- **Type** — scheduled or foreseeable
- **Likely direction** — positive / negative / two-sided
- **Magnitude** — high / medium / low, tied to a value driver where possible ("~$Nm revenue", "~Xbps margin", "removes overhang on segment Y")
- **Confidence** — how sure the date and the outcome are; these are different, and both matter
- **What to watch** — the specific signal that tells you which way it resolved

### Step 6 — Rank and sequence

Rank by **expected impact**, not chronology — a large two-sided event in nine months usually matters more than a routine print next week. Then give the chronological calendar separately, so the reader gets both views.

Close with the **2–3 catalysts that dominate** the next few quarters and what each would change.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version if useful.

## Quality bar

Non-negotiables:

- Every catalyst carries a **date or window** — undated speculation is not a catalyst
- Direction, magnitude, and confidence given separately; date confidence distinguished from outcome confidence
- Magnitude tied to a value driver, not just labelled "high"
- Ranked by impact **and** listed chronologically
- Standing risks with no resolution date excluded — they belong in a risk assessment
- Facts separated from analysis and implications
