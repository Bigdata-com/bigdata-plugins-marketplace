# Brief: Skills Re-cut Review

**Reader**: Marko, deciding item by item how the Bigdata.com skills get re-packaged. Possibly forwarded to the plugin team afterwards.

**Questions the page answers (actions the reader takes)**
1. For each proposed change, what does the current text look like and what would it become, in full?
2. Approve, approve with changes, or reject each one, and say why in a comment.
3. For the footer, which of three policies; for each merge, merge or keep; for the sequence, go or change.
4. Leave a general comment.
5. Have every answer saved so Claude can read it back without a copy-paste.

**Data**
- Current skill bodies (`plugins/bigdata-com/skills/bigdata-valuation/SKILL.md`, `bigdata-earnings-review/SKILL.md`): shown in full as the before.
- Re-cut drafts (`docs/proposals/2026-10-26-recut/valuation.recut.md`, `earnings-review.recut.md`): shown in full as the after.
- Current `library/output-standard.md` and the draft `house-style.md`: both in full.
- `library/methods/base-rates.md` formula 1 and its Sources section: the provenance before and after.
- `library/methods/expectations.md` output lines: the reader-gating before and after.
- The GM with-skill report's section list and the GM prompt: the write-step example.
- Current skill descriptions for the six merge candidates and the proposed merged descriptions.
- The GM eval assertions (`eval_metadata.json`) and the proposed question-fit assertions.
- Reading-budget numbers per skill (body words, library words read up front): shown in item 1.
- Answers: the page's own database, collection `reviews`, one document per item.

**Type**: review form.

**Existing page**: none. Related: Skills Eval Reader (https://claude.ai/artifact/HPgghcdyAaBcEM9x3JwDrg) and Job Skills Proposal (https://claude.ai/artifact/CoETtAqbh3bWgotehF1bEU); this page links to both.

**Brand**: `bigdata-analytics:bigdata-design`, Platform system (same tokens, fonts and logo as the eval reader).

- References: GitHub pull request review (file-by-file diff with a comment box and an approve / request changes decision; taken: one decision control per item, comments beside the text); Google Docs suggesting mode (the proposed text readable in place; taken: before and after rendered as documents, not as raw markdown); Linear issue triage (keyboard-driven accept or defer; taken: j and k to move, number keys to decide). The eval reader's two-pane layout is reused for before and after.

**Components**: kit (tooltip, rail, fold, search), `marked` 12.0.2 and DOMPurify 3.0.9 from cdnjs, `db` and `user` capabilities for the answers.

**Spacing scale**: 4 px base; steps 4, 8, 12, 16, 24, 32, 48. Page gutter 20 px, section gap 48 px, title-to-content 12 px, pane padding 16 px.

- Loaded: build-artifact (defaults.md, documents.md, publishing.md), artifact-design (via quickstart, earlier this session), visual-design (look.md, accessibility.md), bigdata-analytics:bigdata-design (platform/README.md, colors_and_type.css), artifact-capabilities (db.d.ts, claude.d.ts), marko-comms:writing-core (voice files).
