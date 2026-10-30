#!/usr/bin/env python3
"""Copy the plugin's reviewable files into <inputs>/plugin and write tree.json for the page's file browser.
usage: make_tree.py <worktree> <inputs-dir>
Entries: {"path": plugin-relative path shown in the tree, "src": the file served under plugin/}. A skill's references/
copy points its src at the library file, so each library text is published once."""
import os, sys, json, shutil, filecmp
W, IN = sys.argv[1], sys.argv[2]
PLUG = f"{W}/plugins/bigdata-com"; OUT = f"{IN}/plugin"
if os.path.isdir(OUT): shutil.rmtree(OUT)
entries = []
def put(path, src=None):
    src = src or path
    if src == path:
        d = os.path.dirname(f"{OUT}/{path}"); os.makedirs(d, exist_ok=True)
        shutil.copy2(f"{PLUG}/{path}", f"{OUT}/{path}")
    entries.append({"path": path, "src": src})
for p in [".claude-plugin/plugin.json", ".cursor-plugin/plugin.json", ".gitignore", ".mcp.json", "LICENSE", "README.md"]:
    if os.path.isfile(f"{PLUG}/{p}"): put(p)
for p in ["library/working-with-bigdata.md", "library/output-standard.md"]: put(p)
for sub in ["methods", "sectors"]:
    for f in sorted(os.listdir(f"{PLUG}/library/{sub}")): put(f"library/{sub}/{f}")
# the sector-primer bundle: identical across skills, published once from the first skill that carries it
bundle = None
skills = sorted(d for d in os.listdir(f"{PLUG}/skills") if os.path.isfile(f"{PLUG}/skills/{d}/SKILL.md"))
for s in skills:
    b = f"{PLUG}/skills/{s}/references/sector-primers.md"
    if os.path.isfile(b):
        if bundle is None:
            bundle = b; os.makedirs(f"{OUT}/library", exist_ok=True); shutil.copy2(b, f"{OUT}/library/sector-primers.md")
            entries.append({"path": "library/sector-primers.md", "src": "library/sector-primers.md"})
        elif not filecmp.cmp(b, bundle, shallow=False): print("warning: primer bundle differs in", s)
for s in skills:
    put(f"skills/{s}/SKILL.md")
    if os.path.isfile(f"{PLUG}/skills/{s}/agents/openai.yaml"): put(f"skills/{s}/agents/openai.yaml")
    if os.path.isfile(f"{PLUG}/skills/{s}/README.md"): put(f"skills/{s}/README.md")
    rd = f"{PLUG}/skills/{s}/references"
    if os.path.isdir(rd):
        for f in sorted(os.listdir(rd)):
            if f == "sector-primers.md": put(f"skills/{s}/references/{f}", "library/sector-primers.md"); continue
            for cand in [f"library/methods/{f}", f"library/sectors/{f}", f"library/{f}"]:
                if os.path.isfile(f"{PLUG}/{cand}"): put(f"skills/{s}/references/{f}", cand); break
            else:
                put(f"skills/{s}/references/{f}")  # a skill-own reference (the entry skill's skill-builder)
json.dump(entries, open(f"{OUT}/tree.json", "w"), indent=0)
n_files = sum(1 for e in entries if e["path"] == e["src"])
print(f"{len(entries)} entries, {n_files} files copied, {len(skills)} skills")
