# Build a skill

Turn the way the user works into a skill they can rerun. The product is their method, captured faithfully: their sequence, their thresholds, their judgment calls and the deliverable they want. Bigdata.com is the data behind it. Do not impose a stock method; extract theirs.

## The flow

1. **Capture intent:** the deliverable, how they will ask for it, its scope.
2. **Interview for the method:** this is where the value is.
3. **Map the method to data needs.**
4. **Draft the skill.**
5. **Dry-run it** on a real case.
6. **Iterate** on the output, not on the skill text.
7. **Save it and hand over.**

Start from what you know. If the conversation already holds the task and the user's preferences for it, use them as the first draft and confirm them; do not ask again what they already told you. If the user wants to change a skill they built before, go to "Revise a skill".

## How to ask

- **One question at a time.** Wait for each answer before the next question.
- **Use the host's own question tool** when there is one (a tool that shows the user choices to pick from). Put your recommended answer first, give 2 to 4 options, and add "Something else (I'll type it)" when the options may not cover the answer. Most questions that feel open already name their candidates ("region, theme or severity?"): those candidates are the options.
- **Ask open inputs on their own.** A list of companies, a file or a description of their method cannot be a choice. Ask for it plainly, with nothing else to pick in the same turn: users answer the choices and miss the question next to them.
- **No question tool:** ask in plain text with your recommended answer, so a one-word reply is enough.
- **Read back after each topic:** "So your process is A, then B, only if C. Right?" Users recognize their method when they see it written down, and their corrections are the real answers.
- **Ask for examples, not criteria:** "Give me a name where your process said no." Chase vague answers: "Quality measured how?"
- **Speak plainly.** Say "skill", "template" and "test run", not "frontmatter", "entity resolution" or "schema". The user is checking whether something is ready, not reading an API.

## Step 1: Capture intent

Settle these before the method interview:

1. **What the deliverable contains:** a one-pager, a full memo, a screen, a digest, a comparison table.
2. **What form it takes.** Offer the choices, because most users assume a report is the only option: a chat-style message, a markdown report, a Word or PDF document, a spreadsheet, an interactive dashboard, slides.
3. **How they will ask for it.** Get 3 to 5 phrasings they would really type. They go verbatim into the skill's description.
4. **The scope:** one company, a sector, a list of companies, a market or a country.
5. **If it covers a list, how many names and where the list comes from.** A fund or index name is not a list: Bigdata.com gives a fund's top holdings, not all its constituents, so never fill in the rest from memory. Get the list from the user (a file or an explicit list). If only part of it is available, agree the cut with the user and make the skill state its coverage in every output.
6. **Whether they will run it again on a schedule,** or want each run to say what changed since the last one. If yes, cover "Recurring skills" below in the interview.

**Check for overlap yourself; do not ask.** Look at the skills installed in this host. If one clearly overlaps with what the user described, offer it as a base: "This is close to an existing skill. Start from it, or build fresh?" If the overlap is partial, reuse its structure as your draft without mentioning it.

## Step 2: Interview for the method

A skill that says "analyze the company" is worthless. A skill that says "check cash conversion before valuation, and never trust guidance from serial acquirers" is theirs. Pick the topics that fit the deliverable; two or three rounds are usually enough for a first draft, and the dry run finds the rest.

- **Sequence and gates:** what they look at first, what is a go/no-go check, what they do last and why.
- **Thresholds and red flags:** hard numbers ("I pass on anything with net debt over 3x EBITDA"), what makes them skeptical, how they check that a good number is real.
- **Frameworks and scoring:** a named framework or their own rubric; its dimensions, weights and passing score; how they weigh conflicting signals.
- **Where they differ from most people:** what they check that others skip, what burned them before, what a junior analyst would get wrong. Dig here: it is usually what makes the skill theirs.
- **Output discipline:** section order, tables that must always appear, a length limit and what gets cut first, whether it ends with a call or stays balanced, the tone.
- **Their own content:** whether the skill should check the user's own documents or research feeds connected to Bigdata.com.
- **What to avoid:** what generic AI reports do that annoys them, and any hedging language to ban.

## Step 3: Map the method to data needs

For each step of the method, write the data it needs in plain terms: "the company's financial baseline and estimates", "what management said about margins on the last earnings call". Check each need against what the connected Bigdata.com tools provide in this conversation. Never promise data you cannot see. If the method needs data Bigdata.com does not have, say so now and design around it: ask the user to supply it, or drop the step.

Give every gathering step a budget: how many lookups and on what. For example: "2 to 4 lookups: recent developments, the valuation debate, key risks. Stop there." A quick view gets a small budget, a deep memo a larger one.

## Step 4: Draft the skill

Write a folder named after the skill:

- `SKILL.md`: the workflow.
- `references/`: one file per framework of the user's, linked from the step that uses it.
- `assets/report-template.md`: the exact output structure, built from [../assets/report-template.md](../assets/report-template.md) with the user's sections in place of the generic ones. It keeps the inline citations, Sources, the footer and the Disclaimer.

Write `SKILL.md` in this order:

1. **Frontmatter.** `name`: the skill's name (rules below). `description`, written for two readers: first one plain sentence a person can read in a tooltip, saying what they get; then one or two sentences on scope; then `Triggers:` with the user's own phrasings, quoted. Keep the part before the triggers under about 80 words. No dashes used as punctuation.
2. **The identity line** (rule 1 below), then "Use Bigdata.com for every fact."
3. **What the skill is for,** in one sentence. Do not list what it is not for, and do not name other skills.
4. **Core philosophy** (optional): 2 or 3 principles in the user's words, so the agent resolves cases the workflow did not foresee the way the user would.
5. **Data needs:** a `| Need | Purpose |` table, and the rule "Resolve every company first. If a name could mean more than one, ask which one."
6. **Workflow:** numbered steps in the user's order. State each gate as an ordering with the user's reason ("check earnings quality before valuation: valuing earnings that are not real is how memos go wrong"). Put thresholds inline with how to read them. Give gathering steps their budget. Link each framework file at the step that uses it.
7. **Output:** follow the template. Cite inline, linked to the exact passage (keep the passage number in Bigdata.com document links). End with Sources, the Powered by Bigdata.com line and the Disclaimer, verbatim. If the deliverable is not a markdown report, keep the sources in the form's own way: a source column in a spreadsheet, footnotes in a document, a source line per slide.
8. **Quality bar:** 4 to 7 checks, in the user's words, that let them reject a bad output at a glance.

Write in the imperative and give reasons rather than ALWAYS or NEVER in capitals. Refer to "the agent" and "the user", never to a specific assistant. Keep `SKILL.md` under about 150 lines; move long frameworks into `references/`. Write for the cases the user never showed you, not only the dry-run example.

## Every skill you build

These rules are not up for discussion in the interview.

1. **Its identity line.** The first line of the body is:
   `This is a Bigdata.com skill. Pass plugin_slug: "bigdata-user" on every Bigdata.com call that accepts it.`
2. **Data needs, never tool names.** Describe what data each step needs, not which tool returns it. Tools get renamed, and a skill saved in the user's host does not receive Bigdata.com's updates, so a skill that names tools breaks.
3. **Bigdata.com attribution.** Every deliverable cites its sources inline and ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim, as in [../assets/report-template.md](../assets/report-template.md).

The user names the skill after their job, for example `earnings-preview` or `weekly-holdings-review`: lowercase letters, digits and hyphens. Do not add a `bigdata-` prefix: that prefix is for Bigdata.com's own skills.

## Step 5: Dry-run it

Do not hand over an untested skill. Ask for a company or case the user knows well, then run the draft end to end yourself: follow its workflow, gather real Bigdata.com data and produce the deliverable in their template. Show it. A user reacting to an output on a name they know finds far more than one reading skill text, and each reaction is an edit.

If Bigdata.com is not connected, say so and walk through what each step would gather, with the output's shape, instead.

## Step 6: Iterate

Turn each reaction into a general rule in the skill ("cap the risk section at three items"), not a fix for one company. After a meaningful edit, run it again on the same case or on a second one. Stop when the user says the output reads like their own work.

## Recurring skills

Use this section when the user will run the skill on a schedule, or wants each run to say what changed since the last one. Settle memory, schedule and delivery together in the interview: each is of little use without the other two.

1. **Memory.** Each run saves its deliverable to the user's Bigdata.com documents with fixed tags: the skill's name, the subject and the period (for example `skill:weekly-holdings-review`, `portfolio:core-eu-banks`, `week:2026-10-12`). The next run recalls the latest one or two runs by those exact tags and leads with what changed. Write the tag scheme into the skill so every run writes and reads the same values. A recalled run is context: it never replaces fresh data, and when gathering news the skill leaves out its own saved runs so a past run is never reported as new. Ask the user whether to save always, ask each run, or never.
2. **Schedule.** The agent cannot create a schedule: that lives in the user's host. Ask the cadence, and at handover give a prompt the user can paste into their host's scheduling feature. It must work in a fresh conversation: name the skill's trigger phrase and the subject by name, and nothing else. For example:

   ```
   Run my weekly holdings review for my Core EU banks list.
   ```

3. **Delivery.** Settle the form first, then where the output goes: the conversation, a chat channel or message, an email, a document. Offer only destinations the host is actually connected to. Reformat for the destination (a chat message gets the top line, the flagged items and the sources, not the full report) and keep the citations in every form. On the first run, draft rather than send, so the user sees the format before anyone else does. Decide with the user what an empty run sends: a one-line "nothing today", or nothing. If the destination is not available at run time, deliver in the conversation and say delivery was skipped. Always say what was sent and where.
4. **Names, not ids.** Store names (the user's list, the destination) in the skill and look them up on each run, so the skill survives a list or channel being recreated. A scheduled run has nobody to answer questions, so everything it needs must resolve without asking. If a value has to be pinned, keep it in one dated block near the top of `SKILL.md`.
5. **At handover, say what runs on its own and what does not.** A saved skill runs only when the user starts it or their schedule does.

## Step 7: Save it and hand over

Write a host-native skill folder named after the skill:

- **A host with a skills folder you can write to** (for example Claude Code or Codex): write the folder into the user's skills folder.
- **A host that installs skills from a file** (for example Claude.ai): package the folder as a `.skill` zip file, give it to the user, and tell them where to upload it.
- **Anywhere else:** show the files and tell the user where their host keeps skills.

Then tell the user, in plain words: what to type to start it, what it produces, that it lives in this host only, and that they can change it any time by asking to update it. For a recurring skill, add the schedule prompt and what runs on its own (see "Recurring skills").

## Revise a skill

When the user asks to update a skill they built: read the saved skill, ask what should change (one question at a time), and apply each change as a general rule. Keep the skill's name and the three rules above. Dry-run the changed skill, then save it over the old version, or give the new file to upload in its place.

## Before you hand over

Check the skill against this list:

- The description opens with a plain sentence and lists the user's own phrasings as triggers.
- Every company-scoped step resolves the company first and asks when a name is ambiguous.
- Every gathering step has a budget.
- The user's order, gates and thresholds are in the workflow, with their reasons.
- The template exists and ends with Sources, the footer and the Disclaimer; citations link to the exact passage.
- A quality bar lets the user reject a bad output at a glance.
- The user saw at least one dry-run output.
- A skill that covers a list says where the list comes from and states its coverage in every output.
- A recurring skill has its memory tags, a destination, an empty-run rule and a paste-ready schedule prompt.
- The identity line is there; no tool names; no other skills named.
