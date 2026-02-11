# L-ZIP VS Code Integration Guide

**Version:** 1.0.0  
**Author:** ezixen  
**Status:** Direct API & CLI Available | MCP Integration Planned

---

## Installation & Setup

### Step 1: Install L-ZIP

```bash
cd l-zip
pip install -r requirements.txt
```

### Step 2: Configure VS Code

1. Open VS Code Settings (JSON):
   - Press `Ctrl+Shift+P`
   - Type: "Preferences: Open User Settings (JSON)"
   - Press Enter

2. Add Java JDK configuration:

```json
{
  "java.jdt.ls.java.home": "C:\\Program Files\\Eclipse Adoptium\\jdk-21.0.10.7-hotspot"
}
```

### Step 3: Install L-ZIP VS Code Extension

Load the local extension for status bar + token estimator:

1. Open VS Code
2. Press `Ctrl+Shift+P` → "Extensions: Install from VSIX"
3. Navigate to `vscode-extension/` folder
4. Select the extension

---

## Core Usage Methods

### Method A: CLI Interface

Interactive command-line tool for L-ZIP operations:

```bash
python cli.py
```

**Available commands:**
```
compress    - Translate English to L-ZIP
expand      - Translate L-ZIP back to English
batch       - Compress multiple prompts
dict        - Show L-ZIP operators
templates   - Show example templates
demo        - Run interactive demo
help        - Show all commands
```

**Example:**
```
lzip> compress
Enter English prompt (or 'cancel' to abort):
> Write a Python function that validates email addresses

L-ZIP Translation:
ACT:Dev [Lang:Python] OBJ:Email_Validator GEN:Function OUT:Code+Tests
```

### Method B: Python API

Use L-ZIP directly in your Python code:

```python
from lzip import LZIPTranslator

translator = LZIPTranslator()

# Translate to L-ZIP
english = "Please write a Python script that processes CSV files"
lzip_prompt, stats = translator.translate_to_lzip(english)

print(f"L-ZIP: {lzip_prompt}")
print(f"Token Savings: {stats['compression_ratio']}%")

# Expand back to English
expanded, _ = translator.translate_from_lzip(lzip_prompt)
print(f"Expanded: {expanded}")
```

### Method C: VS Code Extension

Built-in status bar tools for token estimation:

1. **L-ZIP MCP Toggle** - Shows enabled/disabled status
2. **L-ZIP Estimator** - Enter prompts to see compression

---

## VS Code Snippets

Pre-built templates for quick prompting:

| Snippet | Command | Purpose |
|---------|---------|----------|
| `lzip-func` | Snippet autocomplete | Generate function |
| `lzip-review` | Snippet autocomplete | Code review |
| `lzip-fix` | Snippet autocomplete | Debug & fix |
| `lzip-test` | Snippet autocomplete | Create tests |
| `lzip-docs` | Snippet autocomplete | Write docs |
| `lzip-refactor` | Snippet autocomplete | Refactor code |
| `lzip-optimize` | Snippet autocomplete | Optimize perf |
| `lzip-types` | Snippet autocomplete | Add type hints |
| `lzip-api` | Snippet autocomplete | API endpoint |
| `lzip-class` | Snippet autocomplete | Design class |
| `lzip-db` | Snippet autocomplete | Database model |
| `lzip-error` | Snippet autocomplete | Error handling |

**Installation:**
1. Copy `.vscode/python.json`
2. Paste into `%APPDATA%\Code\User\snippets\python.json`
3. Restart VS Code
4. Type any `lzip-*` to autocomplete

---

## Usage Examples

### Example 1: Function Generation

**Step 1: Create L-ZIP prompt**
```
ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON GEN:Function OUT:Code+Docstring+Tests
```

**Step 2: Use with your AI tool of choice**
- Paste into ChatGPT, Claude, Gemini, or any LLM
- Much more efficient than verbose English prompts

### Example 2: Code Review

```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review | Optimize
EVAL:Performance+Security+Readability OUT:Report+Suggestions
```

### Example 3: Bug Fixing

```
ACT:Debugger CTX:[Error_Log] OBJ:Fix_Bug 
THINK:RootCause+Prevention OUT:Solution+Explanation
```

---

## Troubleshooting

### Snippets Not Showing?

1. Check `.vscode/python.json` is in `%APPDATA%\Code\User\snippets\`
2. Restart VS Code completely
3. Verify file has `.json` extension

### Python Version Issues?

```powershell
python --version
# Should show 3.8 or higher
```

### Import Errors?

```powershell
cd d:\Dev\L-ZIP
python -c "from lzip import LZIPTranslator; print('✓ OK')"
```

---

## Future Enhancements

### Planned: Direct Language Model Integration

Future versions will include native integration with:
- **OpenAI GPT models** - Direct API calls for prompt compression
- **Anthropic Claude** - Stream L-ZIP translations via Claude API
- **Google Gemini** - Native compression as LLM feature
- **Open source LLMs** - Local model support with Ollama/LM Studio

This will eliminate the need to copy-paste L-ZIP prompts manually and provide real-time compression with streaming results.

### Architecture

```
┌─────────────────────────────────────────┐
│   User Input (English Prompt)           │
└────────────────┬────────────────────────┘
                 │
                 ↓
        ┌─────────────────┐
        │  L-ZIP Engine   │  (Current)
        └────────┬────────┘
                 │
                 ├─→ CLI Output
                 ├─→ Python API
                 ├─→ VS Code Extension
                 │
                 ↓
        ┌──────────────────────────┐
        │  [Future] LLM Integration │
        │  - Auto compression      │
        │  - Streaming results     │
        │  - Multi-model support   │
        │  - Real-time preview     │
        └──────────────────────────┘
```

---

## Next Steps

1. ✅ Install L-ZIP package
2. ✅ Set up VS Code Java settings
3. ✅ Install L-ZIP extension
4. ✅ Try CLI: `python cli.py`
5. ✅ Try Python API with your own code
6. ✅ Use snippets in VS Code
7. ⏳ Future: Use native LLM integration when released

---

For more details:
- [README.md](README.md) - Overview & examples
- [MCP_INTEGRATION.md](MCP_INTEGRATION.md) - MCP protocol details
- [BEST_PRACTICES.md](BEST_PRACTICES.md) - Compression best practices

**Questions?** https://github.com/ezixen/l-zip/issues
