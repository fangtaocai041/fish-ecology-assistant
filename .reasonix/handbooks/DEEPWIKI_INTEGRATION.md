# 🔗 DeepWiki Integration Analysis

> **Source**: [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) + [CognitionAI/deepwiki](https://github.com/CognitionAI/deepwiki)
> **Principle**: Adopt non-conflicting advanced features, adapt to our dual-core architecture.

---

## 1. DeepWiki Features — Adoption Assessment

| DeepWiki Feature | Compatible? | Action |
|-----------------|:----------:|--------|
| **Docker deployment** (Dockerfile + compose) | ✅ No conflict | Add Docker support to both projects |
| **Multi-LLM via litellm** | ✅ Aligns with P3 models.yaml | Already have multi-provider; add litellm as optional bridge |
| **MCP server for AI agents** | ✅ Complementary | Our projects ARE AI agents; can CONSUME deepwiki MCP as a knowledge source |
| **Auto-generated code docs** | ✅ Complementary | DeepWiki can generate docs FOR our projects |
| **Multi-language README (8+ langs)** | ⚠️ Partial | We have EN+ZH; expanding to more langs adds maintenance cost |
| **Next.js web UI** | ❌ Conflict | Our projects are CLI/agent-based, not web apps |
| **Auto-refresh via badge** | ✅ No conflict | Add deepwiki badge to README for auto-doc generation |
| **Visual code diagrams** | ✅ No conflict | Can consume as output, not build into our pipeline |

---

## 2. Features to Adopt

### 2.1 Docker Deployment

Add `Dockerfile` + `docker-compose.yml` to both projects for one-command deployment.

```dockerfile
# fish-ecology-assistant/Dockerfile
FROM node:22-alpine
WORKDIR /app
COPY .reasonix/ .reasonix/
COPY config/ config/
COPY package.json .
RUN npm install
CMD ["node", "node_modules/.reasonix/mcp-servers/ima-server.mjs"]
```

### 2.2 DeepWiki MCP as Knowledge Source

DeepWiki provides an MCP server (`https://mcp.deepwiki.com/sse`) with three tools:
- `ask_question` — Ask about any repo's codebase
- `read_wiki_structure` — Get wiki navigation tree
- `read_wiki_contents` — Get full wiki content

**Integration**: Add deepwiki MCP server to our `mcp_servers.yaml` as an optional knowledge source.

### 2.3 Multi-LLM Bridge (litellm)

DeepWiki uses litellm for provider abstraction. We already have P3 multi-provider in `models.yaml`. Add litellm as an optional Docker Compose service for local model support.

### 2.4 DeepWiki Badge

Add a badge to README that auto-generates documentation for our repos on deepwiki.com.

---

## 3. Features NOT to Adopt (conflict risk)

| Feature | Why Not |
|---------|--------|
| Next.js web UI | Our projects are agent/CLI-based, not web apps. Adding a web UI would conflict with the Reasonix Skills architecture |
| 8+ language READMEs | Maintenance burden. EN+ZH is sufficient for our domain (Chinese academia + international publishing) |
| Ollama local-only mode | Our projects are cloud-first (DeepSeek API). Local mode is a different use case |

---

## 4. Implementation Plan

| # | Feature | Files | Effort |
|:--|---------|-------|:------:|
| 1 | Docker support | `Dockerfile` + `docker-compose.yml` ×2 | 30 min |
| 2 | DeepWiki MCP | `mcp_servers.yaml` ×2 | 15 min |
| 3 | DeepWiki badge | `README.md` ×2 | 5 min |
| 4 | litellm bridge | `docker-compose-litellm.yml` ×2 | 15 min |

---

**Last updated: 2026-06-06**
