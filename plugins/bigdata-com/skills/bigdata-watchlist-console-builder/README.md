# Bigdata Watchlist Console

Part of the **Bigdata.com** plugin.

Turns your existing Bigdata.com watchlists into an **interactive monitoring console** — a published HTML
page that re-queries Bigdata.com live, remembers what you have already looked at, and keeps a compact
local store of everything it shows you. Powered by **Bigdata.com MCP**.

---

## What It Produces

- A holdings grid per watchlist: price, 1-day change, actual EPS, analyst price target
- A per-security event tick rail — new, might-be-wrong, viewed — with an "N to view" caption
- An expandable drawer per security: M&A (with deal stage, counterparty, value and rationale),
  competitor releases, executive changes, hiring trends, supplier risks, and research notes
- Novelty monitors, **one per company per topic**, named so you can tell at a glance which company and
  which topic they cover — created only with your approval, and activated only if you say yes
- A compact local store of exactly what the console displays, plus the monitor and run ids to fetch the
  rest back on demand — and the price observations that become the console's price history over time
- A handoff note recording coverage, monitors, whether they are active, and what sits outside coverage

---

## What It Does Not Do

- **It never creates a watchlist.** Build those in the Bigdata.com platform; the console visualizes
  what already exists.
- **It never shows sample data.** A tab with no monitor offers to create one; an inactive monitor says
  it is switched off; a monitor with no completed run shows a spinner; a run that found nothing says so.
- **It never activates a monitor on its own.** Creating one and switching it on are two separate
  approvals.

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:watchlist-console-builder

---

## Structure

    bigdata-watchlist-console-builder/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/
    │   ├── bigdata-logo-on-dark.svg   the Bigdata.com lockup, inlined into the page
    │   ├── console-template.html       the standalone console page
    │   └── report-template.md          the handoff note
    └── references/
        ├── live-console.md            markup contract + runtime rules
        ├── monitor-configuration.md   per-company topic monitors, naming, activation
        ├── archive-format.md          the local display-projection store
        └── console-customization.md   reshaping the console

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform. The skill uses
`get_watchlist`, `bigdata_portfolio_tearsheet`, `bigdata_fetch_monitors`, `bigdata_configure_monitor`,
`bigdata_simulate_monitors` and `bigdata_fetch_monitor_runs`.

The live console — a page that refreshes itself and persists your viewed marks — requires a host that
grants Artifact runtime capabilities. Without them the page still renders as a static snapshot, which is
what the OpenAI target gets.

The local store requires filesystem access. Without it the console is built from live calls and keeps
no history — and the Pricing tab, which is accumulated from stored price observations, never appears.

---

## Fonts

Two Bigdata brand faces are licensed and deliberately **not** shipped with this skill: ModernoFB
Condensed and Apercu Pro Mono. The console substitutes open equivalents and loads Hanken Grotesk and
Roboto from Google Fonts. See `references/console-customization.md` to restore the brand faces for
internal builds.

---

## Related Skills

- **Company brief** — one company in depth
- **Peer comparables** — a static cited comparison across a list
- **Catalyst monitor** — dated events for one name
- **Quick take** — a fast verbal read on one stock

---

## License

See the root `LICENSE` file of the plugin repository for details.
