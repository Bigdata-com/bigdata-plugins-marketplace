# dd-asml#1

USER: Give me a deep dive on ASML

  [tool call] Skill {"skill": "bigdata-com:bigdata-deep-dive", "args": "ASML"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && ls && wc -l *.md && cat working-with-bigdata.md output-standard.md", "description": "List skill references and read dat

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_fetch_document,mcp__claude_ai_Bigdata_com__bigdata_screen_companies,mcp__claude_ai_Bigdata_com__bigdata_e

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "ASML", "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && cat roic.md industry-structure.md earnings-quality.md capital-allocation.md", "description": "Read ROIC, industry, earn

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["company_overview", "c_level_leadership", "analyst_ratings"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["latest_earnings", "earnings_calendar", "key_metrics", "financial_ratios"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["financial_statements"], "interval": "annual", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["analyst_estimates"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["revenue_segmentation", "mergers_acquisitions"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["fund_trends_history", "hiring_trends", "dividends"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "cd /Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-wj89x5e4/00458c96-497c-463b-b526-e77539db7d39/tool-results/\nF=mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792585507.txt\njq -c '.estimates | {source,periodicity,cu

  [tool call] Bash {"command": "cd /Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-wj89x5e4/00458c96-497c-463b-b526-e77539db7d39/tool-results/\nF=mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792585507.txt\njq -r '.estimates.records[] | \"\\(.fiscal

  [tool call] Bash {"command": "cd /Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-wj89x5e4/00458c96-497c-463b-b526-e77539db7d39/tool-results/\nF=mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792585507.txt\njq -r '.estimates.records[] | select(.fisc

  [tool call] Bash {"command": "cd /Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-wj89x5e4/00458c96-497c-463b-b526-e77539db7d39/tool-results/\nF=mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792585729.txt\njq -c '.dividends[:8]' $F | head -c 2000; 

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Holding Q3 2026 earnings call: guidance for Q4 2026 and outlook for 2027 revenue and gross margin", "max_chunks": 25}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Holding Q2 2026 earnings call: management commentary on bookings, AI demand and full-year 2026 guidance", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Holding Q1 2026 earnings call: guidance and comments on China sales and EUV demand", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did ASML shares fall this week?", "max_chunks": 15}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML annual report 2025 risk factors: export controls, customer concentration and supplier dependence on Carl Zeiss", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Q3 2026 other income or one-off gain, including any revaluation of its Mistral AI stake", "max_chunks": 15}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "outlook for 2027 sales growth, EUV capacity and customer demand beyond supply", "filters": {"document_type": {"mode": "INCLUDE", "values": [{"type": "TRANSCRIPT", "subtypes": ["EARNINGS_CALL"]}]}, "reporting_entities": ["AFCFF2"], "reporting_per

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Q4 2025 earnings call January 2026: 2026 guidance, order bookings and the new 2026-2028 share buyback programme size", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "risk factors customer concentration largest customer share of total net sales 2025 China share", "filters": {"document_type": {"mode": "INCLUDE", "values": [{"type": "FILING", "subtypes": ["SEC_20_F"]}]}, "reporting_entities": ["AFCFF2"], "times

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Chinese domestic lithography competition to ASML: SMEE, Shanghai Aishengna immersion DUV, Huawei EUV efforts in 2026", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Export control changes affecting ASML sales and servicing in China during 2026", "max_chunks": 15}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML High-NA EUV adoption by TSMC, Samsung, SK Hynix and Intel and timing of high-volume manufacturing insertion", "max_chunks": 15}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "AMAT", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "LRCX", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "KLAC", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "Tokyo Electron", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "remuneration policy Board of Management performance measures long-term incentive ROAIC TSR", "filters": {"reporting_entities": ["AFCFF2"], "timestamp": {"start": "2026-01-15T00:00:00Z", "end": "2026-04-30T23:59:59Z"}, "category": {"mode": "INCLU

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML investment in Mistral AI: amount, stake size and accounting", "max_chunks": 10}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "A4BCDE", "company_type": "Public", "sections": ["key_metrics", "financial_ratios"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "0B57D7", "company_type": "Public", "sections": ["key_metrics", "financial_ratios"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "507AE7", "company_type": "Public", "sections": ["key_metrics", "financial_ratios"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "61DE17", "company_type": "Public", "sections": ["key_metrics", "financial_ratios"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Broker research on ASML after Q3 2026 results: price target changes, 2027 and 2028 earnings estimates and key debates", "max_chunks": 20}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && grep -n -i -A3 \"semicon\\|cyclical\" sector-primers.md | head -80; echo ----; grep -n -i \"sales growth\\|consensus gr

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && sed -n 60,96p base-rates.md; sed -n 150,195p base-rates.md; sed -n 170,186p sector-primers.md", "description": "Read sa

  [tool call] Bash {"command": "mkdir -p /tmp/asml_calc && cat > /tmp/asml_calc/calc.py <<'EOF'\n# ASML deep dive arithmetic; inputs from Bigdata.com tearsheet (FactSet), EUR bn\nyrs=[2021,2022,2023,2024,2025]\nrev=[18.611,21.1734,27.5585,28.2629,32.6673]\nebit=[6.5364,6.5007,9.0423,9.0226,11.3014]\npti=[6.7055,6.4561

  [tool call] Bash {"command": "cat > /tmp/asml_calc/dcf.py <<'EOF'\n# Three-case DCF, EUR bn; valuation at end-2026 discounted ~0.2y back is ignored (approximation)\nSH=0.383; NETCASH=10.8; MISTRAL=1.8; TAX=0.17\ndef run(sales, margins, wacc, g_term, ronic_term, ic_per_sales=0.25, s2026=44.5):\n    pv=0; prev=s2026; 

  [tool call] Bash {"command": "cat >> /tmp/asml_calc/dcf.py <<'EOF'\nprint(\"\\n--- 15-year explicit horizon (2027-2041), terminal RONIC 20% judgment ---\")\ndef extend(s,m,g,n=5):\n    s=list(s); m=list(m)\n    for _ in range(n): s.append(s[-1]*(1+g)); m.append(m[-1])\n    return s,m\next={'base':extend(*cases['base

  [tool call] Bash {"command": "cat >> /tmp/asml_calc/dcf.py <<'EOF'\nprint(\"\\n--- consensus path: 2027 58.5, 2028 73 (3Q annualised), then +8%/yr to 2032, +5% to 2041; margin 45% ---\")\ns=[58.5,73.0]; \nfor _ in range(4): s.append(s[-1]*1.08)\nfor _ in range(9): s.append(s[-1]*1.05)\nm=[0.443,0.45]+[0.45]*13\nfor 

ASSISTANT: I have the data I need. Now I'm running the return-on-capital, earnings-quality and valuation arithmetic (three cases with a discount-rate sensitivity).

# ASML Holding (ASML): deep dive, 23 October 2026

Data as of: price 22 Oct 2026 (Nasdaq close $1,589.60); consensus estimates retrieved 23 Oct 2026 (FactSet, quarterly records); statements FY2021 to FY2025 annual and Q3 2026 quarterly; newest document 23 Oct 2026.

## What the evidence shows

ASML is the only supplier of EUV lithography tools, the machines needed for the most advanced logic and DRAM chips. It also sells DUV (deep ultraviolet) scanners, metrology tools, and service and upgrades to a growing installed base. 2026 sales are guided to €44-45bn with a gross margin of about 56% [1]. That is 36% growth, and it already reaches the bottom of the 2030 targets the company set in 2024 (€44-60bn sales, 56-60% gross margin) [2].

The economics are very strong and partly financed by customers. Prepayments (contract liabilities) of €16.0bn at end-2025 exceed the company's operating capital excluding goodwill. ROIC before that customer funding was 42% in 2025 (derived). Reported earnings are mostly clean. The exceptions are a €0.5bn revaluation gain on the Mistral AI stake in Q3 2026 net income [1], and a margin mix that leans on high-margin installed-base upgrades.

Over 2021-2025, management returned €31.9bn through buybacks and dividends, about 109% of FactSet free cash flow, and cut the average share count by about 6.5%. The one non-core deal is €1.3bn for 11% of Mistral AI [3].

At about €1,472 per share (derived), the price matches the consensus path: about €73bn of sales in 2028, then steady growth at a 45% operating margin and no cyclical downturn for 15 years, discounted at 8.5-9%. My three cases give €702 to €1,514 per share, with a probability-weighted value of about €1,082 (derived). That is roughly a quarter below the current price.

The main risk is the semiconductor equipment cycle, with China export rules second. The next dated test is the Q4 2026 report with 2027 guidance in late January 2027.

## The business

ASML sells three things:
- **EUV systems**: Low-NA tools at roughly $200m and High-NA tools at roughly $400m [4].
- **Non-EUV systems**: DUV immersion and dry scanners, plus metrology and inspection.
- **Installed Base Management**: service, upgrades and spare parts. This part is growing fastest because customers buy throughput upgrades to get capacity before new fabs are ready [1].

**2026 mix and units**

| Item | 2026 figure | Basis | Source |
|---|---|---|---|
| Total net sales guide | €44-45bn, about +36% | reported | [1] |
| EUV sales growth | over +45% | reported | [1] |
| Non-EUV system sales growth | about +20% | reported | [1] |
| Installed Base sales growth | about +50% | reported | [1] |
| Logic / Memory system sales growth | about +10% / about +75% | reported | [1] |
| Q3 2026 system sales: EUV / non-EUV | €4.1bn / €4.3bn; Logic 54%, Memory 46% | reported | [1] |
| Low-NA EUV units | 44 (2025), about 65 (2026), +30% capacity in 2027, more than +30% under study for 2028 | reported | [1] |
| China share of sales | about 20% (2026 guide); about 16% in H1 2026 | reported | [1], [5] |

**Geography (customer location)**

| Region | 2024 | 2025 | Basis | Source |
|---|---|---|---|---|
| China | 36.1% | 29.1% | reported | [6] |
| Taiwan | 15.4% | 25.5% | reported | [7] |
| South Korea | 22.7% | 25.0% | reported | [7] |

**Five-year trend (FactSet, EUR bn)**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Basis | Source |
|---|---|---|---|---|---|---|---|
| Revenue | 18.61 | 21.17 | 27.56 | 28.26 | 32.67 | reported | Data |
| Gross margin | 51.9% | 49.5% | 50.2% | 49.8% | 51.6% | derived | Data |
| EBIT margin | 35.1% | 30.7% | 32.8% | 31.9% | 34.6% | derived | Data |
| Net income | 5.88 | 5.62 | 7.84 | 7.57 | 9.61 | reported | Data |
| Free cash flow (FactSet definition) | 8.58 | 4.65 | 0.94 | 6.65 | 8.53 | reported | Data |
| EPS (€) | 14.36 | 14.14 | 19.91 | 19.25 | 24.73 | reported | Data |

FactSet's gross margin for 2025 (51.6%) is below the company's 52.8% [8] because FactSet classifies costs differently.

Over five years, profit has moved toward EUV and the installed base. The company's 2026 outlook attributes the margin rise to EUV volume, immersion volume and upgrades [1]. The tearsheet's segment table was empty, so a five-year segment-margin series is not available (see Gaps).

## Economics

ROIC is shown on two bases. The FactSet field is given separately and not mixed into the table.

| Year | Tax rate | NOPAT (€bn) | Operating capital incl. goodwill (€bn) | ROIC on it | Capital before customer prepayments (€bn) | ROIC on it | Basis |
|---|---|---|---|---|---|---|---|
| 2021 | 15.2% | 5.54 | 6.25 | 88.7%* | 14.18 | 39.1%* | derived |
| 2022 | 15.0% | 5.52 | 4.92 | 98.9% | 17.40 | 35.0% | derived |
| 2023 | 15.8% | 7.61 | 9.80 | 103.4% | 21.24 | 39.4% | derived |
| 2024 | 18.6% | 7.35 | 8.42 | 80.6% | 20.99 | 34.8% | derived |
| 2025 | 17.7% | 9.31 | 7.37 | 117.9% | 23.37 | 42.0% | derived |

*2021 uses end-year capital only, because the 2020 balance sheet is not in the data.

How the table is built:
- NOPAT is EBIT times (1 minus the effective tax rate).
- Operating capital is total assets minus cash, short-term investments and long-term investments, minus non-debt current liabilities and other non-current liabilities.
- "Before customer prepayments" adds back contract liabilities (€16.0bn in 2025).
- Returns use average capital.
- Excluding goodwill and intangibles, operating capital is negative in every year. Customers fund the working capital.

**Which ROIC this report quotes.** I quote the 42.0% figure (2025, capital before customer prepayments), because prepayments can reverse in a downturn. The FactSet ROIC field is 47.4% for FY2025 and 66.6% trailing at Q3 2026. It divides by debt plus equity (€24.3bn), which includes about €13bn of cash and leaves out the prepayments.

**Decomposition and incremental returns** (2025, prepayment-adjusted basis):
- ROIC of 42.0% = NOPAT margin 28.5% × capital turnover 1.47.
- Return on incremental capital: 41% for 2021→2025 and 63% for 2022→2025.
- Spread over an assumed 9% cost of capital: about 33 points.

## Industry structure and moat

| Item | Evidence | Basis | Source |
|---|---|---|---|
| Market position | Only producer of EUV tools. China is barred from EUV and some advanced DUV. | reported | [5] |
| Cost to enter | EUV took more than €6bn of R&D and over 17 years, and depends on Zeiss optics and imec research. | reported | [9] |
| Pricing power | Price increases on the most critical products were agreed with key customers. Some effect in 2027, full effect from 2028. About +10% on service parts to Korea. | reported | [1], [10] |
| Demand visibility | Customers see demand above their supply until at least 2028. Orders are arriving for 2028, and some customers want to order for 2029-2030. Orders come with significant prepayments. | reported | [11], [12] |
| Customer concentration | Largest customer 16.6% of 2024 sales (31.8% in 2023). Top two 30.5% in 2024. | reported | [13] |
| Supplier power | Single-source critical suppliers, including Zeiss for optics. ASML holds a minority stake in Carl Zeiss SMT ($1.11bn, 2016). | reported | [13], Data |
| China substitution | Shanghai Aishengna has started producing immersion DUV tools. SMEE plans 12 DUV tools by end-2026. JPMorgan says a handful of tools is not high-volume manufacturing. | reported | [5], [14] |
| Long-run challenge | Huawei/SiCarrier EUV light-source prototype at about 100-150W against ASML's 250W+. No working chip produced. | reported | [15] |
| Technology roadmap | High-NA in production at Intel. Samsung and SK Hynix plan production use in 2028, TSMC from 2030. Hyper-NA about 10 years out. Larger-mask production readiness by 2033. | reported | [4], [16], [17] |
| Competition in DUV (Nikon, Canon shares) | Not retrieved | gap | n/a |
| Duration of the advantage | EUV leadership through the early 2030s is supported by the High-NA and Hyper-NA roadmap. In DUV, the China share is the most exposed, from 2027-2030. | judgment | n/a |

Base rates set the bounds on persistence. In information technology, operating margins have a 5-year persistence correlation of 0.62 and CFROI (cash flow return on investment) a 4-year correlation of 0.50. Both are among the fastest-fading sectors (top 1,000 global companies 1950-2015, and HOLT global sample 1983-2015; not current facts).

ASML's EUV position is an outlier within that class. I therefore use a 15-year competitive advantage period (judgment), not the sector default.

## Earnings quality

| Measure | 2021 | 2022 | 2023 | 2024 | 2025 | Basis |
|---|---|---|---|---|---|---|
| Accruals: (net income minus operating cash flow) / average assets | -16.4% | -8.6% | +6.3% | -8.1% | -6.2% | derived |
| FactSet FCF / net income | 1.46 | 0.83 | 0.12 | 0.88 | 0.89 | derived |
| Change in contract liabilities (€bn) | n/a | +4.55 | -1.04 | +1.13 | +3.44 | derived |
| Stock compensation / EBIT | 1.8% | 1.1% | 1.5% | 1.9% | 1.8% | derived |
| Capex / D&A | 2.0 | 2.3 | 3.0 | 2.3 | 1.6 | derived |

**Operating profit rebuild (EBITA, € bn)**

| Item | FY2025 | Trailing 12 months to Q3 2026 | Basis |
|---|---|---|---|
| Reported EBIT | 11.30 | 15.21 | reported / derived from quarterly margins |
| + Amortization of acquired intangibles | 0.12 | about 0.12 | reported |
| + Q2 2026 IT transformation charge (once in five years) | 0 | about 0.1 (R&D €1.3bn against about €1.2bn run-rate) | derived [18] |
| Rebuilt EBITA | 11.42 | about 15.4 | derived |
| Below EBIT: Mistral AI revaluation gain (once in five years) | 0 | about 0.5 | reported [1] |

**Flags**

| Flag | Severity | Basis | Source |
|---|---|---|---|
| Q3 2026 net income includes about €0.5bn Mistral revaluation (about €1.3 per share) | Low (disclosed) | reported | [1], [19] |
| Margin outperformance came from about €0.4bn of extra high-margin upgrades in Q3 2026. Mirae calls the operating improvement "limited". | Medium | reported | [1], [19] |
| Cash flow follows customer prepayments: Q3 2026 FCF was €11.4bn, 2023 FCF was €0.94bn | Medium (timing) | reported | [1], Data |
| Inventory rose 115% (2021-2025) against revenue +76%. Cash conversion cycle 292 days at FY2025. | Medium (ramp) | derived | Data |
| Goodwill €4.59bn unchanged 2023-2025, no impairment | Low | reported | Data |

Piotroski F-score is 9 (Q3 2026) and Altman Z is 14.6 (Q2 2026), both as reported by FactSet.

## Capital allocation

**Sources and uses, 2021-2025 cumulative (€bn)**

| Item | Amount | Basis |
|---|---|---|
| Operating cash flow | 48.6 | reported |
| Capex | -8.2 | reported |
| Buybacks | -20.7 | reported |
| Dividends | -11.3 | reported |
| Mistral AI stake (2025) | -1.3 | reported [3] |
| Net debt change | -0.1 | reported |
| Increase in cash and short-term investments | +5.7 | reported |

**Buybacks.** For 2022-2025, €12.1bn of buybacks reduced the average share count by 21.3m net of issuance (397.7m in 2022 to 388.5m in 2025, from 409.8m in 2021). That implies about €568 per share retired (derived; weighted share counts lag, so this is approximate). Against today's €1,472, that is 2.6 times, or about 33% a year from mid-2023, before dividends. That is well above an assumed 9% cost of equity.

The 2021 programme (€8.6bn) is excluded because the 2020 share count is not in the data. A new programme of up to €12bn runs to end-2028 [8], and €4.1bn was bought in Q3 2026 alone [1].

**Dividend.** €7.50 for 2025, up 17% [8]. Quarterly interims of €1.88 in 2026 [1].

**Deals**

| Deal | Year | Value | Basis | Source |
|---|---|---|---|---|
| Carl Zeiss SMT minority stake | 2016 | $1.11bn | reported | Data |
| Mapper Lithography | 2019 | undisclosed | reported | Data |
| Berliner Glas (parts) | 2020-21 | $348m disclosed | reported | Data |
| Mistral AI, about 11% stake | 2025 | €1.3bn; revalued up about €0.5bn in Q3 2026 | reported | [3], [1] |

No synergy targets were disclosed, so a premium-versus-synergy test is not possible.

**Leverage.** Net cash of about €10.8bn (derived from the FactSet net debt/EBITDA ratio of -0.66). Debt/EBITDA is 0.12. Rating medians are not in the data.

**Management pay.** The 2026-2028 long-term incentive (LTI) plan weights:
- relative TSR against the Philadelphia Semiconductor Index: 25%
- ROAIC (return on average invested capital): 35%, with threshold 45%, target 55%, stretch 65%
- Technology Leadership Index: 20%
- ESG measures: 20%

These targets were set when the 2026 guide was €34-39bn. ROAIC subtracts current liabilities and non-current contract liabilities from capital, so customer prepayments raise it. FactSet's ROIC field is already 66.6% (a different definition, so it does not settle whether the ROAIC stretch is met). The 2023-2025 plan vested at 137.4% of target [20].

## What the price implies

Assumptions: 9% cost of capital (assumed: euro equity with beta above 1), 17% tax rate (company guide [1]), 383m shares (derived from Q3 2026 net income/EPS), net cash €10.8bn plus Mistral stake about €1.8bn.

- **Steady state.** 2027 consensus EBIT is €25.9bn (sum of quarterly means). After tax that is €21.5bn of NOPAT, worth €239bn at 9% with no growth, or about €652 per share. That is 43% of enterprise value (about €551bn). The other 57% is paid for future value creation.
- **Implied growth and duration.** The price requires about 13 years of 12% annual NOPAT growth after 2027 at a 40% return on new capital, or 10 years at 15% (derived).
- **Warranted multiple compared with actual.** A warranted EV/NOPAT of 14.2x (3% growth, 20% return on new capital) to 17.3x (4%, 30%) compares with an actual 25.6x on 2027 NOPAT. P/E is 25.2x on 2027 consensus EPS of €58.4, and 35.9x on 2026 EPS excluding the Mistral gain.
- **Base rate.** Consensus implies 2025-2028 sales growth of about 30% a year (€32.7bn to about €73bn, with 2028 annualized from three quarters). Among companies with more than $25bn of sales, 4.6% achieved 3-year real growth of 20% or more, and 37.0% had negative 3-year real growth (top 1,000 global companies, 1950-2015, inflation-adjusted; not a current fact). 2026's 36% is already largely in hand. 2027 and 2028 are the part that stands against the base rate.

## Valuation

**Forecast and cases (15 explicit years, 2027-2041; 25% of incremental sales reinvested; 3% terminal growth; 20% terminal return on new capital, judgment)**

| Case | Path | Value per share | Probability | Basis |
|---|---|---|---|---|
| Bear | 2027 €55bn, then a memory/AI capex correction with 2028 sales of €46bn at a 34% EBIT margin. China DUV share lost. 38% mid-cycle margin. | €702 | 25% | assumed |
| Base | 2027 €58bn, 2028 €68bn at 46% margin (pricing). One mid-cycle dip around 2030. Then 5% growth at 42%. | €1,056 | 50% | assumed |
| Bull | Consensus-plus, no downturn: €74bn in 2028, €92bn in 2030, 46-49% margin | €1,514 | 25% | assumed |
| Probability-weighted value | | about €1,082 | | derived |

The weights are judgment. Order coverage for 2027, backed by prepayments [12], argues against a 2027 collapse. The base rate above and the 2023-2024 flat year in the statements argue against assuming no downturn.

**Equity bridge, base case (€bn):** present value of explicit cash flows 226.1 + present value of continuing value 165.8 = enterprise value 391.8; + net cash 10.8 + Mistral stake 1.8 = equity 404.4; divided by 0.383bn shares = €1,056.

**Terminal checks.** Continuing value is 42% of enterprise value. The implied terminal EV/EBIT is 12.1x. Setting the terminal return on new capital equal to the cost of capital lowers the base case to €963.

**Base case per share: cost of capital (rows) × terminal growth (columns)**

| | 2.0% | 2.5% | 3.0% | 3.5% |
|---|---|---|---|---|
| 8.0% | 1,185 | 1,220 | 1,261 | 1,310 |
| 8.5% | 1,092 | 1,118 | 1,149 | 1,186 |
| 9.0% | 1,012 | 1,032 | 1,056 | 1,084 |
| 9.5% | 943 | 959 | 977 | 998 |
| 10.0% | 883 | 895 | 909 | 926 |

The consensus path (2027 €58.5bn, 2028 €73bn, then 8% and later 5% growth at a 45% margin) is worth €1,372 at 9% and €1,654 at 8%. The current price sits between the two.

**Comparable companies (trailing multiples at each company's latest period-end price; dates differ)**

| Company | Period end | P/E | EV/EBIT | Gross margin | Op. margin | FactSet ROIC | Basis | Source |
|---|---|---|---|---|---|---|---|---|
| ASML | 30 Sep 2026 | 43.5 | 37.7 | 57.4% | 44.4% | 66.6% | reported | Data |
| Applied Materials | 31 Jul 2026 | 46.2 | 44.5 | 50.3% | 33.7% | 32.4% | reported | Data |
| Lam Research | 30 Sep 2026 | 46.9 | 40.6 | 52.3% | 40.0% | 59.7% | reported | Data |
| KLA | 30 Jun 2026 | 82.3 | 70.3 | 62.0% | 43.4% | 48.6% | reported | Data |
| Tokyo Electron | 30 Jun 2026 | 56.8 | 50.4 | 46.8% | 28.9% | 33.6% | reported | Data |

ASML has the lowest trailing EV/EBIT in the group and the highest operating margin. KB Securities puts ASML's forward PEG at 0.7x, against 0.7x for Lam and 0.6x for Applied [19]. Rothschild & Co Redburn shows ASML's forward EV/EBIT premium over peers moving to a discount in 2024 [21].

The comparison does not suggest ASML is expensive relative to peers. The whole group is priced for the AI capex cycle to continue.

**Range:** €702-1,514 per share, with a probability-weighted value of about €1,082, against a current price of about €1,472 (derived).

## Risks and kill criteria

| Rank | Risk | Probability / size | Early signal | Basis | Source |
|---|---|---|---|---|---|
| 1 | Equipment cycle: AI or memory capex slows after the 2026-2028 build | Medium / large: bear case €702 | Customer capex cuts; memory prices; contract liabilities falling quarter on quarter | judgment | [22], [23] |
| 2 | US MATCH Act bars DUV sales and servicing in China | Medium / about 15-20% of sales plus high-margin service | Bill progress; Dutch alignment | reported | [24], [25] |
| 3 | Ramp execution: supply chain (Zeiss) and ramp costs reduce margins | Medium / medium | Q4 2026 gross margin guided down to about 57% from 57.5% on ramp costs | reported | [1] |
| 4 | Chinese DUV substitution in the China market | Low near term / medium by 2028-2030 | SMIC qualifying domestic tools | reported | [5], [14] |
| 5 | Lower valuation multiple across semicap even as estimates rise | High / medium | Sector multiples contracted in October 2026 | reported | [26] |
| 6 | Taiwan or Korea geopolitical disruption | Low / very large | n/a | reported | [7] |

**Downside markers.** The no-growth steady-state value is about €652 per share (derived). The bear case is €702. Net cash is small relative to the company's value, and part of it is customer prepayments that would reverse in a downturn.

**Kill criteria (each breaks the base case):**
1. 2027 sales guidance below about €55bn, or 2027 gross margin guidance below 55%, at the Q4 2026 report (late January 2027).
2. Contract liabilities fall for two consecutive quarters during 2027.
3. MATCH Act enacted with servicing restrictions.
4. Capital Markets Day (10 June 2027) 2030 targets below about €75bn of sales.

## Catalysts and what to watch

| Date or window | Event | Mechanism | Direction / size | Certainty | Basis | Source |
|---|---|---|---|---|---|---|
| 4 Nov 2026 | €1.88 interim dividend paid | Cash return | Small | Set | reported | [1] |
| Late Jan 2027 (LBBW lists 27 Jan; the Quartr calendar lists 24 Feb) | Q4 2026 results, 2027 guidance and gross margin | Confirms or cuts the 2027-2028 path | Large, either way | Date to verify | reported | [27], Data |
| Early 2027 | First NXE:3800F shipments (260 wafers/hour) | Mix and ASP | Positive, small | Planned | reported | [28] |
| Mid-April 2027 (window) | Q1 2027 results | Ramp costs against pricing | Medium | Expected | judgment | n/a |
| 10 Jun 2027 | Capital Markets Day: new long-term targets | Resets the 2030 range | Large | Set | reported | [29] |
| Undated | US MATCH Act progress | China access | Negative, medium to large | Uncertain | reported | [24] |
| 2028 | Samsung and SK Hynix High-NA production | High-NA volume | Positive, medium | Planned | reported | [4] |

**Five metrics to track:**
1. Low-NA EUV units against about 65 (2026) and about 85 (2027 plan).
2. Installed Base sales against €3.7bn (Q4 guide) and the upgrade share.
3. Contract liabilities and down payments.
4. China share of sales against about 20%.
5. Gross margin against about 56% (2026) and the 56-60% 2030 range.

## What would change this view

1. The 2027 guide (late January 2027) at or above €60bn with a gross margin of 58% or more would move the base case toward the consensus path (€1,372 at 9%).
2. ASML disclosing 2028 order coverage above the 110-unit capacity scenario [12] would lower the bear-case weight.
3. Contract liabilities falling for two consecutive quarters would raise the bear-case weight.
4. MATCH Act passage including servicing would take about a fifth of revenue out of every case.
5. 2030 targets above €90bn at the 10 June 2027 Capital Markets Day would support the bull path.

## Gaps

- Statements cover five fiscal years (2021-2025), not ten. The tearsheet has no period offset.
- Revenue segmentation in the tearsheet was empty, so segment figures come from earnings calls.
- Not in Bigdata.com and treated as assumptions: cost of capital, credit ratings, Nikon and Canon market shares, Cymer and HMI deal terms, and buyback prices paid.
- The tearsheet market cap ($547bn) conflicts with the share count implied by Q3 2026 net income/EPS. I used 383m shares.
- The euro price uses EUR/USD 1.08, derived from same-day quotes on 14 Oct ($1,650.00 in New York [30] and €1,528.20 in Amsterdam [27]).

## Sources

[1] [ASML Q3 2026 Earnings Call - Oct 14, 2026 (S&P Global)](https://app.bigdata.com/documents/DCD3DA8A66FF90AAD5397279C492EF0C)
[2] [ASML Q4 2025 Earnings Call - Jan 28, 2026 (S&P Global)](https://app.bigdata.com/documents/C44D06834C39C22B0CCCC46A254899CB?cnum=3&cnum=6&cnum=7&cnum=8)
[3] [ASML invests EUR1.3 billion in Mistral for 11% stake - Alliance News, Sep 9, 2025](https://app.bigdata.com/documents/696DC97C0D6A52A78CC80095F441CFC0?cnum=1)
[4] [Analysis - ASML extends chipmaking dominance as customers embrace High NA - AOL, Sep 14, 2026](https://app.bigdata.com/documents/EDCC21DB8D35B200EB3660678C86B0DC?cnum=2)
[5] [China starts production of home-grown immersion DUV tools - Straits Times, Jul 29, 2026](https://app.bigdata.com/documents/D01DAB5BE0FAB4CBCE010F6FFE1BFF21?cnum=5)
[6] [ASML Form 6-K (Annual Report 2025) - Feb 25, 2026](https://app.bigdata.com/documents/3BDC142E085B1B7833C5553013E3B1A0?cnum=138&cnum=137)
[7] [ASML Q4 2025 Report (risk factors) - Quartr, Jan 28, 2026](https://app.bigdata.com/documents/4CEC1CB6578581E66EF103ADF556A7E1?cnum=230)
[8] [ASML Q4 2025 Earnings Call - Jan 28, 2026 (S&P Global)](https://app.bigdata.com/documents/B48FA475E9F6951870D39974676736A1?cnum=6&cnum=7&cnum=9&cnum=10)
[9] [Taking Stock of China's EUV Lithography Efforts - Power Electronics News, Feb 17, 2026](https://app.bigdata.com/documents/C156FE77C01D9ECF31E9C0BD9D2749BF?cnum=5)
[10] [ASML - Two-way growth through capacity expansion and price increases - Eugene Investment & Securities, Oct 17, 2026](https://app.bigdata.com/documents/F7F476E5F274DE4FC655BB48D593DFF1?cnum=4)
[11] [ASML Q3 2026 Earnings Call - Oct 14, 2026 (S&P Global, Q&A)](https://app.bigdata.com/documents/F0D8A94B710916632FADB086B5606949?cnum=3&cnum=4)
[12] [ASML Q2 2026 Earnings Call - Jul 15, 2026 (FactSet)](https://app.bigdata.com/documents/749F673802981A6B67BC7FE6AC513813)
[13] [ASML Form 20-F FY2024 - Mar 5, 2025](https://app.bigdata.com/documents/F44BC5F8ED34CFA28D8DDC5F3A1B602B)
[14] [Huawei Leads China's Semiconductor Self-Sufficiency Drive - Financial News, Sep 8, 2026](https://app.bigdata.com/documents/406519080E132A39467B642E0E3118B4?cnum=3)
[15] [ASML as the last polite monopolist - Asia Times, Apr 28, 2026](https://app.bigdata.com/documents/1624731A42BFB5E7401AB5E8DCF311D8?cnum=15)
[16] [ASML, Zeiss: Next-generation chip manufacturing technology within about 10 years - Anue, Oct 10, 2026](https://app.bigdata.com/documents/6692DB2B58A3BBE1F8F2832CA7A23ABB?cnum=2)
[17] [ASML and Chip Giants like TSMC Plot a Bigger Canvas - Yahoo! Finance, Sep 20, 2026](https://app.bigdata.com/documents/71C05A896F1FAA61028C7D450EC821ED?cnum=1)
[18] [ASML Q2 2026 Earnings Call - Jul 15, 2026 (Quartr)](https://app.bigdata.com/documents/DE59CECAAB440528DA38FA60FDA1F7C9)
[19] [ASML Holding - Even capacity expansion cannot keep up with demand - KB Securities, Oct 17, 2026](https://app.bigdata.com/documents/2162CA8A058ED7A6DEB3A74EDD8DA561?cnum=8)
[20] [ASML Form 6-K (Remuneration report) - Feb 25, 2026](https://app.bigdata.com/documents/3BDC142E085B1B7833C5553013E3B1A0?cnum=298&cnum=291&cnum=787&cnum=294)
[21] [New Zealand Weekly (Rothschild & Co Redburn chart) - Auerbach Grayson, Oct 19, 2026](https://app.bigdata.com/documents/6C52ABD4F09AEBE1539428137576EAFF?cnum=25)
[22] [Lam Research Sinks 9% as Supply Constraints Cap Outlook - AOL, Oct 22, 2026](https://app.bigdata.com/documents/BD7F34559BE7A8D0A7AB86EE0D37584B?cnum=2)
[23] [The Earnings Twist In The AI Chip Bubble Debate - Benzinga, Oct 21, 2026](https://app.bigdata.com/documents/941BF0686C48BA715E0C476C8142472D?cnum=5)
[24] [ASML Q2 2026: Sales Growth Flatten, China Concerns Remain - Leverage Shares, Jul 17, 2026](https://app.bigdata.com/documents/17B2337BC603940CDFBD82026AFFD882?cnum=3)
[25] [ASML's Chip Dominance Runs Into New Silicon Boundaries - Nasdaq, Jun 25, 2026](https://app.bigdata.com/documents/12C2E9835A98DFBF683AEC7843D2E3B4?cnum=3)
[26] [Global Insights - KB Securities, Oct 23, 2026](https://app.bigdata.com/documents/985C2FFCC0C0A68395F2B7EAC0372CEC?cnum=7)
[27] [ASML Holding Stock Compact: AI Boom Leads to Higher Annual Targets Again - LBBW, Oct 15, 2026](https://app.bigdata.com/documents/2D1279EE25101B4F736E11DD909E9C94?cnum=7&cnum=1&cnum=2)
[28] [ASML Q3 2026 Earnings Call - Oct 14, 2026 (Quartr)](https://app.bigdata.com/documents/DAEADC8248E76E72980C5DE74063BE56)
[29] [ASML Q2 2026 Earnings Call - Jul 15, 2026 (Quartr, prepared remarks)](https://app.bigdata.com/documents/DE59CECAAB440528DA38FA60FDA1F7C9)
[30] [International Stock Market Flash - ASML - Yuanta, Oct 15, 2026](https://app.bigdata.com/documents/1E6CCEB3CC416A85BD9D5F0A90EC42D8?cnum=1)

Data: Bigdata.com company tearsheets for ASML, Applied Materials, Lam Research, KLA and Tokyo Electron (FactSet fundamentals, ratios and consensus estimates; FMP price targets and ratings; fund holdings; LinkUp hiring), retrieved 23 Oct 2026. Derived figures (ROIC, accruals, DCF, reverse DCF, sensitivities) were computed from those fields with the formulas stated under each table.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

---

If you want, I can save this report to your Bigdata.com account so later searches can find it, or turn it into a Word document.
