#!/usr/bin/env python3
"""Run the bigdata-com skill evals in Claude Code headless.

Each case sends a prompt to `claude -p` with this branch's plugin loaded through
--plugin-dir and the synced or directory copy switched off. Interview cases go on
for several turns: a small model plays the user and answers each question. A
judge model then grades the transcript against the case's criteria, and the
runner adds checks it can count itself (questions asked, Bigdata.com calls,
skills used).

Usage:
    evals/run_evals.py                       # every case, once
    evals/run_evals.py --case 03-clear-task  # one case
    evals/run_evals.py --runs 3 --model sonnet

See evals/README.md for what the setup switches off and why.
"""

import argparse
import concurrent.futures
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN_DIR = REPO / "plugins" / "bigdata-com"
RESULTS_DIR = Path(__file__).resolve().parent / "results"

# The production Bigdata.com connector, as claude.ai names it in Claude Code.
CONNECTOR = "mcp__claude_ai_Bigdata_com"
CONNECTOR_PREFIX = CONNECTOR + "__"
# Tools that change the user's Bigdata.com account. Evals must never call them.
ACCOUNT_CHANGING = [
    "bigdata_create_watchlist",
    "bigdata_edit_watchlist",
    "bigdata_delete_watchlist",
    "bigdata_upload_document",
    "bigdata_configure_monitor",
    "bigdata_delete_monitors",
]
OTHER_BIGDATA_SERVERS = ["mcp__claude_ai_Bigdata_com_-_STG"]
# Project settings alone still load the claude.ai connectors after start-up;
# this variable is what keeps them out.
CONNECTOR_OFF_ENV = {"ENABLE_CLAUDEAI_MCP_SERVERS": "false"}
ALLOWED = [CONNECTOR, "Skill", "Read", "Glob", "Grep", "ToolSearch"]
DISALLOWED = [CONNECTOR_PREFIX + t for t in ACCOUNT_CHANGING] + OTHER_BIGDATA_SERVERS


def claude(args, cwd, timeout=1800, env=None):
    proc = subprocess.run(
        ["claude", *args], cwd=cwd, capture_output=True, text=True, timeout=timeout,
        env={**os.environ, **(env or {})},
    )
    return proc.stdout, proc.stderr


def other_plugins_off():
    """Settings that switch off every installed plugin except this branch's.

    Loading user settings is what brings in the claude.ai connectors, and it
    also loads every plugin the user has installed. Read the list once from an
    init message and disable all of them, including bigdata-com@synced.
    """
    with tempfile.TemporaryDirectory(prefix="bigdata-eval-probe-") as cwd:
        out, _ = claude(
            ["-p", "ok", "--model", "haiku", "--max-turns", "1",
             "--output-format", "stream-json", "--verbose"],
            cwd,
        )
    for line in out.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "system" and event.get("subtype") == "init":
            sources = [p["source"] for p in event.get("plugins", [])]
            off = {s: False for s in sources
                   if not s.endswith("@builtin") and not s.endswith("@inline")}
            off["bigdata-com@synced"] = False
            return {"enabledPlugins": off}
    sys.exit("Could not read the installed plugins from Claude Code's init message.")


def subject_args(prompt, model, connector, settings, session_id=None):
    args = ["-p", prompt, "--model", model, "--output-format", "stream-json",
            "--verbose", "--max-turns", "40", "--plugin-dir", str(PLUGIN_DIR)]
    if session_id:
        args += ["--resume", session_id]
    if connector == "on":
        args += ["--settings", json.dumps(settings)]
    else:
        # No user plugins, and (with CONNECTOR_OFF_ENV) no claude.ai connectors.
        # The plugin's own server loads unauthenticated, as it does for a user
        # who has not signed in.
        args += ["--setting-sources", "project,local"]
    args += ["--allowedTools", *ALLOWED, "--disallowedTools", *DISALLOWED]
    return args


def parse_turn(stdout):
    turn = {"events": [], "texts": [], "tool_uses": [], "final_text": "",
            "cost_usd": 0.0, "session_id": None, "denials": [], "stop": None,
            "skill_loaded": False}
    after_last_tool = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        turn["events"].append(event)
        kind = event.get("type")
        if kind == "assistant":
            for block in event["message"]["content"]:
                if block["type"] == "text":
                    turn["texts"].append(block["text"])
                    after_last_tool.append(block["text"])
                elif block["type"] == "tool_use":
                    turn["tool_uses"].append({"name": block["name"], "input": block["input"]})
                    after_last_tool = []
        elif kind == "user":
            content = event["message"]["content"]
            blocks = [content] if isinstance(content, str) else content
            for block in blocks:
                text = block if isinstance(block, str) else block.get("text", "")
                if re.search(r"Base directory for this skill: \S*/skills/bigdata(?![\w-])", text):
                    turn["skill_loaded"] = True
        elif kind == "result":
            turn["cost_usd"] = event.get("total_cost_usd") or 0.0
            turn["session_id"] = event.get("session_id")
            turn["denials"] = event.get("permission_denials") or []
            turn["stop"] = event.get("subtype")
    turn["final_text"] = "\n\n".join(after_last_tool).strip()
    return turn


def bigdata_calls(turn):
    return [t for t in turn["tool_uses"] if t["name"].startswith(CONNECTOR_PREFIX)]


def question_sentences(text):
    """Questions in a message, leaving out list items (options offered to pick from)."""
    prose = "\n".join(
        line for line in text.splitlines()
        if not re.match(r"\s*([-*]|\d+[.)]|[A-D][.)])\s", line)
    )
    return len(re.findall(r"\?(\s|$|\*|\))", prose))


def is_interview_question(turn):
    return not bigdata_calls(turn) and "?" in turn["final_text"]


def ask_simulated_user(persona, transcript_text, cwd):
    prompt = (
        "You are role-playing a user talking to a research assistant. Stay in character.\n\n"
        f"Who you are: {persona}\n\n"
        f"The conversation so far:\n{transcript_text}\n\n"
        "Write the user's next reply: one or two short sentences that answer only what the "
        "assistant just asked. If it offered options, pick one in your own words. "
        "Output the reply text only."
    )
    out, _ = claude(
        ["-p", prompt, "--model", "haiku", "--setting-sources", "project,local",
         "--strict-mcp-config", "--tools", "", "--max-turns", "1", "--output-format", "json"],
        cwd, timeout=300,
    )
    data = json.loads(out)
    return data.get("result", "").strip(), data.get("total_cost_usd") or 0.0


def render(conversation, with_tools=True):
    parts = []
    for step in conversation:
        parts.append(f"USER: {step['user']}")
        turn = step["turn"]
        if with_tools:
            for t in turn["tool_uses"]:
                parts.append(f"  [tool call] {t['name']} {json.dumps(t['input'])[:300]}")
        parts.append("ASSISTANT: " + "\n\n".join(turn["texts"]))
    return "\n\n".join(parts)


def judge(case, conversation, cwd, model):
    criteria = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(case["judge"]))
    prompt = (
        "You grade a transcript of an assistant that uses the Bigdata.com financial data tools. "
        "Tool calls are shown as [tool call] lines; the user did not see them.\n\n"
        f"TRANSCRIPT\n{render(conversation)}\n\nCRITERIA\n{criteria}\n\n"
        "Grade each criterion strictly against the transcript. Reply with JSON only, in this shape: "
        '{"criteria": [{"n": 1, "pass": true, "reason": "one sentence"}]}'
    )
    out, _ = claude(
        ["-p", prompt, "--model", model, "--setting-sources", "project,local",
         "--strict-mcp-config", "--tools", "", "--max-turns", "1", "--output-format", "json"],
        cwd, timeout=600,
    )
    data = json.loads(out)
    text = data.get("result", "")
    match = re.search(r"\{.*\}", text, re.S)
    grades = json.loads(match.group(0))["criteria"] if match else []
    by_n = {g.get("n"): g for g in grades}
    results = []
    for i, c in enumerate(case["judge"]):
        g = by_n.get(i + 1, {})
        results.append({"criterion": c, "pass": bool(g.get("pass")),
                        "reason": g.get("reason", "no grade returned")})
    return results, data.get("total_cost_usd") or 0.0


def run_case(case, run_no, args, settings, out_dir):
    label = f"{case['id']}#{run_no}"
    conversation, user_cost = [], 0.0
    with tempfile.TemporaryDirectory(prefix="bigdata-eval-") as cwd:
        user_msg, session_id = case["prompt"], None
        for _ in range(case.get("max_user_turns", 0) + 1):
            out, err = claude(subject_args(user_msg, args.model, case["connector"], settings, session_id), cwd,
                              env=CONNECTOR_OFF_ENV if case["connector"] == "off" else None)
            turn = parse_turn(out)
            if not turn["events"]:
                turn["error"] = err[-2000:]
            conversation.append({"user": user_msg, "turn": turn})
            session_id = turn["session_id"] or session_id
            if not is_interview_question(turn) or len(conversation) > case.get("max_user_turns", 0) or not case.get("persona"):
                break
            user_msg, cost = ask_simulated_user(case["persona"], render(conversation, with_tools=False), cwd)
            user_cost += cost
        grades, judge_cost = judge(case, conversation, cwd, args.judge_model)

    turns = [s["turn"] for s in conversation]
    calls = [c for t in turns for c in bigdata_calls(t)]
    questions = 0
    for t in turns:
        if is_interview_question(t):
            questions += 1
        else:
            break
    multi_question_turns = [i + 1 for i, t in enumerate(turns[:questions])
                            if question_sentences(t["final_text"]) > 1]
    # A skill counts as used when it is invoked, or when its SKILL.md is read by
    # any tool: models also read skills with a shell command.
    skills_used = sorted({
        str(t["input"].get("skill", "")) for turn in turns for t in turn["tool_uses"] if t["name"] == "Skill"
    } | {
        name for turn in turns for t in turn["tool_uses"]
        for name in re.findall(r"/([\w-]+)/SKILL\.md", json.dumps(t["input"]))
    })
    checks = case.get("checks", {})
    counted = []
    if "max_questions" in checks:
        counted.append({"check": f"questions before the first result <= {checks['max_questions']}",
                        "pass": questions <= checks["max_questions"], "value": questions})
    if "min_bigdata_calls" in checks:
        counted.append({"check": f"Bigdata.com calls >= {checks['min_bigdata_calls']}",
                        "pass": len(calls) >= checks["min_bigdata_calls"], "value": len(calls)})
    if "max_bigdata_calls" in checks:
        counted.append({"check": f"Bigdata.com calls <= {checks['max_bigdata_calls']}",
                        "pass": len(calls) <= checks["max_bigdata_calls"], "value": len(calls)})
    if checks.get("one_question_per_message"):
        counted.append({"check": "one question per interview message",
                        "pass": not multi_question_turns,
                        "value": f"messages with more than one question: {multi_question_turns or 'none'}"})
    if "uses_skill" in checks:
        hit = any(want in used for want in checks["uses_skill"] for used in skills_used)
        counted.append({"check": f"uses the method of {', '.join(checks['uses_skill'])}",
                        "pass": hit, "value": skills_used})
    account_calls = [c["name"] for c in calls if c["name"][len(CONNECTOR_PREFIX):] in ACCOUNT_CHANGING]
    counted.append({"check": "no call that changes the Bigdata.com account",
                    "pass": not account_calls, "value": account_calls or "none"})

    subject_cost = sum(t["cost_usd"] for t in turns)
    record = {
        "case": case["id"], "run": run_no, "prompt": case["prompt"], "connector": case["connector"],
        "model": args.model, "pass": all(c["pass"] for c in counted) and all(g["pass"] for g in grades),
        "counted_checks": counted, "judge": grades,
        "questions_before_result": questions, "bigdata_calls": len(calls),
        "bigdata_tools": [c["name"][len(CONNECTOR_PREFIX):] for c in calls],
        "calls_with_plugin_slug": sum(1 for c in calls if c["input"].get("plugin_slug")),
        "plugin_slugs": sorted({str(c["input"].get("plugin_slug")) for c in calls if c["input"].get("plugin_slug")}),
        "skills_used": skills_used, "bigdata_skill_loaded": any(t["skill_loaded"] for t in turns),
        "turns": len(turns), "stops": [t["stop"] for t in turns],
        "denied_tools": [d.get("tool_name") for t in turns for d in t["denials"]],
        "cost_usd": {"subject": round(subject_cost, 3), "simulated_user": round(user_cost, 3),
                     "judge": round(judge_cost, 3)},
    }

    stem = out_dir / f"{case['id']}-run{run_no}"
    with open(f"{stem}.events.jsonl", "w") as f:
        for i, step in enumerate(conversation):
            f.write(json.dumps({"turn": i + 1, "user": step["user"]}) + "\n")
            for event in step["turn"]["events"]:
                f.write(json.dumps(event) + "\n")
    Path(f"{stem}.md").write_text(f"# {label}\n\n" + render(conversation) + "\n")
    print(f"{label}: {'PASS' if record['pass'] else 'FAIL'} "
          f"(questions {questions}, Bigdata.com calls {len(calls)}, ${subject_cost:.2f})", flush=True)
    return record


def summary_markdown(records, args):
    lines = [f"# Eval results: {args.cases.name}", "",
             f"Model under test: {args.model}. Judge: {args.judge_model}. Simulated user: haiku. "
             f"Plugin: {PLUGIN_DIR.relative_to(REPO)} at {git_head()}.", "",
             "| Case | Run | Result | Questions | Bigdata.com calls | plugin_slug set | Skills used | Cost |",
             "|---|---|---|---|---|---|---|---|"]
    for r in records:
        lines.append(f"| {r['case']} | {r['run']} | {'pass' if r['pass'] else 'FAIL'} | "
                     f"{r['questions_before_result']} | {r['bigdata_calls']} | "
                     f"{r['calls_with_plugin_slug']} of {r['bigdata_calls']} | "
                     f"{', '.join(r['skills_used']) or 'none'} | ${r['cost_usd']['subject']:.2f} |")
    total = sum(sum(r["cost_usd"].values()) for r in records)
    lines += ["", f"Passed {sum(r['pass'] for r in records)} of {len(records)}. Total cost ${total:.2f}.", ""]
    for r in records:
        lines.append(f"## {r['case']}, run {r['run']}: {'pass' if r['pass'] else 'FAIL'}")
        lines.append("")
        lines.append(f"Prompt: `{r['prompt']}` (connector {r['connector']})")
        lines.append("")
        for c in r["counted_checks"]:
            lines.append(f"- {'pass' if c['pass'] else 'FAIL'}: {c['check']} (got {c['value']})")
        for g in r["judge"]:
            lines.append(f"- {'pass' if g['pass'] else 'FAIL'}: {g['criterion']} Judge: {g['reason']}")
        lines.append(f"- Bigdata.com tools called: {', '.join(r['bigdata_tools']) or 'none'}")
        if r["denied_tools"]:
            lines.append(f"- Tools denied by the eval setup: {', '.join(r['denied_tools'])}")
        lines.append(f"- Transcript: `{r['case']}-run{r['run']}.md`")
        lines.append("")
    return "\n".join(lines)


def git_head():
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip() + (
        " plus uncommitted changes" if subprocess.run(
            ["git", "status", "--porcelain", "plugins/bigdata-com"], cwd=REPO,
            capture_output=True, text=True).stdout.strip() else "")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cases", type=Path, default=Path(__file__).resolve().parent / "cases" / "bigdata.json")
    parser.add_argument("--case", action="append", help="run only this case id (repeatable)")
    parser.add_argument("--runs", type=int, default=1, help="runs per case")
    parser.add_argument("--model", default="opus", help="model under test")
    parser.add_argument("--judge-model", default="sonnet")
    parser.add_argument("--parallel", type=int, default=3)
    args = parser.parse_args()

    cases = json.loads(args.cases.read_text())["cases"]
    if args.case:
        cases = [c for c in cases if c["id"] in args.case]
    if not cases:
        sys.exit("No cases match.")

    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    out_dir = RESULTS_DIR / f"{stamp}_{args.model}"
    out_dir.mkdir(parents=True, exist_ok=True)
    settings = other_plugins_off()

    jobs = [(c, n) for c in cases for n in range(1, args.runs + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        records = list(pool.map(lambda job: run_case(job[0], job[1], args, settings, out_dir), jobs))

    (out_dir / "summary.json").write_text(json.dumps(records, indent=2) + "\n")
    (out_dir / "summary.md").write_text(summary_markdown(records, args) + "\n")
    print(f"\nPassed {sum(r['pass'] for r in records)} of {len(records)}. Results: {out_dir.relative_to(REPO)}")


if __name__ == "__main__":
    main()
