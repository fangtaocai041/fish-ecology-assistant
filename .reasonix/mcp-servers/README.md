# MCP Servers

All MCP wrapper scripts and custom servers live here.

## Wrapper Scripts

| File | Type | Description |
|------|------|-------------|
| `tavily.bat` | npx | AI deep search (requires TAVILY_API_KEY) |
| `exa.bat` | npx | Semantic search (requires EXA_API_KEY) |
| `github.bat` | npx | GitHub API (requires GITHUB_TOKEN) |
| `rplay.bat` | uvx | R language environment (uvx + R) |
| `paddleocr.bat` | node | PaddleOCR AI Studio (primary OCR) |
| `ocr-fallback.bat` | node | Tesseract.js offline OCR (fallback) |

## Custom MCP Servers

| Path | Implementation | Dependencies |
|------|---------------|--------------|
| `paddleocr-server.mjs` | Node.js MCP → PaddleOCR REST API | Node.js built-in https |
| `zotero.bat` | npx | Zotero SQLite queries — configure db-path for your machine |
| `ocr-fallback/` | Node.js MCP → Tesseract.js offline OCR | npm: tesseract.js |

## Direct npx Services (no wrapper needed)

Registered directly in your Reasonix `config.json` → `mcp` array:

| Service | Command |
|---------|---------|
| `scholar` | `npx -y scholar-mcp` |
| `article` | `npx -y article-mcp` |
| `scholarly` | `npx -y scholarly-research-mcp` |
| `playwright` | `npx -y @playwright/mcp` |
| `thinking` | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| `coderunner` | `npx -y mcp-server-code-runner@latest` |

## Config Location

`%USERPROFILE%\.reasonix\config.json` → `mcp` array
