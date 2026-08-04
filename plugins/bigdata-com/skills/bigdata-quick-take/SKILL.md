---
name: bigdata-quick-take
description: >
  Give a fast, PM-style quick take on a stock using Bigdata.com data — a one-line current view,
  the 2-3 drivers that actually matter right now, the key risks and what would change the view,
  and the near-term setup with the next catalyst. Deliberately short: one page, no full thesis,
  no model. Triggers: "quick take on X", "what do you think of X", "give me a fast view on X",
  "thoughts on X", "X in a nutshell", "one-liner on X", "is X interesting right now".
---

# Bigdata Quick Take

One page, PM-style. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants a fast view, not a document. Not this skill when:

| Request | Use instead |
|---------|-------------|
| Full thesis with recommendation and conviction | Investment memo |
| 30 days of developments, categorized | Company brief |
| "What is it worth" | Valuation snapshot |
| Risks rated by likelihood and impact | Risk assessment |
| Analysis around an earnings event | Earnings preview / digest |

**The discipline of this deliverable is brevity.** If the answer is running past a page, the user asked for a different skill.

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `find_securities` | Resolve company name → RavenPack `entity_id` | None |
| `bigdata_company_tearsheet` | Financial baseline, estimates, sentiment | `find_securities` |
| `bigdata_search` | What's live on the name right now | None |

If the company name is ambiguous after `find_securities`, ask:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Workflow

### Step 1 — Identify the company

Call `find_securities` with the company name to get the `entity_id`.

### Step 2 — Baseline

Call `bigdata_company_tearsheet` for the financial and valuation baseline plus sentiment. One pass, no exhaustive extraction.

### Step 3 — What's live (2–4 searches, not ten)

- "[Company] recent developments last 30 days"
- "[Company] analyst view valuation debate"
- "[Company] risks concerns"

Enough to know what the market is arguing about. Stop there.

### Step 4 — Filter to what matters

Keep the **2–3 drivers** that actually move the name now. Apply the EPIC lens quickly — is it material, can you form a view, does consensus miss it? — without writing the table out. Depth if needed: [references/epic-framework.md](./references/epic-framework.md).

### Step 5 — Take a view

State a current view in one line. Name the key risks and **what would change the view**. Give the near-term setup and the next catalyst with its date.

## Output

Follow [assets/report-template.md](./assets/report-template.md).

- Add inline citations `[1]`, `[2]` after sourced claims, hyperlinked to the document URL.
- End with **Sources**, then the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim.
- Markdown by default. A quick take rarely needs a Word document — offer only if the user asks.

## Quality bar

Pass the PM test: **What's different?** **What matters?** **What should I do about it?** (net assessment, key risk, next catalyst — no position sizing).

Non-negotiables:

- A **view** is actually stated — "it depends" is not a quick take
- 2–3 drivers maximum
- What would change the view is named and falsifiable
- Next catalyst has a date, or is flagged as undated
- One page. Brevity is the product.
