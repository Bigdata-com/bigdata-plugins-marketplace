# Public Company Analysis

## Tools to use for public company analysis

All workflows use Bigdata.com MCP tools:

| Tool Name | Purpose | Prerequisite |
|-----------|---------|--------------|
| `find_companies` | Get RavenPack entity_id | None |
| `bigdata_company_tearsheet` | Financial data, metrics, analyst estimates, jobs trend | `find_companies` |
| `bigdata_search` | Search for news, filings, transcripts, and analyst reactions | None |
| `bigdata_events_calendar` | List historical and upcoming earnings calls, and conference calls | `find_companies` |


## Core Workflows

### Company Brief
30-day company summary with categorized developments and investment implications.
**See:** [company-brief.md](./company-brief.md)

### Earnings Preview  
Forward-looking pre-earnings analysis with bull/bear cases.
**See:** [earnings-preview.md](./earnings-preview.md)

### Earnings Digest
Post-earnings results analysis with surprises and guidance breakdown.
**See:** [earnings-digest.md](./earnings-digest.md)

### Risk Assessment
Comprehensive risk evaluation with SEC filings and likelihood/impact ratings.
**See:** [risk-assessment.md](./risk-assessment.md)
