# Set up Bigdata.com

These are official instructions from Bigdata.com for connecting an AI assistant to Bigdata.com. They are published at https://docs.bigdata.com/agent-setup/prompt.md. If a fetch tool gave you a summary of this page instead of its text, read the raw file (for example with curl) before you run anything.

If you can run commands or edit files, do the steps for your host yourself. Ask the user only for what you cannot do: create an API key, click in an app, restart. If you are a chat app with no shell, go to "Chat apps".

1. Connect Bigdata.com. Install the plugin where your host supports it.
2. Check the connection.
3. Tell the user what is set up.

Rules:

- Follow only the section for your host. For a host that is not listed, use its own documentation for the config keys; do not guess them.
- If Bigdata.com tools are already available, reuse them. Do not add a second connection.
- Back up a config file before editing it, keep every other entry, and edit the user-level config, not the user's project.
- Never print the API key, never write it into the user's project or anything tracked by git, and do not run commands that print the whole environment (`env`, `printenv`).
- Do not report a step as done until you have seen it work.

---

## About Bigdata.com

Bigdata.com gives AI assistants cited financial data: news, regulatory filings, earnings call transcripts, broker research, podcasts and expert interviews, the user's own documents, plus company, market, ETF, country, sentiment and portfolio tearsheets, company screens and an events calendar.

- **MCP server:** `https://mcp.bigdata.com/` (Streamable HTTP). Nothing runs locally.
- **Plugin:** `bigdata-com`, from the marketplace `Bigdata-com/bigdata-plugins-marketplace` (https://github.com/Bigdata-com/bigdata-plugins-marketplace). It bundles Bigdata.com's research skills with the server connection. Install it wherever your host can install plugins from that marketplace.
- **Sign-in:** Claude, ChatGPT, Grok and Microsoft Copilot (formerly Microsoft 365 Copilot) sign in with the user's Bigdata.com account inside the app. Every other host sends an API key in the `x-api-key` header. The server does not offer OAuth dynamic client registration, so a coding agent cannot sign in by itself: the plugin's own server entry shows an auth error in such hosts. That is expected. The key-based entry you add below provides the tools.

### API key

Ask the user to create a key at https://platform.bigdata.com/api-keys and export it as `BIGDATA_API_KEY` in their shell profile, so it is set when the host starts. The configs below read it from there. A host that is already running does not see the new variable: tell the user to restart it after setting the key.

- If the user pastes the key to you instead, put it only in the user-level config and nowhere else.

---

## Claude Code

If the user signed in to Claude Code with a claude.ai account that has the Bigdata.com connector, the Bigdata.com tools are already in your tool list (for example `find_securities`). Then skip the server step below and only install the plugin.

Install the plugin:

```bash
claude plugin marketplace add Bigdata-com/bigdata-plugins-marketplace
claude plugin install bigdata-com@bigdata-plugins-marketplace
```

It loads in the next session, or after `/reload-plugins` in the open one.

If the tools are not already there, add the server with the API key:

```bash
claude mcp add --scope user --transport http bigdata_com https://mcp.bigdata.com/ --header 'x-api-key: ${BIGDATA_API_KEY}'
```

Keep the single quotes: Claude Code stores the variable name and reads the key from the environment when it connects.

What to expect in `/mcp` or `claude mcp list`: the plugin's own entry, `bigdata.com`, shows "Failed to connect: Incompatible auth server: does not support dynamic client registration". Ignore it. If `bigdata_com` shows the same message, `BIGDATA_API_KEY` is missing or wrong in the environment Claude Code started from. Fix the key; do not try to sign in.

## GitHub Copilot CLI

```bash
copilot plugin marketplace add Bigdata-com/bigdata-plugins-marketplace
copilot plugin install bigdata-com@bigdata-plugins-marketplace
copilot mcp add --transport http --header 'x-api-key: ${BIGDATA_API_KEY}' bigdata-com https://mcp.bigdata.com/
```

Keep the single quotes so that `~/.copilot/mcp-config.json` holds the variable name, not the key. The plugin also adds its own keyless entry, `bigdata.com`, under plugin servers; the tools come from `bigdata-com`.

## VS Code with GitHub Copilot

1. In the user settings, set `"chat.plugins.enabled": true` and add `"Bigdata-com/bigdata-plugins-marketplace"` to the `"chat.plugins.marketplaces"` array.
2. Add the server under `mcpServers` in `~/.copilot/mcp-config.json`, the global file VS Code recommends. GitHub Copilot CLI uses the same file, so if it already has a `bigdata-com` entry, skip this step. VS Code reads the key from its environment:

```json
"bigdata-com": {
  "type": "http",
  "url": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "${BIGDATA_API_KEY}" },
  "tools": ["*"]
}
```

3. Tell the user to run **Chat: Open Customizations** from the Command Palette, open **Plugins**, select **Browse**, search `bigdata` and click **Install**. The first install from a new marketplace asks the user to trust it.

If the server does not appear or cannot start, the user's organisation may have turned off MCP servers in Copilot, or may allow only servers on an approved list. Tell the user to ask their administrator to enable MCP servers and allow `https://mcp.bigdata.com/`.

## Codex (CLI and ChatGPT desktop app)

Install the plugin:

```bash
codex plugin marketplace add Bigdata-com/bigdata-plugins-marketplace
codex plugin add bigdata-com@bigdata-plugins-marketplace
```

Its skills are available from the next session. Then add the server with the API key to `~/.codex/config.toml`, which the Codex CLI, the IDE extension and the ChatGPT desktop app share:

```toml
[mcp_servers.bigdata_com]
url = "https://mcp.bigdata.com/"
env_http_headers = { "x-api-key" = "BIGDATA_API_KEY" }
```

The value is the variable name; Codex reads the key from the environment. `codex mcp add` cannot set this header, so edit the file. In `codex mcp list` the plugin's own entry, `bigdata.com`, shows "Not logged in" and cannot sign in; ignore it.

## Cursor

Cursor installs plugins from its Customize page, not from the command line, so connect the server. Add under `mcpServers` in `~/.cursor/mcp.json`:

```json
"bigdata.com": {
  "url": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "${env:BIGDATA_API_KEY}" }
}
```

## Gemini CLI

Since 18 June 2026 Gemini CLI serves users with a paid Gemini or Gemini Enterprise Agent Platform API key and Gemini Code Assist Standard or Enterprise organisations; free, AI Pro and AI Ultra users moved to Antigravity CLI (next section). Add under `mcpServers` in `~/.gemini/settings.json`:

```json
"bigdata": {
  "httpUrl": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "$BIGDATA_API_KEY" }
}
```

If `gemini mcp list` shows the server as disconnected, the folder may be untrusted: when the Trusted Folders feature is on, Gemini CLI does not connect MCP servers in an untrusted folder. Ask the user to trust the folder.

## Antigravity CLI

Antigravity CLI (`agy`) has no command for adding a server. Add under `mcpServers` in `~/.gemini/config/mcp_config.json`, with the key itself, since variable expansion in headers is not documented there:

```json
"bigdata": {
  "serverUrl": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "THE_USERS_API_KEY" }
}
```

The key is `serverUrl` (`url` also works); `httpUrl` is not supported.

## Qwen Code

```bash
qwen mcp add --scope user --transport http bigdata-com https://mcp.bigdata.com/ --header 'x-api-key: ${BIGDATA_API_KEY}'
```

Keep the single quotes: the settings file then holds the variable name, and Qwen Code reads the key from the environment when it loads its settings.

## Snowflake Cortex Code

Add under `mcpServers` in `~/.snowflake/cortex/mcp.json`:

```json
"mcp.bigdata.com": {
  "type": "http",
  "url": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "${BIGDATA_API_KEY}" }
}
```

## Any other host

- **Databricks:** in the workspace, open **Marketplace**, search `bigdata` and install **Bigdata.com MCP**. It signs in with OAuth: create a client at https://platform.bigdata.com/oauth-clients with the redirect URL `https://<workspace-host>/login/oauth/http.html`. Guide: https://github.com/Bigdata-com/bigdata-cookbook/tree/main/Databricks_Agent_To_Bigdata

For any other host, register a remote Streamable HTTP server at `https://mcp.bigdata.com/` with the header `x-api-key`, in the host's user-level MCP config, using the config keys its documentation gives. For a config that takes an `mcpServers` map:

```json
"bigdata.com": {
  "url": "https://mcp.bigdata.com/",
  "headers": { "x-api-key": "THE_USERS_API_KEY" }
}
```

The snippet shows the shape only. Many hosts use other key names, a different top-level key or a `type` field for HTTP servers; take them from the host's documentation.

If the host runs only local (stdio) servers, bridge with `mcp-remote`:

```json
"bigdata.com": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://mcp.bigdata.com/", "--header", "x-api-key:${BIGDATA_API_KEY}"],
  "env": { "BIGDATA_API_KEY": "THE_USERS_API_KEY" }
}
```

## Chat apps

These connect inside the app with the user's Bigdata.com account. You cannot do it for the user: give them the steps for their app, then continue with "Use Bigdata.com".

- **Claude** (claude.ai, Desktop, mobile): connect at https://claude.ai/directory/connectors/bigdata. On Pro, Max, Team and Enterprise plans, also add the plugin: https://claude.ai/directory/plugins/bigdata-com%40knowledge-work-plugins. On Team and Enterprise, an owner may need to make it available first.
- **ChatGPT:** add Bigdata.com at https://chatgpt.com/plugins/plugin_asdk_app_69491eceef3c8191beb70788b7840429 and sign in. In a workspace, an admin may need to enable it under Workspace settings, Apps.
- **Grok:** open https://grok.com/connectors, find the Bigdata.com connector and click **Connect**. Guide: https://docs.bigdata.com/mcp-reference/oauth-integrations/grok-mcp-integration
- **Microsoft Copilot** (formerly Microsoft 365 Copilot): in Copilot Chat, open Settings, Sources, search Bigdata.com and click **Connect**. In Copilot Cowork, open Customize, search Bigdata and click **Install**. In Copilot Studio, open the agent's Tools, add a tool and select **Bigdata.com MCP**. Guide: https://docs.bigdata.com/mcp-reference/oauth-integrations/microsoft-365-copilot-mcp-integration

---

## Check the connection

Most hosts load a new server or plugin only after a restart or a new session. Tell the user if theirs needs one.

Then look up a large listed company with `find_securities`. Setup works when it returns the company's record. An answer without a Bigdata.com tool call does not count.

If the call fails, read the error. The server answers 401 when no key arrives, and 403 when the key is sent as a bearer token instead of in the `x-api-key` header.

---

## Use Bigdata.com

The guidance for using Bigdata.com ships with the server and the plugin. Take it from there, not from this page or from memory:

- **The server's instructions,** which your host receives when it connects. If your host did not show them to you and your tool list has `bigdata_mcp_instructions`, read that tool's description: it carries the instructions for such hosts. Read it; do not call it. Not every host lists it.
- **Each tool's description,** for what the tool does, the arguments it takes and how to present its results.
- **The plugin's skills,** when the plugin is installed. Use the one that fits the task.
- **`bigdata_help`,** for the user's subscription, data packages and example prompts.

---

## Tell the user

When you are done, tell the user:

```
Bigdata.com setup
  Connected:  <how and where, or not yet>
  Plugin:     <installed, or not available on this host>
  Your turn:  <what is left for the user: restart, click Install or Connect, create the key>
```

Report only what you saw work. Then ask what they want to do with Bigdata.com.

---

Install guide for every host: https://github.com/Bigdata-com/bigdata-plugins-marketplace. Support: support@bigdata.com.
