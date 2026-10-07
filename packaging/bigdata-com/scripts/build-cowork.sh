#!/bin/bash
set -euo pipefail

# Build the Microsoft 365 Copilot Cowork plugin package from cowork/ and the
# skills in plugins/bigdata-com/skills/.
# Writes dist/cowork-plugin-bigdata-com_<version>.zip, ready to upload to Cowork.
#
# Usage:
#   scripts/build-cowork.sh
#
# The package ships the skills listed in cowork/manifest.json (agentSkills),
# with the version taken from plugins/bigdata-com/.claude-plugin/plugin.json.
# The build fails on anything Cowork would reject at upload.

cd "$(dirname "$0")/.."

PLUGIN_DIR="../../plugins/bigdata-com"

PLUGIN_ID="cowork-plugin-bigdata-com"
OUTPUT_DIR="dist"
COWORK_DIR="cowork"
MANIFEST="${PLUGIN_DIR}/.claude-plugin/plugin.json"

if [ ! -f "${MANIFEST}" ]; then
  echo "ERROR: Plugin manifest not found: ${MANIFEST}" >&2
  exit 1
fi

VERSION=$(python3 -c "import json; print(json.load(open('${MANIFEST}'))['version'])")
OUTPUT_FILE="${OUTPUT_DIR}/${PLUGIN_ID}_${VERSION}.zip"

STAGING=$(mktemp -d)
trap 'rm -rf "${STAGING}"' EXIT

python3 - "${COWORK_DIR}" "${PLUGIN_DIR}/skills" "${STAGING}" "${VERSION}" <<'PYEOF'
import json, os, re, shutil, struct, sys

cowork_dir, skills_root, staging, version = sys.argv[1:5]
errors = []

# Cowork limits: https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-plugin-development
MAX_SKILLS = 20
MAX_FILES_PER_SKILL = 20
MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_SKILL_BYTES = 10 * 1024 * 1024
# Upload rejects .svg in a skill folder, and the allowed list is not documented.
# Add an extension here only after an upload with it has passed.
ALLOWED_EXTENSIONS = {".md", ".py"}
# Files other platforms need that Cowork does not read.
EXCLUDED_FILES = {"README.md"}
EXCLUDED_DIRS = {"agents", "__pycache__"}
EXCLUDED_EXTENSIONS = {".svg", ".pyc"}
ICON_SIZES = {"color.png": (192, 192), "outline.png": (32, 32)}

manifest = json.load(open(os.path.join(cowork_dir, "manifest.json"), encoding="utf-8"))
manifest["version"] = version

skills = [entry["folder"].removeprefix("./skills/") for entry in manifest["agentSkills"]]
if len(skills) > MAX_SKILLS:
    errors.append(f"{len(skills)} skills listed, Cowork allows {MAX_SKILLS}")
if len(skills) != len(set(skills)):
    errors.append("agentSkills lists a skill twice")

for skill in skills:
    source = os.path.join(skills_root, skill)
    target = os.path.join(staging, "skills", skill)
    if not os.path.isfile(os.path.join(source, "SKILL.md")):
        errors.append(f"{skill}: skills/{skill}/SKILL.md not found")
        continue

    text = open(os.path.join(source, "SKILL.md"), encoding="utf-8").read()
    name = re.search(r"^name:[ \t]*(.+?)[ \t]*$", text.split("---")[1], re.M)
    if not name or name.group(1).strip("\"'") != skill:
        errors.append(f"{skill}: SKILL.md name must equal the folder name")

    files = []
    for dirpath, dirnames, filenames in os.walk(source):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for filename in filenames:
            if filename in EXCLUDED_FILES or filename == ".DS_Store":
                continue
            extension = os.path.splitext(filename)[1]
            if extension in EXCLUDED_EXTENSIONS:
                continue
            path = os.path.join(dirpath, filename)
            relative = os.path.relpath(path, source)
            if extension not in ALLOWED_EXTENSIONS:
                errors.append(f"{skill}: {relative} has a file type not yet tested in Cowork")
            if os.path.getsize(path) > MAX_FILE_BYTES:
                errors.append(f"{skill}: {relative} is larger than 5 MB")
            files.append((path, relative))

    # SKILL.md itself does not count towards the companion file limit.
    if len(files) - 1 > MAX_FILES_PER_SKILL:
        errors.append(f"{skill}: {len(files) - 1} companion files, Cowork allows {MAX_FILES_PER_SKILL}")
    if sum(os.path.getsize(path) for path, _ in files) > MAX_SKILL_BYTES:
        errors.append(f"{skill}: larger than 10 MB in total")

    for path, relative in files:
        os.makedirs(os.path.dirname(os.path.join(target, relative)), exist_ok=True)
        shutil.copy2(path, os.path.join(target, relative))

    for link in re.findall(r"\]\((\./[^)#]+)", text):
        if not os.path.exists(os.path.join(target, link)):
            errors.append(f"{skill}: SKILL.md links to {link}, which is not in the package")

for icon, expected in ICON_SIZES.items():
    path = os.path.join(cowork_dir, icon)
    with open(path, "rb") as handle:
        header = handle.read(24)
    size = struct.unpack(">II", header[16:24])
    if header[:8] != b"\x89PNG\r\n\x1a\n" or size != expected:
        errors.append(f"{icon} must be a {expected[0]}x{expected[1]} PNG")
    shutil.copy2(path, os.path.join(staging, icon))

left_out = [
    name for name in sorted(os.listdir(skills_root))
    if name not in skills and os.path.isfile(os.path.join(skills_root, name, "SKILL.md"))
]
if left_out:
    print(f"  NOTE  not in cowork/manifest.json, so left out: {', '.join(left_out)}")

for error in errors:
    print(f"  ERROR {error}", file=sys.stderr)
if errors:
    sys.exit(1)

with open(os.path.join(staging, "manifest.json"), "w", encoding="utf-8") as handle:
    json.dump(manifest, handle, indent=2)
    handle.write("\n")
print(f"  {len(skills)} skills, version {version}")
PYEOF

mkdir -p "${OUTPUT_DIR}"
rm -f "${OUTPUT_FILE}"

echo "Building Cowork package: ${OUTPUT_FILE}"
(
  cd "${STAGING}"
  zip -r -q -X "${OLDPWD}/${OUTPUT_FILE}" manifest.json color.png outline.png skills/
)

echo "Created: ${OUTPUT_FILE} ($(du -h "${OUTPUT_FILE}" | cut -f1))"
