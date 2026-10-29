# Brief: Job Skills Proposal page

- Reader: Marko first, for review and decisions. Then the Bigdata.com product and MCP team, and the person who builds the skills. May be forwarded to the CEO. Readers know Bigdata.com and the current plugin; they have not seen the research sessions.
- Questions:
  1. What is being proposed: which skills, how many, grouped how?
  2. Why these: what evidence (usage counts, search topics) supports each job?
  3. What does each skill do, when does it fire, and what does it not do?
  4. Which methods back the skills, where do they come from, and what does each method file contain?
  5. How does one skill folder ship to Claude, ChatGPT and Microsoft, and which host limits shape the design?
  6. How are the skills evaluated before release and narrowed after?
  7. Which decisions are Marko's, and what is the recommendation on each?
  8. What does a finished skill look like (four complete drafts)?
  9. Where did the 26 October plan fall short of the 23 October goals, what changes, what did Marko answer on the review page, and in what order does the work finish? (added 27 October)
- Data:
  - Mixpanel skill runs by skill, 10 Sep to 13 Oct 2026: shown (table in section 2).
  - Topic-model shares and empty-result rates, 22 Sep to 22 Oct: shown (same table).
  - The 26 skills with group, job, rationale: shown (sortable table; row click opens the full description).
  - Each skill's description text and character count: one click away (row detail).
  - The 14 method files with contents and loading skills: shown (table); each file's full spec: one click away (fold per file).
  - 11 sector primers: shown (list).
  - Host limits for Claude, ChatGPT, Microsoft: shown (three tables).
  - Build and check steps: shown.
  - Eval layers, the six-prompt pattern, the fixtures, the rubric examples, costs: shown.
  - Migration map old to new: shown (table).
  - Decisions for Marko: shown at the top, after the summary.
  - Finish plan (27 October): the four gaps as a table, the four changes, the valuation body in three versions (today, 26 October re-cut, 27 October guideline shape) as folds with word counts, the review-page answers as a table, the order of work with cost.
  - Four SKILL.md drafts: one click away (fold each, rendered as a document, not raw markdown).
  - Sources: fold at the end.
  - Dropped: the session's working notes, the tool-result paths, the agent fan-out details (reply only).
- Type: plan / proposal, with a file browser for the plugin (tree on the left, the selected file rendered on the right) so the 287 files can be reviewed one by one.
- Existing page: none for this proposal. The onboarding plan page (https://claude.ai/artifact/HNEgzgUaizVqYBi6TZBFUo) is a different document and is linked from the summary.
- Brand: bigdata-analytics:bigdata-design (tokens, fonts, logo image in the rail).
- References:
  1. Stripe docs page (docs.stripe.com): the fixed contents rail with the current section marked, and the 65-character measure for prose.
  2. GitHub rendered RFC / design doc: tables that fit the column, headings as short labels, code blocks for file layouts.
  3. Linear's changelog page: density of a long document, section spacing, one accent.
  4. GitHub's repository file browser and the VS Code explorer: a tree with folders collapsed by default, the file name as the click target, the open file's path shown above its content.
- Components: the kit (tokens replaced by brand tokens, rail, fold, tooltip, table, search).
- Spacing scale: base 4 px; steps 4, 8, 12, 16, 24, 32, 48; page gutter 24 px desktop, 16 px phone; section gap 48; title-to-content 12; row padding 6 x 10.
- Loaded: artifact-design, visual-design (look.md, accessibility.md), bigdata-analytics:bigdata-design (Platform system: platform/README.md, platform/colors_and_type.css, fonts embedded, logo file), build-artifact references/defaults.md, references/documents.md, references/publishing.md, marko-comms:writing-core (lint run on the markdown source). 27 October update: artifact-design, build-artifact (defaults.md, documents.md, publishing.md), marko-comms:writing-core (marko-voice, public-voice, lexicon, structural-patterns, self-check; lint on the addendum), skill-craft, skill-creator, plugin-dev skill-development and plugin-structure (for the body shape); bigdata-design not reloaded, the brand tokens come from the existing generator.
