# Brief: Skills Eval Reader

**Reader**: Marko first, reading the full text of each eval run. May be forwarded to the Bigdata.com plugin and MCP teams, so no session context on the page.

**Questions the page answers**
1. What was the user prompt for each of the ten evals, and which skill and reader voice (PM or corporate) it tested?
2. What did the with-skill run produce, in full, rendered as a document?
3. What did the without-skill run produce, in full, readable next to the with-skill run?
4. How did each run score, assertion by assertion, with the grader's evidence, and where did the two arms differ?
5. What did each run cost: tokens, minutes, tool calls, words?
6. For the four skills rerun after the library fixes, how does the second run read against the first?
7. What did the agent do during the run (skill files read, tool calls, what it could not get)?

**Data** (`plugins/bigdata-com/evals/quality-2026-10-26/`)
- `evals.json` prompt, skill, voice, selected: shown for the ten selected; the ten unselected spare prompts in a fold at the end.
- `iteration-*/<eval>/eval_metadata.json` assertions: shown in the grades view.
- `report.md` (24 runs): shown, rendered.
- `run_log.md`: one click away (Run log tab in the pane).
- `grading.json` expectations with passed and evidence: shown (Grades tab, and the side-by-side grades table).
- `citation_grading.json` (4 iteration-1 with-skill runs) and iteration-2 `citation_sample`: shown under Grades as the citation sample.
- `timing.json` tokens, seconds, tool calls, words: shown in the pane header and the overview table.
- `benchmark.json` (both iterations): the overview table is computed from grading and timing directly; benchmark files dropped as derived.
- `agent_final_message.md`: dropped, it repeats the report with a harness preamble.

**Type**: investigation viewer (app-like reader).

**Existing page**: none for the eval outputs. The proposal page (https://claude.ai/artifact/CoETtAqbh3bWgotehF1bEU) holds the score tables; this page links to it and gets linked from it.

**Brand**: `bigdata-analytics:bigdata-design`, Platform system (same tokens, fonts and logo as the proposal page).

- References: promptfoo web UI eval grid (the prompt-by-variant matrix with pass marks, taken as the overview entry point); GitHub pull request split diff (two equal panes with sticky headers, taken as the reader layout); Braintrust experiment comparison (per-example scores under each output, taken as the grades list). Screenshots in the scratchpad eval-reader/refs folder.
- promptfoo web UI eval grid: the matrix of prompts by variants with pass marks in each cell, one click to the full output. Taken: the overview matrix as the entry point.
- GitHub pull request split diff: two equal panes with their own headers, reading left and right at the same scroll. Taken: the two-pane reader with sticky pane headers.
- Braintrust experiment comparison: per-example scores listed under each output. Taken: the assertion list with evidence under each report.

**Components**: kit (tokens, tooltip, fold, search), `marked` 12.0.2 from cdnjs for rendering the markdown reports.

**Spacing scale**: 4 px base; steps 4, 8, 12, 16, 24, 32, 48. Page gutter 20 px, section gap 48 px, title-to-content 12 px, row padding 6 px 10 px.

- Loaded: build-artifact (defaults.md, documents.md, publishing.md), artifact-design (via quickstart), visual-design (look.md, accessibility.md), bigdata-analytics:bigdata-design (platform/README.md, colors_and_type.css), marko-comms:writing-core (voice files, loaded earlier in the session).
