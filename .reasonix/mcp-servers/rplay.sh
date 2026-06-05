#!/bin/bash
# R Playground MCP — Linux/macOS
export RPLAYGROUND_MCP_SUPPORT_IMAGE_OUTPUT=True
export R_HOME="${R_HOME:-/usr/lib/R}"
export TMPDIR="${TMPDIR:-/tmp}"
uvx --python 3.13 rplayground-mcp
