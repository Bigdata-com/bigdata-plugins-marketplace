# Local store — the display projection

A small local store holding **exactly what the console renders**, plus the two ids needed to go back
for anything it does not hold. The **skill** writes it; the published page cannot — an Artifact runs
sandboxed with no filesystem access, and the `downloads` capability only offers a single file through
a save dialog the viewer confirms.

This is not an archive of raw payloads. A monitor run's full event object is large, mostly unrendered,
and re-fetchable on demand; keeping it made every rebuild parse megabytes to fill a five-column table.
What is kept instead is one record per displayed cell, and `(monitor_id, run_id)` as the pointer back.

## The pointer

Every stored event carries the run it came from, and every topic carries its monitor:

```
bigdata_fetch_monitor_runs({ monitor_id: "<uuid>", run_id: "<execution id>", include_events: true })
```

That returns the complete original event — every extracted field, every citation, the full text — for
any row the user wants expanded. **This is the contract that makes the projection safe.** Storing a
displayed cell without its `run_id` throws information away permanently; storing it with one is a
cache.

Both ids come straight from `bigdata_fetch_monitor_runs`: the run's own execution id, and the
`monitor_id` it was fetched with. Never invent either, and never store an event whose run id is
unknown — carry it as a build error instead.

## Layout

```
<root>/
  .bigdata-console.json       config: root, watchlists, timezone, run pointers
  monitors.json               registry: entity → topic → monitor id, status, last run
  securities/
    D8442A.json               one file per company: grid cells + display events per topic
    228D42.json
  prices.jsonl                append-only price observations — the Pricing tab's series
  runs.jsonl                  append-only, one line per build run
```

One file per **company**, not per watchlist and not per hour. The console renders a row and its drawer
together, so one company is one read; building the active watchlist touches only its own members'
files. Companies shared across watchlists are stored once.

Timestamps are **UTC**, ISO-8601, matching the windows the monitor tools use. The choice is recorded
in the config so it cannot drift silently.

## `.bigdata-console.json`

```json
{
  "schema": 2,
  "timezone": "UTC",
  "watchlists": [{"id": "…", "name": "My Portfolio", "items": ["D8442A", "228D42"]}],
  "activeWatchlist": "…",
  "topics": ["ma", "comp", "exec", "jobs", "sup"],
  "created": "2026-08-20T14:05:00Z",
  "last_run": "2026-08-27T09:12:00Z",
  "retention_days": 180
}
```

Schema 1 stores were per-hour raw payload folders keyed by watchlist. There is no migration: leave a
schema 1 folder untouched, start a schema 2 store beside it, and say so once.

## `monitors.json`

The registry that replaces deriving the mapping from monitor names on every run.

```json
{
  "D8442A": {
    "ma": {
      "monitor_id": "8f2c…", "name": "[Watchlist] NVDA · M&A",
      "status": "active", "frequency": "1h",
      "last_run_id": "run_71b…", "last_run_at": "2026-08-27T06:00:00Z",
      "created_at": "2026-08-20T14:06:11Z", "created_by_console": true
    }
  }
}
```

`status` is the value the API last reported — `active` or `inactive` — never an assumption about what
create did. It is what decides between the `pending` and `inactive` pane states.

## `securities/<rp_entity_id>.json`

```json
{
  "rp_entity_id": "D8442A", "ticker": "NVDA", "name": "NVIDIA Corporation",
  "watchlists": ["wl_7c1…"],
  "grid": { "px": "183.22", "ccy": "USD", "chg": "-1.24%", "eps": "1.30", "pt": "210.00",
            "as_of": "2026-08-27T09:11:04Z" },
  "topics": {
    "ma": {
      "monitor_id": "8f2c…", "run_id": "run_71b…", "fetched_at": "2026-08-27T09:11:22Z",
      "state": "ok",
      "events": [
        { "key": "evt_4d19…", "run_id": "run_71b…", "first_seen": "2026-08-20T14:07:02Z",
          "cells": { "cp": "Marvell Technology Inc.", "cp_id": "E7D47B",
                     "stage": "agreed", "val": "$12.18bn", "date": "2026-08-18" },
          "sort":  { "val": 12180, "date": "2026-08-18" },
          "flag": "",
          "source": { "title": "Reuters", "url": "https://…", "published": "2026-08-18" } }
      ]
    }
  }
}
```

### What goes in `cells` — and nothing else

**A key in `cells` must be a `data-col` of that topic's table.** The column sets are defined in
[live-console.md §3](./live-console.md#3-row-markup); if a field has no column, it is not stored. Two
deliberate exceptions travel alongside, not inside, `cells`:

| Also stored | Why |
|---|---|
| `sort` | The `data-sort-value` a column renders with. Derived from the value, not extra data. |
| `flag` | Renders as the red tick and the `.bd-flag` note. Empty string when clean. |
| `source` | The citation the cell hyperlinks to. Title, url and published date only. |
| `source.published` | The newest grounding document's publication timestamp, rendered in the summary cell's source label as `MMM DD, YYYY - Sources via bigdata.com`, not in the counterparty cell. Null where the feed gave no usable timestamp. |
| `sources[]` | The distinct source names shown at the foot of the summary cell — name plus url, deduped by document id then by name. Store what the row displays, not the whole `grounding` array. |
| `summary` | The event summary shown in the `sum` column. |
| `event_date` | `{raw, display, precision}` — the source string as received, the normalised `MMM DD, YYYY` (or coarser) rendering, and which of day/month/quarter/year/text/none it resolved to. Keep `raw`: it is the only record of what the feed actually said. |
| `cp_id`-style id cells | Carried on the cell as `data-cp-id` for later re-fetch and enrichment. Not displayed as a column, and its absence is what sets `data-unresolved`. |

Not stored, by design: full event text, extraction confidence, the document chunk, entity lists beyond
the displayed counterparty, the monitor's own config echo, and every field of the extraction schema
the drawer does not render. All of it is one `run_id` away.

`state` is the pane state the last fetch produced — `ok`, `pending`, `inactive`, `empty` or `error`.
Storing it is what lets a rebuild show the correct empty state without re-deriving it.

**Viewed marks, dismissals and notes are never stored here.** They live in the published document,
which is where a viewer's gesture is saved. A rebuild reads them from the page, not from this store.

## `prices.jsonl` and the price series

One line per observation, append-only:

```json
{"t": "2026-08-27T09:11:04Z", "e": "D8442A", "px": 183.22, "chg": -1.24, "ccy": "USD"}
```

The three tool families give latest price and 1-day change — no history. Accumulated snapshots become
one:

- Enable the Pricing tab only at **two or more** observations for that security.
- Plot the real observed closes at their real timestamps. **Never interpolate across a gap** and never
  synthesize intermediate points.
- Label the axis with the true first and last observation dates, and state the resolution ("14 hourly
  observations, 2026-08-19 to 2026-08-20").
- Say plainly that it starts at the first run — it is forward-looking, not backfilled history.

## `runs.jsonl`

One line per build, append-only. It is the session log and the re-fetch index.

```json
{"started_at": "…", "finished_at": "…", "watchlists": ["…"],
 "counts": {"securities": 12, "monitors": 41, "events": 47, "created": 5, "activated": 5},
 "runs_read": {"8f2c…": "run_71b…"}, "errors": []}
```

`runs_read` maps monitor id to the run id read this build — the same pointer as on each event, kept
once more at run level so a re-fetch can replay a whole build.

## Write rules

- **Upsert, don't append, for events.** An event is identified by its `key`. A later run that carries
  the same key **updates its cells in place and keeps `first_seen`** — a deal moving from `announced`
  to `agreed` is the same event, further along. Only a new key appends.
- **Append-only for `prices.jsonl` and `runs.jsonl`.** Those two are the history.
- **Retention: 180 days** of events per (company, topic), by `event_date` where present and
  `first_seen` otherwise. Pruning is safe here in a way it never was for raw payloads: the run id
  survives in `runs.jsonl`. Prices are never pruned — they are the series.
- **Rewrite a security file whole.** It is small; a partial write that fails halfway is worse than a
  rewrite that does.
- **Optional.** No filesystem on this platform → skip the store, say so once, build from live calls
  and ship the console without a Pricing tab.
- **Confirm the root** before the first write, and create it only where the user named it. Never
  default to a path inside a plugin or code repository.
- If the root sits inside a git working tree, say so and suggest a `.gitignore` entry — the store
  holds the user's watchlist, holdings and financial data.

## Reading it back

Read the active watchlist's `securities/*.json` and `monitors.json`. That is the whole build input for
a rendered console — no folder walk, no bounded window, no payload parsing. `prices.jsonl` is read
filtered to the entities on screen.

The store is a cache of what was displayed, so a rebuild is expected to refresh it from live calls.
Render from the store first so the console is up immediately, then reconcile with what the live calls
return.
