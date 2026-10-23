# ep-narrow#1

USER: What is consensus for Micron's next quarter and what did they guide?

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_events_calendar", "max_results": 4}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["analyst_estimates", "latest_earnings", "earnings_calendar"]}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology guidance for fiscal first quarter 2027 revenue, gross margin and EPS from the fiscal Q4 2026 earnings release"}}}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-ohdwtbsc/bee723e2-0f88-4c6d-9dab-0af380da0816/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791729215.txt; jq -c '.latest_earnings, .events_calendar, .est

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-ohdwtbsc/bee723e2-0f88-4c6d-9dab-0af380da0816/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791729215.txt; jq -c '.estimates.records|length' $F; jq -c '[.

ASSISTANT: Consensus for Micron's next quarter (fiscal Q1 2027, ending late November 2026) is almost exactly at the midpoint of what Micron guided. Analysts have not added any expected beat to their numbers.

**Fiscal Q1 2027: guidance vs. consensus (non-GAAP)**

| Metric | Micron guidance (Sep 30, 2026) | Consensus (FactSet mean) | Consensus vs. guidance midpoint |
|---|---|---|---|
| Revenue | $61.5B ± $1.5B ($60.0B to $63.0B) | $61.63B | +0.2% |
| Gross margin | ~86.25% | 86.28% | +3 basis points |
| Operating expenses | ~$2.06B | ~$2.11B (R&D $1.56B + SG&A $0.55B) | about $45M higher |
| EPS | $38.15 ± $1.00 ($37.15 to $39.15) | $38.19 | +$0.04 |
| GAAP EPS | $37.84 ± $1.00 | $37.98 | +$0.14 |
| Capex | ~$11.5B | $11.28B | slightly lower |

The guided share count is about 1.15 billion, and the guided tax rate is about 15.5%.

**Other points from the guidance**
- **Gross margin will be lowest in Q1.** Micron raised fiscal 2026 bonuses in Q4. Most of the manufacturing part of that cost went into inventory, so it hits Q1 gross margin when that inventory is sold. Management put this and startup costs at about $1B. They expect higher margins for the rest of fiscal 2027, with price increases slowing.
- **Revenue:** Micron expects fiscal 2027 to be another record year, with revenue up every quarter.
- **Supply and cost:** the Q1 guide assumes single-digit growth in bits shipped from Q4 and double-digit unit cost changes for both DRAM and NAND.
- **Spending:** operating expenses rise about $2.5B in fiscal 2027, mostly R&D and higher bonuses. Capex is about $25B in the first half and higher in the second half.
- **Contracts:** Micron has 26 signed supply agreements (customers pay for committed volumes even if they don't take delivery), with about $150B of contracted future revenue. Most of calendar 2027 HBM supply is already contracted at significantly higher prices.

**Context for the print**
- Last quarter (fiscal Q4 2026), Micron beat consensus by 5.6% on revenue ($54.2B vs. $51.3B) and 5.2% on EPS ($33.42 vs. $31.77). Revenue, gross margin and EPS were all above the top of its own guidance range.
- The next report is scheduled for December 16, 2026 (from the Quartr corporate calendar).

The consensus figures are FactSet means pulled today (Oct 23). The data doesn't include how many analysts are in each estimate or how widely they differ.

**Data sources:** [Bigdata.com](https://bigdata.com): FactSet consensus estimates and guidance fields; FMP (latest earnings surprise); Quartr corporate calendar; Micron fiscal Q4 2026 earnings call transcript (S&P Global, FactSet, Quartr), [transcript link](https://app.bigdata.com/documents/6A0919654AA34DAD98411B266DBE7304).
