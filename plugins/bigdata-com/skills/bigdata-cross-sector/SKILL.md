---
name: bigdata-cross-sector
description: >
  Compare two or more sectors using Bigdata.com data — relative valuations, earnings growth,
  analyst sentiment, and where each sits in the economic cycle — and turn that into a rotation
  call with overweight and underweight recommendations. Includes bellwether-level fundamentals
  per sector and a profitability/ROIC-versus-history read that says whether current valuations
  sit on peak, mid-cycle, or trough earnings power. Triggers: "compare X vs Y sectors",
  "which sectors look attractive", "sector rotation", "cyclicals vs defensives",
  "relative value across sectors", "should I rotate out of X into Y".
---

# Bigdata Cross-Sector Comparison

Relative value and rotation across sectors. Use Bigdata.com plugin tools for every fact.

**Use this skill when** two or more sectors are being weighed against each other. Not this skill when:

| Request | Use instead |
|---------|-------------|
| One sector in depth | Sector analysis |
| A sector inside one country | Country-sector analysis |
| An actionable playbook for investing one sector | Sector playbook |
| Regions rather than sectors | Regional comparison |
| Individual companies within a sector | Peer comparables |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Sector performance, valuation, growth, cycle context | None |
| `find_securities` | Entity ids for 3–5 bellwethers per sector | None |
| `bigdata_company_tearsheet` | Bellwether fundamentals and estimates | `find_securities` |

**Required on every call:** pass `plugin_slug: "bigdata-cross-sector"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-cross-sector`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Define the sectors in scope

GICS sectors: Information Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities. If the user named sectors, use theirs; otherwise confirm which to compare rather than sweeping all eleven.

### Step 2 — Gather sector data

For **each** sector in scope:

- "[Sector] sector performance valuation"
- "[Sector] sector earnings growth estimates"
- "[Sector] sector analyst recommendations"

### Step 3 — Select bellwethers

Use `find_securities` for 3–5 companies per sector, then `bigdata_company_tearsheet` for each. These anchor the sector-level numbers in something checkable.

### Step 4 — Economic cycle analysis

- "sector rotation economic cycle"
- "cyclical vs defensive outlook"
- "interest rate sensitive sectors"

### Step 5 — Profitability and ROIC spread context

For **each** sector, add a short read on profitability versus history (or versus cost of capital), using bellwether tearsheets and search:

- "[Sector] sector ROIC margin cycle vs historical average"
- "sector profitability peak trough"

State whether current valuations sit on **peak**, **mid-cycle**, or **trough-like** earnings power — where the evidence allows. This is the difference between a comparison that misleads and one that informs: a low P/E on peak earnings is not cheap. Deeper framework: [references/porter-five-forces.md](./references/porter-five-forces.md).

### Step 6 — Rotation call

Rank the sectors and state the rotation explicitly: what to overweight, what to underweight, and the specific reason for each. Tie the call to cycle positioning and the earnings-power read, not to trailing multiples alone.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- **Inline citations** `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL.
- End with the numbered **Sources** table (source, date, URL), then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown. After delivering, you may ask: "Would you like me to create a Word document or presentation with this analysis?"

## Quality bar

Non-negotiables:

- Every sector in scope covered on the **same** metrics, so the comparison is like-for-like
- Cycle positioning stated per sector, not just aggregate market commentary
- Peak / mid / trough earnings-power read attempted, or its data limits flagged
- A rotation call actually made — overweight and underweight, with reasons
- Every claim from a source carries an inline citation and appears in the Sources table
