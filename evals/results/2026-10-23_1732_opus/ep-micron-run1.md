# ep-micron#1

USER: Earnings preview for Micron

  [tool call] Skill {"skill": "bigdata-com:bigdata-earnings-preview", "args": "Micron"}

  [tool call] Bash {"command": "cd \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-earnings-preview/references\"; ls; ls sectors 2>/dev/null; cat working-with-bigdata.md output-standard.md", "description": "List and read ski

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_fetch_document,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet,mcp__claude_ai_Bigdata_com__bigdat

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU", "plugin_slug": "bigdata-earnings-preview"}

  [tool call] Bash {"command": "cd \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-earnings-preview/references\"; cat expectations.md base-rates.md operating-leverage-and-tam.md", "description": "Read analysis method referen

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["company_overview", "earnings_calendar", "analyst_ratings", "latest_earnings", "analyst_estimates"], "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_events_calendar {"filters": {"calendar_type": "corporate_calendar", "rp_entity_ids": ["49BBBC"], "start_date": "2026-10-23", "end_date": "2027-01-31"}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-1cunynjp/95551adc-e559-4103-846e-b587fd8c46ab/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791173797.txt\njq -c 'del(.estimates)' $F; echo; jq -c '.estim

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-1cunynjp/95551adc-e559-4103-846e-b587fd8c46ab/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791173797.txt\njq -r '.estimates.records[0]|keys|join(\",\")' 

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["financial_statements", "financial_ratios", "key_metrics", "revenue_segmentation"], "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "outlook guidance for fiscal first quarter revenue gross margin EPS", "filters": {"reporting_entities": ["49BBBC"], "reporting_periods": [{"fiscal_year": 2026, "fiscal_quarter": 4}], "document_type": {"mode": "INCLUDE", "values": [{"type": "TRANS

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology fiscal Q4 2026 earnings call guidance for fiscal first quarter 2027 revenue, gross margin and EPS", "max_chunks": 15}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_fetch_document {"id": "001E01ECA51BFB833652E96A7289C954", "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron Technology stock fall in October 2026?", "max_chunks": 15}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "DRAM and NAND contract price trends for the fourth quarter of 2026", "filters": {"timestamp": {"start": "2026-09-30T00:00:00Z", "end": "2026-10-23T23:59:59Z"}}, "max_chunks": 15}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "DRAM contract prices fourth quarter increase TrendForce", "filters": {"category": {"mode": "INCLUDE", "values": ["news", "news_premium", "news_public"]}, "keyword": {"any_of": ["DRAM", "contract price"]}, "timestamp": {"start": "2026-09-25T00:00

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "SK hynix third quarter 2026 earnings results and memory outlook", "max_chunks": 12}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology Taiwan workers strike vote October 2026", "max_chunks": 8}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Analyst notes on Micron Technology ahead of fiscal Q1 2027 earnings: price target changes and estimate revisions in October 2026", "max_chunks": 15}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "Now turning to guidance. We expect fiscal revenue to be plus or minus, gross margin, EPS per share plus or minus", "filters": {"reporting_entities": ["49BBBC"], "reporting_periods": [{"fiscal_year": 2024, "fiscal_quarter": 4}, {"fiscal_year": 20

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet {"rp_entity_id": "49BBBC", "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology share repurchase authorization announcement October 2026", "max_chunks": 10}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Samsung Electronics third quarter 2026 memory division results, DRAM prices and HBM", "max_chunks": 10}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "Non-GAAP diluted earnings per share was, revenue was, above the high end of guidance", "filters": {"reporting_entities": ["49BBBC"], "reporting_periods": [{"fiscal_year": 2025, "fiscal_quarter": 1}, {"fiscal_year": 2025, "fiscal_quarter": 2}, {"

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "non-GAAP guidance for fiscal Q2 revenue plus or minus EPS", "filters": {"reporting_entities": ["49BBBC"], "reporting_periods": [{"fiscal_year": 2024, "fiscal_quarter": 4}, {"fiscal_year": 2025, "fiscal_quarter": 1}], "document_type": {"mode": "I

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron and chip stocks fall on October 22, 2026?", "max_chunks": 10}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "SK hynix third-quarter operating profit results DRAM ASP bit shipments", "filters": {"category": {"mode": "INCLUDE", "values": ["news", "news_premium", "news_public"]}, "keyword": {"any_of": ["SK hynix", "SK Hynix"]}, "timestamp": {"start": "202

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "Non-GAAP diluted earnings per share in fiscal quarter was, up sequentially", "filters": {"reporting_entities": ["49BBBC"], "reporting_periods": [{"fiscal_year": 2025, "fiscal_quarter": 4}, {"fiscal_year": 2026, "fiscal_quarter": 1}, {"fiscal_yea

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron fiscal Q1 2025 earnings call December 2024 guidance for fiscal Q2 2025 revenue and EPS", "max_chunks": 6}}, "plugin_slug": "bigdata-earnings-preview"}

  [tool call] Bash {"command": "cd \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-earnings-preview/references\"; wc -l *.md; grep -n -i \"steady-state\\|steady state\" expectations.md | head -20; echo ----; grep -n \"^#\" b

  [tool call] Bash {"command": "cd \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-earnings-preview/references\"; sed -n 21,231p base-rates.md", "description": "Read base-rate procedure and reference tables"}

  [tool call] Bash {"command": "cd \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-earnings-preview/references\"; grep -n -i -A3 \"earnings\\b\\|surprise\\|drift\" after-a-price-move.md | head -80; echo ======; grep -n -i -B

  [tool call] Bash {"command": "python3 -I - <<'EOF'\ng=[(\"Q2 FY25\",7.9,1.43,8.053,1.56),(\"Q3 FY25\",8.8,1.57,9.301,1.91),(\"Q4 FY25\",10.7,2.50,11.315,3.03),(\"Q1 FY26\",12.5,3.75,13.643,4.78),(\"Q2 FY26\",18.7,8.42,23.860,12.20),(\"Q3 FY26\",33.5,19.15,41.456,25.11),(\"Q4 FY26\",50.0,31.0,54.229,33.42)]\nfor q,gr

ASSISTANT: # Micron Technology (MU) earnings preview: fiscal Q1 2027, reports 16 Dec 2026 after market close

Data as of: price is the 22 Oct 2026 close ($856.49). Estimates are the FactSet consensus retrieved 23 Oct 2026; the tearsheet does not give a vintage date or the number of estimates. Latest statements are fiscal Q4 2026, the quarter ended Aug/Sep 2026. Newest document read is dated 23 Oct 2026. The calendar lists the call at 23:00 UTC on 16 Dec 2026.

## The setup

The quarter depends mainly on how fast DRAM and NAND contract prices keep rising, and on the fiscal Q2 guide. Management guided fiscal Q1 to $61.5bn of revenue (plus or minus $1.5bn), about 86.25% gross margin and $38.15 EPS (plus or minus $1) [1]. Consensus sits almost exactly on that midpoint: $61.63bn and $38.19.

Measured against Micron's record, that bar is low. In each of the last seven quarters with a published guide, revenue and EPS came in above the guided midpoint. The revenue beat was 2% to 28%. But the beat narrowed to 8.5% last quarter, and price increases are slowing: DRAM prices rose in the low 60s percent in fiscal Q3 and in the high teens in fiscal Q4 [15].

The stock fell about 20% in the month to 22 Oct while consensus for the quarter rose about 7%. At about 4.9x fiscal 2027 consensus EPS, the price treats fiscal 2027 as a peak. The guidance at the print is therefore less important than three items on the call:

- the fiscal Q2 guide;
- whether management repeats that supply will be tighter in calendar 2027 and 2028;
- how fast the $35.16bn buyback, which can start on 9 Dec, will be used.

## The quarter at a glance

| Metric (fiscal Q1 2027) | Consensus | Change since 1 Oct | Guidance (low / mid / high) | Prior year (Q1 FY26) | Growth y/y | Prior quarter (Q4 FY26) | Basis | Source |
|---|---|---|---|---|---|---|---|---|
| Revenue | $61.63bn | +7.4% (from $57.40bn) | $60.0 / $61.5 / $63.0bn | $13.64bn | +352% | $54.23bn (a 14-week quarter) | reported; growth derived | Data, [1], [2] |
| Gross margin | 86.3% | n/a | about 86.25% | 56.0% | +30 pts | 86.8% (company non-GAAP: 87.0%) | reported | Data, [1] |
| EBIT | $50.79bn (82.4% margin) | n/a | about $51.0bn implied (82.9%) | $6.13bn | +728% | $44.28bn | reported; guide-implied figure derived | Data, [1] |
| EPS (non-GAAP) | $38.19 | +7.7% (from $35.47) | $37.15 / $38.15 / $39.15 | $4.78 | +699% | $33.42 | reported | Data, [1], [2], [5] |
| Opex (R&D + SG&A) | $2.11bn | n/a | about $2.06bn | $1.51bn | | $2.77bn | reported | Data, [1] |
| Free cash flow | $29.43bn | n/a | "significantly higher than the $33 billion" (verbal) | $2.89bn | | $32.69bn | reported | Data, [1] |
| Capex | $11.28bn | n/a | about $11.5bn | $5.39bn | | $11.11bn | reported | Data, [1] |

Notes on the table:
- The "change since 1 Oct" column compares today's mean with the FactSet consensus quoted by MT Newswires on 1 Oct, before the guide had been absorbed [2]. The tearsheet does not give 30-day or 90-day revision history.
- The guide-implied EBIT is revenue midpoint x 86.25% - $2.06bn.
- Revenue growth from fiscal Q4 to Q1 is +13.7% as reported. Because fiscal Q4 had 14 weeks and Q1 has 13, growth per week is about +22% (derived) [15].
- The free cash flow consensus is below what management said verbally on the call. Customer deposits under the long-term contracts are booked in financing cash flow and do not count toward free cash flow [1], so a definition difference is possible.

## Guidance record

| Quarter | Guided revenue midpoint | Actual revenue | Difference | Guided EPS midpoint | Actual EPS | Difference | Source |
|---|---|---|---|---|---|---|---|
| Q1 FY25 | not retrieved | $8.71bn | "at the midpoint" (management) | not retrieved | $1.79 | "above the midpoint" | [9], [8] |
| Q2 FY25 | $7.9bn | $8.05bn | +1.9% | $1.43 | $1.56 | +9.1% | [9], [8] |
| Q3 FY25 | $8.8bn | $9.30bn | +5.7% | $1.57 | $1.91 | +21.7% | [8], [7] |
| Q4 FY25 | $10.7bn | $11.32bn | +5.7% | $2.50 | $3.03 | +21.2% | [7], [6] |
| Q1 FY26 | $12.5bn | $13.64bn | +9.1% | $3.75 | $4.78 | +27.5% | [6], [5] |
| Q2 FY26 | $18.7bn | $23.86bn | +27.6% | $8.42 | $12.20 | +44.9% | [5], [10] |
| Q3 FY26 | $33.5bn | $41.46bn | +23.7% | $19.15 | $25.11 | +31.1% | [4], [3] |
| Q4 FY26 | $50.0bn | $54.23bn | +8.5% | $31.00 | $33.42 | +7.8% | [3], [1] |

Actual revenue is FactSet data; actual EPS is non-GAAP as stated on each call. The differences are derived.

Pattern: EPS came in above the guided midpoint in all 8 quarters. Revenue did so in 7 of 8, and the other was at the midpoint. The size of the beat peaked in fiscal Q2 to Q3 2026 and fell back to about 8% last quarter. If the last quarter's pattern repeats, revenue would land near $66bn, against $61.6bn consensus. If the beat keeps shrinking as price increases slow, a print near the top of the range ($63bn) is the closer comparison.

## Drivers

**1. DRAM pricing (73% of fiscal Q4 revenue) [1].**
- What consensus assumes: about 22% revenue growth per week from Q4 to Q1, which requires price increases of at least the mid-teens percent plus some bit growth (derived; the split between price and volume cannot be inferred from the estimates).
- Evidence since the call:
  - TrendForce expects conventional DRAM contract prices to rise 10-15% from calendar Q3 to Q4, and notes that price ceilings in long-term contracts are slowing increases (6 Oct) [12].
  - Including HBM (high-bandwidth memory, the stacked DRAM used in AI accelerators), TrendForce expects the DRAM increase to be 15-20% (23 Oct) [13].
  - KeyBanc expects DRAM prices to rise 15-20% in calendar Q4 and another 10-15% in calendar Q1 [14].
- Direction of risk: neutral to slightly positive. Micron's fiscal Q1 (September to November) covers most of calendar Q4 pricing.

**2. NAND and data center SSDs (26% of revenue) [1].**
- What consensus assumes: not separable from the total.
- Evidence: in fiscal Q4, NAND prices rose about 30% and NAND bits about 10%, and data center SSD revenue was nearly $10bn [1]. TrendForce expects NAND contract prices to rise 15-20% in calendar Q4 and enterprise SSD prices 23-28% [13]. SK hynix has dropped its plan for a US listing of its Solidigm NAND subsidiary, which LYNX Equity Strategies reads as lowering the risk of NAND oversupply (sentiment data).
- Direction of risk: positive.

**3. Gross-margin costs and Taiwan labor.**
- What the guide includes: about $1bn of extra cost in fiscal Q1, mostly fiscal 2026 incentive pay that was absorbed into inventory, plus start-up costs. Management called fiscal Q1 "the floor for gross margins in fiscal 2027" [1].
- Evidence since the call:
  - The union at the Taoyuan plant held a 24-hour strike on 22 Oct [19].
  - On 22 Oct, Micron Taiwan's president said the company would introduce a quarterly profit-sharing bonus for all staff worldwide starting in fiscal 2027 [18]. The Taoyuan union rejected the offer, and the next talks are set for 27 Oct [18]. The union at the Taichung plant has settled [20].
  - The cost of the new bonus scheme has not been disclosed. Each 100 basis points of gross margin is worth about $0.45 of EPS (derived).
- Direction of risk: negative for margin; small for revenue unless the strikes are repeated.

**4. Bit supply and the shorter quarter.**
- What consensus assumes: revenue up 13.7% as reported, on one fewer week.
- Evidence: days of inventory rose to 129, partly from building ahead of end-of-life nodes, and management expects that figure to fall in the coming quarters [1]. More than 75% of 2027 output is already committed [1].
- Direction of risk: neutral. There is no new evidence on bit shipments.

**5. HBM pricing and mix.**
- What consensus assumes: the gross margin consensus of 86.5% for fiscal Q2 implies some lift from HBM.
- Evidence: Micron has contracted most of its calendar 2027 HBM supply at "much higher" prices than 2026, with the increases starting in calendar 2027 [1].
- Direction of risk: little effect on fiscal Q1; it matters for the fiscal Q2 guide.

## Consensus against base rates

All base rates below are historical, from the top 1,000 global companies, 1950-2015, inflation-adjusted. They are not forecasts.

- **Fiscal 2027 revenue** consensus of $275.8bn requires 107% nominal growth, about 101% real at an assumed 3% inflation. Across all sizes, 5.5% of companies grew real sales more than 45% in a single year. The source does not publish one-year figures by size. Micron's starting revenue of $133bn puts it in the largest class (above $50B); the closest available figure for that class is that only 2.8% achieved a real sales CAGR of 20% or more over three years.
- **Two-year revenue path:** fiscal 2028 consensus of $329.0bn requires a 57% nominal CAGR, about 53% real. That rate is beyond every published band for companies above $50B.
- **Fiscal 2027 EPS** consensus of $174.63 requires 131% nominal growth, about 125% real. Across all sizes, 24.4% of companies grew real net income 30% or more in one year; higher thresholds are not published.
- **Fiscal 2028 EPS** of $213.97 implies a 68% two-year CAGR. In the above-$50B class, 13.5% grew net income 30% or more a year over three years, and 42.6% had lower net income after three years.

## What is priced in

- **Price:** down 20.1% over one month and up 323% over one year (Data). Over the month to 19 Oct, the Nasdaq 100 fell 0.4% while Micron fell 10.9% [16]. The fall came after the results: on news of a strike vote, a claimed DRAM design breakthrough at the Chinese DRAM maker CXMT, a hot inflation print, and on 22 Oct, worries about oil prices and how AI spending will be financed [16], [17], [22].
- **Forward P/E against steady-state P/E:**
  - Micron trades at 4.9x fiscal 2027 consensus EPS (derived).
  - The steady-state P/E is the multiple a company deserves if current earnings simply continue with no further value creation; it equals 1 divided by the cost of equity. At an assumed 10% cost of equity (about 5% risk-free rate plus a 5% equity premium, assumed), it is 10x. The ratio of 0.49 means the price assumes earnings fall from the fiscal 2027 level.
  - After subtracting $49 per share of net cash, the price equals a perpetual EPS of about $81 at 10% (derived). The net cash figure is $68.3bn less the $12.7bn of customer deposits that must be returned [1]. The range is $73 at 9% and $97 at 12%.
  - That is about 46% of fiscal 2027 consensus EPS and close to the $75.52 Micron earned in fiscal 2026.
- **Estimates against price:** consensus for the quarter rose about 7.5% since 1 Oct while the price fell about 20%. Expectations for the quarter went up while the valuation multiple shrank, which means the market is discounting how long these earnings last, not the near-term numbers.
- **Sentiment:** news sentiment over 90 days is -0.28 against a -0.20 baseline. The one-month z-score is -1.05 (sentiment about one standard deviation below its normal range). The negative stories are mostly sector-wide: AI capex funding, CXMT and the Taiwan strike (Data).
- **Analyst targets:** mean $1,589, range $1,200 to $3,000. The lowest target is 40% above the price (Data). Equisights set a fair value of $714 [27], which is below the price and is not in the tearsheet sample.

The bar for the printed quarter is low. Consensus equals the guide midpoint, and Micron has beaten its midpoint for eight quarters. The bar for the stock is set by fiscal 2028: the price already allows for earnings roughly halving from fiscal 2027 levels, so the guidance and the commentary on calendar 2028 supply matter more than the size of the fiscal Q1 beat.

## Sensitivity

| Revenue vs consensus | EBIT effect, inside view (0.86) | EBIT effect, sector beta (0.173) | EPS effect (inside / sector) | Basis |
|---|---|---|---|---|
| -5% (-$3.08bn) | -$2.65bn | -$0.53bn | -$1.95 (-5.1%) / -$0.39 (-1.0%) | derived |
| -3% (-$1.85bn) | -$1.59bn | -$0.32bn | -$1.17 (-3.1%) / -$0.24 (-0.6%) | derived |
| +3% | +$1.59bn | +$0.32bn | +$1.17 / +$0.24 | derived |
| +5% | +$2.65bn | +$0.53bn | +$1.95 / +$0.39 | derived |

How the table is built:
- Formula: change in EPS = change in revenue x margin beta x (1 - 15.5% tax rate) / 1.15bn shares. The tax rate and share count are from the guidance [1].
- Inside view: Micron's own incremental operating margin from fiscal Q3 to Q4 2026 was 0.86. In the two quarters before that it was 0.98 (Data).
- Outside view: the historical operating margin beta for information technology is 0.173 (1950-2015).
- The inside view is the relevant one here. Revenue swings are driven by price, which flows almost entirely to profit. The sector beta understates the effect for this quarter.
- Cycle context: in fiscal 2025, the last year of the 8 quarters in the tearsheet that was not at peak pricing, the operating margin was 26.8%. Consensus for this quarter is 82.4%. A pre-2025 mid-cycle margin cannot be computed from the data available here.

## Scenarios

| Case | What has to be true | Revenue / EPS vs consensus | Probability | Likely reaction | Watch for |
|---|---|---|---|---|---|
| Beat and raise | DRAM prices up mid-teens or more, NAND up about 20%, labor costs contained; fiscal Q2 guide well above $66.7bn | Revenue at least $63bn (+2%), EPS at least $39.50 | 50% | +5% to +12% | Fiscal Q2 revenue guide above $69bn, with tighter calendar 2028 supply repeated |
| In line | Prices up about 10-15%, gross margin near 86.25%, fiscal Q2 guide near consensus | Revenue $61.5-63bn, EPS $38-39.5 | 35% | -3% to -8% | Fiscal Q2 guide of $65-68bn with no change to the 2028 commentary |
| Miss or cut | Price ceilings in long-term contracts bind, lost output or profit-sharing cost from Taiwan, or slower customer orders | Revenue below $61.5bn or fiscal Q2 guide below $64bn | 15% | -10% to -20% | Gross margin below 85.5%, or any softening of the "no line of sight to balance" language |

How the probabilities and reactions were set:
- Probabilities start from the 8-of-8 EPS beat record. They are reduced from that because the beat has been shrinking and price increases are slowing (judgment).
- The reaction ranges are judgment. After the last beat-and-raise, the stock fell 1-2% the next day [2], so a beat alone is not enough to lift it.
- The expected value of the three cases is about 0%, which is consistent with the conclusion that the price is set by fiscal 2028 rather than fiscal Q1.
- For context, historical base rates show that after earnings-driven one-day drops of 10% or more in stocks with strong momentum, the stock kept drifting lower: -1.5% over the next 30 days (N 408, 1990-2014).

## What to check first

1. **Fiscal Q2 revenue guide midpoint** against $66.7bn consensus. Below $64bn is negative; above $69bn is positive.
2. **Fiscal Q1 revenue** against the $61.5bn midpoint and the $63bn top of the range. A figure below $62bn would break the pattern of beats.
3. **Gross margin** against 86.25%, and the fiscal Q2 gross margin guide against 86.5% consensus. Management called fiscal Q1 the floor, so a fiscal Q2 guide below 86.25% would contradict that.
4. **DRAM and NAND price changes from Q4 to Q1.** Last quarter they were high teens and about 30%. Below 10% for DRAM would indicate the contract price ceilings are binding.
5. **Free cash flow** against $29.4bn consensus and the verbal "significantly higher than $33bn".
6. **Buyback size and pace** from 9 Dec under the $35.16bn authorization [21].
7. **Long-term contract count and RPO** (remaining performance obligations, the contracted value of future revenue) against 26 contracts and about $150bn [1].

## Questions for the call

1. How much did DRAM and NAND prices rise in fiscal Q1, and how much of the fiscal Q2 guide depends on the price ceilings in the long-term contracts? This tests drivers 1 and 2, and TrendForce's statement that ceilings are slowing increases [12].
2. What does the new quarterly profit-sharing scheme cost per quarter, and is it in the fiscal Q2 gross margin guide? Did the 22 Oct strike affect output? This tests driver 3 [18], [19].
3. Has the target cash level been reached, and how fast will the $35.16bn authorization be used? This tests the September statement that excess cash will be returned [1], [21].
4. Is calendar 2028 still tighter than 2026, given industry cleanroom additions and CXMT's claimed 4F2 server DRAM (a denser memory-cell layout) shipping by the end of 2026? This tests the "no line of sight" claim [1], [17].
5. Are customers reducing memory content per server further, and what is the HBM4E timing with NVIDIA? This tests the September statements on content growth and on custom HBM [1].

## What would change this view

- SK hynix's Q3 results and 2027 commentary in late October. The bar was raised to about KRW 77trn of operating profit [23], [24].
- The Taoyuan labor talks on 27 Oct, and any repeat strike [18].
- TrendForce's December contract price update. A DRAM increase below 10% would weaken the positive case.
- Whether CXMT actually ships 4F2 server DRAM by the end of 2026 [17].
- How quickly the buyback starts after 9 Dec [21].

## Gaps

- The tearsheet has no estimate count, no vintage date and no 30-day or 90-day revision history; the 1 Oct press consensus was used as the reference point.
- The guided midpoints for Q1 FY25 were not retrieved.
- Samsung's Q3 memory results were not found.
- Bigdata.com does not carry short interest, options positioning or whisper numbers.
- The tearsheet covers only 8 quarters, so the mid-cycle margin uses fiscal 2025.
- The price used is the 22 Oct close. The press reported a rise of about 3.5% on 23 Oct [sentiment data] that is not reflected here.

## Sources

[1] [Micron Technology, Inc.: Q4 2026 Earnings Call - Sep 30, 2026 (FactSet)](https://app.bigdata.com/documents/001E01ECA51BFB833652E96A7289C954)
[2] [MT Newswires: Micron Shares Fall Despite Strong Earnings, Guidance - Oct 1, 2026](https://app.bigdata.com/documents/598954447715B13C6F62F95BFDFCF9A4?cnum=1)
[3] [Micron Q3 2026 Earnings Call - Jun 24, 2026 (S&P Global)](https://app.bigdata.com/documents/4448B479D4BC7928B23639F8731A3130?cnum=22)
[4] [Micron Q2 2026 Earnings Call - Mar 18, 2026 (S&P Global)](https://app.bigdata.com/documents/13E19F661B93A4636B11EBE98C9E6411?cnum=21)
[5] [Micron Q1 2026 Earnings Call - Dec 17, 2025 (S&P Global)](https://app.bigdata.com/documents/EC92612230AFD7F5EAEC9BF55901E8F7?cnum=21)
[6] [Micron Q4 2025 Earnings Call - Sep 23, 2025 (S&P Global)](https://app.bigdata.com/documents/8F7D9DC679CDD9D6A5876340B9928E77?cnum=23)
[7] [Micron Q3 2025 Earnings Call - Jun 25, 2025 (S&P Global)](https://app.bigdata.com/documents/230B5D4B7C458EBB52E2477C033049CA?cnum=22) and [FactSet transcript, EPS $1.91](https://app.bigdata.com/documents/0744AC4F3012B3C66CCD545FC7BAEF07?cnum=21)
[8] [Micron Q2 2025 Earnings Call - Mar 20, 2025 (Quartr)](https://app.bigdata.com/documents/31DD9A3C79747644530F217A8A7B7244?cnum=22)
[9] [Micron Q1 2025 Earnings Call - Dec 18, 2024 (S&P Global)](https://app.bigdata.com/documents/460019FEC5F39D5C50F38F67685E0D1A?cnum=25) and [Quartr transcript](https://app.bigdata.com/documents/06C989DCBF154FE0BA3D359B829C316D)
[10] [Micron Q2 2026 Earnings Call - Mar 18, 2026 (Quartr)](https://app.bigdata.com/documents/CAB6A37085191E7ED822C7BBA679304F?cnum=22)
[12] [US News: Samsung's Q3 Profit Seen Jumping Nine-Fold, but Chip Margins May Be Flat - Oct 6, 2026](https://app.bigdata.com/documents/AECC5C041EC558E96C8F20C22CD0B2A4?cnum=3)
[13] [Eastmoney: Jensen Huang and price hike data speak up at the same time - Oct 23, 2026](https://app.bigdata.com/documents/661C554A32740190FCA66C9775873B63?cnum=3)
[14] [Flush Financial: KeyBanc memory price forecasts - Oct 23, 2026](https://app.bigdata.com/documents/11CD7D011D12565B863D0EEDB08EBF22?cnum=5)
[15] [Nasdaq: History Says Micron Stock Saves Its Biggest Gains for the Fourth Quarter - Oct 13, 2026](https://app.bigdata.com/documents/08D4210BD17C69099921B2E7EB59628B?cnum=5)
[16] [Yahoo! Finance: Micron Just Dropped 10% in a Month - Oct 20, 2026](https://app.bigdata.com/documents/B091E15F450A4423C3FAB9B4C4671FFC?cnum=2&cnum=1)
[17] [MT Newswires: SK Hynix, Micron Shares Fall on CXMT Breakthrough Reports - Oct 13, 2026](https://app.bigdata.com/documents/BD342F38ACC585D447A4E67A046AA649?cnum=1)
[18] [Mediapart: Micron Taoyuan employees reject proposed bonus - Oct 23, 2026](https://app.bigdata.com/documents/7AB479D072552643CA88274D150DE7B4?cnum=3)
[19] [Caixin Global: Micron Taiwan Workers Stage Strike - Oct 22, 2026](https://app.bigdata.com/documents/80869F41EA33E5705DA8BB778F7C303B?cnum=3)
[20] [KB Securities: Global Tracker+ - Oct 22, 2026](https://app.bigdata.com/documents/7FB124856440458095446F40BBF78484?cnum=26)
[21] [Micron Technology Form 10-K for FY2026 - Oct 9, 2026](https://app.bigdata.com/documents/01257A3C9BB0BBF855F808C2AC59655C?cnum=178&cnum=161)
[22] [Yahoo! Finance: Why Micron Stock Dropped on Thursday - Oct 22, 2026](https://app.bigdata.com/documents/D1A6A1B393726E8A19F49D581A4451B2?cnum=1)
[23] [Financial News: Will SK hynix's Q3 operating profit exceed 80 trillion won - Oct 17, 2026](https://app.bigdata.com/documents/BE692AC2EAF50B51DDA7D6ACBE55B80A?cnum=2)
[24] [Benzinga: Korea's Chip Selloff Flashes Capitulation Signal Ahead of SK Hynix Earnings - Oct 23, 2026](https://app.bigdata.com/documents/C4AA436933AA2DC90EFF5F3B6798C166?cnum=5)
[27] [Equisights: Micron Technology initiation of coverage - Oct 5, 2026](https://app.bigdata.com/documents/ACF3FF2734A0328BCA911CF74210E22E)

The numbers skip [11], [25] and [26]: those documents were read but not cited in the final text.

Data: Bigdata.com company tearsheet for Micron (FactSet fundamentals and consensus estimates, FMP analyst data and latest earnings), Bigdata.com sentiment tearsheet (90 days) and corporate calendar, all retrieved 23 Oct 2026. Base rates are from the skill's method files (top 1,000 global companies, 1950-2015, inflation-adjusted; one-day price-move studies, 1990-2015).

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

---

I can set up a Bigdata.com monitor that flags Micron news until the 16 Dec report, or save this note to your Bigdata.com account so later searches can find it. Say which, if either.
