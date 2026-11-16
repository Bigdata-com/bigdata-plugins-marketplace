#!/usr/bin/env python3
"""Write the plugin version into the `plugin_slug` every skill sends.

A skill passes `plugin_slug: "<skill name>@<plugin version>"` on its
Bigdata.com calls, for example `bigdata-quick-take@2.0.0`, so the server can
tell which release of the plugin a user runs. The version is the one in
plugins/bigdata-com/.claude-plugin/plugin.json. The same skill files ship to
every host, so every host reports that version, whatever number its own
package carries.

The value is written in each SKILL.md and in the identity line the entry
skill's builder gives the skills it writes (references/skill-builder.md).
Raise the version in plugin.json, run this script, and commit both.

    stamp_version.py          write the version, and report what changed
    stamp_version.py --check  exit 1 if a file does not carry the version
"""
import glob, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "plugins", "bigdata-com"))
SKILLS = os.path.join(ROOT, "skills")
MANIFEST = os.path.join(ROOT, ".claude-plugin", "plugin.json")
# What the server accepts after the "@": one to three dot-separated numbers.
VERSION = re.compile(r"[0-9]{1,5}(\.[0-9]{1,5}){0,2}")
SLUG = re.compile(r'(plugin_slug: ")([a-z0-9-]+)(?:@[^"]*)?(")')


def main():
    check = "--check" in sys.argv
    version = json.load(open(MANIFEST, encoding="utf-8")).get("version", "")
    if not VERSION.fullmatch(version):
        print(f"ERROR plugin.json version {version!r} is not one to three dot-separated numbers", file=sys.stderr)
        return 1
    files = sorted(glob.glob(os.path.join(SKILLS, "*", "SKILL.md")))
    files.append(os.path.join(SKILLS, "bigdata", "references", "skill-builder.md"))
    changed, errors = [], []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8").read()
        stamped, count = SLUG.subn(lambda m: f"{m.group(1)}{m.group(2)}@{version}{m.group(3)}", text)
        if count != 1:
            errors.append(f'{rel}: expected one plugin_slug: "<slug>", found {count}')
            continue
        if stamped != text:
            changed.append(rel)
            if not check:
                open(path, "w", encoding="utf-8").write(stamped)
    for error in errors:
        print("ERROR", error, file=sys.stderr)
    for rel in changed:
        print(("STALE " if check else "wrote ") + rel)
    print(f"{len(files)} files, version {version}, {len(changed)} {'stale' if check else 'changed'}, {len(errors)} errors")
    return 1 if errors or (check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
