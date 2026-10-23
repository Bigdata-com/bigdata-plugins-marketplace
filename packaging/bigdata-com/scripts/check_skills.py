#!/usr/bin/env python3
"""Validate every skill against the union of the Claude, OpenAI and Microsoft rules.

Fails on: a missing SKILL.md or frontmatter; name not equal to the folder;
description over 1,024 characters or under 200; body over 400 lines; a
link to a file that does not exist; a `../` path; more than 20 companion
files, a file over 5 MB or a skill over 10 MB (Cowork); a text file over
256 KiB (Anthropic directory); the eight required headings missing; a
rating word; "Prepared with Claude"; a hard-coded year in an instruction;
non-ASCII characters; a missing agents/openai.yaml; a plugin:skill name over
64 characters for the OpenAI app id; more than 512 files in the plugin.
"""
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "plugins", "bigdata-com"))
SKILLS = os.path.join(ROOT, "skills")
OPENAI_APP = "app-69491eceef3c8191beb70788b7840429"
HEADINGS = ["## Before starting", "## Scope the request", "## Gather", "## Analyse", "## Write", "## Checks before sending", "## Hand-offs"]
RATING = re.compile(r"\b(strong buy|buy rating|sell rating|overweight|underweight|accumulate|outperform|underperform)\b", re.I)
errors, warnings = [], []
total_files = 0

for skill in sorted(os.listdir(SKILLS)):
    d = os.path.join(SKILLS, skill)
    if not os.path.isdir(d):
        continue
    sk = os.path.join(d, "SKILL.md")
    if not os.path.isfile(sk):
        errors.append(f"{skill}: no SKILL.md"); continue
    text = open(sk, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        errors.append(f"{skill}: no frontmatter"); continue
    fm, body = m.group(1), m.group(2)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != skill:
        errors.append(f"{skill}: frontmatter name must equal the folder name")
    if len(OPENAI_APP) + 1 + len(skill) > 64:
        errors.append(f"{skill}: plugin:skill name is over 64 characters for the OpenAI app id")
    dm = re.search(r"^description:\s*(.+?)(?=^\w|\Z)", fm, re.M | re.S)
    desc = " ".join(dm.group(1).split()) if dm else ""
    if desc.startswith(">"):
        desc = " ".join(desc[1:].split())
    if not desc:
        errors.append(f"{skill}: no description")
    elif len(desc) > 1024:
        errors.append(f"{skill}: description is {len(desc)} characters, over 1,024")
    elif len(desc) < 200:
        errors.append(f"{skill}: description is {len(desc)} characters, too thin to route on")
    elif len(desc) > 600:
        warnings.append(f"{skill}: description is {len(desc)} characters; target is about 500")
    lines = body.count("\n") + 1
    if lines > 400:
        errors.append(f"{skill}: body is {lines} lines, over 400")
    if skill != "bigdata":
        for h in HEADINGS:
            if h not in body:
                errors.append(f"{skill}: missing heading {h}")
    for link in re.findall(r"\]\(([^)#]+)\)", text) + re.findall(r"`(references/[^`]+\.md)`", text):
        if link.startswith("http"):
            continue
        if link.startswith("../"):
            errors.append(f"{skill}: path escapes the skill folder: {link}")
        elif not os.path.exists(os.path.join(d, link)):
            errors.append(f"{skill}: links to {link}, which does not exist")
    if RATING.search(body):
        errors.append(f"{skill}: rating word in body: {RATING.search(body).group(0)}")
    if "Prepared with Claude" in text:
        errors.append(f"{skill}: 'Prepared with Claude' footer")
    for y in re.findall(r"\b(20[12]\d)\b", body):
        if f"FY{y}" not in body and f"FY {y}" not in body:
            warnings.append(f"{skill}: year {y} appears in the body; make sure it is an example, not a rule")
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"{skill}: SKILL.md has non-ASCII characters")
    if "—" in text:
        errors.append(f"{skill}: em dash in SKILL.md")
    if not os.path.isfile(os.path.join(d, "agents", "openai.yaml")):
        errors.append(f"{skill}: agents/openai.yaml missing")
    # companion files
    files, size = [], 0
    for dp, dn, fn in os.walk(d):
        dn[:] = [x for x in dn if x not in ("__pycache__",)]
        for f in fn:
            if f == ".DS_Store":
                continue
            p = os.path.join(dp, f); s = os.path.getsize(p); size += s; files.append(p)
            if s > 5 * 1024 * 1024:
                errors.append(f"{skill}: {os.path.relpath(p, d)} is over 5 MB")
            if f.endswith((".md", ".yaml", ".json", ".txt")) and s > 256 * 1024:
                errors.append(f"{skill}: {os.path.relpath(p, d)} is over 256 KiB (directory review)")
            if f.endswith(".md") and f != "SKILL.md":
                t = open(p, encoding="utf-8").read()
                if "—" in t:
                    errors.append(f"{skill}: em dash in {os.path.relpath(p, d)}")
    total_files += len(files)
    companions = [p for p in files if not p.endswith("SKILL.md") and "/agents/" not in p and not p.endswith(".svg")]
    if len(companions) > 20:
        errors.append(f"{skill}: {len(companions)} companion files, Cowork allows 20")
    if size > 10 * 1024 * 1024:
        errors.append(f"{skill}: over 10 MB in total")

for dp, dn, fn in os.walk(ROOT):
    pass
plugin_files = sum(len(fn) for _, _, fn in os.walk(ROOT))
if plugin_files > 512:
    errors.append(f"plugin has {plugin_files} files; the Anthropic directory holds plugins above 512 for a reviewer")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e, file=sys.stderr)
print(f"{len([s for s in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, s, 'SKILL.md'))])} skills, {plugin_files} files in the plugin, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
