#!/usr/bin/env python3
"""Generate the trigger-eval suite for `claude plugin eval` from a prompts file.

    gen_trigger_evals.py <trigger-prompts.json>

Writes plugins/bigdata-com/evals/<skill>--<kind>-<n>/prompt.md and its
graders. Positive cases grade that the skill fired (tool_used Skill, which the
two-arm run reports as a plugin-fired indicator). Near-miss cases grade that
the neighbour fired and this skill did not. Negative cases grade that no
bigdata job skill fired (arm: both, so the check counts in both arms).
Run with: claude plugin eval plugins/bigdata-com --ablation none --runs 1
"""
import json, os, re, sys, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "plugins", "bigdata-com"))
EVALS = os.path.join(ROOT, "evals")
FM = "---\nmax_turns: 6\ntimeout_seconds: 240\nallowed_tools: [Read, Glob, Grep, Skill]\ntags: [{tags}]\n---\n\n{prompt}\n"


def grader(name, skill, mn=1, mx=None, arm=None):
    lines = ["---", "type: tool_used", "tool: Skill", f"input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'", f"min: {mn}"]
    if mx is not None:
        lines.append(f"max: {mx}")
    if arm:
        lines.append(f"arm: {arm}")
    lines.append("---\n")
    return name, "\n".join(lines)


def write_case(cdir, prompt, tags, graders):
    os.makedirs(os.path.join(cdir, "graders"), exist_ok=True)
    open(os.path.join(cdir, "prompt.md"), "w").write(FM.format(tags=", ".join(tags), prompt=prompt))
    for name, body in graders:
        open(os.path.join(cdir, "graders", name + ".md"), "w").write(body)


def main():
    data = json.load(open(sys.argv[1]))
    for d in os.listdir(EVALS) if os.path.isdir(EVALS) else []:
        if "--" in d:
            shutil.rmtree(os.path.join(EVALS, d))
    n = 0
    for skill, cases in data.items():
        for i, p in enumerate(cases.get("positive", []), 1):
            write_case(os.path.join(EVALS, f"{skill}--fires-{i}"), p, ["trigger", "positive", skill], [grader("skill-fired", skill)]); n += 1
        for i, nm in enumerate(cases.get("near_miss", []), 1):
            write_case(os.path.join(EVALS, f"{skill}--near-miss-{i}"), nm["prompt"], ["trigger", "near-miss", skill],
                       [grader("neighbour-fired", nm["expected"]), grader("this-skill-silent", skill, 0, 0, "both")]); n += 1
        for i, p in enumerate(cases.get("negative", []) if isinstance(cases.get("negative"), list) else [cases.get("negative")], 1):
            if not p:
                continue
            write_case(os.path.join(EVALS, f"{skill}--no-fire-{i}"), p, ["trigger", "negative", skill],
                       [grader("no-job-skill", "bigdata-[\\w-]+", 0, 0, "both")]); n += 1
    print(f"wrote {n} cases under {EVALS}")


if __name__ == "__main__":
    main()
