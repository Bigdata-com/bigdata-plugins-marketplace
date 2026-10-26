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
style_new = rd(f"{RECUT}/house-style.md")
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
def item(id, title, what, before, after, options=("Approve", "Approve with changes", "Reject"), before_label="Now", after_label="Proposed", layout="two"):
    ITEMS.append({"id": id, "title": title, "what": what, "before": before, "after": after, "options": list(options),
                  "before_label": before_label, "after_label": after_label, "layout": layout})

item("body-valuation", "Skill body: valuation",
     f"A middle ground, not a rewrite. The opener, the scope, the ordered gather steps and the ordered analyse steps stay, because the method is sequential and the gather steps are what found the better evidence in the evals. What goes: the \"done when\" line on every step, the step-number pointers into the method files (replaced by the file named by topic), the 10-table write template with fixed columns, the formula numbers, the hand-offs section and the 11-item checklist. The pitfalls the audit found (beta, excess cash, capex from net PP&E, the horizon set from the price) sit inside the step they belong to. The write section gives the natural order of the tables and lets a narrower question keep only what it needs. "
     f"Current body {vb:,} words plus {vl:,} words of library the agent is told to read before the first call; proposed {val_new_words:,} words, with the method files opened when a step needs them. Both in full. The description does not change, so triggering is unaffected.",
     body_of(val_cur), body_of(val_new))

item("body-earnings-review", "Skill body: earnings review",
     f"The same treatment for the skill behind the GM report. The scope now checks the premise of the question against the release (GM did not lower its outlook) and settles the reader before gathering; the write section puts the results and guidance tables first and then follows the order of the question, with the investor sections left out for a supplier, customer or competitor unless asked. "
     f"Current body {eb:,} words plus {el:,} words of library read up front; proposed {er_new_words:,} words. Both in full.",
     body_of(er_cur), body_of(er_new))

gm_after = [
    "What happened against expectations (the beat, the narrowed range with the midpoint unchanged)",
    "What the quarter says about North American vehicle demand",
    "The 2026 outlook change, precisely (prior against new, dated, and what management stopped saying)",
    "GM's cost plans and where a supplier sits in them (warranty and EV savings fading, purchased material next, the December budget)",
    "Programme timing: the full-size pickup changeover and other capacity moves",
    "How the Street read it (revisions, targets, the reasons given)",
    "What our planning team should take from it: volume, commercial and pricing, footprint, finance (the $4.5bn inventory banking facility and the $1.2bn supplier-finance programme go here)",
    "What to watch, with dates",
]
item("write-step", "Write step: the GM prompt as the test",
     "The write step keeps the tables that everything rests on in a fixed place and lets the rest follow the question. "
     "Below, what the current template produced for the supplier prompt against what the proposed rule would produce for the same prompt, using the evidence the with-skill run actually found (the inventory banking facility, the supplier-finance programme, the dropped free-cash-flow language). "
     "The point is not that the without-skill structure was perfect; it is that the structure should come from the question.",
     "**The prompt**\n\n> " + gm_meta["prompt"] + "\n\n**Sections the current template produced (with skill, round 1)**\n\n" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(gm_heads)) +
     "\n\nThe supplier's three questions are answered in section 12 of 16, after valuation and targets, peer read-across, quality signals and market reaction. The results grid carries nine n/a cells where GM does not guide.",
     "**The prompt**\n\n> " + gm_meta["prompt"] + "\n\n**Sections the proposed write rule gives for the same prompt**\n\n" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(gm_after)) +
     "\n\n**The rule, as it reads in the skill**\n\n> The results table and the guidance table come next, because everything else rests on them. Then the sections the question needs, in the order the question asked them: for a thesis holder, the thesis check, the valuation refresh, quality signals, the reaction, the read-across; for a supplier, customer or competitor, what the print means for their business, then the Street's reception and the read-across, with the investor sections left out unless asked. A row exists only where there is a figure.\n\n"
     "**For comparison, the sections the without-skill run chose**\n\n" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(gm_wo_heads)),
     before_label="Now (round 1 with skill)", after_label="Proposed")

item("house-style", "Output standard becomes a house style",
     f"The current output standard ({len(std_cur.split()):,} words) fixes a six-part frame, mandatory Basis and Source columns, a Gaps section, a Sources section and the footer on every deliverable including one-line answers. "
     f"The proposed house style ({len(style_new.split()):,} words) keeps what protects quality (answer first, numbers with their basis, citations at capture, no recommendation, plain language) and drops the frame, the mandatory columns and the hand-off offers. Both in full.",
     std_cur, style_new)

item("provenance", "Library: research provenance out of the text the agent reads",
     "The method files carry the research phase's audit trail in the running text: file keys for the literature folder (\"F\", \"A\"), \"source example\" lines, \"(verify)\" working notes (65 of them in the sector primers), and notes about what the note author approximated. "
     "The agent reproduces them (\"method gaps about missing primers\", \"1950 to 2015 base rates\" in a corporate memo). Proposed: the keys and working notes move to one provenance file under docs/, each method file keeps its Sources section at the end, and the formulas read as formulas. Example: formula 1 of base-rates.md.",
     br_formula + "\n\n*(and, at the end of the file)*\n\n" + br_sources,
     """**1. Regression to the mean and shrinkage**

- Expected outcome = mean + r x (current outcome - mean), where r is the correlation between the metric now and the same metric earlier. With r = 1 the best estimate is the last value; with r = 0 it is the mean.
- Shrinkage form: estimated true level = grand average + c x (observed - grand average), c between 0 and 1, with r as the proxy for c. Example: grand average 8 percent, observed 12 percent, c = 0.10 gives 8.4 percent.
- The more luck in the outcome, the more weight on the base rate; the more skill, the more on the inside view.
- Use the r that matches the horizon. The four-year r is higher than the one-year r compounded, so applying a one-year r four times overstates the speed of fading. Interpolating between years with r^(t/4) is an approximation, not a published method.

*(at the end of the file, unchanged)*

## Sources

- Mauboussin, Callahan and co-authors, Credit Suisse: The Base Rate Book (2016) and its sales growth, earnings growth and gross profitability volumes (2015 to 2016); How to Model Reversion to the Mean (2013); What Makes for a Useful Statistic (2016).

*(and in docs/proposals/2026-10-26-recut/provenance.md, for the team, never read by the agent)*

**base-rates.md, formula 1.** From "F" How to Model Reversion to the Mean (17 Sep 2013) and "A" The Base Rate Book (26 Sep 2016). Worked examples: Microsoft CFROI 16.1 percent, IT sector mean 9.0 percent, four-year r 0.50 gives 12.6 percent (F). Staples with CFROI 10 points above the sector mean: 0.89 applied four times leaves 6.3 points, the four-year r of 0.78 leaves 7.8 (paper F with its 2013 data gives 6.0 against 7.3). The r^(t/4) interpolation is the note author's, not in the papers.""")

item("reader-gating", "Library: investor-only outputs marked as such",
     "The method files produce investor outputs by default: the implied competitive advantage period, the steady-state P/E, kill criteria, who must own the stock. A corporate ask inherits them, which is how a supplier memo got a competitive advantage period. "
     "Proposed: each method file's output section names which lines are for an investor reader; the skill's reader paragraph says the same from the other side. Example: the output lines of expectations.md.",
     exp_out,
     """## Output lines

For every reader:

- "EV is Z, from market cap X and net debt Y (reported). NOPAT1 is N from consensus EBIT of E [vintage] at a T percent tax rate (derived)."
- "At an assumed cost of capital of K percent (assumed; range K-1 to K+1), the price implies perpetual NOPAT growth of g percent at ROIIC of R percent (derived)."
- "The price needs g percent growth for N years at R percent ROIIC. Consensus is A. In the reference class, B percent of companies achieved this [sample and period] (reported, historical base rate)."

For an investor reader, when they asked what is priced in or for a view:

- "The steady state explains S percent of EV; V turns of the P/E pay for future value creation (derived)."
- "The implied terminal multiple is X against Y today (derived)."
- "The value trigger is [incremental return | sales growth] because ROIIC is [near | well above] the cost of capital (judgment)."

A corporate reader gets the first three and what they mean for the decision they asked about (a target's price, their own plan, a competitor's rating). The investor lines appear only when asked for.""")

footer_before = """**Did Nike beat?**

Yes. Revenue of $12.4bn against consensus of $12.1bn and EPS of $0.78 against $0.70 ([Nike Q1 FY2027 release, 30 Sep 2026](https://app.bigdata.com/documents/...)). Guidance for Q2 was held at low-single-digit growth ([Q1 call, 30 Sep 2026](https://app.bigdata.com/documents/...)).

Data: Bigdata.com company tearsheet for Nike, FactSet consensus, retrieved 26 Oct 2026.

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.

*(the same two blocks close every deliverable, from a one-line answer to a ten-page deep dive)*"""
footer_after = """**Option A: as now.** The Powered by line and the full disclaimer close every deliverable, including a one-line answer. Nothing changes.

**Option B: full text on documents, one line in chat.** A report delivered as a document or a file (Word, a saved report) ends on the full disclaimer. A chat answer ends on one line:

> *Research assistance from Bigdata.com (https://bigdata.com), not investment advice.*

So the Nike answer above would end:

> Data: Bigdata.com company tearsheet for Nike, FactSet consensus, retrieved 26 Oct 2026.
> *Research assistance from Bigdata.com (https://bigdata.com), not investment advice.*

**Option C: full text once per conversation.** The first deliverable in a conversation ends on the full disclaimer; later ones in the same conversation end on the one-liner.

In every option the no-recommendation rule stays as it is. Whether the full text is a legal requirement is a question for your side; the page does not assume an answer."""
item("footer", "Footer and disclaimer", "Where the footer came from: the shipped plugin on main already required both blocks verbatim at the end of every deliverable, the 23 October proposal carried it, and the output standard added \"including a one-line answer\". The position at the end is convention, not a decision anyone took. Pick a policy.",
     footer_before, footer_after, options=("A: full text everywhere", "B: documents full, chat one line", "C: full once per conversation"), before_label="Now, on a one-line answer", after_label="Options")

merges = [
    ("merge-scenarios", "Merge: scenarios into valuation",
     "Valuation already produces three cases with probabilities and an expected value; scenarios adds signposts and nothing else. One skill, one description.",
     f"**bigdata-valuation**\n\n{desc_of('valuation')}\n\n**bigdata-scenarios**\n\n{desc_of('scenarios')}",
     "**bigdata-valuation**\n\nWhat a company is worth: the growth, margin and return the price implies, a DCF with the equity bridge checked, three cases with probabilities and signposts, a multiples cross-check, a range. Use for fair value, DCF, is it cheap, what is priced in, scenarios, what if a driver changes. Not peers only: bigdata-comps.\n\n*bigdata-scenarios is removed; its signposts step joins the valuation checklist.*"),
    ("merge-catalysts", "Merge: catalysts into watchlist, earnings preview and quick take",
     "Catalysts is a dated-events list with expected impact. The watchlist already carries the next event per name, the earnings preview carries the setup, and the quick take carries the next catalyst for one name. The one thing lost is a standalone \"what is coming up for X\" list, which the watchlist description picks up.",
     f"**bigdata-watchlist**\n\n{desc_of('watchlist')}\n\n**bigdata-catalysts**\n\n{desc_of('catalysts')}",
     "**bigdata-watchlist**\n\nDaily or weekly check on a list of companies, or the dated events ahead for one: price move, the news behind it, earnings vs estimates, what is coming up and what it could move. Use for holdings, watchlist, peer or competitor set, what changed today, what is coming up, events to watch. Not one company's news: bigdata-company-brief.\n\n*bigdata-catalysts is removed; its \"what happens if nothing happens\" step joins the thesis checklist.*"),
    ("merge-macro", "Merge: macro-compare into country",
     "Macro-compare is the country skill with more than one country. The trigger suite confused the two until the descriptions were retuned, which is the sign of a boundary that should not exist.",
     f"**bigdata-country**\n\n{desc_of('country')}\n\n**bigdata-macro-compare**\n\n{desc_of('macro-compare')}",
     "**bigdata-country**\n\nOne country's economy and markets, or several compared on the same indicators: growth, inflation, rates, currency, fiscal and external balances, politics, what is priced in. Use for a country outlook, political risk, market entry, compare economies, which country is stronger, where to expand.\n\n*bigdata-macro-compare is removed; its comparison table joins the country checklist.*"),
]
for id, t, w, b, a in merges: item(id, t, w, b, a, options=("Merge", "Keep separate"), before_label="Now, two skills", after_label="Proposed, one skill")
item("thesis", "Keep or cut: thesis",
     "Thesis is the deep dive minus the economics plus \"where my view differs from consensus\". Portfolio managers ask for it; corporate readers never do. It stays unless you say otherwise.",
     f"**bigdata-thesis**\n\n{desc_of('thesis')}\n\n**bigdata-deep-dive**\n\n{desc_of('deep-dive')}",
     "Keep: thesis stays as a separate skill for the investor reader.\n\nCut: the variant-view and kill-criteria steps join the deep-dive checklist as investor-only items, and the thesis description's triggers (a thesis, variant view, bull and bear case, stress-test my idea) move to the deep-dive description.",
     options=("Keep", "Cut"), before_label="Now", after_label="The two options")

gm_assert_new = [
    "States the outlook change precisely: the EBIT-adjusted range narrowed from $14 to 16bn to $14.5 to 15.5bn with the midpoint unchanged, and corrects the prompt's \"lowered\" premise",
    "Answers what the quarter says about North American vehicle demand, with GMNA volumes, pricing and inventory figures and their sources",
    "Describes GM's cost plans and where a tier-1 supplier sits in them (warranty, EV, purchased material, the budget timing), with sources",
    "Gives programme timing a supplier can plan against (the full-size pickup changeover and other capacity moves), with dates",
    "Gives the planning team concrete takeaways by function (volume, commercial, footprint, finance), each tied to a fact in the note",
    "The supplier's questions are answered before any section an investor would want; nothing in the note serves only an investor",
    "Prior guidance is quoted from the earlier call with its date, next to the new range",
    "Every number in the opening agrees with the table it came from",
    "Citations sit next to the claims they support as links; five sampled citations point at documents that can plausibly hold the fact",
    "No n/a cells: a figure the data could not give is a line under Gaps, not a table cell",
]
item("evals", "Evals: assertions from the question, not the template",
     "Six of the current assertions mirror the output standard and the rest mirror the skill's sections, so a templated report scores 11 of 11 while a supplier cannot use it. Proposed: assertions written from each prompt (what the reader asked, what a wrong answer would look like), a pairwise judge given the reader persona and both reports, and a residue lint script that counts n/a cells, numbered citations, method-gap notes, investor-only terms in a corporate report and template section order. "
     "Regrade the 24 existing reports on this first, so there is a before number without new runs. Example: the GM prompt.",
     "**Current assertions for the GM prompt**\n\n" + md_list(gm_meta["assertions"]),
     "**Proposed assertions for the GM prompt**\n\n" + md_list(gm_assert_new) + "\n\n**Pairwise judge**\n\nA Sonnet judge is given the prompt, the reader persona (a tier-1 supplier's planning team) and both reports, and asked which one that reader would use and why, with the evidence named. Run both orders to cancel position bias.\n\n**Residue lint, run on every report**\n\n" + md_list([
         "n/a, dash and \"not found\" cells per table", "numbered citations", "method-gap notes (\"primer not found\", \"method notes\", \"(verify)\")",
         "investor-only terms in a corporate report (competitive advantage period, steady-state P/E, kill criteria, who must own it, position)",
         "section order equal to the skill's section list", "closing offers (save, monitor, build a skill)", "words, tokens, tool calls"]))

seq = [
    "Three decisions from you: the footer policy, the merges, and that the research provenance moves to docs rather than being deleted. (This page.)",
    "House style and the two exemplar bodies, by hand (the drafts on this page, revised with your comments). You read them before anything fans out.",
    "Three Opus agents re-cut the remaining bodies to the shape, from the existing bodies: every pitfall and data step survives, every step-number pointer and table template goes. I read each one.",
    "Library pass: provenance to docs, investor-only outputs marked, a Haiku check that no formula changed.",
    "Residue lint and the new assertions; regrade the 24 existing reports for the before number.",
    "Rerun the ten prompts with the re-cut skills, grade the same way, compare against both old arms.",
    "Trigger suite rerun (descriptions unchanged except the merges), packages, pages.",
]
item("sequence", "Sequence", "The order of work and the one gate that matters: nothing fans out to 23 skills before you have read the two exemplars. About one working day of my time and roughly $100 of agent and eval runs, most of it step 6.",
     "", md_list([f"{i+1}. {s}" for i, s in enumerate(seq)]).replace("- ", ""), options=("Go", "Change the order"), layout="one", after_label="Proposed")

item("general", "Anything else", "Anything the items above did not cover.", "", "", options=(), layout="none")

fonts = rd(f"{INPUTS}/fonts-platform.css")
logo = rd(f"{INPUTS}/logo.datauri").strip()
logo_dark = rd(f"{INPUTS}/logo-dark.datauri").strip() if os.path.exists(f"{INPUTS}/logo-dark.datauri") else logo
produced = time.strftime("%d %b %Y, %H:%M %Z")
data_json = json.dumps({"items": ITEMS}, ensure_ascii=True).replace("</", "<\\/")

rail_items = "".join(f'<li><a href="#{it["id"]}">{it["title"]}</a></li>' for it in ITEMS)
sections = "".join(f'''
<section id="{it["id"]}" data-rail="{it["title"]}" data-item="{it["id"]}">
  <h2>{it["title"]}</h2>
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
p.what { color: var(--fg-2); margin: 0 0 16px; max-width: 90ch; }

/* Before and after */
.cmp { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
.cmp.one { grid-template-columns: 1fr; }
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
  <p class="sub">Each proposed change to how the Bigdata.com skills are packaged, with the current text and the proposed text in full. Pick a decision and leave a comment on each; the answers are saved on this page and read back from it.</p>
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
    document.getElementById("what-" + it.id).textContent = it.what;
    var c = document.getElementById("cmp-" + it.id); c.textContent = "";
    if (it.layout === "two") { c.appendChild(pane(it.before_label, it.before, "before")); c.appendChild(pane(it.after_label, it.after, "after")); }
    else if (it.layout === "one") { c.appendChild(pane(it.after_label, it.after, "after")); }
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
