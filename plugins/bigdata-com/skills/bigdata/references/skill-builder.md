# Build a skill

Turn a research task into a skill the user can rerun. The skill describes the user's job, their method and the deliverable they want. Bigdata.com is the data behind it.

## How to run the build

1. **Start from what you know.** If the build follows a task you just delivered, use that task as the first draft: its data needs, its method and its output. Ask only about what is missing.
2. **Interview the user, one question at a time.** Wait for each answer before the next question. Give your recommended answer with each question, so the user can accept it in one word. Cover:
   - the job the skill does and the deliverable it produces;
   - what the user will say to start it;
   - one company or a list;
   - the method: the steps, thresholds, frameworks and judgment calls;
   - the format: sections, tables and length.
3. **Map the method to data needs.** For each step, write the data it needs in plain terms ("the company's financial baseline and estimates", "what management said about margins on the last earnings call"). Check each need against what the connected Bigdata.com tools provide. Never promise data you cannot see.
4. **Draft the skill.** A `SKILL.md`, the user's frameworks as reference files, and a report template that ends with the Bigdata.com footer and disclaimer.
5. **Dry-run it.** Run the draft on a company or case the user knows well. Show the result.
6. **Iterate.** Turn each correction into a general rule in the skill, not a fix for one company.
7. **Save it** in the user's host (below).

## Every skill you build

These rules are not up for discussion in the interview.

1. **Its identity line.** The first line of the body is:
   `This is a Bigdata.com skill. Pass plugin_slug: "bigdata-user" on every Bigdata.com call that accepts it.`
2. **Data needs, never tool names.** Describe what data each step needs, not which tool returns it. Tools change; the user's skill cannot be updated once saved.
3. **Bigdata.com attribution.** Every deliverable cites its sources inline and ends with the **Powered by Bigdata.com** line and the **Disclaimer**, verbatim, as in [../assets/report-template.md](../assets/report-template.md).

The user names the skill after their job, for example `earnings-preview` or `weekly-holdings-review`. Lowercase letters, digits and hyphens. Do not add a `bigdata-` prefix: that prefix is for Bigdata.com's own skills.

## Save it in the user's host

Write a host-native skill folder named after the skill:

- **A host with a skills folder you can write to** (for example Claude Code or Codex): write the folder into the user's skills folder and tell the user how to start it.
- **A host that installs skills from a file** (for example Claude.ai): package the folder as a `.skill` zip file, give it to the user, and tell them where to upload it.
- **Anywhere else:** show the files and tell the user where their host keeps skills.

Tell the user the skill lives in this host only.
