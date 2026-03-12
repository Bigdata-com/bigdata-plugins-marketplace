# Sector Analysis Workflow

## When to Use
- "Analyze [sector] sector"
- "What's happening in [sector]?"
- Sector performance, trends, or outlook requests

## Workflow Steps

### Step 1: Gather Sector Context
Use `bigdata_search` with queries:
- "[Sector] sector outlook trends analysis"
- "[Sector] sector earnings performance"
- "[Sector] sector headwinds tailwinds"
- "[Sector] sector valuations multiples"
- "[Sector] sector regulatory policy"

### Step 2: Identify Key Companies
Use `find_companies` for 5-10 major sector companies, then `bigdata_company_tearsheet` for each:
- Financial metrics and performance
- Analyst estimates and sentiment
- Revenue segmentation
- ESG scores

### Step 3: Aggregate Sector Metrics
From tearsheets, compile:
- Average P/E, P/S, EV/EBITDA
- Revenue/earnings growth trends
- Analyst rating distribution
- Sentiment indicators

### Step 4: Search Sector Catalysts
Use `bigdata_search`:
- "[Sector] regulatory changes policy"
- "[Sector] technology disruption"
- "[Sector] M&A consolidation"
- "[Sector] earnings expectations"
- "[Sector] supply chain tariffs"

### Step 5: Events Calendar
Use `bigdata_events_calendar` for upcoming earnings/conferences.

## Output Template

```markdown
# Sector Analysis: [Sector Name]
Report Date: [Date]

## Executive Summary
[3-4 sentence overview]

## Sector Performance Overview

### Key Metrics
| Metric | Current | YoY Change | vs. S&P 500 |
|--------|---------|------------|-------------|
| Avg P/E | X.Xx | +/-X% | Premium/Discount |
| Revenue Growth (TTM) | X.X% | +/- bps | Outperform/Underperform |

### Analyst Sentiment
| Rating | % of Coverage |
|--------|---------------|
| Strong Buy/Buy | X% |
| Hold | X% |
| Sell | X% |

## Key Themes & Drivers

### Tailwinds
1. **[Theme]** - [Description], Impact: [Timeline], Beneficiaries: [List]

### Headwinds
1. **[Risk]** - [Description], Severity: [H/M/L], Exposed: [List]

## Sub-Industry Breakdown
| Sub-Industry | Performance | Valuation | Outlook |
|--------------|-------------|-----------|---------|

## Upcoming Catalysts

### Earnings Calendar (Next 30 Days)
| Company | Date | Consensus EPS | Key Metrics |
|---------|------|---------------|-------------|

## Investment Implications
- **Positioning**: [Overweight/Neutral/Underweight]
- **Top Picks**: [Companies with brief thesis]
- **Avoid**: [Areas with rationale]

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com
```

## GICS Sectors Reference
Information Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities
