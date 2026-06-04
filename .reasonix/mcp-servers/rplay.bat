@echo off
REM R language MCP wrapper — adjust R_HOME, TMPDIR, and uvx path for your machine
set RPLAYGROUND_MCP_SUPPORT_IMAGE_OUTPUT=True
set R_HOME=C:\Program Files\R\R-4.6.0
set TMPDIR=%USERPROFILE%\R_temp
%USERPROFILE%\.local\bin\uvx.exe --python 3.13 rplayground-mcp
