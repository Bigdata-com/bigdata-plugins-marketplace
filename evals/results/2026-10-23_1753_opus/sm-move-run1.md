# sm-move#1

USER: Why did Micron move this week?

  [tool call] Skill {"skill": "bigdata-com:bigdata-stock-move", "args": "Micron (MU) - why did it move this week (week of 2026-10-19 to 2026-10-23)"}

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet,mcp__claude_ai_Bigdata_com__bigd

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-stock-move/references && ls && cat working-with-bigdata.md output-standard.md", "description": "Read skill reference files"}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU", "plugin_slug": "bigdata-stock-move"}

  [tool call] Bash {"command": "cd /Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-stock-move/references && cat after-a-price-move.md", "description": "Read base-rate reference file"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["company_overview", "analyst_ratings", "latest_earnings", "earnings_calendar", "analyst_estimates"], "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_market_tearsheet {"plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron Technology stock move this week? News on Micron shares this week", "max_chunks": 25}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-o8yc9klr/5a55b49d-bf2d-4bd7-913d-9888aa142748/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792438378.txt\njq -c '.company_overview, .analyst_data, .price

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\nhelp(client)", "intent": "List the data client methods to find daily price series", "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "from bigdata_data import client\ne = client.find.etfs('SPDR S&P 500 ETF', limit=3); print(e[['key','name','ticker']])\nspy = e.iloc[0]['key']\nmu = client.price.daily('49BBBC','2026-10-09','2026-10-23')\nprint(mu[['date','close','change_percent','close_to_close_return_percent','volume']].t

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_computer {"code": "import numpy as np\nm = mu.set_index('date')['close']; s = sp.set_index('date')['close']\nb=2.226\nwk_m = m['2026-10-23']/m['2026-10-16']-1; wk_s = s['2026-10-23']/s['2026-10-16']-1\nprint(f\"week MU {wk_m*100:.2f}  SPY {wk_s*100:.2f}  rel {(wk_m-wk_s)*100:.2f}  beta-adj {(wk_m-b*wk_s)*100

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Analyst price target changes and rating changes on Micron Technology this week", "max_chunks": 20}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Micron Technology company announcements, 8-K filings and press releases this week", "max_chunks": 15}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron and memory chip stocks rise on Monday October 19 2026?", "max_chunks": 12}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "fast", "query": {"text": "analyst raises or lowers Micron price target, maintains rating", "filters": {"entity": {"search_in": "ALL", "all_of": ["49BBBC"]}, "keyword": {"search_in": "ALL", "any_of": ["price target", "price forecast", "downgrade", "upgrade"]}, "timestamp"

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-o8yc9klr/5a55b49d-bf2d-4bd7-913d-9888aa142748/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792792438378.txt\njq -r '.estimates.records[] | select((.metric==

ASSISTANT: I am pulling Micron's daily closing prices for the week to settle the size of the move, because the tearsheet's price data stops at Thursday's close.

# Micron (MU): flat for the week, down 0.15 percent on Oct 19 to 23, 2026, up 0.28 percent against the S&P 500

Data as of: prices at the close on Oct 23, 2026; estimates from the FactSet consensus in the Bigdata.com tearsheet, retrieved Oct 23, 2026; newest document Oct 23, 2026.

## What happened

Micron ended the week almost where it started. It closed at $878.84 on Friday Oct 16 and at $877.55 on Friday Oct 23, a change of -0.15 percent. The S&P 500 ETF (SPY) fell 0.43 percent over the same days. The week looks calm only because the daily moves cancelled out: +3.0, -1.0, +2.0, -6.3 and +2.5 percent (derived from daily closes).

The one large move was Thursday Oct 22, when the stock fell 6.26 percent while the S&P 500 fell 1.18 percent. The cause was a market-wide selloff in technology stocks, not news about Micron. Investors were worried that the large technology companies are spending too much on AI. Meta's planned capital spending of $135 to $145 billion, rising oil prices and rising interest rates added to that worry [1][2][3]. Other memory stocks such as SK hynix and Western Digital fell on the same day [4].

Analysts did not change their view during the week. Every target change found in the sources was a reiteration, and none was cut. Because the move against the index was under 5 percent, the historical base-rate tables for large one-day moves do not apply.

## The trigger, day by day

| Date | MU close-to-close | SPY | Event | Basis | Source |
|---|---|---|---|---|---|
| Mon Oct 19 | +2.97% | +0.42% | Memory and chip stocks rebounded after the previous week's selloff. Bernstein said demand remains "extremely strong" but that memory price increases are no longer accelerating. | reported | [5][6] |
| Tue Oct 20 | -0.98% | +0.34% | Cantor Fitzgerald kept its Overweight rating and $2,000 target. Micron invested an undisclosed sum in Indium Corp for critical-minerals processing. | reported | [7][8] |
| Wed Oct 21 | +1.96% | +0.53% | Micron held a technology webinar with its CTO, Scott DeBoer. Micron said it has dropped the 4F DRAM cell design that its rivals Samsung, SK hynix and CXMT are developing. | reported | [9][10] |
| Thu Oct 22 | -6.26% | -1.18% | Tech-led selloff over AI spending, rates and oil. A union at Micron's Taoyuan plant in Taiwan planned a 24-hour strike over profit-sharing. Micron announced a quarterly profit-linked bonus for all employees. | reported | [1][2][3][11][12] |
| Fri Oct 23 | +2.46% | -0.52% | Chip stocks rebounded. Wedbush ($1,400) and BNP Paribas ($1,700) kept their Buy-equivalent ratings. | reported | [13][14][15] |

Price returns are from Bigdata.com daily price data.

Thursday's drop was 5.08 percentage points worse than the index. Adjusted for Micron's beta of 2.23 (the stock tends to move about 2.2 times as much as the market), the gap was 3.63 points (derived). Using the same beta adjustment, the stock did 0.81 points better than the index over the whole week (derived). Benzinga reported that Micron fell 3.08 points more than the technology sector ETF (XLK) on Thursday [1]. That suggests some selling specific to memory stocks on top of the broad tech selling. The Taiwan strike headline and the profit-sharing cost are the only Micron-specific items found that day [1][11]. A Trendforce analyst quoted by Reuters said a one-day strike would likely have limited effect on supply [1].

## Did the long-term outlook change?

Nothing found this week changes Micron's expected growth, margins or returns.

- **Margins:** The new profit-linked bonus raises labor cost, but no source puts a figure on it [11].
- **Growth:** Micron's own messages to investors this week pointed to tighter supply. Cantor's note says Micron expects 2027 to be tighter than 2026, with the shortage lasting through 2028 [7].
- **What the market is worried about** is the long-term risk that the industry adds too much capacity and memory prices fall, and the risk that AI spending slows. Both concerns were already present before this week [5][18].

The implied-growth calculation was not run because the move is too small to show a change in what the market expects.

## What the estimate-setters did

| Measure | Value | Date | Basis | Source |
|---|---|---|---|---|
| FY2027 EPS consensus (sum of 4 quarters) | $174.64 | Oct 23, 2026 | derived | Data line |
| FY2027 EPS consensus, press figure | $176.50, up from $159.46 a month earlier | Oct 22, 2026 | reported | [16] |
| Q1 FY2027 revenue consensus | $61.6bn, against company guidance of $61.5bn ± $1.5bn | Oct 23, 2026 | reported | Data line |
| Mean / median price target | $1,588.85 / $1,500 (high $3,000, low $1,200) | Oct 23, 2026 | reported | Data line |
| Ratings | 58 Buy, 10 Hold, 2 Sell | Oct 23, 2026 | reported | Data line |
| Target actions in the week | Cantor $2,000, Needham $1,650, Rosenblatt $1,900, RBC $1,500, D.A. Davidson $3,000, Wedbush $1,400, BNP $1,700. All were reiterated; none was raised or cut. | Oct 20 to 23 | reported | [1][7][10][14][15][17] |

The tearsheet gives no history of consensus, so there is no before-and-after value for this week alone. When the price falls while estimates hold or rise, the drop is a change in the valuation multiple or in positioning, not a change in fundamentals. At $877.55 the stock trades at about 5.0 times FY2027 consensus EPS (derived).

## Context beyond the week

The stock fell 20.1 percent in the month to Oct 22 and closed the week 30 percent below its 52-week high of $1,255 (derived). Over the year it is still up 323 percent.

The next dated events are:

- **Dec 9, 2026:** the date from which Micron said it will increase capital returns, under a $35.16bn buyback authorization [7].
- **Dec 16, 2026, after the market close:** Q1 FY2027 results (Data line).

## What would change this view

- Large cloud companies cut their capital spending plans in their Q3 reports, which are due through late October and November.
- The Taoyuan labor dispute leads to a longer strike, or to a profit-sharing settlement that materially raises Micron's cost base [12].
- Memory contract prices stop rising. Bernstein already flagged that price increases are slowing [5].
- Micron's Q1 FY2027 revenue on Dec 16 lands below the $60.0bn low end of its guidance.

## Gaps

- Bigdata.com does not have short interest, options activity or intraday fund flows. These would show whether Thursday's extra selling came from de-risking by hedge funds or long-only investors.
- The sell-side search for rating reports returned no broker documents, so analyst actions come from press summaries.
- No consensus history was available to show revisions within the week.

## Sources

[1] [What's Going On With Micron Technology Stock Thursday? - Benzinga, Oct 22, 2026](https://app.bigdata.com/documents/EA17A0882ED33ACD9316E60BA035DA71?cnum=1&cnum=2&cnum=3&cnum=4)
[2] [Why Micron Stock Is Falling Hard Today - Nasdaq, Oct 23, 2026](https://app.bigdata.com/documents/E8149EE5F1A060C81F5E9A4568A3B2EA?cnum=2&cnum=3&cnum=1)
[3] [Why Micron Stock Dropped on Thursday - The Globe And Mail, Oct 22, 2026](https://app.bigdata.com/documents/DC4AA9FA7048200D4D3EE3310AA93016?cnum=1)
[4] [Micron shares fall along with semiconductor stocks - Edaily, Oct 22, 2026](https://app.bigdata.com/documents/C9E7C1433798DC6CC520660423AD95B9?cnum=1)
[5] [Why Micron and Sandisk Stocks Are Surging Monday - Benzinga, Oct 19, 2026](https://app.bigdata.com/documents/E687BC5A03B7F4B02D2A68F39F331428?cnum=3&cnum=4)
[6] [ICBCI Express Daily 20 October 2026 - ICBC International Research, Oct 20, 2026](https://app.bigdata.com/documents/7FBC3F8D43CBAC2A6F71B561728A04E1?cnum=2)
[7] [Micron Stock Moves Higher: What's Going On? - Benzinga, Oct 20, 2026](https://app.bigdata.com/documents/E09B345294245DA6FA28EA981BA37035?cnum=1&cnum=2)
[8] [Micron expands US critical minerals processing with Indium investment - Alliance News, Oct 20, 2026](https://app.bigdata.com/documents/5EAB61CE6A832D0F3930434AB4A75A53?cnum=1)
[9] [Micron Technology Inc: Investor update on Oct 21, 2026 - Transcript - Quartr, Oct 21, 2026](https://app.bigdata.com/documents/BFCF658D6DA36B05106BF4235A08E18A?cnum=7)
[10] [Micron's Long-Term Memory Strategy Supports Growth Outlook, RBC Says - MT Newswires, Oct 22, 2026](https://app.bigdata.com/documents/30E0629C8ABFFB11B41AC7F7CB408912?cnum=1)
[11] [Market Chatter: Micron Introduces Global Profit-Linked Bonuses After Taiwan Union Demands - MT Newswires, Oct 22, 2026](https://app.bigdata.com/documents/EA137532E74BEC22C9899C60436BD788?cnum=1)
[12] [KB Asia Market Headline - KB Securities, Oct 22, 2026](https://app.bigdata.com/documents/B4607D1C473A69EA37BBD7FF0E41FCFE?cnum=12)
[13] [What's Going On With Micron Technology Stock Friday? - Benzinga, Oct 23, 2026](https://app.bigdata.com/documents/AC0EF03DE76B45F04176A978DEAACDF1?cnum=1&cnum=3&cnum=2)
[14] [Micron Stock Rises as Wedbush Reaffirms $1,400 Price Target - Yahoo! Finance, Oct 23, 2026](https://app.bigdata.com/documents/9AE70B45E4B7F93F1EC6E5370700E842?cnum=1)
[15] [Micron Stocks Rise 3.41% as $1,700 Target Puts Cash Durability in Focus - Yahoo! Finance, Oct 23, 2026](https://app.bigdata.com/documents/0A09EBEBCFAA26B7E0BA516CA1AD194A?cnum=1)
[16] [Micron Technology Has Lost 25% From Its June High: Here's Why Needham Sees 81% Upside - Yahoo! Finance, Oct 22, 2026](https://app.bigdata.com/documents/9EE7E91CFD89B5B9D348518441AFA73D?cnum=1)
[17] [Jensen Huang shouts 'there's no such thing as too much memory' - Anue, Oct 23, 2026](https://app.bigdata.com/documents/0677A153C690441E681ED764B8F8DFF5?cnum=3)
[18] [Micron CTO Downplays New Memory Chip Design as 'Complex and Costly' While Chinese Rival CXMT Advances DRAM Technology - Benzinga, Oct 22, 2026](https://app.bigdata.com/documents/0634A2AB636D58514753B7AE9C4CAB4F?cnum=3)

Data: Bigdata.com company tearsheet for Micron Technology (FactSet prices and consensus estimates, FMP analyst ratings and targets, Quartr corporate calendar), Bigdata.com daily prices for MU and SPY, and the Bigdata.com market tearsheet, all retrieved Oct 23, 2026. Weekly and daily relative returns, the beta-adjusted figures (beta 2.226 from the company profile) and the forward P/E were computed in `bigdata_computer`.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

---

I can set up a Bigdata.com monitor on Micron news for the next two weeks, which covers the cloud-company earnings reports and the Taiwan labor dispute. Do you want me to?
