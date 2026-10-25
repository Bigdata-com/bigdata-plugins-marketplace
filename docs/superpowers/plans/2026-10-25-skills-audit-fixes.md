# Skills audit fixes: implementation plan and session state

> For agentic workers: this file is the single source of truth for the 2026-10-25 fix session. If context is compacted, re-read this file first, then re-load every skill in "Skills loaded" with the Skill tool, then continue from "Progress".

**Goal:** Fix the 26 Bigdata.com plugin skills on branch `skills-audit-fixes-2026-10-25` (worktree `.claude/worktrees/skills-audit-fixes`, branched from `skills-proposal-2026-10-23` at 9ac002e) so they trigger reliably on all hosts and would pass a senior PM and a Fortune 500 IR head on first read. Marko compares the branches later. Nothing is pushed or merged.

**Spec:** Marko's messages in this session (summarised under "Directions") plus the audit findings under "Findings".

## Skills loaded in this session (re-load all after compaction)

skill-craft, skill-creator:skill-creator, plugin-dev:skill-development, marko-comms:writing-core, marko-comms:comms-voice, superpowers:writing-plans. Also read: the voice files under `~/claude-plugins/marko-comms/skills/*/references/` (marko-voice.md, chat-and-text.md, documents.md, sent-messages.md, lexicon.md).

## Directions from Marko (verbatim where it matters)

1. Verify the sector-primers.md length against skill-craft, skill-creator and plugin-dev rules; then audit the whole plugin structure.
2. "Stop telling me what's right and tell me what's wrong." Reply in his own voice (writing-core, comms-voice): lowercase, short, en dashes, no filler, no metaphors, no emojis.
3. The skills are guidelines that "jog memory" on financial concepts to produce an enterprise-level outcome. Audience: financial professionals and prosumers, but must generalise to corporates doing competitive analysis, IR research, due diligence.
4. `~/Downloads/investing-resources` holds the high-quality literature. Reviewers (opus/sonnet) must not opine on finance without it. "You are fable... don't rely on everything they said as god's written rule. Use your expertise and best judgment."
5. Frontmatter matters most: he worries "from Bigdata.com news..." in descriptions makes skills fire only when the user names Bigdata. Research modern skill design.
6. If findings "2. broken" and "3. not senior-PM level" are accurate, fix ASAP. "We can't allow to release something that's embarrassing."
7. Implement all the changes in a new branch for later comparison. He is away. Log every decision he might have wanted to be asked about in `docs/superpowers/plans/2026-10-25-decisions.md`; review at the end.
8. On compaction: re-load ALL loaded skills and note all directions and back and forth.
9. Global rules (CLAUDE.md): no emojis; every Agent call passes an explicit model (opus for implementation at high effort, sonnet for research, haiku for verification); never launch Fable subagents; fan-out over 3 agents uses sonnet/haiku unless approved; never claim done without verifying; after two failed fixes, re-diagnose; never modify what he did not ask about.

## Findings carried into this plan (verified by me unless marked)

Listing budget: Claude Code caps the skill listing at 1 percent of the context window (about 8,000 chars on 200k) and drops descriptions least-used first; Codex caps at 2 percent or 8,000 chars and shortens then omits. Plugin listing is 12,852 chars (26 descriptions 385-522 chars each). Target: each description at or under 240 chars, task-first, product out of the first clause, corporate trigger words in, boundaries between thesis/scenarios/risk and moat/sector and screen/comps.

Library formula defects (verified in files): expectations.md:39 divides excess cash by cost of capital and :41 adds it again; valuation.md:28 labels gross capex as net capex; earnings-quality.md:46 subtracts SBC from net income which already deducts it; roic.md:124 forbids ROIIC vs WACC while expectations.md:67-73 and formula 1 use it. Four method files carry garbled section names from the rename script ("`financial_statements, financial_ratios, key_metrics` key metrics", "`fund_trends_history`, `fund_trends_history`"). Every copied reference cites files not shipped in that skill (research notes like mckinsey-part1.md, and library files the skill does not list). skills/bigdata/references/skill-builder.md cites assets/report-template.md which does not exist.

Tool reality (verified against live MCP schemas): company tearsheet analyst_estimates = forward projections only, no revision history; latest_earnings = one quarter; statements = five periods, interval quarter (default) or annual, no offset; sentiment tearsheet takes only rp_entity_id and asks to be presented verbatim; bigdata_get_credit_factor and bigdata_screen_credit_factor return news-based credit catalysts, no prices or ratios; events calendar corporate = earnings, conferences, IPOs, delistings only; fund_trends_history carries options activity (working-with-bigdata.md:106 says options are not available, contradiction); the tearsheet tool text says not to pass `sections` for general pulls while every skill always passes it.

Eight skills ask for five fiscal years and never set interval annual: comps, credit, earnings-review, earnings-preview, risk, sector, screen, theme. Seven ask for 30-day consensus change or before/after targets with no fallback (company-brief, stock-move, watchlist, catalysts, quick-take, earnings-preview, earnings-review has a search fallback). Two ask for eight quarters of surprises; deep-dive and moat ask for ten years.

Finance quality (reviewer claims, to be checked against the literature by me before editing): credit maps ratings on 2011-13 EBIT/interest and debt/capital medians, no debt/EBITDA or FFO/debt, no refinancing-rate shock, no structural subordination step; stock-move scores valuation after the move (after-a-price-move.md:28 says before) and its sub-10 percent rules contradict (lines 48, 52, 94); merger arb p* without carry, time, hedge for stock deals; screen ranks on gross profitability, ROIC, margin regardless of ask; country has no macro method; nominal vs real not separated in country and macro-compare; dated comparators printed as live (McKinsey 5th ed, S&P 1981-2003 defaults, HOLT 2016, 2014 comp survey); "(verify)" printed in deliverables; 9-12 column tables; "What would change this view" in no-view reports; software primer CAC payback unit error and pre-OBBBA R&D line; banks primer lacks LCR, uninsured deposits, CRE concentration.

Corporate reader: output-standard.md:3 defines the reader as a PM or analyst; sector, theme, deal-analysis, screen have no slot for the user's own company; deep-dive refuses private companies while thesis routes them there; risk assumes a long holder; entry skill interview has no competitor/IR/diligence goal.

Skill craft: five bodies restate 10-19 percent of their references (earnings-quality, capital-allocation, valuation, comps, moat); the "Before starting" bullet states the same prohibition three ways; primer bundle is 33k tokens for one 2.7k section, flat H2 headings, slugs in the contents list that match nothing, no grep hint; stock-move ships the primer and never points at it.

Trigger suite: 156 cases, 154 pass, 0 corporate-voice prompts, only this plugin installed, `/bigdata` case failed, macro-compare fires-2 flaky.

## Tasks

- [ ] T1 Setup: worktree, this plan, decisions log, memory file.
- [ ] T2 Literature check (Fable, main session): each finance claim above against the extracted texts in the scratchpad `lit/` folder (copied from the 23 Oct session) and the PDFs in `~/Downloads/investing-resources`. Record the verdict per claim in decisions.md.
- [ ] T3 Library fixes (Fable): formulas, ROIIC rule, garbled names, citation policy, working-with-bigdata.md corrections (options, sections, revisions fallback, annual interval, sentiment, credit-factor, calendar), output-standard.md (reader, verify tag, view section, table width).
- [ ] T4 Descriptions (Fable): rewrite all 26 to the target above; keep names.
- [ ] T5 Credit, stock-move, special-situations (Fable): method files and SKILL.md bodies.
- [ ] T6 Per-skill pass by 3 opus agents (high effort), groups A/B/C minus the three in T5, with a fixed checklist (see decisions.md for the checklist text).
- [ ] T7 Primer: fix headings (H2 sector, H3 subsections, slug anchors), add navigation line to every SKILL.md that loads it, add the pointer in stock-move. Keep the single bundle (decision logged).
- [ ] T8 Sync and validate: sync_library.py, check_skills.py, build scripts, file counts (Cowork 20 companions), listing chars.
- [ ] T9 Trigger evals: add corporate-voice prompts, run `claude plugin eval`, fix descriptions that fail, rerun.
- [ ] T10 Summary for Marko: what changed, decisions, eval results, what is left.

## Progress

(updated as tasks complete)
