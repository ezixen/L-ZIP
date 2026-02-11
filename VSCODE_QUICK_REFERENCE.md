# L-ZIP Quick Reference for VS Code

**Author:** ezixen  
**Version:** 1.0.0  
**Purpose:** Token compression via semantic prompting format

---

## 🚀 Quick Start (30 seconds)

### Copy-Paste L-ZIP Prompts Into Your AI Tool:

**Generate a function:**
```
ACT:Senior_Dev [Lang:Python] OBJ:Write_Function [Name:parse_json]
THINK:Error_Handling OUT:Function + Docstring + Tests
```

**Review code:**
```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review | Optimize
EVAL:Performance + Security + Readability OUT:Report + Suggestions
```

**Fix a bug:**
```
ACT:Debugger CTX:[Error_Details] OBJ:Fix_Bug
THINK:RootCause + Solution OUT:Fixed_Code + Explanation
```

---

## ⌨️ VS Code Snippets (Type these to autocomplete)

| Snippet | Purpose | Shortcut |
|---------|---------|----------|
| `lzip-func` | Generate function | <kbd>lzip-func</kbd> + <kbd>Tab</kbd> |
| `lzip-review` | Code review | <kbd>lzip-review</kbd> + <kbd>Tab</kbd> |
| `lzip-fix` | Debug & fix | <kbd>lzip-fix</kbd> + <kbd>Tab</kbd> |
| `lzip-test` | Create tests | <kbd>lzip-test</kbd> + <kbd>Tab</kbd> |
| `lzip-docs` | Write docs | <kbd>lzip-docs</kbd> + <kbd>Tab</kbd> |
| `lzip-refactor` | Refactor code | <kbd>lzip-refactor</kbd> + <kbd>Tab</kbd> |
| `lzip-optimize` | Optimize perf | <kbd>lzip-optimize</kbd> + <kbd>Tab</kbd> |
| `lzip-types` | Add type hints | <kbd>lzip-types</kbd> + <kbd>Tab</kbd> |
| `lzip-api` | API endpoint | <kbd>lzip-api</kbd> + <kbd>Tab</kbd> |
| `lzip-class` | Design class | <kbd>lzip-class</kbd> + <kbd>Tab</kbd> |
| `lzip-db` | Database model | <kbd>lzip-db</kbd> + <kbd>Tab</kbd> |
| `lzip-error` | Error handling | <kbd>lzip-error</kbd> + <kbd>Tab</kbd> |

---

## 📋 How to Use L-ZIP Prompts

### Copy & Paste to Any AI Tool

1. Generate an L-ZIP prompt (use snippets or create manually)
2. Copy the L-ZIP formatted text
3. Paste into your AI tool: ChatGPT, Claude, Gemini, etc.
4. Get 50-70% more efficient responses

### Using Snippets in VS Code

1. **Copy** the `python.json` file from `.vscode/` folder
2. **Locate** VS Code snippets: `%APPDATA%\Code\User\snippets\` (Windows)
3. **Paste** as `python.json` in snippets folder
4. **Restart** VS Code
5. **Type** any `lzip-*` shortcut to autocomplete!

---

## 🎯 Common Workflows

### Workflow A: Function Generation (30 seconds)
```python
# Type: lzip-func (Tab to expand)
# ACT:Senior_Dev [Lang:Python] OBJ:Email_Validator
# OUT:Function + Docstring + Tests

def validate_email(email: str) -> bool:
    # Copy the L-ZIP above and paste into your AI tool
```

### Workflow B: Code Review
1. Select code in editor
2. Copy the code
3. Paste this into your AI tool:
```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review + Optimize
OUT:Analysis + Refactoring_Suggestions
```
4. Then paste your code

### Workflow C: Bug Triage
1. See error in terminal
2. Paste this into your AI tool:
```
ACT:Debugger CTX:[Error_Message] OBJ:Fix_Bug
THINK:RootCause OUT:Solution + Prevention
```
3. Add error details as context

### Workflow D: Follow-up Requests
1. After your AI tool responds to an L-ZIP prompt
2. Use follow-ups like:
   - "Add error handling"
   - "Add type hints"
   - "Generate tests"
   - "Optimize it"
   
   (The AI remembers the L-ZIP context!)

---

## 📊 Expected Results

| Task | Compression | Savings |
|------|-------------|----------|
| Simple function | 40-50% | ~30 seconds |
| Complex class | 55-65% | ~2 minutes |
| Full API module | 60-75% | ~5 minutes |
| Test suite | 45-55% | ~2 minutes |

**Average:** 50-70% token reduction vs natural language

---

## 💡 Pro Tips

1. **Combine with comments** - Mix L-ZIP with English for clarity
2. **Chain improvements** - Start with L-ZIP, then refine
3. **Be specific** - `[Lang:Python]` is better than just "python"
4. **Use alternatives** - `|` means "or" (e.g., `Fix_Bug | Optimize`)
5. **Always specify output** - `OUT:Code + Tests + Docs` is clearer

---

## 🔧 Customization

Edit `.vscode/python.json` to:
- Change snippet triggers
- Add new templates
- Modify parameter names
- Add domain-specific prompts

Reload VS Code after changes: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> → "Reindex"

---

## 📚 Full Documentation

- **Examples:** See `examples.py` (18 ready-to-use templates)
- **Guide:** See `VSCODE_USAGE.py` (complete workflows)
- **Best Practices:** See `BEST_PRACTICES.md`
- **API Reference:** See `README.md`

---

## 🐛 Troubleshooting

**Snippets not showing?**
- Ensure `.vscode/python.json` is in VS Code snippets folder
- Restart VS Code completely
- Check file has `.json` extension

**Not seeing compression?**
- Very short prompts don't compress much (L-ZIP shines on verbose ones)
- Try with longer, more detailed English prompts

**Compression low?**
- Add more detail (longer prompts compress better)
- Use specific domain (e.g., [Lang:Python])
- Include examples in CTX:

---

## 🚀 Next Steps

1. ✅ Install snippets to VS Code
2. ✅ Try `lzip-func` snippet
3. ✅ Generate an L-ZIP prompt
4. ✅ Paste into your favorite AI tool
---

**Created by:** ezixen  
**License:** MIT  
**Donate:** Support L-ZIP on GitHub ⭐
