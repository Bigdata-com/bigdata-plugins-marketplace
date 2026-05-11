# Public Company Analysis

## Tools to use for public company analysis

All workflows use Bigdata.com MCP tools:

| Tool Name | Purpose | Prerequisite |
|-----------|---------|--------------|
| `find_securities` | Get RavenPack entity_id | None |
| `bigdata_company_tearsheet` | Financial data, metrics, analyst estimates, jobs trend | `find_securities` |
| `bigdata_search` | Search for news, filings, transcripts, and analyst reactions | None |
| `bigdata_events_calendar` | List historical and upcoming earnings calls, and conference calls | `find_securities` |

## Before you synthesize (all workflows)

Read [analytical-frameworks.md](./analytical-frameworks.md): **EPIC-style filter**, **quality over quantity**, and **lead with the 2–3 factors that actually matter** for this name—before filling every template section evenly.

## Universal output quality

Every deliverable should pass a **PM-style test**:

- **What’s different?** What changed or what is the non-consensus angle?  
- **What matters?** Which 2–3 drivers dominate the setup?  
- **What should I do about it?** Net assessment, key risk, next catalyst (no portfolio sizing).

**Morning-meeting bar:** Would this survive a short, skeptical institutional review without sounding like a data dump?

**Structured closing (use where relevant):**  
`Net assessment: [Positive / Negative / Neutral] because [specific reason]; key risk: [X]; next catalyst: [Y] ([timing if known]).`

For full **conviction / variant perception / scenario** discipline on thesis-style work, see the institutional equity index: [../equity-analysis/main.md](../equity-analysis/main.md).

## Universal report footer (mandatory)

End every user-facing deliverable with the **Powered by Bigdata.com** line and **Disclaimer** exactly as specified in [../report-footer.md](../report-footer.md) (same text as in each workflow output template).

## Core Workflows

### Company Brief
30-day company summary with categorized developments and investment implications.
**See:** [company-brief.md](./company-brief.md)

### Earnings Preview  
Forward-looking pre-earnings analysis: **EPIC** driver table, **FaVeS**, **sentiment/positioning** data, **scenarios + EV**, **watch-for** quality column, wide **legal/regulatory** search net.
**See:** [earnings-preview.md](./earnings-preview.md)

### Earnings Digest
Post-earnings results analysis with surprises and guidance breakdown.
**See:** [earnings-digest.md](./earnings-digest.md)

### Risk Assessment
Comprehensive risk evaluation with SEC filings and likelihood/impact ratings.
**See:** [risk-assessment.md](./risk-assessment.md)

### Valuation snapshot
What the market is paying for vs history/peers and implied expectations—using tearsheet and search (no standalone model required).
**See:** [valuation-snapshot.md](./valuation-snapshot.md)

## Optional: institutional equity layer

When the user wants a **thesis**, **deep valuation**, **forensic quality**, **full moat**, **sector playbook**, or **special-situations** depth beyond these workflows, read [references/equity-analysis/main.md](../equity-analysis/main.md).

**Templates for equity-style outputs** (after you have gathered facts with MCP tools):

| Deliverable | Template |
|-------------|----------|
| Full investment memo | [../../assets/templates/investment-memo.md](../../assets/templates/investment-memo.md) |
| Quick take | [../../assets/templates/quick-take.md](../../assets/templates/quick-take.md) |
| Earnings reaction note | [../../assets/templates/earnings-reaction.md](../../assets/templates/earnings-reaction.md) |

**Risk workflow vs accounting red flags:** This folder’s risk assessment focuses on process, filings, and news. For **manipulation / quality-of-earnings** depth, use [references/equity-analysis/financial-analysis/red-flags-checklist.md](../equity-analysis/financial-analysis/red-flags-checklist.md) and [references/equity-analysis/financial-analysis/quality-of-earnings.md](../equity-analysis/financial-analysis/quality-of-earnings.md).

**Per-workflow hooks:** Each core workflow below includes a short note on when to layer institutional equity references or templates.
