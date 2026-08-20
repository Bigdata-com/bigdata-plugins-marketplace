---
name: bigdata-earnings-digest
description: >
  Analyze a public company's latest reported earnings — a cited post-print digest using
  Bigdata.com data (results, consensus and surprise, transcript, analyst reactions, tearsheet
  financials). Breaks down revenue and margins, segment and operating KPIs, management guidance,
  cash flow and balance sheet, and surprises versus expectations with sustainable-vs-one-time
  framing, plus a bull/bear thesis check, quality signals with forward watch-fors, sentiment and
  positioning, a post-print scenario refresh with probability-weighted expected value, and a
  valuation cross-check. Triggers: "analyze X earnings", "earnings digest for X", "how did X
  do last quarter", "X Q3 results", "break down X's earnings", "what did X report",
  "post-earnings analysis", "did X beat or miss".
---

# Bigdata Earnings Digest

Deep dive on one earnings event that has already been reported. Use Bigdata.com plugin tools for every fact.

**Use this skill when** results are out and the user wants them broken down. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Analysis ahead of an upcoming print | Earnings preview |
| 30 days of all developments, not one event | Company brief |
| "What is it worth" with no earnings event | Valuation snapshot |
| Comprehensive risk mapping | Risk assessment |
| Short reaction note against a stated thesis | Earnings reaction |

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Latest quarter, consensus, surprise, segments, history, sentiment/positioning fields | `find_securities` |
| `bigdata_events_calendar` | Date of the most recent earnings call | `find_securities` |
| `bigdata_search` | Release, transcript, analyst reactions, guidance, legal coverage | None |

**Required on every call:** pass `plugin_slug: "bigdata-earnings-digest"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-earnings-digest`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Before you synthesize — quality over quantity

The digest is **forward-looking**, not a transcription of the release. Before writing, identify the **2–3 factors that dominate the forward debate after this print** and lead with them. Everything else is supporting detail — do not give every line item equal weight.

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Financial data

Call `bigdata_company_tearsheet` with the `entity_id` for:

- Latest quarterly results (most recent Q)
- Analyst estimates and consensus
- Latest earnings surprise data
- Historical trends for comparison
- Segment performance breakdown
- **Sentiment, ownership, insider, options/short** fields where exposed — these fill the structured positioning table

If more than one recent quarter is available, confirm which to analyze:

> "I see results for Q3 2024 (most recent) and Q2 2024. Should I analyze the latest Q3 results?"

### Step 3 — Earnings date

Call `bigdata_events_calendar` with the `entity_id` to pin down when the most recent earnings call was.

### Step 4 — Search earnings materials

Run **5–7 targeted `bigdata_search` queries**:

- "[Company] earnings results Q[X] [Fiscal Year]"
- "[Company] earnings transcript conference call"
- "[Company] analyst reactions upgrades downgrades"
- "[Company] guidance outlook management commentary"
- "[Company] earnings surprise beat miss"
- "[Company] lawsuit litigation regulatory ruling investigation" — post-print legal overhang not in the press release

Cover the official release and metrics, transcript highlights, analyst reactions and rating changes, management guidance, and market reaction. Extract **key quotes** from the transcript where available.

If the call isn't published yet:

> "The earnings call transcript isn't available yet. I'll analyze the press release and update once the call is published."

### Step 5 — Results analysis

Organize the numbers into:

- **Revenue and margins** — total vs consensus, by segment/geography, gross/operating/net margin, YoY and QoQ
- **Operating metrics and segments** — KPIs, segment results, customer/user metrics, geographic performance
- **Management guidance and commentary** — forward guidance vs consensus, strategic initiatives, market conditions, capital allocation
- **Cash flow and balance sheet** — OCF and FCF trends, balance sheet strength, capex and investments

Note accounting changes and one-time items explicitly.

### Step 6 — Surprises: magnitude and quality

For each beat or miss:

- Quantify in **% or bps** vs consensus
- Frame **magnitude** as approximate **standard deviations** against the company's typical surprise volatility where data allows
- Label it **sustainable vs one-time** — revenue volume or price vs buyback, tax, timing, or other one-timers
- Identify what actually drove the market reaction

Focus on business fundamentals, not just the stock move.

### Step 7 — Thesis check (forward-looking)

Even with no thesis supplied by the user, frame both sides:

- **For bulls:** this quarter **strengthened / weakened / left unchanged** the bull case because [specific evidence].
- **For bears:** this quarter **strengthened / weakened / left unchanged** the bear case because [specific evidence].

If the user *did* supply a thesis, state its status explicitly as **Intact / Strengthened / Weakened / Broken**, with the specific data points that support the call. Methodology: [references/thesis-construction.md](./references/thesis-construction.md).

### Step 8 — Quality signals

Build the table with a forward **watch for** column — monitoring, not just a backward check:

| Signal | This quarter | Prior quarter | Trend / note | **Watch for (forward)** |
|--------|--------------|---------------|--------------|-------------------------|
| OCF vs net income | | | | |
| DSO | | | | |
| Inventory (if material) | | | | |
| Guidance vs actual (credibility) | | | | |

Depth: [references/quality-of-earnings.md](./references/quality-of-earnings.md).

### Step 9 — Sentiment & positioning (structured, not anecdotes)

Same discipline as the earnings preview: pull every **numeric** sentiment, insider, 13F/flow, and options/short field from the tearsheet first, then use Step 4 results to fill gaps. Write **"Not available"** for missing cells rather than dropping rows. A single sell-side note is not a substitute for positioning data.

### Step 10 — Scenario refresh + valuation cross-check

**Scenario refresh (post-print):** rebuild Bull / Base / Bear against the *new* information — probabilities summing to ~100%, what changed versus pre-print, price level or range, and the **probability-weighted expected value with the arithmetic shown**. Compute in prose/table by default; run [scripts/scenario_probability.py](./scripts/scenario_probability.py) only if the user explicitly asks for scripted math.

**Valuation cross-check:** current EV/EBITDA, P/E, FCF yield from the tearsheet vs recent history and peers. Answer directly: **does the reaction fit the surprise and the guidance?** Does the price now embed the new guidance?

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, mandatory tables, sources, and footer.

- Add inline citations as superscript-style numbers `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) or presentation version at the end if useful.

## Quality bar

Pass the PM test before delivering: **What's different?** **What matters (2–3 forward factors)?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing). Would it survive a short, skeptical morning meeting without reading as a press-release recap?

Non-negotiables in every digest:

- Thesis check for **both** bull and bear, with evidence — this is what makes the digest forward-looking
- Surprise magnitude quantified, and labelled **sustainable vs one-time**
- Quality signals table with the **watch for** column filled
- Sentiment & positioning as structured data — tearsheet first, then search
- Scenario refresh with probabilities and **EV math shown**
- Valuation cross-check tying implications back to price
- Legal/regulatory search run, with overhangs surfaced
- Facts separated from analysis and implications
