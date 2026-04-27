# Architecture Documentation

## High-Level Components
- Core translator: ../lzip.py
- CLI entrypoints: ../cli.py, ../cli_noui.py, ../cli_only.py
- GUI app: ../gui.py
- MCP adapters: ../mcp_server.py, ../mcp_stdio_server.py
- Extended operators: ../lzip_extended_operators.py

## Runtime Flows
### GUI Flow
1. User inputs text/paste/open file
2. Input is sanitized
3. Translator compresses prompt
4. Output shown and optionally copied to clipboard

### CLI Flow
1. Input from args/stdin/interactive
2. Translation through core engine
3. Stats + compressed output emitted
4. Clipboard copy where enabled

### MCP Flow
1. Client request arrives via stdio or server endpoint
2. Action routed to translator
3. Structured response returned with result and metadata

## Build/Release Layout
- Specs: ../build_exe.spec, ../build_cli_standalone.spec
- Built outputs: ../builds/
- Release binaries: ../releases/

## Extension Surface
- VS Code extension source: ../vscode-extension/
- Browser extension source: ../browser-extension/ (development status documented in ../BROWSER_EXTENSIONS_DEV.md)

## Quality and Operations
- Security policy: ../SECURITY.md
- Contribution guide: ../CONTRIBUTING.md
- Changelog: ../CHANGELOG.md
