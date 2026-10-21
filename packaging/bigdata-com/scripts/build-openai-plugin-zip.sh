#!/bin/bash
set -euo pipefail

# Build the OpenAI plugin package from openai/ and the assets and skills in
# plugins/bigdata-com/.
# Writes dist/openai-plugin-bigdata-com_<version>.zip, ready to submit to OpenAI.
#
# Usage:
#   scripts/build-openai-plugin-zip.sh
#
# The package holds plugin.json and mcp.json from openai/, plus assets/ and
# every skill under skills/. The version is taken from openai/plugin.json.
# Only files tracked by git are packaged, so caches, virtualenvs and editor
# files in the checkout stay out; git add a new file before building.
# The build fails if plugin.json points at a file that is not in the package.
# The zip is reproducible: the same sources always give the same bytes.
#
# Requires git and python3.

cd "$(dirname "$0")/.."

PLUGIN_DIR="../../plugins/bigdata-com"

PLUGIN_ID="openai-plugin-bigdata-com"
OUTPUT_DIR="dist"
OPENAI_DIR="openai"

for file in "${OPENAI_DIR}/plugin.json" "${OPENAI_DIR}/mcp.json"; do
  if [ ! -f "${file}" ]; then
    echo "ERROR: Not found: ${file}" >&2
    exit 1
  fi
done

STAGING=$(mktemp -d)
trap 'rm -rf "${STAGING}"' EXIT
PACKAGE="${STAGING}/package.zip"

VERSION=$(python3 - "${OPENAI_DIR}" "${PLUGIN_DIR}" "${STAGING}/files" "${PACKAGE}" <<'PYEOF'
import json, os, re, shutil, subprocess, sys, zipfile

openai_dir, plugin_dir, staging, package = sys.argv[1:5]
os.makedirs(staging)
errors = []

manifests = {}
for name in ("plugin.json", "mcp.json"):
    try:
        manifests[name] = json.load(open(os.path.join(openai_dir, name), encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{name} is not valid JSON: {error}")
    shutil.copy2(os.path.join(openai_dir, name), os.path.join(staging, name))

# Package only the files git tracks, so whatever else is in the checkout stays out.
tracked = subprocess.run(
    ["git", "-C", plugin_dir, "ls-files", "-z", "--", "assets", "skills"],
    check=True, capture_output=True, text=True,
).stdout.split("\0")
tracked = [path for path in tracked if path and os.path.isfile(os.path.join(plugin_dir, path))]

for path in tracked:
    os.makedirs(os.path.dirname(os.path.join(staging, path)), exist_ok=True)
    shutil.copy2(os.path.join(plugin_dir, path), os.path.join(staging, path))

skills = sorted({path.split("/")[1] for path in tracked if path.startswith("skills/")})
for skill in skills:
    source = os.path.join(staging, "skills", skill)
    if not os.path.isfile(os.path.join(source, "SKILL.md")):
        errors.append(f"{skill}: skills/{skill}/SKILL.md not found or not tracked by git")
        continue
    text = open(os.path.join(source, "SKILL.md"), encoding="utf-8").read()
    name = re.search(r"^name:[ \t]*(.+?)[ \t]*$", text.split("---")[1], re.M)
    if not name or name.group(1).strip("\"'") != skill:
        errors.append(f"{skill}: SKILL.md name must equal the folder name")

# Every relative path in plugin.json (logo, composerIcon, ...) must be in the package.
def local_paths(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from local_paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from local_paths(item)
    elif isinstance(value, str) and value.startswith("./"):
        yield value

plugin = manifests.get("plugin.json", {})
for path in sorted(set(local_paths(plugin))):
    if not os.path.isfile(os.path.join(staging, path)):
        errors.append(f"plugin.json points at {path}, which is not in the package")

version = plugin.get("version")
if not version:
    errors.append("plugin.json has no version")

for error in errors:
    print(f"  ERROR {error}", file=sys.stderr)
if errors:
    sys.exit(1)

# Sorted entries with a fixed date and fixed permissions, so the zip does not
# change between builds unless a packaged file does.
entries = []
for dirpath, dirnames, filenames in os.walk(staging):
    for name in dirnames:
        entries.append(os.path.relpath(os.path.join(dirpath, name), staging) + "/")
    for name in filenames:
        entries.append(os.path.relpath(os.path.join(dirpath, name), staging))

with zipfile.ZipFile(package, "w") as archive:
    for entry in sorted(entries):
        info = zipfile.ZipInfo(entry, date_time=(1980, 1, 1, 0, 0, 0))
        if entry.endswith("/"):
            info.external_attr = (0o40755 << 16) | 0x10
            archive.writestr(info, b"")
        else:
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(os.path.join(staging, entry), "rb") as handle:
                archive.writestr(info, handle.read())

print(f"  {len(skills)} skills, version {version}", file=sys.stderr)
print(version)
PYEOF
)

OUTPUT_FILE="${OUTPUT_DIR}/${PLUGIN_ID}_${VERSION}.zip"
mkdir -p "${OUTPUT_DIR}"
rm -f "${OUTPUT_FILE}"

mv "${PACKAGE}" "${OUTPUT_FILE}"

echo "Created: ${OUTPUT_FILE} ($(du -h "${OUTPUT_FILE}" | cut -f1))"
