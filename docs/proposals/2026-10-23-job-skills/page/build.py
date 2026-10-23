#!/usr/bin/env python3
"""Build the Job Skills Proposal page from the markdown sources."""
import re, json, html, os, datetime, sys
S = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.dirname(os.path.abspath(__file__))
def rd(p): return open(p, encoding="utf-8").read()

# ---------- minimal markdown -> html ----------
GLOSS = {
 "ROIC": "Return on invested capital: after-tax operating profit divided by the capital tied up in operations.",
 "ROIIC": "Return on incremental invested capital: the change in after-tax operating profit divided by the investment that produced it.",
 "RONIC": "Return on new invested capital, the return assumed on investment made after the explicit forecast period.",
 "NOPAT": "Net operating profit after tax: operating profit taxed at the operating rate, before interest.",
 "WACC": "Weighted average cost of capital. Bigdata.com has no WACC field, so the skills state it as an assumption.",
 "SVAR": "Shareholder value at risk: the premium paid in a deal as a share of the acquirer's market value.",
 "HHI": "Herfindahl-Hirschman index: the sum of squared market shares, a concentration measure.",
 "EBITA": "Earnings before interest, tax and amortisation of acquired intangibles.",
 "13F": "Quarterly holdings filings by US institutional investment managers.",
 "Cowork": "Claude's agent mode in the desktop app; Microsoft also calls its Copilot agent workspace Cowork.",
 "Codex": "OpenAI's coding agent, which shares the ChatGPT plugin and skill format.",
 "tearsheet": "The Bigdata.com company profile: FactSet statements, estimates, segments, holders, targets and events.",
 "SKILL.md": "The one required file in a skill folder: YAML frontmatter with name and description, then the instructions.",
 "plugin_slug": "A field on every Bigdata.com tool call that names the skill in use, so usage can be counted per skill.",
 "CAP": "Competitive advantage period: the years over which new investment earns more than the cost of capital.",
}
def esc(s): return html.escape(s, quote=False)
def inline(s):
    out = []; i = 0
    # split on code spans first
    parts = re.split(r"(`[^`]+`)", s)
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append("<code>" + esc(p[1:-1]) + "</code>")
        else:
            t = esc(p)
            t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
            t = re.sub(r"\[([^\]]+)\]\((\.?/?[^)\s]+)\)", r"<code>\2</code>", t)
            t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
            t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
            t = re.sub(r"(?<![\"'>=])(https?://[^\s<>()]+[^\s<>().,;])", r'<a href="\1" target="_blank" rel="noopener">\1</a>', t)
            out.append(t)
    return "".join(out)
seen_terms = set()
def gloss(htmltext):
    """Wrap the first occurrence of each glossary term in a tooltip span (text outside tags only)."""
    pieces = re.split(r"(<[^>]+>)", htmltext); incode = 0; res = []
    for pc in pieces:
        if pc.startswith("<"):
            if pc.startswith("<code") or pc.startswith("<a "): incode += 1
            elif pc.startswith("</code") or pc.startswith("</a"): incode -= 1
            res.append(pc); continue
        if incode: res.append(pc); continue
        for term, tip in GLOSS.items():
            if term in seen_terms: continue
            m = re.search(r"(?<![\w.-])" + re.escape(term) + r"(?![\w-])", pc)
            if m:
                seen_terms.add(term)
                pc = pc[:m.start()] + '<span class="term" tabindex="0" data-tip="' + esc(tip).replace('"', "&quot;") + '">' + m.group(0) + "</span>" + pc[m.end():]
        res.append(pc)
    return "".join(res)

def md(text, gl=True, base_h=2):
    lines = text.split("\n"); out = []; i = 0
    def flush_para(buf):
        if buf:
            h = inline(" ".join(buf).strip())
            out.append("<p>" + (gloss(h) if gl else h) + "</p>")
    buf = []
    while i < len(lines):
        ln = lines[i]
        if ln.strip() == "---" and i == 0:  # frontmatter
            j = i + 1; fm = []
            while j < len(lines) and lines[j].strip() != "---": fm.append(lines[j]); j += 1
            out.append('<div class="fm"><div class="fm-label">Frontmatter</div><pre>' + esc("\n".join(fm)) + "</pre></div>")
            i = j + 1; continue
        if ln.startswith("```"):
            flush_para(buf); buf = []
            j = i + 1; code = []
            while j < len(lines) and not lines[j].startswith("```"): code.append(lines[j]); j += 1
            out.append("<pre class=\"code\">" + esc("\n".join(code)) + "</pre>"); i = j + 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            flush_para(buf); buf = []
            lvl = min(6, len(m.group(1)) - 1 + base_h); txt = re.sub(r"^\d+(\.\d+)* ", "", m.group(2).strip()) if gl else m.group(2).strip()
            hid = re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")[:60]
            out.append(f'<h{lvl} id="h-{hid}">{inline(txt)}</h{lvl}>'); i += 1; continue
        if ln.lstrip().startswith("|"):
            flush_para(buf); buf = []
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            if len(rows) >= 2 and all(re.match(r"^:?-+:?$", c) for c in rows[1] if c):
                head = rows[0]; body = rows[2:]
            else:
                head = None; body = rows
            t = ['<div class="tbl"><table>']
            if head: t.append("<thead><tr>" + "".join("<th>" + inline(c) + "</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>")
            for r in body:
                t.append("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>"); out.append("".join(t)); continue
        m = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", ln)
        if m:
            flush_para(buf); buf = []
            ordered = m.group(2)[0].isdigit(); items = []; start = int(m.group(2)[:-1]) if ordered else 1
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", lines[i])
                if mm and (mm.group(2)[0].isdigit() == ordered):
                    items.append(mm.group(3)); i += 1
                elif lines[i].startswith("   ") and items and lines[i].strip() and not lines[i].strip().startswith("|"):
                    items[-1] += " " + lines[i].strip(); i += 1
                elif lines[i].startswith("   |") or (lines[i].startswith("   ") and lines[i].strip().startswith("|")):
                    # nested table inside a list item: render after list
                    break
                else: break
            tag = "ol" if ordered else "ul"
            cls = ' class="gaps"' if any(it.startswith("GAP") for it in items) else ""
            st = f' start="{start}"' if ordered and start != 1 else ""
            out.append(f"<{tag}{cls}{st}>" + "".join("<li>" + (gloss(inline(it)) if gl else inline(it)) + "</li>" for it in items) + f"</{tag}>")
            # handle nested indented table
            if i < len(lines) and lines[i].startswith("   |"):
                sub = []
                while i < len(lines) and lines[i].startswith("   |"): sub.append(lines[i][3:]); i += 1
                out.append(md("\n".join(sub), gl, base_h))
            continue
        if ln.strip() == "":
            flush_para(buf); buf = []; i += 1; continue
        buf.append(ln); i += 1
    flush_para(buf)
    return "\n".join(out)


SECNAME = {1: "Summary", 2: "What users ask for", 3: "rules", 4: "skill set", 5: "method library", 6: "How a skill is built", 7: "Packaging", 8: "Evaluation", 9: "Migration", 10: "Decisions"}
def xref(text):
    text = text.replace("Sections 2 to 9 give the reasoning and the detail. Appendix A has the description for every skill, Appendix B has four complete SKILL.md drafts, Appendix C has the specification of each method file, and Appendix D lists the sources.",
        "The sections below give the reasoning and the detail. The skill set table carries every skill's description, the Skill drafts section has four complete SKILL.md drafts, the Method specs section has the specification of each method file, and Sources lists what the work rests on.")
    text = text.replace("Appendix B shows four complete drafts in this shape.", "The Skill drafts section shows four complete drafts in this shape.")
    text = text.replace("Appendix C specifies each file:", "The Method specs section specifies each file:")
    text = text.replace("the four flagship skills in Appendix B", "the four flagship skills in the Skill drafts section")
    text = text.replace("Appendix B", "the Skill drafts section").replace("Appendix C", "the Method specs section").replace("Appendix A", "the skill set table").replace("Appendix D", "the Sources section")
    def rep(m):
        n = int(m.group(1)); sub = m.group(2) or ""
        return ("sections " if m.group(0).startswith("sections") else ("Sections " if m.group(0).startswith("Sections") else "")) + (("section " if m.group(0)[0] == "s" else "Section ") + m.group(1) + sub if n not in SECNAME else ("the " + SECNAME[n] + " section" if sub == "" else "the " + SECNAME[n] + " section (" + m.group(1) + sub + ")"))
    text = re.sub(r"(?<![\w.])[Ss]ection (\d+)(\.\d+)?", rep, text)
    return text

# ---------- sources ----------
main = xref(rd(f"{S}/proposal/2026-10-23-job-skills-proposal.md"))
appA = rd(f"{S}/proposal/appendix-a-descriptions.md")
appD = rd(f"{S}/proposal/appendix-d-sources.md")
specs_dir = f"{S}/method-specs"; skills_dir = f"{S}/proposal/skills"
W = "/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal"
PLUG = f"{W}/plugins/bigdata-com"
import glob, subprocess
def built_skill(name):
    p = f"{PLUG}/skills/{name}/SKILL.md"
    if not os.path.isfile(p): return None
    txt = rd(p); fm = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    refs = re.search(r"bigdata-refs:\s*(.+)", fm.group(1) if fm else "")
    primer = re.search(r"bigdata-sector-primer:\s*(\w+)", fm.group(1) if fm else "")
    files = [f for f in glob.glob(f"{PLUG}/skills/{name}/**/*", recursive=True) if os.path.isfile(f)]
    return {"text": txt, "lines": txt.count("\n") + 1, "refs": [r.strip() for r in refs.group(1).split(",")] if refs else [],
            "primer": primer.group(1) if primer else "none", "files": len(files),
            "yaml": rd(f"{PLUG}/skills/{name}/agents/openai.yaml") if os.path.isfile(f"{PLUG}/skills/{name}/agents/openai.yaml") else ""}
COWORK = set(e["folder"].split("/")[-1] for e in json.load(open(f"{W}/packaging/bigdata-com/microsoft/manifest.json"))["agentSkills"])
try:
    COMMIT = subprocess.run(["git", "-C", W, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
except Exception:
    COMMIT = "unknown"

# split main into sections by "## N. Title"
secs = re.split(r"^## (\d+)\. ", main, flags=re.M)
head = secs[0]; sections = {}
for k in range(1, len(secs), 2):
    n = int(secs[k]); body = secs[k + 1]
    title, _, rest = body.partition("\n")
    sections[n] = (title.strip(), rest)

# descriptions
desc = {}
for m in re.finditer(r"\*\*(bigdata[\w-]*)\*\*(?: \(\d+\))?\. (.+)", appA):
    desc[m.group(1)] = m.group(2).strip()

# skill rows from section 4 tables
groups = {"4.1": "Keep up", "4.2": "Company in depth", "4.3": "Earnings and events", "4.4": "Sectors and macro"}
rows = []
sec4 = sections[4][1]
for g, gname in groups.items():
    blk = re.search(r"### " + re.escape(g) + r".*?\n(.*?)(?=\n### |\Z)", sec4, re.S).group(1)
    for ln in blk.split("\n"):
        if ln.startswith("| bigdata-"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            rows.append({"skill": c[0], "group": gname, "job": c[1], "why": c[2]})
rows.insert(0, {"skill": "bigdata", "group": "Entry", "job": "The interview for vague requests, the hand-off table to the job skills, the answer to what Bigdata.com has, and the skill builder", "why": "Session one wrote it; it stays as the entry point"})
# refs mapping from section 5.1 table
refs = {}
for ln in sections[5][1].split("\n"):
    if ln.startswith("| ") and ".md |" in ln:
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) == 3 and c[0].endswith(".md"):
            for sk in [x.strip() for x in c[2].split(",")]:
                refs.setdefault("bigdata-" + sk, []).append(c[0].replace(".md", ""))
# migration map from section 9
replaces = {}
for ln in sections[9][1].split("\n"):
    if ln.startswith("| ") and "bigdata-" in ln and not ln.startswith("| Current"):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) == 2:
            for sk in re.findall(r"bigdata-[\w-]+", c[1]):
                if c[0] != "none": replaces.setdefault(sk, []).append(c[0])
for r in rows:
    r["desc"] = desc.get(r["skill"], ""); r["chars"] = len(r["desc"])
    r["refs"] = ", ".join(refs.get(r["skill"], [])) or ("working-with-bigdata, skill-builder" if r["skill"] == "bigdata" else "")
    r["replaces"] = "; ".join(replaces.get(r["skill"], [])) or "none, a new skill"
    b = built_skill(r["skill"])
    r["lines"] = b["lines"] if b else 0; r["files"] = b["files"] if b else 0
    r["cowork"] = "yes" if r["skill"] in COWORK else "no"
    r["primer"] = b["primer"] if b else "none"
    if b: r["refs"] = ", ".join(x for x in b["refs"] if x not in ("working-with-bigdata", "output-standard"))
assert len(rows) == 26, len(rows)

# section 4 body without the four group tables (the KTable replaces them)
s4 = re.sub(r"### 4\.[1-4] .*?(?=\n### 4\.5)", "", sec4, flags=re.S)
s4_intro, _, s4_rest = s4.partition("\n### 4.5")
s4_rest = "### 4.5" + s4_rest

# ---------- assemble ----------
fonts = rd(f"{PAGE}/fonts-platform.css")
logo = rd(f"{PAGE}/logo.datauri").strip()
now = datetime.datetime.now().astimezone().strftime("%d %b %Y, %H:%M %Z")

def section(n, label, title, inner, cls=""):
    return f'<section id="{n}" data-rail="{esc(label)}" class="{cls}"><h2>{esc(title)}</h2>\n{inner}\n</section>'

order = []
status = ('<p class="status"><strong>Status, ' + esc(datetime.date.today().strftime("%d %b %Y")) + '.</strong> Built on the local branch <code>skills-proposal-2026-10-23</code> at commit <code>' + esc(COMMIT) + '</code>: all 26 skill folders, the shared library (two shared files, 14 method files, 12 sector primers), the library sync and validation scripts, the three host packages, a 156-case trigger suite and live-connector cases. The sections "Skills as built", "Library as built", "Evaluation results" and "Packages built" show the result. Nothing is merged, pushed or published to any host.</p>')
order.append(section("summary", "Summary", "Summary", status + md(sections[1][1])))
order.append(section("decisions", "Decisions", "Decisions for Marko", md(sections[10][1])))
order.append(section("demand", "What users ask for", "What users ask for", re.sub(r'(<div class="tbl">.*?</div>)\s*(<div class="tbl">.*?</div>)', r'<div class="pair">\1\2</div>', md(sections[2][1]), count=1, flags=re.S)))
order.append(section("rules", "Rules", "Rules every skill follows", md(sections[3][1])))
skills_inner = md(s4_intro) + '<div id="skills-table" data-search="The 26 skills" data-search-hint="Table"></div><div id="skills-list" class="sk-list"></div>' + md(s4_rest)
order.append(section("skills", "Skill set", "The skill set", skills_inner))
order.append(section("library", "Method library", "The shared method library", md(sections[5][1])))
order.append(section("build", "How a skill is built", "How a skill is built", md(sections[6][1])))
order.append(section("packaging", "Packaging", "Packaging per host", md(sections[7][1])))
order.append(section("evals", "Evaluation", "Evaluation", md(sections[8][1])))
order.append(section("migration", "Migration", "Migration and release", md(sections[9][1])))

spec_order = ["expectations", "base-rates", "roic", "valuation", "multiples-and-peers", "earnings-quality", "capital-allocation", "industry-structure", "operating-leverage-and-tam", "after-a-price-move", "downside-and-catalysts", "forecasting-discipline", "credit", "special-situations-arithmetic"]
# The skills as built: one fold per skill with the rendered SKILL.md and its listing file
skill_folds = []
for r in rows:
    b = built_skill(r["skill"])
    if not b: continue
    body = md(b["text"], gl=False, base_h=4)
    yaml_block = "<h5>agents/openai.yaml</h5><pre>" + esc(b["yaml"]) + "</pre>" if b["yaml"] else ""
    skill_folds.append(f'<details class="k-fold" id="skill-{r["skill"]}"><summary><span class="fold-name">{esc(r["skill"])}</span><span class="fold-job">{esc(r["group"])}: {esc(r["job"])}</span><small>{b["lines"]} lines</small></summary><div class="k-fold-body doc">{body}{yaml_block}</div></details>')
order.append(section("built", "Skills as built", "The 26 skills as built",
    f'<p>Every skill folder on the branch <code>skills-proposal-2026-10-23</code> at commit <code>{esc(COMMIT)}</code>: the SKILL.md rendered as a document, then its ChatGPT listing file. The references each skill carries are copies of the library files below, placed by the build.</p><div class="folds">' + "".join(skill_folds) + "</div>"))

lib_folds = []
for name in ["output-standard", "working-with-bigdata"]:
    txt = rd(f"{PLUG}/library/{name}.md")
    lib_folds.append(f'<details class="k-fold" id="lib-{name}"><summary>{esc(name)}.md <small>{len(txt.split()):,} words</small></summary><div class="k-fold-body doc">{md(txt, gl=False, base_h=4)}</div></details>')
for name in spec_order:
    p = f"{PLUG}/library/methods/{name}.md"
    if not os.path.isfile(p): continue
    txt = rd(p); gaps = txt.count("Not in the sources")
    lib_folds.append(f'<details class="k-fold" id="method-{name}"><summary>methods/{esc(name)}.md <small>{len(txt.split()):,} words, {gaps} not-in-the-sources line{"s" if gaps != 1 else ""}</small></summary><div class="k-fold-body doc">{md(txt, gl=False, base_h=4)}</div></details>')
for p in sorted(glob.glob(f"{PLUG}/library/sectors/*.md")):
    name = os.path.basename(p)[:-3]; txt = rd(p)
    lib_folds.append(f'<details class="k-fold" id="sector-{name}"><summary>sectors/{esc(name)}.md <small>{len(txt.split()):,} words</small></summary><div class="k-fold-body doc">{md(txt, gl=False, base_h=4)}</div></details>')
order.append(section("library-built", "Library as built", "The library as built",
    '<p>The two shared files, the fourteen method files and the twelve sector primers, as they stand on the branch. Each method file keeps the points where the source papers were silent as a "Not in the sources" line, so the writer of a skill states those as assumptions.</p><div class="folds">' + "".join(lib_folds) + "</div>"))

CASE_LABELS = {"ep-micron": "Earnings preview, Micron", "ep-narrow": "Narrow question, Micron consensus and guidance", "sm-move": "Stock move, Micron this week", "qt-jpm": "Quick take, JPMorgan (a bank)", "qt-connector-off": "Quick take with the connector off", "dd-asml": "Deep dive, ASML (non-US)"}
COUNTED = ("questions before", "Bigdata.com calls", "uses the method", "no call that changes")
def eval_results_html():
    parts = []
    trig = f"{PLUG}/evals/results/trigger-wave1.json"
    if os.path.isfile(trig):
        try:
            d = json.load(open(trig)); cases = d.get("cases", [])
            agg = d.get("aggregates", {})
            passed = agg.get("casesPassed", 0); total = agg.get("casesTotal", len(cases))
            parts.append(f"<p><strong>Trigger suite: {passed} of {total} cases passed.</strong> A case passes when the skill does what its prompt is meant to test: a <em>fires</em> case passes when the model invoked that skill on a prompt written for it, a <em>near miss</em> case passes when the model invoked the named neighbour and left this skill alone, and a <em>no fire</em> case passes when no Bigdata.com job skill was invoked on an unrelated prompt. Each skill has three fires, two near-miss and one no-fire prompt. The suite ran once per case (so a single run decides each case), with the plugin loaded and the Bigdata.com server mocked out, on the session's default model, at a list-price cost of ${d.get('costUsd', 0):.2f}. No baseline arm was run: the suite measures routing between the skills, and a run without the plugin could not invoke any of them. The prompts were written by the same team that wrote the skills, so the result says the descriptions route as designed, not how real users phrase things; that comes from usage after release.</p>")
            exc = [c for c in cases if (c.get("aggregates", {}).get("score") or 0) < 1]
            if exc:
                rows_h = []
                for c in exc:
                    nm = c["name"]; pr = ""
                    try: pr = open(f"{PLUG}/evals/{nm}/prompt.md").read().split("---")[-1].strip()
                    except Exception: pass
                    note = {"bigdata--fires-1": "The prompt was the literal /bigdata; a headless run cannot route a slash command. The prompt was replaced with a natural sentence and the case then passed 2 of 2.",
                            "bigdata-macro-compare--fires-2": "A colloquial prompt that could be read as sport; on re-run it fired 1 of 2. Left as the one known soft spot."}.get(nm, "")
                    rows_h.append(f"<tr><td>{esc(nm.split('--')[0])}</td><td>{esc(nm.split('--')[1].rsplit('-', 1)[0])}</td><td>{esc(pr)}</td><td>{esc(note)}</td></tr>")
                parts.append("<p>The cases that did not pass on the first run:</p>" + '<div class="tbl"><table><thead><tr><th>Skill</th><th>Kind</th><th>Prompt</th><th>What happened</th></tr></thead><tbody>' + "".join(rows_h) + "</tbody></table></div>")
        except Exception as e:
            parts.append(f"<p>Trigger suite result could not be read: {esc(str(e))}</p>")
    else:
        parts.append("<p>Trigger suite: not yet run when this page was built.</p>")
    live = sorted(glob.glob(f"{W}/evals/results/*/summary.json"))
    if live:
        recs = []
        for f in live:
            try: recs += json.load(open(f))
            except Exception: pass
        latest = {}
        for r in recs: latest[r["case"]] = r
        recs = [latest[k] for k in ["ep-micron", "ep-narrow", "sm-move", "qt-jpm", "qt-connector-off", "dd-asml"] if k in latest] + [v for k, v in latest.items() if k not in CASE_LABELS]
        n_pass = sum(1 for r in recs if r["pass"])
        parts.append(f"<p><strong>Live runs: {n_pass} of {len(recs)} cases passed every check.</strong> Each case sends one prompt to Claude Code headless on Opus with the plugin loaded and the production Bigdata.com connector connected, then grades the transcript twice: counted checks (questions asked before the first result, the number of Bigdata.com calls, whether the intended skill ran, no call that changes the account) and judged checks (a Sonnet judge reads the transcript against the method checklist for that skill, one item at a time). A case passes only when every check passes; the table lists each failed item in full. The latest run of each case is shown; earlier runs, with the fixes they led to, are in the repo under evals/results. Costs are the list price of the model calls for the run under test, in US dollars. The transcripts hold licensed content and stay on the machine.</p>")
        rows_h = []
        for r in recs:
            cc = [(c["check"], c["pass"]) for c in r["counted_checks"]]; jj = [(g["criterion"], g["pass"], g.get("reason", "")) for g in r["judge"]]
            passed = sum(1 for _, p in cc if p) + sum(1 for _, p, _ in jj if p); total = len(cc) + len(jj)
            fails = [f"<li>{esc(c)} (counted)</li>" for c, p in cc if not p] + [f"<li>{esc(c)} <span class=\"why\">Judge: {esc(w)}</span></li>" for c, p, w in jj if not p]
            verdict = '<span class="ok">pass</span>' if r["pass"] else '<span class="no">fail</span>'
            rows_h.append(f'<tr><td>{esc(CASE_LABELS.get(r["case"], r["case"]))}<br><span class="dim">{esc(r["prompt"])}</span></td><td>{verdict}</td><td class="num">{passed} of {total}</td><td class="num">{r["bigdata_calls"]}</td><td>{"<ul class=\"fails\">" + "".join(fails) + "</ul>" if fails else "none"}</td><td class="num">${r["cost_usd"]["subject"]:.2f}</td></tr>')
        parts.append('<div class="tbl live"><table><thead><tr><th>Case and prompt</th><th>Verdict</th><th class="num">Checks passed</th><th class="num">Bigdata.com calls</th><th>Failed checks</th><th class="num">Cost</th></tr></thead><tbody>' + "".join(rows_h) + "</tbody></table></div>")
    else:
        parts.append("<p>Live runs: none recorded when this page was built.</p>")
    return "".join(parts)
order.append(section("results", "Eval results", "Evaluation results", eval_results_html()))

PKG_DESC = {"claude-plugin": ("Claude, development zip", "The plugin folder as claude.ai accepts it under Customize, Plugins, Upload, so a branch can be tried on claude.ai next to the released plugin. All 26 skills. The version is the plugin manifest's, with the commit in the name."),
            "openai-plugin": ("ChatGPT and Codex", "The zip submitted to OpenAI's plugin directory: plugin.json, mcp.json, the assets and all 26 skills with their listing files. The OpenAI app has its own version line, 11.0.0 for this release."),
            "microsoft-cowork": ("Microsoft 365 Copilot Cowork", "The zip uploaded to Cowork: manifest.json with agentSkills, the icons and the 20 skills the manifest names, because Cowork allows at most 20 per package. Left out for the first release: capital-allocation, comps, credit, macro-compare, screen and special-situations.")}
pk = []
for z in sorted(glob.glob(f"{W}/packaging/bigdata-com/dist/*.zip")):
    base = os.path.basename(z); key = next((k for k in PKG_DESC if base.startswith(k)), None)
    host, what = PKG_DESC.get(key, ("", ""))
    pk.append(f'<tr><td>{esc(host)}</td><td><code>{esc(base)}</code></td><td>{esc(what)}</td><td class="num">{os.path.getsize(z)/1e6:.1f} MB</td></tr>')
order.append(section("packages", "Packages", "Packages built",
    '<p>The three host packages built from the branch by the scripts in <code>packaging/bigdata-com/scripts/</code>. The Microsoft package carries the twenty skills its manifest names; the other two carry all twenty-six.</p><div class="tbl"><table><thead><tr><th>Host</th><th>File</th><th>What it holds</th><th class="num">Size</th></tr></thead><tbody>' + "".join(pk) + "</tbody></table></div>"))

order.append(section("sources", "Sources", "Sources", md(re.sub(r"^## Appendix D\. Sources\n", "", appD), gl=False, base_h=3)))

rows_json = json.dumps(rows, ensure_ascii=True)

page = f"""<title>Job Skills Proposal</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
{fonts}
/* Layout: contents rail left, one 900px column; the skill-set table with row detail is the one bold element. */
:root {{
  --surface-0: #121212; --dp01: #1E1E1E; --dp03: #252525; --dp08: #2E2E2E; --dp12: #333333;
  --fg-1: #FFFDF5; --fg-2: #FFFDF5B2; --fg-3: #FFFDF580; --border: #FFFFFF29;
  --bd-blue: #4CA7F9; --bd-blue-700: #206EB5; --overlay-blue: rgba(83,166,251,0.12); --overlay-yellow: rgba(235,183,30,0.12); --yellow-500: #FDF16F;
  --bg: var(--surface-0); --surface: var(--dp01); --surface-2: var(--dp03); --line: var(--border);
  --ink: var(--fg-1); --ink-2: var(--fg-2); --muted: #A9A79F; --accent: var(--bd-blue);
  --font-display: "Moderno", "Hanken Grotesk", serif; --font-sans: "Hanken Grotesk", "Inter", system-ui, sans-serif; --font-mono: "Apercu Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --k-page-width: 900px;
  color-scheme: dark;
}}
html {{ background: var(--bg); }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--font-sans); font-size: 15px; line-height: 1.55; margin: 0; -webkit-font-smoothing: antialiased; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
a {{ color: var(--accent); text-decoration: none; }} a:hover {{ text-decoration: underline; }}
.k-page {{ padding-left: max(24px, env(safe-area-inset-left, 0px)); padding-right: max(24px, env(safe-area-inset-right, 0px)); padding-block: 32px 96px; }}
header.top {{ margin-bottom: 48px; }}
header.top .eyebrow {{ font-size: 11px; letter-spacing: .18em; text-transform: uppercase; color: var(--fg-2); font-weight: 600; margin-bottom: 12px; }}
header.top h1 {{ font-family: var(--font-display); font-weight: 400; font-size: 44px; line-height: 1.05; letter-spacing: -0.01em; margin: 0 0 12px; text-wrap: balance; }}
header.top .sub {{ color: var(--fg-2); font-size: 15px; max-width: 70ch; }}
header.top .meta {{ color: var(--fg-3); font-size: 13px; margin-top: 12px; font-variant-numeric: tabular-nums; }}
section[id] {{ margin-bottom: 48px; }}
h2 {{ font-size: 26px; font-weight: 600; line-height: 1.2; margin: 0 0 12px; text-wrap: balance; }}
h3 {{ font-size: 18px; font-weight: 600; margin: 28px 0 8px; }}
h4 {{ font-size: 15px; font-weight: 600; margin: 20px 0 6px; }}
h5, h6 {{ font-size: 14px; font-weight: 600; margin: 16px 0 4px; }}
p {{ margin: 0 0 12px; max-width: 70ch; }}
ul, ol {{ margin: 0 0 12px; padding-left: 22px; max-width: 70ch; }}
li {{ margin: 0 0 4px; }}
li::marker {{ color: var(--fg-3); }}
strong {{ font-weight: 600; }}
code {{ font-family: var(--font-mono); font-size: 0.9em; background: #FFFFFF14; padding: 0.05em 0.35em; border-radius: 4px; overflow-wrap: anywhere; }}
p, li, h2, h3, h4, dd {{ overflow-wrap: anywhere; }}
pre {{ font-family: var(--font-mono); font-size: 12.5px; line-height: 1.5; background: var(--dp01); border: 1px solid var(--line); border-radius: 8px; padding: 12px 14px; overflow-x: auto; margin: 0 0 12px; white-space: pre; }}
pre.code {{ white-space: pre; }}
.fm {{ margin: 0 0 12px; }} .fm-label {{ font-size: 11px; letter-spacing: .14em; text-transform: uppercase; color: var(--fg-3); margin-bottom: 4px; }}
.tbl {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); margin: 0 0 16px; }}
.tbl table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
.tbl th, .tbl td {{ text-align: left; vertical-align: top; padding: 6px 10px; border-bottom: 1px solid var(--line); }}
.tbl th {{ font-weight: 500; font-size: 12px; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); white-space: nowrap; }}
.tbl tr:last-child td {{ border-bottom: 0; }}
.tbl td:first-child {{ overflow-wrap: normal; }}
.tbl td:first-child code {{ white-space: nowrap; }}
.tbl td code {{ white-space: nowrap; }}
.term {{ border-bottom: 1px dotted var(--fg-3); cursor: default; }}
p.status {{ background: var(--overlay-blue); border: 1px solid var(--line); border-radius: 8px; padding: 10px 14px; max-width: none; }}
ul.gaps li {{ background: var(--overlay-yellow); padding: 2px 8px; border-radius: 4px; list-style: none; margin-left: -22px; }}
.folds {{ display: flex; flex-direction: column; gap: 8px; }}
details.k-fold > summary {{ font-size: 15px; color: var(--ink); font-family: var(--font-mono); flex-wrap: wrap; }}\n.fold-name {{ flex: none; }}\n.fold-job {{ font-family: var(--font-sans); font-size: 13px; color: var(--fg-2); flex: 1 1 320px; min-width: 0; }}\n.k-fold-body.doc em {{ font-style: italic; }}
details.k-fold > summary small {{ margin-left: auto; color: var(--muted); font-size: 12px; font-family: var(--font-sans); font-variant-numeric: tabular-nums; }}
#skills-table .k-table tr.k-row > td:first-child {{ white-space: nowrap; }}
#skills-table tr.k-click > td:first-child::before {{ content: ""; display: inline-block; width: 6px; height: 6px; border-right: 1.5px solid var(--muted); border-bottom: 1.5px solid var(--muted); transform: rotate(-45deg); margin: 0 10px 2px 0; transition: transform 120ms; }}
#skills-table tr.k-click.k-open > td:first-child::before {{ transform: rotate(45deg); }}
.k-rail::after {{ content: ""; position: absolute; right: 0; top: 0; bottom: 0; width: 64px; background: linear-gradient(90deg, rgba(18,18,18,0), var(--bg) 70%); pointer-events: none; }}
@media (min-width: 1240px) {{ .k-rail::after {{ display: none; }} }}
.k-fold-body.doc h4 {{ font-size: 16px; margin-top: 20px; }}
.k-fold-body.doc h5 {{ font-size: 14px; }}
.k-fold-body.doc p, .k-fold-body.doc ul, .k-fold-body.doc ol {{ max-width: 76ch; }}
#skills-table {{ margin: 16px 0 24px; }}\n.tbl.live td {{ vertical-align: top; }}\n.tbl.live td:first-child {{ white-space: normal; min-width: 180px; }}\nul.fails {{ margin: 0; padding-left: 18px; max-width: none; font-size: 13px; }}\nul.fails li {{ margin: 0 0 6px; }}\n.why {{ color: var(--fg-2); }}\n.dim {{ color: var(--fg-3); font-size: 13px; }}\n.ok {{ color: #04E0A9; font-weight: 600; }}\n.no {{ color: #FD8282; font-weight: 600; }}\n.tbl th.num {{ text-align: right; }}
.sk-list {{ display: none; flex-direction: column; gap: 6px; margin: 16px 0 24px; }}
.sk-list details {{ border: 1px solid var(--line); border-radius: 8px; background: var(--surface); }}
.sk-list summary {{ cursor: pointer; padding: 8px 12px; list-style: none; display: flex; flex-direction: column; gap: 2px; }}
.sk-list summary::-webkit-details-marker {{ display: none; }}
.sk-list summary b {{ font-weight: 600; font-family: var(--font-mono); font-size: 13px; }}
.sk-list summary span {{ color: var(--fg-2); font-size: 14px; }}
.sk-list .sk-body {{ padding: 4px 12px 12px; font-size: 14px; }}
.sk-list .sk-body p {{ margin: 0 0 6px; }}
.sk-list .sk-group {{ font-size: 11px; letter-spacing: .14em; text-transform: uppercase; color: var(--fg-3); margin: 10px 0 2px; }}
.pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; margin-bottom: 16px; }}
.pair .tbl {{ margin: 0; min-width: 0; }}
.pair th {{ white-space: normal; }}
@media (max-width: 760px) {{ .pair {{ grid-template-columns: 1fr; }} }}
.sk-detail {{ display: grid; grid-template-columns: 120px 1fr; gap: 6px 14px; font-size: 14px; max-width: 100%; }}
.sk-detail dt {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .05em; padding-top: 2px; }}
.sk-detail dd {{ margin: 0; font-size: 15px; }}
.sk-detail dt {{ color: var(--fg-2); }}
.k-rail-head img {{ width: 128px; }}
@media (max-width: 600px) {{
  .k-page {{ padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
  header.top h1 {{ font-size: 34px; }}
  .sk-detail {{ grid-template-columns: 1fr; }}
  #skills-table {{ display: none; }}
  .sk-list {{ display: flex; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; animation: none !important; }} }}
</style>
<!-- kit: tooltip rail fold table search -->
<nav class="k-rail" aria-label="Contents"><div class="k-rail-head"><img src="{logo}" alt="Bigdata.com"><span>Proposal</span></div><ul></ul></nav>
<main class="k-page">
<header class="top">
  <div class="eyebrow">Bigdata.com plugin, skills rewrite</div>
  <h1>Bigdata.com job skills</h1>
  <div class="sub">The rewrite of the skills in the Bigdata.com plugin: 25 job skills plus the entry skill, a shared method library, one package per host, and the evaluation that gates release. The proposal first, then the skills and the library as built on the branch, with the eval results. For review by Marko and the Bigdata.com product and MCP team.</div>
  <div class="meta">Produced {esc(now)}. Press Cmd+K to search this page.</div>
</header>
{chr(10).join(order)}
</main>
<script>
var SKILLS = {rows_json};
(function () {{
  function el(t, c, x) {{ var e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }}
  function detail(r) {{
    var d = el("dl", "sk-detail");
    function row(k, v) {{ var dt = el("dt", null, k), dd = el("dd", null, v); d.appendChild(dt); d.appendChild(dd); }}
    row("Description", r.desc + " (" + r.chars + " characters)");
    row("Loads", r.refs ? r.refs + ", plus working-with-bigdata and output-standard" : "working-with-bigdata, output-standard");
    row("Replaces", r.replaces);
    return d;
  }}
  var list = document.getElementById("skills-list"), lastGroup = null;
  SKILLS.forEach(function (r) {{
    if (r.group !== lastGroup) {{ list.appendChild(el("div", "sk-group", r.group)); lastGroup = r.group; }}
    var d = el("details"), s = el("summary"), body = el("div", "sk-body");
    s.appendChild(el("b", null, r.skill)); s.appendChild(el("span", null, r.job)); d.appendChild(s);
    body.appendChild(el("p", null, r.desc + " (" + r.chars + " characters)"));
    body.appendChild(el("p", null, "Why: " + r.why));
    body.appendChild(el("p", null, "Loads: " + (r.refs ? r.refs + ", plus working-with-bigdata and output-standard" : "working-with-bigdata, output-standard")));
    body.appendChild(el("p", null, "Replaces: " + r.replaces));
    d.appendChild(body); list.appendChild(d);
  }});
  KTable.mount(document.getElementById("skills-table"), {{
    columns: [
      {{ key: "skill", label: "Skill" }},
      {{ key: "group", label: "Group" }},
      {{ key: "job", label: "Job" }},
      {{ key: "why", label: "Why it is in the set" }}
    ],
    rows: SKILLS, detail: detail, filter: true, noun: "skills"
  }});
}})();
</script>
"""
out = f"{PAGE}/skills-proposal.html"
open(out, "w", encoding="ascii", errors="xmlcharrefreplace").write(page)
print("wrote", out, len(page))
