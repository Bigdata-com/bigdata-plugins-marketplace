# ep-narrow#1

USER: What is consensus for Micron's next quarter and what did they guide?

  [tool call] ToolSearch {"query": "bigdata", "max_results": 10}

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_search", "max_results": 2}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology guidance for next fiscal quarter revenue, gross margin and EPS from latest earnings release", "max_chunks": 20}}}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["analyst_estimates", "earnings_calendar", "latest_earnings"]}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-cmdy-a-9/ac0882c4-4d84-4371-9c8b-e65910abc461/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792434976.txt; jq -c '.latest_earnings, .events_calendar, .est

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-cmdy-a-9/ac0882c4-4d84-4371-9c8b-e65910abc461/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792434976.txt; jq -r '.estimates.records[0]|keys' $F; jq -r '.

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-cmdy-a-9/ac0882c4-4d84-4371-9c8b-e65910abc461/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792434976.txt; jq -c '.estimates.records[]|select(.fiscal_year

ASSISTANT: Now consensus from the tearsheet.

The next quarter is Micron's fiscal Q1 2027, which ends around November 30, 2026. Micron's call is scheduled for December 16, 2026. Consensus sits almost exactly on the midpoint of the company's guidance.

| Metric | Guidance (Sep 30, 2026 call) | Consensus (FactSet mean) | Consensus vs. guidance midpoint |
|---|---|---|---|
| Revenue | $61.5B, plus or minus $1.5B (range $60.0B to $63.0B) | $61.63B | +0.2% |
| Gross margin | about 86.25% | 86.28% | Same |
| Operating expenses | about $2.06B | about $2.11B (R&D $1.56B plus SG&A $0.55B) | About $50M higher |
| Non-GAAP EPS | $38.15, plus or minus $1.00 (range $37.15 to $39.15) | $38.19 | +$0.04 |
| GAAP EPS | $37.84 midpoint (range $36.84 to $38.84) | $37.98 | +$0.14 |
| Tax rate | about 15.5% | about 15.4% (implied) | Same |
| CapEx | about $11.5B | $11.28B | About $0.2B lower |
| Share count | about 1.15B | n/a | n/a |

**Other points from the guidance**
- **Gross margin:** Management said fiscal Q1 should be the lowest gross margin of fiscal 2027. The reason is that Micron raised fiscal 2026 incentive pay in Q4, and most of the manufacturing part of that cost went into inventory, which will be sold in Q1. They expect higher margins for the rest of the year, with prices still rising but more slowly.
- **Full year:** They expect fiscal 2027 to be a record year, with revenue growing every quarter. Operating expenses should rise by about $2.5B for the year. First-half CapEx should be about $25B, with the second half higher.
- **The quarter just reported:** In fiscal Q4 2026, revenue was $54.23B against a $51.33B consensus (5.6% above). EPS was $33.42 against $31.77 (5.2% above). Revenue, gross margin and EPS all came in above the top of Micron's own guidance range.

**Consensus for the following quarters:** Revenue of $66.7B and EPS of $41.86 for fiscal Q2, rising to $75.9B and $49.01 by fiscal Q4. That matches management's comment that revenue will grow every quarter.

The consensus figures are means of analyst estimates and may change between now and December 16. The opex consensus is my sum of the separate R&D and SG&A estimates, and the tax rate is my division of estimated tax by estimated pre-tax income. Neither is a published consensus number.

**Sources**
- [Bigdata.com](https://bigdata.com) company tearsheet for Micron: FactSet consensus estimates, FMP latest-earnings data, Quartr corporate calendar
- [Micron Q4 2026 Earnings Call - FactSet Transcripts, Sep 30, 2026](https://app.bigdata.com/documents/001E01ECA51BFB833652E96A7289C954)
- [Micron Q4 2026 Earnings Call - S&P Global Transcripts, Sep 30, 2026](https://app.bigdata.com/documents/6A0919654AA34DAD98411B266DBE7304)
- [Micron Q4 2026 Earnings Call - Quartr Transcripts, Sep 30, 2026](https://app.bigdata.com/documents/C0336060C7BE19A6A354815E7DE99EF0)
