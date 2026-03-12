# Cross-Sector Comparison Workflow

## When to Use
- "Compare [sector A] vs [sector B]"
- "Which sectors look attractive?"
- Sector rotation analysis
- Relative value across sectors

## Workflow Steps

### Step 1: Define Sectors
GICS sectors: Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities

### Step 2: Gather Sector Data
For each sector, use `bigdata_search`:
- "[Sector] sector performance valuation"
- "[Sector] sector earnings growth estimates"
- "[Sector] sector analyst recommendations"

### Step 3: Select Bellwethers
Use `find_companies` for 3-5 companies per sector, then `bigdata_company_tearsheet`.

### Step 4: Economic Cycle Analysis
Use `bigdata_search`:
- "sector rotation economic cycle"
- "cyclical vs defensive outlook"
- "interest rate sensitive sectors"

## Output Template

```markdown
# Cross-Sector Comparison
Report Date: [Date]

## Executive Summary
[Overview of relative attractiveness]

## Sector Scorecard

| Sector | YTD | P/E | EPS Growth | Sentiment | Score |
|--------|-----|-----|------------|-----------|-------|
| Technology | +X.X% | XX.X | +X.X% | Bullish | ⭐⭐⭐⭐⭐ |
| Financials | +X.X% | XX.X | +X.X% | Neutral | ⭐⭐⭐⭐ |

## Economic Cycle Positioning

**Current Phase**: [Early/Mid/Late Cycle or Recession]

| Phase | Historical Winners | Current Signals |
|-------|-------------------|-----------------|
| Early | Financials, Consumer Disc, Industrials | [Assessment] |
| Mid | Technology, Communication | [Assessment] |
| Late | Energy, Materials, Health Care | [Assessment] |
| Recession | Staples, Utilities, Health Care | [Assessment] |

## Rotation Recommendations

### Overweight
1. **[Sector]** - Score: X/10, Rationale: [Brief], Plays: [Companies]

### Neutral
[Similar format]

### Underweight
[Similar format]

## Key Factors Driving Rotation
1. [Factor]: [Impact on sectors]

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com
```
