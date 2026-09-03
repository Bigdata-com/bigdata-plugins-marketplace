---
name: bigdata-watchlist-console-builder
description: >
  Build an interactive monitoring console from a user's existing Bigdata.com watchlists — a published
  HTML page with a holdings grid (price, 1-day change, EPS, price target), and topic drawers for M&A, competitor releases, executive changes, hiring trends and supplier risks fed by novelty monitors — one monitor per company per topic. The console re-queries Bigdata.com live, persists viewed marks and research notes across sessions, and keeps a compact local store of exactly what it displays plus the monitor and run ids to fetch the rest. It never creates a watchlist — it visualizes the ones that already exist. Triggers: "build a watchlist console", "watchlist console", "monitoring console for my
  watchlist", "dashboard for my watchlist", "what's new across my portfolio", "visualize my
  watchlist", "monitor my holdings", "what changed on my watchlist".
---

# Bigdata Watchlist Console Builder

An interactive console, not a report. Use Bigdata.com plugin tools for every fact.

**Use this skill when** the user wants to see what is moving across a whole watchlist and keep coming
back to it. Not this skill when:

| Request | Use instead |
|---------|-------------|
| One company in depth | Company brief / investment memo |
| A static cited document across a list | Peer comparables |
| Dated events for one name | Catalyst monitor |
| "What is it worth" | Valuation snapshot |
| A quick verbal read on one stock | Quick take |

**Two hard boundaries.**

1. **Never create a watchlist.** You can advise the user to use the `create_watchlist` instead.
2. **Never invent data.** No sample rows, no placeholder events, no illustrative charts. A tab with
   nothing in it says so — see [Empty states](#empty-states).

## Data foundation (plugin tools)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `get_watchlist` | No `id` → list owned watchlists. With `id` → that list's member entity ids | None |
| `bigdata_portfolio_tearsheet` | The holdings grid, and the source of every name and ticker | `get_watchlist` |
| `bigdata_fetch_monitors` | Which monitors already exist | None |
| `bigdata_configure_monitor` | Create a per-company topic monitor, set its `structured_output`, activate or deactivate it | `bigdata_portfolio_tearsheet` — the monitor name and its `entity_watchlist` need the company name |
| `bigdata_simulate_monitors` | Backfill a feed for a monitor with no run history | A monitor id |
| `bigdata_fetch_monitor_runs` | The event feed behind every drawer tab | A monitor id |

`find_securities` is **not** used. Watchlist `items` are already RavenPack entity ids, and the company name and ticker arrive as the portfolio tearsheet's identity columns — nothing needs resolving.

**Required on every call:** pass `plugin_slug: "bigdata-watchlist-console-builder"` in the request
parameters of *every* Bigdata.com plugin tool call made while running this skill. The value is always
the skill name, regardless of watchlist or query.

**Exceptions:** the `search` and `fetch` tools do not accept `plugin_slug` — omit it there. It is a
request parameter, **not** a tool input: never put it inside a tool's arguments object.

### Limits that change the calls

- `bigdata_portfolio_tearsheet` caps at **100 companies** when `EPS` or `PRICE_TARGET` is requested —
  **and when `metrics` is omitted**, since that returns every column. Above 100 names, request only
  `["PRICE","PRICE_CHANGE_1D"]` (3000 cap) and take the other two over a shortlist. Always pass
  `metrics` explicitly.
- **A monitor covers one company and one topic.** `config.entity_watchlist` holds exactly one
  `{name, rp_entity_id}` pair, so the old 100-entity cap never binds — but monitor count is now
  **companies × topics**, and 25 names across 5 topics is 125 monitors. Count the gaps, show the
  number, and offer to narrow before creating anything. [Scale](./references/monitor-configuration.md#scale).
- Monitors are **not tied to a watchlist**. A company covered from one list is already covered on every
  other list it appears on — discovery dedupes by `(rp_entity_id, topic)`.
- One `bigdata_fetch_monitor_runs` call per monitor per build. Fetch eagerly for the active watchlist
  only, and render the rest from the local store.
- `bigdata_fetch_monitor_runs` caps `limit` at **20** runs per call.

## Workflow

### Step 0 — Local store

The console renders from a small local store that holds **only what the page displays**, plus the
`(monitor_id, run_id)` pointer back to the full payload. Look for `.bigdata-console.json` at a path the
user named, or one used earlier in the conversation.

- Found, `schema: 2` → read `monitors.json` and the active watchlist's `securities/*.json`. That is the
  whole build input; render from it first so the console is up, then reconcile with live calls.
- Found, `schema: 1` → that is the old raw-payload archive. Leave it untouched, start a schema 2 store
  beside it, and say so once.
- Not found → ask once for a folder, confirm the path, then write the config.
- No filesystem access on this platform → skip the store, say so once, build from live calls alone, and
  ship without a Pricing tab.

Full layout and write rules: [references/archive-format.md](./references/archive-format.md). Never
default to a path inside a plugin or code repository, and if the chosen root sits in a git working
tree, say so and suggest a `.gitignore` entry — the store holds the user's holdings and financial data.

### Step 1 — List the watchlists

Call `get_watchlist` with no `id`. It returns display-ready markdown — relay it rather than rewriting
it, and render ids as inline code.

- **None owned** → tell the user, point at the platform, stop. Do not offer to create one.
- **The one they want is missing** → the listing covers only *owned* lists. Shared, public and global
  watchlists need their id pasted from the platform UI or a URL. Ask for it.
- **Several** → ask which to cover, and which is the starting view.

### Step 2 — Members and grid

Per watchlist: `get_watchlist` with the `id` for `items`, then `bigdata_portfolio_tearsheet` over those
ids with `metrics` set per the cap rule. Build the active list eagerly; leave the others until the user
switches.

A company with no market data keeps its row with blank cells — that is the tool's own behavior and the
console preserves it. Never drop a name.

### Step 3 — Monitor discovery

Read `monitors.json` from the store first — that is the mapping, already resolved. Then call
`bigdata_fetch_monitors` with `{name: "[Watchlist]"}` to pick up monitors created outside this store,
and match names against the convention:

```
[Watchlist] <TICKER> · <Topic>
```

The topic is the last ` · ` segment; everything before it (the ticker, or the company name when there is
no ticker) is a human label that is never parsed. The entity id is **not** in the name — read it from
the monitor's own `config.entity_watchlist[0].rp_entity_id` in the `bigdata_fetch_monitors` response.
The pair `(rp_entity_id, topic)` is what tells the console which monitor feeds which drawer tab — the
watchlist plays no part, so a company covered from another list needs nothing created.

Record every `(company, topic)` cell that has no monitor, and every monitor whose reported `status` is
`inactive` — those two states are different and stay different downstream.

### Step 4 — Monitor proposal, creation and activation

**Show the count before the calls.** Gaps are companies × topics; state the arithmetic
("36 names × 5 topics = 180, 41 exist, 139 to create") and offer the two ways to cut it — fewer topics,
or fewer companies — before asking for approval.

Then, per approved gap:

1. **Preview** — `action: "create"`, `create_monitoring: false`. Nothing is persisted, the generated
   config is shown to the user, and the tool's real response envelope is observed. That observation is
   what makes shipping a create button in the page legitimate (see step 7).
2. **Create** — the same payload with `create_monitoring: true`. Returns `id`.
3. **Extraction schema** — `structured_output` is **update-only** and cannot ride on the create call.
   Send `{"action": "update", "monitor_id": "<id>", "structured_output": {…}}` right after.
4. **Ask about activation, once for the batch:**

   > Created 12 monitors. Activate them now so they start running on schedule, or leave them off until
   > you have reviewed them?

   `status` is update-only too, so a monitor **cannot be created inactive** — read the status the create
   response actually reports rather than assuming one. **Yes** → make sure each ends up `active`, and
   send nothing where it already is. **No** → `{"action": "update", "monitor_id": "<id>",
   "status": "inactive"}` — the same update call that carries the extraction schema.

Never activate on your own initiative, and never treat silence as approval. An inactive monitor produces
no runs at all: its tab ships at `inactive`, not `pending`.

A declined cell is not a failure — its tab ships with a create button instead.

Per-topic intents, fast-mode search payloads, `structured_output` schemas, naming and the scale table:
[references/monitor-configuration.md](./references/monitor-configuration.md).

### Step 5 — Feed

`bigdata_fetch_monitor_runs` with `include_events: true` per monitor — one call per (company, topic).
Fetch eagerly only for the **active** watchlist; other lists render from the store until the user
switches. Skip inactive monitors entirely: they have no new runs to return.

**Record the run.** Keep the `run_id` of every run whose events reach the page — on the event record,
on the `<tr>`, and on the pane. It is what makes the display projection re-expandable; without it, a
stored cell is all that is left of the event.

For a monitor with no history, `bigdata_simulate_monitors` (with `end_timestamp` at least 5 minutes
in the past), then poll by
**calling `bigdata_fetch_monitor_runs` again** every 10–15 seconds. Never run a shell `sleep` and never
block waiting.

Simulations analyse earlier baseline windows first so novelty can be measured. Extra earlier windows in
the results are expected — do not report them as a problem.

Novelty per run drives the tick rail. Where an extracted event looks wrong — a closed deal resurfacing
as new, a third-degree link, a role that does not fit — carry that as the event's `flag`, which renders
as a red "might be wrong" tick rather than being silently dropped.

### Step 6 — Write the store

Write the **display projection**, not the payloads: `monitors.json`, one `securities/<entity>.json` per
company holding its grid cells and its per-topic events, an appended line per company in
`prices.jsonl`, and one line in `runs.jsonl`.

A stored `cells` key must be a `data-col` of that topic's table — if the page does not render it, it is
not stored. Events upsert by their own key and keep `first_seen`; prices and runs append.
[references/archive-format.md](./references/archive-format.md).

### Step 7 — Build and publish

Copy [assets/console-template.html](./assets/console-template.html), fill its injection markers with
HTML generated from real data, populate the `#bd-config` block, and publish with the `Artifact` tool.

**Before writing any runtime code:** load the `artifact-capabilities` skill and read the
platform-served `claude.d.ts` and `mcp.d.ts` for the live contract version. They are authoritative over
any remembered API shape. The markup contract, the manifest, and every rule the page must satisfy:
[references/live-console.md](./references/live-console.md).

The essentials:

- **Capabilities:** `{mcp: {servers: [{server, tools}]}, artifact: {}}`. `server` must be the
  connector's **display name exactly as claude.ai shows it** — `"Bigdata.com"`. **Get it by calling `ListConnectors`** (filter on
  `bigdata`) and take the `name` of the entry that is `connected` and `enabledInChat`. Do **not**
  derive it from your own tool-name prefix: the segment between `mcp__` and the next `__` is a
  sanitized identifier (`Bigdata_com`) that is not a valid `server` value and does not exist as a
  connector. **Declare exactly one server** — the one in use. A manifest is a viewer-consented grant,
  so a speculative second entry shows the viewer a connector name that isn't real; if you are unsure
  which name is right, call `ListConnectors` rather than declaring both. Have the page confirm the name
  from `listTools()` at load (matching case- and punctuation-insensitively) so it still binds if the
  display name is styled differently than expected.
- **Content is markup.** Generate the rows and events as HTML into the markers. Never render displayed
  content from a JS object at runtime: the markup *is* the shared document, and a viewer's gesture on
  it is what persists.
- **Set `createObserved: true` only if a real `bigdata_configure_monitor` response was seen this
  session** (the step 4 preview counts). Otherwise leave it `false` — the page disables its create
  buttons rather than calling a tool whose shape was guessed — and say so in your reply.
- **Bake `createRequests`** with the exact request payload per **(company, topic)**, so the button
  sends a shape you verified rather than one the page invents. `monitors` and `createRequests` are both
  keyed by `rp_entity_id`.
- **Watch on open, not on load.** 64 watches is the per-view budget and per-company monitors exceed it
  many times over: the page watches the grid always and a monitor only while its drawer is open.

### Step 8 — Customize

The default page is a starting point. Offer to drop columns the user does not care about, regroup or
re-sort the table, add or remove a topic tab, or change the refresh interval.
[references/console-customization.md](./references/console-customization.md).

## Empty states

Five distinct states. Collapsing any two of them misreports reality.

| Condition | Pane `data-state` | Shows |
|---|---|---|
| No monitor for this (company, topic) | `nomonitor` | "Create this monitor" button |
| Monitor exists but `status: "inactive"` | `inactive` | "Switched off — ask Claude to activate it" |
| Monitor active, no `COMPLETED` run yet | `pending` | Spinner, "first run pending" |
| A run completed, zero events in the window | `empty` | "No events in this period" |
| The call failed | `error` | The fix for that specific error code |

A tab that failed to load is **not** a tab with no news, and a tab whose monitor was never activated is
**not** a tab whose first run is pending — that one would spin forever.

## Output

The console is the deliverable. Alongside it, write the short handoff note in
[assets/report-template.md](./assets/report-template.md) — which watchlists are covered, which monitors
exist or were created and whether they are active, where the store lives, and what is outside
coverage.

Tell the user three things at publish time:

- A page declaring `mcp` **cannot be shared publicly** — it is private and team-shareable only.
- The page embeds a snapshot of their real watchlist data, which matters if they share it onward.
- The console can create monitors in their Bigdata.com account, so anyone given edit access can too.
- Which monitors were left **inactive**, if they declined activation — those tabs will stay empty until
  someone turns them on.

## Quality bar

- **No watchlist is ever created**, no monitor without explicit approval, and **no monitor activated
  without a separate explicit yes**.
- No invented watchlist ids, monitor ids, or entity ids.
- **No synthetic data anywhere.** Empty means empty, and the five states above stay distinct.
- Every stored event carries its `monitor_id` and `run_id`, and every stored cell corresponds to
  something the page actually renders.
- Every name in the active watchlist appears; missing data is a blank cell, never a dropped row.
- A live refresh never clobbers a viewed mark or a dismissal.
- The page renders correctly with both capabilities, with `mcp` unavailable, and for a read-only viewer.
- Correct in light and dark themes.
- Caps respected and surfaced — the 100-name metric cap, the 20-run fetch limit, and the 64-watch
  per-view budget that per-company monitors would otherwise blow through.
- The monitor count was shown to the user before any monitor was created.
