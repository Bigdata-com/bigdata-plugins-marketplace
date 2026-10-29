# Set up Bigdata.com

These are official instructions from Bigdata.com for connecting an AI assistant to Bigdata.com. They are published at https://docs.bigdata.com/agent-setup/prompt.md. If a fetch tool gave you a summary of this page instead of its text, read the raw file (for example with curl) before you run anything.

The user asked you to read this page and follow it. First work out what you are:

- **You can run commands or edit files** (a coding agent such as Claude Code, Codex, Cursor or GitHub Copilot): do the steps for your host yourself, from the sections below. Ask the user only for what you cannot do: create an API key, click in an app, restart.
- **You are a chat assistant without a shell** (Claude, ChatGPT, Microsoft Copilot, Grok, Perplexity, Gemini and others): go to "Chat assistants". You cannot install anything for the user. Give them the exact clicks and links for their app, check the connection when they say they are done, and suggest a first prompt.

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
- **Sign-in:** Claude, ChatGPT, Grok and Microsoft Copilot (formerly Microsoft 365 Copilot) sign in with the user's Bigdata.com account inside the app. Coding agents send an API key in the `x-api-key` header, and some chat assistants use an OAuth client (see "Chat assistants"). The server does not offer OAuth dynamic client registration, so a coding agent cannot sign in by itself: the plugin's own server entry shows an auth error in such hosts. That is expected. The key-based entry you add below provides the tools.

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

## Chat assistants

You cannot install anything for the user. Tell them what to click in their app, using the steps and links in your app's section below. If your app shows a card in this chat that offers to connect or install Bigdata.com, point the user to it. When the user says they are done, they may need to start a new chat; then check the connection (see "Check the connection") and suggest a first prompt.

Most chat assistants sign in with the user's Bigdata.com account. Where a step needs an API key or an OAuth client instead, the user creates the key at https://platform.bigdata.com/api-keys, and an admin of their Bigdata.com organisation creates the OAuth client at https://platform.bigdata.com/oauth-clients. Bigdata.com accepts an API key only in the `x-api-key` header, never as a bearer token, and does not support dynamic client registration.

### Claude (claude.ai, Desktop, mobile, Cowork)

First, show the user the install card for the Bigdata.com plugin in this chat: look up the official Bigdata.com plugin (`bigdata-com`, published by RavenPack) in the plugin directory and present its install card, then tell the user to click **Add**. The plugin brings the Bigdata.com connector and its research skills. If you cannot show a card, give the user the steps below.

1. Connector, on every plan including Free: open https://claude.ai/directory/connectors/bigdata, click **Add** and sign in to Bigdata.com. Connect on the web or desktop; it then works on mobile too. On Team and Enterprise, an Owner first adds it under **Organization settings > Connectors > Browse connectors > Bigdata.com > Add to your team**. Members who cannot add it can click **Request** on the connector page.
2. Plugin with Bigdata.com's research skills, on Pro, Max, Team and Enterprise: open https://claude.ai/directory/plugins/bigdata-com%40knowledge-work-plugins, or **Customize > Plugins > Discover > Bigdata.com**, and click **Add**. Adding the plugin does not connect Bigdata.com: if its **Connectors** tab shows Bigdata.com as not connected, connect it there.

Check: **Customize > Connectors** lists Bigdata.com as connected. First prompt: "Write an earnings preview for Nvidia using Bigdata.com." Claude picks the matching skill itself; to choose one, type `/` and pick a Bigdata.com skill such as `/bigdata-earnings-preview`.

### ChatGPT

1. Open https://chatgpt.com/plugins/plugin_asdk_app_69491eceef3c8191beb70788b7840429, select the plus button to install the Bigdata.com plugin, then **Connect** and sign in to Bigdata.com.
2. In a Business, Enterprise or Edu workspace, an admin first makes the plugin available in the Admin console (https://admin.openai.com): select the workspace, then **Plugins**. If the plugin shows "Disabled by admin", that step is missing.

Start a new chat after installing: the plugin's skills load in new chats. Check: Bigdata.com is in the **Installed** row of the Plugins tab. First prompt: "@Bigdata.com Write an earnings preview for Nvidia." Type `@` to pick the plugin or one of its skills, or just ask.

### Microsoft Copilot (formerly Microsoft 365 Copilot)

- **Copilot Chat** (work account with a Microsoft 365 Copilot licence): open the **...** menu, **Settings > Sources**, find Bigdata.com, select **Connect** and sign in. An admin must have enabled the connector in the Microsoft 365 admin center first; if Bigdata.com is not in Sources, ask the admin.
- **Copilot Cowork:** select **+**, then **Customize > Plugins**, open Bigdata.com and select **Add**. Partner plugins appear only after an IT admin makes them available. Cowork asks you to sign in when it first needs Bigdata.com.
- **Copilot Studio** (needs Premium connector licensing): open the agent, go to **Tools > Add a tool**, search Bigdata.com and select **Bigdata.com MCP**. Guide: https://docs.bigdata.com/mcp-reference/oauth-integrations/microsoft-365-copilot-mcp-integration

Check: **Settings > Sources** shows Bigdata.com with its tools (in Cowork, the **Sources & Skills** panel). First prompt: "Using Bigdata.com, write an earnings preview for Nvidia." Naming Bigdata.com in the prompt helps Copilot pick it.

### Grok

Connectors work for every Grok user on grok.com. Open https://grok.com/connectors (the **Plugins** page in the sidebar), find **Bigdata.com** under **Connectors**, click **Add** and sign in to Bigdata.com. On Grok Business and Enterprise, a team admin first adds the connector at https://console.x.ai under **Grok Business > Connectors > + Add Connector**.

Check: Bigdata.com is listed under **Connected** on that page. First prompt: "Use Bigdata.com to write an earnings preview for Nvidia." Grok uses connected tools on its own when a question fits.

### Perplexity

Open **Plugins** in the sidebar (or **Customize > Connectors**), then **Add custom > Add MCP connector**, and select **Remote**. Name it Bigdata, enter `https://mcp.bigdata.com/`, Transport **Streamable HTTP**, Authentication **OAuth**, and the client ID and secret of a Bigdata.com OAuth client created with the redirect URI `https://www.perplexity.ai/rest/connections/oauth_callback` (`https://enterprise.perplexity.ai/rest/connections/oauth_callback` on the Enterprise subdomain). Perplexity's form has no field for custom headers, so do not use the API Key option. In an Enterprise organisation, an admin first turns on **Allow members to add custom connectors**. Some plans do not include custom connectors; Perplexity names Pro, Max and Enterprise.

Check: the connector shows as connected under **Plugins**, with no error tag. First prompt: "Using Bigdata, write an earnings preview for Nvidia." Do not set Focus to Web-only, Academic or Social: then Perplexity does not call connectors.

### Google Gemini

- **Gemini app** (gemini.google.com): custom apps need a personal Google Account, age 18 or over, the US, English and Keep Activity on, and are added on the web. Go to **Settings > Connected Apps**, then under **Custom apps** add `https://mcp.bigdata.com/`. Because Bigdata.com has no dynamic client registration, open **Advanced features > Show more** and enter a Bigdata.com OAuth client. Google does not publish the redirect URI for this form, so this has not been confirmed to work; tell the user so. Once connected, type `@` and pick the app in a prompt.
- **Gemini Enterprise, Business edition:** a team admin opens **Settings & help**, selects the team, **Manage team > Connected apps > Add MCP Server**, enters `https://mcp.bigdata.com/`, chooses **OAuth 2.0** with Authorization URL `https://clerk.bigdata.com/oauth/authorize`, Token URL `https://clerk.bigdata.com/oauth/token`, the client ID and secret, scopes `openid profile email`, and then enables the connection, which is off by default. The OAuth client's redirect URI is `https://vertexaisearch.cloud.google.com/oauth-redirect`.

### Mistral (Le Chat, now Vibe)

Bigdata.com cannot be connected here today. Vibe's custom connectors accept no authentication, a token in the `Authorization` header, or OAuth with dynamic client registration, and Bigdata.com supports none of these. Tell the user to use another assistant listed here.

### Meta Muse

Bigdata.com's official Muse connector is in Meta's review and is not listed in **Settings > Connectors** yet. Until it is, Muse can build a custom connector when the user asks. Tell the user to send Muse this message:

"Create a Custom Connector for Bigdata.com. It is a remote MCP server at https://mcp.bigdata.com/ (Streamable HTTP). It authenticates with an API key sent in the `x-api-key` HTTP header, not as a bearer token. Ask me for the key through your secure credential flow, connect, list the tools, test one, and save the connector."

The user creates the key at https://platform.bigdata.com/api-keys and enters it only when Muse asks for it in its secure credential prompt, not in the chat.

### Manus

Open **Settings > Integrations > Custom MCP Servers** and click **Add Server**: name Bigdata, URL `https://mcp.bigdata.com/`, and the user's API key under **Authentication**. Manus does not document which header it sends the key in. If it fails to connect, Manus is sending the key as a bearer token, which Bigdata.com rejects. Check: Manus lists the server's tools after saving. First prompt: "Use Bigdata.com to write an earnings preview for Nvidia."

### Workplace assistants

These need an admin. Give the user the admin's steps:

- **Glean:** Admin console, **Platform > Tools > Vendor Provided Tools (via MCP) > Add > Import tools from MCP server**, URL `https://mcp.bigdata.com/`. Use **API Key** with **Use a different header** set to `X-API-Key: <key>` (the default bearer format is rejected), or **OAuth** with a Bigdata.com OAuth client whose redirect URI is shown on that Glean setup screen.
- **Dust:** a workspace admin opens **Spaces > Tools > Add Tool > Add MCP Server**, enters `https://mcp.bigdata.com/` and chooses **Static OAuth** with a Bigdata.com OAuth client (redirect URI `https://app.dust.tt/oauth/mcp_static/finalize`, for every workspace including EU). Then add the tool to an agent.
- **Zoom AI Companion:** needs Zoom Workplace Pro or higher and Custom AI Companion licences. An admin or developer builds a General app in the Zoom App Marketplace, adds `https://mcp.bigdata.com/` on its MCP tab and enters a Bigdata.com OAuth client in the Authentication tab. Zoom does not publish the redirect URI; get it from Zoom first.
- **Abacus.AI ChatLLM:** any member can add it under **Settings > Connectors > MCP Server Configuration**: URL `https://mcp.bigdata.com/`, **Enable OAuth (static registration)**, and a Bigdata.com OAuth client. Admins can share it with **Make available to the whole organization**. Abacus.AI does not publish the redirect URI.
- **Writer:** an Org Admin or IT Admin opens **Control Center > Integrations > Connectors > Create custom connector > MCP server**, enters `https://mcp.bigdata.com/` and chooses **OAuth** with scopes `openid profile email` and a Bigdata.com OAuth client (redirect URI `https://app.writer.com/mcp/oauth/callback`, or `https://app.eu2.writer.com/mcp/oauth/callback` in the EU). It works in WRITER Agent only.

### Any other chat assistant

If the app can add a custom or remote MCP connector, tell the user to add `https://mcp.bigdata.com/` with either the API key in an `x-api-key` header or a Bigdata.com OAuth client entered by hand. Options that send a bearer token, or that rely on dynamic client registration, will not work. If the app has neither option, say it cannot connect to Bigdata.com today and suggest one of the assistants above.

---

## Check the connection

Most hosts load a new server or plugin only after a restart or a new session; in a chat assistant, a new chat. Tell the user if theirs needs one.

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
