# Live console — markup contract and runtime rules

Everything the published page must satisfy. Read this before generating markup, and load the
`artifact-capabilities` skill plus the platform-served `claude.d.ts` / `mcp.d.ts` before writing any
runtime code — those type definitions are authoritative over anything written here about the call
envelope.

## 1. Two classes of state

This is the design, not a detail. Get it wrong and the tick rail stops meaning anything.

| Class | Where it lives | Saved? |
|---|---|---|
| **Persisted** — viewed marks, dismissals, per-security monitor mute, notes | `data-seen` on `<tr>`, `hidden` on `<tr>`, `data-mon` on `.bd-row`, textarea value | Yes — the live doc saves what a viewer's gesture changes in the DOM |
| **Local** — open drawer, active tab, sort order, period | `data-local-*` attributes | No — per viewer, per session |

A live doc saves **only** what a gesture changes. What script does on load, on a timer, or on an `mcp`
delivery is not saved. That is why the merge rule below works.

**The merge rule.** An `mcp` refresh may append rows for new event keys and update cell content. It must
**never** write `data-seen` or `hidden`. An event the viewer already marked viewed stays viewed when its
monitor run is delivered again.

**Never render displayed content from a JS object at runtime.** The markup *is* the shared document.
Generate it as HTML at build time and mutate it in handlers.

## 2. Injection markers

| Marker | Fill with |
|---|---|
| `<div id="bd-rail">` | One `.bd-wl` button per watchlist; exactly one `aria-current="true"` |
| `<h1 id="bd-title">` / `<p id="bd-desc">` | Active watchlist name; its description, or the member count |
| `<span id="bd-crumb-wl">` | `/ <active watchlist name>` |
| `<div id="bd-rows">` | One `.bd-row` per security — see §3 |
| `<script id="bd-config">` | The config object — see §4 |

## 3. Row markup

One per security in the active watchlist. `data-entity` is the RavenPack entity id and is how live grid
deliveries find the row.

```html
<div class="bd-row" data-entity="D8442A" data-ticker="NVDA" data-mon="1" data-local-open="0">
  <button class="bd-rowhead bd-grid">
    <span class="bd-ini">N</span>
    <span class="bd-id">
      <span class="bd-tk">NVDA</span>
      <span class="bd-nm">NVIDIA Corporation</span>
    </span>
    <span class="bd-num" data-cell="px"  data-na="0">183.22 <small>USD</small></span>
    <span class="bd-num bd-down" data-cell="chg" data-na="0">-1.24%</span>
    <span class="bd-num" data-cell="eps" data-na="0">1.30</span>
    <span class="bd-num" data-cell="pt"  data-na="0">210.00</span>
    <span><button class="bd-tog" aria-pressed="true" title="Disable news monitor for NVDA"><i></i></button></span>
    <span style="display:flex;align-items:center">
      <span class="bd-rail">
        <span class="bd-tick" data-key="evt-1" data-state="new"></span>
        <span class="bd-tick" data-key="evt-2" data-state="flag"></span>
      </span>
      <span class="bd-cap">2 to view</span>
    </span>
    <span style="display:flex;align-items:center;gap:8px;justify-self:end">
      <span class="bd-count" data-empty="0">2</span>
    </span>
    <span class="bd-chev"></span>
  </button>

  <div class="bd-drawer" data-local-tab="ma">
    <div class="bd-tabs">
      <button class="bd-tab" data-tab="comp"  aria-selected="false">Competitor releases</button>
      <button class="bd-tab" data-tab="exec"  aria-selected="false">Executives</button>
      <button class="bd-tab" data-tab="jobs"  aria-selected="false">Jobs trending</button>
      <button class="bd-tab" data-tab="ma"    aria-selected="true">M&amp;A</button>
      <button class="bd-tab" data-tab="notes" aria-selected="false">Notes</button>
      <button class="bd-tab" data-tab="sup"   aria-selected="false">Supplier risks</button>
    </div>
    <!-- one .bd-pane per tab -->
  </div>
</div>
```

Cells carry `data-cell` so live grid deliveries can update them, and `data-na="1"` when the value is
absent (renders dimmed as `—`). A `.bd-tick` must share its `data-key` with the `<tr>` it represents.

### Panes

Every pane declares its state. Only `ok` shows `.bd-body`; the others show their matching `.bd-state-*`
block, which the template already styles.

```html
<div class="bd-pane" data-tab="ma" data-active="1" data-state="ok"
     data-monitor="8f2c…" data-run="run_71b…" data-mon-status="active">
  <div class="bd-state bd-state-nomonitor">
    <div class="bd-kicker">No monitor yet</div>
    <p>Nothing is watching M&amp;A for NVIDIA Corporation.</p>
    <button class="bd-cta bd-create"><svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2"><use href="#i-plus"></use></svg>Create this monitor</button>
  </div>
  <div class="bd-state bd-state-pending"><span class="bd-spin"></span>First run pending — results appear once the monitor completes a window.</div>
  <div class="bd-state bd-state-inactive">
    <div class="bd-kicker">Monitor inactive</div>
    <p>This monitor exists but is switched off, so it will not run. Ask Claude to activate it.</p>
  </div>
  <div class="bd-state bd-state-empty"><p>No events in this period.</p></div>
  <div class="bd-state bd-state-error bd-err"></div>

  <div class="bd-body bd-pane-scroll">
    <table class="bd-evt" data-row-template="&lt;tr&gt;…&lt;/tr&gt;">
      <thead><tr>
        <th><button class="bd-sort" data-col="cp">Counterparty<i></i></button></th>
        <th><button class="bd-sort" data-col="stage">Stage<i></i></button></th>
        <th><button class="bd-sort" data-col="val">Value<i></i></button></th>
        <th><button class="bd-sort" data-col="date" aria-sort="descending">Event date<i></i></button></th>
        <th></th>
      </tr></thead>
      <tbody>
        <tr data-key="evt-1" data-run="run_71b…" data-seen="0" data-flag="">
          <td data-col="cp"><span class="bd-cp" data-live="counterparty">Marvell Technology Inc.</span><span class="bd-cpid" data-unresolved="0">E7D47B</span></td>
          <td data-col="stage"><span class="bd-pill" data-stage="agreed">agreed</span></td>
          <td data-col="val" class="bd-num" data-sort-value="12180">$12.18bn</td>
          <td data-col="date" class="bd-num" data-sort-value="2026-08-18">2026-08-18</td>
          <td>
            <span class="bd-acts">
              <button class="bd-iconbtn bd-seen" aria-pressed="false" title="Mark as viewed"><svg viewBox="0 0 24 24"><use href="#i-eye"></use></svg></button>
              <button class="bd-iconbtn bd-del" title="Remove — not relevant to this security"><svg viewBox="0 0 24 24"><use href="#i-trash"></use></svg></button>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### The pane's monitor, and the column sets

A pane is one **(company, topic)** pair, which is exactly one monitor. It carries three attributes so
the runtime and any later enrichment know what produced it:

| Attribute | Value | Used for |
|---|---|---|
| `data-monitor` | the monitor uuid | subscribing this pane's feed when the drawer opens |
| `data-run` | the execution id of the run the rows came from | re-fetching the full events behind them |
| `data-mon-status` | `active` or `inactive`, as the API last reported it | choosing between the `pending` and `inactive` states |

Each `<tr>` repeats `data-run`, because a table can hold rows from different runs — an older event that
last appeared two runs ago keeps pointing at the run that carried it. Together with the pane's
`data-monitor`, that is the pointer described in
[archive-format.md](./archive-format.md#the-pointer): everything the projection does not store is one
`bigdata_fetch_monitor_runs({monitor_id, run_id, include_events: true})` away.

**Column sets.** These `data-col` values are canonical — the local store's `cells` keys are defined as
"a `data-col` of that topic's table", so changing one changes both.

| Topic | `data-col` values, in order |
|---|---|
| `ma` | `cp` (+ `cp_id` inside the cell), `stage`, `val`, `date` |
| `comp` | `competitor`, `title`, `date`, `overlap` |
| `exec` | `person`, `change`, `role`, `date` |
| `jobs` | `area`, `openings`, `direction`, `trend` |
| `sup` | `supplier`, `level`, `risk`, `note` |

Every table also ends with the unlabelled actions column holding `.bd-seen` and `.bd-del`.

Rules for the event table:

- `data-key` must be the monitor event's own stable id. Without it the merge rule cannot work and a
  refresh will duplicate rows.
- `data-sort-value` carries the sortable form for numeric and date columns; the sorter falls back to
  text content otherwise. Nulls always sort last regardless of direction.
- `data-flag` non-empty turns the tick red, and the cell carries a `.bd-flag` note saying why the
  extraction looks wrong:

  ```html
  <span class="bd-flag"><svg viewBox="0 0 24 24"><use href="#i-flag"></use></svg>Closed earlier in 2026 — resurfaced as new</span>
  ```

  Use it for a stale event resurfacing, a third-degree link where the company is not a party, or a role
  that does not fit. Flagging beats dropping: a wrong extraction the user can see is better than a
  silent omission.
- `data-row-template` on `<tbody>`'s table holds an **HTML-escaped** empty `<tr>` skeleton whose cells
  carry `data-live="<field>"`. New events delivered live are built from it. Omit the attribute and live
  deliveries will update existing rows but not add new ones — a safe, if less useful, default.

### Notes pane

```html
<div class="bd-pane" data-tab="notes" data-active="0" data-state="ok">
  <div class="bd-body bd-note">
    <textarea placeholder="Add research notes for this security…"></textarea>
    <div class="bd-foot-note">Saved with the console · visible to everyone it is shared with</div>
  </div>
</div>
```

The mockup labelled notes "private to you". On a live doc that is **wrong** — a gesture saves as the
viewer and reaches every view. Use the caption above instead.

### Pricing pane

Ship it **only** when `prices.jsonl` holds two or more observations for that security. Render the
polyline server-side from the real stored prices into the template's `.bd-chart` SVG; label the axis
with the true first and last observation dates and state the resolution. Never interpolate across a gap
in the series, and never generate one. With fewer than two observations, omit the tab entirely.

## 4. Config block

```json
{
  "server": "claude_ai_Bigdata_com",
  "tools": ["bigdata_portfolio_tearsheet","bigdata_fetch_monitors",
            "bigdata_fetch_monitor_runs","bigdata_configure_monitor"],
  "activeWatchlist": "<watchlist id>",
  "watchlists": [{"id":"…","name":"My Portfolio","items":["D8442A","228D42"]}],
  "monitors": {"<rp_entity_id>": {"ma": {"id":"<uuid>","run":"<run id>","status":"active"}}},
  "createRequests": {"<rp_entity_id>": {"ma": { "request": { "action":"create", "…":"…" } }}},
  "topics": ["ma","comp","exec","jobs","sup"],
  "refetchIntervalMs": 300000,
  "generatedAt": "2026-08-20T14:05:00Z",
  "store": "<root>",
  "createObserved": true
}
```

Config only — ids, names, and the request payloads the buttons send. Never displayed content.

**Both maps are keyed by `rp_entity_id`, not by watchlist.** A monitor covers one company and one
topic and is shared by every watchlist that company sits on, so keying by watchlist would duplicate
ids and drift the moment a name moves between lists. `createRequests[entity][topic].request` is the
create payload baked for that exact company — the button never assembles one.

`plugin_slug` does **not** belong in any of these payloads. The tool schemas set
`additionalProperties: false`, so an extra key is rejected; it is a request parameter, not a tool input.

## 5. Manifest and the runtime contract

```
capabilities: {
  mcp: { servers: [{ server: "<connector segment>", tools: [<minimal list>] }] },
  artifact: {}
}
```

`server` is the segment between `mcp__` and the next `__` in the agent's own tool names — read it from
there, never hardcode it, because DEV, STG and Beta Bigdata.com connectors exist alongside production.
Keep `tools` minimal: it is a viewer-consented grant.

**Never publish a page that calls a connector tool without having observed one real request/response
pair for that tool in this session.** Steps 2–5 of the workflow observe the read tools. For the write
tool, the step 4 `create_monitoring: false` preview is a real call with no persistence — that is the one
that legitimises the create button. No observation, no button: set `createObserved: false` and say so in
your reply rather than shipping a guessed shape.

### watchTool vs callTool

- **`watchTool`** for everything displayed — it replays cache immediately, refreshes when stale, and
  coalesces identical identities so N panes cost one flight. Reads only: a tool the connector annotates
  `readOnlyHint: false` is rejected. Call `listTools()` at load and adapt to what the viewer has.
- **`callTool`** for actions: the create button, and an explicit "refresh now".
- Drive every freshness indicator from `result.cache.storedAt`, **never** from a clock reading taken at
  receipt.

### The watch budget

The per-view limit is **64 watches**, and per-company monitors blow straight through it: 25 names × 5
topics is 125 feeds. The page therefore watches **the grid always, and a monitor only while its drawer
is open**.

- One `bigdata_portfolio_tearsheet` watch for the active watchlist — that is the whole grid.
- Opening a row subscribes that row's panes, reading each pane's `data-monitor`. Closing it
  unsubscribes them. A closed drawer costs nothing.
- Cap concurrent monitor watches at **48**, leaving headroom under the limit for the grid and for a
  viewer who opens rows faster than they close them. At the cap, drop the least-recently-opened row's
  subscriptions first and leave its rendered rows in place — they are still the last-good data.
- Switching watchlist tears everything down first.

`watchTool` returns a synchronous unsubscribe — store it before the first delivery can fire
(deliveries arrive no earlier than a microtask after registration), and key the stored unsubscribes by
`(entity, topic)` so closing one drawer cannot cancel another's.

A pane with `data-mon-status="inactive"` is **not watched at all**: an inactive monitor produces no
new runs, so a subscription would poll forever for a window that never advances.

### Errors

Branch on `error.code`, never on message text, and never collapse the codes that have distinct fixes
into one banner — that is the named anti-pattern for this capability.

| Code | Response |
|---|---|
| `needs_reauth` | "Reconnect Bigdata.com in claude.ai Settings → Connectors" · retract data |
| `server_not_connected` | "Add Bigdata.com in claude.ai Settings → Connectors" · retract |
| `selection_required` | Ask the viewer to choose a connector · degrade like not-connected |
| `blocked_by_policy` / `approval_required` | Explain, no retry · retract |
| `not_in_manifest` | The page was published without that tool · retract |
| `not_granted` / `capability_disabled` / `capability_removed` | Snapshot-only, **silently** — no banner |
| `server_unavailable` | Transient. Keep last-good data, mark stale. `retryable` — at most one retry per user-visible refresh |
| `tool_error` | Surface the reported message in the affected section |
| anything else | Treat as `upstream_error` |

Contain each failure in the section it affects; when every section fails with the same code, show one
page-level message instead of repeating it.

### Writes are ambiguous

`server_unavailable`, `upstream_error` and `cancelled` are **ambiguous for a write** — a rejection is
not proof the tool did not run. For the create button that means:

1. One call per gesture; the button is disabled while in flight.
2. Never auto-retry.
3. On an ambiguous failure, **re-read `bigdata_fetch_monitors`** (with `cache: {refresh: true}`) to find
   out what actually happened, and report that — created-despite-the-error, or not created.
4. After a confirmed create, `invalidate()` the monitor reads so watched sections refetch, then move the
   pane to `pending`.

## 6. Page requirements

- **Self-contained.** Strict CSP blocks every external host except Google Fonts. No CDN scripts, no
  remote images, no fetch to anything but the capability surface.
- **Theme-aware in all three states** — explicit light, explicit dark, and system default. The template
  already defines the full palette on bare `:root` and redefines the dark swap under both
  `prefers-color-scheme` and `[data-theme="dark"]`. Keep it that way: no colour may have its only
  definition inside a media query.
- Wide tables scroll inside their own `overflow-x: auto` container; the page body never scrolls
  sideways.
- Citations hyperlink to the source document URL.
- **Powered by Bigdata.com** and the disclaimer stay in the footer, verbatim.
- A stable `<title>`, a `description`, and a `favicon` that does not change across redeploys.
- Redeploy to the **same file path** to keep the same URL; pass `url` when updating a console published
  in an earlier conversation.
