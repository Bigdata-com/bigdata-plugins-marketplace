#!/usr/bin/env python3
"""Build the Job Skills Proposal page from the markdown sources."""
import re, json, html, os, datetime, sys
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the proposal folder in the repo
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
main = xref(rd(f"{S}/proposal.md"))
appA = rd(f"{S}/appendix-a-descriptions.md")
appD = rd(f"{S}/appendix-d-sources.md")
specs_dir = f"{S}/method-specs"
W = os.environ.get("SKILLS_WORKTREE", "/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-audit-fixes")
OLDW = "/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-proposal"  # the 23 Oct build, for the live-run records
INPUTS = os.environ.get("PAGE_INPUTS", PAGE)  # fonts-platform.css, logo.datauri and plugin/ (from make_tree.py)
add = rd(f"{S}/addendum-2026-10-26.md")
ADD = {}
for k in re.split(r"^## ", add, flags=re.M)[1:]:
    t, _, body = k.partition("\n"); ADD[t.strip()] = body
add28 = rd(f"{S}/addendum-2026-10-28.md")
ADD28 = {}
for k in re.split(r"^## ", add28, flags=re.M)[1:]:
    t, _, body = k.partition("\n"); ADD28[t.strip()] = body
add27 = rd(f"{S}/addendum-2026-10-27.md")
ADD27 = {}
for k in re.split(r"^## ", add27, flags=re.M)[1:]:
    t, _, body = k.partition("\n"); ADD27[t.strip()] = body
RECUT = os.path.join(os.path.dirname(S), "2026-10-26-recut")
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
fonts = rd(f"{INPUTS}/fonts-platform.css")
logo = rd(f"{INPUTS}/logo.datauri").strip()
now = datetime.datetime.now().astimezone().strftime("%d %b %Y, %H:%M %Z")

def section(n, label, title, inner, cls=""):
    return f'<section id="{n}" data-rail="{esc(label)}" class="{cls}"><h2>{esc(title)}</h2>\n{inner}\n</section>'

order = []
status = ('<p class="status"><strong>Status, ' + esc(datetime.date.today().strftime("%d %b %Y")) + '.</strong> The 23 October build (branch <code>skills-proposal-2026-10-23</code>) was audited on 25 October and every fix was made on a second branch, <code>skills-audit-fixes-2026-10-25</code>, now at commit <code>' + esc(COMMIT) + '</code>: library formulas corrected, tool steps matched to what the data holds, all 26 descriptions rewritten and the trigger suite grown to 182 cases, skill bodies made tool-agnostic, and ten skills run on live prompts with and without the skill. The section "What changed since 23 October" carries the audit and the fixes, "Quality evals" the live runs, and "Decisions for Marko" the calls still open. On 27 October the re-cut was checked against the 23 October goals and found short in four places; "Finish plan" states the four, what changes, the answers from the review page, and the order of work to the release. On 28 October the earnings-preview skill lost a blind comparison to a no-skill run; the cause was traced to the packaging (source names, basis labels and numbered pointers reaching the page), the library and the output standard were rewritten in three layers, the skill then won six of six blind comparisons, and every other body was revised the same way; "Packaging, 28 October" carries the diagnosis, the rules and the evidence. The file browser shows the files as of that revision. Nothing is merged, pushed or published to any host.</p>')
order.append(section("summary", "Summary", "Summary", status + md(sections[1][1])))
order.append(section("changes", "Since 23 Oct", "What changed since 23 October", md(ADD["What changed since 23 October"])))
def body_fold(label, job, text, open_=False):
    words = len(text.split())
    return (f'<details class="k-fold"{" open" if open_ else ""}><summary><span class="fold-name">{esc(label)}</span><span class="fold-job">{esc(job)}</span><small>{words:,} words</small></summary>'
            f'<div class="k-fold-body doc">{md(text, gl=False, base_h=4)}</div></details>')
finish_html = (md(ADD27["Where the plan fell short"]) + "<h3>What changes</h3>" + md(ADD27["What changes"]).replace("<h3>", "<h4>").replace("</h3>", "</h4>")
    + '<h4>The valuation body in three versions</h4><p>Open each to read it as the agent would. The third is the shape proposed for all 22 bodies.</p><div class="folds">'
    + body_fold("SKILL.md, today", "The file on the audit branch, 25 October: gather, analyse, write, eleven checks.", rd(f"{PLUG}/skills/bigdata-valuation/SKILL.md"))
    + body_fold("valuation.recut.md, 26 October", "The first re-cut: the same procedure, shorter, 23 numbered steps.", rd(f"{RECUT}/valuation.recut.md"))
    + body_fold("valuation.recut2.md, 27 October", "Only what the agent would not supply itself: the method choices, the recorded mistakes, the data facts, three checks.", rd(f"{RECUT}/valuation.recut2.md"), open_=True)
    + '</div><h3>Answers from the review page</h3>' + md(ADD27["Answers from the review page"]) + "<h3>Order of work</h3>" + md(ADD27["Order of work"]))
order.append(section("finish", "Finish plan", "Finish plan, 27 October", finish_html))
pack_html = "".join("<h3>" + esc(h) + "</h3>" + md(ADD28[h]) for h in ADD28)
order.append(section("packaging", "Packaging, 28 Oct", "Packaging, 28 October", pack_html))
order.append(section("decisions", "Decisions", "Decisions for Marko", "<h3>Open after the audit and the evals, 26 October</h3>" + md(ADD["Decisions still open for Marko"]) + "<h3>From the 23 October proposal</h3><p>Two of these were settled by the evals: the citation format is now inline links carried with each fact, after numbered references put six of ten reports on a wrong document, and the cost of capital stays an assumption but the valuation method now checks the beta and shows the value at the market-implied rate.</p>" + md(sections[10][1])))
tree = json.load(open(f"{INPUTS}/plugin/tree.json"))
# every served file inlined, so the page is self-contained (the publish script sends one HTML file, and file:// works)
files_inline = {}
for _e in tree:
    if _e.get("src") and _e["src"] not in files_inline:
        files_inline[_e["src"]] = open(f"{INPUTS}/plugin/{_e['src']}", encoding="utf-8").read()
browse_html = ('<p>The plugin as it stands on the branch, file by file: the manifest, the library, and every skill folder with its SKILL.md, its ChatGPT listing file and the references the build placed in it. Pick a file in the tree, or press Cmd+K and type its name. A reference inside a skill is a copy of a library file; the viewer says which one and shows it from the library, so the same text is not stored twenty times.</p>'
    '<div class="fb"><div class="fb-side"><input id="fb-filter" type="search" placeholder="Filter files" aria-label="Filter files"><nav id="fb-tree" class="fb-tree" aria-label="Plugin files" data-check="skip"></nav></div>'
    '<div class="fb-view"><div class="fb-head"><div class="fb-path" id="fb-path">Pick a file</div><div class="fb-meta" id="fb-meta"></div><div class="fb-nav"><button type="button" id="fb-prev">Previous</button><button type="button" id="fb-next">Next</button><button type="button" id="fb-raw">Raw</button></div></div><div class="fb-body doc" id="fb-body" data-check="skip"><p class="dim">The 26 skills, the library and the manifests are listed on the left. A SKILL.md opens as a document with its frontmatter in a box at the top.</p></div></div></div>')
order.append(section("browse", "Browse the plugin", "Browse the plugin", browse_html))
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
CASE_LABELS = {"ep-micron": "Earnings preview, Micron", "ep-narrow": "Narrow question, Micron consensus and guidance", "sm-move": "Stock move, Micron this week", "qt-jpm": "Quick take, JPMorgan (a bank)", "qt-connector-off": "Quick take with the connector off", "dd-asml": "Deep dive, ASML (non-US)"}
COUNTED = ("questions before", "Bigdata.com calls", "uses the method", "no call that changes")
def eval_results_html():
    parts = []
    trig = f"{PLUG}/evals/results/run-2026-10-25.json"
    if os.path.isfile(trig):
        try:
            d = json.load(open(trig)); cases = d.get("cases", [])
            agg = d.get("aggregates", {})
            passed = agg.get("casesPassed", 0); total = agg.get("casesTotal", len(cases))
            parts.append(f"<p><strong>Trigger suite: {passed} of {total} cases passed.</strong> A case passes when the skill does what its prompt is meant to test: a <em>fires</em> case passes when the model invoked that skill on a prompt written for it, a <em>near miss</em> case passes when the model invoked the named neighbour and left this skill alone, and a <em>no fire</em> case passes when no Bigdata.com job skill was invoked on an unrelated prompt. Each skill has three or four <em>fires</em> prompts, one of them in a corporate voice (a head of IR, a supplier, a treasury team), two near-miss and one no-fire prompt. The suite ran once per case (so a single run decides each case), with the plugin loaded and the Bigdata.com server mocked out, on the session's default model, at a list-price cost of ${d.get('costUsd', 0):.2f}. No baseline arm was run: the suite measures routing between the skills, and a run without the plugin could not invoke any of them. The prompts were written by the same team that wrote the skills, so the result says the descriptions route as designed, not how real users phrase things; that comes from usage after release.</p>")
            exc = [c for c in cases if (c.get("aggregates", {}).get("score") or 0) < 1]
            if exc:
                rows_h = []
                for c in exc:
                    nm = c["name"]; pr = ""
                    try: pr = open(f"{PLUG}/evals/{nm}/prompt.md").read().split("---")[-1].strip()
                    except Exception: pass
                    note = {"bigdata-macro-compare--fires-2": "Fired nothing. The description was retuned with the prompt's own words; the first rerun fired 1 of 3, a second edit took it to 3 of 3.",
                            "bigdata-quick-take--fires-4": "Fired nothing. Retuned with \"a one-page read on X\"; 3 of 3 on rerun.",
                            "bigdata-screen--fires-2": "Fired nothing. Retuned with \"who else does what X does\"; 3 of 3 on rerun.",
                            "bigdata-sector--fires-2": "Fired nothing. Retuned with \"which sectors look interesting\"; 3 of 3 on rerun.",
                            "bigdata-special-situations--fires-3": "Fired nothing. Retuned with \"a rights issue\"; the first rerun fired 1 of 3, a second edit took it to 3 of 3."}.get(nm, "")
                    rows_h.append(f"<tr><td>{esc(nm.split('--')[0])}</td><td>{esc(nm.split('--')[1].rsplit('-', 1)[0])}</td><td>{esc(pr)}</td><td>{esc(note)}</td></tr>")
                parts.append("<p>The cases that did not pass on the first run:</p>" + '<div class="tbl"><table><thead><tr><th>Skill</th><th>Kind</th><th>Prompt</th><th>What happened</th></tr></thead><tbody>' + "".join(rows_h) + "</tbody></table></div>")
        except Exception as e:
            parts.append(f"<p>Trigger suite result could not be read: {esc(str(e))}</p>")
    else:
        parts.append("<p>Trigger suite: not yet run when this page was built.</p>")
    live = sorted(glob.glob(f"{OLDW}/evals/results/*/summary.json"))
    if live:
        recs = []
        for f in live:
            try: recs += json.load(open(f))
            except Exception: pass
        latest = {}
        for r in recs: latest[r["case"]] = r
        recs = [latest[k] for k in ["ep-micron", "ep-narrow", "sm-move", "qt-jpm", "qt-connector-off", "dd-asml"] if k in latest] + [v for k, v in latest.items() if k not in CASE_LABELS]
        n_pass = sum(1 for r in recs if r["pass"])
        parts.append(f"<p><strong>Live runs on the 23 October build: {n_pass} of {len(recs)} cases passed every check.</strong> These ran before the audit and are kept as the record of that build; the 26 October quality evals below ran on the audited branch. Each case sends one prompt to Claude Code headless on Opus with the plugin loaded and the production Bigdata.com connector connected, then grades the transcript twice: counted checks (questions asked before the first result, the number of Bigdata.com calls, whether the intended skill ran, no call that changes the account) and judged checks (a Sonnet judge reads the transcript against the method checklist for that skill, one item at a time). A case passes only when every check passes; the table lists each failed item in full. The latest run of each case is shown; earlier runs, with the fixes they led to, are in the repo under evals/results. Costs are the list price of the model calls for the run under test, in US dollars. The transcripts hold licensed content and stay on the machine.</p>")
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
order.append(section("quality", "Quality evals", "Quality evals, 26 October", md(ADD["Quality evals, 26 October"]) + "<h3>Tool-agnostic bodies and the second round</h3>" + md(ADD["Tool-agnostic bodies and the second round"]) + "<h3>Open after 26 October</h3>" + md(ADD["Open after 26 October"])))

PKG_DESC = {"claude-plugin": ("Claude, development zip", "The plugin folder as claude.ai accepts it under Customize, Plugins, Upload, so a branch can be tried on claude.ai next to the released plugin. All 26 skills. The version is the plugin manifest's, with the commit in the name."),
            "openai-plugin": ("ChatGPT and Codex", "The zip submitted to OpenAI's plugin directory: plugin.json, mcp.json, the assets and all 26 skills with their listing files. The OpenAI app has its own version line, 11.0.0 for this release."),
            "microsoft-cowork": ("Microsoft 365 Copilot Cowork", "The zip uploaded to Cowork: manifest.json with agentSkills, the icons and the 20 skills the manifest names, because Cowork allows at most 20 per package. Left out for the first release: capital-allocation, comps, credit, macro-compare, screen and special-situations.")}
pk = []
newest = {}
for z in glob.glob(f"{W}/packaging/bigdata-com/dist/*.zip"):
    key = next((k for k in PKG_DESC if os.path.basename(z).startswith(k)), os.path.basename(z))
    if key not in newest or os.path.getmtime(z) > os.path.getmtime(newest[key]): newest[key] = z
for z in sorted(newest.values()):
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
#skills-table {{ margin: 16px 0 24px; }}
.fb {{ display: grid; grid-template-columns: 280px minmax(0, 1fr); gap: 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); height: 700px; overflow: hidden; }}
.fb-side {{ border-right: 1px solid var(--line); padding: 10px; display: flex; flex-direction: column; gap: 8px; min-width: 0; min-height: 0; height: 100%; box-sizing: border-box; overflow: hidden; }}
.fb-side input {{ background: var(--bg); color: var(--ink); border: 1px solid var(--line); border-radius: 6px; padding: 5px 10px; font: inherit; font-size: 13px; width: 100%; box-sizing: border-box; }}
.fb-tree {{ overflow: auto; flex: 1 1 auto; min-height: 0; font-size: 13px; }}
.fb-tree ul {{ list-style: none; margin: 0; padding-left: 14px; max-width: none; }}
.fb-tree > ul {{ padding-left: 0; }}
.fb-tree li {{ margin: 0; }}
.fb-tree .fb-dir > span, .fb-tree .fb-file > a {{ display: block; padding: 3px 6px; border-radius: 4px; color: var(--ink-2); text-decoration: none; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.fb-tree .fb-dir > span {{ color: var(--ink); font-weight: 600; }}
.fb-tree .fb-dir > span::before {{ content: ""; display: inline-block; width: 5px; height: 5px; border-right: 1.5px solid var(--muted); border-bottom: 1.5px solid var(--muted); transform: rotate(45deg); margin: 0 8px 2px 2px; }}
.fb-tree .fb-dir.closed > span::before {{ transform: rotate(-45deg); }}
.fb-tree .fb-dir.closed > ul {{ display: none; }}
.fb-tree .fb-file > a:hover {{ background: var(--surface-2); color: var(--ink); }}
.fb-tree .fb-file.active > a {{ background: var(--overlay-blue); color: var(--ink); }}
.fb-tree .fb-file.copy > a {{ color: var(--fg-3); }}
.fb-view {{ padding: 12px 18px 18px; min-width: 0; min-height: 0; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; overflow: hidden; }}
.fb-head {{ display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: baseline; border-bottom: 1px solid var(--line); padding-bottom: 8px; margin-bottom: 12px; }}
.fb-path {{ font-family: var(--font-mono); font-size: 13px; color: var(--ink); flex: 1 1 260px; min-width: 0; overflow-wrap: anywhere; }}
.fb-meta {{ font-size: 12px; color: var(--fg-3); }}
.fb-nav button {{ background: var(--surface-2); color: var(--ink); border: 1px solid var(--line); border-radius: 6px; padding: 3px 10px; font: inherit; font-size: 12px; cursor: pointer; }}
.fb-nav button:hover {{ border-color: var(--muted); }}
.fb-body {{ flex: 1 1 auto; min-height: 0; overflow: auto; }}
.fb-body h1 {{ font-family: var(--font-sans); font-size: 22px; font-weight: 600; margin: 0 0 10px; }}
.fb-body h2 {{ font-size: 18px; margin: 20px 0 8px; }}
.fb-body h3 {{ font-size: 16px; }}
.fb-body p, .fb-body ul, .fb-body ol {{ max-width: 78ch; }}
.fb-body .fm {{ background: var(--dp01); border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px; margin: 0 0 14px; }}
.fb-body .fm dl {{ display: grid; grid-template-columns: 150px 1fr; gap: 4px 12px; font-size: 13px; margin: 0; }}
.fb-body .fm dt {{ color: var(--fg-3); }} .fb-body .fm dd {{ margin: 0; overflow-wrap: anywhere; }}
.fb-body pre {{ white-space: pre-wrap; }}
.fb-body .copy-note {{ background: var(--overlay-blue); border-radius: 6px; padding: 6px 10px; font-size: 13px; margin: 0 0 12px; }}
@media (max-width: 760px) {{ .fb {{ grid-template-columns: 1fr; height: auto; }} .fb-side {{ border-right: 0; border-bottom: 1px solid var(--line); height: auto; }} .fb-tree {{ max-height: 240px; }} .fb-view {{ height: auto; }} .fb-body {{ max-height: 560px; }} }}\n.tbl.live td {{ vertical-align: top; }}\n.tbl.live td:first-child {{ white-space: normal; min-width: 180px; }}\nul.fails {{ margin: 0; padding-left: 18px; max-width: none; font-size: 13px; }}\nul.fails li {{ margin: 0 0 6px; }}\n.why {{ color: var(--fg-2); }}\n.dim {{ color: var(--fg-3); font-size: 13px; }}\n.ok {{ color: #04E0A9; font-weight: 600; }}\n.no {{ color: #FD8282; font-weight: 600; }}\n.tbl th.num {{ text-align: right; }}
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
var SKILLS = {rows_json};
var TREE = {json.dumps(tree, ensure_ascii=True)};
var FILES = {json.dumps(files_inline, ensure_ascii=True).replace("</", "<\\/")};
(function () {{
  function el(t, c, x) {{ var e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }}
  function detail(r) {{
    var d = el("dl", "sk-detail");
    function row(k, v) {{ var dt = el("dt", null, k), dd = el("dd", null, v); d.appendChild(dt); d.appendChild(dd); }}
    row("Description", r.desc + " (" + r.chars + " characters)");
    row("Loads", r.refs ? r.refs + ", plus working-with-bigdata and output-standard" : "working-with-bigdata, output-standard");
    row("Replaces", r.replaces);
    var dt = el("dt", null, "Files"), dd = el("dd"); var a = el("a", null, "Open SKILL.md in the browser"); a.href = "#f.skills." + r.skill + ".SKILL.md"; dd.appendChild(a); d.appendChild(dt); d.appendChild(dd);
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
  // ---- file browser ----
  (function () {{
    var treeEl = document.getElementById("fb-tree"), body = document.getElementById("fb-body"), pathEl = document.getElementById("fb-path"), metaEl = document.getElementById("fb-meta"), filterEl = document.getElementById("fb-filter");
    var files = TREE.filter(function (e) {{ return e.src; }}), order = files.map(function (e) {{ return e.path; }}), current = null, raw = false, cache = {{}};
    function token(path) {{ return "f." + path.replace(/\\//g, "."); }}
    function fromToken(tok) {{ var want = tok.slice(2); for (var i = 0; i < files.length; i++) if (files[i].path.replace(/\\//g, ".") === want) return files[i]; return null; }}
    // nested tree
    var root = {{ dirs: {{}}, files: [] }};
    files.forEach(function (e) {{ var parts = e.path.split("/"), node = root; for (var i = 0; i < parts.length - 1; i++) {{ node.dirs[parts[i]] = node.dirs[parts[i]] || {{ dirs: {{}}, files: [] }}; node = node.dirs[parts[i]]; }} node.files.push(e); }});
    function render(node, prefix, depth) {{
      var ul = el("ul");
      Object.keys(node.dirs).sort().forEach(function (name) {{
        var li = el("li", "fb-dir" + ((depth >= 1 && prefix.indexOf("skills/") === 0) || name === "sectors" || name === "methods" ? " closed" : "")), label = el("span", null, name + "/"); li.appendChild(label);
        label.addEventListener("click", function () {{ li.classList.toggle("closed"); }});
        li.appendChild(render(node.dirs[name], prefix + name + "/", depth + 1)); ul.appendChild(li);
      }});
      node.files.sort(function (a, b) {{ return a.path < b.path ? -1 : 1; }}).forEach(function (e) {{
        var li = el("li", "fb-file" + (e.src !== e.path ? " copy" : "")), a = el("a", null, e.path.split("/").pop()); a.href = "#" + token(e.path); a.setAttribute("data-path", e.path);
        a.addEventListener("click", function (ev) {{ ev.preventDefault(); open(e); history.replaceState(null, "", "#" + token(e.path)); }});
        li.appendChild(a); ul.appendChild(li);
      }});
      return ul;
    }}
    treeEl.appendChild(render(root, "", 0));
    function renderMd(text) {{
      var fm = null, m = text.match(/^---\\n([\\s\S]*?)\\n---\\n/);
      if (m) {{ fm = m[1]; text = text.slice(m[0].length); }}
      var html = window.marked ? marked.parse(text, {{ gfm: true, breaks: false }}) : "<pre>" + text.replace(/[&<>]/g, function (c) {{ return {{ "&": "&amp;", "<": "&lt;", ">": "&gt;" }}[c]; }}) + "</pre>";
      var wrap = el("div"); wrap.innerHTML = html;
      Array.prototype.forEach.call(wrap.querySelectorAll("table"), function (tb) {{ var d = el("div", "tbl"); tb.parentNode.insertBefore(d, tb); d.appendChild(tb); }});
      Array.prototype.forEach.call(wrap.querySelectorAll("a[href]"), function (a) {{ if (/^https?:/.test(a.getAttribute("href"))) {{ a.target = "_blank"; a.rel = "noopener"; }} else {{ var c = el("code", null, a.textContent); a.parentNode.replaceChild(c, a); }} }});
      var out = el("div");
      if (fm) {{
        var box = el("div", "fm"), dl = el("dl"), key = null, val = [];
        function flush() {{ if (key) {{ var dt = el("dt", null, key), dd = el("dd", null, val.join(" ").replace(/\\s+/g, " ").trim()); dl.appendChild(dt); dl.appendChild(dd); }} key = null; val = []; }}
        fm.split("\\n").forEach(function (line) {{ var km = line.match(/^(\\s*)([\\w-]+):\\s*(.*)$/); if (km && km[1].length <= 2 && !/^>-?$|^\|-?$/.test(km[3]) ) {{ flush(); key = (km[1] ? "  " : "") + km[2]; if (km[3] && !/^[>|]-?$/.test(km[3])) val.push(km[3]); }} else if (km && km[1].length <= 2) {{ flush(); key = km[2]; }} else {{ val.push(line.trim()); }} }});
        flush(); box.appendChild(el("div", "fm-label", "Frontmatter")); box.appendChild(dl); out.appendChild(box);
      }}
      out.appendChild(wrap); return out;
    }}
    function show(e, text) {{
      body.textContent = "";
      if (e.src !== e.path) {{ var n = el("p", "copy-note", "This file is a copy of " + e.src + ", placed in the skill folder by the build; the library file is shown."); body.appendChild(n); }}
      if (raw || !/\\.md$/.test(e.src)) {{ var pre = el("pre", null, text); body.appendChild(pre); }} else body.appendChild(renderMd(text));
      pathEl.textContent = e.path; metaEl.textContent = text.split("\\n").length + " lines, " + Math.round(text.length / 1024) + " KB";
      Array.prototype.forEach.call(treeEl.querySelectorAll(".fb-file"), function (li) {{ li.classList.toggle("active", li.firstChild.getAttribute("data-path") === e.path); }});
      var li = treeEl.querySelector('.fb-file a[data-path="' + e.path + '"]'); if (li) {{ for (var n2 = li.parentElement; n2 && n2 !== treeEl; n2 = n2.parentElement) if (n2.classList && n2.classList.contains("fb-dir")) n2.classList.remove("closed"); li.scrollIntoView({{ block: "nearest" }}); }}
      body.scrollTop = 0;
    }}
    function open(e) {{
      current = e;
      if (cache[e.src]) return show(e, cache[e.src]);
      if (FILES[e.src] !== undefined) {{ cache[e.src] = FILES[e.src]; return show(e, cache[e.src]); }}
      body.textContent = "Loading " + e.path;
      fetch("plugin/" + e.src).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (txt) {{ cache[e.src] = txt; if (current === e) show(e, txt); }}).catch(function (err) {{ body.textContent = "Could not load " + e.path + " (" + err.message + ")."; }});
    }}
    document.getElementById("fb-prev").addEventListener("click", function () {{ if (!current) return; var i = order.indexOf(current.path); if (i > 0) open(files[i - 1]); }});
    document.getElementById("fb-next").addEventListener("click", function () {{ var i = current ? order.indexOf(current.path) : -1; if (i < files.length - 1) open(files[i + 1]); }});
    document.getElementById("fb-raw").addEventListener("click", function () {{ raw = !raw; this.textContent = raw ? "Rendered" : "Raw"; if (current) open(current); }});
    filterEl.addEventListener("input", function () {{ var q = filterEl.value.trim().toLowerCase(); Array.prototype.forEach.call(treeEl.querySelectorAll(".fb-file"), function (li) {{ li.hidden = q ? li.firstChild.getAttribute("data-path").toLowerCase().indexOf(q) === -1 : false; }}); Array.prototype.forEach.call(treeEl.querySelectorAll(".fb-dir"), function (li) {{ var any = li.querySelector(".fb-file:not([hidden])"); li.hidden = q ? !any : false; if (q && any) li.classList.remove("closed"); }}); }});
    function fromHash() {{ var h = location.hash.slice(1); if (h.indexOf("f.") === 0) {{ var e = fromToken(h); if (e) {{ open(e); var sec = document.getElementById("browse"); if (sec) sec.scrollIntoView(); }} }} }}
    window.addEventListener("hashchange", fromHash); fromHash();
    if (window.KSearch) files.forEach(function (e) {{ KSearch.add(e.path, "File", function () {{ open(e); location.hash = token(e.path); }}); }});
    if (!location.hash) open(files.filter(function (e) {{ return e.path === "skills/bigdata-earnings-preview/SKILL.md"; }})[0] || files[0]);
  }})();
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
