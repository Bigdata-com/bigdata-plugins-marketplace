#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

PLUGIN_ID="claude-plugin-bigdata-com"
OUTPUT_DIR="dist"
MANIFEST=".claude-plugin/plugin.json"

if [ ! -f "${MANIFEST}" ]; then
  echo "ERROR: Plugin manifest not found: ${MANIFEST}" >&2
  exit 1
fi

VERSION=$(python3 -c "import json; print(json.load(open('${MANIFEST}'))['version'])")
OUTPUT_FILE="${OUTPUT_DIR}/${PLUGIN_ID}_${VERSION}.zip"

mkdir -p "${OUTPUT_DIR}"

echo "Building plugin package: ${OUTPUT_FILE}"
rm -f "${OUTPUT_FILE}"

zip -r "${OUTPUT_FILE}" \
  .claude-plugin/ \
  .mcp.json \
  commands/ \
  skills/

echo "Created: ${OUTPUT_FILE}"