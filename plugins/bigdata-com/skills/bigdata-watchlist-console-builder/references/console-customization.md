# Customizing the console

The default page is a starting point. This is the "builder" half of the skill — after publishing, offer
to reshape it.

## Columns

The holdings grid ships with what the three tool families actually serve: **Latest**, **1D Chg %**,
**Actual EPS**, **Price target**. To change the set, edit the `.bd-grid` template column list in the
stylesheet and keep the header cells in `.bd-colhead` aligned with the cells in each `.bd-rowhead` —
they are one grid, so a mismatch shifts every row.

```css
.bd-grid{grid-template-columns:34px 158px 96px 74px 62px 92px minmax(0,1fr) auto 18px}
/*                            ini  id    px  chg  eps  pt   rail          count chev */
```

### Restoring the mockup's dropped columns

Four columns and one tab were cut because the three chosen tool families cannot fill them. Each needs
one more tool, and each is a **per-company** call — so cap the enriched columns to a shortlist on a
large watchlist rather than fanning out over every name.

| Column | Tool | Cost |
|---|---|---|
| P/E Ratio (LTM), Capital Expenditure (FQ), Debt to Market Cap (LTM) | `bigdata_company_tearsheet` | One call per security |
| Next earnings | `bigdata_events_calendar` | One call per security |
| Bigdata signal (−1..+1) and its diverging bar | `bigdata_sentiment_tearsheet` | One call per security |
| Daily sentiment bars in the Pricing tab | `bigdata_sentiment_tearsheet` | One call per security |

The signal column also needs its bar markup back — a `.bd-num` cell plus a track element whose fill is
positioned from the value, mirroring the mockup's `sigBar` computation: width `abs(v) * 50%`, left
`50%` for positive and `50% - width` for negative.

"Consensus" in the mockup was an analyst **rating** (`Buy`). No tool in this plugin returns one, which
is why the default console shows the **price target** instead. Do not relabel it back without a source.

## Topics

Topics are declared in three places and all three must agree: `topics` in the config block, the tab
buttons in each drawer, and the `.bd-pane` blocks. To add one, define its monitor in
[monitor-configuration.md](./monitor-configuration.md) style — intent, fast-mode payload, schedule,
`structured_output` — give its pane a `data-tab` matching the new key, and add its `data-col` set to
the column table in [live-console.md §3](./live-console.md#3-row-markup), which is also what the local
store is allowed to keep.

**A topic costs one monitor per company**, so adding one to a 30-name watchlist is 30 monitors and 30
more `bigdata_fetch_monitor_runs` calls per build. Dropping the topics a user does not read is the
cheapest lever this console has — offer it before offering anything else.

Removing a topic means deleting the tab, the pane, and the config entry — for every company. It does
**not** delete the monitors from the user's account; offer `bigdata_configure_monitor` with
`action: "update"` and `status: "inactive"` if they want them stopped, or `bigdata_delete_monitors` if
they want them gone. That is one call per company, so state the count first.

## Sort, grouping and period

- Default sort is set by `aria-sort` on one `.bd-sort` button per table. Move it to change the default;
  `data-local-sort` on the pane then tracks the viewer's own choice.
- Grouping is not built in. To group by sector or conviction, emit `.bd-row` elements in the order you
  want with a heading row between groups — the interaction code is delegated from `document`, so it
  keeps working for rows in any arrangement.
- The period selector filters what the live layer polls. Its options live in `#bd-period-menu`; the
  handler calls `live.repoll()`, so adding an option only needs a `data-period` value the build step
  understands.

## Refresh cadence

`refetchIntervalMs` in the config drives `watchTool` polling. It is clamped to a ~30s floor by the
runtime, and minutes are the sensible range here — monitor runs are scheduled in hours, so polling
faster than the monitors run only re-reads the same window. Five minutes is the default.

## Fonts

Two brand faces are **not** shipped: ModernoFB Condensed (licensed from The Font Bureau) and Apercu Pro
Mono (from Colophon). Their own `fonts.css` says not to re-host them outside Bigdata/RavenPack work, and
this skill is distributed publicly. The template substitutes:

| Brand face | Substitute | Token |
|---|---|---|
| ModernoFB Condensed | `Georgia, 'Times New Roman', ui-serif, serif` | `--pf-display` |
| Apercu Pro Mono | `ui-monospace, 'SF Mono', 'Cascadia Mono', Menlo, Consolas, monospace` | `--pf-mono` |
| Hanken Grotesk | Google Fonts (open licence) | `--pf-ui` |
| Roboto | Google Fonts (open licence) | `--pf-kicker` |

For an **internal** build, redefine `--pf-display` and `--pf-mono` and add `@font-face` rules with the
binaries embedded as data URIs (~810KB total, well under the 16MB page cap). Do not do this for a page
that leaves Bigdata/RavenPack.

## Theme

The palette is Bigdata's platform tokens, `--pf-*`, kept under their original names so a brand update
can be re-applied by name. If you change them, keep the theme contract intact: the complete palette on
bare `:root`, the dark swap redefined under **both** `prefers-color-scheme` and `[data-theme="dark"]`.
A token defined only inside a media query breaks the explicit-choice toggle.
