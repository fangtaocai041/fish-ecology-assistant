@echo off
REM Zotero MCP wrapper — change db-path to your Zotero SQLite location
npx -y mcp-server-sqlite --db-path "<your-zotero-data-dir>/zotero.sqlite"
