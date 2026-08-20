---
name: bigdata-post-ipo-day179
description: >
  Write a day-179 post-IPO note on the 180-day lock-up expiry using Bigdata.com data plus
  filings and market data. Covers lock-up terms from the prospectus (expiry date, covered
  holders, share count, early-release provisions), float and overhang math (post-expiry float,
  days-to-trade versus ADV), insider and VC selling-intention signals, positioning into the
  event (short interest, borrow, options skew), the historical lock-up-expiry effect with
  analogs, and a two-sided read. Balanced, no buy/avoid call. Triggers: "180-day lock-up expiry
  for X", "lockup expiration impact", "post-IPO day 179", "shares unlocking for X",
  "insider selling after lockup", "float expansion at lockup".
---

# Bigdata Post-IPO Day 179 — 180-Day Lock-Up Expiry

The standard **180-day lock-up** is about to release insider, employee, and pre-IPO investor shares. Run this note around **day 179** to size the potential supply overhang and how the stock is set up into the unlock. Use Bigdata.com plugin tools plus web search.

Read [references/post-ipo-common.md](./references/post-ipo-common.md) first — scope rules, data foundation, reference math, and the verify checklist apply in full.

> **Confirm the terms from the filing.** Lock-up duration, exact expiry date, covered holders, the share count released, and any **early-release provisions** (price or time triggers, underwriter waivers) are issuer-specific. Pull them from the prospectus and any subsequent 8-K/424B — do not assume a generic 180 days for every holder.

**Use this skill when** the first lock-up tranche is about to expire. Not this skill when:

| Request | Use instead |
|---------|-------------|
| The company has not yet priced | Pre-IPO analysis |
| Day-1 debut reaction | Post-IPO day 1 |
| ~Day 14, index inclusion question | Post-IPO day 14 |
| The later 366-day founder tranche | Post-IPO day 365 |

## What this note answers

- How many shares unlock, and how much does free float expand?
- How large is the overhang relative to the stock's capacity to absorb it (days-to-trade)?
- Are insiders and VCs signaling intent to sell (secondary filings, 10b5-1 plans)?
- How has positioning — short interest, borrow, options skew — set up into the date?

## Plugin tool calls

**Required on every call:** pass `plugin_slug: "bigdata-post-ipo-day179"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-post-ipo-day179`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

## Workflow

### Step 1 — Lock-up terms recap (cite the filing)

Expiry date, who is locked (founders, employees, pre-IPO VC/PE, strategic holders), the **share count releasing**, and any tiered or early-release provisions. Distinguish this 180-day tranche from a later founder tranche if the deal staggered its lock-ups.

### Step 2 — Float and overhang math (show inputs)

- Current free float vs **post-expiry float** = current float + newly unlocked shares. Express the increase as a multiple of current float and as a % of shares outstanding.
- **Days-to-trade** = newly unlocked shares / ADV — the headline overhang measure.

### Step 3 — Selling-intention signals

Search for disclosed secondary offerings, 10b5-1 trading plans, prior insider sales, and management or VC commentary. VC funds near end-of-life are more likely distributors than long-horizon founders.

### Step 4 — Positioning into the event

Short interest and days-to-cover, borrow availability and cost, options skew, and recent price action. Heavy pre-positioning can mean the overhang is already partly discounted.

### Step 5 — Historical lock-up effect

Cite the typical pattern — often a modest negative drift into and just after expiry, scaled by the float increase, insider ownership, and post-IPO performance — plus 1–2 recent analogs.

### Step 6 — Two-sided read and watch points

**Bear:** dilution of tradable supply, insider distribution. **Bull:** overhang already priced, expiry as a clearing event, float increase aiding index eligibility and liquidity. Watch points: exact expiry date, any early release or waiver, follow-on secondary, next earnings.

## Output

Follow [assets/report-template.md](./assets/report-template.md).

- Length: 4–7 pages — this is a single-catalyst note.
- Cover line: company name, "Post-IPO — 180-Day Lock-Up Expiry", date, "Prepared with Claude".
- Inline citations `[1]`, `[2]` after every sourced claim, hyperlinked to the document URL. Brand Bigdata.com content exactly "Bigdata.com".
- Full **Sources** section, then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Suggested filename: `Post_IPO_Day179_LockUp_<Company>_<YYYY-MM-DD>` in the user's requested format.

## Quality bar

Run the verify checklist in [references/post-ipo-common.md](./references/post-ipo-common.md) before delivering. In particular:

- Lock-up terms cited to the filing, including early-release provisions — never assumed
- Float and overhang math shown with its inputs; float % + locked % reconcile to shares outstanding
- Days-to-trade computed against a stated ADV
- Both sides framed — the bull read on a clearing event is not optional
- No recommendation language, no price target, no conviction rating
