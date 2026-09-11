# Monitor configuration — one monitor per company, per topic

A monitor covers **one security and one topic**. `config.entity_watchlist` holds exactly one
`{name, rp_entity_id}` pair, and the monitor is not tied to any watchlist: the same
`NVDA · M&A` monitor serves every watchlist NVDA appears on, and keeps serving it after the user
renames the list or drops the name from it.

Per-company is narrower than the old per-watchlist monitor in two ways that matter. The query text can
name the company, so novelty is measured against that company's own history rather than a 40-name
pool. And an event arrives already attributed — no post-hoc filtering of a shared feed to guess which
row it belongs to.

The cost is monitor count. See [Scale](#scale) before creating anything.

## Naming

```
config.name = "[Watchlist] <TICKER> · <Topic>"
```

```
[Watchlist] NVDA · M&A
[Watchlist] ASML · Supplier risks
```

Topic labels, verbatim: `M&A`, `Competitor releases`, `Executives`, `Jobs trending`,
`Supplier risks`.

- **Read it right to left.** The last ` · ` segment is the topic label. Everything before it —
  normally the ticker, or the company name when there is no ticker — is a human label and is never
  parsed.
- **Ticker segment falls back to the company name when the tearsheet has no ticker** —
  `[Watchlist] <Company name> · <Topic>`. Parsing from the right is what makes that safe.
- Keep the whole string under ~80 characters; truncate the human-label segment, never the topic.
- The entity id is **not** in the name. `bigdata_fetch_monitors` matches names case-insensitively on a
  partial string, so `{name: "[Watchlist]"}` returns every console monitor; to scope to one company,
  fetch that set and filter client-side on `config.entity_watchlist[0].rp_entity_id`.

The watchlist name appears **nowhere** in the name. Mapping a monitor to a drawer tab is
`(rp_entity_id, topic)` — topic read from the name's last segment, `rp_entity_id` read from
`config.entity_watchlist[0]`, and both cached in `.bigdata-console.json` so later runs skip the
derivation entirely.

## The create sequence

Four calls per monitor, and the split is forced by the tool's own schema — the create branch and the
update branch accept different fields.

**1 · Preview.** `action: "create"`, `create_monitoring: false`. Returns the generated config with no
`id` and persists nothing. Show it to the user. This is also the observed request/response pair that
legitimises the console's create button.

**2 · Create.** Same payload with `create_monitoring: true` on approval. Returns `id`.

```json
{"action": "create", "create_monitoring": true,
 "intent": "<per-topic intent, naming the company>",
 "config": {
   "name": "[Watchlist] NVDA · M&A",
   "schedule": {"frequency": "1h"},
   "entity_watchlist": [{"name": "NVIDIA Corporation", "rp_entity_id": "D8442A"}],
   "search_queries": ["{\"search_mode\":\"fast\",\"query\":{\"text\":\"…\"}}"]
 }}
```

`config` on create accepts **only** `name`, `search_queries`, `schedule`, `extraction_instructions`
and `entity_watchlist`. The object is `additionalProperties: false` — an extra key is rejected, not
ignored.

**Every schema must contain at least one `entity_reference` field.** It is what keys the monitor's
deduplication, and the API rejects a schema without one:

```
at least one field must have field_type='entity_reference' — it keys the monitor's deduplication
```

**Enforcement is inconsistent.** Observed 2026-09-08: four executive monitors were accepted with a
schema carrying no `entity_reference` at all, and the fifth identical call was rejected. Never rely
on a schema being accepted because a previous identical one was — always include the field. If a
batch is already half-built when the error appears, re-send the corrected schema to **every** monitor
in the batch, or the drawer columns read different field names per company.

Pick the field that makes deduplication meaningful: the entity whose recurrence means "same event".
For M&A that is the counterparty; for a leadership change it is the person, not the company (a fixed
company reference would key every row to the same entity and defeat novelty).

**3 · Extraction schema.** `structured_output` is an **update-only** field. It cannot ride along on
the create call. Send it immediately after:

```json
{"action": "update", "monitor_id": "<uuid>", "structured_output": { }}
```

A monitor that never gets this call still runs; its events just arrive without the typed fields the
drawer's columns read, so the pane renders mostly empty cells.

**4 · Activation.** `status` is update-only too, so **a monitor cannot be created inactive** — read
the `status` the create response actually reports and reconcile it with the user's answer. Ask before
touching it:

> Created 12 monitors. Activate them now so they start running on schedule, or leave them off until
> you have reviewed them?

- **Yes** → the monitor must end up `active`. If the create response already reports active, nothing
  to send — say so rather than issuing a no-op call.
- **No** → send `{"action": "update", "monitor_id": "<uuid>", "status": "inactive"}`.

Ask **once per batch**, not once per monitor, and never activate on your own initiative. An inactive
monitor produces no runs at all, so its drawer tab ships at `data-state="inactive"` — a state that is
distinct from `pending` and must not be collapsed into it.

Steps 3 and 4 are one `update` call when the answer is "no": `structured_output` and `status` travel
together.

## Shared rules

- **Pin, don't regenerate.** Set `config.name`, `config.schedule`, `config.entity_watchlist` and
  `config.search_queries` explicitly. Anything left out is invented by the generator from `intent`.
- **`config.search_queries` takes fast-mode payloads as raw JSON strings** — one string per search
  text. Smart mode is rejected outright: a monitor stores what it runs, and a smart query would be
  re-planned every run. Payloads sharing filters are fused into one multi-text search, so list every
  phrasing of the same subject rather than picking one.
- **Name the company in the query text.** This is the point of a per-company monitor. Use the legal
  name and the common short form — "NVIDIA Corporation", "Nvidia" — plus the ticker where it is
  unambiguous. A bare ticker alone is a bad query term.
- The monitor sets its own time window per run, retrieves everything the query matches and does not
  rerank — so `max_chunks`, `timestamp` filters and reranker settings are dropped. Do not tune them.
- **Schedule**: `{frequency: "<n><h|d|w>"}`. Default `1h` for M&A and competitor releases, `1d` for
  executives and supplier risks, `1w` for hiring trends. Match the topic's real pace.
- **`text` fields never drive novelty.** Put free-form rationale and context in a `text` field so a
  reworded description does not resurface a known event as new.
- **Never re-create a monitor that exists.** Discovery runs before creation, and a company already
  covered for a topic — on any watchlist, from any earlier session — is reused.

## The five topics

`<Company>` is the tearsheet's company name, `<TICKER>` its ticker. Substitute both into the intent
and the query text; the structured output schema is the same for every company.

### M&A — `ma`

Fills the deal table, and the only topic with an ordered stage.

```
intent: "Track M&A activity involving <Company> (<TICKER>) — acquisitions, stake purchases, asset
         sales, joint ventures, divestitures and mergers, where <Company> is acquirer, target,
         investor or issuer."
```

`structured_output` (sent by the step-3 update):

| Field | `field_type` | Notes |
|---|---|---|
| `counterparty` | `entity_reference` | The other side of the deal |
| `deal_type` | `enum` | `acquisition`, `stake purchase`, `asset sale`, `joint venture`, `divestiture`, `merger` |
| `stage` | `ordered_enum` | `rumoured`, `exploring`, `announced`, `agreed`, `regulatory_review`, `completed`, `withdrawn` — **in that order**, so a deal advancing registers as movement rather than a new event |
| `role` | `enum` | `acquirer`, `target`, `stake_investor`, `stake_issuer`, `asset_buyer`, `asset_seller` |
| `value` | `currency` | Deal value |
| `stake` | `number` | Percentage where disclosed |
| `event_date` | `datetime` | |
| `rationale` | `text` | Why the deal is happening — context, not a novelty driver |

### Competitor releases — `comp`

```
intent: "Track product, service and platform launches by direct competitors of <Company> (<TICKER>),
         and note where each overlaps <Company>'s own product line."
```

Fields: `competitor` (`entity_reference`), `title` (`string`), `release_date` (`datetime`),
`overlap` (`text`).

### Executives — `exec`

```
intent: "Track senior executive and board changes at <Company> (<TICKER>) — appointments, departures,
         role changes and succession announcements."
```

Fields: `person` (**`entity_reference`** — this topic's deduplication key, so the same individual
resurfacing is recognised as the same event; it is also what satisfies the mandatory
`entity_reference` rule above), `change_type` (`enum`: `appointment`, `departure`, `role_change`,
`succession`), `role` (`string`), `effective_date` (`datetime`), `context` (`text`).

`person` arrives as an object (`{name, rp_entity_id}`) like any entity reference, so render
`person.name` in the column — writing the object straight into a cell yields `[object Object]`.

### Jobs trending — `jobs`

```
intent: "Track hiring activity and job posting trends at <Company> (<TICKER>) by functional area,
         including notable expansions and reductions."
```

Fields: `area` (`string`), `openings` (`number`), `trend` (`string`), `direction`
(`enum`: `expanding`, `flat`, `contracting`), `context` (`text`).

A weekly schedule suits this one — hiring data moves slowly and an hourly monitor mostly re-reports.

### Supplier risks — `sup`

```
intent: "Track supply chain and supplier risk affecting <Company> (<TICKER>) — capacity constraints,
         allocation disputes, qualification delays, concentration and single-source exposure."
```

Fields: `supplier` (`entity_reference`), `level` (`ordered_enum`: `low`, `medium`, `high`),
`risk_type` (`string`), `note` (`text`).

`level` is ordered so an escalation from medium to high registers as movement.

## Backfilling a new monitor

A monitor created now has no history, so its tab would sit at `pending` until the first scheduled run.
An **inactive** monitor never leaves that state at all — simulate before deactivating, or the tab has
nothing to show.

1. `bigdata_simulate_monitors` with `end_timestamp` at least 5 minutes in the past, `number_of_runs`
   sized to the period the user cares about (1–90 frequency-sized windows).
2. Poll with `bigdata_fetch_monitor_runs`, filtering on the returned `simulation_id` and passing
   `include_events: true`. Re-call the tool every 10–15 seconds; never shell `sleep`.
   - **Inventory before events.** A first pass with `include_events: false, limit: 20` returns every
     window with its `status` and `event_count` for a fraction of the payload. Use it to confirm the
     simulation is finished — all `number_of_runs` windows present and terminal — and to get the
     expected event total, *then* fetch the events.
   - **`limit` defaults to 1 and caps at 20.** Always pass a `limit` at least as large as
     `number_of_runs`, or the read is truncated in a way that is indistinguishable from a quiet feed.
   - If a `simulation_id`-filtered call comes back empty, retry **unfiltered** before concluding
     there are no runs — the filter has been observed returning nothing for a monitor that had
     completed runs.
   - **The response envelope is not consistent.** With runs, the tool returns a **bare JSON array**;
     with none, it returns `{"result": []}`. Accept both, plus the legacy `runs`/`items` keys:
     `Array.isArray(p) ? p : (p.result || p.runs || p.items || [])`. Code that reads only one shape
     silently sees an empty feed.
   - **A run's execution id is `id`, never `run_id`.**
   - **Scheduled runs are not aligned across monitors.** Each monitor's windows are offset by
     seconds from its own creation time (`15:06:53` for one, `15:07:13` for another), so window
     edges are not shared. Never derive one monitor's window boundaries from another's, and when
     filtering by period, compare each row's own `window_end` against a single cutoff rather than
     assuming rows fall into common buckets.
   - **`is_simulation` distinguishes a backfill from a real run.** A monitor left running produces
     scheduled runs (`is_simulation: false`) that accumulate between sessions; a returning session
     should read those rather than re-simulating, and must re-anchor its reference clock to the
     newest `window_end` instead of reusing the timestamp baked into an earlier build.
3. Simulations analyse earlier baseline windows first so novelty can be measured against existing
   content. Extra earlier windows appear in the results — that is expected. Report the requested
   window and its events, not the backfill internals.
4. **Reconcile before building.** Rows rendered for that (company, topic) must equal the summed
   `event_count` from the inventory. A mismatch means the build under-read, not that the monitor is
   quiet.

Record the `run_id` of every run whose events reach the console. It is half the pointer that makes the
stored display record re-expandable — see [archive-format.md](./archive-format.md).

## Scale

Monitor count is **companies × topics**, and it grows fast:

| Watchlist | 5 topics | 2 topics |
|---|---|---|
| 10 names | 50 monitors | 20 |
| 25 names | 125 | 50 |
| 40 names | 200 | 80 |

Each monitor also costs one `bigdata_fetch_monitor_runs` call per build and one watch subscription
when its drawer is open, against a per-view budget of 64.

**Never create a full grid without showing the number first.** Before any create call:

1. Discover what already exists — shared monitors mean a company covered from another watchlist needs
   nothing.
2. Count the gaps and state it plainly: *"36 companies × 5 topics = 180 monitors, 41 already exist,
   139 to create."*
3. Offer the two ways to cut it before asking for approval: **fewer topics** (M&A and executives are
   the usual keepers) or **fewer companies** (top holdings, or the ones the user names).
4. Create only the approved set. Every company left uncovered ships with a create button on that tab
   and is named in the handoff note.

Above roughly **60 monitors in one session**, create in batches and confirm between them rather than
firing a long unattended sequence.
