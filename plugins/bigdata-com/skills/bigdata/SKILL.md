---
name: bigdata
description: >-
  Bigdata.com research on companies, markets and economies. Use when the user types /bigdata,
  names Bigdata.com, asks what it can do, brings a financial research task, or wants their own
  research skill. With no clear task, it interviews the user first.metadata:
  bigdata-refs: working-with-bigdata, output-standard
  bigdata-sector-primer: none
---

# Bigdata.com

This is the Bigdata.com skill `bigdata`. Pass `plugin_slug: "bigdata"` on every Bigdata.com call that accepts it.

Treat this skill as guidelines, not a script. Skip any step that does not apply to the task at hand, except the connection check below and the footer in Output. Research further whenever the task needs it to be thorough and accurate.

## Before starting

If the Bigdata.com tools are not available in this conversation, say so and ask the user to connect the Bigdata.com connector and sign in: it comes with this plugin. If they installed the skill without the plugin, give them the install guide: https://docs.bigdata.com/mcp-reference/introduction. Do not answer from memory or web search instead, unless the user asks for that: an unsourced answer looks like Bigdata.com data and is not.

Before the first Bigdata.com call, read [references/working-with-bigdata.md](./references/working-with-bigdata.md): which data answers which question, resolving companies, searching well, retrying a weak search, when to read a full document, and when to offer saving.

## Read the request

| The user typed | What to do |
|---|---|
| `/bigdata` and nothing else | Run the interview (below), then the first task. |
| Something vague: "help me with stocks", "what can you do" | Run the interview, starting from what they said and skipping what it already answers. For "what can you do", first give a short answer from "What Bigdata.com has". |
| A clear task: a subject and what they want to know | Do the task straight away (see "Do the task"). Ask only if a name is ambiguous. |

A request is clear when data gathering could start now. "Earnings preview for Nike" is clear. "Nike" alone is not: it names the subject, not the job.

## The interview

Learn enough to do something useful, then do it. The interview is done when the job and the subject are known, usually after two or three questions.

How to ask:

- **One question per message.** Wait for the answer before the next one; several questions at once get partial answers.
- **Use the host's question tool** when there is one (a tool that shows the user choices to pick from). Put the recommended option first, give 2 to 4 options, and let the user type their own answer. With no question tool, ask in plain text and list the options, so a one-word reply is enough.
- **Ask open inputs on their own.** A list of companies or a market cannot be a set of options. Ask for it plainly, with nothing else to pick in the same message: users answer the choices and miss the question next to them.
- **Skip what is already known,** from the request or from earlier in the conversation.

The questions, in order. Reword them to fit what the user said.

1. **The goal.** "What would you like to get done?" Options: follow companies I own or watch; prepare for earnings; research a sector, theme or country; find new ideas.
2. **The subject.** Which companies, sector, theme, country or market, as an open question. For "find new ideas", ask what kind instead: a sector, a size, a region, a style.
3. **One-off or recurring.** "Is this a one-off, or something you'll come back to?" Options: just this once; every morning; around earnings; when something changes. Ask it unless the request already settles it or the task is plainly a single lookup.

Never ask more than three questions before the first result. Then run the first task without asking permission to start, sized as in Output, and use the answers to pick the offer in "After delivering".

## Do the task

1. **Use a job skill's method when one fits.** When the task matches one of the plugin's job skills and it is installed, read that skill and follow its method and output structure, then go beyond it where this task needs more. Do not hand off and stop: the answer is still this skill's to deliver.

   | The task | Skill |
   |---|---|
   | What moved in markets today, this week, this month | `bigdata-markets-today` |
   | A list of companies: what changed, side by side | `bigdata-watchlist` |
   | What happened at one company over a window | `bigdata-company-brief` |
   | Why a stock moved | `bigdata-stock-move` |
   | Upcoming events that could move a stock | `bigdata-catalysts` |
   | A fast view on a stock | `bigdata-quick-take` |
   | A full report on a company | `bigdata-deep-dive` |
   | A thesis, a variant view, the bull and bear case | `bigdata-thesis` |
   | What a company is worth, a DCF, what is priced in | `bigdata-valuation` |
   | Peer comparables | `bigdata-comps` |
   | Scenarios, probability-weighted value | `bigdata-scenarios` |
   | Accounting quality, red flags | `bigdata-earnings-quality` |
   | Moat, industry structure, pricing power | `bigdata-moat` |
   | Buybacks, dividends, M&A record, incentives | `bigdata-capital-allocation` |
   | What could go wrong, the downside | `bigdata-risk` |
   | Debt, leverage, refinancing, credit quality | `bigdata-credit` |
   | Before an earnings report | `bigdata-earnings-preview` |
   | After an earnings report | `bigdata-earnings-review` |
   | A merger, acquisition or bid | `bigdata-deal-analysis` |
   | A spin-off, arbitrage spread, rights issue, restructuring | `bigdata-special-situations` |
   | A sector or industry, or several compared | `bigdata-sector` |
   | A theme and who benefits | `bigdata-theme` |
   | A country or region | `bigdata-country` |
   | Countries or regions compared | `bigdata-macro-compare` |
   | Find companies that fit a profile | `bigdata-screen` |

   When none fits (markets today, a list of companies, the user's own documents, a one-line question), work from this skill and its reference file.

2. **Resolve first.** Resolve every company or security a tool needs an entity id for, as the reference describes. If a name could mean more than one, ask which one before going further.
3. **Plan the data needs.** Decide what the task must establish (the facts, the period, the comparison), then gather it. This step is done when every company, period and aspect in the request has evidence, or is named as a gap.
4. **Keep facts apart from analysis.** State what the data shows, then what it means.
5. **Cite every sourced claim** with inline numbers `[1]`, `[2]`, and list each source once under Sources in the server's link format, as `references/output-standard.md` shows. For figures computed from Bigdata.com data with no document behind them, name the data in a **Data** line under Sources.
6. **Name the gaps.** If Bigdata.com cannot answer part of the task, say so, rather than filling it from memory or web search without telling the user.

Bigdata.com is a research assistant: give no buy, hold or sell call, including when a job skill's template asks for a rating, stance or net assessment. Describe the balance of evidence and what would change it instead. The disclaimer on every output says no recommendation is given, and a call would contradict it.

## What Bigdata.com has

Use this to plan a task, and to answer when the user asks what Bigdata.com can do. Offer only what the connected tools provide.

| Data | Example request |
|------|-----------------|
| Companies, securities, ETFs and other entities, resolved to one identity | "Which company trades as BYD?" |
| News, filings, earnings call transcripts, broker research, podcasts and expert interviews, with citations | "What did management say about pricing on the last earnings call?" |
| One company in depth: financials, estimates, valuation, analyst ratings and sentiment | "Give me Microsoft's financial baseline and consensus estimates." |
| News sentiment on a company and the stories behind it | "How has news sentiment on Boeing moved this quarter?" |
| A list of companies side by side: price, daily move, earnings against estimates, price targets, sentiment | "How did these ten names do today?" |
| Watchlists: save a list of companies, then search news across all of them at once | "Save my holdings and tell me what changed on them." |
| ETFs, countries and global markets: indexes, sectors, commodities, rates, currencies and crypto | "How are global markets doing this week?" |
| Upcoming events: earnings dates, conferences, IPOs and economic releases | "Which large US banks report next week?" |
| Company screens by size, price, beta, volume, dividend, sector, industry, country or exchange | "US software companies worth more than $10bn." |
| The user's own documents, emails and research feeds, and saved Bigdata.com reports | "What do my broker notes say about this name?" |
| Monitors that check for new developments on a schedule | "Tell me when there is M&A news on my names." |
| Analysis code on Bigdata.com data: prices, returns, fundamentals, peers and charts | "Chart revenue growth for these five peers." |

## Output

If the user asked for a structure, length or format, follow it. Otherwise follow [references/output-standard.md](./references/output-standard.md), sized to the question: a direct answer for a quick question, the full frame for a research task. In every case, cite inline and end with **Sources**, then the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.

Markdown by default. For a formal deliverable, offer a Word document if the host can create files.

## After delivering

Make at most one offer, in one line: the first in this list that fits. If the user declines, do not repeat it in this conversation. Act only on a clear yes.

- **Save something to the user's Bigdata.com account:** a watchlist of the companies they named, a monitor for "when something changes", or the deliverable itself. The reference's "Saving to the user's Bigdata.com account" says when each fits.
- **Turn the task into a skill,** when both are true: the user has shaped how the task is done with preferences of their own (scope, sources, method or format), and they are likely to run it again, for example every morning or around earnings. A task that is only likely to recur does not qualify: "latest news on X" with nothing added needs no skill. Offer: "Want this as a skill you can rerun? I'll ask a few questions, one at a time."

## Build a skill

When the user wants to build their own skill, from the offer above or on their own, read [references/skill-builder.md](./references/skill-builder.md) and follow it.
