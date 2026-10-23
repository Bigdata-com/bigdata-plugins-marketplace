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
  - Four SKILL.md drafts: one click away (fold each, rendered as a document, not raw markdown).
  - Sources: fold at the end.
  - Dropped: the session's working notes, the tool-result paths, the agent fan-out details (reply only).
- Type: plan / proposal.
- Existing page: none for this proposal. The onboarding plan page (https://claude.ai/artifact/HNEgzgUaizVqYBi6TZBFUo) is a different document and is linked from the summary.
- Brand: bigdata-analytics:bigdata-design (tokens, fonts, logo image in the rail).
- References:
  1. Stripe docs page (docs.stripe.com): the fixed contents rail with the current section marked, and the 65-character measure for prose.
  2. GitHub rendered RFC / design doc: tables that fit the column, headings as short labels, code blocks for file layouts.
  3. Linear's changelog page: density of a long document, section spacing, one accent.
- Components: the kit (tokens replaced by brand tokens, rail, fold, tooltip, table, search).
- Spacing scale: base 4 px; steps 4, 8, 12, 16, 24, 32, 48; page gutter 24 px desktop, 16 px phone; section gap 48; title-to-content 12; row padding 6 x 10.
- Loaded: artifact-design, visual-design (look.md, accessibility.md), bigdata-analytics:bigdata-design (Platform system: platform/README.md, platform/colors_and_type.css, fonts embedded, logo file), build-artifact references/defaults.md, references/documents.md, references/publishing.md, marko-comms:writing-core (lint run on the markdown source)
