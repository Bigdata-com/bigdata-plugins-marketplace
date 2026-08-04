---
name: bigdata-post-ipo-day365
description: >
  Write a day-365 post-IPO note on the 366-day founder and significant-investor lock-up expiry
  and float expansion toward 15-20%, using Bigdata.com data plus filings and market data. Covers
  the staggered lock-up structure from the prospectus, float expansion math and days-to-trade,
  the offsetting float-adjusted index reweight demand netted against new supply, a realistic
  read on whether founders actually sell, the dual-class governance angle, and a two-sided
  setup. Balanced, no buy/avoid call. Triggers: "366-day lock-up for X", "founder lock-up
  expiry", "float expansion for X", "post-IPO one year lockup", "index reweight after float
  increase", "founder selling after IPO".
---

# Bigdata Post-IPO Day 365 — Founder Lock-Up & Float Expansion

A later **366-day lock-up** tranche releases founder and significant-investor shares, potentially expanding free float toward **15–20%**. Run this note around **day 365** to prepare for the supply increase and the offsetting mechanical demand. Use Bigdata.com plugin tools plus web search.

Read [references/post-ipo-common.md](./references/post-ipo-common.md) first — scope rules, data foundation, reference math, and the verify checklist apply in full.

> **Confirm the staggered structure from the filing.** Multi-tranche lock-ups, exactly which holders the 366-day tranche covers, the share count, and dual-class voting implications are issuer-specific. Pull them from the prospectus and subsequent filings — do not assume a standard structure.

**Use this skill when** the second, founder-level tranche is about to expire. Not this skill when:

| Request | Use instead |
|---------|-------------|
| The company has not yet priced | Pre-IPO analysis |
| Day-1 debut reaction | Post-IPO day 1 |
| ~Day 14, index inclusion question | Post-IPO day 14 |
| The earlier 180-day tranche | Post-IPO day 179 |

## What this note answers

- How far does free float expand (toward 15–20%?), and how many founder/investor shares become eligible?
- Does float-adjusted index re-weighting create mechanical buying that absorbs some of the new supply?
- How likely are founders and long-horizon investors to actually sell, versus diversify gradually?
- Does the founder retain control through super-voting shares even after selling economic stake?

## Workflow

### Step 1 — Lock-up structure recap (cite the filing)

The 366-day tranche: covered holders (founders, major VC/PE, strategic), the share count releasing, and how it stacks on the earlier 180-day unlock. Note any dual-class or super-voting structure.

### Step 2 — Float expansion math (show inputs)

- **Projected post-expiry float** = current float + newly eligible founder/investor shares. Express as a % of shares outstanding and check it against the 15–20% expectation.
- **Days-to-trade** = newly eligible shares / ADV. Treat this as a **ceiling** — founders rarely sell all at once.

### Step 3 — The offsetting demand: float-adjusted index reweighting

Many indices weight by **free-float** market cap, so a float increase raises the company's float-adjusted weight and triggers **mechanical passive buying** at the next reweight. Estimate the weight change and implied passive demand — show the math, label it an estimate — and **net it against the new supply**.

### Step 4 — Realistic supply assessment

Founders typically diversify gradually, often via 10b5-1 plans, rather than dump. End-of-life VC funds may distribute to LPs instead. Search for disclosed plans, prior selling behavior, and management commentary.

### Step 5 — Governance angle

Whether founders retain voting control via super-voting shares after selling economic stake, and what that means for the alignment narrative.

### Step 6 — Two-sided read and watch points

**Bear:** meaningful new founder and VC supply, plus the signaling effect. **Bull:** float increase improves liquidity, index weight, and institutional accessibility; passive demand offsets supply. Watch points: exact expiry date, index reweight date, disclosed sale plans, next earnings.

## Output

Follow [assets/report-template.md](./assets/report-template.md).

- Length: 4–7 pages — this is a single-catalyst note.
- Cover line: company name, "Post-IPO — Founder Lock-Up & Float Expansion", date, "Prepared with Claude".
- Inline citations `[1]`, `[2]` after every sourced claim, hyperlinked to the document URL. Brand Bigdata.com content exactly "Bigdata.com".
- Full **Sources** section, then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Suggested filename: `Post_IPO_Day365_FounderLockUp_<Company>_<YYYY-MM-DD>` in the user's requested format.

## Quality bar

Run the verify checklist in [references/post-ipo-common.md](./references/post-ipo-common.md) before delivering. In particular:

- Staggered lock-up structure cited to the filing — never assumed
- Supply and index-demand both quantified, with arithmetic shown, then **netted** against each other
- Days-to-trade presented as a ceiling, not a forecast
- Governance and voting control addressed explicitly where a dual-class structure exists
- No recommendation language, no price target, no conviction rating
