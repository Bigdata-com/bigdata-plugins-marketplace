---
name: bigdata-post-ipo-day14
description: >
  Write a day-14 post-IPO note on potential NASDAQ-100 fast-track index inclusion for a recently
  listed large-cap, using Bigdata.com data plus web search for index methodology and market data.
  Covers two-week trading status, an eligibility check against Nasdaq's current published rules
  (cited, never assumed), a float-adjusted index weight and implied passive-demand estimate with
  the math shown, days-to-cover versus ADV, the historical index effect and reversal risk, and
  dated watch points. Balanced, no buy/avoid call. Triggers: "NASDAQ-100 fast track for X",
  "index inclusion impact on X", "post-IPO day 14", "will X be added to the Nasdaq-100",
  "passive flows from index inclusion".
---

# Bigdata Post-IPO Day 14 — NASDAQ-100 Fast-Track Inclusion

A major IPO can qualify for **fast-track inclusion** in the NASDAQ-100 after a short minimum trading period, with inclusion effective around day 15. Run this note around **day 14** to capture the stock's status and the potential impact **before** inclusion takes effect. Use Bigdata.com plugin tools plus web search.

Read [references/post-ipo-common.md](./references/post-ipo-common.md) first — scope rules, data foundation, reference math, and the verify checklist apply in full.

> **Verify the rule, don't assume it.** NASDAQ-100 fast-entry eligibility (minimum trading days, the market-cap-rank threshold — historically top ~25% of the index) and the effective date are set by Nasdaq's published index methodology and can change. Confirm the current criteria and the specific effective date via web search before drawing conclusions, and state them as cited facts.

**Use this skill when** the company listed ~2 weeks ago and index inclusion is the live question. Not this skill when:

| Request | Use instead |
|---------|-------------|
| The company has not yet priced | Pre-IPO analysis |
| Day-1 debut reaction | Post-IPO day 1 |
| ~Day 179, 180-day lock-up expiry | Post-IPO day 179 |
| ~Day 365, founder lock-up and float expansion | Post-IPO day 365 |

## What this note answers

- Does the stock plausibly meet the fast-track eligibility criteria (market-cap rank, liquidity, seasoning)?
- If included, how large is the likely index weight and the mechanical passive demand?
- How does that demand compare to average daily volume — the "index effect" magnitude?
- How is the stock trading two weeks in, and what is already priced in?

## Plugin tool calls

**Required on every call:** pass `plugin_slug: "bigdata-post-ipo-day14"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-post-ipo-day14`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Two-week trading status

Price vs the offer and vs the day-1 close, trend and volatility, average daily volume (ADV), and current free float. Summarize whether the deal is working or fading.

### Step 2 — Eligibility check (cite the methodology)

From Nasdaq's **current** index methodology: minimum trading period, market-cap threshold, and liquidity/float requirements. Compare the company's market cap to the smallest current NASDAQ-100 constituents to gauge where it would rank. State eligibility as **likely / borderline / unlikely**, with the source.

### Step 3 — Passive-demand estimate (show the math, label as estimate)

- **Float-adjusted index weight** = company float-adjusted market cap / total NASDAQ-100 float-adjusted market cap
- **Implied passive buying** ≈ index weight × AUM tracking the NASDAQ-100 (QQQ plus other trackers — cite the AUM figure) / price = shares passive funds must buy
- **Days-to-cover** = implied passive buying / ADV — the core index-effect magnitude

### Step 4 — The index effect

Additions often drift up into the effective date as funds and front-runners accumulate, sometimes partially reversing afterwards. Cite recent NASDAQ-100 fast-track additions as analogs and how they traded around the event.

### Step 5 — Sentiment and risks

Bigdata.com sentiment and positioning. Risks both ways: inclusion not granted or delayed, the move already priced in, post-event reversal, or a high float/ADV diluting the effect.

### Step 6 — Watch points

Effective inclusion and rebalance date, rebalance mechanics, the 180- and 366-day lock-up expiries, and first earnings.

## Output

Follow [assets/report-template.md](./assets/report-template.md).

- Length: 4–7 pages — this is a single-catalyst note.
- Cover line: company name, "Post-IPO — NASDAQ-100 Fast-Track Inclusion", date, "Prepared with Claude".
- Inline citations `[1]`, `[2]` after every sourced claim, hyperlinked to the document URL. Brand Bigdata.com content exactly "Bigdata.com".
- Full **Sources** section, then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Suggested filename: `Post_IPO_Day14_IndexInclusion_<Company>_<YYYY-MM-DD>` in the user's requested format.

## Quality bar

Run the verify checklist in [references/post-ipo-common.md](./references/post-ipo-common.md) before delivering. In particular:

- Eligibility rules cited to Nasdaq's current methodology, never asserted from memory
- Every estimate labeled as an estimate, with its inputs and arithmetic shown
- AUM figure sourced, not assumed
- Days-to-cover computed against a stated ADV
- No recommendation language, no price target, no conviction rating
