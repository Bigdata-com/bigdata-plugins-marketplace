#!/bin/bash
set -euo pipefail

# Build a development zip of plugins/bigdata-com for uploading to claude.ai as a
# custom plugin, so a branch can be tried there before it is released.
# Writes dist/claude-plugin-bigdata-com_<version>-dev-<commit>.zip.
#
# Usage:
#   scripts/build-claude-dev-zip.sh
#   scripts/build-claude-dev-zip.sh --name bigdata-com-dev
#
# --name changes the plugin name in the zipped plugin.json (not in the repo),
# so the dev build installs next to an existing bigdata-com plugin on claude.ai
# instead of replacing it.
#
# The zip holds .claude-plugin/, .mcp.json, assets/ and skills/ at its root,
# the layout claude.ai expects. Only files tracked by git are packaged, so
# commit or git add a change before building; the build stops if a packaged
# file has uncommitted changes, because the commit in the name would be wrong.
# Apart from --name, the manifest is packaged as it is: the version in the
# file name is for telling builds apart, not a release number.
#
# Requires git and python3.

NAME=""
if [ "${1:-}" = "--name" ] && [ -n "${2:-}" ]; then
  NAME="$2"
elif [ $# -gt 0 ]; then
  echo "Usage: $0 [--name <plugin-name>]" >&2
  exit 1
fi

cd "$(dirname "$0")/.."

PLUGIN_DIR="../../plugins/bigdata-com"
OUTPUT_DIR="dist"
PATHS=(.claude-plugin .mcp.json assets skills)

if [ -n "$(git -C "${PLUGIN_DIR}" status --porcelain -- "${PATHS[@]}")" ]; then
  echo "ERROR: plugins/bigdata-com has uncommitted changes; commit them first." >&2
  exit 1
fi

VERSION=$(python3 -c "import json, sys; print(json.load(open(sys.argv[1]))['version'])" \
  "${PLUGIN_DIR}/.claude-plugin/plugin.json")
COMMIT=$(git -C "${PLUGIN_DIR}" rev-parse --short HEAD)
OUTPUT_FILE="${OUTPUT_DIR}/claude-plugin-${NAME:-bigdata-com}_${VERSION}-dev-${COMMIT}.zip"

mkdir -p "${OUTPUT_DIR}"
rm -f "${OUTPUT_FILE}"

python3 - "${PLUGIN_DIR}" "${OUTPUT_FILE}" "${NAME}" "${PATHS[@]}" <<'PYEOF'
import json, os, subprocess, sys, zipfile

plugin_dir, output, name, *paths = sys.argv[1:]
tracked = subprocess.run(
    ["git", "-C", plugin_dir, "ls-files", "-z", "--", *paths],
    check=True, capture_output=True, text=True,
).stdout.split("\0")
tracked = sorted(path for path in tracked if path and os.path.isfile(os.path.join(plugin_dir, path)))

# Fixed dates and permissions, so the same commit always gives the same bytes.
with zipfile.ZipFile(output, "w") as archive:
    for path in tracked:
        info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
        info.external_attr = 0o100644 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        with open(os.path.join(plugin_dir, path), "rb") as handle:
            data = handle.read()
        if name and path == ".claude-plugin/plugin.json":
            manifest = json.loads(data)
            manifest["name"] = name
            data = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        archive.writestr(info, data)

skills = {path.split("/")[1] for path in tracked if path.startswith("skills/")}
print(f"  {len(tracked)} files, {len(skills)} skills", file=sys.stderr)
PYEOF

echo "Created: packaging/bigdata-com/${OUTPUT_FILE} ($(du -h "${OUTPUT_FILE}" | cut -f1))"
