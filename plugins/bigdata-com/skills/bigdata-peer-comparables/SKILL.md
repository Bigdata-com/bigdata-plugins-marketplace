---
name: bigdata-peer-comparables
description: >
  Compare a public company against its peer set using Bigdata.com data — valuation multiples,
  growth, profitability, returns, leverage, and sentiment — to judge relative attractiveness.
  Builds the peer set with an explicit rationale for inclusion and exclusion, tabulates
  like-for-like metrics with peer median and quartile positioning, decomposes any premium or
  discount into what fundamentals justify versus what they do not, and closes with a relative
  verdict. Triggers: "compare X to its peers", "peer comparables for X", "how does X screen vs
  competitors", "is X cheap relative to peers", "comps table for X", "relative valuation of X",
  "who are X's peers".
---

# Bigdata Peer Comparables

Relative screen against a defensible peer set. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the question is relative. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Absolute value — what is it worth | Valuation snapshot |
| Sector-level performance and themes | Sector analysis |
| Sectors ranked against each other | Cross-sector comparison |
| Full thesis with recommendation | Investment memo |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve the subject and every peer → `entity_id` | None |
| `bigdata_company_tearsheet` | Multiples, growth, margins, returns, leverage, sentiment per company | `find_securities` |
| `bigdata_search` | Peer-set validation, competitive positioning, valuation debate | None |

**Required on every call:** pass `plugin_slug: "bigdata-peer-comparables"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-peer-comparables`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the subject company

Call `find_securities`, then `bigdata_company_tearsheet` to establish the business model, segment mix, and size.

### Step 2 — Construct the peer set (state the rationale)

Pick **5–8 peers** on business model and economics, not just sector label. Screen on: revenue model, end markets, size within an order of magnitude, growth profile, geographic mix, and capital intensity.

Search to validate: "[Company] competitors peer group comparison", "[Company] closest comparable companies".

**Write down why each peer is in — and name the obvious candidates you excluded, with the reason.** A comps table is only as good as its peer set, and an unstated peer set is unfalsifiable.

### Step 3 — Pull peer data

Run `find_securities` then `bigdata_company_tearsheet` for each peer. Pull the **same** metrics for everyone, from the same period, so the table is like-for-like. Note any fiscal-year misalignment.

### Step 4 — Build the comparables table

| Category | Metrics |
|----------|---------|
| Valuation | EV/Sales, EV/EBITDA, P/E (NTM and TTM), FCF yield, plus the sector-standard multiple |
| Growth | Revenue growth (TTM, NTM consensus), EPS growth |
| Profitability | Gross margin, EBITDA margin, operating margin, FCF margin |
| Returns | ROIC, ROE |
| Leverage | Net debt/EBITDA, interest coverage |
| Sentiment | Mean price target vs spot, rating distribution, quantified sentiment where available |

Use the multiples that fit the business — P/TBV for banks, P/AFFO for REITs, EV/Sales for pre-profit growth. Framework: [references/multiples-framework.md](./references/multiples-framework.md). Sector-specific KPIs: [references/sector-routing.md](./references/sector-routing.md).

### Step 5 — Position against the set

For each metric: the subject's value, the **peer median**, and its **quartile**. Percentile positioning shows what a raw table hides.

### Step 6 — Decompose the premium or discount

The core analytical step. If the company trades at a premium or discount, ask **what fundamentals justify it** — faster growth, higher margins, better returns, lower leverage, cleaner accounting — and how much of the gap remains **unexplained**. An unexplained gap is where the opportunity or the warning sits.

### Step 7 — Verdict

State relative attractiveness with the specific drivers, plus what would close or widen the gap.

Run [scripts/peer_comparables.py](./scripts/peer_comparables.py) only when the user explicitly wants a scripted comp table.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or spreadsheet-style version if useful.

## Quality bar

Non-negotiables:

- Peer set **justified**, with exclusions named — this is the credibility of the whole deliverable
- Same metrics, same period, for every company; fiscal misalignment flagged
- Multiples chosen for the business type, not generic P/E across a mixed set
- Peer median **and** quartile positioning given, not just raw values
- Premium/discount **decomposed** into justified and unexplained
- A relative verdict stated, with what would close the gap
