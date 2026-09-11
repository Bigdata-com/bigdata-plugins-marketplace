# Watchlist console — handoff note template

The console itself is the deliverable. This note ships alongside it so the user knows what was built,
what is watching what, and what is outside coverage. Keep the section order. Where a section has no
content, write "None" rather than dropping it.

---

<!-- Writing style: ASD-STE100 Simplified Technical English — simple, brief,
     clear, human. One idea per sentence, one word per meaning, active voice,
     articles kept, no idiom. See the Writing style section in SKILL.md. -->

# Watchlist Console — [DATE]

**Console:** [artifact URL]
**Watchlists covered:** [N] · **Securities:** [N] · **Monitors:** [N] total, [N] active, [N] inactive

---

## Coverage

One monitor per company per topic. One row per security in the active watchlist.

| Security | M&A | Competitors | Executives | Jobs | Suppliers |
|----------|-----|-------------|------------|------|-----------|
| [TICKER] [Name] | ✓ / ◦ / — | ✓ / ◦ / — | ✓ / ◦ / — | ✓ / ◦ / — | ✓ / ◦ / — |

✓ = an **active** monitor that has completed at least one run. ◦ = a monitor exists but is **inactive**
or has no completed run yet — that tab is empty and says why. — = no monitor; the console shows a
create button on that tab.

For more than ~15 securities, give the totals per topic instead of a row per name, and list the
uncovered names under "What is outside coverage".

## Monitors created this session

| Security | Topic | Monitor name | Schedule | Status | First run |
|----------|-------|--------------|----------|--------|-----------|
| [TICKER] | [Topic] | `[Watchlist] NVDA · M&A` | [1h] | [active / inactive] | [pending / backfilled via simulation] |

Monitor names carry the company and the topic, not the watchlist — the same monitor serves every list
that security appears on.

**Activation:** [activated on the user's approval / left inactive at the user's request — these tabs
stay empty until someone turns the monitors on]. If nothing was created, write "None — the console
reads existing monitors only."

## What is outside coverage

State every gap explicitly. Silence here reads as full coverage.

- **Securities with no monitors:** [names, or "None"]
- **Topics not covered:** [e.g. "Jobs trending and Supplier risks were skipped to keep the count at 72
  monitors instead of 180", or "None"]
- **Monitors left inactive:** [names, or "None"]
- **Metrics not requested:** [e.g. "EPS and price target taken over a 40-name shortlist; the full
  [N]-name list carries price and 1-day change only"]
- **Columns not available from this tool set:** P/E, capital expenditure, debt to market cap, next
  earnings, and the Bigdata signal are not in this console — each needs a tool outside the three
  families it uses.
- **Pricing tab:** [enabled from [N] stored observations, [date] to [date] / not yet — needs two runs]

## Local store

**Root:** `[path]` · **Companies stored:** [N] · **Events stored:** [N] · **Price observations:** [N]

Holds only what the console displays, plus the `(monitor_id, run_id)` pointer behind every event — so
any row can be re-expanded with `bigdata_fetch_monitor_runs` without keeping the full payloads.
Retention is [180] days for events; price observations are never pruned, and they are what the Pricing
tab plots.

If the store was skipped, say why: "No filesystem access on this platform — the console was built from
live calls and keeps no history."

## Notes on the live console

- The page re-queries Bigdata.com with the viewer's own credentials. It cannot be shared publicly.
- It embeds a snapshot of this watchlist data, which travels with the page if shared.
- It can create monitors in the account, so anyone with edit access can too.
- Viewed marks, dismissals and notes are saved with the console and are visible to everyone it is
  shared with. They live in the page, never in the local store.
- Monitor feeds are subscribed only while a drawer is open — the per-view watch budget is 64 and
  per-company monitors run well past it.

## Sources

List every document referenced in the console's event feed, numbered to match its citations:

- Reference number matching the inline citation
- Source name and publication date (MMM DD, YYYY) hyperlinked to the URL

**Example:**
[1] (Reuters - Aug 18, 2026)[https://www.reuters.com/…]
[2] (NVIDIA Q2 2027 Earnings Call - Aug 20, 2026)[https://…]

---

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

---

## Footer rule

The **Powered by Bigdata.com** line and the **Disclaimer** block above are mandatory and must be
reproduced **verbatim** — in this note after the Sources section, and in the console's own page footer.
