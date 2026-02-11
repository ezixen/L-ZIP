# L-ZIP VS Code Extension

**Logic-based Zero-redundancy Information Prompting for VS Code**

Compress your AI prompts by 40-70% while preserving meaning. Save tokens, reduce costs, and get faster responses from AI models.

## 🎯 Features

### Status Bar Integration
- **L-ZIP MCP Toggle** - Enable/disable MCP status indicator
- **L-ZIP Estimator** - Real-time token savings calculator

### Smart Prompt Compression
- **Context-aware compression** - Removes filler words intelligently
- **Symbol replacements** - Converts verbose phrases to compact operators
- **Number abbreviations** - `5000` → `5k`, `1000000` → `1M`
- **Time compression** - `30 minutes` → `30m`, `2 hours` → `2h`
- **Tech term shortcuts** - `image` → `img`, `database` → `db`
- **Extended operators** - IMAGE, CODE, CONTENT specific tags

### Copy & Paste Ready
- One-click copy of compressed prompts
- Visual comparison of original vs compressed
- Real-time token count and savings percentage
- Prominent display of L-ZIP translation at the top

## 📊 Example

**Original (644 tokens):**
```
Make a picture for me in high as possible quality, nice realistic looks, 
but still happy, kind, fantasy style please. Theme is a Weekend Magic Festival...
```

**L-ZIP (450 tokens - 30% saved):**
```
STYLE:Realistic MOOD:Happy LIGHTING:Sunny QUALITY:4K RATIO:16:9 
Make a picture in high quality, nice realistic looks, happy, kind, fantasy style. 
Theme is Weekend Magic Festival...
```

## 🚀 Quick Start

1. Install the extension
2. Click the **🧪 L-ZIP Estimator** button in the status bar
3. Paste your prompt
4. Copy the compressed version with one click
5. Use it with any AI model (ChatGPT, Claude, Gemini, etc.)

## 📋 Requirements

- **Python 3.8+** installed and accessible
- **L-ZIP Python module** (automatically found in parent directory)

## ⚙️ Extension Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `lzip.pythonPath` | Python executable path | `"python"` |
| `lzip.estimatorDefaultText` | Placeholder text for estimator | `"Insert prompt..."` |

## 🎨 Usage Tips

### For Image Generation
The extension auto-detects image-specific keywords:
- Detects quality: `4k`, `8k`, `high quality` → `QUALITY:4K`
- Detects style: `realistic`, `anime`, `oil painting` → `STYLE:Realistic`
- Detects mood: `happy`, `dark`, `cheerful` → `MOOD:Happy`
- Detects aspect ratios: `16:9`, `1:1` → `RATIO:16:9`

### For Code Requests
Removes politeness without losing meaning:
- ❌ Removes: `please`, `kindly`, `for me`, `if you can`
- ✅ Keeps: All technical requirements and constraints

### For Analysis Tasks
Compresses sequential steps:
- `and then` → `|`
- `as well as` → `+`
- `leads to` → `=>`

## 🔧 Development

### Debug the Extension
1. Open the `vscode-extension` folder in VS Code
2. Press `F5` to launch Extension Development Host
3. Test the status bar buttons in the new window
4. Changes auto-reload with the watch task

### Build from Source
```bash
cd vscode-extension
npm install  # If you add dependencies later
# No build step needed - pure JavaScript
```

### Project Structure
```
vscode-extension/
├── src/
│   └── extension.js       # Main extension code
├── .vscode/
│   ├── launch.json        # Debug configuration
│   └── tasks.json         # Build tasks
├── package.json           # Extension manifest
├── README.md              # This file
└── SMART_COMPRESSION.md   # Future ML enhancement plan
```

## 🐛 Troubleshooting

**Extension not activating:**
- Extension activates on startup (`onStartupFinished`)
- Check Output panel → "Extension Host" for errors

**Status bar buttons not showing:**
- Reload the Extension Development Host window (`Ctrl+R`)
- Check if other extensions are hiding the status bar

**Python module not found:**
- Extension looks for `lzip.py` in parent directory
- Ensure your workspace includes the parent L-ZIP folder
- Check Python path in settings: `lzip.pythonPath`

**Compression not working:**
- Verify Python is installed: `python --version`
- Check if `lzip.py` exists in parent folder
- See error details in the Estimator output panel

## 📝 Version History

### v0.0.1 (Current)
- ✅ Status bar MCP toggle
- ✅ Token estimator with copy button
- ✅ Context-aware compression (40-70% token reduction)
- ✅ Extended operators (IMAGE, CODE, CONTENT)
- ✅ Symbol replacements with word boundaries
- ✅ Number and time abbreviations
- ✅ Safe filler word removal

### Planned (v0.1.0)
- 🔄 ML-based context understanding (SmolLM-135M)
- 🔄 Custom compression rules per workspace
- 🔄 Batch processing multiple prompts
- 🔄 Direct language model API integration

## 📄 License

MIT License - See parent project LICENSE file

## 🤝 Contributing

This extension is part of the L-ZIP project by [ezixen](https://github.com/ezixen).

To contribute:
1. Review the main L-ZIP documentation in parent directory
2. Fork the repository
3. Make your changes
4. Test thoroughly with F5 debugging
5. Submit a pull request

## 🔗 Related

- [L-ZIP Main Project](../README.md)
- [L-ZIP Best Practices](../BEST_PRACTICES.md)
- [MCP Integration Guide](../MCP_INTEGRATION.md)

---

**Made with ❤️ by ezixen** | Reducing AI's carbon footprint, one token at a time.
