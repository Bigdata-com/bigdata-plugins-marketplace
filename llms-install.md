# Installing the Bigdata.com MCP server

Bigdata.com is a remote MCP server. There is nothing to run locally.

Endpoint: `https://mcp.bigdata.com/` (Streamable HTTP).

Authentication, one of:

- API key: create one at https://platform.bigdata.com/api-keys and send it as the `x-api-key` header. Use this in Cline and any client that configures headers.
- OAuth (authorization code with PKCE): hosts with an official Bigdata.com connector, app or tool (Claude.ai and Claude Desktop, ChatGPT, Microsoft Copilot Studio) connect by signing in, without an API key.

Configuration for any client that takes an `mcpServers` map:

```json
{
  "mcpServers": {
    "bigdata.com": {
      "url": "https://mcp.bigdata.com/",
      "headers": { "x-api-key": "YOUR_API_KEY" }
    }
  }
}
```

Clients that only speak stdio can bridge with `mcp-remote`:

```json
{
  "mcpServers": {
    "bigdata.com": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.bigdata.com/", "--header", "x-api-key:${BIGDATA_API_KEY}"],
      "env": { "BIGDATA_API_KEY": "YOUR_API_KEY" }
    }
  }
}
```

Tools, grouped by job: cited search across news, filings, transcripts, research and private documents; company, security and entity lookup; company, country, market, ETF, sentiment and portfolio tearsheets; company screens and event calendars; private content connectors, tags, documents, fetch and upload. Read the current list from the server's `tools/list`; reference: https://docs.bigdata.com/mcp-reference/introduction#tools

Verify: ask the assistant for recent news on a listed company and check that the answer carries source citations.
