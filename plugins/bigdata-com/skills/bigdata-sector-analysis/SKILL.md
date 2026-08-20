---
name: bigdata-sector-analysis
description: >
  Analyze a market sector using Bigdata.com data — performance, valuations, themes,
  sub-industries, and upcoming catalysts. Maps the sector to its own operating and valuation
  KPIs rather than generic P/E, reads cycle and profitability positioning as early, mid, or late
  versus history, aggregates bellwether tearsheet metrics, and closes with a positioning call
  plus top picks and areas to avoid. Triggers: "analyze the X sector", "what's happening in X
  sector", "X sector outlook", "how is the X industry doing", "X sector valuations",
  "is the X sector attractive", "semiconductor/energy/healthcare sector view".
---

# Bigdata Sector Analysis

Full read on one sector: where it trades, what drives it, and what is coming. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the subject is one sector. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Two or more sectors compared, or rotation | Cross-sector comparison |
| A sector inside a specific country or region | Country-sector analysis |
| An actionable KPI-and-debates playbook for investing the sector | Sector playbook |
| A macro theme that cuts across sectors | Thematic research |
| One company in the sector | Company brief / investment memo |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Sector trends, valuations, policy, catalysts, cycle context | None |
| `find_securities` | Entity ids for 5–10 sector bellwethers | None |
| `bigdata_company_tearsheet` | Per-company metrics, estimates, sentiment, segments | `find_securities` |
| `bigdata_events_calendar` | Upcoming earnings and conferences | `find_securities` |

**Required on every call:** pass `plugin_slug: "bigdata-sector-analysis"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-sector-analysis`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

Run **5–10 targeted searches** across the workflow. Include temporal context ("last 30 days", "2026 outlook").

## Workflow

### Step 1 — Sector context

Search:

- "[Sector] sector outlook trends analysis"
- "[Sector] sector earnings performance"
- "[Sector] sector headwinds tailwinds"
- "[Sector] sector valuations multiples"
- "[Sector] sector regulatory policy"

### Step 2 — Sector-specific KPI lens (GICS)

Do **not** rely only on generic P/E, P/S, and EV/EBITDA. Map the sector to its primary operating and valuation KPIs:

| GICS sector | Emphasize these KPIs |
|-------------|----------------------|
| Information Technology / Software-SaaS | ARR growth, NRR, Rule of 40, FCF margin, payback |
| Financials | NIM, CET1 / capital, credit costs, ROTCE, efficiency |
| Health Care (incl. Pharma) | Growth drivers, pipeline / patent, R&D, payer mix, regulatory |
| Real Estate (REITs) | AFFO, NAV, cap rates vs bonds, same-store NOI |
| Industrials | Backlog, book-to-bill, margin mix, OEM / capex cycle |
| Consumer Discretionary / Staples | Same-store sales, promo, input costs, private label |
| Energy | Commodity linkage, breakeven, FCF at forward curve, capital discipline |
| Materials | Price/volume, capacity, inventory, China / construction linkage |
| Communication Services | Subscribers, ARPU, churn, ad market / streaming economics |
| Utilities | Allowed ROE, rate case risk, weather / load growth |
| (Other) | Default to margin trajectory, ROIC vs peers, and segment growth |

Deeper playbooks: [references/sector-routing.md](./references/sector-routing.md).

### Step 3 — Key companies

Use `find_securities` for 5–10 major sector companies, then `bigdata_company_tearsheet` for each: financial metrics and performance, analyst estimates and sentiment, revenue segmentation, ESG scores.

### Step 4 — Aggregate sector metrics

From the tearsheets, compile sector-relevant multiples (per Step 2, not only P/E), the Step 2 KPIs where visible, revenue and earnings growth trends, the analyst rating distribution, and sentiment indicators.

### Step 5 — Cycle and profitability positioning

Add brief, evidence-based cycle context:

- Search "[Sector] sector ROIC profitability cycle outlook" and "[Sector] margin cycle vs history"
- State whether ROIC (or a sector proxy) and margins look **early / mid / late** versus a normal cycle — or flag the data limits
- Industry-economics mental model: [references/porter-five-forces.md](./references/porter-five-forces.md)

### Step 6 — Catalysts

Search:

- "[Sector] regulatory changes policy"
- "[Sector] technology disruption"
- "[Sector] M&A consolidation"
- "[Sector] earnings expectations"
- "[Sector] supply chain tariffs"

### Step 7 — Events calendar

Use `bigdata_events_calendar` for upcoming earnings and conferences across the bellwethers.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables in every sector analysis:

- Sector-specific KPIs present — a report built only on P/E has not done the job
- Cycle positioning stated (early / mid / late) or its data limits flagged
- Tailwinds and headwinds name **which companies** are exposed
- Positioning call given: overweight / neutral / underweight, with top picks and areas to avoid
- Every claim from a source carries an inline citation and appears in the Sources table

## GICS sectors reference

Information Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities.
