---
name: bigdata-post-ipo-day1
description: >
  Write a first-trading-day post-IPO reaction note for a newly listed company using Bigdata.com
  data plus web market data. Anchors the deal (offer price vs range, shares, greenshoe, implied
  market cap), reconstructs day 1 (open, intraday range, close, volume, first-day return),
  reads demand and float mechanics including stabilization, resets valuation against peers at
  the close, notes the quiet-period coverage gap, and maps the dated post-IPO timeline.
  Balanced, no buy/avoid call. Triggers: "post-IPO day 1", "first day trading reaction for X",
  "how did X's IPO debut", "X IPO pop", "X first day of trading", "IPO debut analysis".
---

# Bigdata Post-IPO Day 1 — First-Trading-Day Reaction

Assess the **first trading day** of a newly listed company: how price discovery played out against the offer, what demand and stabilization signals say, and how the stock is set up for the weeks ahead. Use Bigdata.com plugin tools plus web search for market data.

Read [references/post-ipo-common.md](./references/post-ipo-common.md) first — scope rules, data foundation, reference math, and the verify checklist apply in full.

**Use this skill when** the company has listed and is on or near day 1. Not this skill when:

| Request | Use instead |
|---------|-------------|
| The company has not yet priced | Pre-IPO analysis |
| ~Day 14, index inclusion question | Post-IPO day 14 |
| ~Day 179, 180-day lock-up expiry | Post-IPO day 179 |
| ~Day 365, founder lock-up and float expansion | Post-IPO day 365 |

Confirm the listing date and compute the trading-day count before committing to this workflow.

## What this note answers

- Where did the deal price (above / within / below range) and how did day 1 trade against it?
- Is the first-day move demand-driven, stabilization-supported, or thin-float mechanics?
- What do the open, close, and intraday range imply about the new valuation vs peers?
- What are the dated catalysts that now define the post-IPO timeline?

## Plugin tool calls

**Required on every call:** pass `plugin_slug: "bigdata-post-ipo-day1"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-post-ipo-day1`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Anchor the deal

From the prospectus / 424B and the pricing press release: final offer price, the range, shares offered (primary vs secondary), greenshoe size, total raised, implied market cap and EV at the offer, underwriters, listing date, ticker, exchange.

### Step 2 — Reconstruct day 1 (web search for market data)

Opening print, intraday high and low, first-day close, total volume and turnover vs shares offered, and the **first-day return** = (close − offer) / offer. Note any disclosed underwriter **stabilization / greenshoe** activity and whether the stock held above the offer.

### Step 3 — Demand and float mechanics

Free float as a % of shares outstanding — a small float amplifies moves. Retail vs institutional demand signals, oversubscription commentary, cornerstone and anchor behavior. Flag explicitly if the move is more about **scarce float** than fundamental demand.

### Step 4 — Valuation reset at the close

Recompute EV/Sales (and EV/EBITDA or P/E if profitable) at the first-day close, versus the offer and versus 3–6 listed peers. State where it screens rich or cheap — **without** a fair-value target.

### Step 5 — Sentiment and coverage

Bigdata.com sentiment and media reaction over the first day(s). Underwriter analysts are still in the **quiet period**, so there are no sell-side ratings yet — say so rather than implying a consensus that doesn't exist.

### Step 6 — Map the post-IPO timeline

Lay out the dated watch points: quiet-period end and first analyst initiations (~day 25), potential NASDAQ-100 fast-track inclusion (~day 15), first earnings report, and the 180-day and 366-day lock-up expiries.

## Output

Follow [assets/report-template.md](./assets/report-template.md).

- Length: 4–7 pages — this is a single-catalyst note.
- Cover line: company name, "Post-IPO — First Trading Day", date, "Prepared with Claude".
- Inline citations `[1]`, `[2]` after every sourced claim, hyperlinked to the document URL. Brand Bigdata.com content exactly "Bigdata.com".
- Full **Sources** section, then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Suggested filename: `Post_IPO_Day1_<Company>_<YYYY-MM-DD>` in the user's requested format.

## Quality bar

Run the verify checklist in [references/post-ipo-common.md](./references/post-ipo-common.md) before delivering. In particular:

- Every number traces to a recorded source or a labeled, shown calculation
- Float % + locked % reconcile to shares outstanding; market cap = price × shares outstanding
- The trading-day count matches the listing date
- No recommendation language ("we recommend", "attractive entry", "avoid", "buy the dip")
- Balanced bull/bear read and dated watch points only — no price target, no conviction rating
