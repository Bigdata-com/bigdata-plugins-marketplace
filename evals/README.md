# Skill evals

Cases and a runner that test the bigdata-com skills in Claude Code headless (`claude -p`), with this branch's plugin loaded.

## Run

```bash
evals/run_evals.py                          # every case in cases/bigdata.json, once
evals/run_evals.py --case 03-clear-task     # one case
evals/run_evals.py --runs 3 --model sonnet  # three runs per case on Sonnet
```

It needs Claude Code signed in to a claude.ai account that has the Bigdata.com connector connected. Results go to `evals/results/<date>_<model>/`, which git ignores because the transcripts hold licensed Bigdata.com content:

- `summary.md`: one row per run, then each check with the judge's reason
- `summary.json`: the same, for scripts
- `<case>-run<n>.md`: the conversation, with tool calls
- `<case>-run<n>.events.jsonl`: Claude Code's raw event stream

A run of all six cases on Opus costs about $10 to $15.

## What a run does

1. **Loads the branch's plugin** with `--plugin-dir plugins/bigdata-com`.
2. **Switches off every other plugin,** including the synced or directory copy of bigdata-com (`bigdata-com@synced`). Claude Code only brings in the claude.ai connectors when it loads user settings, and user settings also load every installed plugin, so the runner reads the installed list once and passes `enabledPlugins: false` for each.
3. **Connector off:** cases with `"connector": "off"` load project settings only and set `ENABLE_CLAUDEAI_MCP_SERVERS=false`. Project settings alone are not enough: the claude.ai connectors still arrive after start-up. The plugin's own server is still there, unauthenticated, as it is for a user who has not signed in.
4. **Limits the tools** to the production Bigdata.com connector, Skill, Read, Glob, Grep and ToolSearch. Tools that change the Bigdata.com account (watchlist create, edit and delete, document upload, monitor create and delete) and the staging connector are blocked. Any other tool the model tries is denied and listed in the summary.
5. **Plays the user** in interview cases. Headless Claude Code has no question tool, so the skill asks in plain text. When a turn ends with a question and no Bigdata.com call, Haiku answers in character, using the case's `persona`, and the conversation resumes with `--resume`.
6. **Grades** each run twice:
   - counted checks: questions asked before the first result, Bigdata.com calls, whether the expected job skill was used, and no account-changing call
   - judge checks: Sonnet reads the transcript and grades each `judge` criterion

A run passes only if every check passes.

## What it does not cover

- Your global `CLAUDE.md` and personal skills still load, because they come with user settings.
- The host's question tool (the clickable options in claude.ai) does not exist in headless mode. Check it with a manual run on claude.ai.
- Questions are counted from the text: a turn counts as a question when it ends with a "?" and made no Bigdata.com call. The judge reads the same transcript as a second check.

## Add a case

Add an object to `cases/bigdata.json`:

| Field | Meaning |
|---|---|
| `id` | Short name, used for file names |
| `prompt` | The first user message |
| `connector` | `on` or `off` |
| `persona` | For interview cases: who the simulated user is and what they want. Leave it out for single-turn cases. |
| `max_user_turns` | How many simulated replies at most |
| `checks` | Counted checks: `max_questions`, `min_bigdata_calls`, `max_bigdata_calls`, `one_question_per_message`, `uses_skill` |
| `judge` | Criteria the judge grades, one sentence each, written so a transcript can show them true or false |
