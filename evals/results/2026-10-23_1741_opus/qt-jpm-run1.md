# qt-jpm#1

USER: Quick take on JPMorgan

  [tool call] Skill {"skill": "bigdata-com:bigdata-quick-take", "args": "JPMorgan Chase (JPM)"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references && ls && cat working-with-bigdata.md expectations.md output-standard.md && grep -n -i -A30 \"bank\" sector-primers.md | h

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_fetch_document,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet", "max_results": 5}

  [tool call] Bash {"command": "F=/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references; sed -n '1,200p' $F/expectations.md; echo ----; sed -n '1,120p' $F/output-standard.md", "description": "Read expectations 

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "JPM", "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "619882", "company_type": "Public", "sections": ["company_overview", "key_metrics", "financial_ratios", "analyst_estimates", "latest_earnings", "earnings_calendar", "analyst_ratings", "financial_statements"], "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "JPMorgan Chase news over the last 30 days that moved the stock or analyst estimates", "max_chunks": 20}}, "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "JPMorgan Chase third quarter 2026 earnings call guidance on net interest income and expenses", "max_chunks": 20}}, "plugin_slug": "bigdata-quick-take"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet {"rp_entity_id": "619882", "plugin_slug": "bigdata-quick-take"}

  [tool call] Bash {"command": "F=/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references; grep -n -i \"^#\" $F/sector-primers.md | head -40; grep -n -i -B2 -A40 \"^## .*bank\" $F/sector-primers.md | head -70; gr

  [tool call] Bash {"command": "F=/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references; sed -n 255,296p $F/sector-primers.md; sed -n 60,90p $F/base-rates.md\nT=/Users/mkangrga/.claude-work/projects/-private-va

  [tool call] Bash {"command": "T=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-p1xogye4/ae3498ce-94e6-43d1-81ee-3201818bfe71/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791783616.txt\njq -c '.estimates.periodicity, .estimates.sourc

  [tool call] Bash {"command": "F=/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-quick-take/references; grep -n -i -A16 \"Table [0-9]*\\. .*\\(EPS\\|earnings\\|net income\\)\" $F/base-rates.md | head -60\npython3 -I -c \"\np=

ASSISTANT: The data is in: price, consensus, the Q3 call and sentiment. Next I'm pulling the annual EPS consensus and working out what the price implies.

# JPMorgan Chase (JPM) quick take, 23 Oct 2026
Data as of: price close 23 Oct 2026 ($331.58); FactSet consensus retrieved 23 Oct 2026; latest statements Q3 2026 (reported 13 Oct 2026); newest document read 23 Oct 2026.

## The view
At $331.58, JPM trades at 12.9x consensus 2027 EPS and about 3.0x tangible book. At an assumed 10% cost of equity, about three-quarters of the price is explained by holding today's earnings flat forever. The remaining quarter needs roughly 3.6% a year of long-run earnings growth at a return on tangible common equity (ROTCE, net income over tangible common equity) of about 21%. That bar is modest for a bank that just earned 20% ROTCE [1] and has guided net interest income (NII) up about $5bn for 2027 [1]. The price is therefore not paying for growth. It is paying for those returns to last. Q3 was the first earnings miss in nearly three years [2], and most of the miss came from the Corporate line, not the operating businesses [4]. The reading turns more negative if 2027 expense guidance in January comes in above the roughly $114bn consensus, or if card losses move above the 3.2% guide.

## What the price implies
| Measure | Value | Basis | Source |
|---|---|---|---|
| Forward P/E, 2027 consensus EPS $25.62 | 12.9x | derived | Data |
| Price to tangible book, Q3 2026 | 3.0x | derived | Data |
| Cost of equity | 10% (range 9 to 11%) | assumed: a conventional large-US-bank cost of equity; the current 10-year Treasury yield was not retrieved | judgment |
| Steady-state P/E (1 / cost of equity) | 10.0x (9.1x to 11.1x) | derived | - |
| Share of the price explained by the steady state | 77% (70 to 86%) | derived | - |
| Implied perpetual EPS growth at a 2027 ROTCE of 20.8% | 3.6% (2.0 to 5.2%) | derived | Data |
| Consensus long-term EPS growth | 10.9% a year | reported | Data |
| Consensus 2027 EPS vs 2026 EPS (3 reported quarters plus Q4 estimate) | +2.1% | derived | Data |
| Analyst price targets vs price | mean $373 (+13%); low $312 (-6%); high $425 (+28%) | reported | Data |
| 30-day estimate revision | not available | gap | - |

Implied growth comes from the justified P/E formula, P/E = (1 - g/ROE) / (ke - g), where g is perpetual earnings growth, ROE is return on equity and ke is the cost of equity. 2027 ROTCE is consensus 2027 EPS divided by average consensus tangible book per share for end-2026 and end-2027.

Base rate: the implied 3.6% nominal growth sits close to the 3.3% real 10-year median net income growth for companies with more than $50bn in sales. Consensus long-term growth of 10.9% is well above that median; over 10 years, only 8.3% of those companies grew real net income 20% a year or more. (Historical base rate: top 1,000 global companies, 1950 to 2015, inflation-adjusted. Not a current fact.)

## The three drivers
ROTCE is about twice the assumed cost of equity, so growth in earnings and in the equity base is what moves value.

1. **Net interest income.** Management's central case for 2027 NII excluding Markets is $107bn, about $5bn above the annualised Q4 2026 guide of $25.5bn a quarter. About a quarter of that growth depends on the rate hikes in the forward curve: one in December 2026 and two in the first half of 2027 [1]. Management also said 2026 NII would be $106.2bn, raised from $105.5bn [3]. The risk runs both ways with the rate path. Dimon said there is "more uncertainty around that number than normal" [1].
2. **Markets and investment banking activity.** In Q3, equities revenue rose 49% and FICC (fixed income, currencies and commodities) revenue fell 4%. Investment banking fees rose 14%, but "evolving market conditions have recently slowed activity a bit" [1]. Commercial & Investment Bank net income rose 20% to $8.2bn [1]. The risk runs lower: this is peak-type activity, and Dimon said "we just don't know when it's going to stop" [2].
3. **Expenses.** Q3 expenses were $27.3bn, up 12% year on year; Q4 is guided at about $27.5bn. Management called the roughly $114bn 2027 consensus "not too far off", with the budget unfinished and AI spending flagged as a variable [1]. Morgan Stanley expects 2027 EPS consensus to rise about 4% because the NII outlook went up while consensus expenses did not [4]. The risk is that expenses get reset higher in January.

## Risks and what would change the view
- **Credit turns.** Card net charge-offs are guided at about 3.2%, and Q3 included a $539m reserve build [1]. Early signal: card net charge-offs above 3.2% in the Q4 print, or larger reserve builds.
- **Capital pressure from rising rates.** The CET1 capital ratio fell 30bp to 13.9%, as unrealised bond losses (OCI) and higher risk-weighted assets outweighed earnings [1]. Early signal: CET1 falling further or a slower buyback pace.
- **AI agents and cyber threats.** In Q3 Q&A, analyst Mike Mayo asked whether AI agents could pull deposits out of the bank, and Dimon said regulators should be preparing for it [1]. Large US banks reportedly detected unauthorized AI agents inside customer accounts this week [7]. Early signal: consumer deposit growth, which was 4% year on year in Q3 [1], slowing.
- **More positive if:** January confirms 2027 NII at or above $107bn, with expenses at or below about $114bn.
- **More negative if:** 2027 expense guidance comes in above $114bn, Markets revenue falls year on year, or the forward curve drops the expected rate hikes.

Media sentiment over 90 days is -0.16 against a -0.13 baseline, mildly worse. Media attention is high: 2.07 standard deviations above its quarterly norm [8]. The stock is down 6.9% over three months and 9% below its 12 Aug record close of $365.18 [6].

## Next date
Q4 2026 results and the 2027 outlook (expense guide, NII refinement): 14 Jan 2027, 8:30 a.m. ET (Data).

**Gaps:** Bigdata.com did not return 30-day consensus revisions or the current 10-year Treasury yield, so the cost of equity is assumed and shown as a range. The reason for the high Q2 2026 EPS ($7.70) was not checked.

## Sources
[1] [JPMorgan Chase & Co.: Q3 2026 Earnings Call - Oct 13, 2026 (FactSet Transcripts)](https://app.bigdata.com/documents/03E0A18161F6E16AA00C64F04D0A3AB5)
[2] [JPMorgan CEO Jamie Dimon Sounds Alarm on Inflation, Rising Rates and Economic Risks - Benzinga, Oct 13, 2026](https://app.bigdata.com/documents/92C3559BF65CFBC52DEB56620A734EB6?cnum=1)
[3] [Top Midday Stories: JPMorgan Shares Rise Despite Q3 Miss - MT Newswires, Oct 13, 2026](https://app.bigdata.com/documents/BA4CAEED06C3A075BFB0BD4EE252B25B?cnum=1)
[4] [JPMorgan price target raised to $377 from $370 at Morgan Stanley - The Fly, Oct 14, 2026](https://app.bigdata.com/documents/21BE87F07E96044BFE70CF2E6FE322DF?cnum=1)
[6] [Is JPMorgan Chase Stock a Buy 8% Below Its Record High? - The Globe And Mail, Oct 18, 2026](https://app.bigdata.com/documents/E1B48EF58901C692B5B3448D892DDEC4?cnum=1)
[7] [Bitcoin's Rally Hits 3 Roadblocks - Benzinga, Oct 23, 2026](https://app.bigdata.com/documents/6E5E82D22A5EA48AFF7A3DC078E7AEC3?cnum=2)
[8] Bigdata.com sentiment tearsheet for JPMorgan Chase, 90-day lookback, retrieved Oct 23, 2026

Data: Bigdata.com company tearsheet for JPMorgan Chase (FactSet price, fundamentals and consensus estimates; FMP analyst targets and earnings; Quartr corporate calendar), retrieved Oct 23, 2026.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

Do you want me to add JPM to a Bigdata.com watchlist?
