---
name: bigdata-sector-playbook
description: >
  Build an actionable investment playbook for a sector using Bigdata.com data and sector-specific
  frameworks — the KPIs that actually matter in that sector, how to value companies in it and
  why, the live debates and where consensus sits on each, valuation context against the sector's
  own history, a sub-industry map with cycle position, screening criteria and sector-specific
  red flags, and an actionable setup of what to own, avoid, and watch. More operational than a
  sector analysis: it teaches how to invest the sector, not just how it is doing. Triggers:
  "sector playbook for X", "how do I analyze X companies", "what KPIs matter in X",
  "how to value X sector companies", "investing framework for X sector", "X sector cheat sheet".
---

# Bigdata Sector Playbook

The operating manual for a sector: what to measure, what is debated, what to own. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants the framework for investing a sector. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Current performance, valuations, and catalysts | Sector analysis |
| Sectors ranked against each other | Cross-sector comparison |
| A sector inside one country | Country-sector analysis |
| One company against its peers | Peer comparables |

**Analysis vs playbook:** the sector analysis says how the sector is doing right now; the playbook says how to analyze any company in it, and what setup is actionable today.

## Sector references

Load the matching playbook for the sector in scope — routing table: [references/sector-routing.md](./references/sector-routing.md).

| Sector (GICS) | Reference |
|---------------|-----------|
| Information Technology (SaaS / software) | [references/technology-saas.md](./references/technology-saas.md) |
| Financials (banks, insurance) | [references/financials-banks.md](./references/financials-banks.md) |
| Health Care (pharma, biotech, devices) | [references/healthcare-pharma.md](./references/healthcare-pharma.md) |
| Real Estate (REITs) | [references/reits.md](./references/reits.md) |
| Industrials (A&D, machinery, transport) | [references/industrials.md](./references/industrials.md) |
| Consumer Discretionary / Staples | [references/consumer-retail.md](./references/consumer-retail.md) |
| Energy | [references/energy.md](./references/energy.md) |

If the fit is unclear: [references/sector-selection-guide.md](./references/sector-selection-guide.md). For sectors without a dedicated file (Materials, Communication Services, Utilities), build the KPI framework from the closest analog plus first principles — margin structure, capital intensity, cycle drivers — and say that you did.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Sector debates, valuation context, structural trends | None |
| `find_securities` | Entity ids for sector constituents | None |
| `bigdata_company_tearsheet` | KPI availability and current levels across the sector | `find_securities` |
| `bigdata_events_calendar` | Sector catalyst timing | `find_securities` |

**Required on every call:** pass `plugin_slug: "bigdata-sector-playbook"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-sector-playbook`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Load the sector reference

Read the matching file above **before** searching. It defines the KPI vocabulary the rest of the playbook uses.

### Step 2 — KPI framework

Set out the operating and valuation KPIs that matter in this sector, what "good" looks like for each, and where each is found. This is the core of the playbook — a reader should be able to pick up any company in the sector and know what to measure.

### Step 3 — Valuation approach

State how companies in this sector are valued and **why** that method fits the economics — P/AFFO and NAV for REITs, P/TBV and ROTCE for banks, EV/Sales with Rule of 40 for SaaS. Note where the standard method breaks down.

### Step 4 — The live debates

Search for what the sector is actually arguing about:

- "[Sector] investment debate bulls bears"
- "[Sector] structural change disruption outlook"
- "[Sector] margin sustainability capacity"

For each debate: state both sides, where consensus currently sits, and what evidence would settle it. Sector calls are usually made or lost on these.

### Step 5 — Valuation context

Where the sector trades versus its **own** history — not just versus the market. Multiples now against 5- and 10-year ranges, and on what earnings base (peak, mid-cycle, trough). Industry structure: [references/porter-five-forces.md](./references/porter-five-forces.md).

### Step 6 — Sub-industry map

Break the sector into sub-industries, and for each: economics, cycle position, and current setup. Sector-level averages usually hide the dispersion that matters.

### Step 7 — Screening criteria and red flags

- **Screen for:** the metrics that identify quality and value in this sector specifically
- **Red flags:** the sector's characteristic failure modes — channel stuffing in consumer, reserve releases in insurance, capitalized development in software, decline-rate masking in energy

### Step 8 — Actionable setup

Close with what to own, what to avoid, and what to watch — each tied to the KPIs and debates above, with named companies where the evidence supports it.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version if useful.

## Quality bar

Non-negotiables:

- KPI framework is **sector-specific** and usable on any company in the sector
- Valuation method justified by the economics, with its breaking point named
- Debates presented two-sided, with where consensus sits and what would settle them
- Valuation context against the sector's **own** history, on a stated earnings base
- Sub-industry dispersion shown, not averaged away
- Sector-characteristic red flags named
- An actionable setup delivered — own / avoid / watch
