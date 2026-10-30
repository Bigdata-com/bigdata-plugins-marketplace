# dd-asml#1

USER: Give me a deep dive on ASML

  [tool call] Skill {"skill": "bigdata-com:bigdata-deep-dive", "args": "ASML"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive && ls references/ && cat references/working-with-bigdata.md references/output-standard.md", "description": "List skill references and

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_fetch_document,mcp__claude_ai_Bigdata_com__bigdata_screen_companies", "max_results": 5}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "ASML", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["company_overview", "c_level_leadership", "analyst_ratings"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["latest_earnings", "earnings_calendar", "financial_ratios", "key_metrics"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["financial_statements"], "interval": "annual", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["analyst_estimates", "revenue_segmentation"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "AFCFF2", "company_type": "Public", "sections": ["fund_trends_history", "mergers_acquisitions", "hiring_trends", "dividends"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "D=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results\nF=$D/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791813823.txt\njq -c '.revenue_segmentation.source, (.re

  [tool call] Bash {"command": "D=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results\nF=$D/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791813823.txt\njq -r '.estimates.records|map(.metric)|un

  [tool call] Bash {"command": "D=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results\nF=$D/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791814379.txt\njq -c '.mergers_acquisitions.summary_stat

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "guidance for next quarter and full year, net bookings, EUV demand", "filters": {"reporting_entities": ["AFCFF2"], "reporting_periods": [{"fiscal_year": 2026, "fiscal_quarter": 3}], "document_type": {"mode": "INCLUDE", "values": [{"type": "TRANSC

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "outlook guidance, 2027 growth, China revenue, High-NA EUV adoption", "filters": {"reporting_entities": ["AFCFF2"], "reporting_periods": [{"fiscal_year": 2026, "fiscal_quarter": 2}], "document_type": {"mode": "INCLUDE", "values": [{"type": "TRANS

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "full-year 2026 guidance revenue gross margin, 2030 targets, capital return buyback", "filters": {"reporting_entities": ["AFCFF2"], "reporting_periods": [{"fiscal_year": 2025, "fiscal_quarter": 4}], "document_type": {"mode": "INCLUDE", "values": 

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Holding Q3 2026 earnings call October 2026 guidance and bookings"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML Holding Q4 2025 earnings call January 2026 full-year 2026 guidance"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_fetch_document {"id": "749F673802981A6B67BC7FE6AC513813", "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results/toolu_01DCHB7YNu87JAz4vNmM2z6R.txt\njq -r '.text' $F | grep -iE \"booking|backlog|2027|guid|gross margin|China|High.NA

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_fetch_document {"id": "DAEADC8248E76E72980C5DE74063BE56", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did ASML shares fall around October 21 2026?"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML 2025 annual report risk factors: customer concentration, export controls, Carl Zeiss single supplier"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Chinese domestic lithography competition to ASML, SMEE, SiCarrier, Huawei EUV prototype progress in 2026"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "US and Dutch export restrictions on ASML DUV immersion sales and servicing in China, 2026 developments"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Analyst research notes on ASML after Q3 2026 results: price target changes and 2027 2028 estimates"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Lithography equipment market share ASML versus Canon and Nikon, nanoimprint lithography alternative"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "AMAT", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "LRCX", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "KLAC", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "Tokyo Electron", "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML 2025 annual report remuneration policy for Board of Management: performance metrics for short-term and long-term incentives"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "ASML investment in Mistral AI: amount invested, stake size and accounting treatment"}}, "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "A4BCDE", "company_type": "Public", "sections": ["key_metrics", "financial_ratios", "analyst_estimates"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "0B57D7", "company_type": "Public", "sections": ["key_metrics", "financial_ratios", "analyst_estimates"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "507AE7", "company_type": "Public", "sections": ["key_metrics", "financial_ratios", "analyst_estimates"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "61DE17", "company_type": "Public", "sections": ["key_metrics", "financial_ratios", "analyst_estimates"], "plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "D=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results\nfor n in AMAT:1792791895632 LRCX:1792791897564 KLAC:1792791898056 TEL:1792791898914; do\n t=${n%%:*}; f=$D/mcp-claude

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet", "max_results": 1}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet {"plugin_slug": "bigdata-deep-dive"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && wc -l *.md && grep -n -i -A25 \"semicond\\|cyclical\" sector-primers.md | head -90 && grep -n -i -B2 -A12 \"cyclical\" 

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-deep-dive/references && sed -n 86,96p base-rates.md && grep -n -A12 \"Table 12\" base-rates.md | head -20 && grep -n -A10 \"Table 8\\|Table 9\"

  [tool call] Bash {"command": "mkdir -p /tmp/asml_calc && cat > /tmp/asml_calc/a.py <<'EOF'\nD='/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-64e0o7p1/6399f27a-e97b-4097-a0f7-d5ff894399d3/tool-results/'\nimport json\n# annual statements pasted from tearshe

  [tool call] Bash {"command": "cat > /tmp/asml_calc/v.py <<'EOF'\ntax=0.17; inc_ic=0.40\nprice_usd=1589.60; fx=1.12; sh=383.0\nprice=price_usd/fx; mcap=price*sh/1000\ncash=12.7; debt=21.93*0.0890; nonop=3.81+0.5\nev=mcap-(cash-debt)-nonop\nprint(f\"price EUR {price:.0f} mcap {mcap:.1f} netcash {cash-debt:.2f} debt {d

  [tool call] Bash {"command": "cat >> /tmp/asml_calc/v.py <<'EOF'\nprint(\"---- 15-year horizon (CAP judgment), terminal RONIC=WACC; and RONIC=25% variant\")\ndef dcf2(revs, margins, wacc, g_term=0.03, ronic=None, rev0=44.3):\n    pv=0; prev=rev0\n    for t,(r,m) in enumerate(zip(revs,margins),1):\n        nopat=r*m*

ASSISTANT: Pulling ASML's data from Bigdata.com: financial statements and analyst ratings are in hand. Next I'm extracting consensus estimates, then earnings calls and industry research.

Data collection is done. I'm now running the numbers: returns on capital, earnings quality, buyback returns, what the share price implies, and a three-case valuation.

I've finished the ASML deep dive. It uses Bigdata.com data (company financials, consensus estimates, peer data, earnings-call transcripts, filings, broker notes and news) and five years of financial statements, because the data tool only returned five.

# ASML Holding (ASML): deep dive, 23 Oct 2026

Data as of: share price $1,589.60, the Oct 22, 2026 close in the Bigdata.com company data (about €1,419 at EUR/USD 1.12 on Oct 23); consensus estimates retrieved Oct 23, 2026 (FactSet, quarterly, number of estimates not given); statements FY2025 annual and Q3 2026 quarterly; newest document Oct 23, 2026.

## Summary

ASML is the only company that makes EUV (extreme ultraviolet) lithography machines, the tools needed to print the most advanced chips. It also leads the older DUV (deep ultraviolet) segment, and it services an installed base of machines that grows every year. FY2026 sales are guided to €44–45bn, about 36% growth [1].

The economics are exceptional, partly because customers pay large down payments that fund ASML's working capital:
- Return on invested capital (ROIC) was 123% in 2025 on capital net of cash and those prepayments (derived).
- Counting the prepayments as capital, ROIC was 42% (derived), against an assumed 9% cost of capital.

The competitive position rests on a sole-source EUV position that nobody has matched. Nikon left EUV in 2011 [27], and China's EUV prototype has not yet produced a working chip [23]. Pricing power is visible: ASML completed price increases on its most critical products that take effect from 2027 and fully from 2028 [1].

Earnings are mostly clean, with three caveats:
- Q3 2026 net income includes a €0.5bn revaluation gain on the Mistral AI stake [1].
- Gross margin is being lifted by machine-upgrade sales, which the CFO calls a "swing factor" [1].
- Operating cash flow depends on customer down payments, which reversed in 2023.

Capital allocation leans heavily to shareholders: 65% of 2021–2025 operating cash flow went to buybacks and dividends (derived). At today's price, the 2022–2025 buybacks returned roughly 2.5 times their cost (derived, approximate).

At an assumed 9% cost of capital, the price assumes consensus through 2028, then about 10% annual growth for another ten years at a 45% operating margin (derived). The probability-weighted value from three cases is about €1,005 per share at 9% (derived), with a range of €884–1,359 across 8–10% discount rates and terminal assumptions, below the €1,419 price. Peer multiples point the other way, to about €1,900. Most of that gap comes from the discount rate and from how long the advantage is assumed to last.

The main risk is a semiconductor capex cycle that turns after the AI build-out, combined with US legislation (the MATCH Act) that would ban DUV immersion sales and servicing in China. The next dated events are Nov 10, 2026, when the US Affiliates Rule suspension and China's rare-earth export-curb suspension both expire [8], and the Q4 results with 2027 guidance in January–February 2027.

## The business

ASML sells lithography systems (EUV, DUV immersion, DUV dry), metrology and inspection tools, and "Installed Base Management": service and upgrades on machines already in customer fabs. The Bigdata.com revenue segmentation section came back empty, so the segment figures below come from company calls.

| Segment | FY2025 | Growth 2025 | FY2026 guide (Oct 14) | Basis | Source |
|---|---|---|---|---|---|
| EUV systems | €11.6bn (48 systems incl. High-NA) | +39% | more than +45%; about 65 Low-NA units vs 44 | reported | [4], [1] |
| DUV systems | €12.0bn | -6% | non-EUV systems about +20% | reported | [4], [1] |
| Metrology and inspection | €0.83bn | +28% | YieldStar demand to more than double vs 2025 | reported | [4], [1] |
| Installed Base Management | €8.2bn | +26% | about +50% | reported | [4], [1] |
| Total net sales | €32.7bn | +16% | €44–45bn, gross margin about 56% | reported | [5], [1] |
| Logic / memory systems | €16.1bn / €8.4bn | +22% / -2% | about +10% (advanced logic more than +25%) / about +75% | reported | [4], [1] |

| Geography, share of net sales | 2023 | 2024 | 2025 | 2026 guide | Basis | Source |
|---|---|---|---|---|---|---|
| China | n/a | 36.1% | 29.1% | about 20% | reported | [7], [9], [1] |
| Taiwan | 29.3% | 15.4% | n/a | n/a | reported | [7] |
| South Korea | 25.2% | 22.7% | n/a | n/a | reported | [7] |
| Top four customers | n/a | n/a | about 61% | n/a | reported | [10] |

| Five-year trend (FactSet) | 2021 | 2022 | 2023 | 2024 | 2025 | Basis |
|---|---|---|---|---|---|---|
| Revenue, €bn | 18.6 | 21.2 | 27.6 | 28.3 | 32.7 | reported |
| Gross margin | 51.9% | 49.5% | 50.2% | 49.8% | 51.6% | derived |
| R&D, % of sales | 13.1% | 14.5% | 13.5% | 13.9% | 13.2% | derived |
| Operating (EBIT) margin | 35.1% | 30.7% | 32.8% | 31.9% | 34.6% | derived |

Notes on the tables:
- Margins are FactSet line items over revenue. FactSet's 51.6% 2025 gross margin is below the company's 52.8% [5] because of how cost of sales is defined.
- Profit has shifted toward EUV and the installed base. The installed base was 25% of 2025 sales (derived) and carries "very high-margin" upgrade components [1].
- Q3 2026 gross margin was 57.5%. At the start of 2026 the company guided 51–53% [17].
- Backlog at end-2025 was €38.8bn, of which €25.5bn was EUV [5]. ASML no longer discloses bookings, and the CFO pointed to down payments in non-current liabilities as "a nice proxy" [1].

## Economics

ROIC is shown three ways because customer prepayments (€16.0bn of deferred revenue at end-2025) are larger than ASML's whole net operating capital. The report quotes the hand-built ROIC with goodwill and shows the version that counts prepayments as capital beside it.

| Year | Tax rate | NOPAT, €bn | Invested capital, €bn | ROIC (avg capital) | NOPAT margin x turnover | ROIC counting prepayments as capital | Basis |
|---|---|---|---|---|---|---|---|
| 2021 | 15.2% | 5.54 | 5.97 | 92.9% (year-end) | 29.8% x 3.12 | 39.9% | derived |
| 2022 | 15.0% | 5.52 | 4.61 | 104.5% | 26.1% x 4.01 | 35.7% | derived |
| 2023 | 15.8% | 7.61 | 9.38 | 108.9% | 27.6% x 3.94 | 40.2% | derived |
| 2024 | 18.6% | 7.35 | 8.05 | 84.3% | 26.0% x 3.24 | 35.4% | derived |
| 2025 | 17.7% | 9.31 | 7.12 | 122.7% | 28.5% x 4.31 | 42.5% | derived |

How the figures are built:
- NOPAT (net operating profit after tax) is EBIT times (1 minus the effective tax rate).
- Invested capital is equity plus debt minus cash and short-term investments minus long-term investments. The operating-side build (assets minus cash and investments, minus non-debt liabilities) gives the same figure.
- Excluding goodwill and intangibles, invested capital is negative in every year, so that version of ROIC has no meaning.
- Return on incremental invested capital (ROIIC) for 2022–2025 was 110% (change in NOPAT over the lagged change in capital, derived).
- The spread over an assumed 9% cost of capital is about 114 points on the quoted basis and about 34 points counting prepayments.
- Reconciliation with FactSet: FactSet's ROIC was 47.4% for FY2025 and 66.6% on a trailing basis at Q3 2026. It divides by total capital (equity plus debt, €24.3bn) without deducting the €13.3bn of cash and €3.8bn of investments.
- R&D is expensed under US GAAP. Capitalizing it would lower every ROIC figure, and the R&D history needed to do that is not in the data.
- Only five years are tabled because the tearsheet returns five fiscal periods and offers no period offset.

## Industry structure and moat

| Checklist item | Evidence | Source |
|---|---|---|
| Industry map and share | Sole commercial EUV supplier; JPMorgan put ASML's lithography share at 100% in 2023. In 2009 ASML had 65–70% value share against Nikon and Canon. | [29], [30] |
| Share stability | Share has risen over 15 years. Nikon and Canon withdrew from EUV more than a decade before it became commercially viable. | [36], [27] |
| Pricing power | Price increases on "most critical products" agreed with customers, effect 2027 and fully from 2028. Value-based pricing (prices tied to customer productivity gains). About 10% parts increase in Korea. | [1], [28] |
| Concentration and customer power | Four customers about 61% of 2025 sales. TSMC has called High-NA too expensive, and TSMC High-NA volume production is planned for 2030, Samsung's for 2028. | [10], [2], [1] |
| Supplier power | Zeiss is the sole optics supplier; ASML owns a stake accounted as an associate, and in 2016 paid about $1.1bn (Bigdata.com deal data). ASML owns its light-source maker Cymer (acquired 2013). An EUV machine has more than 100,000 parts from about 200 principal suppliers. | Data, [13], [37], [26] |
| Entry and exit | A Chinese state-backed company began producing DUV immersion tools: about 5 in 2026 and 20 in 2027, against ASML's 131 immersion systems in 2025. China's EUV prototype has not yet made a working chip; chip production is targeted for 2028, and 2030 is considered more realistic. | [21], [22], [23] |
| Substitutes | Canon nanoimprint is in production at Kioxia for some memory layers. DUV multi-patterning is a costly workaround. | [31], [24] |
| Regulation | No EUV has ever shipped to China. Advanced DUV immersion needs a license. The MATCH Act would cut DUV immersion sales and servicing to China; CFRA put 10–15% of 2026 sales at risk and less than a 50% chance of enactment. | [8], [19], [20] |
| Technology that could change the structure | High-NA EUV (Intel has exposed more than 1 million wafers; fleet availability approaching 90%). 12-inch masks: pilot line 2031, production 2033. | [1], [35] |
| Source of advantage | Accumulated field data and the supplier ecosystem: "beyond a certain technological threshold, markets no longer correct monopolies." | [36] |
| Profit pool and direction | Litho intensity (lithography content per chip) is rising: DRAM is moving multi-patterning DUV to single-expose EUV, and new DRAM customers are adopting EUV. Gap: no wafer-fab-equipment profit-pool data in Bigdata.com. | [3], [1] |

Duration judgment: for EUV, the advantage should last 15 years or more (judgment). That is longer than the information-technology base rate, where about half of excess returns fade within four to five years (CFROI, a cash-flow return measure, has a 4-year persistence correlation of 0.50; global companies 1983–2015, historical base rate). The exception rests on three pieces of evidence: no rival has accumulated EUV field data, China's EUV effort is years from producing chips, and customers are asking to place orders for 2029–2030 [1].

The DUV business is less protected. Chinese domestic substitution could reach the China DUV revenue within three to five years if export controls tighten (judgment, [24], [38]).

## Earnings quality

| Year | Net income, €bn | Operating cash flow, €bn | Accrual ratio | OCF / net income | Change in deferred revenue, €bn | Stock comp, % of sales | Basis |
|---|---|---|---|---|---|---|---|
| 2021 | 5.88 | 10.85 | -16.4% | 1.84 | n/a | 0.63% | derived |
| 2022 | 5.62 | 8.49 | -8.6% | 1.51 | +4.55 | 0.33% | derived |
| 2023 | 7.84 | 5.44 | +6.3% | 0.69 | -1.04 | 0.49% | derived |
| 2024 | 7.57 | 11.17 | -8.1% | 1.47 | +1.13 | 0.61% | derived |
| 2025 | 9.61 | 12.66 | -6.2% | 1.32 | +3.44 | 0.62% | derived |

The accrual ratio is (net income minus operating cash flow) over average total assets. A negative figure means cash came in ahead of reported earnings.

EBITA rebuild for 2025: EBIT €11.30bn plus €0.12bn amortization of intangibles gives EBITA of €11.42bn. FactSet's "operating income after unusual items" differs by only €14m, so no material one-offs were found in 2025 (derived). For Q3 2026, operating profit of €5.16bn (44.4% margin) is clean, but pre-tax margin of 49.3% includes the Mistral gain.

| Flag | Recurrence | Severity | Source |
|---|---|---|---|
| €0.5bn Mistral AI fair-value gain in Q3 2026 net income (about €1.3 per share), valued with a venture-capital method (Level 3: no market price, model inputs) | one-off | medium for EPS comparisons | [1], [11] |
| Q2 2026 Technology and IT transformation costs booked mainly in R&D; amount not given | one year | low | [2] |
| Upgrade revenue lifting gross margin (installed-base revenue beat guidance by about €0.4bn in Q3) | recurring but variable | medium | [1], [14] |
| Cash flow depends on down payments: Q3 2026 FCF of €11.4bn "underpinning... down payments"; in 2023 OCF/net income fell to 0.69 as deferred revenue reversed | cyclical | medium | [1] |
| A 2025 cash inflow from receivables factoring (selling receivables early for cash) was questioned at the 2026 AGM. The incentive plan's cash-conversion metric paid 200% of target for 2022–24. Amount not found. | unknown | medium (governance) | [13], [7] |
| Inventory €11.8bn, about 131 days of sales, during a capacity ramp | ramp-related | low | Data |
| Stock compensation 0.6% of sales, expensed under US GAAP | recurring | low | Data |

Piotroski F-score 9 (Q3 2026) and Altman Z of 14.6 (Q2 2026), as reported by FactSet. Free cash flow note: the company's 2025 FCF of €11.0bn [4] matches operating cash flow minus capex (derived). The FactSet free-cash-flow field (€8.5bn) appears to also subtract dividends.

## Capital allocation

| 2021–2025, €bn | Amount | % of OCF | Basis |
|---|---|---|---|
| Operating cash flow | 48.6 | 100% | reported |
| Capex | 8.2 | 17% | reported |
| Buybacks | 20.7 | 42% | reported |
| Dividends | 11.3 | 23% | reported |
| Acquisitions and net investment purchases (including €1.3bn Mistral) | 0.4 + other investing 2.2 | 5% | reported |
| Cash build (€7.6bn to €13.3bn) | 5.7 | 12% | derived |

- **Buyback return, net of issuance.** Average shares fell from 409.7m (2021) to 388.6m (2025): 21.1m net shares retired for €12.1bn spent in 2022–2025, or about €573 per share. Against €1,419 today that is about 2.5 times, roughly 35–40% a year over an average holding of about 2.8 years. This is above the assumed 9.5% cost of equity. The figure is approximate because average share counts lag the timing of 2021 purchases (derived).
- **2026 buybacks.** €1.1bn in Q2 and €4.1bn in Q3 under the new €12bn 2026–2028 program [2], [1]. The Q1 amount is not in the data. Q3 purchases were made near current prices, so their return is not yet known.
- **Dividend.** €7.50 per share for 2025, up 17% [3]. 2026 interims are €1.88 per quarter [1].
- **Deals.** Five tracked deals totalled $1.46bn disclosed, all cash (Bigdata.com deal data): the Zeiss SMT stake (about $1.1bn, 2016), Mapper (2019) and Berliner Glas (2020–21). Mistral (€1.3bn for about 11%, 2025 [12]) shows a €0.5bn unrealized gain so far, about 38% (derived). Deal premiums and synergy claims are not disclosed.
- **Leverage.** Net cash of about €10.8bn (derived). Rated A1 by Moody's and A+ by Fitch, both stable [17].
- **Incentives.** The short-term bonus is 60% EBIT margin, 20% customer goals and 20% strategic goals. The long-term plan is 30% relative total shareholder return, 30% cash conversion, 20% technology leadership and 20% ESG [7]. No metric rewards return on capital or growth per share. The CEO has said he is tying his pay to employee satisfaction [34].

## What the price implies

| Measure | Value | Basis |
|---|---|---|
| Price | €1,419 ($1,589.60 / 1.12) | derived |
| Market cap / EV | €543.6bn / €528.5bn (383.0m shares; net cash €10.8bn; non-operating investments €4.3bn) | derived |
| P/E: FY2026E / FY2027E | 33.6x / 24.3x (EPS €42.3 / €58.4) | derived from consensus |
| EV/EBITDA: trailing / FY2027E | 32.3x / 19.0x | derived |
| Steady-state value (FY2027E NOPAT €21.5bn / 9%) | €239bn, 45% of EV | derived |
| Value attributed to growth beyond 2027 | 55% of EV | derived |
| Warranted P/E (growth 4–5%, return on new investment 40%, cost of equity 9.5%) | 16–19x vs 24.3x actual | derived |

At a 9% cost of capital, the price requires consensus revenue of €58.5bn in 2027 and about €73bn in 2028. Consensus covers only Q1–Q3 2028, so the 2028 figure is an extrapolation (assumed). After that, the price needs 10% annual growth for another 10 years at a 45% EBIT margin, which puts revenue near €190bn in 2038. Alternatives are 8% growth for 14 years or 12% for 8 years. In each case the competitive advantage has to last 10 to 16 years from now (derived).

Base rates, from top-1,000 global companies 1950–2015, inflation-adjusted (historical, not current facts):
- Consensus implies about 31% nominal sales growth a year from 2025 to 2028. Only 4.6% of companies with sales above $25bn grew 20% or more a year in real terms over three years.
- Over ten years, the median real growth for that size class was 1.8% a year. Only 1.5% sustained 15% or more.
- 37% of that class saw real sales fall over three years.

The price therefore assumes growth from a company that is already large, in the top few percent of history.

## Valuation

Assumptions: WACC of 9% (assumed: little debt, an assumed euro risk-free rate of about 3.5%, equity beta 1.2, risk premium 5%; Bigdata.com has no WACC; US 10-year yield is 5.00%). Tax 17% [1]. Incremental invested capital of €0.40 per €1 of new sales (assumed, between 0.22 net of prepayments and 0.71 gross). An explicit forecast for 2027–2041 (15 years, set by the moat judgment). Continuing value with the return on new investment fading to WACC, with a 25% return variant. Valuation date end-2026. ASML is treated as a cyclical: each case includes a demand path, and the bear case includes a downturn.

| Case | Path | Value per share (9%, terminal return = WACC) | With 25% terminal return | Probability | Basis |
|---|---|---|---|---|---|
| Bear | Sales €55bn in 2027–28, -24% to €42bn in 2029 (AI capex digestion plus MATCH Act), then 3–5% growth; EBIT margin 32–40% | €568 | €625 | 30% | judgment |
| Base | €58.5bn 2027, €70bn 2028, -10% in 2029, then 8% fading to 4%; €128bn by 2041; EBIT margin 44% | €1,022 | €1,144 | 50% | judgment |
| Bull | €60bn, €78bn, €88bn, €95bn by 2030, then 11% fading to 5%; €206bn by 2041; EBIT margin 47–48% | €1,619 | €1,834 | 20% | judgment |
| Probability-weighted | | €1,005 | €1,126 | 100% | derived |

Probabilities are anchored on the 37% of large companies with three-year real sales declines and on information technology having the highest operating-margin sensitivity to sales of any sector (0.17; 1950–2015 base rates). The bull case is held below the base case because sustained top-tail growth at this size is rare.

Terminal checks for the base case at 9%:
- Terminal value is 39% of EV.
- The implied terminal EV/EBIT is 9.5x, against 20.4x today.
- ROIC counting prepayments rises from 64% in 2027 to 76% in 2041 (derived), above the 35–43% history. The capital assumption is generous, so the values lean high.

Bridge per share, base case: EV €376.4bn + net cash €10.8bn + investments €4.3bn = equity €391.4bn / 383.0m shares = €1,022. Minority interests are zero, there is no pension deficit in the data, and leases (€61m current) are left out as immaterial.

Base case value per share by WACC and terminal growth (25% terminal return):

| WACC \ g | 2% | 3% | 4% |
|---|---|---|---|
| 7% | €1,561 | €1,733 | €2,018 |
| 8% | €1,284 | €1,379 | €1,522 |
| 9% | €1,087 | €1,144 | €1,223 |
| 10% | €941 | €977 | €1,024 |

Comps cross-check (FactSet trailing multiples at each company's last quarter-end, not today's prices):

| Company | P/E | EV/EBITDA | EV/Sales | ROIC | Operating margin |
|---|---|---|---|---|---|
| ASML (Q3 2026) | 43.5x | 35.3x | 14.5x | 66.6% | 44.4% |
| Applied Materials | 46.2x | 42.2x | 13.9x | 32.4% | 33.7% |
| Lam Research | 46.9x | 38.8x | 15.0x | 59.7% | 40.0% |
| KLA (verify) | 82.3x | 65.7x | 29.3x | 48.6% | 43.4% |
| Tokyo Electron | 56.8x | 44.8x | 13.3x | 33.6% | 28.9% |

The peer median EV/EBITDA of 43.5x on ASML's trailing EBITDA of €16.35bn gives about €1,900 per share (derived). KB Securities puts ASML's forward P/E at 29.6x with a PEG (P/E divided by growth) of 0.7, in line with Lam (0.7) and Applied Materials (0.6) [15].

The sector as a whole is priced for long growth, so comps do not provide an independent anchor. Sell-side targets of €1,900 (LBBW, a DCF) [16] and €2,100 (Berenberg) [18] are consistent with a cost of capital near 7%, or near 8% with a 25% terminal return.

Range: €884–1,359 per share across 8–10% WACC and both terminal assumptions; €1,361–1,709 at 7%. The price sits between the base and bull cases at 9%; it would take about a two-thirds weight on the bull case to reach it with no bear case (derived).

## Risks and kill criteria

| Rank | Risk | Probability (judgment) | Size | Early signal | Source |
|---|---|---|---|---|---|
| 1 | AI and memory capex digestion after 2027–28 | about 30% within 3 years | revenue -20 to -25%, value toward €570 | quarter-on-quarter fall in down payments; memory price declines | [1], [33] |
| 2 | MATCH Act: DUV immersion sales and servicing ban in China | less than 50% (CFRA) | 10–15% of sales at risk, or about 5% net (Quilter) | committee votes; Dutch alignment | [19], [20] |
| 3 | Chinese domestic DUV | low before 2028 | China DUV, the bulk of an approximately 20% sales share | SMIC or CXMT qualification; unit counts above 20 a year | [21], [24] |
| 4 | Ramp execution and cost (30% more capacity in 2027 and more in 2028) | medium | 1–2 points of gross margin | Q4 margin guided down to about 57% on ramp costs | [1] |
| 5 | Upgrade revenue normalizes | medium | gross margin swing | installed-base revenue against the €3.7bn Q4 guide | [1] |
| 6 | US–Netherlands compliance dispute (alleged EUV shipment to China, denied by ASML) | low | license regime | Commerce Department actions | [39] |
| 7 | Sector multiple compression | ongoing | stock fell 8% in a month as the 10-year yield reached 5.0% | yields; Lam's Oct 21 supply-constraint warning | [32], Data |

Downside floors (derived):
- Steady-state value on FY2026 NOPAT plus net cash and investments: about €480 per share.
- The same on FY2027 NOPAT: about €665 per share.
- Bear case at 9%: €568 per share.
- The balance sheet does not threaten solvency: net cash and A1/A+ ratings.

What breaks the base case (observable thresholds):
- 2027 gross margin guidance below 56% in January–February 2027.
- A quarter-on-quarter decline in non-current liabilities (the down-payment proxy) in two consecutive quarters.
- MATCH Act enacted with a servicing ban.
- 2027 EUV output below about 85 units (the 30% increase).
- Capital Markets Day on June 10, 2027 [2] leaving the €44–60bn 2030 revenue range [16] unchanged, even though 2026 is already at its low end.

## Catalysts and what to watch

| Date or window | Event | Mechanism | Direction and size | Certainty |
|---|---|---|---|---|
| Nov 4, 2026 | €1.88 interim dividend payable [1] | cash return | small | scheduled |
| Nov 10, 2026 | US Affiliates Rule suspension and China rare-earth curb suspension expire [8] | China customer access; magnet supply | down if not renewed; up to the China share | scheduled; outcome unknown |
| Late Jan to Feb 24, 2027 | Q4 2026 results and 2027 gross margin guide. LBBW lists Jan 27; the Quartr calendar lists Feb 24. [16], Data | first 2027 numbers; pricing effect | ±10% stock moves on prior prints | scheduled; date conflict |
| Early 2027 | NXE:3800F (260 wafers per hour) and 330 wafers-per-hour immersion launch [1] | higher selling price and mix | up for margin | planned |
| 2026–27 | MATCH Act progress [19] | China DUV | down 5–15% of sales | uncertain |
| Jun 10, 2027 | Capital Markets Day [2] | new 2030 targets | likely up if raised | scheduled |
| 2028 / 2030 | Samsung / TSMC High-NA in volume production [1] | High-NA units ($400m each [29]) | up | announced |

Five metrics to watch:
1. Quarterly change in down payments in non-current liabilities.
2. EUV units, against about 65 in 2026 and about 85 in 2027.
3. Installed-base revenue and gross margin, separating upgrades from the rest.
4. China share of sales, against about 20%.
5. Capex guidance from TSMC, Samsung, SK Hynix and Micron.

## What would change this view

1. A lower justified discount rate. The price is consistent with the base case at about 7%. Lower euro rates would close most of the gap.
2. Evidence the cycle is longer: customers' 2029–2030 orders accepted with down payments, expected after ASML's current demand review [1].
3. 2027 gross margin guided at or above 58%, showing the pricing reset is reaching profit.
4. A MATCH Act enactment or a non-renewal on Nov 10, 2026, which moves weight toward the bear case.
5. A second memory maker qualifying Canon nanoimprint, or China's DUV output exceeding 20 units in 2027 [31], [21].

## Gaps

- Only five years of statements (no period offset in the tearsheet).
- The revenue segmentation section was empty, so segment data comes from calls.
- The number of estimates per consensus figure is not given; FY2028 is extrapolated from three quarters.
- Not found: Q1 2026 buyback amount, factoring amount, deal premiums, the full FY2025 20-F remuneration section (the FY2024 20-F was used), and wafer-fab-equipment market share data.
- WACC is assumed. No short interest or positioning data.
- The Q4 earnings date conflicts between sources.
- KLA multiples look high and should be checked.
- The Q4 2025 transcript prints "2025 revenue opportunity €44–60bn"; other calls give this as the 2030 range, and the report uses 2030.

## Sources

[1] [ASML Holding N.V.: Q3 2026 Earnings Call on Oct 14, 2026 - Transcript (Quartr)](https://app.bigdata.com/documents/DAEADC8248E76E72980C5DE74063BE56)
[2] [ASML Holding NV: Q2 2026 Earnings Call - Jul 15, 2026 (FactSet)](https://app.bigdata.com/documents/749F673802981A6B67BC7FE6AC513813?cnum=11)
[3] [ASML Holding NV: Q4 2025 Earnings Call - Jan 28, 2026 (FactSet)](https://app.bigdata.com/documents/98F2B164C7CDBBB2B908ECF795A6B402?cnum=8&cnum=11&cnum=12&cnum=10&cnum=9)
[4] [ASML Holding N.V.: Q4 2025 Earnings Call on Jan 28, 2026 - Transcript (Quartr)](https://app.bigdata.com/documents/B9EFDAF3615B720884E4AA6BFD98911F)
[5] [ASML Holding N.V.: Q4 2025 Earnings Call on Jan 28, 2026 - Transcript (Quartr, CFO remarks)](https://app.bigdata.com/documents/1D26071B58B0E420087D4644DF779E53?cnum=16&cnum=2&cnum=4)
[7] [ASML Holding NV Form 20-F for FY 2024 - Mar 5, 2025](https://app.bigdata.com/documents/F44BC5F8ED34CFA28D8DDC5F3A1B602B)
[8] [ASML Holding NV Form 6-K - Feb 25, 2026](https://app.bigdata.com/documents/3BDC142E085B1B7833C5553013E3B1A0?cnum=137&cnum=43)
[9] [ASML Holding N.V. Annual Activity Report - Feb 24, 2026](https://app.bigdata.com/documents/3B729FAA03075575C2B3C61AF05CB27C?cnum=141)
[10] [ASML vs. Taiwan Semiconductor Manufacturing - Nasdaq, Oct 12, 2026](https://app.bigdata.com/documents/30EADE655EE1EFE9BC1CE35305C97679?cnum=2)
[11] [ASML Holding NV Form 6-K - Jul 15, 2026](https://app.bigdata.com/documents/2698D49F08BCBAF742BD6FE6F6A937B3?cnum=66&cnum=67)
[12] [ASML invests EUR1.3 billion in French AI firm Mistral for 11% stake - Alliance News, Sep 9, 2025](https://app.bigdata.com/documents/696DC97C0D6A52A78CC80095F441CFC0?cnum=1&cnum=2)
[13] [ASML Holding N.V.: 2026 Annual General Meeting - Apr 22, 2026 (Quartr)](https://app.bigdata.com/documents/DADABFA132444C4EDD5C28CD9B5546EC?cnum=135)
[14] [ASML failed to smile despite strong results - Financial News, Oct 14, 2026](https://app.bigdata.com/documents/EA1BD4B93CCFFB4FBB63D2EF634DE529?cnum=3)
[15] [ASML Holding - Even capacity expansion cannot keep up with demand - KB Securities, Oct 17, 2026](https://app.bigdata.com/documents/2162CA8A058ED7A6DEB3A74EDD8DA561?cnum=32&cnum=51)
[16] [ASML Holding Stock Compact: AI Boom Leads to Higher Annual Targets Again - LBBW, Oct 15, 2026](https://app.bigdata.com/documents/2D1279EE25101B4F736E11DD909E9C94?cnum=7&cnum=1&cnum=2)
[17] [ASML Holding Credit Kompakt: Annual targets raised - LBBW, Jul 16, 2026](https://app.bigdata.com/documents/E3ED4199A6AFC9A9E7B566BB7EE2B01A?cnum=3)
[18] [Berenberg Sees 'Strong' Demand Visibility for ASML Through 2028 - MT Newswires, Sep 10, 2026](https://app.bigdata.com/documents/BFD51BB7A49AE8DA2050BEBFE59BBCEC?cnum=1)
[19] [OL260518_OUTLOOK - S&P Capital IQ NetAdvantage (CFRA), May 18, 2026](https://app.bigdata.com/documents/8CBCD9BD188E3A9B72C49111B29736A7?cnum=7)
[20] [ASML shares fall after proposed U.S. export curbs - CNBC, Apr 7, 2026](https://app.bigdata.com/documents/D546824328D45628E95826E069734305?cnum=3&cnum=1)
[21] [IN THE KNOW: JPMorgan plays down threat to ASML after China DUV report - Alliance News, Jul 27, 2026](https://app.bigdata.com/documents/5B78F8FC44C0B143019BD8ED6D22AFB2?cnum=1)
[22] [Why Is ASML Stock Falling Today? - Yahoo! Finance, Jul 27, 2026](https://app.bigdata.com/documents/C9917B66D8833146BC011F53073411D8?cnum=1)
[23] [China talks up EUV progress, but gap with ASML remains wide - Korea Herald, Oct 21, 2026](https://app.bigdata.com/documents/176FF00976375D55F88147A4474C99D1?cnum=5)
[24] [Huawei drives China's push to make its own advanced chips - Financial Times, Sep 8, 2026](https://app.bigdata.com/documents/05FC7C380B480635F3992FFADF0C2933?cnum=2&cnum=6&cnum=4)
[26] [ASML Has a China Warning for Trump - Benzinga, Sep 28, 2026](https://app.bigdata.com/documents/D53B66C815AEF675894874EA9FBEC5FE?cnum=2)
[27] [ASML Forces First-Ever Blanket Parts Hike on Samsung and SK Hynix - Tech Times, Oct 13, 2026](https://app.bigdata.com/documents/A943EA30D711FC61C27080FA0AB34718?cnum=6)
[28] [ASML - Two-way growth through capacity expansion and price increases - Eugene Investment & Securities, Oct 17, 2026](https://app.bigdata.com/documents/F7F476E5F274DE4FC655BB48D593DFF1?cnum=4)
[29] [Giants Finally Kneel Before ASML - Global Economic, Sep 15, 2026](https://app.bigdata.com/documents/167C0FC2C8656E546A5F1738004C756B?cnum=3)
[30] [ASML Holding N.V.: UBS Global Technology and Services Conference - Jun 8, 2010](https://app.bigdata.com/documents/DC3DCCC2A1A3181B3819A1131DE5D55D?cnum=2)
[31] [Chasing ASML's Dominance: Canon and Nikon - AOL.com, Sep 17, 2026](https://app.bigdata.com/documents/9E52298A85A393C4F4CF389E604A0D2C?cnum=1&cnum=4)
[32] [Lam Research Sinks 9% as Supply Constraints Cap Outlook - AOL.com, Oct 22, 2026](https://app.bigdata.com/documents/BD7F34559BE7A8D0A7AB86EE0D37584B?cnum=2)
[33] [The Earnings Twist In The AI Chip Bubble Debate - Benzinga, Oct 21, 2026](https://app.bigdata.com/documents/941BF0686C48BA715E0C476C8142472D?cnum=5)
[34] [The CEO of Europe's most valuable company says he is tying his pay to employee satisfaction - Business Insider, Oct 23, 2026](https://app.bigdata.com/documents/C6ED8014E0D1BD535051B25906A87D41?cnum=5)
[35] [TSMC, ASML Launch 12-inch EUV Mask Initiative - MT Newswires, Sep 8, 2026](https://app.bigdata.com/documents/9D6F3672E11071DC0E540EADD3F7BAF5?cnum=1)
[36] [Why Asia or the US have not produced a rival to ASML - Financial Times, Jan 21, 2026](https://app.bigdata.com/documents/DF3F4C90F90682927567E97CF65E955B?cnum=5)
[37] [China unveils prototype of core EUV lithography equipment component - Financial News, Oct 15, 2026](https://app.bigdata.com/documents/2DA405BAB339DDC719C4226277E49DB6?cnum=2)
[38] [China's Mid-Tier Emergence Threatens ASML Over the Next 3-5 Years - AOL.com, Oct 23, 2026](https://app.bigdata.com/documents/E271B52BFED80FCFFB1EC34D11A4904F?cnum=1&cnum=6)
[39] [Market Chatter: ASML Says It Has Not Shipped EUV Chipmaking Tools to China - MT Newswires, Jun 22, 2026](https://app.bigdata.com/documents/85FA9DCFC75FDB4CD17B16693B93605F?cnum=1)

Data: Bigdata.com company tearsheets for ASML, Applied Materials, Lam Research, KLA and Tokyo Electron (FactSet fundamentals, ratios and consensus estimates; FMP analyst ratings and targets; deal history, 13F holdings and dividends), and the Bigdata.com market tearsheet (EUR/USD, US yields), all retrieved Oct 23, 2026. The analyst consensus is 26 buy or strong buy, 16 hold and 3 sell, with a mean target of $2,330.75 (range $2,100–2,623). Base rates come from the skill's reference file (Mauboussin Base Rate Book, top-1,000 global companies, 1950–2015).

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

I can save this report to your Bigdata.com account so later searches can find it, or produce it as a Word document.
