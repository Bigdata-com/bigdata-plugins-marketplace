# sm-move#1

USER: Why did Micron move this week?

  [tool call] Skill {"skill": "bigdata-com:bigdata-stock-move", "args": "Why did Micron move this week?"}

  [tool call] Bash {"command": "cat \"/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal/plugins/bigdata-com/skills/bigdata-stock-move/references/working-with-bigdata.md\"", "description": "Read the Bigdata.com working reference"}

  [tool call] ToolSearch {"query": "select:mcp__claude_ai_Bigdata_com__find_securities,mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet,mcp__claude_ai_Bigdata_com__bigdata_search,mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet", "max_results": 4}

  [tool call] mcp__claude_ai_Bigdata_com__find_securities {"query": "MU", "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_company_tearsheet {"rp_entity_id": "49BBBC", "company_type": "Public", "sections": ["company_overview", "analyst_ratings", "analyst_estimates", "latest_earnings", "earnings_calendar", "key_metrics"], "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Why did Micron Technology stock move this week?", "max_chunks": 25}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_search {"request": {"search_mode": "smart", "query": {"text": "Analyst price target and rating changes on Micron Technology this week", "max_chunks": 20}}, "plugin_slug": "bigdata-stock-move"}

  [tool call] mcp__claude_ai_Bigdata_com__bigdata_sentiment_tearsheet {"rp_entity_id": "49BBBC", "plugin_slug": "bigdata-stock-move"}

  [tool call] Bash {"command": "F=/Users/mkangrga/.claude-work/projects/-private-var-folders-90-45dhw1s97jz5923f1-yhcdf00000gp-T-bigdata-eval-26e4dxtm/144301fb-aec1-495a-abb8-525ee54fafd4/tool-results/mcp-claude_ai_Bigdata_com-bigdata_company_tearsheet-1792791729813.txt\njq -c '.company_overview, .price_performance, .

ASSISTANT: Micron's price data and the news for the week are in. Here is the summary.

# Micron (MU): a volatile week, mainly driven by a sector selloff on Thursday

**Data as of:** Bigdata.com's price feed ends at the Thursday, October 22 close. Friday's figures below come from intraday news reports, not a closing price.

## What happened

Micron did not have its own catalyst this week. The stock moved with a broad selloff in chip and AI stocks, and a labor dispute in Taiwan added some pressure.

- **Day by day:**
  - Monday: up about 3%, when tech stocks bounced back from the previous week's fall.
  - Tuesday: down 1.0%.
  - Wednesday: up more than 3% before the open, after Micron agreed a deal with the union at its Taichung plant in Taiwan, its largest site there.
  - Thursday: down 6.26% to $856.49.
  - Friday: up about 3.5% to around $887 by midday.
- **Thursday was the main move.** Two things drove it:
  - Investors worried that big tech companies are spending too much on AI. Meta's results beat estimates, but it also announced $135 to $145 billion of capital spending, and the market reacted badly. Nvidia's CEO also said capital for AI cloud expansion is scarce.
  - Rising interest rates and inflation weighed on all tech stocks. The Nasdaq fell 2.59% and the tech sector ETF (XLK) fell 3.15%.
- **Micron fell harder than the sector on Thursday,** by about 3 percentage points. The likely company-specific reason is that the union at Micron's Taoyuan plant in Taiwan held a 24-hour strike over profit-sharing. It was reported as the first chip-industry strike in Taiwan. Micron responded by announcing a global quarterly bonus tied to profits, paid half in cash and half in stock, plus higher pension contributions in Taiwan. The Taoyuan union then rejected the bonus offer, and talks continue.
- **Friday's rebound** came as chip stocks recovered across the sector. SK hynix also cancelled the planned US IPO of its flash-memory unit Solidigm. One analyst firm (LYNX) said that lowers the risk of too much flash-memory supply in future, which helps Micron.

## Bigger picture

- Over the 5 trading days to Thursday, the stock fell 8.0%. Over one month it is down 20.1%.
- It is still up 323% over one year and well below its 52-week high of $1,213.56.
- This week continues a pullback that began after Micron's September 30 earnings. Those results beat estimates: revenue was $54.2 billion against $51.3 billion expected, and EPS was $33.42 against $31.77 expected. The stock fell anyway.

## What analysts did

I found no rating downgrades or target cuts this week. Several firms kept their Buy-type ratings and targets:
- RBC: Outperform, $1,500 target (October 22).
- Rosenblatt: Buy, $1,900 target.
- Needham: Buy, $1,650 target.

The overall picture is 58 Buy, 10 Hold and 2 Sell ratings, with an average target of $1,588.85. So the price fell while analysts' views stayed the same. That points to investors paying less for the stock because of sector-wide fear, not to analysts cutting their forecasts.

## Next date

Micron's fiscal Q1 2027 earnings call is on December 16, 2026.

## Gaps

- I don't have the closing price from Friday, October 16, so I can't give an exact Monday-to-Friday change. I also can't compare the full week to the index.
- I didn't check whether consensus estimates changed during the week, or pull a historical comparison for moves like this one.
- Bigdata.com does not have short interest, detailed options data or intraday trading flows.

## Sources (via [Bigdata.com](https://bigdata.com))
1. Company tearsheet: prices, ratings and estimates from FactSet and FMP, as of October 22–23, 2026
2. [Benzinga, "What's Going On With Micron Technology Stock Thursday?", Oct 22](https://app.bigdata.com/documents/EA17A0882ED33ACD9316E60BA035DA71?cnum=1&cnum=2)
3. [Nasdaq/Motley Fool, "Why Micron Stock Is Falling Hard Today", Oct 22](https://app.bigdata.com/documents/E8149EE5F1A060C81F5E9A4568A3B2EA?cnum=2&cnum=1)
4. [Benzinga, "What's Going On With Micron Technology Stock Friday?", Oct 23](https://app.bigdata.com/documents/AC0EF03DE76B45F04176A978DEAACDF1?cnum=1&cnum=3&cnum=2)
5. [MT Newswires, Micron employee incentives after Taiwan union talks, Oct 23](https://app.bigdata.com/documents/5C5C3943EF023C012F383FBF273746F2?cnum=1)
6. [MT Newswires, tech stocks before the open, Taichung union deal, Oct 21](https://app.bigdata.com/documents/E5BBE3E06FC95CD232567E3F866C4BA6?cnum=1)
7. [MT Newswires, RBC note, Oct 22](https://app.bigdata.com/documents/30E0629C8ABFFB11B41AC7F7CB408912?cnum=1)
8. [CNBC Daily Open, Oct 20](https://app.bigdata.com/documents/02C89C6A8F6A2271174D771A71698087?cnum=2) and [Alliance News market close, Oct 20](https://app.bigdata.com/documents/9CA5B15FE571840EE7F2D4396AFFE4CF?cnum=5)
9. Bigdata.com sentiment tearsheet: sentiment is -0.28 against a baseline of -0.20, and still falling

Powered by [Bigdata.com](https://bigdata.com). This is for information only and is not investment advice.

Would you like me to set up a Bigdata.com monitor on Micron news for the next two weeks? It would mainly catch updates on the Taoyuan strike talks.
