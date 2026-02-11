# Changelog

All notable changes to the L-ZIP VS Code extension will be documented in this file.

## [0.0.1] - 2026-02-11

### Added
- Initial release of L-ZIP VS Code extension
- Status bar MCP toggle button with persistent state
- Token estimator with visual output panel
- One-click copy button for L-ZIP compressed prompts
- Context-aware prompt compression (40-70% token reduction)
- Extended operator detection (IMAGE, CODE, CONTENT domains)
- Symbol replacements for common phrases (`=>`, `|`, `+`, etc.)
- Number abbreviations (5000 → 5k, 1M, 1B)
- Time abbreviations (30m, 2h, 5d, etc.)
- Tech term shortcuts (img, vid, doc, db, etc.)
- Safe filler word removal (please, kindly, for me, etc.)
- Word boundary protection to prevent corrupting words
- Auto-detection of image quality, style, mood, lighting, aspect ratio
- Prominent L-ZIP translation display at top of output
- Token savings notification with copy option
- Integration with parent L-ZIP Python module
- Debug logging for troubleshooting

### Fixed
- Overly aggressive symbol replacements (removed ambiguous "for", "above", "except")
- Word corruption issues (e.g., "realistic" → "realis>c")
- False positive replacements in wrong contexts
- Extension activation on startup
- Problem matcher for watch task
- Python module path resolution from vscode-extension subdirectory

### Technical Details
- Pure JavaScript implementation (no TypeScript compilation needed)
- Uses Node.js child_process for Python execution
- Conservative compression mode by default
- Configurable via VS Code settings
- Activates on startup (`onStartupFinished`)
- Supports both local and remote workspaces

### Known Limitations
- Requires Python 3.8+ installed
- Python path must be configured if not in system PATH
- Compression quality depends on L-ZIP Python module version
- Large prompts (>5000 tokens) may take 1-2 seconds to process

### Coming Soon (v0.1.0)
- ML-based context understanding with SmolLM-135M
- Batch processing for multiple prompts
- Custom compression rules per workspace
- Direct language model API integration (OpenAI, Claude, Gemini)
- Offline mode with cached translations
- Performance optimizations
- Compression level slider (conservative/balanced/aggressive)

---

## Future Versions

### [0.1.0] - Planned
- **Smart Compression:** ML model for context-aware compression
- **Batch Mode:** Process multiple prompts at once
- **Custom Rules:** Workspace-specific compression preferences
- **LLM Integration:** Direct language model support (OpenAI, Claude, Gemini)

### [0.2.0] - Planned
- **Templates:** Pre-built L-ZIP templates for common tasks
- **Snippets:** Code snippets for L-ZIP operators
- **Syntax Highlighting:** L-ZIP syntax highlighting in editors
- **Marketplace:** Share and download community compression rules

---

**Note:** This extension is part of the larger L-ZIP project aimed at reducing AI token consumption and carbon footprint.
