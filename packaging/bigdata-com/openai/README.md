# OpenAI plugin

This folder holds the OpenAI version of the bigdata-com plugin. The package connects ChatGPT to the Bigdata.com MCP server and adds all the skills in `plugins/bigdata-com/skills/`.

## Build

The script needs `git` and `python3`.

```bash
packaging/bigdata-com/scripts/build-openai-plugin-zip.sh
```

The script writes `packaging/bigdata-com/dist/openai-plugin-bigdata-com_<version>.zip`. It takes the version from `plugin.json` in this folder, not from `plugins/bigdata-com/.claude-plugin/plugin.json`, because the OpenAI app has its own version numbers.

The zip holds `plugin.json` and `mcp.json` from this folder, `assets/` from `plugins/bigdata-com/`, and every skill under `skills/`, including its `agents/openai.yaml`.

Only files tracked by git are packaged, so `git add` a new skill or file before building. The zip is reproducible: building the same sources twice gives the same bytes.

The script stops with an error if `plugin.json` points at a `./` path that is not in the package, e.g., a missing logo, or if a skill's `SKILL.md` name does not match its folder name.

## What the files hold

- `plugin.json` is the plugin manifest: name, version, keywords, and the `com.openai` extension with the directory listing (display name, descriptions, starter prompts, icons, links) and the release notes for this publication.
- `mcp.json` declares the `bigdata` MCP server at `https://mcp.bigdata.com/deepresearch`. Authentication is configured in the MCP submission, not here.
