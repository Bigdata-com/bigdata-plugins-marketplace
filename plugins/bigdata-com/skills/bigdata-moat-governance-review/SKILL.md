---
name: bigdata-moat-governance-review
description: >
  Assess how durable a public company's competitive advantage is and whether management can be
  trusted with the capital, using Bigdata.com data. Covers moat identification by type with
  evidence, moat strength via ROIC versus WACC, pricing power and share trend, a competitive
  advantage period estimate with erosion signals, industry structure via five forces, the
  capital allocation track record across M&A, buybacks, dividends and reinvestment, and
  governance — board independence, dual roles, compensation design, related-party exposure,
  insider activity. Triggers: "does X have a moat", "moat review for X", "how durable is X's
  advantage", "is X's management any good", "capital allocation at X", "governance review of X",
  "competitive advantage of X".
---

# Bigdata Moat & Governance Review

Two questions that decide long-run returns: is the advantage durable, and are the stewards any good? Use Bigdata.com plugin tools for every fact.

**Use this skill when** durability and stewardship are the question. Not this skill when:

| Request | Use instead |
|---------|-------------|
| All risk categories rated | Risk assessment |
| Accounting reliability | Earnings quality screen |
| What the business is worth | Valuation snapshot |
| Full thesis with recommendation | Investment memo |
| Sector-wide structure | Sector analysis / playbook |

These two topics belong together: a wide moat run by poor capital allocators leaks value, and excellent management cannot rescue a business with no structural advantage.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Returns, margins, reinvestment, buybacks, dividends, insider summary | `find_securities` |
| `bigdata_search` | Competitive position, share, pricing, governance, capital allocation history | None |

**Required on every call:** pass `plugin_slug: "bigdata-moat-governance-review"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-moat-governance-review`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company and its industry

Call `find_securities`, then `bigdata_company_tearsheet` for the returns and margin history that the moat assessment rests on.

### Step 2 — Identify the moat by type

Name the moat type — network effects, switching costs, cost advantage, intangibles (brand, patents, licenses), or efficient scale — and give the **evidence** for each claimed source. "Strong brand" without pricing evidence is not a moat finding. Taxonomy: [references/moat-taxonomy.md](./references/moat-taxonomy.md).

Search: "[Company] competitive advantage market share pricing power", "[Company] switching costs customer retention".

### Step 3 — Test moat strength with numbers

| Test | What it shows |
|------|---------------|
| ROIC vs WACC, sustained | Whether the advantage converts to economic profit |
| ROIC trend over 5–10 years | Whether it is widening or eroding |
| Gross and operating margin vs peers | Pricing power in practice |
| Market share trend | Whether the position is being defended |
| Reinvestment rate at high ROIC | Whether the moat has runway |

A moat that does not show up as durable excess returns is a story, not a moat.

### Step 4 — Competitive advantage period and erosion

Estimate how long the advantage plausibly persists, and name the **erosion signals** to monitor: pricing pressure (usually the first sign), share loss to entrants or substitutes, ROIC compression toward WACC, rising customer churn, technology shifts. Industry structure context: [references/porter-five-forces.md](./references/porter-five-forces.md).

### Step 5 — Capital allocation track record

Assess where the cash has gone and what it earned:

- **M&A** — deals done, prices paid, returns achieved, write-downs taken
- **Buybacks** — bought at what valuations; repurchasing above intrinsic value destroys value
- **Dividends** — sustainability against FCF, and consistency
- **Reinvestment** — incremental ROIC on organic capex and R&D
- **Balance sheet** — leverage choices through the cycle

Framework: [references/capital-allocation.md](./references/capital-allocation.md). Search: "[Company] acquisitions track record write-down", "[Company] buyback history capital returns".

### Step 6 — Governance

- Board independence, size, refreshment, and relevant expertise
- Combined CEO/chair role, classified board, dual-class shares and voting concentration
- Compensation design: what metrics vest, over what horizon, and whether they align with per-share value
- Related-party transactions
- Insider buying and selling patterns, read in context rather than mechanically
- Guidance track record — a proxy for candor

Search: "[Company] CEO chairman combined role board independence", "[Company] executive compensation say on pay", "[Company] insider selling Form 4", "[Company] related party transactions".

### Step 7 — Combined verdict

Grade the **moat** (None / Narrow / Wide) and its **trend** (widening / stable / eroding), and grade **management quality** (Strong / Adequate / Weak) on capital allocation and governance separately. Then state what the combination means for the durability of returns, and what would change each grade.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) version if useful.

## Quality bar

Non-negotiables:

- Every claimed moat source backed by **evidence**, not adjectives
- ROIC versus WACC shown over time — the numerical test is mandatory
- Erosion signals named specifically, with what to watch
- Capital allocation judged on **returns achieved**, not on stated intentions
- Governance graded separately from capital allocation — they diverge often
- Both grades come with what would change them
