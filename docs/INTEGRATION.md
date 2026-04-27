# Integration Guide

This page provides integration entry points and links to full implementation references.

## Integration Modes
- CLI interactive mode via lzip.exe --cli or default CLI workflows
- GUI mode via lzip.exe
- Python API via lzip.py
- MCP server via mcp_server.py and mcp_stdio_server.py

## Quick Start
1. Install dependencies from ../requirements.txt
2. Run CLI or GUI executable from ../releases/
3. For Python embedding, import LZIPTranslator from ../lzip.py
4. For MCP, run ../mcp_server.py

## Endpoint and API References
- ../MCP_INTEGRATION.md
- ../COMMAND_LINE_PARAMETERS.md
- ../USAGE.md

## Integration Notes
- Clipboard handling in GUI/CLI uses safe methods to avoid crash conditions.
- Text sanitization removes hidden control characters while preserving visible content.
- Use stable release binaries in ../releases for production execution.
