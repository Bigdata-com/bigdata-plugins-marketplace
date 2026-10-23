#!/usr/bin/env python3
"""Copy the shared library into each skill's references/ folder.

Each SKILL.md lists what it needs in its frontmatter:

    metadata:
      bigdata-refs: working-with-bigdata, output-standard, expectations, base-rates
      bigdata-sector-primer: auto | none

Method files and the two shared files are copied one to one. With
bigdata-sector-primer set to auto, the eleven sector primers are joined into
one references/sector-primers.md with a contents list, so a skill never
carries more than one primer file (Microsoft Cowork allows 20 companion
files per skill). Files in references/ that the library does not own (for
example the entry skill's skill-builder.md) are left alone.

    sync_library.py          copy, and report what changed
    sync_library.py --check  exit 1 if any skill's copies differ from the library
"""
import os, re, sys, hashlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "plugins", "bigdata-com"))
LIB = os.path.join(ROOT, "library")
SKILLS = os.path.join(ROOT, "skills")
SECTOR_ORDER = ["technology-software", "semiconductors-and-hardware", "financials-banks", "insurance", "healthcare-pharma",
                "reits", "industrials", "consumer-retail", "energy", "materials", "communication-services", "utilities"]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def meta_value(fm, key):
    m = re.search(r"^\s*" + re.escape(key) + r":\s*(.+?)\s*$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else ""


def library_file(name):
    for cand in (os.path.join(LIB, name + ".md"), os.path.join(LIB, "methods", name + ".md")):
        if os.path.isfile(cand):
            return cand
    return None


def primers_bundle():
    parts, toc = [], []
    for name in SECTOR_ORDER:
        path = os.path.join(LIB, "sectors", name + ".md")
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read().strip()
        title = re.match(r"^#\s+(.*)", text)
        toc.append(f"- {title.group(1) if title else name} (`{name}`)")
        parts.append(text.replace("\n# ", "\n## ", 1) if text.startswith("# ") else text)
        parts[-1] = re.sub(r"^# ", "## ", parts[-1], count=1)
    head = ("# Sector primers\n\nRead the section for the company's sector before analysing; skip the rest. "
            "Every figure is a range with its source and a (verify) mark, never a current fact.\n\n" + "\n".join(toc) + "\n\n")
    return head + "\n\n".join(parts) + "\n"


def main():
    check = "--check" in sys.argv
    changed, errors = [], []
    bundle = primers_bundle()
    for skill in sorted(os.listdir(SKILLS)):
        sk = os.path.join(SKILLS, skill, "SKILL.md")
        if not os.path.isfile(sk):
            continue
        fm = frontmatter(open(sk, encoding="utf-8").read())
        refs = [r.strip() for r in meta_value(fm, "bigdata-refs").split(",") if r.strip()]
        primer = meta_value(fm, "bigdata-sector-primer") or "none"
        refdir = os.path.join(SKILLS, skill, "references")
        wanted = {}
        for r in refs:
            src = library_file(r)
            if not src:
                errors.append(f"{skill}: bigdata-refs names {r}, which is not in the library")
                continue
            wanted[r + ".md"] = open(src, encoding="utf-8").read()
        if primer == "auto":
            wanted["sector-primers.md"] = bundle
        for fname, content in wanted.items():
            dst = os.path.join(refdir, fname)
            cur = open(dst, encoding="utf-8").read() if os.path.isfile(dst) else None
            if cur != content:
                changed.append(f"{skill}/references/{fname}")
                if not check:
                    os.makedirs(refdir, exist_ok=True)
                    open(dst, "w", encoding="utf-8").write(content)
        # stale copies of library files that the skill no longer lists
        if os.path.isdir(refdir):
            for fname in os.listdir(refdir):
                base = fname[:-3] if fname.endswith(".md") else fname
                if fname not in wanted and (library_file(base) or fname == "sector-primers.md"):
                    changed.append(f"{skill}/references/{fname} (stale, removed)")
                    if not check:
                        os.remove(os.path.join(refdir, fname))
    for e in errors:
        print("ERROR", e, file=sys.stderr)
    for c in changed:
        print(("DIFF " if check else "wrote ") + c)
    if errors or (check and changed):
        sys.exit(1)
    print(f"library in sync across {len([s for s in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, s, 'SKILL.md'))])} skills")


if __name__ == "__main__":
    main()
