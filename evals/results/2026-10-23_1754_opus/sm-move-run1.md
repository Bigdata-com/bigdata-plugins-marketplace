# sm-move#1

USER: Why did Micron move this week?

  [tool call] Skill {"skill": "bigdata-com:bigdata-stock-move", "args": "Why did Micron move this week?"}

  [tool call] Bash {"command": "D=/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-stock-move/references; ls $D; cat $D/working-with-bigdata.md $D/after-a-price-move.md $D/output-standard.md", "description": "List and read the 

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet,mcp__claude_ai_Bigdata_com__bigd

  [tool call] Read {"file_path": "/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-c3wa3nif/7c1f6d46-5889-4a47-8efe-6febcff9f110/tool-results/b0dkgxl08.txt"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU", "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["company_overview", "analyst_ratings", "latest_earnings", "earnings_calendar", "analyst_estimates"], "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet {"plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron Technology stock move this week?", "max_chunks": 25}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-c3wa3nif/7c1f6d46-5889-4a47-8efe-6febcff9f110/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792511932.txt\njq -c '.company_overview, .analyst_data, .price

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\nhelp(client)", "intent": "List the price methods available", "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\ne = client.find.etfs('SPDR S&P 500 ETF SPY', limit=5)\nprint(e[['key','name','ticker']].to_string())\ns = client.find.etfs('iShares Semiconductor ETF SOXX', limit=3)\nprint(s[['key','name','ticker']].to_string())\nmu = client.price.daily('49BBBC','2026-10-1

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\nfor q in ['SPY','SOXX']:\n    e = client.find.etfs(q, limit=3)\n    print(q, e.columns.tolist()[:12]); print(e.head(3).to_string()[:1200])\nmu = client.price.daily('49BBBC','2026-10-12','2026-10-23')\nprint(mu[['date','open','close','close_to_close_return_p

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\nids={'MU':'49BBBC','SPY':'672082','SOXX':'9AGK3Q'}\nd={}\nfor k,v in ids.items():\n    p=client.price.daily(v,'2026-10-15','2026-10-23').sort_values('date')\n    d[k]=p.set_index('date')['close']\ndf=pd.DataFrame(d); r=df.pct_change()*100\nprint(df.round(2)

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did semiconductor stocks sell off on Thursday October 22, 2026?", "max_chunks": 15}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Analyst price target and rating changes on Micron Technology this week", "max_chunks": 15}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Taoyuan Taiwan union strike outcome and production impact this week", "max_chunks": 10}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet {"rp_entity_id": "49BBBC", "plugin_slug": "bigdata-stock-move"}

ASSISTANT: Micron's tearsheet stops at Thursday's close: $856.49, down 6.3% that day. I'm now pulling the daily closes for Monday through Friday so the week's move covers the full window.

# Micron (MU): down 0.15% for the week of Oct 19-23, 2026, against down 0.43% for the S&P 500 (SPY) and down 3.08% for semiconductors (SOXX)

Data as of: prices at the Oct 23, 2026 close; analyst ratings and targets Oct 23, 2026; newest document read Oct 23, 2026.

## What happened

Over the week as a whole, Micron barely moved: it closed Friday at $877.55, against $878.84 the Friday before (derived from daily closes). Inside the week it was volatile. It gained 3.0% Monday, rose to $913.67 by Wednesday, fell 6.3% on Thursday and recovered 2.5% on Friday.

Thursday's drop came from a selloff across the whole chip sector, not from news about Micron. Three things started it:
- Lam Research, which makes chip manufacturing equipment, said supply-chain constraints had held back its guidance [3].
- Tesla cut its 2026 capital spending plan, and Meta's AI spending raised new doubts about whether AI investment will pay off [4][5].
- Oil prices and 10-year Treasury yields near 5% added pressure [5].

The PHLX semiconductor index fell 6.7% that day, and all 30 of its members closed lower [6]. Micron fell less than the semiconductor ETF did (6.26% against 6.79%).

Two Micron-specific stories ran alongside. The first was a one-day strike at its Taoyuan plant in Taiwan, which KB Securities says holds about 22% of Micron's DRAM capacity [7]. The second was a new quarterly profit-sharing bonus for staff [8]. Neither appears to have driven the price on its own day.

No analyst cut a rating or a price target this week in the sources I found. The tables of what usually happens after a large drop do not cover a move this size.

## The trigger

| Date | Event | MU | SPY | SOXX | Basis | Source |
|---|---|---|---|---|---|---|
| Mon Oct 19 | Tech stocks bounce after the prior week's chip selloff | +2.97% | +0.42% | +1.73% | reported | [13] |
| Tue Oct 20 | Taoyuan union announces a strike for Oct 22; Micron invests in Indium Corp, a US critical-minerals supplier | -0.98% | +0.34% | -0.38% | reported | [15][7] |
| Wed Oct 21 | Micron reaches a deal with the union at Taichung, its largest Taiwan plant; RBC keeps Outperform with a $1,500 target | +1.96% | +0.53% | +2.07% | reported | [12][11] |
| Thu Oct 22 | Sector-wide chip selloff (Lam Research supply warning, Tesla capital spending cut, Meta spending worries); Taoyuan strike goes ahead | -6.26% | -1.18% | -6.79% | reported | [3][4][6][9] |
| Fri Oct 23 | Chips rebound; SK hynix drops plans to list its flash-memory unit Solidigm in the US, which LYNX says lowers the risk of a NAND flash glut; Taoyuan workers reject the bonus offer | +2.46% | -0.52% | +0.53% | reported | [1][14][10] |

Daily returns come from Bigdata.com price data.

Beta measures how much Micron typically moves when the S&P 500 moves 1%. Over the 60 months to September 2026 it was 2.2 (derived). Adjusting for that, Thursday's drop was 3.7 percentage points worse than the market alone would explain, and the full week was 0.8 points better (derived).

## Headline or outlook

This week's news did not change Micron's long-term growth path, profit margins or capital returns in any way the evidence can measure. The selloff was about investors pricing in a risk that AI spending slows, which hit every chip stock. It was not new information about Micron's own results.

The one item that could affect margins is the new quarterly bonus, starting in fiscal 2027. It is paid out of after-tax profit minus the next quarter's planned capital spending [8], but Micron has not said how large the pool will be, so its effect cannot be calculated. The Taoyuan strike lasted one day. Its effect on output depends on which production lines were staffed [2], and the dispute there is still unresolved [10].

## What the analysts did

| Measure | Value | Date | Basis | Source |
|---|---|---|---|---|
| Ratings | 58 Buy, 10 Hold, 2 Sell | Oct 23 | reported | tearsheet |
| Average price target | $1,588.85 (median $1,500, range $1,200-$3,000) | Oct 23 | reported | tearsheet |
| Changes this week | RBC kept Outperform and $1,500 (Oct 22); Rosenblatt kept Buy and $1,900, and Needham kept Buy and $1,650 (Oct 22) | Oct 22 | reported | [11][1] |

Bigdata.com does not keep a history of consensus estimates, so I could not compare earnings forecasts before and after the week. No cuts to estimates were reported.

## What history says

The historical tables available to this method come from two Credit Suisse studies. They cover one-day moves of 10% or more against the index. Thursday's 6.3% drop (3.7% after adjusting for beta) is below that threshold, so no row applies directly.

The nearest row is a drop with no earnings report behind it, in a stock that had strong momentum going in. Micron qualifies: it was up 323% over the past year to Oct 22 (reported). That row has 1,041 cases from 1990 to mid-2014, and on average those stocks beat the index by 3.7%, 4.9% and 6.2% over the next 30, 60 and 90 trading days. This is a historical average for a larger move than Micron's, not a forecast. Outcomes in those studies varied by 32 to 47 percentage points either way.

## Floors and the next date

- Selling came from investors cutting their exposure to the AI-infrastructure trade: SOXX is down 16% since the start of October [4].
- Micron's next earnings report is Q1 FY2027 on Dec 16, 2026, after the market closes (tearsheet).
- Before then, the next test is Alphabet, Microsoft and Amazon earnings next week, when they update their AI capital spending plans [6].

## What would change this view

- Those three companies confirm or cut their AI capital spending.
- The Taoyuan dispute spreads to Taichung, which KB Securities describes as a key site for high-bandwidth memory [7].
- Micron discloses the cost of the new bonus pool.
- The Dec 16 guidance.

## Gaps

- Short interest, options positioning and intraday trading flows are not in Bigdata.com.
- The consensus estimate history is not available, so I could not show estimate changes before and after the week.
- I found no broker research notes dated this week. Analyst actions come from news reports.

## Sources

[1] [What's Going On With Micron Technology Stock Friday? - Benzinga, Oct 23, 2026](https://app.bigdata.com/documents/AC0EF03DE76B45F04176A978DEAACDF1?cnum=1&cnum=3&cnum=2)
[2] [What's Going On With Micron Technology Stock Thursday? - Benzinga, Oct 22, 2026](https://app.bigdata.com/documents/EA17A0882ED33ACD9316E60BA035DA71?cnum=1&cnum=2)
[3] [Chip stocks fall as equipment maker Lam Research cites 'supply chain constraints' - Yahoo! Finance, Oct 22, 2026](https://app.bigdata.com/documents/DA46476DD0BEEE73EADFD4D934C37CD6?cnum=1)
[4] [3 reasons for the sharp drop in semiconductor stocks - Money Today, Oct 23, 2026](https://app.bigdata.com/documents/8089003ACBBA959B4C4D6ED9F6DDEDAE?cnum=1)
[5] [The Dow plunges 500 points as fears of renewed Middle East fighting send oil soaring - Business Insider, Oct 23, 2026](https://app.bigdata.com/documents/A26E3B1A63B81ED4C521060577386337?cnum=3)
[6] [Will the China-South Korea "Great Miracle Day" awaken the semiconductor bull market narrative? - Flush Financial, Oct 23, 2026](https://app.bigdata.com/documents/11CD7D011D12565B863D0EEDB08EBF22?cnum=2)
[7] [Semiconductor - Micron Union Announces Strike; Spillover Benefits Expected - KB Securities, Oct 21, 2026](https://app.bigdata.com/documents/A71AF35EB152BF77B4D4F583BE11EC32?cnum=2)
[8] [Market Chatter: Micron to Boost Employee Incentives After Taiwan Union Talks - MT Newswires, Oct 23, 2026](https://app.bigdata.com/documents/5C5C3943EF023C012F383FBF273746F2?cnum=1)
[9] [Micron labor union stages Taiwan's first-ever industry strike, Nikkei Asia says - The Fly, Oct 23, 2026](https://asia.nikkei.com/business/tech/semiconductors/taiwan-s-first-ever-chip-workers-strike-begins-at-micron-plant)
[10] [Taiwan: employees at Micron's Taoyuan plant reject proposed bonus - Mediapart, Oct 23, 2026](https://www.mediapart.fr/journal/fil-dactualites/231026/taiwan-les-salaries-de-l-usine-micron-de-taoyuan-rejettent-la-prime-proposee-selon-leur-syndicat)
[11] [Micron's Long-Term Memory Strategy Supports Growth Outlook, RBC Says - MT Newswires, Oct 22, 2026](https://app.bigdata.com/documents/30E0629C8ABFFB11B41AC7F7CB408912?cnum=1)
[12] [Sector Update: Tech Stocks Rise Premarket Wednesday - MT Newswires, Oct 21, 2026](https://app.bigdata.com/documents/E5BBE3E06FC95CD232567E3F866C4BA6?cnum=1)
[13] [CNBC Daily Open: Tech investors buy the dip - CNBC, Oct 20, 2026](https://app.bigdata.com/documents/02C89C6A8F6A2271174D771A71698087?cnum=2)
[14] [Analyst: SK hynix abandoning Solidigm US IPO plan may benefit Micron - Wallstreetcn, Oct 23, 2026](https://wallstreetcn.com/livenews/3184957)
[15] [NEW YORK MARKET CLOSE: Dow, S&P higher as Wall Street digests earnings - Alliance News, Oct 20, 2026](https://app.bigdata.com/documents/9CA5B15FE571840EE7F2D4396AFFE4CF?cnum=5)

Data: Bigdata.com company tearsheet for Micron (FactSet prices, FMP ratings and targets, Quartr earnings calendar), market tearsheet, and daily prices for MU, SPY and SOXX from bigdata_computer, retrieved Oct 23, 2026.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

---

Do you want me to set up a Bigdata.com monitor on Micron news for the next two weeks? It would cover the Taiwan labor talks and the hyperscaler capital spending updates.
