# Packaging rules for skills and the library, 28 October 2026

Decided by Marko on 28 October after the earnings-preview with-skill report lost a blind comparison to the no-skill report. The with-skill report carried "expectations formula 1", "software primer, backlog duration", a paragraph citing the Base Rate Book and Mauboussin's drift tables, and thirty basis labels. Ten of fifteen with-skill reports named a library file, formula, primer or source book; none of the ten no-skill reports did.

## The standard

The reader wants a high-quality, actionable write-up about the company and the question. Everything that exists to produce the write-up stays out of it. The note reads as the work of an analyst who knows the method.

## Three layers

**Provenance, for the maintainer, never shipped.** Source, edition, page, exhibit, what the sources do not cover, verification status. Lives in `docs/proposals/2026-10-23-job-skills/method-specs/`. The plugin build does not copy it.

**The library, the agent's working knowledge, shipped.** Written as a firm's internal manual:
- No author, paper, book, bank, research house or page is named anywhere.
- Formulas are named by what they compute, never numbered. Tables are named by their content, never numbered.
- A historical figure carries only population and period ("companies with more than $50 billion of sales, 1950 to 2015").
- Techniques, not procedures: what a technique answers, when it applies, the inputs, the arithmetic, the trap. No "Procedure", no "When a skill loads this file", no "Done when". The skill body owns the order of work.
- Limits are conditions on observable facts ("for a cyclical, normalise profit to mid-cycle before solving"), never notes to the author ("not in the sources", "verify").
- No dated worked examples from the sources.

**The output rules, what the reader sees.** `library/output-standard.md`. Facts carry a linked source and date. An assumption a conclusion rests on is stated once, in plain words, where it matters. Nothing else is labelled. Methods, formulas, historical statistics and the skill's files are never cited or named.

## Tables (added after round 6)

With-skill reports averaged 7.3 columns at the widest table and 113 characters of header row against 5.8 and 85 without the skill, because the output standard pushed unit, period and assumptions into headings, the library's dense reference tables were imitated, bodies asked for comparisons on identical rows, and the "inputs once" rule was met with columns. The output standard now carries a table recipe: at most four columns (five of short numbers), headings of one to three words, qualifiers in one line under the table, one measure per cell, narrative cells for case comparisons.

## Rules retired

From the 23 October proposal: rule 5 (basis words and the Basis column), rule 7 (a base rate labelled with sample and period next to every growth claim), rule 11's "(verify)" convention. Audience framing (portfolio manager against corporate reader) is not a design axis: one note, one bar; readers skip what they do not need.

## Skill bodies

- Directions with their reasons, not artefacts to produce. A method step applies under a stated condition, and the user's parts come first, in the user's order, each with the same depth. A body never names the columns of a table and never produces a classification word; a judgment is a sentence with its evidence. (Added after round 6: bodies that mandated pieces lost two corporate-voice comparisons by filling forms and thinning the reader's own question.)
- Method files are pointed to by the question they answer, never by formula or table number.
- No anecdotes from eval runs. A recorded failure is one line stating the condition and the rule.
- "Not available" means no structured field. Documents often carry the figure; search before stating a gap.

## Evals

A blind pairwise judge (which note would an expert rather have, and why), three runs per arm, a leak check that fails any report naming a library file, formula, table, primer, source book or author, words against the baseline, tokens at most 1.5 times the no-skill run. Output wording is micro-tested (five single-shot reps against a no-guidance control) before a full run.

## Result on the pattern skill, 28 October

Micro-test of the output rules (Sonnet, five single-shot reps per arm, same working notes): old rules 13 to 18 basis labels per 440-word section and method names in 2 of 5; new rules 0 and 0 in 5 of 5. Full rerun of earnings-preview (Opus, three with-skill runs against a fresh no-skill run, blind Sonnet judges): with-skill won 3 of 3 with no library or source name in any note. Details in `plugins/bigdata-com/evals/quality-2026-10-26/iteration-4/earnings-preview-pm-amazon/RESULTS.md`.

The Skills Eval Reader with rounds 4 and 5 added: https://claude.ai/artifact/HPgghcdyAaBcEM9x3JwDrg (updated in place on 28 October).

Published 28 Oct to the original RavenPack artifacts: Job Skills Proposal https://claude.ai/artifact/CoETtAqbh3bWgotehF1bEU (UUID 5f89092d-5cb6-42dc-ada6-b5930a4c2075) and Skills Eval Reader https://claude.ai/artifact/HPgghcdyAaBcEM9x3JwDrg (UUID 84bd09b6-0998-467a-a1a8-7a2ea8a35471).
