---
name: bigdata-risk-assessment
description: >
  Produce a comprehensive risk assessment for a public company using Bigdata.com data (10-K risk
  factors, 8-K material events, news, tearsheet financials). Covers six categories — regulatory
  and legal, competitive and moat erosion, operational, financial and balance sheet, macro, and
  management and governance — each rated by likelihood and impact, with a distress screen when
  leverage is stretched, mitigation status, a priority matrix, and a scenario bridge to value
  drivers. Triggers: "risk assessment for X", "assess risks for X", "what are the risks with X",
  "what could go wrong at X", "risk factors for X", "how risky is X", "downside risks for X".
---

# Bigdata Risk Assessment

Comprehensive, evidence-rated risk profile of a public company. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants risks identified, rated, and prioritized. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Recent developments over the past month | Company brief |
| Near-term drivers around a specific print | Earnings preview / digest |
| Accounting and manipulation red flags specifically | Earnings quality screen |
| Moat durability and management quality specifically | Moat & governance review |
| Full thesis with a recommendation | Investment memo |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Leverage, liquidity, cash flow, coverage, debt maturity | `find_securities` |
| `bigdata_search` | 10-K risk factors, 8-K events, news, governance signals | None |

**Required on every call:** pass `plugin_slug: "bigdata-risk-assessment"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-risk-assessment`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Before you synthesize — prioritize

Rate everything, but **lead with what moves the name**. A long list of low-likelihood, low-impact risks is a data dump. Identify the 2–3 risks that dominate the debate and put them first in the executive summary and the priority matrix.

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Financial health baseline

Call `bigdata_company_tearsheet` with the `entity_id` and analyze:

- **Leverage** — debt/equity, debt/assets, debt/EBITDA
- **Liquidity** — current ratio, quick ratio, cash position
- **Cash flow** — operating cash flow and free cash flow trends
- **Debt maturity** — short-term vs long-term
- **Interest coverage** — ability to service debt

### Step 3 — Distress quick screen (conditional)

When leverage is elevated, coverage is thin, FCF is weak against debt service, or liquidity is tight, add a quantitative flag:

- **Altman Z-Score (simplified)** — compute from tearsheet or filing inputs (working capital, retained earnings, EBIT, equity, total liabilities, sales, total assets). If inputs are incomplete, state the **data gaps** and give a qualitative distress read instead.
- **Manipulation context** — if accruals or earnings quality look aggressive, work through [references/red-flags-checklist.md](./references/red-flags-checklist.md). Run [scripts/earnings_quality.py](./scripts/earnings_quality.py) only if the user explicitly wants scripted metrics.

### Step 4 — Moat and competitive durability

Identify the **moat type** (if any) and how it could erode, using [references/moat-taxonomy.md](./references/moat-taxonomy.md):

- Pricing power trend vs peers
- Share shifts to entrants or substitutes
- ROIC compression vs history and vs cost of capital

Search if needed: "[Company] pricing power market share competition ROIC".

### Step 5 — Official risk disclosures

Use `bigdata_search` for the company's own disclosures — the authoritative baseline:

- "risk factors material risks regulatory competitive in the last 10-K SEC filing of [Company]"

If the 10-K can't be found:

> "I couldn't locate the most recent 10-K filing. Should I proceed with 8-K filings and news-based risk analysis?"

### Step 6 — Material events (8-K)

- "material events changes risks in 8-K SEC filing of [Company] in the last 90 days"

8-Ks catch emerging risks that post-date the annual report.

### Step 7 — Emerging risks in the news

Run **4–6 targeted searches** across risk categories:

- "[Company] regulatory investigation lawsuit controversy in the last 30 days"
- "[Company] competitive pressure market share losses"
- "[Company] supply chain disruption operational challenges"
- "[Company] executive departure management changes"
- "[Company] cybersecurity breach data incident"

### Step 8 — Management and governance signals

Especially for founder-led or concentrated-ownership names:

- "[Company] CEO chairman combined role board independence"
- "[Company] insider selling stock compensation"
- "[Company] activist shareholder governance"
- "[Company] related party transactions"

Cross-check patterns against [references/capital-allocation.md](./references/capital-allocation.md).

### Step 9 — Categorize and rate

Sort every risk into the six categories and rate each on **likelihood** and **impact**:

**Likelihood** — High: >50% within 12 months or already materializing · Medium: 20–50% within 12–24 months · Low: <20% or >24 months out

**Impact** — High: >10% of revenue/earnings or existential · Medium: 3–10% or significant operational impairment · Low: <3% or manageable

**Combined priority** — High×High = Critical · High×Medium or Medium×High = High · Medium×Medium = Medium · otherwise Lower

The six categories:

1. **Regulatory/legal** — litigation, investigations, antitrust, framework changes, product liability
2. **Competitive** — moat erosion first: which moat, how it breaks; then share loss, entrants, pricing pressure (often the first signal of moat damage), customer concentration, ROIC vs WACC compression
3. **Operational** — supply chain, key personnel, technology and cyber, production constraints, execution
4. **Financial/balance sheet** — refinancing and covenants, liquidity, FX and rates, pensions, off-balance-sheet, plus the Step 3 distress read
5. **Macro/market** — cycle sensitivity, geopolitics, secular decline, commodities, policy
6. **Management & governance** — board independence, dual CEO/chair, related-party exposure, compensation design, insider patterns, capital allocation credibility, succession

Be **objective and evidence-based** in the ratings, note **mitigation status** for each material risk, and distinguish materiality — not every disclosed risk factor deserves equal weight.

### Step 10 — Scenario bridge

Connect the likelihood × impact view to a brief **bull / base / bear narrative** for the value drivers. Narrative, not a full DCF — this is what makes the assessment actionable rather than descriptive.

If the profile comes out thin:

> "Risk profile appears relatively low based on available information. Would you like me to expand the search parameters or focus on industry-specific risks?"

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, rating tables, sources, and footer.

- Add inline citations as superscript-style numbers `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version at the end if useful.

## Quality bar

Pass the PM test before delivering: **What's different?** **What matters (2–3 risks)?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing).

Non-negotiables in every assessment:

- Official 10-K disclosures used as the baseline, then validated against 8-Ks and news
- Every material risk carries **likelihood, impact, evidence, and mitigation status**
- Moat erosion treated as a first-order competitive risk, not a footnote
- Distress screen run whenever leverage or coverage is weak
- Governance and management assessed explicitly, not folded into "operational"
- Scenario bridge present — descriptive risk lists are not actionable
- Facts separated from analysis and implications
