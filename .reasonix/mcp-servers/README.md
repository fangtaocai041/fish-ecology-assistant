# MCP Servers — 统一目录

所有 MCP 包装脚本和自定义服务器都在这里。

## 包装脚本（批处理 + 子目录）

| 文件 | 类型 | 说明 |
|------|------|------|
| `tavily.bat` | npx | 🔍 AI 深度搜索（含 TAVILY_API_KEY） |
| `exa.bat` | npx | 🧠 语义搜索（含 EXA_API_KEY） |
| `github.bat` | npx | 🐙 GitHub API（含 GITHUB_TOKEN） |
| `rplay.bat` | uvx | 📊 R 语言环境（uvx + R 4.6.0） |
| `paddleocr.bat` | node | 🖼️ PaddleOCR AI Studio（主 OCR） |
| `ocr-fallback.bat` | node | 🖼️ Tesseract.js 离线 OCR（备选） |

## 自定义 MCP 服务器

| 目录/文件 | 实现 | 依赖 |
|----------|------|------|
| `paddleocr-server.mjs` | Node.js MCP → PaddleOCR REST API | node 内置 https 模块 |
| `zotero.bat` | npx | 📚 Zotero SQLite 查询 — 指向 D:\ZoteroData |
| `ocr-fallback/` | Node.js MCP → Tesseract.js 离线 OCR | npm: tesseract.js |

## 无包装脚本（直接注册在 config.json）

| 服务名 | 命令 |
|-------|------|
| `scholar` | `npx -y scholar-mcp` |
| `article` | `npx -y article-mcp` |
| `scholarly` | `npx -y scholarly-research-mcp` |
| `playwright` | `npx -y @playwright/mcp` |
| `thinking` | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| `coderunner` | `npx -y mcp-server-code-runner@latest` |

## 配置文件位置

`C:\Users\小陶\.reasonix\config.json` → `mcp` 数组
