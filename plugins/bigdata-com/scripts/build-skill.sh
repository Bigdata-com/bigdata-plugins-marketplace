#!/bin/bash
set -euo pipefail

# Build a standalone, self-contained skill package from skills/<name>/.
# Emits the same archive twice: <name>_<version>.skill and <name>_<version>.zip.
#
# Usage:
#   scripts/build-skill.sh [-v VERSION] [-o OUTPUT_DIR] <skill-dir> [<skill-dir> ...]
#   scripts/build-skill.sh [-v VERSION] --all
#
# Examples:
#   scripts/build-skill.sh bigdata-earnings-preview
#   scripts/build-skill.sh -v 1.0.0 bigdata-earnings-preview
#   scripts/build-skill.sh --all
#
# VERSION defaults to the version in .claude-plugin/plugin.json.
# Each skill is validated before packaging; a failing skill aborts the build.

# Navigate to plugin root (parent of scripts/)
cd "$(dirname "$0")/.."

SKILLS_ROOT="skills"
OUTPUT_DIR="dist"
MANIFEST=".claude-plugin/plugin.json"
VERSION=""
BUILD_ALL=false

# Skills --all should skip (e.g. work in progress). Empty by default.
EXCLUDE_SKILLS=()

usage() {
  sed -n '3,17p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-1}"
}

while [ $# -gt 0 ]; do
  case "$1" in
    -v|--version) VERSION="${2:?-v requires a version}"; shift 2 ;;
    -o|--output)  OUTPUT_DIR="${2:?-o requires a directory}"; shift 2 ;;
    --all)        BUILD_ALL=true; shift ;;
    -h|--help)    usage 0 ;;
    -*)           echo "ERROR: unknown option: $1" >&2; usage ;;
    *)            break ;;
  esac
done

if [ -z "${VERSION}" ]; then
  if [ ! -f "${MANIFEST}" ]; then
    echo "ERROR: no -v VERSION given and manifest not found: ${MANIFEST}" >&2
    exit 1
  fi
  VERSION=$(python3 -c "import json; print(json.load(open('${MANIFEST}'))['version'])")
fi

# Resolve the list of skills to build
SKILLS=()
if [ "${BUILD_ALL}" = true ]; then
  for dir in "${SKILLS_ROOT}"/*/; do
    name=$(basename "${dir}")
    # a directory without a SKILL.md is not a skill
    [ -f "${dir}SKILL.md" ] || continue
    skip=false
    for excluded in ${EXCLUDE_SKILLS[@]+"${EXCLUDE_SKILLS[@]}"}; do
      [ "${name}" = "${excluded}" ] && skip=true
    done
    [ "${skip}" = true ] && continue
    SKILLS+=("${name}")
  done
elif [ $# -gt 0 ]; then
  SKILLS=("$@")
else
  echo "ERROR: no skill specified." >&2
  echo "Available skills in ${SKILLS_ROOT}/:" >&2
  for dir in "${SKILLS_ROOT}"/*/; do echo "  - $(basename "${dir}")" >&2; done
  echo >&2
  usage
fi

if [ ${#SKILLS[@]} -eq 0 ]; then
  echo "ERROR: nothing to build." >&2
  exit 1
fi

# Validate one skill directory. Fails loudly on anything that would ship broken.
validate_skill() {
  local skill_dir="$1"
  local skill_name="$2"

  [ -f "${skill_dir}/SKILL.md" ] || {
    echo "ERROR: ${skill_dir}/SKILL.md not found" >&2; return 1
  }
  [ -f "${skill_dir}/agents/openai.yaml" ] || {
    echo "ERROR: ${skill_dir}/agents/openai.yaml not found (required for OpenAI)" >&2; return 1
  }

  python3 - "${skill_dir}" "${skill_name}" <<'PYEOF'
import os, re, sys

skill_dir, skill_name = sys.argv[1], sys.argv[2]
errors, warnings = [], []

# --- SKILL.md frontmatter -------------------------------------------------
text = open(os.path.join(skill_dir, "SKILL.md"), encoding="utf-8").read()
match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
if not match:
    errors.append("SKILL.md has no YAML frontmatter block")
else:
    fm = match.group(1)
    name = re.search(r"^name:[ \t]*(.+?)[ \t]*$", fm, re.M)
    if not name:
        errors.append("SKILL.md frontmatter has no 'name' field")
    elif name.group(1).strip("\"'") != skill_name:
        errors.append(
            f"SKILL.md name '{name.group(1)}' does not match directory '{skill_name}'"
        )

    # description may be inline or a folded/literal block scalar
    desc_match = re.search(
        r"^description:[ \t]*(>|\|)?[-+]?[ \t]*\r?\n?(.*)", fm, re.S | re.M
    )
    if not desc_match:
        errors.append("SKILL.md frontmatter has no 'description' field")
    else:
        if desc_match.group(1):  # block scalar: take the indented lines
            lines = []
            for line in desc_match.group(2).splitlines():
                if line.strip() and not line[:1].isspace():
                    break  # next top-level key
                lines.append(line.strip())
            desc = " ".join(l for l in lines if l)
        else:
            desc = desc_match.group(2).splitlines()[0].strip().strip("\"'")
        if len(desc) < 40:
            errors.append(f"description is only {len(desc)} chars — too thin to route on")
        if len(desc) > 1024:
            errors.append(f"description is {len(desc)} chars — exceeds the 1024 limit")

# --- relative links resolve within the package ----------------------------
for target in re.findall(r"\]\((\.{1,2}/[^)#]+)", text):
    if not os.path.exists(os.path.join(skill_dir, target)):
        errors.append(f"SKILL.md links to missing file: {target}")
    if target.startswith("../"):
        errors.append(f"SKILL.md escapes the skill folder (not self-contained): {target}")

# --- the report template must exist and be self-contained too -------------
# Templates are usually lifted from the monolith, so they arrive carrying
# links that only resolved there.
tpl = os.path.join(skill_dir, "assets", "report-template.md")
if not os.path.exists(tpl):
    errors.append("assets/report-template.md not found")
else:
    tpl_text = open(tpl, encoding="utf-8").read()
    for target in re.findall(r"\]\((\.{1,2}/[^)#]+)", tpl_text):
        resolved = os.path.normpath(os.path.join(skill_dir, "assets", target))
        if not os.path.exists(resolved):
            errors.append(f"report-template.md links to missing file: {target}")
        if target.startswith("../"):
            errors.append(f"report-template.md escapes the skill folder: {target}")
    # bare "apply ./some-file.md" prose references left over from the monolith
    for stray in re.findall(r"(?<!\]\()\.\/[A-Za-z0-9_\-]+\.md", tpl_text):
        errors.append(f"report-template.md has a dangling file reference: {stray}")
    if "Powered by Bigdata.com" not in tpl_text:
        errors.append("report-template.md is missing the Powered by Bigdata.com footer")
    if not re.search(r"^#+ *Sources", tpl_text, re.M) and "| # | Source" not in tpl_text:
        warnings.append("report-template.md has no Sources section")

# --- openai.yaml icons ----------------------------------------------------
agent_manifest = os.path.join(skill_dir, "agents", "openai.yaml")
agent_text = open(agent_manifest, encoding="utf-8").read()
for icon in re.findall(r"^\s*icon_(?:small|large):[ \t]*(.+?)[ \t]*$", agent_text, re.M):
    icon = icon.strip("\"'")
    if not os.path.exists(os.path.join(skill_dir, icon)):
        errors.append(f"agents/openai.yaml references missing icon: {icon}")
if "display_name:" not in agent_text:
    warnings.append("agents/openai.yaml has no interface.display_name")

for w in warnings:
    print(f"  WARN  {w}")
for e in errors:
    print(f"  ERROR {e}", file=sys.stderr)
sys.exit(1 if errors else 0)
PYEOF
}

mkdir -p "${OUTPUT_DIR}"
built=()

for skill_name in "${SKILLS[@]}"; do
  skill_name="${skill_name%/}"
  skill_name="$(basename "${skill_name}")"
  skill_dir="${SKILLS_ROOT}/${skill_name}"

  if [ ! -d "${skill_dir}" ]; then
    echo "ERROR: skill directory not found: ${skill_dir}" >&2
    exit 1
  fi

  echo "Validating ${skill_name}..."
  validate_skill "${skill_dir}" "${skill_name}"

  output_file="${OUTPUT_DIR}/${skill_name}_${VERSION}.skill"
  zip_file="${OUTPUT_DIR}/${skill_name}_${VERSION}.zip"
  echo "Building ${output_file}"
  rm -f "${output_file}" "${zip_file}"

  # zip the folder under its own directory name (keeps structure)
  (
    cd "${SKILLS_ROOT}"
    zip -r -q "../${output_file}" "${skill_name}" \
      -x '*/.DS_Store' \
      -x '*/__pycache__/*' \
      -x '*.pyc' \
      -x '*/.pytest_cache/*'
  )

  # same archive, .zip extension — for platforms that reject .skill
  cp "${output_file}" "${zip_file}"

  built+=("${output_file}" "${zip_file}")
done

echo
echo "Created:"
for f in "${built[@]}"; do
  echo "  ${f} ($(du -h "${f}" | cut -f1))"
done
