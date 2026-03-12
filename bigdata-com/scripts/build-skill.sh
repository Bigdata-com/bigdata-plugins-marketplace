#!/bin/bash
set -euo pipefail

# Navigate to repo root (parent of scripts/)
cd "$(dirname "$0")/.."

VERSION="${1:?Version is required as first argument}"

# New structure
SKILL_DIR="skills/financial-research-analyst"
SKILL_NAME="bigdata-financial-research-analyst"

OUTPUT_DIR="dist"
OUTPUT_FILE="${OUTPUT_DIR}/${SKILL_NAME}_${VERSION}.skill"

# Ensure output directory exists
mkdir -p "${OUTPUT_DIR}"

if [ ! -d "${SKILL_DIR}" ]; then
  echo "ERROR: Skill directory not found: ${SKILL_DIR}" >&2
  exit 1
fi

echo "Building legacy skill package: ${OUTPUT_FILE}"
rm -f "${OUTPUT_FILE}"

# zip the folder content under its directory name (keeps structure)
(
  cd "$(dirname "${SKILL_DIR}")"
  zip -r "../${OUTPUT_FILE}" "$(basename "${SKILL_DIR}")"
)

echo "Created: ${OUTPUT_FILE}"