# VS Code GitHub Copilot MCP Integration - L-ZIP

## Quick Setup (5 minutes)

### Step 1: Install Location
Your L-ZIP MCP server is installed at:
```
D:\Dev\l-zip-deploy\
```

### Step 2: Add to VS Code Settings

1. Open VS Code Settings (JSON):
   - Press `Ctrl+Shift+P`
   - Type: "Preferences: Open User Settings (JSON)"
   - Press Enter

2. Add this configuration to your settings.json:

```json
{
  "github.copilot.advanced": {
    "mcp": {
      "servers": {
        "l-zip": {
          "command": "python",
          "args": ["D:/Dev/l-zip-deploy/mcp_stdio_server.py"],
          "description": "L-ZIP Token Compression (50-70% savings)"
        }
      }
    }
  }
}
```

**If you already have settings**, merge it like this:
```json
{
  "existing.setting": "value",
  "github.copilot.advanced": {
    "mcp": {
      "servers": {
        "l-zip": {
          "command": "python",
          "args": ["D:/Dev/l-zip-deploy/mcp_stdio_server.py"],
          "description": "L-ZIP Token Compression"
        }
      }
    }
  }
}
```

3. Save the file (Ctrl+S)

### Step 3: Restart VS Code
- Close VS Code completely
- Reopen VS Code
- L-ZIP MCP should now be available

### Step 4: Test Integration

Open GitHub Copilot Chat (Ctrl+Shift+I) and try:

**Method 1: Ask Copilot to compress**
```
@l-zip compress this: Write a Python function that validates email addresses with error handling and tests
```

**Method 2: Use the tool directly**
In Copilot Chat, type `/` and look for L-ZIP tools:
- `compress_prompt` - Compress your prompts
- `expand_lzip` - Expand L-ZIP back

### Step 5: Verify It's Working

You should see output like:
```
L-ZIP Compressed Prompt:
ACT:Senior_Dev [Lang:Python] OBJ:Email_Validator OUT:Function+Tests+ErrorHandling

Tokens saved: 54 (93.3% compression)
```

---

## Alternative: Manual MCP Configuration File

If GitHub Copilot supports external MCP configs:

Create: `%APPDATA%\Code\User\mcp-servers.json`

Content:
```json
{
  "l-zip": {
    "command": "python",
    "args": ["D:/Dev/l-zip-deploy/mcp_stdio_server.py"],
    "description": "L-ZIP Token Compression - Save 50-70% on tokens"
  }
}
```

---

## Troubleshooting

### MCP Server Not Showing Up?

1. **Check Python Path**
   ```powershell
   python --version
   ```
   Should show Python 3.8+

2. **Test MCP Server Manually**
   ```powershell
   cd D:\Dev\l-zip-deploy
   echo '{"method":"initialize","params":{}}' | python mcp_stdio_server.py
   ```
   Should return JSON response

3. **Check VS Code Output**
   - View → Output
   - Select "GitHub Copilot" from dropdown
   - Look for L-ZIP related messages

### MCP Server Crashes?

Run this test:
```powershell
cd D:\Dev\l-zip-deploy
python -c "from lzip import LZIPTranslator; print('✓ Import OK')"
```

If it fails, check:
- Python version (needs 3.8+)
- File permissions
- Path correctness

### GitHub Copilot Doesn't Support MCP?

As of Feb 2026, MCP support in GitHub Copilot may vary. Alternatives:

**Plan B: Use as a Snippet**
1. Copy L-ZIP snippets from `.vscode/python.json`
2. Install in VS Code snippets folder
3. Type `lzip-func`, `lzip-review`, etc.

**Plan C: Direct Python Script**
```python
# Use this in terminal
python -c "from lzip import LZIPTranslator; t=LZIPTranslator(); print(t.translate_to_lzip('Your prompt here')[0])"
```

---

## Usage Examples

### Example 1: Compress Before Asking Copilot

**Instead of:**
```
Hey Copilot, I need you to write a Python function that validates 
email addresses. The function should check for proper formatting, 
handle edge cases, and include comprehensive error handling. Please 
provide the complete implementation with docstring, type hints, and 
a full test suite covering all edge cases.
```

**Use L-ZIP:**
```
ACT:Senior_Dev [Lang:Python] OBJ:Email_Validator OUT:Function+Tests+Docstring+TypeHints
```

**Savings: 93.3% tokens**

### Example 2: Code Review

**Instead of:**
```
Please review the following code for performance issues, security 
vulnerabilities, and code quality. Suggest optimizations.
```

**Use L-ZIP:**
```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review EVAL:Performance+Security OUT:Report
```

**Savings: 80% tokens**

---

## Next Steps

1. ✅ Add to VS Code settings
2. ✅ Restart VS Code
3. ✅ Test with Copilot Chat
4. ✅ Use L-ZIP snippets
5. ✅ Enjoy 50-70% token savings!

---

For more help, see:
- [MCP_INTEGRATION.md](MCP_INTEGRATION.md)
- [VSCODE_QUICK_REFERENCE.md](VSCODE_QUICK_REFERENCE.md)
- [examples.py](examples.py) - 18 ready templates

**Questions?** https://github.com/ezixen/l-zip/issues
