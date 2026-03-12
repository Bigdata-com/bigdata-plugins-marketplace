# Earnings Preview Workflow

Create a forward-looking earnings preview analyzing recent developments, industry trends, bull/bear cases, and key metrics to watch ahead of earnings releases.

## When to Use

- User asks: "Create an earnings preview for [company]"
- User asks: "Preview [company] earnings"
- User requests pre-earnings analysis
- User wants to know what to expect before earnings

## Workflow Steps

### Step 1: Identify the Company

Call `find_companies` with the company name to get the RavenPack entity_id.

### Step 2: Get Financial Baseline

Call `bigdata_company_tearsheet` with the entity_id to get:
- Recent quarterly performance trends
- Historical earnings surprises
- Analyst estimates for upcoming quarter
- Key financial metrics and margins
- Year-over-year comparisons

### Step 3: Identify the date of the next company's earnings call

Call `bigdata_events_calendar` with the entity_id to find out when the next earnings call is.

### Step 4: Search for Recent Developments

Use `bigdata_search` to find relevant information from the last 60-90 days:

**Recommended searches:**
- "[Company Name] recent developments last 90 days"
- "[Company Name] product launches initiatives"
- "[Company Name] guidance commentary management"
- "[Company Name] analyst expectations earnings preview"
- "[Industry] trends headwinds tailwinds"

Conduct 4-6 targeted searches covering:
- Company-specific initiatives and announcements
- Management commentary and guidance
- Analyst previews and expectations
- Industry trends and competitive dynamics
- Macro factors affecting the sector

### Step 5: Analyze and Synthesize

Organize findings into a comprehensive preview covering:

**Recent Developments and Initiatives**
- Product launches or major announcements
- Strategic partnerships or acquisitions
- Operational improvements or challenges
- Geographic expansion or market share changes

**Industry Trends and Sector Dynamics**
- Macro trends affecting the industry
- Competitive landscape changes
- Supply chain or cost pressures
- Regulatory or policy impacts

**Bull Case Analysis**
- Positive drivers that could lead to upside surprise
- Tailwinds supporting strong results
- Areas of operational strength

**Bear Case Analysis**
- Headwinds that could pressure results
- Areas of concern or weakness
- Risks to consensus expectations

**Key Metrics to Watch**
- Most important KPIs for this company
- Metrics that could move the stock
- Areas where surprises are most likely

## Output Format

Add inline citation with Superscript Numbers [1], [2] immediately after claims and add a hyperlink pointing to the document url.

Structure the report as:

```
# Earnings Preview: [Company Name]
Upcoming Earnings: [Date if known]
Reporting for: [Quarter and Fiscal Year]

## Executive Summary
[2-3 sentences on setup heading into earnings]

## Financial Expectations

### Consensus Estimates
- Revenue: [Estimate] (YoY growth: X%)
- EPS: [Estimate] (YoY change: X%)
- Operating Margin: [Estimate]
- [Other key metrics]

### Recent Performance Context
[Brief summary of last quarter's results and trends]

## Recent Developments and Initiatives
[Bulleted list of key developments since last earnings]
- [Development 1 with date and implication]
- [Development 2 with date and implication]

## Industry Trends and Sector Dynamics
[Analysis of broader industry context]
- [Trend 1 and impact on company]
- [Trend 2 and impact on company]

## Bull Case: Drivers for Upside Surprise
1. [Bull point 1]
   - Supporting evidence
   - Potential impact

2. [Bull point 2]
   - Supporting evidence
   - Potential impact

## Bear Case: Risks to Consensus
1. [Bear point 1]
   - Supporting evidence
   - Potential impact

2. [Bear point 2]
   - Supporting evidence
   - Potential impact

## Key Metrics to Watch
1. **[Metric 1]:** Why it matters and what to look for
2. **[Metric 2]:** Why it matters and what to look for
3. **[Metric 3]:** Why it matters and what to look for

## Management Guidance Focus Areas
[What to listen for in guidance and Q&A]
- [Topic 1]
- [Topic 2]

## Investment Implications
[Balanced assessment of risk/reward setup]

## Sources
  ALWAYS include a "Sources" section at the end listing ALL documents referenced with:
   - Reference number matching the inline Superscript Numbers
   - Source name and Publication date (MMM DD, YYYY format) with a hyperlink to the URL
  
   **Example:**
   [1] (NVIDIA Q3 2026 Earnings Call - Nov 19, 2025)[https://www.benzinga.com/node/...]
   [2] (Benzinga - Nov 20, 2025)[https://www.benzinga.com/node/...]
   [3] (Yahoo! Finance - Jan 18, 2026)[https://finance.yahoo.com/news/...]


---

**Powered by Bigdata.com** - https://bigdata.com
```

## Best Practices

- Focus on **forward-looking** analysis, not just historical recap
- Balance bull and bear cases objectively
- Highlight metrics that are most likely to drive stock reaction
- Use recent developments to build investment thesis
- Cite analyst consensus where available from tearsheet
- Search broadly (60-90 days) for context but emphasize recent developments

## Key Differences from Other Workflows

- **vs. Company Brief:** Preview is forward-looking; Brief is retrospective summary
- **vs. Earnings Digest:** Preview is before earnings; Digest is after earnings analysis
- **vs. Risk Assessment:** Preview focuses on near-term earnings drivers; Risk Assessment is comprehensive risk analysis

## Example Queries to User

If earnings date unknown:
- "I don't have the exact earnings date yet. Shall I proceed with the preview based on recent developments and expectations?"

If limited recent news:
- "There's been limited news recently. Would you like me to expand the search period or focus on industry trends?"
