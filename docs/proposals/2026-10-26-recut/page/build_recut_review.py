#!/usr/bin/env python3
"""Build the Skills Re-cut Review page: each proposed change with its before and after in full,
a decision and a comment per item, saved in the page's database (collection `reviews`).

    PAGE_INPUTS=<dir with fonts-platform.css, logo.datauri, logo-dark.datauri> python3 -I build_recut_review.py [out.html]
    python3 ~/.agents/skills/build-artifact/scripts/kit.py inline <out.html>
"""
import glob, json, os, re, sys, time

PAGE = os.path.dirname(os.path.abspath(__file__))
RECUT = os.path.dirname(PAGE)
W = os.environ.get("SKILLS_WORKTREE", "/Users/mkangrga/python_projects/bigdata-mcp/bigdata-plugins-marketplace/.claude/worktrees/skills-audit-fixes")
INPUTS = os.environ.get("PAGE_INPUTS", PAGE)
PLUG = f"{W}/plugins/bigdata-com"
EV = f"{PLUG}/evals/quality-2026-10-26"
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{PAGE}/recut-review.html"
READER_URL = "https://claude.ai/artifact/HPgghcdyAaBcEM9x3JwDrg"
PROPOSAL_URL = "https://claude.ai/artifact/CoETtAqbh3bWgotehF1bEU"

def rd(p):
    with open(p, encoding="utf-8") as f: return f.read()
def rj(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
def body_of(skill_md):
    """Drop the frontmatter so the rendered page shows the body."""
    parts = skill_md.split("---", 2)
    return parts[2].strip() if len(parts) == 3 else skill_md
def desc_of(name):
    s = rd(f"{PLUG}/skills/bigdata-{name}/SKILL.md"); m = re.search(r"description: >-\n((?:  .*\n)+)", s)
    return " ".join(l.strip() for l in m.group(1).splitlines())
def section(md, heading, until=None):
    """Lines from `## heading` to the next `## ` (or `until`)."""
    lines = md.splitlines(); out = []; on = False
    for l in lines:
        if l.startswith("## ") and on and (until is None or l.startswith(until) or l.startswith("## ")): break
        if l.strip() == f"## {heading}": on = True
        if on: out.append(l)
    return "\n".join(out)

val_cur = rd(f"{PLUG}/skills/bigdata-valuation/SKILL.md")
er_cur = rd(f"{PLUG}/skills/bigdata-earnings-review/SKILL.md")
val_new = rd(f"{RECUT}/valuation.recut.md")
er_new = rd(f"{RECUT}/earnings-review.recut.md")
std_cur = rd(f"{PLUG}/library/output-standard.md")
style_new = rd(f"{RECUT}/output-standard.recut.md")
br = rd(f"{PLUG}/library/methods/base-rates.md")
br_formula = section(br, "Formulas").split("\n**2.")[0].strip()
br_sources = section(br, "Sources").strip()
exp = rd(f"{PLUG}/library/methods/expectations.md")
exp_out = section(exp, "Output lines").strip()
gm_meta = rj(f"{EV}/iteration-1/earnings-review-corp-gm/eval_metadata.json")
gm_with = rd(f"{EV}/iteration-1/earnings-review-corp-gm/with_skill/outputs/report.md")
gm_heads = [h for h in re.findall(r"^## (.+)$", gm_with, re.M)]
gm_without = rd(f"{EV}/iteration-1/earnings-review-corp-gm/without_skill/outputs/report.md")
gm_wo_heads = [h for h in re.findall(r"^## (.+)$", gm_without, re.M)]

def words(p): return len(rd(p).split())
LIB = {os.path.basename(f)[:-3]: words(f) for f in glob.glob(f"{PLUG}/library/**/*.md", recursive=True)}
def read_budget(name):
    s = rd(f"{PLUG}/skills/bigdata-{name}/SKILL.md"); m = re.search(r"bigdata-refs: (.*)", s)
    refs = [r.strip() for r in m.group(1).split(",")] if m else []
    lib = sum(LIB.get(r, 0) for r in refs); primer = 1800 if "sector-primer: auto" in s else 0
    return len(body_of(s).split()), len(refs), lib, primer
vb, vr, vl, vp = read_budget("valuation"); eb, er_, el, ep = read_budget("earnings-review")
val_new_words = len(body_of(val_new).split()); er_new_words = len(body_of(er_new).split())

def md_list(items): return "\n".join(f"- {i}" for i in items)

ITEMS = []
def item(id, title, q, why, before, after, options=("Yes", "Yes, with the changes in my comment", "No"), before_label="Now", after_label="Proposed", layout="two"):
    ITEMS.append({"id": id, "title": title, "q": q, "why": why, "before": before, "after": after, "options": list(options),
                  "before_label": before_label, "after_label": after_label, "layout": layout})

item("body-valuation", "Skill bodies: the valuation example",
     "Is this the shape for all the skill bodies?",
     f"Same steps as today, in the same order. Gone: the \"done when\" after every step, the step-number pointers into the method files, the fixed-column report template, the eleven checks and the hand-offs. The pitfalls sit inside the step they belong to. {val_new_words:,} words instead of {vb:,}, and the method files open only when a step needs them instead of {vl:,} words read before the first call.",
     body_of(val_cur), body_of(val_new))

item("body-earnings-review", "Skill bodies: the earnings review example",
     "Same question, for the skill behind the GM report.",
     f"This one also checks the premise of the question against the release first (GM did not lower its outlook), and puts a supplier's or customer's questions before the investor sections. {er_new_words:,} words instead of {eb:,}.",
     body_of(er_cur), body_of(er_new))

gm_after = [
    "What happened against expectations (the beat, the narrowed range with the midpoint unchanged)",
    "Results and guidance tables",
    "What the quarter says about North American vehicle demand",
    "GM's cost plans and where a supplier sits in them",
    "Programme timing: the full-size pickup changeover and other capacity moves",
    "How the Street read it",
    "What our planning team should take from it: volume, commercial and pricing, footprint, finance (the $4.5bn inventory banking facility and the $1.2bn supplier-finance programme go here)",
    "What to watch, with dates",
]
item("write-step", "Report structure follows the question",
     "Should only the core tables be fixed, with the rest of the report following the question?",
     "For the GM supplier prompt the template put the supplier's three questions in section 12 of 16, after valuation, peer read-across and market reaction. The rule on the right fixes the results and guidance tables and lets the question set the rest.",
     "**The prompt**\n\n> " + gm_meta["prompt"] + "\n\n**Sections the template produced**\n\n" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(gm_heads)),
     "**Sections for the same prompt under the new rule**\n\n" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(gm_after)) +
     "\n\n**The rule, as it reads in the earnings review skill**\n\n> The results table and the guidance table come next, because everything else rests on them. Then the sections the question needs, in the order the question asked them: for a thesis holder, the thesis check, the valuation refresh, quality signals, the reaction, the read-across; for a supplier, customer or competitor, what the print means for their business, then the Street's reception and the read-across, with the investor sections left out unless asked. A row exists only where there is a figure.",
     options=("Yes", "No, keep a fixed order per skill"))

item("output-rules", "The shared output rules",
     "Keep one short shared file of rules every report follows, trimmed to this?",
     f"Today's file (output-standard.md, {len(std_cur.split()):,} words) fixes a six-part frame, mandatory Basis and Source columns, a Gaps section and the footer on every answer including one-liners. The draft is {len(style_new.split()):,} words: answer first, numbers with their basis, citations as links at the claim, no recommendation, the footer. Each skill points to it instead of repeating it.",
     std_cur, style_new, options=("Keep, trimmed to this", "Drop the file, put the few rules in each skill", "Keep as it is today"))

lib_before = ("**base-rates.md, formula 1, as it reads now**\n\n" + br_formula + "\n\n**base-rates.md, the Sources section at the end**\n\n" + br_sources +
              "\n\n**expectations.md, the Output lines section**\n\n" + exp_out)
lib_after = """**base-rates.md, formula 1**

**1. Regression to the mean and shrinkage**

- Expected outcome = mean + r x (current outcome - mean), where r is the correlation between the metric now and the same metric earlier. With r = 1 the best estimate is the last value; with r = 0 it is the mean.
- Shrinkage form: estimated true level = grand average + c x (observed - grand average), c between 0 and 1, with r as the proxy for c.
- The more luck in the outcome, the more weight on the base rate; the more skill, the more on the inside view.
- Use the r that matches the horizon. The four-year r is higher than the one-year r compounded, so applying a one-year r four times overstates the speed of fading.

**Removed from every method file and primer**

- The Sources sections and the literature file keys ("A" to "G", "PE", "EI", "DCF2").
- The "(verify)" working notes (65 of them, mostly in the sector primers).
- The Output lines sections: scripted sentences for the agent to fill in.
- Worked examples copied from the papers (Microsoft CFROI, staples fade).
- "Note author" remarks about what was approximated.

**What stays**: when to use the method, the inputs and where they come from, the procedure, the formulas, the reference tables with their sample and period, the limits.

The research trail (which paper each formula came from, the worked examples, the open verify notes) moves to docs/proposals/2026-10-26-recut/provenance.md for the team. The agent never reads it."""
item("library", "The library: only what the agent acts on",
     "Strip the method files to procedure, formulas, tables and pitfalls?",
     "Everything else goes: the sources sections, the literature file keys, the verify notes, the scripted output sentences, the worked examples from the papers. The research trail moves to a file under docs that the agent never reads. Example: the regression formula in base-rates.md and the output lines of expectations.md.",
     lib_before, lib_after, options=("Yes", "Yes, but keep the worked examples", "No"))

footer_now = """**Did Nike beat?**

Yes. Revenue of $12.4bn against consensus of $12.1bn and EPS of $0.78 against $0.70 ([Nike Q1 FY2027 release, 30 Sep 2026](https://app.bigdata.com/documents/...)). Guidance for Q2 was held at low-single-digit growth ([Q1 call, 30 Sep 2026](https://app.bigdata.com/documents/...)).

Data: Bigdata.com company tearsheet for Nike, FactSet consensus, retrieved 26 Oct 2026.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions."""
footer_found = """**What a search of Slack, Confluence, Jira, Drive and the repo found**

- The disclaimer started as a product decision, not a legal one. Jira [PX-1575, "Skills - Add disclaimer in reports"](https://ravenpack.atlassian.net/browse/PX-1575), opened 5 Mar 2026 by the plugin's product manager: the LLM judge in the comparative evals flagged that outputs had no disclaimer, and adding one would improve the score. Done 14 Apr 2026. No legal reviewer on the ticket.
- The wording asked for there was one line: *"Disclaimer: This report is for informational purposes only and does not constitute investment advice. Past performance is not indicative of future results."* The longer text now in use first appears in the repo on 8 May 2026 (commit 6a57dfe); nothing found says why it grew.
- The ticket scopes it to reports. Nothing found says verbatim, at the end, or on every message.
- "Powered by Bigdata.com" came from a [sales thread in #bigdata-api, 4 Feb 2026](https://ravenpack.slack.com/archives/C06QREADVK6/p1770228042488039) asking for a watermark on the skill; the product manager replied it was already at the bottom. Branding, not legal.
- The one disclaimer a product manager called a legal requirement (18 Aug 2026, DM) is the chat-interface notice "You are interacting with an AI system", which is a different text for a different surface.
- Not covered: the Responsible AI Management Policy page on Confluence was not read, the Jira search stopped after one page, Drive hits were not opened.

So the search did not find the requirement you confirmed. If it lives somewhere the search did not reach, say where and it can be checked."""
item("footer", "The disclaimer",
     "No decision now. You confirmed it has to be there, so it stays as it is.",
     "Below, the current footer on a one-line answer, and what a search for the requirement's origin found. Comment if there is a placement you want looked at later.",
     footer_now, footer_found, options=(), before_label="Now, on a one-line answer", after_label="What the search found", layout="two")

merges = [
    ("merge-scenarios", "Merge: scenarios into valuation", "Fold scenarios into valuation?",
     "Valuation already produces three cases with probabilities and an expected value. Scenarios adds signposts. One skill, one description; the trigger words move across.",
     f"**bigdata-valuation**\n\n{desc_of('valuation')}\n\n**bigdata-scenarios**\n\n{desc_of('scenarios')}",
     "**bigdata-valuation**\n\nWhat a company is worth: the growth, margin and return the price implies, a DCF with the equity bridge checked, three cases with probabilities and signposts, a multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is priced in, scenarios, what if a driver changes. Not peers only: bigdata-comps."),
    ("merge-catalysts", "Merge: catalysts into watchlist", "Fold catalysts into watchlist?",
     "Catalysts is a dated-events list with expected impact. Watchlist already carries the next event per name, earnings preview the setup, quick take the next catalyst for one name.",
     f"**bigdata-watchlist**\n\n{desc_of('watchlist')}\n\n**bigdata-catalysts**\n\n{desc_of('catalysts')}",
     "**bigdata-watchlist**\n\nDaily or weekly check on a list of companies, or the dated events ahead for one: price move, the news behind it, earnings vs estimates, what is coming up and what it could move. Use for holdings, watchlist, peer or competitor set, what changed today, what is coming up, events to watch. Not one company's news: bigdata-company-brief."),
    ("merge-macro", "Merge: macro-compare into country", "Fold macro-compare into country?",
     "It is the country skill with more than one country, and the two kept triggering on each other's prompts until the descriptions were retuned.",
     f"**bigdata-country**\n\n{desc_of('country')}\n\n**bigdata-macro-compare**\n\n{desc_of('macro-compare')}",
     "**bigdata-country**\n\nOne country's economy and markets, or several compared on the same indicators: growth, inflation, rates, currency, fiscal and external balances, politics, what is priced in. Use for a country outlook, political risk, market entry, compare economies, which country is stronger, where to expand."),
]
for id, t, q, w, b, a in merges: item(id, t, q, w, b, a, options=("Merge", "Keep separate"), before_label="Now, two skills", after_label="Proposed, one skill")
item("thesis", "Thesis", "Keep thesis as its own skill?",
     "It is the deep dive minus the economics, plus the variant view and kill criteria. Investors ask for it; corporate readers do not.",
     f"**bigdata-thesis**\n\n{desc_of('thesis')}", f"**bigdata-deep-dive**\n\n{desc_of('deep-dive')}",
     options=("Keep", "Fold into deep dive"), before_label="Thesis", after_label="Deep dive")

cur_template = [a for a in gm_meta["assertions"] if a.startswith(("No table", "No '(verify)'", "The deliverable states what data", "The deliverable closes"))]
new_assert = [
    "States the outlook change precisely: the EBIT-adjusted range narrowed from $14 to 16bn to $14.5 to 15.5bn with the midpoint unchanged, and corrects the prompt's \"lowered\"",
    "Answers what the quarter says about North American vehicle demand, with GMNA volumes, pricing and inventory figures and their sources",
    "Describes GM's cost plans and where a tier-1 supplier sits in them, with sources",
    "The supplier's questions come before any section an investor would want; nothing in the note serves only an investor",
]
item("evals", "How the next round is graded",
     "Grade on whether the report answers the question, not on whether it follows the template?",
     "Today six of the twelve assertions mirror the output standard and the rest mirror the skill's sections, so the GM template scored 11 of 11 while a supplier could not use it.",
     "**Four of today's assertions for the GM prompt**\n\n" + md_list(cur_template),
     "**Four proposed ones**\n\n" + md_list(new_assert) + "\n\nPlus a side-by-side judge given the reader's role and both reports, and a script that counts empty cells, numbered citations and investor terms in a corporate report.",
     options=("Yes", "No"))

seq = [
    "Your answers on this page.",
    "I finish the two example bodies and the shared rules with your comments. You read them.",
    "The other 21 bodies get the same treatment. I read each one.",
    "The library stripped; the existing 24 reports re-graded the new way for a before number.",
    "The ten prompts rerun with the new skills and compared with both old runs.",
]
item("sequence", "Order of work", "Go in this order?", "About a day of my time and roughly $100 of agent and eval runs, most of it the rerun.",
     "", "\n".join(f"{i+1}. {s}" for i, s in enumerate(seq)), options=("Go", "Change"), layout="one", after_label="Proposed")

item("general", "Anything else", "", "", "", "", options=(), layout="none")

fonts = rd(f"{INPUTS}/fonts-platform.css")
logo = rd(f"{INPUTS}/logo.datauri").strip()
logo_dark = rd(f"{INPUTS}/logo-dark.datauri").strip() if os.path.exists(f"{INPUTS}/logo-dark.datauri") else logo
produced = time.strftime("%d %b %Y, %H:%M %Z")
data_json = json.dumps({"items": ITEMS}, ensure_ascii=True).replace("</", "<\\/")

rail_items = "".join(f'<li><a href="#{it["id"]}">{it["title"]}</a></li>' for it in ITEMS)
sections = "".join(f'''
<section id="{it["id"]}" data-rail="{it["title"]}" data-item="{it["id"]}">
  <h2>{it["title"]}</h2>
  <p class="q" id="q-{it["id"]}"></p>
  <p class="what" id="what-{it["id"]}"></p>
  <div class="cmp {it["layout"]}" id="cmp-{it["id"]}"></div>
  <div class="decide" id="decide-{it["id"]}"></div>
</section>''' for it in ITEMS)

page = r"""<title>Skills Re-cut Review</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
__FONTS__
/* Layout: contents rail left, one 1400px column of review items; each item is a before/after pair over a decision row. The decision row is the one bold element. */
:root {
  --surface-0: #121212; --dp01: #1E1E1E; --dp03: #252525; --dp08: #2E2E2E; --dp12: #333333;
  --fg-1: #FFFDF5; --fg-2: #FFFDF5B2; --fg-3: #FFFDF580; --border: #FFFFFF29;
  --bd-blue: #4CA7F9; --bd-blue-700: #206EB5; --overlay-blue: rgba(83,166,251,0.12);
  --green-500: #04E0A9; --overlay-green: rgba(3,166,125,0.18); --red-500: #FC4848; --overlay-red: rgba(207,102,121,0.18); --overlay-yellow: rgba(235,183,30,0.14); --yellow-500: #FDF16F;
  --bg: var(--surface-0); --surface: var(--dp01); --surface-2: var(--dp03); --line: var(--border);
  --ink: var(--fg-1); --ink-2: var(--fg-2); --muted: #A9A79F; --accent: var(--bd-blue);
  --font-display: "Moderno", "Hanken Grotesk", serif; --font-sans: "Hanken Grotesk", "Inter", system-ui, sans-serif; --font-mono: "Apercu Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --k-page-width: 1400px;
  color-scheme: dark;
}
:root[data-theme="light"] {
  --surface-0: #F4F3EF; --dp01: #FCFCFB; --dp03: #EEEDE8; --dp08: #E6E5DF; --dp12: #DCDAD3;
  --fg-1: #14161A; --fg-2: #464A51; --fg-3: #6C7178; --border: #00000024;
  --bd-blue: #206EB5; --overlay-blue: rgba(32,110,181,0.12); --green-500: #03795B; --overlay-green: rgba(3,166,125,0.16); --red-500: #C62828; --overlay-red: rgba(207,102,121,0.16); --overlay-yellow: rgba(201,172,18,0.16); --yellow-500: #8A7400;
  --muted: #6C7178; --accent: var(--bd-blue);
  color-scheme: light;
}
html { background: var(--bg); }
body { background: var(--bg); color: var(--ink); font-family: var(--font-sans); font-size: 15px; line-height: 1.55; margin: 0; -webkit-font-smoothing: antialiased; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
a { color: var(--accent); text-decoration: none; } a:hover { text-decoration: underline; }
[hidden] { display: none !important; }
main.page { padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); padding-block: 32px 96px; }
.k-rail-head img { width: 128px; }
.k-rail-head img.logo-on-light { display: none; }
:root[data-theme="light"] .k-rail-head img.logo-on-dark { display: none; }
:root[data-theme="light"] .k-rail-head img.logo-on-light { display: block; }
header.top { margin-bottom: 48px; }
header.top .eyebrow { font-size: 11px; letter-spacing: .18em; text-transform: uppercase; color: var(--fg-2); font-weight: 600; margin-bottom: 12px; }
header.top h1 { font-family: var(--font-display); font-weight: 400; font-size: 44px; line-height: 1.05; letter-spacing: -0.01em; margin: 0 0 12px; text-wrap: balance; }
header.top .sub { color: var(--fg-2); font-size: 15px; max-width: 70ch; margin: 0 0 8px; }
header.top .meta { color: var(--fg-3); font-size: 13px; margin-top: 12px; font-variant-numeric: tabular-nums; }
header.top .meta a { color: var(--fg-2); }
.keys { font-size: 13px; color: var(--fg-3); margin-top: 8px; }
kbd { font-family: var(--font-mono); font-size: 12px; border: 1px solid var(--line); border-radius: 4px; padding: 1px 6px; color: var(--ink-2); }
.save-state { display: inline-flex; align-items: center; gap: 8px; margin-top: 12px; font-size: 13px; color: var(--fg-2); border: 1px solid var(--line); border-radius: 35px; padding: 4px 12px; background: var(--surface); }
.save-state .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--muted); }
.save-state.ok .dot { background: var(--green-500); }
.save-state.warn .dot { background: var(--yellow-500); }
.progress { font-size: 13px; color: var(--fg-3); margin-top: 8px; font-variant-numeric: tabular-nums; }
section[id] { margin-bottom: 56px; padding-top: 8px; }
h2 { font-size: 24px; font-weight: 600; line-height: 1.2; margin: 0 0 12px; text-wrap: balance; }
p.q { font-size: 17px; font-weight: 600; margin: 0 0 6px; max-width: 80ch; }
p.what { color: var(--fg-2); margin: 0 0 16px; max-width: 90ch; }
p.q:empty, p.what:empty { display: none; }

/* Before and after */
.cmp { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
.cmp.one, .cmp.one-before { grid-template-columns: 1fr; }
.cmp.none { display: none; }
.pane { border: 1px solid var(--line); border-radius: 8px; background: var(--surface); min-width: 0; }
.pane-h { padding: 8px 16px; border-bottom: 1px solid var(--line); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--fg-3); font-weight: 600; display: flex; justify-content: space-between; gap: 12px; }
.pane-h span:last-child { letter-spacing: 0; text-transform: none; font-weight: 400; font-variant-numeric: tabular-nums; }
.pane-b { padding: 14px 16px 20px; overflow: auto; max-height: 70vh; overscroll-behavior: contain; }
.pane.after { border-color: var(--bd-blue-700); }
.pane.after .pane-h { color: var(--accent); }

/* Rendered markdown */
.doc { font-size: 14.5px; line-height: 1.6; }
.doc > :first-child { margin-top: 0; }
.doc h1 { font-size: 20px; font-weight: 600; line-height: 1.25; margin: 0 0 12px; }
.doc h2 { font-size: 16px; font-weight: 600; margin: 22px 0 8px; }
.doc h3 { font-size: 15px; font-weight: 600; margin: 16px 0 6px; }
.doc h4, .doc h5, .doc h6 { font-size: 14px; font-weight: 600; margin: 14px 0 4px; }
.doc p { margin: 0 0 10px; }
.doc ul, .doc ol { margin: 0 0 10px; padding-left: 22px; }
.doc li { margin: 0 0 4px; }
.doc li::marker { color: var(--fg-3); }
.doc em { font-style: italic; }
.doc hr { border: 0; border-top: 1px solid var(--line); margin: 16px 0; }
.doc blockquote { margin: 0 0 10px; padding: 2px 12px; border-left: 2px solid var(--line); color: var(--fg-2); }
.doc code { font-family: var(--font-mono); font-size: 0.9em; background: var(--surface-2); padding: 0.05em 0.35em; border-radius: 4px; overflow-wrap: anywhere; }
.doc pre { font-family: var(--font-mono); font-size: 12.5px; line-height: 1.5; background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 10px 12px; overflow-x: auto; margin: 0 0 10px; white-space: pre-wrap; }
.doc pre code { background: none; padding: 0; }
.doc .tbl { overflow-x: auto; margin: 0 0 12px; border: 1px solid var(--line); border-radius: 8px; }
.doc table { border-collapse: collapse; width: 100%; font-size: 13px; }
.doc th, .doc td { text-align: left; vertical-align: top; padding: 5px 9px; border-bottom: 1px solid var(--line); }
.doc th { font-weight: 600; color: var(--fg-2); white-space: nowrap; background: var(--surface-2); }
.doc tr:last-child td { border-bottom: 0; }
.doc a { overflow-wrap: anywhere; }

/* Decision row */
.decide { border: 1px solid var(--line); border-radius: 8px; background: var(--surface); padding: 12px 16px 16px; display: grid; grid-template-columns: auto 1fr; gap: 12px 24px; align-items: start; }
.decide.noopts { grid-template-columns: 1fr; }
.decide .lbl { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--fg-3); font-weight: 600; margin-bottom: 6px; }
.seg { display: inline-flex; flex-wrap: wrap; border: 1px solid var(--line); border-radius: 35px; overflow: hidden; background: var(--bg); }
.seg button { background: transparent; color: var(--ink-2); border: 0; padding: 7px 14px; font: inherit; font-size: 13px; cursor: pointer; white-space: nowrap; }
.seg button + button { border-left: 1px solid var(--line); }
.seg button[aria-pressed="true"] { background: var(--overlay-blue); color: var(--ink); font-weight: 600; }
.seg button:hover { color: var(--ink); }
.seg button:focus-visible { outline-offset: -3px; }
.seg button kbd { margin-right: 6px; font-size: 11px; }
textarea { width: 100%; box-sizing: border-box; min-height: 72px; background: var(--bg); color: var(--ink); border: 1px solid var(--line); border-radius: 4px; padding: 8px 10px; font: inherit; font-size: 14px; line-height: 1.5; resize: vertical; }
.decide .state { font-size: 12px; color: var(--fg-3); margin-top: 4px; min-height: 16px; font-variant-numeric: tabular-nums; }
section.answered h2::after { content: "answered"; font-family: var(--font-mono); font-size: 11px; letter-spacing: .04em; text-transform: uppercase; color: var(--green-500); background: var(--overlay-green); border-radius: 4px; padding: 2px 7px; margin-left: 12px; vertical-align: middle; font-weight: 600; }

@media (max-width: 900px) {
  header.top h1 { font-size: 34px; }
  .cmp { grid-template-columns: 1fr; }
  .pane-b { max-height: 60vh; }
  .decide { grid-template-columns: 1fr; }
  .seg { flex-direction: column; border-radius: 8px; width: 100%; }
  .seg button { text-align: left; }
  .seg button + button { border-left: 0; border-top: 1px solid var(--line); }
}
</style>
<!-- kit: tooltip rail fold search -->
<nav class="k-rail" aria-label="Contents"><div class="k-rail-head"><img class="logo-on-dark" src="__LOGO__" alt="Bigdata.com"><img class="logo-on-light" src="__LOGO_DARK__" alt="Bigdata.com"><span>Re-cut review</span></div><ul></ul></nav>
<main class="k-page page">
<header class="top">
  <div class="eyebrow">Bigdata.com skills, re-cut</div>
  <h1>Skills Re-cut Review</h1>
  <p class="sub">One question per item, with the current text and the proposed text in full underneath. Pick an answer and leave a comment where you want something changed; the answers are saved on this page.</p>
  <div class="meta">Produced __PRODUCED__. The reports behind this are on the <a href="__READER_URL__" target="_blank" rel="noopener">Skills Eval Reader</a>; the score tables and the audit are on the <a href="__PROPOSAL_URL__" target="_blank" rel="noopener">Job Skills Proposal</a>.</div>
  <div class="keys">Keys: <kbd>j</kbd> and <kbd>k</kbd> move between items, <kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd> pick a decision on the item in view, <kbd>c</kbd> jumps to its comment box, <kbd>Cmd</kbd>+<kbd>K</kbd> searches the page.</div>
  <div class="save-state" id="save-state"><span class="dot"></span><span id="save-text">Connecting to the page's database</span></div>
  <div class="progress" id="progress"></div>
</header>
__SECTIONS__
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js" integrity="sha384-/TQbtLCAerC3jgaim+N78RZSDYV7ryeoBCVqTuzRrFec2akfBkHS7ACQ3PQhvMVi" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.0.9/purify.min.js" integrity="sha384-3HPB1XT51W3gGRxAmZ+qbZwRpRlFQL632y8x+adAqCr4Wp3TaWwCLSTAJJKbyWEK" crossorigin="anonymous"></script>
<script type="application/json" id="data">__DATA__</script>
<script>
(function () {
  var DATA = JSON.parse(document.getElementById("data").textContent), ITEMS = DATA.items;
  var answers = {}, db = null, timers = {}, dbState = "connecting";
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function renderMd(md) {
    var box = el("div", "doc"); var html = marked.parse(md || "", { gfm: true, breaks: false });
    box.innerHTML = window.DOMPurify ? DOMPurify.sanitize(html) : html;
    Array.prototype.forEach.call(box.querySelectorAll("table"), function (t) { var w = el("div", "tbl"); t.parentNode.insertBefore(w, t); w.appendChild(t); });
    Array.prototype.forEach.call(box.querySelectorAll("a[href]"), function (a) { if (!/^https?:\/\//i.test(a.getAttribute("href"))) { a.removeAttribute("href"); return; } a.target = "_blank"; a.rel = "noopener"; });
    return box;
  }
  function wc(s) { return (s || "").split(/\s+/).filter(Boolean).length; }
  function pane(label, md, cls) {
    var p = el("div", "pane " + cls); var h = el("div", "pane-h"); h.appendChild(el("span", null, label)); h.appendChild(el("span", null, wc(md).toLocaleString("en-US") + " words")); p.appendChild(h);
    var b = el("div", "pane-b"); b.setAttribute("data-check", "skip"); b.appendChild(renderMd(md)); p.appendChild(b); return p;
  }
  function setState(cls, text) { var s = document.getElementById("save-state"); s.className = "save-state " + cls; document.getElementById("save-text").textContent = text; }
  function progress() {
    var n = 0, total = 0; ITEMS.forEach(function (it) { if (it.options.length) { total++; if (answers[it.id] && answers[it.id].decision) n++; } });
    document.getElementById("progress").textContent = n + " of " + total + " decisions made";
    ITEMS.forEach(function (it) { var a = answers[it.id]; document.getElementById(it.id).classList.toggle("answered", !!(a && (a.decision || (a.comment && a.comment.trim())))); });
  }
  function fmt(iso) { try { var d = new Date(iso); return d.toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" }); } catch (e) { return ""; } }
  function save(id) {
    var a = answers[id] || {}; var state = document.querySelector('#decide-' + id + ' .state');
    if (!db) { state.textContent = "Not saved: this page's database is not available in this view."; return; }
    state.textContent = "Saving";
    var body = { decision: a.decision || "", comment: a.comment || "", updatedAt: new Date().toISOString() };
    db.doc("reviews/" + id).set(body).then(function () { answers[id] = body; state.textContent = "Saved " + fmt(body.updatedAt); setState("ok", "Answers are being saved to this page"); progress(); })
      .catch(function (e) { state.textContent = "Not saved (" + (e && e.code ? e.code : "error") + "). Try again, or paste the answer in chat."; setState("warn", "A save failed; see the item"); });
  }
  function renderItem(it) {
    document.getElementById("q-" + it.id).textContent = it.q; document.getElementById("what-" + it.id).textContent = it.why;
    var c = document.getElementById("cmp-" + it.id); c.textContent = "";
    if (it.layout === "two") { c.appendChild(pane(it.before_label, it.before, "before")); c.appendChild(pane(it.after_label, it.after, "after")); }
    else if (it.layout === "one") { c.appendChild(pane(it.after_label, it.after, "after")); }
    else if (it.layout === "one-before") { c.appendChild(pane(it.before_label, it.before, "before")); }
    var d = document.getElementById("decide-" + it.id); d.textContent = ""; d.classList.toggle("noopts", !it.options.length);
    var a = answers[it.id] || {};
    if (it.options.length) {
      var left = el("div"); left.appendChild(el("div", "lbl", "Decision"));
      var seg = el("div", "seg"); seg.setAttribute("role", "group"); seg.setAttribute("aria-label", "Decision on " + it.title);
      it.options.forEach(function (o, i) {
        var b = el("button"); b.type = "button"; var k = el("kbd", null, String(i + 1)); b.appendChild(k); b.appendChild(document.createTextNode(o));
        b.setAttribute("aria-pressed", String(a.decision === o)); b.setAttribute("data-opt", o);
        b.addEventListener("click", function () { answers[it.id] = Object.assign({}, answers[it.id] || {}, { decision: o }); Array.prototype.forEach.call(seg.children, function (x) { x.setAttribute("aria-pressed", String(x === b)); }); save(it.id); });
        seg.appendChild(b);
      });
      left.appendChild(seg); d.appendChild(left);
    }
    var right = el("div"); right.appendChild(el("div", "lbl", it.options.length ? "Comment" : "Comments"));
    var ta = el("textarea"); ta.id = "comment-" + it.id; ta.setAttribute("aria-label", "Comment on " + it.title); ta.placeholder = it.options.length ? "What to change, or why" : "Anything else"; ta.value = a.comment || "";
    ta.addEventListener("input", function () { answers[it.id] = Object.assign({}, answers[it.id] || {}, { comment: ta.value }); clearTimeout(timers[it.id]); timers[it.id] = setTimeout(function () { save(it.id); }, 900); });
    right.appendChild(ta); var st = el("div", "state"); st.textContent = a.updatedAt ? "Saved " + fmt(a.updatedAt) : ""; right.appendChild(st); d.appendChild(right);
  }
  ITEMS.forEach(renderItem); progress();

  /* Keys */
  function current() { var best = null, bestD = Infinity; ITEMS.forEach(function (it) { var r = document.getElementById(it.id).getBoundingClientRect(); var d = Math.abs(r.top - 80); if (r.bottom > 80 && d < bestD) { bestD = d; best = it; } }); return best || ITEMS[0]; }
  document.addEventListener("keydown", function (ev) {
    if (ev.target && (ev.target.tagName === "INPUT" || ev.target.tagName === "TEXTAREA" || ev.target.tagName === "SELECT")) return;
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    var it = current(), i = ITEMS.indexOf(it);
    if (ev.key === "j" && i < ITEMS.length - 1) document.getElementById(ITEMS[i + 1].id).scrollIntoView({ behavior: "smooth", block: "start" });
    else if (ev.key === "k" && i > 0) document.getElementById(ITEMS[i - 1].id).scrollIntoView({ behavior: "smooth", block: "start" });
    else if (ev.key === "c") { var ta = document.getElementById("comment-" + it.id); if (ta) { ta.focus(); ev.preventDefault(); } }
    else if (/^[1-3]$/.test(ev.key)) { var b = document.querySelectorAll("#decide-" + it.id + " .seg button")[Number(ev.key) - 1]; if (b) b.click(); }
  });

  /* Database */
  function boot() {
    if (!window.claude || !window.claude.use) { setState("warn", "Not on claude.ai: answers are not saved. Open the page on claude.ai, signed in."); return; }
    window.claude.use("db").then(function (d) {
      if (!d) { setState("warn", "Answers are not being saved in this view (no database access). Paste them in chat instead."); return; }
      db = d;
      return db.collection("reviews").get().then(function (snap) {
        snap.docs.forEach(function (doc) { if (doc.exists) answers[doc.id] = doc.data(); });
        ITEMS.forEach(renderItem); progress(); setState("ok", "Answers are saved to this page as you go");
      });
    }).catch(function () { setState("warn", "Could not read earlier answers; new ones will still be saved"); });
  }
  boot();
})();
</script>
"""
page = (page.replace("__FONTS__", fonts).replace("__LOGO__", logo).replace("__LOGO_DARK__", logo_dark).replace("__PRODUCED__", produced)
        .replace("__READER_URL__", READER_URL).replace("__PROPOSAL_URL__", PROPOSAL_URL).replace("__SECTIONS__", sections).replace("__DATA__", data_json))
with open(OUT, "w", encoding="utf-8") as f: f.write(page)
print(f"wrote {OUT} ({len(page.encode('utf-8'))/1e6:.2f} MB), {len(ITEMS)} items")
