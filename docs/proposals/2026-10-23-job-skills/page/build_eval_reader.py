#!/usr/bin/env python3
"""Build the Skills Eval Reader page: every quality-eval run's report, run log and grades,
readable in full, with the two arms side by side.

    PAGE_INPUTS=<dir with fonts-platform.css and logo.datauri> python3 -I build_eval_reader.py [out.html]
    python3 ~/.agents/skills/build-artifact/scripts/kit.py inline <out.html>

Reads plugins/bigdata-com/evals/quality-2026-10-26/ in the skills worktree (SKILLS_WORKTREE env)."""
import glob, json, os, re, sys, time

PAGE = os.path.dirname(os.path.abspath(__file__))
W = os.environ.get("SKILLS_WORKTREE", "/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-audit-fixes")
INPUTS = os.environ.get("PAGE_INPUTS", PAGE)
EV = f"{W}/plugins/bigdata-com/evals/quality-2026-10-26"
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{PAGE}/eval-reader.html"
PROPOSAL_URL = "https://claude.ai/artifact/CoETtAqbh3bWgotehF1bEU"

def rd(p):
    with open(p, encoding="utf-8") as f: return f.read()
def rj(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
def exists(p): return os.path.exists(p)

SKILL_LABEL = {"company-brief": "Company brief", "credit": "Credit", "deep-dive": "Deep dive", "earnings-preview": "Earnings preview",
               "earnings-review": "Earnings review", "earnings-recap": "Earnings recap", "markets": "Markets today", "sector": "Sector", "stock-move": "Stock move",
               "theme": "Theme", "valuation": "Valuation"}
SUBJECT = {"coreweave": "CoreWeave", "cableone": "Cable One", "spacex": "SpaceX", "amazon": "Amazon", "gm": "General Motors",
           "week": "Last week", "semis": "Semiconductors", "deckers": "Deckers", "nvent": "nVent", "nvidia": "Nvidia",
           "jetblue": "JetBlue", "meta": "Meta", "netflix": "Netflix", "equinix": "Equinix", "refining": "US refining",
           "dc-power": "Data-centre power", "cfo-brief": "CFO briefing", "alphabet": "Alphabet", "cfo-thursday": "CFO briefing, Thursday"}
VOICE = {"pm": "PM", "corp": "Corporate", "corporate": "Corporate"}
ARM = {"with_skill": "With skill", "without_skill": "Without skill"}

def split_id(eid):
    m = re.match(r"^(.*)-(pm|corp)-(.*)$", eid)
    skill, voice, subj = m.group(1), m.group(2), m.group(3)
    return SKILL_LABEL.get(skill, skill), VOICE[voice], SUBJECT.get(subj, subj)

def parse_verdict(text, letter):
    """The judge's fixed structure (1 Winner ... 8 Actionability) into the pieces the page shows next to a note."""
    secs = {}
    for chunk in re.split(r"\n(?=\d\. \*\*)", "\n" + text):
        m = re.match(r"(\d)\. \*\*[^*]+\*\*:?\s*(.*)", chunk.strip(), re.S)
        if m: secs[int(m.group(1))] = m.group(2).strip()
    def bullets(n, k=2):
        out = [re.sub(r"^[-*]\s+", "", ln).strip() for ln in secs.get(n, "").splitlines() if re.match(r"^\s*[-*]\s+", ln)]
        return out[:k]
    def for_letter(n):
        for ln in secs.get(n, "").splitlines():
            m = re.match(r"^\s*[-*]?\s*\**([AB])\**\s*[:.]\**\s*(.+)$", ln.strip())
            if m and m.group(1) == letter: return m.group(2).strip()
        return ""
    s1 = secs.get(1, "")
    low = s1.lower()
    margin = ("not close" if re.search(r"not (very )?close", low) else "narrowly" if ("narrow" in low or "small margin" in low) else
              "moderately close" if "moderately close" in low else "close" if re.search(r"\bclose\b", low) else "")
    other = "B" if letter == "A" else "A"
    return {"winner_line": re.sub(r"^[AB],?\s*(narrowly|by a small margin)?[.,]?\s*", "", s1).strip(), "margin": margin,
            "winner_pts": bullets(2), "loser_pts": bullets(3), "one_change": for_letter(7), "act": for_letter(8), "other": other}

evals_json = rj(f"{EV}/evals.json")["evals"]
by_id = {e["id"]: e for e in evals_json}

runs = {}       # key "<eval>|<iter>|<arm>"
evals = []      # ordered selected evals
for it_dir in sorted(glob.glob(f"{EV}/iteration-*")):
    it = int(it_dir.split("-")[-1])
    for ed in sorted(glob.glob(f"{it_dir}/*/")):
        eid = os.path.basename(ed.rstrip("/"))
        meta = rj(f"{ed}/eval_metadata.json")
        single = {}
        arms = sorted(os.path.basename(a.rstrip("/")) for a in glob.glob(f"{ed}/*/") if exists(f"{a}/outputs/report.md"))
        arms = [a for a in arms if a == "with_skill"] + [a for a in arms if a == "without_skill"] + [a for a in arms if a.startswith("with_skill_")]
        for vp, kp, arm_key in [(f"{ed}/judge/verdict.md", f"{ed}/judge/pair.key", "with_skill")] + [(f"{ed}/judge/verdict_v{n}.md", f"{ed}/judge/pair_v{n}.key", f"with_skill_v{n}") for n in range(2, 10)]:
            if exists(vp) and exists(kp):
                key = rd(kp).strip(); letter = "A" if key.startswith("A=with_skill") else "B"
                vt = rd(vp); w = re.search(r"\*\*Winner\*\*:\s*([AB])", vt)
                verdicts_single = {"text": vt, "letter": letter, "won": bool(w and w.group(1) == letter)}
                single[arm_key] = verdicts_single
        verdicts = {}
        for vp in sorted(glob.glob(f"{ed}/judge/verdict_*.md")):
            if re.search(r"verdict_v\d+\.md$", vp): continue
            n = vp.rsplit("_", 1)[1].split(".")[0]
            key = rd(f"{ed}/judge/pair_{n}.key").strip() if exists(f"{ed}/judge/pair_{n}.key") else ""
            m = re.search(r"(with_skill_\d+)", key)
            if not m: continue
            letter = "A" if key.startswith("A=with_skill") else "B"
            vt = rd(vp)
            w = re.search(r"\*\*Winner\*\*:\s*([AB])", vt)
            won = bool(w and w.group(1) == letter)
            verdicts[m.group(1)] = {"text": vt, "letter": letter, "won": won}
        results_md = rd(f"{ed}/RESULTS.md") if exists(f"{ed}/RESULTS.md") else ""
        for arm in arms:
            od = f"{ed}/{arm}/outputs"
            if not exists(f"{od}/report.md"): continue
            g = rj(f"{od}/grading.json") if exists(f"{od}/grading.json") else {"expectations": []}
            t = rj(f"{od}/timing.json") if exists(f"{od}/timing.json") else {}
            rb = rj(f"{od}/reading.json") if exists(f"{od}/reading.json") else {}
            cit = None
            if exists(f"{od}/citation_grading.json"):
                c = rj(f"{od}/citation_grading.json")
                cit = {"sampled": c.get("sampled", []), "estimate": c.get("implausible_total_estimate"),
                       "notes": c.get("implausible_notes") or c.get("notes") or "", "regraded": True}
            elif g.get("citation_sample"):
                cit = {"sampled": g["citation_sample"], "estimate": g.get("implausible_total_estimate"), "notes": "", "regraded": False}
            base_arm = "with_skill" if arm.startswith("with_skill") else "without_skill"
            if re.match(r"with_skill_v\d+$", arm):
                label = f"With skill, round {it}, " + ({"with_skill_v3": "final rules, 29 October"} if eid == "company-brief-corp-jetblue" else {"with_skill_v2": "rules revised after review", "with_skill_v3": "stripped: tool guide and standard only"} if it == 7 else {"with_skill_v2": "body revised", "with_skill_v3": "body revised, table recipe"}).get(arm, "revised " + arm[-2:])
            elif arm.startswith("with_skill_"):
                label = f"With skill, round {it}, run {arm.rsplit('_', 1)[1]}"
            elif arm == "without_skill" and it > 1:
                label = f"Without skill, round {it}"
            else:
                label = ARM[arm] + (f", round {it}" if arm == "with_skill" else "")
            v = verdicts.get(arm) or single.get(arm)
            if v and v.get("text"): v = dict(v, **{"x": parse_verdict(v["text"], v["letter"])})
            allv = dict(verdicts); allv.update(single)
            if arm == "without_skill" and allv:
                v = {"text": "", "letter": "", "won": None, "lost": sum(1 for x in allv.values() if x["won"]), "of": len(allv)}
            runs[f"{eid}|{it}|{arm}"] = {
                "eval": eid, "iter": it, "arm": base_arm, "arm_dir": arm,
                "label": label, "verdict": v, "results": results_md if arm.startswith("with_skill") or (arm == "without_skill" and it > 1) else "",
                "report": rd(f"{od}/report.md"),
                "run_log": rd(f"{od}/run_log.md") if exists(f"{od}/run_log.md") else "",
                "expectations": [{"text": x["text"], "passed": bool(x["passed"]), "evidence": x.get("evidence", "")} for x in g.get("expectations", [])],
                "pass": g.get("pass_count", sum(1 for x in g.get("expectations", []) if x["passed"])),
                "total": g.get("total", len(g.get("expectations", []))),
                "notes": g.get("suspicious", []),
                "citation": cit,
                "tokens": t.get("total_tokens"), "secs": t.get("total_duration_seconds"), "calls": t.get("tool_calls_total"),
                "words": t.get("report_words") or len(rd(f"{od}/report.md").split()),
                "by_name": t.get("tool_calls_by_name", {}),
                "read_before": rb.get("words_before_first_call"), "read_files": [os.path.basename(x["file"]) + " " + str(x["words"]) for x in rb.get("files_read_before_first_call", [])],
                "method_files": len(rb.get("method_files_opened_whole_run", [])) if rb else None,
            }
        if eid not in [e["id"] for e in evals]:
            sk, vo, su = split_id(eid)
            src = by_id.get(eid) or by_id.get(eid.replace("earnings-recap", "earnings-review")) or {"skill": meta.get("skill", ""), "prompt": meta.get("prompt", "")}
            evals.append({"id": eid, "skill": sk, "skill_id": src["skill"], "voice": vo, "subject": su,
                          "label": f"{sk}: {su}", "prompt": src["prompt"], "first_round": it})
from collections import Counter as _C
_lc = _C(e["label"] for e in evals)
for e in evals:
    if _lc[e["label"]] > 1: e["label"] = f'{e["label"]} ({"PM" if e["voice"] == "PM" else e["voice"].lower()})'
for e in evals:
    ks = [k for k in runs if k.startswith(e["id"] + "|")]
    def order(k):
        _, it, arm = k.split("|"); it = int(it)
        return (it, 0 if arm == "with_skill" else 1 if arm == "without_skill" else 2, arm)
    e["run_keys"] = [k.split("|", 1)[1] for k in sorted(ks, key=order)]

spare = []
run_ids = {k.split("|")[0] for k in runs}
for e in evals_json:
    if e.get("selected") or e["id"] in run_ids or e["id"].replace("earnings-review", "earnings-recap") in run_ids: continue
    sk, vo, su = split_id(e["id"])
    spare.append({"skill": sk, "voice": vo, "subject": su, "prompt": e["prompt"]})

# Overview rows
def k(n): return "" if n is None else f"{round(n/1000):,}k"
def mins(s): return "" if s is None else f"{s/60:.1f}"
rows = []
for e in evals:
    fr = e.get("first_round", 1)
    a = runs.get(f"{e['id']}|1|with_skill") or runs[f"{e['id']}|{fr}|with_skill"]; b = runs.get(f"{e['id']}|1|without_skill") or runs[f"{e['id']}|{fr}|without_skill"]; c = runs.get(f"{e['id']}|2|with_skill"); d = runs.get(f"{e['id']}|3|with_skill")
    pairs = []
    for rk in e["run_keys"]:
        r = runs[f"{e['id']}|{rk}"]
        if r["arm"] == "with_skill" and r["verdict"] and r["verdict"].get("won") is not None:
            pairs.append({"key": rk, "round": r["iter"], "won": r["verdict"]["won"], "margin": r["verdict"].get("x", {}).get("margin", ""), "label": r["label"]})
    e["pairs"] = pairs
    if pairs:
        last = pairs[-1]; e["standing"] = "ahead" if last["won"] else "behind"
        outcome = ("won" if last["won"] else "lost") + (", " + last["margin"] if last["margin"] else "")
        e["latest"] = last["key"]
    else:
        e["standing"] = "assertions"; outcome = ""; e["latest"] = None
    hist = " \u00b7 ".join(f"R{p['round']} {'won' if p['won'] else 'lost'}" for p in pairs)
    r13 = (f"{a['pass']}/{a['total']} vs {b['pass']}/{b['total']}, {a['pass']-b['pass']:+d}" if a["total"] else "")
    if c: r13 += f"; R2 {c['pass']}/{c['total']}"
    if d: r13 += f"; R3 {d['pass']}/{d['total']}"
    rows.append({"eval": e["label"], "id": e["id"], "voice": e["voice"], "standing": e["standing"], "outcome": outcome, "runs": hist, "r13": r13,
                 "with": f"{a['pass']}/{a['total']}" if a["total"] else "", "without": f"{b['pass']}/{b['total']}" if b["total"] else "",
                 "r2": f"{c['pass']}/{c['total']}" if c else ("not rerun" if fr == 1 else ""), "r3": f"{d['pass']}/{d['total']}" if d else "", "gain": (f"{a['pass']-b['pass']:+d}" if a["pass"]!=b["pass"] else "0") if a["total"] else "",
                 "words": f"{a['words']:,} / {b['words']:,}", "tokens": f"{k(a['tokens'])} / {k(b['tokens'])}",
                 "minutes": f"{mins(a['secs'])} / {mins(b['secs'])}"})
groups = [{"key": "behind", "title": "Skill behind", "note": "the latest judged with-skill note lost its blind pair", "rows": [r for r in rows if r["standing"] == "behind"]},
          {"key": "ahead", "title": "Skill ahead", "note": "the latest judged with-skill note won its blind pair", "rows": [r for r in rows if r["standing"] == "ahead"]},
          {"key": "assertions", "title": "Assertion rounds only", "note": "26 to 27 October, graded against a checklist, never judged blind", "rows": [r for r in rows if r["standing"] == "assertions"]}]
judged = [e for e in evals if e["pairs"]]
n_behind = sum(1 for e in judged if e["standing"] == "behind"); n_ahead = len(judged) - n_behind
n_close = sum(1 for e in judged if e["pairs"][-1]["margin"] in ("close", "narrowly", "moderately close"))
behind_names = [e["label"] for e in judged if e["standing"] == "behind"]
summary = (f"Blind pairs on the latest rules: the skill is ahead on {n_ahead} prompts and behind on {n_behind}"
           + (f" ({', '.join(behind_names)})" if behind_names else "") + f"; {n_close} of {len(judged)} latest verdicts are within the judge's own margin (\"close\" or \"narrowly\").")

r1 = [e for e in evals if f"{e['id']}|1|with_skill" in runs]
tot_w = sum(runs[f"{e['id']}|1|with_skill"]["pass"] for e in r1); tot_wt = sum(runs[f"{e['id']}|1|with_skill"]["total"] for e in r1)
tot_o = sum(runs[f"{e['id']}|1|without_skill"]["pass"] for e in r1); tot_ot = sum(runs[f"{e['id']}|1|without_skill"]["total"] for e in r1)
n_runs = len(runs); n_words = sum(r["words"] for r in runs.values())

fonts = rd(f"{INPUTS}/fonts-platform.css")
logo = rd(f"{INPUTS}/logo.datauri").strip()
logo_dark = rd(f"{INPUTS}/logo-dark.datauri").strip() if exists(f"{INPUTS}/logo-dark.datauri") else logo
produced = time.strftime("%d %b %Y, %H:%M %Z")

data = {"evals": evals, "runs": runs, "rows": rows, "groups": groups, "spare": spare, "summary": summary}
data_json = json.dumps(data, ensure_ascii=True).replace("</", "<\\/")

spare_html = "".join(
    f'<div class="spare"><div class="spare-h"><b>{s["skill"]}: {s["subject"]}</b><span>{s["voice"]} reader</span></div><p>{s["prompt"]}</p></div>'
    for s in spare)

page = f"""<title>Skills Eval Reader</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
{fonts}
/* Layout: one 1400px column; the two-pane reader with its own run selectors is the one bold element, the overview table above it is the way in. */
:root {{
  --surface-0: #121212; --dp01: #1E1E1E; --dp03: #252525; --dp08: #2E2E2E; --dp12: #333333;
  --fg-1: #FFFDF5; --fg-2: #FFFDF5B2; --fg-3: #FFFDF580; --border: #FFFFFF29;
  --bd-blue: #4CA7F9; --bd-blue-700: #206EB5; --overlay-blue: rgba(83,166,251,0.12);
  --green-500: #04E0A9; --overlay-green: rgba(3,166,125,0.18); --red-500: #FC4848; --overlay-red: rgba(207,102,121,0.18); --overlay-yellow: rgba(235,183,30,0.12);
  --bg: var(--surface-0); --surface: var(--dp01); --surface-2: var(--dp03); --line: var(--border);
  --ink: var(--fg-1); --ink-2: var(--fg-2); --muted: #A9A79F; --accent: var(--bd-blue);
  --font-display: "Moderno", "Hanken Grotesk", serif; --font-sans: "Hanken Grotesk", "Inter", system-ui, sans-serif; --font-mono: "Apercu Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --k-page-width: 1400px;
  color-scheme: dark;
}}
:root[data-theme="light"] {{
  --surface-0: #F4F3EF; --dp01: #FCFCFB; --dp03: #EEEDE8; --dp08: #E6E5DF; --dp12: #DCDAD3;
  --fg-1: #14161A; --fg-2: #464A51; --fg-3: #6C7178; --border: #00000024;
  --bd-blue: #206EB5; --overlay-blue: rgba(32,110,181,0.12); --green-500: #03795B; --overlay-green: rgba(3,166,125,0.16); --red-500: #C62828; --overlay-red: rgba(207,102,121,0.16);
  --muted: #6C7178; --accent: var(--bd-blue);
  color-scheme: light;
}}
html {{ background: var(--bg); }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--font-sans); font-size: 15px; line-height: 1.55; margin: 0; -webkit-font-smoothing: antialiased; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
a {{ color: var(--accent); text-decoration: none; }} a:hover {{ text-decoration: underline; }}
[hidden] {{ display: none !important; }}
main.page {{ padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); padding-block: 32px 96px; }}
header.top {{ margin-bottom: 48px; }}
.k-rail-head img {{ width: 128px; }}
.k-rail-head img.logo-on-light {{ display: none; }}
:root[data-theme="light"] .k-rail-head img.logo-on-dark {{ display: none; }}
:root[data-theme="light"] .k-rail-head img.logo-on-light {{ display: block; }}
header.top .eyebrow {{ font-size: 11px; letter-spacing: .18em; text-transform: uppercase; color: var(--fg-2); font-weight: 600; margin-bottom: 12px; }}
header.top h1 {{ font-family: var(--font-display); font-weight: 400; font-size: 44px; line-height: 1.05; letter-spacing: -0.01em; margin: 0 0 12px; text-wrap: balance; }}
header.top .sub {{ color: var(--fg-2); font-size: 15px; max-width: 70ch; margin: 0; }}
header.top .meta {{ color: var(--fg-3); font-size: 13px; margin-top: 12px; font-variant-numeric: tabular-nums; }}
header.top .meta a {{ color: var(--fg-2); }}
.keys {{ font-size: 13px; color: var(--fg-3); margin-top: 8px; }}
.keys kbd {{ font-family: var(--font-mono); font-size: 12px; border: 1px solid var(--line); border-radius: 4px; padding: 1px 6px; color: var(--ink-2); }}
section[id] {{ margin-bottom: 48px; }}
h2 {{ font-size: 24px; font-weight: 600; line-height: 1.2; margin: 0 0 12px; text-wrap: balance; }}
.lead {{ color: var(--fg-2); margin: 0 0 16px; max-width: 80ch; }}
strong {{ font-weight: 600; }}

/* Overview table: cells hold "with / without" pairs */
#ov .k-table td {{ font-variant-numeric: tabular-nums; white-space: nowrap; }}
#ov .k-table th, #ov .k-table td {{ padding-left: 8px; padding-right: 8px; }}
#ov .k-table tbody tr.k-row {{ cursor: pointer; }}
#ov .k-table tbody tr.k-row:hover td {{ background: var(--surface-2); }}
#ov .k-table tbody tr.k-row.sel td {{ background: var(--overlay-blue); }}
#ov .k-table td:first-child {{ white-space: normal; font-weight: 600; }}
.ov-foot {{ font-size: 13px; color: var(--fg-3); margin-top: 8px; }}
.ov-sum {{ font-size: 15px; margin: 0 0 16px; max-width: 100ch; }}
.ov-sum b {{ font-weight: 600; }}
.ov-group {{ margin-top: 20px; }}
.ov-group h3 {{ font-size: 15px; font-weight: 600; margin: 0 0 6px; display: flex; gap: 10px; align-items: baseline; }}
.ov-group h3 small {{ font-weight: 400; color: var(--fg-3); font-size: 13px; }}
.ov-group .k-table-tools {{ display: none; }}
#ov .k-table td:nth-child(3), #ov .k-table td:nth-child(4) {{ white-space: normal; }}
#ov .k-table tbody tr.st-behind td:first-child {{ box-shadow: inset 3px 0 0 var(--red-500); }}
#ov .k-table tbody tr.st-ahead td:first-child {{ box-shadow: inset 3px 0 0 var(--green-500); }}
.tok {{ font-weight: 600; }}
.tok.won {{ color: var(--green-500); }} .tok.lost {{ color: var(--red-500); }}
.tok-m {{ color: var(--fg-2); font-weight: 400; }}
.runtok {{ cursor: pointer; white-space: nowrap; }} .runtok:hover {{ text-decoration: underline; }}
.runtok + .runtok::before {{ content: "\00b7"; color: var(--fg-3); margin: 0 6px; text-decoration: none; display: inline-block; }}
.vstrip {{ border: 1px solid var(--line); border-radius: 8px; background: var(--surface); padding: 10px 14px; margin: 0 0 16px; font-size: 14px; display: flex; gap: 12px; align-items: baseline; flex-wrap: wrap; }}
.vstrip .vs-k {{ font-size: 12px; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); white-space: nowrap; }}
.vstrip .vs-v {{ max-width: 110ch; }}
.pane-res {{ font-size: 13px; font-weight: 600; }}
.pane-res.won {{ color: var(--green-500); }} .pane-res.lost {{ color: var(--red-500); }} .pane-res.none {{ color: var(--fg-3); font-weight: 400; }}
.why {{ border: 1px solid var(--line); border-left: 3px solid var(--red-500); border-radius: 0 8px 8px 0; background: var(--surface-2); padding: 12px 14px; margin: 0 0 20px; font-size: 14px; }}
.why.won {{ border-left-color: var(--green-500); }}
.why h4 {{ margin: 0 0 8px; font-size: 13px; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); font-weight: 500; }}
.why dt {{ font-weight: 600; margin-top: 8px; }} .why dd {{ margin: 2px 0 0; color: var(--ink-2); }} .why dl {{ margin: 0; }}
.why ul {{ margin: 2px 0 0; padding-left: 18px; color: var(--ink-2); }}

/* Reader controls */
.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; background: var(--bg); border-bottom: 1px solid var(--line); margin: 0 0 16px; padding: 10px 0; display: flex; flex-wrap: wrap; gap: 12px 16px; align-items: center; }}
.bar label {{ font-size: 13px; color: var(--fg-2); display: flex; align-items: center; gap: 8px; min-width: 0; max-width: 100%; }}
.bar select {{ background: var(--surface); color: var(--ink); border: 1px solid var(--line); border-radius: 4px; padding: 7px 10px; font: inherit; font-size: 14px; min-width: 0; flex: 1 1 auto; max-width: 100%; }}
.seg {{ display: inline-flex; border: 1px solid var(--line); border-radius: 35px; overflow: hidden; background: var(--surface); }}
.seg button {{ background: transparent; color: var(--ink-2); border: 0; padding: 6px 14px; font: inherit; font-size: 13px; cursor: pointer; white-space: nowrap; }}
.seg button + button {{ border-left: 1px solid var(--line); }}
.seg button[aria-pressed="true"] {{ background: var(--overlay-blue); color: var(--ink); }}
.seg button:hover {{ color: var(--ink); }}
.seg button:focus-visible {{ outline-offset: -3px; }}
.nav-btn {{ background: var(--surface); color: var(--ink-2); border: 1px solid var(--line); border-radius: 35px; padding: 6px 14px; font: inherit; font-size: 13px; cursor: pointer; }}
.nav-btn:hover {{ color: var(--ink); background: var(--surface-2); }}
.nav-btn[disabled] {{ opacity: .4; cursor: default; }}

/* Prompt */
.prompt {{ border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 0 8px 8px 0; background: var(--surface); padding: 12px 14px; margin: 0 0 16px; }}
.prompt .ph {{ display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 13px; color: var(--fg-2); margin-bottom: 6px; }}
.prompt .ph b {{ color: var(--ink); font-weight: 600; }}
.prompt .ph code {{ font-family: var(--font-mono); font-size: 12px; color: var(--fg-2); }}
.prompt p {{ margin: 0; max-width: 100ch; }}

/* Panes */
.panes {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
.panes.one {{ grid-template-columns: 1fr; }}
.panes.one .pane[data-side="R"] {{ display: none; }}
.pane {{ border: 1px solid var(--line); border-radius: 8px; background: var(--surface); min-width: 0; display: flex; flex-direction: column; }}
.pane-h {{ padding: 10px 16px; border-bottom: 1px solid var(--line); display: flex; flex-direction: column; gap: 8px; }}
.pane-h .row {{ display: flex; flex-wrap: wrap; gap: 8px 20px; align-items: center; }}
.pane-h .seg {{ flex-wrap: wrap; border-radius: 8px; }}
.stats {{ display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 13px; color: var(--fg-2); margin: 0; font-variant-numeric: tabular-nums; }}
.stats div {{ display: flex; gap: 5px; align-items: baseline; }}
.stats dt {{ color: var(--fg-3); }}
.stats dd {{ margin: 0; color: var(--ink); }}
.stats dd.pass {{ font-family: var(--font-mono); }}
.tabs {{ display: flex; gap: 2px; }}
.tabs button {{ background: transparent; color: var(--fg-2); border: 0; border-bottom: 2px solid transparent; padding: 4px 10px 6px; font: inherit; font-size: 13px; cursor: pointer; }}
.tabs button[aria-selected="true"] {{ color: var(--ink); border-bottom-color: var(--accent); }}
.tabs button:hover {{ color: var(--ink); }}
.pane-b {{ padding: 14px 16px 24px; overflow: auto; height: calc(100vh - 250px); min-height: 480px; overscroll-behavior: contain; }}

/* Rendered reports */
.doc {{ font-size: 14.5px; line-height: 1.6; }}
.doc > :first-child {{ margin-top: 0; }}
.doc h1 {{ font-size: 21px; font-weight: 600; line-height: 1.25; margin: 0 0 12px; }}
.doc h2 {{ font-size: 17px; font-weight: 600; margin: 24px 0 8px; }}
.doc h3 {{ font-size: 15px; font-weight: 600; margin: 18px 0 6px; }}
.doc h4, .doc h5, .doc h6 {{ font-size: 14px; font-weight: 600; margin: 14px 0 4px; }}
.doc p {{ margin: 0 0 10px; }}
.doc ul, .doc ol {{ margin: 0 0 10px; padding-left: 22px; }}
.doc li {{ margin: 0 0 3px; }}
.doc li::marker {{ color: var(--fg-3); }}
.doc em {{ font-style: italic; }}
.doc hr {{ border: 0; border-top: 1px solid var(--line); margin: 16px 0; }}
.doc blockquote {{ margin: 0 0 10px; padding: 2px 12px; border-left: 2px solid var(--line); color: var(--fg-2); }}
.doc code {{ font-family: var(--font-mono); font-size: 0.9em; background: var(--surface-2); padding: 0.05em 0.35em; border-radius: 4px; overflow-wrap: anywhere; }}
.doc pre {{ font-family: var(--font-mono); font-size: 12.5px; line-height: 1.5; background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 10px 12px; overflow-x: auto; margin: 0 0 10px; }}
.doc pre code {{ background: none; padding: 0; }}
.doc .tbl {{ overflow-x: auto; margin: 0 0 12px; border: 1px solid var(--line); border-radius: 8px; }}
.doc table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
.doc th, .doc td {{ text-align: left; vertical-align: top; padding: 5px 9px; border-bottom: 1px solid var(--line); }}
.doc th {{ font-weight: 600; color: var(--fg-2); white-space: nowrap; background: var(--surface-2); }}
.doc tr:last-child td {{ border-bottom: 0; }}
.doc td {{ min-width: 7ch; }}
.doc a {{ overflow-wrap: anywhere; }}

/* Grades */
.gr {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 10px; }}
.gr li {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: start; }}
.mark {{ font-family: var(--font-mono); font-size: 11px; letter-spacing: .04em; text-transform: uppercase; border-radius: 4px; padding: 2px 0; text-align: center; font-weight: 600; margin-top: 3px; }}
.mark.p {{ background: var(--overlay-green); color: var(--green-500); }}
.mark.f {{ background: var(--overlay-red); color: var(--red-500); }}
.mark.n {{ background: var(--surface-2); color: var(--fg-3); }}
.gr .at {{ font-size: 14px; }}
.gr .ev {{ font-size: 13px; color: var(--fg-2); margin-top: 2px; }}
.gh {{ font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--fg-3); font-weight: 600; margin: 22px 0 8px; }}
.gh:first-child {{ margin-top: 0; }}
.notes {{ margin: 0; padding-left: 20px; font-size: 13.5px; color: var(--ink-2); }}
.notes li {{ margin-bottom: 6px; }}
.cit-note {{ font-size: 13px; color: var(--fg-2); margin: 8px 0 0; }}

/* Side-by-side grades fold */
details.k-fold {{ margin: 0 0 16px; }}
details.k-fold > summary {{ font-size: 14px; }}
.cmp {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
.cmp th, .cmp td {{ text-align: left; vertical-align: top; padding: 6px 10px; border-bottom: 1px solid var(--line); }}
.cmp th {{ font-size: 12px; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); font-weight: 500; white-space: nowrap; }}
.cmp td.m {{ width: 64px; }}
.cmp tr:last-child td {{ border-bottom: 0; }}
.cmp tr.diff td:first-child {{ color: var(--ink); font-weight: 600; }}

/* Spare prompts, method */
.spare {{ padding: 10px 0; border-bottom: 1px solid var(--line); }}
.spare:last-child {{ border-bottom: 0; }}
.spare-h {{ display: flex; flex-wrap: wrap; gap: 4px 12px; font-size: 13px; color: var(--fg-2); margin-bottom: 2px; }}
.spare-h b {{ color: var(--ink); }}
.spare p {{ margin: 0; max-width: 100ch; font-size: 14px; }}
.k-fold-body p {{ max-width: 80ch; margin: 0 0 10px; }}
.k-fold-body ul {{ max-width: 80ch; margin: 0 0 10px; padding-left: 22px; }}

@media (max-width: 900px) {{
  header.top h1 {{ font-size: 34px; }}
  .bar label {{ flex: 1 1 100%; }}
  #ov .k-table {{ min-width: 900px; }}
  #ov .k-table td:first-child {{ white-space: nowrap; }}
  #ov .k-table col {{ width: auto !important; }}
  #ov .k-table {{ table-layout: auto !important; }}
  .panes {{ grid-template-columns: 1fr; }}
  .panes:not(.one) .pane[data-side="R"] {{ display: flex; }}
  .pane-b {{ height: auto; min-height: 0; overflow: visible; }}
  .seg button {{ font-size: 12px; padding: 6px 9px; }}
  .pane-h {{ position: sticky; top: 60px; background: var(--surface); z-index: 5; border-radius: 8px 8px 0 0; }}
}}
</style>
<!-- kit: tooltip rail fold table search -->
<nav class="k-rail" aria-label="Contents"><div class="k-rail-head"><img class="logo-on-dark" src="{logo}" alt="Bigdata.com"><img class="logo-on-light" src="{logo_dark}" alt="Bigdata.com"><span>Eval reader</span></div><ul></ul></nav>
<main class="k-page page">
<header class="top">
  <div>
    <div class="eyebrow">Bigdata.com skills, quality evals</div>
    <h1>Skills Eval Reader</h1>
    <p class="sub">The full text of every run from the quality evals of the Bigdata.com skills, 26 to 28 October 2026: fifteen prompts, each answered with the skill and without it, plus the repeats after each revision of the skills and the library. Pick a prompt, then read the two reports side by side with their grades and run logs.</p>
    <div class="meta">Produced {produced}. {n_runs} runs, {n_words:,} words. Score tables and the audit write-up are on the <a href="{PROPOSAL_URL}" target="_blank" rel="noopener">Job Skills Proposal</a> page.</div>
    <div class="keys">Keys: <kbd>[</kbd> and <kbd>]</kbd> move to the previous and next prompt, <kbd>Cmd</kbd>+<kbd>K</kbd> searches the page.</div>
  </div>
</header>

<section id="overview" data-rail="Overview" data-rail-note="10">
  <h2>Overview</h2>
  <p class="lead">One row per prompt, grouped by where the skill stands. <strong>Outcome</strong> is the latest blind verdict on the with-skill note: a Fable judge read it and the same-day no-skill note without knowing which was which, and the margin is the judge's own word. <strong>Runs</strong> lists every judged with-skill run in order, oldest first; click one to open it. <strong>Rounds 1 to 3</strong> are the earlier checklist scores, with skill against without, from 26 to 27 October. Words and tokens read with skill / without skill. Click a row to open the pair with the verdict.</p>
  <p class="ov-sum" id="ov-sum"></p>
  <div id="ov" data-search="Overview table" data-search-hint="Table"></div>
  <div class="ov-foot">Checklist rounds: round 1 totals with skill {tot_w}/{tot_wt}, without skill {tot_o}/{tot_ot}; round 2 repeated four with-skill runs after the library fixes on one more assertion; round 3 repeated them on 27 October after the bodies were rewritten. From round 4 (28 October) every run is judged by blind comparison instead.</div>
</section>

<section id="reader" data-rail="Read the runs" data-rail-note="{n_runs}">
  <h2>Read the runs</h2>
  <div class="bar">
    <label>Prompt <select id="ev" aria-label="Prompt"></select></label>
    <button class="nav-btn" id="prev" type="button" aria-label="Previous prompt">Previous</button>
    <button class="nav-btn" id="next" type="button" aria-label="Next prompt">Next</button>
    <div class="seg" role="group" aria-label="Layout" id="layout">
      <button type="button" data-layout="two" aria-pressed="true">Side by side</button>
      <button type="button" data-layout="one" aria-pressed="false">One pane</button>
    </div>
  </div>
  <div class="prompt" id="prompt"></div>
  <div class="vstrip" id="vstrip" hidden></div>
  <details class="k-fold" id="cmp"><summary>Assertions side by side</summary><div class="k-fold-body" id="cmp-body"></div></details>
  <div class="panes" id="panes">
    <div class="pane" data-side="L"></div>
    <div class="pane" data-side="R"></div>
  </div>
</section>

<section id="method" data-rail="Method">
  <h2>How the runs were made</h2>
  <div class="k-fold-body" style="padding:0">
  <p>Each of the ten prompts was written on 26 October 2026 from that day's news, in the words a portfolio manager or a corporate strategy, treasury or investor-relations reader would use. Each ran twice with a fresh Claude Opus agent at high effort: once after reading the skill's instructions and its library, once with the Bigdata.com tools alone. Neither run had web tools. Four prompts carried a premise that was not true (a guidance cut, a lowered outlook, a price move, a yield level); both arms were left to check it.</p>
  <p>One Claude Sonnet grader per run scored 11 to 13 assertions against the report. Six are shared by every prompt and mirror the output standard (sources and dates on material facts, no unfinished-work markers, tables of at most eight columns, a gaps note, a closing watch list, framing for the stated reader). The rest are specific to the skill under test. The grader also left notes on anything it found suspicious, shown under Grades. Round 2 repeated four with-skill runs after the library fixes, with a citation-fidelity assertion that samples five citations and checks that each points at a document that could plausibly hold the fact; the round 1 reports for those four were regraded on the same sample. Round 3, on 27 October, repeated one prompt (the Amazon earnings preview) after the skill bodies were rewritten as guidelines and the library was stripped; its pane header also shows how much skill and library text the agent read before its first Bigdata.com call.</p>
  <p>Round 4, on 28 October, followed the packaging rewrite of the earnings-preview skill and the library files it loads: no author, paper or book named, formulas and tables named by content rather than numbered, no procedures inside reference files, and an output standard under which an assumption is stated once in plain words and nothing else is labelled. Three fresh with-skill runs and one fresh no-skill run were made the same afternoon, then three Claude Sonnet judges each read one with-skill note beside the no-skill note with the order randomised and said which an expert would rather have and why. No assertion grades were run for round 4; the blind verdict, the word count and the tokens are the measures. A scan of each note for library file names, formula or table numbers, primer or source names, and basis labels found none in any round-4 note.</p>
  <p>Tokens are the agent's total input and output tokens for the run. Minutes are wall-clock time from launch to the final message. Tool calls count every call, including file reads of the skill and Bigdata.com calls.</p>
  </div>
  <details class="k-fold" id="spare"><summary>{len(spare)} prompts drafted but not run<small>spares from 26 October</small></summary><div class="k-fold-body">{spare_html}</div></details>
</section>
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js" integrity="sha384-/TQbtLCAerC3jgaim+N78RZSDYV7ryeoBCVqTuzRrFec2akfBkHS7ACQ3PQhvMVi" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.0.9/purify.min.js" integrity="sha384-3HPB1XT51W3gGRxAmZ+qbZwRpRlFQL632y8x+adAqCr4Wp3TaWwCLSTAJJKbyWEK" crossorigin="anonymous"></script>
<script type="application/json" id="data">{data_json}</script>
<script>
(function () {{
  var DATA = JSON.parse(document.getElementById("data").textContent);
  var EVALS = DATA.evals, RUNS = DATA.runs;
  var state = {{ ev: EVALS[0].id, L: {{ run: "1|with_skill", tab: "report" }}, R: {{ run: "1|without_skill", tab: "report" }}, layout: "two" }};
  try {{ var saved = JSON.parse(localStorage.getItem("eval-reader") || "null"); if (saved && saved.layout) state.layout = saved.layout; }} catch (e) {{}}
  var hashId = location.hash.slice(1); if (hashId && byId(hashId)) state.ev = hashId;
  if (window.innerWidth < 900) state.layout = "one";   /* a phone shows one full-length pane; the run selector switches it */

  function byId(id) {{ for (var i = 0; i < EVALS.length; i++) if (EVALS[i].id === id) return EVALS[i]; return null; }}
  function idx(id) {{ for (var i = 0; i < EVALS.length; i++) if (EVALS[i].id === id) return i; return -1; }}
  function el(tag, cls, text) {{ var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }}
  function fmtK(n) {{ return n == null ? "\\u2013" : Math.round(n / 1000).toLocaleString("en-US") + "k"; }}
  function fmtMin(s) {{ return s == null ? "\\u2013" : (s / 60).toFixed(1); }}
  function fmtN(n) {{ return n == null ? "\\u2013" : n.toLocaleString("en-US"); }}
  function save() {{ try {{ localStorage.setItem("eval-reader", JSON.stringify({{ layout: state.layout }})); }} catch (e) {{}} }}
  function runsFor(id) {{ var e = byId(id); var out = []; (e && e.run_keys ? e.run_keys : ["1|with_skill", "1|without_skill", "2|with_skill", "3|with_skill"]).forEach(function (k) {{ if (RUNS[id + "|" + k]) out.push(k); }}); return out; }}
  function run(side) {{ return RUNS[state.ev + "|" + state[side].run]; }}

  function renderMd(md) {{
    var box = el("div", "doc");
    var html = marked.parse(md, {{ gfm: true, breaks: false }}); box.innerHTML = window.DOMPurify ? DOMPurify.sanitize(html) : html;
    Array.prototype.forEach.call(box.querySelectorAll("table"), function (t) {{ var w = el("div", "tbl"); t.parentNode.insertBefore(w, t); w.appendChild(t); }});
    Array.prototype.forEach.call(box.querySelectorAll("a[href]"), function (a) {{ if (!/^https?:\/\//i.test(a.getAttribute("href"))) {{ a.removeAttribute("href"); return; }} a.target = "_blank"; a.rel = "noopener"; }});
    return box;
  }}
  function mark(v) {{ return el("span", "mark " + (v === true ? "p" : v === false ? "f" : "n"), v === true ? "pass" : v === false ? "fail" : "\\u2013"); }}

  function renderGrades(r) {{
    var box = el("div");
    box.appendChild(el("div", "gh", "Assertions, " + r.pass + " of " + r.total + " passed" + (r.pass < r.total ? ", failures first" : "")));
    var ul = el("ul", "gr");
    r.expectations.filter(function (x) {{ return !x.passed; }}).concat(r.expectations.filter(function (x) {{ return x.passed; }})).forEach(function (x) {{
      var li = el("li"); li.appendChild(mark(x.passed));
      var d = el("div"); d.appendChild(el("div", "at", x.text)); if (x.evidence) d.appendChild(el("div", "ev", x.evidence)); li.appendChild(d); ul.appendChild(li);
    }});
    box.appendChild(ul);
    if (r.notes && r.notes.length) {{
      box.appendChild(el("div", "gh", "Grader's notes"));
      var ol = el("ul", "notes"); r.notes.forEach(function (n) {{ ol.appendChild(el("li", null, n)); }}); box.appendChild(ol);
    }}
    if (r.citation) {{
      var c = r.citation;
      box.appendChild(el("div", "gh", "Citation sample, " + c.sampled.filter(function (s) {{ return s.plausible; }}).length + " of " + c.sampled.length + " plausible" + (c.regraded ? " (regraded after round 2)" : "")));
      var cl = el("ul", "gr");
      c.sampled.forEach(function (s) {{
        var li = el("li"); li.appendChild(mark(!!s.plausible));
        var d = el("div"); d.appendChild(el("div", "at", s.claim));
        var ev = []; if (s.citation) ev.push("Cited: " + s.citation); if (s.source_title) ev.push("Source: " + s.source_title); if (s.why) ev.push(s.why);
        if (ev.length) d.appendChild(el("div", "ev", ev.join(" \\u2014 ").replace(/ \\u2014 /g, ". ")));
        li.appendChild(d); cl.appendChild(li);
      }});
      box.appendChild(cl);
      var est = el("p", "cit-note", "Implausible citations the grader estimated across the whole report: " + (c.estimate == null ? "not estimated" : c.estimate) + (c.notes ? ". " + c.notes : ""));
      box.appendChild(est);
    }}
    return box;
  }}

  function renderWhy(r) {{
    if (!(r.arm === "with_skill" && r.verdict && r.verdict.won != null && r.verdict.x)) return null;
    var x = r.verdict.x, won = r.verdict.won, box = el("div", "why" + (won ? " won" : ""));
    box.appendChild(el("h4", null, (won ? "Why it won, in the judge's words" : "Why it lost, in the judge's words") + " (this note is " + r.verdict.letter + ", the no-skill note is " + x.other + ")"));
    var dl = el("dl");
    function item(k, v) {{ if (!v || (v.length === 0)) return; dl.appendChild(el("dt", null, k)); var dd = el("dd"); if (typeof v === "string") dd.textContent = v; else {{ var ul = el("ul"); v.forEach(function (s) {{ ul.appendChild(el("li", null, s)); }}); dd.appendChild(ul); }} dl.appendChild(dd); }}
    item("The verdict", x.winner_line);
    item(won ? "What this note has that the no-skill note does not" : "What the no-skill note has that this note does not", won ? x.winner_pts : x.winner_pts);
    item(won ? "What the no-skill note still does better" : "What this note still does better", x.loser_pts);
    item("The one change the judge asked for", x.one_change);
    item("Could the reader act on it", x.act);
    box.appendChild(dl);
    var more = el("p", "cit-note", "The full verdict is on the Blind verdict tab."); box.appendChild(more);
    return box;
  }}

  function renderPane(side) {{
    var host = document.querySelector('.pane[data-side="' + side + '"]'); host.textContent = "";
    var keys = runsFor(state.ev); if (keys.indexOf(state[side].run) < 0) state[side].run = side === "L" ? keys[0] : (keys[1] || keys[0]);
    var r = run(side);
    var h = el("div", "pane-h");
    var res = null;
    if (r.arm === "with_skill" && r.verdict && r.verdict.won != null) {{
      var xm = (r.verdict.x || {{}}).margin;
      res = el("div", "pane-res " + (r.verdict.won ? "won" : "lost"), (r.verdict.won ? "Won the blind pair" : "Lost the blind pair") + (xm ? ", " + xm : ""));
    }} else if (r.arm === "without_skill" && r.verdict && r.verdict.of) {{
      var wn = r.verdict.of - r.verdict.lost;
      res = el("div", "pane-res " + (wn > 0 ? "won" : "lost"), "Won " + wn + " of " + r.verdict.of + " blind pair" + (r.verdict.of === 1 ? "" : "s") + " against the with-skill runs");
    }} else if (r.arm === "with_skill" && r.total > 0) res = el("div", "pane-res none", "Checklist round, not judged blind");
    if (res) h.appendChild(res);
    var row1 = el("div", "row");
    var seg = el("div", "seg"); seg.setAttribute("role", "group"); seg.setAttribute("aria-label", "Run shown in the " + (side === "L" ? "left" : "right") + " pane");
    keys.forEach(function (k) {{
      var b = el("button", null, RUNS[state.ev + "|" + k].label); b.type = "button"; b.setAttribute("aria-pressed", String(k === state[side].run));
      b.addEventListener("click", function () {{ state[side].run = k; renderPane(side); renderCompare(); renderStrip(); }}); seg.appendChild(b);
    }});
    row1.appendChild(seg);
    var tabs = el("div", "tabs"); tabs.setAttribute("role", "tablist");
    var tabList = [["report", "Report"]]; if (r.total > 0) tabList.push(["grades", "Grades"]); if (r.verdict && r.verdict.text) tabList.push(["verdict", "Blind verdict"]); if (r.results) tabList.push(["results", "Round notes"]); tabList.push(["log", "Run log"]);
    if (!tabList.some(function (t) {{ return t[0] === state[side].tab; }})) state[side].tab = "report";
    tabList.forEach(function (t) {{
      var b = el("button", null, t[1]); b.type = "button"; b.setAttribute("role", "tab"); b.setAttribute("aria-selected", String(t[0] === state[side].tab));
      b.addEventListener("click", function () {{ state[side].tab = t[0]; renderPane(side); }}); tabs.appendChild(b);
    }});
    row1.appendChild(tabs); h.appendChild(row1);
    var st = el("dl", "stats");
    function stat(k, v, tip, cls) {{ var d = el("div"); d.appendChild(el("dt", null, k)); var dd = el("dd", cls, v); d.appendChild(dd); if (tip) {{ d.setAttribute("data-tip", tip); d.tabIndex = 0; }} st.appendChild(d); }}
    if (r.total > 0) stat("Passed", r.pass + "/" + r.total, "Assertions passed over assertions graded by the Sonnet grader", "pass");
    if (r.verdict && r.verdict.won != null) stat("Blind pair", r.verdict.won ? "won" : "lost", "A judge (Sonnet in round 4, Fable in round 5) read this note and the same-day no-skill note with the order randomised (this note was Report " + r.verdict.letter + ") and picked the one an expert would rather have", r.verdict.won ? "pass" : "");
    else if (r.verdict && r.verdict.of) stat("Blind pairs", "lost " + r.verdict.lost + " of " + r.verdict.of, "This no-skill note was judged blind against each with-skill run of the same round", "");
    stat("Words", fmtN(r.words), "Words in the report");
    stat("Tokens", fmtK(r.tokens), "Input and output tokens the agent used in the run");
    stat("Minutes", fmtMin(r.secs), "Wall-clock time from launch to the final message");
    if (r.read_before != null) stat("Read first", fmtN(r.read_before), "Words of skill and library text the agent read before its first Bigdata.com call: " + (r.read_files || []).join(", ") + (r.method_files != null ? ". Method files opened over the run: " + r.method_files : ""));
    stat("Tool calls", fmtN(r.calls), Object.keys(r.by_name || {{}}).map(function (k) {{ return k.replace(/^mcp__claude_ai_Bigdata_com(_2)?__/, "") + ": " + r.by_name[k]; }}).join("\\n") || "Tool calls in the run");
    h.appendChild(st); host.appendChild(h);
    var b = el("div", "pane-b"); b.setAttribute("role", "tabpanel"); b.setAttribute("data-check", "skip");   /* the agents' own reports: wide tables scroll inside the pane, and clipped text is not an overlap */
    if (state[side].tab === "report") {{ var why = renderWhy(r); if (why) b.appendChild(why); b.appendChild(renderMd(r.report)); }}
    else if (state[side].tab === "grades") b.appendChild(renderGrades(r));
    else if (state[side].tab === "verdict") {{ b.appendChild(el("p", "cit-note", "The judge saw this note as Report " + r.verdict.letter + " and the no-skill note of the same day as Report " + (r.verdict.letter === "A" ? "B" : "A") + ". It did not know which was which.")); b.appendChild(renderMd(r.verdict.text)); }}
    else if (state[side].tab === "results") b.appendChild(renderMd(r.results));
    else b.appendChild(r.run_log ? renderMd(r.run_log) : el("p", "cit-note", "No run log was saved for this run."));
    host.appendChild(b);
  }}

  function renderCompare() {{
    var body = document.getElementById("cmp-body"); body.textContent = "";
    var a = run("L"), b = run("R");
    if (!a.total || !b.total) {{
      var which = !a.total && !b.total ? "these two runs have" : ((!a.total ? a.label : b.label) + " has");
      document.querySelector("#cmp > summary").textContent = "Assertions side by side: " + which + " no assertion grades (rounds 4 and 5 are judged by blind comparison; open the Blind verdict tab).";
      return;
    }}
    var t = el("table", "cmp"); var thead = el("thead"); var tr = el("tr");
    [["Assertion", ""], [a.label, "m"], [b.label, "m"]].forEach(function (c) {{ var th = el("th", c[1], c[0]); tr.appendChild(th); }}); thead.appendChild(tr); t.appendChild(thead);
    var tb = el("tbody"); var seen = {{}}; var order = [];
    a.expectations.concat(b.expectations).forEach(function (x) {{ if (!seen[x.text]) {{ seen[x.text] = true; order.push(x.text); }} }});
    function find(r, text) {{ for (var i = 0; i < r.expectations.length; i++) if (r.expectations[i].text === text) return r.expectations[i]; return null; }}
    var diffs = 0;
    order.forEach(function (text) {{
      var xa = find(a, text), xb = find(b, text); var row = el("tr");
      var same = (xa ? xa.passed : null) === (xb ? xb.passed : null); if (!same) {{ row.className = "diff"; diffs++; }}
      row.appendChild(el("td", null, text));
      [xa, xb].forEach(function (x) {{ var td = el("td", "m"); td.appendChild(mark(x ? x.passed : null)); if (x && x.evidence) {{ td.setAttribute("data-tip", x.evidence); td.tabIndex = 0; }} row.appendChild(td); }});
      tb.appendChild(row);
    }});
    t.appendChild(tb); body.appendChild(t);
    document.querySelector("#cmp > summary").textContent = "Assertions side by side: " + a.label + " passed " + a.pass + " of " + a.total + ", " + b.label + " passed " + b.pass + " of " + b.total + ". " + (diffs === 1 ? "One assertion differs (bold row)" : diffs + " assertions differ (bold rows)") + ". Hover a mark for the grader's evidence, or open the Grades tab in a pane for all of it.";
  }}

  function renderPrompt() {{
    var e = byId(state.ev), box = document.getElementById("prompt"); box.textContent = "";
    var ph = el("div", "ph");
    ph.appendChild(el("b", null, e.label)); ph.appendChild(el("span", null, e.voice + " reader"));
    var c = el("span"); c.appendChild(document.createTextNode("Skill under test: ")); c.appendChild(el("code", null, e.skill_id)); ph.appendChild(c);
    box.appendChild(ph); box.appendChild(el("p", null, e.prompt));
    renderStrip();
  }}
  function judgedRun() {{
    /* the with-skill run whose verdict the strip shows: the one in the left pane if judged, else the right, else the latest judged */
    var e = byId(state.ev), l = run("L"), r = run("R");
    if (l && l.arm === "with_skill" && l.verdict && l.verdict.won != null) return l;
    if (r && r.arm === "with_skill" && r.verdict && r.verdict.won != null) return r;
    return e.latest ? RUNS[e.id + "|" + e.latest] : null;
  }}
  function renderStrip() {{
    var host = document.getElementById("vstrip"); host.textContent = ""; var j = judgedRun();
    if (!j) {{ host.hidden = true; return; }}
    host.hidden = false; var x = j.verdict.x || {{}};
    host.appendChild(el("span", "vs-k", "Blind verdict, " + j.label.toLowerCase().replace(/^with skill, /, "")));
    var v = el("span", "vs-v");
    var w = el("span", "tok " + (j.verdict.won ? "won" : "lost"), (j.verdict.won ? "The with-skill note won" : "The no-skill note won") + (x.margin ? ", " + x.margin : ""));
    v.appendChild(w); v.appendChild(document.createTextNode(". " + (x.winner_line || ""))); host.appendChild(v);
  }}

  function setEval(id, scroll) {{
    state.ev = id; document.getElementById("ev").value = id;
    var i = idx(id); document.getElementById("prev").disabled = i <= 0; document.getElementById("next").disabled = i >= EVALS.length - 1;
    renderPrompt(); renderPane("L"); renderPane("R"); renderCompare(); renderStrip(); markRow();
    if (scroll) document.getElementById("reader").scrollIntoView({{ behavior: "smooth", block: "start" }});
  }}
  function setLayout(l) {{
    state.layout = l; save(); var p = document.getElementById("panes"); p.className = "panes" + (l === "one" ? " one" : "");
    Array.prototype.forEach.call(document.querySelectorAll("#layout button"), function (b) {{ b.setAttribute("aria-pressed", String(b.getAttribute("data-layout") === l)); }});
  }}
  function markRow() {{
    var label = byId(state.ev).label;
    Array.prototype.forEach.call(document.querySelectorAll("#ov tr.k-row"), function (tr) {{ tr.classList.toggle("sel", tr.cells[0].textContent === label); }});
  }}

  /* Overview: a summary line, then one table per standing group; outcome and run cells are decorated after every render */
  document.getElementById("ov-sum").textContent = DATA.summary;
  var rowById = {{}}; DATA.rows.forEach(function (r) {{ rowById[r.eval] = r; }});
  function decorate(tbl) {{
    Array.prototype.forEach.call(tbl.querySelectorAll("tbody tr.k-row"), function (tr) {{
      var row = rowById[tr.cells[0].textContent]; if (!row) return;
      tr.classList.toggle("st-behind", row.standing === "behind"); tr.classList.toggle("st-ahead", row.standing === "ahead");
      var e = byId(row.id); if (!e || !e.pairs || !e.pairs.length) return;
      var oc = tr.cells[2]; if (oc && !oc.querySelector(".tok")) {{
        var last = e.pairs[e.pairs.length - 1]; oc.textContent = "";
        oc.appendChild(el("span", "tok " + (last.won ? "won" : "lost"), last.won ? "won" : "lost"));
        if (last.margin) oc.appendChild(el("span", "tok-m", ", " + last.margin));
      }}
      var rc = tr.cells[3]; if (rc && !rc.querySelector(".runtok")) {{
        rc.textContent = "";
        e.pairs.forEach(function (p) {{
          var s = el("span", "runtok"); s.setAttribute("data-run", p.key); s.setAttribute("data-ev", e.id); s.tabIndex = 0; s.setAttribute("role", "link");
          s.appendChild(document.createTextNode("R" + p.round + " ")); s.appendChild(el("span", "tok " + (p.won ? "won" : "lost"), p.won ? "won" : "lost"));
          s.setAttribute("data-tip", p.label + (p.margin ? ": " + (p.won ? "won" : "lost") + ", " + p.margin : "")); rc.appendChild(s);
        }});
      }}
    }});
  }}
  var judgedCols = [
    {{ key: "eval", label: "Prompt" }}, {{ key: "voice", label: "Reader", tip: "PM: a portfolio manager. Corporate: a strategy, treasury or investor-relations reader." }},
    {{ key: "outcome", label: "Outcome", tip: "The latest blind verdict on the with-skill note, with the judge's own margin word" }},
    {{ key: "runs", label: "Runs", tip: "Every judged with-skill run, oldest first, as R<round> won or lost. Click one to open it. Round 7 reruns are the with-skill note rewritten on the rules revised after Marko's review (no reader types, one figure per quantity, cases that partition, where-to-be as relative value by layer), judged on a brief that weighs faults by their effect on the reader." }},
    {{ key: "r13", label: "Rounds 1 to 3", tip: "Checklist scores, with skill vs without and the gain; R2 and R3 are the with-skill reruns after the library fixes and the body rewrite" }},
    {{ key: "words", label: "Words", tip: "Report length, with skill / without skill, first round" }}, {{ key: "tokens", label: "Tokens", tip: "Input and output tokens, with skill / without skill, first round" }}
  ];
  var checklistCols = [
    {{ key: "eval", label: "Prompt" }}, {{ key: "voice", label: "Reader", tip: "PM: a portfolio manager. Corporate: a strategy, treasury or investor-relations reader." }},
    {{ key: "with", label: "With skill", tip: "Assertions passed out of assertions graded, round 1, with the skill loaded" }}, {{ key: "without", label: "Without skill", tip: "Assertions passed out of assertions graded, round 1, Bigdata.com tools only" }},
    {{ key: "gain", label: "Gain", tip: "With-skill score minus without-skill score, round 1" }},
    {{ key: "r2", label: "Round 2", tip: "With skill, repeated after the library fixes and graded on one extra assertion (citation fidelity)" }},
    {{ key: "r3", label: "Round 3", tip: "With skill, repeated on 27 October after the bodies were rewritten as guidelines and the library stripped" }},
    {{ key: "words", label: "Words", tip: "Report length, with skill / without skill" }}, {{ key: "tokens", label: "Tokens", tip: "Input and output tokens, with skill / without skill" }}
  ];
  var ovHost = document.getElementById("ov");
  DATA.groups.forEach(function (g) {{
    if (!g.rows.length) return;
    var sec = el("div", "ov-group"); var h3 = el("h3", null, g.title + " "); var sm = el("small", null, g.rows.length + (g.rows.length === 1 ? " prompt, " : " prompts, ") + g.note); h3.appendChild(sm); sec.appendChild(h3);
    var mountEl = el("div"); sec.appendChild(mountEl); ovHost.appendChild(sec);
    KTable.mount(mountEl, {{ columns: g.key === "assertions" ? checklistCols : judgedCols, rows: g.rows, noun: "prompts" }});
    decorate(mountEl);
    new MutationObserver(function () {{ decorate(mountEl); }}).observe(mountEl.querySelector("tbody"), {{ childList: true }});
  }});
  function openRun(id, key) {{
    var e = byId(id); state.ev = id; state.L.run = key; state.L.tab = "report";
    var m = key.match(/^(\d+)\|/); var it = m ? m[1] : null;
    var rk = it && RUNS[id + "|" + it + "|without_skill"] ? it + "|without_skill" : (e.run_keys.filter(function (k) {{ return /without_skill$/.test(k); }}).pop() || e.run_keys[1]);
    state.R.run = rk; state.R.tab = "report"; setEval(id, true);
  }}
  ovHost.addEventListener("click", function (ev) {{
    var tok = ev.target.closest(".runtok"); if (tok) {{ ev.stopPropagation(); openRun(tok.getAttribute("data-ev"), tok.getAttribute("data-run")); return; }}
    var tr = ev.target.closest("tr.k-row"); if (!tr) return; var row = rowById[tr.cells[0].textContent]; if (!row) return;
    var e = byId(row.id); if (e && e.latest) openRun(e.id, e.latest); else setEval(row.id, true);
  }});
  ovHost.addEventListener("keydown", function (ev) {{ if (ev.key === "Enter" && ev.target.classList && ev.target.classList.contains("runtok")) ev.target.click(); }});

  /* Controls */
  var sel = document.getElementById("ev");
  EVALS.forEach(function (e) {{ var o = el("option", null, e.label + (e.label.indexOf("(") >= 0 ? "" : " (" + e.voice + ")")); o.value = e.id; sel.appendChild(o); }});
  sel.addEventListener("change", function () {{ setEval(sel.value, false); }});
  document.getElementById("prev").addEventListener("click", function () {{ var i = idx(state.ev); if (i > 0) setEval(EVALS[i - 1].id, false); }});
  document.getElementById("next").addEventListener("click", function () {{ var i = idx(state.ev); if (i < EVALS.length - 1) setEval(EVALS[i + 1].id, false); }});
  Array.prototype.forEach.call(document.querySelectorAll("#layout button"), function (b) {{ b.addEventListener("click", function () {{ setLayout(b.getAttribute("data-layout")); }}); }});
  document.addEventListener("keydown", function (ev) {{
    if (ev.target && (ev.target.tagName === "INPUT" || ev.target.tagName === "SELECT" || ev.target.tagName === "TEXTAREA")) return;
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    if (ev.key === "[") document.getElementById("prev").click(); else if (ev.key === "]") document.getElementById("next").click();
  }});
  window.addEventListener("hashchange", function () {{ var id = location.hash.slice(1); if (byId(id)) setEval(id, true); }});
  EVALS.forEach(function (e) {{ if (window.KSearch) KSearch.add(e.label + (e.label.indexOf("(") >= 0 ? "" : " (" + e.voice + ")"), "Prompt", function () {{ setEval(e.id, true); }}); }});

  setLayout(state.layout); setEval(state.ev, false);
}})();
</script>
"""
with open(OUT, "w", encoding="utf-8") as f: f.write(page)
print(f"wrote {OUT} ({len(page.encode('utf-8'))/1e6:.2f} MB), {n_runs} runs, {len(evals)} evals, {len(spare)} spare")
