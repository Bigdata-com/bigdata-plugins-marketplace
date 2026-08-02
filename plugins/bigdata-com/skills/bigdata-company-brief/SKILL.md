---
name: bigdata-company-brief
description: >
  Generate a company brief — a cited 30-day summary of what happened at a public company and
  why it matters — using Bigdata.com data (news, filings, transcripts, tearsheet financials).
  Findings are categorized into financial results, product and tech launches, M&A and
  partnerships, regulatory and legal, management changes, and other material events, each with
  date, facts, and a bullish/bearish/neutral investment implication tied to a value driver, plus
  competitive context and a ranked top 2-3. Triggers: "company brief for X", "what's happening
  with X", "catch me up on X", "recent developments at X", "what's the news on X",
  "summary of the last month for X", "any updates on X".
---

# Bigdata Company Brief

Retrospective 30-day summary of material developments at a public company, with a "so what" on each. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants to catch up on what has already happened. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Analysis ahead of an upcoming earnings call | Earnings preview |
| Breakdown of results just reported | Earnings digest / earnings reaction |
| "What is it worth" | Valuation snapshot |
| Structured risk mapping with likelihood/impact | Risk assessment |
| Full thesis, DCF, or variant perception | Investment memo |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Profile, sector/industry, financial position, recent performance | `find_securities` |
| `bigdata_search` | News, filings, transcripts, legal and regulatory coverage | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Business context

Call `bigdata_company_tearsheet` with the `entity_id` for the company profile (sector, industry, description), financial position, and recent performance metrics. This context is what lets you judge whether a news item is material — read it before searching.

### Step 3 — Competitive context (one pass)

Run `bigdata_search` at least once on industry structure and positioning:

- "[Company] competitive landscape market share"
- "[Company] vs competitors [Industry]"

A full five-forces write-up is not needed. **2–4 sentences** on concentration, pricing power, and disruption risk materially lift the brief. Mental model: [references/porter-five-forces.md](./references/porter-five-forces.md).

### Step 4 — Search recent news (last 30 days)

Use `bigdata_search` with natural-language queries that include the company name and a temporal reference. Run **5–10 searches** for coverage, then compress.

- "[Company] news last 30 days"
- "[Company] recent developments"
- "[Company] earnings announcement"
- "[Company] product launches partnerships"
- "[Company] regulatory legal updates"
- "[Company] lawsuit litigation court ruling investigation settlement last 30 days"

Cover all of: financial developments, product/technology announcements, partnerships and M&A, regulatory and legal matters, management changes. The explicit legal/litigation query is there so material non-operational items don't get buried under earnings headlines.

If the month was quiet, ask:

> "I haven't found any significant developments for [Company] in the last 30 days. Would you like me to extend the search period or focus on specific topics?"

### Step 5 — Categorize, and mark what is primary

Sort every finding into the six output categories: **Financial Results**, **Product/Tech Launches**, **M&A and Partnerships**, **Regulatory/Legal Updates**, **Management Changes**, **Other Material Events**.

While sorting, tag each item **primary** (material to value or the narrative) or **secondary**. Do not equal-weight the categories in the prose — quantity of headlines is not materiality. If a category is empty, write "No significant developments in this period" rather than padding it.

### Step 6 — Investment implication ("so what")

For each **material** event, give:

- **Date** — when it happened or was announced
- **Facts** — objective summary of what happened
- **Investment implication** — Bullish / Bearish / Neutral, tied to a value driver

Avoid generic labels. Replace "bullish for the stock" with the lever: "could support ~+$Nm revenue run-rate", "+Ybps margin", "de-risks [issue]", "lifts regulatory overhang on segment Z". If it isn't quantifiable, state the **specific mechanism** instead of a direction.

### Step 7 — Rank and synthesize

Rank the top **2–3** developments for the period and lead the executive summary with them. The overall assessment states the **net tilt and why**, not a recap of every bullet.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, sources, and footer.

- Add inline citations as superscript-style numbers `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version at the end if useful.

## Quality bar

Pass the PM test before delivering: **What's different?** **What matters (2–3 items)?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing). Would it survive a short, skeptical morning meeting without reading as a news dump?

Non-negotiables in every brief:

- Competitive context present, not skipped
- Every material event carries date, facts, and a **mechanism-level** implication
- Top 2–3 developments ranked and surfaced in the executive summary
- Legal/regulatory search actually run, with material items shown
- Empty categories marked as such rather than padded
- Facts separated from analysis and implications
