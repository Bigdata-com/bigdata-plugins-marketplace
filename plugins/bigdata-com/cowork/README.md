# Microsoft 365 Copilot Cowork plugin

This folder holds the Microsoft 365 Copilot Cowork version of the bigdata-com plugin. The package connects Cowork to the Bigdata.com MCP server and adds a selection of the skills in `../skills/`.

## Build

```bash
plugins/bigdata-com/scripts/build-cowork.sh
```

The script writes `plugins/bigdata-com/dist/cowork-plugin-bigdata-com_<version>.zip`. It takes the version from `.claude-plugin/plugin.json` and the skill list from `manifest.json`.

The script stops with an error if the package breaks a Cowork limit, e.g., more than 20 skills. It leaves out the files Cowork does not use: `README.md`, `agents/` and `.svg` files.

## Test

1. In Cowork, open Customize, then Plugins, and upload the zip.
2. Sign in to Bigdata.com when Cowork asks.
3. Ask for something that needs a tool and shows a widget, e.g., "Give me the Apple company tearsheet".

Cowork refuses an upload whose version is not higher than the installed one. Delete the installed plugin first, or raise the version in `.claude-plugin/plugin.json`.

## Change the skills

The `agentSkills` list in `manifest.json` decides which skills ship. Cowork allows at most 20 skills in one package. The build prints the skills in `../skills/` that the package leaves out, so you can see when a new skill is missing.

## What the manifest holds

- `id` is the app id. Keep it the same across versions, because Microsoft treats a new id as a different app.
- `mcpServerUrl` ends with a slash. It must match the base URL of the OAuth registration exactly, or Cowork shows a connector setup error.
- `referenceId` points to the OAuth registration in the Teams Developer Portal. It is an identifier, not a secret.
- `validDomains` lists the domains the MCP widgets load from. A widget that loads from a domain missing here is blocked.

The manifest uses schema version 1.30. From 1.29, Cowork does not need a tool list file, because it gets the tools from the MCP server.
