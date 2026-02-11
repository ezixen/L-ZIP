# L-ZIP Quick Reference for VS Code

**Author:** ezixen  
**Version:** 1.0.0  
**Purpose:** Token compression via semantic prompting format

---

## 🚀 Quick Start (30 seconds)

### Copy-Paste These Into Copilot Chat:

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

## 📋 How to Install Snippets

1. **Copy** the `python.json` file from `.vscode/` folder
2. **Locate** VS Code snippets: `%APPDATA%\Code\User\snippets\` (Windows)
3. **Paste** as `python.json` in snippets folder
4. **Restart** VS Code
5. **Type** any `lzip-*` shortcut to autocomplete!

---

## 🎯 Common Workflows

### Workflow A: Function Generation (30 seconds)
```python
# ACT:Senior_Dev [Lang:Python] OBJ:Email_Validator
# OUT:Function + Docstring + Tests

def validate_email(email: str) -> bool:
    # Copilot generates the implementation
```

### Workflow B: Code Review
1. Select code in editor
2. Open Copilot Chat: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>
3. Paste:
```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review + Optimize
OUT:Analysis + Refactoring_Suggestions
```

### Workflow C: Bug Triage
1. See error in terminal
2. Open Copilot Chat
3. Paste:
```
ACT:Debugger CTX:[Error_Message] OBJ:Fix_Bug
THINK:RootCause OUT:Solution + Prevention
```

### Workflow D: Batch Processing
1. Ask Copilot once with L-ZIP
2. For follow-ups, just say:
   - "Add error handling"
   - "Add type hints"
   - "Generate tests"
   - "Optimize it"
   
   (Copilot remembers L-ZIP context!)

---

## 📊 Expected Results

| Task | Compression | Time Saved |
|------|-------------|-----------|
| Simple function | 40-50% | ~30 seconds |
| Complex class | 55-65% | ~2 minutes |
| Full API module | 60-75% | ~5 minutes |
| Test suite | 45-55% | ~2 minutes |

**Average:** 50-70% token reduction vs natural language

---

## 💡 Pro Tips

1. **Use in code comments** - Copilot understands context better
2. **Chain short prompts** - "Add X" after "Generate Y"
3. **Be specific** - [Lang:Python] > "python"
4. **Use alternatives** - `|` means "or" (e.g., `Fix_Bug | Optimize`)
5. **Set output** - Always specify `OUT:Code + Tests + Docs`

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

**Copilot not understanding L-ZIP?**
- Use exact L-ZIP syntax (ACT:, OBJ:, OUT:)
- Put it in code comment first time
- Then use in chat for follow-ups

**Compression low?**
- Add more detail (longer prompts compress better)
- Use specific domain (e.g., [Lang:Python])
- Include examples in CTX:

---

## 🚀 Next Steps

1. ✅ Install snippets to VS Code
2. ✅ Try `lzip-func` snippet
3. ✅ Open Copilot Chat (Ctrl+Shift+I)
4. ✅ Paste an ACT: prompt
5. ✅ Watch tokens reduce by 50-70%!

**Questions?** See `README.md` or run `python cli.py` for interactive demo.

---

**Created by:** ezixen  
**License:** MIT  
**Donate:** Support L-ZIP on GitHub ⭐
