# qt-jpm#1

USER: Quick take on JPMorgan

  [tool call] Skill {"skill": "bigdata-com:bigdata-quick-take", "args": "JPMorgan"}

  [tool call] Bash {"command": "cat /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references/working-with-bigdata.md; ls /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/sk

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_fetch_document,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet", "max_results": 5}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "JPM", "plugin_slug": "bigdata-quick-take"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references/; cat output-standard.md; grep -n -i -A40 \"bank\" sector-primers.md | head -80; grep -n -i -B2 -A15 \"bank\\|price to bo

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "619882", "company_type": "Public", "sections": ["company_overview", "analyst_ratings", "latest_earnings", "earnings_calendar", "analyst_estimates"], "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "619882", "company_type": "Public", "sections": ["financial_statements", "financial_ratios", "key_metrics"], "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "JPMorgan Chase news over the last 30 days that moved the stock or analyst estimates", "max_chunks": 20}}, "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet {"rp_entity_id": "619882", "plugin_slug": "bigdata-quick-take"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-ejzt7u-s/6f87eeef-edc1-4d7b-bb5d-41c532b48d17/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792487466.txt\njq -c '.company_overview, .analyst_data, .lates

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-ejzt7u-s/6f87eeef-edc1-4d7b-bb5d-41c532b48d17/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792487466.txt\njq -c '.estimates.periodicity, .estimates.sourc

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-ejzt7u-s/6f87eeef-edc1-4d7b-bb5d-41c532b48d17/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792487466.txt\njq -c '.estimates.records[] | select(.metric|te

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references/; grep -n -i \"eps\\|earnings growth\\|bank\\|ROE\\|10 percent\\|10%\" base-rates.md | head -40; grep -n -A12 \"^## Formu

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "outlook for net interest income, expenses, card net charge-offs and capital; risks management is worried about", "filters": {"reporting_entities": ["619882"], "reporting_periods": [{"fiscal_year": 2026, "fiscal_quarter": 3}], "document_type": {"

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "JPMorgan Chase third quarter 2026 earnings call: management outlook on net interest income, expenses and credit", "max_chunks": 20}}, "plugin_slug": "bigdata-quick-take"}

  [tool call] Bash {"command": "sed -n 95,125p /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references/base-rates.md", "description": "Read the earnings growth base-rate table"}

ASSISTANT: I have the price, analyst targets, the Q3 results and the news. Next I'm pulling the annual consensus estimates, then the Q3 earnings call.

# JPMorgan Chase (JPM) quick take, 23 Oct 2026
Data as of: price close 23 Oct 2026; FactSet consensus retrieved 23 Oct 2026; latest statements Q3 2026; newest document 23 Oct 2026.

## The view
At $331.58, JPM trades at 2.9x tangible book (the value of shareholders' equity excluding goodwill and intangibles). At an assumed 10% cost of equity, that price assumes JPM keeps earning about 21% on its tangible equity and grows about 4.4% a year indefinitely. Q3 2026 backed up the return assumption (20% ROTCE) but missed on earnings per share. The price relies on two things holding: net interest income (NII) growth in 2027, and trading and advisory activity staying at today's high levels. The view improves if the $107bn NII central case for 2027 holds in January along with flat expense guidance. It weakens if the hikes in the forward rate curve do not happen or if Markets revenue falls back.

## What the price implies
| Measure | Value | Basis | Source |
|---|---|---|---|
| P/E on FY2027 EPS ($25.62, sum of quarterly estimates) | 12.9x | derived | Data |
| Steady-state P/E at 10% cost of equity (assumed: US large-bank range of 9-11%) | 10.0x; steady state is 77% of the price | assumed / derived | - |
| Price to tangible book ($112.84, Q3) | 2.94x | derived | Data |
| FY2027 return on tangible equity implied by consensus | about 20.8% | derived (EPS / average tangible book) | Data |
| Perpetual growth implied by P/TBV = (ROTCE - g)/(COE - g) | 4.4% (2.9% at 9% COE, 5.9% at 11%) | derived | - |
| Consensus growth: FY2027 EPS vs FY2026; analysts' long-term growth rate | +2.1%; 10.9% | reported | Data |
| Base rate | 36.6% of companies grew real net income 10%+ a year over 5 years (Credit Suisse Base Rate Book, 2016, all sizes; verify) | reported, historical | - |
| Analyst price targets | $312-425, consensus $373 (+13%); 32 buy, 27 hold, 2 sell | reported | Data |

The roughly 4% growth the price implies is undemanding. The 10.9% long-term consensus sits in the top 40% of the historical base rate.

## The three drivers
**1. NII.** Management's central case for 2027 NII excluding Markets is about $107bn, roughly $5bn above the annualized Q4 guide. About a quarter of that $5bn depends on rate hikes priced into the forward curve [1]. The risk runs down: management expects some depositors to move into higher-yielding CDs if rates rise, which raises funding costs [2].

**2. Markets and investment banking fees.** In Q3, Equities revenue rose 49% and FICC (fixed income, currencies and commodities) fell 4%. Management said "evolving market conditions have recently slowed activity a bit" [1]. The risk runs down. Dimon on the current environment: "We just don't know when it's going to stop" [7].

**3. Expenses and credit.** Q3 expenses were $27.3bn, up 12% year on year, with a $539m reserve build [1]. Morgan Stanley expects 2027 consensus EPS to rise 4% if expense guidance does not reset higher [4]. Seaport sits above consensus on expenses [6]. The risk runs up on costs.

## Risks and what would change the view
- **Activity normalises.** First signal: the mid-quarter guidance management gives at industry conferences (the last was 15 Sep) [5].
- **Capital.** Unrealised bond losses (other comprehensive income) cut the CET1 capital ratio 30bp to 13.9% in Q3. Q3 also included $658m of securities losses [1]. Signal: CET1 in Q4 if rates keep rising.
- **Credit.** Dimon said "we are tightening up a little bit on credit" because lending terms have loosened [2]. Signal: card net charge-offs above the ~3.2% guide, or further wholesale reserve builds.

More positive: 2027 NII reaffirmed with expense guidance flat. More negative: NII guidance cut, or Markets revenue down year on year.

## Next date
Q4 2026 results on 14 Jan 2027, call at 8:30 ET. Management said it will refine the 2027 NII guide then [1].

## Gaps
The data has no 30-day estimate revisions and no analyst count. Consensus is quarterly only, and FY2028 covers three quarters. The 10% cost of equity is an assumption. Media sentiment over 90 days is mildly negative (-0.16 against a -0.13 baseline), while media attention is high (2.1 standard deviations above its quarterly norm).

## Sources
[1] [JPMorgan Chase Q3 2026 Earnings Call - Oct 13, 2026 (FactSet)](https://app.bigdata.com/documents/03E0A18161F6E16AA00C64F04D0A3AB5?cnum=2&cnum=5&cnum=4&cnum=3)
[2] [JPMorgan Chase Q3 2026 Earnings Call transcript - Oct 13, 2026 (Quartr)](https://app.bigdata.com/documents/A15CB69C7D9E63C1A208A859E44167A0)
[3] [MT Newswires: JPMorgan Shares Rise Despite Q3 Miss - Oct 13, 2026](https://app.bigdata.com/documents/BA4CAEED06C3A075BFB0BD4EE252B25B?cnum=1)
[4] [The Fly: JPMorgan target raised to $377 at Morgan Stanley - Oct 14, 2026](https://app.bigdata.com/documents/21BE87F07E96044BFE70CF2E6FE322DF?cnum=1)
[5] [Benzinga: JPMorgan's Equities Business Surged 86% - Oct 6, 2026](https://app.bigdata.com/documents/A54FD917D776954F889589E01467146A?cnum=1&cnum=2)
[6] [CNBC Pro: Big banks report earnings this week - Oct 11, 2026](https://app.bigdata.com/documents/C4753209CE642D6F1464ED1040A73A0D?cnum=2)
[7] [AOL: Dimon warns forces "shift under the surface" - Oct 16, 2026](https://app.bigdata.com/documents/3714494FD30344AFC85D4042526A0609?cnum=3)

Data: Bigdata.com company tearsheet for JPMorgan Chase (FactSet fundamentals and consensus, FMP price targets and ratings, Quartr calendar) and the Bigdata.com sentiment tearsheet, retrieved 23 Oct 2026.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

Want me to add JPM to a Bigdata.com watchlist?
