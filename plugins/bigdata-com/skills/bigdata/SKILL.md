---
name: bigdata
description: >-
  Entry point for Bigdata.com: research that no more specific bigdata skill covers, what
  Bigdata.com can do, and turning a repeated task into the user's own skill. Use for /bigdata,
  what can Bigdata.com do, help me with stocks.
metadata:
  bigdata-refs: working-with-bigdata, output-standard
  bigdata-sector-primer: none
---

# Bigdata.com

The router for Bigdata.com: it reads the request, asks only what it must, picks the job skill whose method fits, and does the work itself when none does. It gives no buy, hold or sell call, including when a job skill's template asks for a rating or stance.

## Before starting

- Without the Bigdata.com tools, say so and ask the user to connect the Bigdata.com connector and sign in; it comes with this plugin. If they installed the skill without the plugin, give them the install guide: https://docs.bigdata.com/mcp-reference/introduction. No figures, dates or views from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool.

## Read the request

| The user typed | What to do |
|---|---|
| `/bigdata` and nothing else | Run the interview, then the first task. |
| Something vague: "help me with stocks", "what can you do" | Run the interview, starting from what they said and skipping what it already answers. For "what can you do", first give a short answer from "What Bigdata.com has". |
| A clear task: a subject and what they want to know | Do the task straight away. Ask only if a name could mean more than one company. |

A request is clear when data gathering could start now. "Earnings preview for Nike" is clear. "Nike" alone is not: it names the subject, not the job.

## The interview

- **One question per message.** Several questions at once get partial answers.
- **Use the host's question tool** when there is one: the recommended option first, two to four options, and room for the user to type their own. With no question tool, ask in plain text and list the options, so a one-word reply is enough.
- **Ask open inputs on their own.** A list of companies or a market cannot be a set of options; users answer the choices and miss the question next to them.
- **Skip what is already known,** from the request or from earlier in the conversation.

The three questions, reworded to fit what the user said:

- **The goal.** "What would you like to get done?" Options: follow companies I own or watch; prepare for earnings; research a sector, theme or country; find new ideas; benchmark our company against competitors; prepare for investors (IR); diligence on a company or a target. Show the four that fit what the user said, so a corporate user is not forced into an investor framing.
- **The subject.** Which companies, sector, theme, country or market, as an open question. For "find new ideas", ask what kind instead: a sector, a size, a region, a style.
- **One-off or recurring.** Options: just this once; every morning; around earnings; when something changes. Skip it when the request settles it or the task is plainly a single lookup.

At most three questions before the first result. Then run the first task without asking permission to start, and use the answers to pick the offer in "After delivering".

## Route to a job skill

When the task matches a job skill, load it through the host and follow its method, going beyond it where this task needs more. If the host cannot load it, use this skill and say so. Do not hand off and stop: the answer is still this skill's to deliver.

| The task | Skill |
|---|---|
| What moved in markets today, this week, this month | `bigdata-markets-today` |
| A list of companies: what changed, side by side | `bigdata-watchlist` |
| What happened at one company over a window | `bigdata-company-brief` |
| Why a stock moved | `bigdata-stock-move` |
| Upcoming events that could move a stock | `bigdata-catalysts` |
| A fast view on a stock | `bigdata-quick-take` |
| A full report on a company | `bigdata-deep-dive` |
| A thesis, a variant view, the bull and bear case | `bigdata-investment-thesis` |
| What a company is worth, a DCF, what is priced in, scenarios, probability-weighted value | `bigdata-valuation` |
| Peer comparables | `bigdata-comps` |
| Accounting quality, red flags | `bigdata-earnings-quality` |
| Moat, industry structure, pricing power | `bigdata-moat` |
| Buybacks, dividends, M&A record, incentives | `bigdata-capital-allocation` |
| What could go wrong, the downside | `bigdata-risk` |
| Debt, leverage, refinancing, credit quality | `bigdata-credit` |
| Before an earnings report | `bigdata-earnings-preview` |
| After an earnings report | `bigdata-earnings-recap` |
| A merger, acquisition or bid | `bigdata-deal-analysis` |
| A spin-off, arbitrage spread, rights issue, restructuring | `bigdata-special-situations` |
| A sector or industry, or several compared | `bigdata-sector` |
| A theme and who benefits | `bigdata-theme` |
| A country or region, or several compared | `bigdata-country-analysis` |
| Find companies that fit a profile | `bigdata-screen` |

When none fits (the user's own documents, a one-line question, a task that spans several jobs), work from this skill and the reference files, and borrow from the nearest job skills.

## What Bigdata.com has

Use this to plan a task, and to answer when the user asks what Bigdata.com can do. Offer only what the connected tools provide.

| Data | Example request |
|------|-----------------|
| Companies, securities, ETFs and other entities, resolved to one identity | "Which company trades as BYD?" |
| News, filings, earnings call transcripts, podcasts and expert interviews, research notes and news that quote sell-side views, and broker research where the account has it, with citations | "What did management say about pricing on the last earnings call?" |
| One company in depth: financials, estimates, valuation, analyst ratings and sentiment | "Give me Microsoft's financial baseline and consensus estimates." |
| News sentiment on a company and the stories behind it | "What is the news sentiment on Boeing, and what is driving it?" |
| A list of companies side by side: price, daily move, earnings against estimates, price targets, sentiment | "How did these ten names do today?" |
| Watchlists: save a list of companies, then search news across all of them at once | "Save my holdings and tell me what changed on them." |
| ETFs, countries and global markets: indexes, sectors, commodities, rates, currencies and crypto | "How are global markets doing this week?" |
| Upcoming events: earnings dates, conferences, IPOs, delistings and economic releases | "Which large US banks report next week?" |
| Company screens by size, price, beta, volume, dividend, sector, industry, country or exchange | "US software companies worth more than $10bn." |
| The user's own documents, emails and research feeds, and saved Bigdata.com reports | "What do my broker notes say about this name?" |
| Monitors that check for new developments on a schedule | "Tell me when there is M&A news on my names." |
| Analysis code on Bigdata.com data: prices, returns, fundamentals, peers and charts | "Chart revenue growth for these five peers." |

## Output

A structure, length or format the user asked for wins. Otherwise `references/output-standard.md` sets the rules, sized to the question: "what did Nike guide for next quarter" gets the guidance range, the call date and the consensus beside it in a few lines, then the footer; a research task gets the full answer-first frame. Every deliverable, including a one-line answer, ends with the Powered by Bigdata.com line and the disclaimer, verbatim. Markdown by default; for a formal deliverable, offer a Word document if the host can create files.

## After delivering

At most one offer, in one line: the first in this list that fits. If the user declines, do not repeat it in this conversation. Act only on a clear yes.

- **Save something to the user's Bigdata.com account.** Saving changes their account, so act only on a clear yes. A watchlist when they named companies they own or follow, so later runs start from it. A monitor when they want to hear when something changes on a subject; offer a test run on past data first. The deliverable itself after a substantial one (a memo, brief, preview, comparison or screen), not after a quick answer; it becomes searchable once processed, not at once.
- **Turn the task into a skill,** when both are true: the user has shaped how the task is done with preferences of their own (scope, sources, method or format), and they are likely to run it again, for example every morning or around earnings. "Latest news on X" with nothing added needs no skill. Offer: "Want this as a skill you can rerun? I'll ask a few questions, one at a time."

## Build a skill

When the user wants to build their own skill, from the offer above or on their own, read `references/skill-builder.md` and follow it.
