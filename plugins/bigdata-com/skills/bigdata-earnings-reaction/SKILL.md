---
name: bigdata-earnings-reaction
description: >
  Write a tight post-earnings reaction note using Bigdata.com data — headline numbers versus
  consensus with beat/miss magnitude, what mattered on both sides, a prior-versus-new guidance
  table, an explicit thesis check (Intact / Strengthened / Weakened / Broken) with evidence,
  the estimate and price-target revisions the print forces, a pre-versus-post valuation update,
  quality signals for the quarter, and an action with the next key date. Shorter and more
  decision-focused than a full earnings digest. Triggers: "earnings reaction for X", "how
  should I react to X's results", "does X's quarter change the thesis", "X print reaction",
  "revise my numbers after X earnings", "was X's quarter good enough".
---

# Bigdata Earnings Reaction

The decision note after a print: what changed, what to revise, what to do. Use Bigdata.com plugin tools for every fact.

**Use this skill when** results are out and the user needs a fast, thesis-anchored call. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Full breakdown of the quarter — segments, cash flow, guidance detail | Earnings digest |
| Analysis ahead of the print | Earnings preview |
| A view with no earnings event | Quick take |
| Full thesis rebuild | Investment memo |

**Digest vs reaction:** the digest explains the quarter; the reaction decides what to do about it. If the user has a position or a stated thesis, this is the right skill.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Reported numbers, consensus, surprise, multiples pre/post | `find_securities` |
| `bigdata_events_calendar` | Confirm the report date and the next key date | `find_securities` |
| `bigdata_search` | Release, transcript, guidance, analyst reactions | None |

**Required on every call:** pass `plugin_slug: "bigdata-earnings-reaction"` in the request parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always the skill name, `bigdata-earnings-reaction`, regardless of the company or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there.

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Anchor the print

Resolve the entity, confirm the reported date, and pull the tearsheet for actuals versus consensus, the surprise, and multiples before and after the move.

### Step 2 — Ask for the thesis (or infer both sides)

If the user has stated a thesis, use it — the thesis check is the centerpiece of this note. If not, construct the prevailing bull and bear cases from the tearsheet and search, and check the quarter against **both**.

### Step 3 — Headline numbers

Revenue, EPS, and the key sector KPI: reported, consensus, beat/miss in % or bps, and YoY change. Quantify — "solid quarter" is not a number.

### Step 4 — What mattered

Positive and negative surprises, each with its magnitude and whether it is **sustainable or one-time** (revenue volume or price vs buyback, tax, timing). Run 3–5 searches:

- "[Company] earnings results Q[X] [Fiscal Year]"
- "[Company] earnings call transcript guidance commentary"
- "[Company] analyst reactions price target changes"
- "[Company] earnings surprise beat miss reaction"

### Step 5 — Guidance update

Prior guidance versus new guidance versus consensus, per metric. Guidance usually moves the stock more than the reported quarter — treat it as first-order.

### Step 6 — Thesis check

State the status explicitly: **Intact / Strengthened / Weakened / Broken**. Back it with the specific data points from the quarter that support the call — not a general impression.

### Step 7 — Revisions and valuation

What the print forces you to change: FY revenue, FY EPS, price target. Then the valuation update — stock price, NTM P/E, NTM EV/EBITDA, pre- versus post-earnings. Does the move fit the news?

### Step 8 — Quality signals

OCF vs net income, DSO trend, inventory build, and guidance credibility (met/beat versus missed). A beat on declining quality is a different result than a beat on improving quality. Depth: [references/quality-of-earnings.md](./references/quality-of-earnings.md).

### Step 9 — Action

Give the action and the rationale in one or two sentences, plus the next key date. If scenarios need re-weighting, run [scripts/scenario_probability.py](./scripts/scenario_probability.py) only when the user asks for scripted math.

## Output

Follow [assets/report-template.md](./assets/report-template.md) exactly — section order, tables, sources, and footer.

- Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.
- Every deliverable ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Default format is Markdown; offer a Word (.docx) version if useful.

## Quality bar

Non-negotiables:

- Thesis status stated as one of the four words, with evidence — the whole note turns on this
- Beat/miss quantified and labelled sustainable vs one-time
- Guidance treated as first-order, with prior versus new side by side
- Estimate and price-target revisions named explicitly, not left implied
- An action given with a next key date
- Facts separated from analysis and implications
