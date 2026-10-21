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
# The build fails if plugin.json points at a file that is not in the package.

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

VERSION=$(python3 - "${OPENAI_DIR}" "${PLUGIN_DIR}" "${STAGING}" <<'PYEOF'
import json, os, re, shutil, sys

openai_dir, plugin_dir, staging = sys.argv[1:4]
errors = []

EXCLUDED_DIRS = {"__pycache__"}
EXCLUDED_FILES = {".DS_Store"}
EXCLUDED_EXTENSIONS = {".pyc"}

def ignore(_, names):
    return [
        name for name in names
        if name in EXCLUDED_DIRS or name in EXCLUDED_FILES
        or os.path.splitext(name)[1] in EXCLUDED_EXTENSIONS
    ]

manifests = {}
for name in ("plugin.json", "mcp.json"):
    try:
        manifests[name] = json.load(open(os.path.join(openai_dir, name), encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{name} is not valid JSON: {error}")
    shutil.copy2(os.path.join(openai_dir, name), os.path.join(staging, name))

shutil.copytree(os.path.join(plugin_dir, "assets"), os.path.join(staging, "assets"), ignore=ignore)

skills_root = os.path.join(plugin_dir, "skills")
skills = sorted(
    name for name in os.listdir(skills_root)
    if os.path.isdir(os.path.join(skills_root, name))
)
for skill in skills:
    source = os.path.join(skills_root, skill)
    if not os.path.isfile(os.path.join(source, "SKILL.md")):
        errors.append(f"{skill}: skills/{skill}/SKILL.md not found")
        continue
    text = open(os.path.join(source, "SKILL.md"), encoding="utf-8").read()
    name = re.search(r"^name:[ \t]*(.+?)[ \t]*$", text.split("---")[1], re.M)
    if not name or name.group(1).strip("\"'") != skill:
        errors.append(f"{skill}: SKILL.md name must equal the folder name")
    shutil.copytree(source, os.path.join(staging, "skills", skill), ignore=ignore)

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

print(f"  {len(skills)} skills, version {version}", file=sys.stderr)
print(version)
PYEOF
)

OUTPUT_FILE="${OUTPUT_DIR}/${PLUGIN_ID}_${VERSION}.zip"
mkdir -p "${OUTPUT_DIR}"
rm -f "${OUTPUT_FILE}"

echo "Building OpenAI package: ${OUTPUT_FILE}"
(
  cd "${STAGING}"
  zip -r -q -X "${OLDPWD}/${OUTPUT_FILE}" plugin.json mcp.json assets/ skills/
)

echo "Created: ${OUTPUT_FILE} ($(du -h "${OUTPUT_FILE}" | cut -f1))"
