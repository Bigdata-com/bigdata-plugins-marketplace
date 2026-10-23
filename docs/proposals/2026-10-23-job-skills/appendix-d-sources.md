## Appendix D. Sources

### Data

- Mixpanel, skill runs by skill slug, 10 September to 13 October 2026. Counts cover the 2.6 percent of Bigdata.com calls that carry a `plugin_slug`, so each figure is a floor.
- Production search topic model, 568,383 searches from the search agent, 22 September to 22 October 2026, 338 topics in 16 use cases. Caveats: no user identifiers, many queries are written by upstream agents rather than people, and one week of data was clustered.
- Bigdata.com company tearsheet for Micron Technology, 23 October 2026, used to confirm the fields the method files rely on (FactSet fundamentals for five periods per call, consensus to FY2030 with actuals and surprise, guidance where the company gives it, 13F holders, segments, targets, next report date). Fields not available: WACC, short interest, options data.
- Bigdata.com search tests on Micron, 23 October 2026: research notes carry sell-side reactions; guidance for a quarter is found on the previous quarter's call with the reporting-period filter set.

### Method sources (the extraction notes cover these in full)

- Michael Mauboussin and co-authors, Credit Suisse and Legg Mason papers: The Base Rate Book (2016) and its sales growth, earnings growth and gross profitability editions (2015 to 2016); How to Model Reversion to the Mean (2013); What Makes for a Useful Statistic (2016); Calculating ROIC; Estimating the Cost of Capital; Economic Returns, Reversion to the Mean and TSR; Measuring the Moat; Managing the Man Overboard Moment (2015); Celebrating the Summit (2016); A Long Look at Short-Termism (2014); Cultivating Your Judgment Skills (2013); Expectations Investing (CFA Institute, 2006); What Does a Price-Earnings Multiple Mean? (2014); the capital allocation, operating leverage, total addressable market and profit pool papers.
- Robinson and Weyns, UBS: How to analyse and talk the language of multiples (2017); When DCF valuation goes rogue, Episodes I and II (2017).
- Koller, Goedhart and Wessels, Valuation: Measuring and Managing the Value of Companies, fifth edition (McKinsey).
- Graham and Dodd, Security Analysis, sixth edition.
- Klarman, Margin of Safety (1991).
- Damodaran, Return on Capital, Return on Invested Capital and Return on Equity: Measurement and Implications (2007).

### Host documentation checked on 2026-10-23

- Agent Skills specification: https://agentskills.io/specification
- Claude skills, plugins, directory and evals: https://code.claude.com/docs/en/skills, https://code.claude.com/docs/en/plugins-reference, https://code.claude.com/docs/en/plugin-evals, https://code.claude.com/docs/en/mcp, https://claude.com/docs/skills/how-to, https://claude.com/docs/plugins/platform-support, https://claude.com/docs/plugins/pre-submission-checklist, https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
- claude.ai server instructions: https://github.com/anthropics/claude-ai-mcp/issues/93 (a canary test, not Anthropic documentation)
- OpenAI plugins and skills: https://developers.openai.com/plugins/build/skills, https://developers.openai.com/plugins/build/mcp-server, https://developers.openai.com/plugins/deploy/submission, https://developers.openai.com/plugins/deploy/submission-errors, https://learn.chatgpt.com/docs/build-skills
- OpenAI's own finance plugin, the router pattern: https://github.com/openai/plugins/tree/main/plugins/public-equity-investing
- Microsoft 365 Copilot Cowork plugins and declarative agents: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development, https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-skills, https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-manifest-1.9

### Earlier work this proposal builds on

- The onboarding plan of 21 October 2026 and its verdicts (skills are guidelines, no Buy/Hold/Sell, the set of eight as a starting point): https://claude.ai/artifact/HNEgzgUaizVqYBi6TZBFUo
- Session one of the rewrite: the `bigdata` entry skill, `references/working-with-bigdata.md`, the eval runner and its six cases, on the branch `worktree-bigdata-any-prompt`.
- The skills deep-dive research of 14 October 2026 (audit of the 27 skills, official guidance, peer skills from OpenAI, Fiscal.ai, Daloopa and S&P, usage data, delivery patterns) and the skills-mechanics research of 20 October 2026 (Claude, ChatGPT and Codex, Grok, Copilot, Gemini, Perplexity).
