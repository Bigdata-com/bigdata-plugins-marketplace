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
            t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
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
        if ln.startswith("|"):
            flush_para(buf); buf = []
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
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
order.append(section("summary", "Summary", "Summary", md(sections[1][1])))
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

# Appendix B: drafts
drafts = []
for name in ["bigdata-earnings-preview", "bigdata-stock-move", "bigdata-quick-take", "bigdata-deep-dive"]:
    t = rd(f"{skills_dir}/{name}.SKILL.md")
    lines = t.count("\n") + 1
    drafts.append(f'<details class="k-fold" id="draft-{name}"><summary>{esc(name)}/SKILL.md <small>{lines} lines</small></summary><div class="k-fold-body doc">{md(t, gl=False, base_h=4)}</div></details>')
order.append(section("drafts", "Skill drafts", "Four complete SKILL.md drafts",
    "<p>The four skills written first, to the skeleton in section 6. Each opens as a rendered document.</p><div class=\"folds\">" + "".join(drafts) + "</div>"))

# Appendix C: method specs
spec_order = ["expectations", "base-rates", "roic", "valuation", "multiples-and-peers", "earnings-quality", "capital-allocation", "industry-structure", "operating-leverage-and-tam", "after-a-price-move", "downside-and-catalysts", "forecasting-discipline", "credit", "special-situations-arithmetic"]
specs = []
for name in spec_order:
    t = rd(f"{specs_dir}/{name}.md"); t = re.sub(r"^# Spec: ", "# ", t)
    gaps = t.count("GAP"); words = len(t.split())
    specs.append(f'<details class="k-fold" id="spec-{name}"><summary>{esc(name)}.md <small>{words:,} words, {gaps} gap{"s" if gaps != 1 else ""}</small></summary><div class="k-fold-body doc">{md(t, gl=False, base_h=4)}</div></details>')
order.append(section("specs", "Method specs", "Specification of each method file",
    "<p>Each file's specification: inputs mapped to Bigdata.com fields, the procedure with a done condition per step, formulas, reference tables with source and period, interpretation rules, output lines and sources. A GAP line marks something the source papers do not give; the writer sources it elsewhere or leaves it as an assumption.</p><div class=\"folds\">" + "".join(specs) + "</div>"))
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
ul.gaps li {{ background: var(--overlay-yellow); padding: 2px 8px; border-radius: 4px; list-style: none; margin-left: -22px; }}
.folds {{ display: flex; flex-direction: column; gap: 8px; }}
details.k-fold > summary {{ font-size: 15px; color: var(--ink); font-family: var(--font-mono); }}
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
  <div class="sub">Proposal for the rewrite: 25 job skills plus the entry skill, a shared method library, one package per host, and the evaluation that gates release. For review by Marko and the Bigdata.com product and MCP team.</div>
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
