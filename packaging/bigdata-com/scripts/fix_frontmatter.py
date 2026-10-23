#!/usr/bin/env python3
"""Rewrite every SKILL.md frontmatter so it parses as YAML: the description as a folded block scalar."""
import glob, re, sys, textwrap, yaml
root = sys.argv[1] if len(sys.argv) > 1 else "plugins/bigdata-com/skills"
changed = 0
for path in sorted(glob.glob(f"{root}/*/SKILL.md")):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        print("no frontmatter:", path); continue
    fm = m.group(1)
    # pull the description value whatever its current form
    dm = re.search(r"^description:[ \t]*(>-?|\|-?)?[ \t]*\n?((?:[ \t]+.*\n?)+|.*)", fm, re.M)
    if not dm:
        print("no description:", path); continue
    raw = dm.group(2)
    if dm.group(1):
        desc = " ".join(line.strip() for line in raw.splitlines() if line.strip())
    else:
        desc = raw.strip().strip('"').strip("'")
    desc = " ".join(desc.split())
    block = "description: >-\n" + "\n".join("  " + l for l in textwrap.wrap(desc, 96, break_on_hyphens=False, break_long_words=False))
    rest = fm[dm.end():].lstrip("\n").rstrip("\n")
    new_fm = fm[:dm.start()] + block + ("\n" + rest if rest else "")
    try:
        d = yaml.safe_load(new_fm)
        assert d["name"] and d["description"], "name or description missing after rewrite"
        assert "metadata" in d and isinstance(d["metadata"], dict) and "bigdata-refs" in d["metadata"], "metadata lost"
        assert "metadata" not in d["description"], "description swallowed the metadata"
    except Exception as e:
        print("FAILED", path, e); continue
    new = "---\n" + new_fm + "\n---\n" + text[m.end():]
    if new != text:
        open(path, "w", encoding="utf-8").write(new); changed += 1
print("rewrote", changed)
