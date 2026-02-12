# L-ZIP Usage Guide

## Overview
L-ZIP is a token compression tool that translates English prompts into a compressed format optimized for AI language models. The Windows executable (`lzip.exe`) provides multiple ways to use the tool.

---

## Quick Start

### ⚡ Download & Run (No Installation Needed!)
**Windows users:** Download `lzip.exe` from the [**releases folder**](https://github.com/ezixen/L-ZIP/tree/main/releases) and run it directly!

- ✓ No installation needed
- ✓ No prerequisites (Windows 10+)
- ✓ Everything included in one file (~8.4 MB)
- ✓ Just download and double-click!

### Installation for Developers
If you want to build from source or develop:

**Prerequisites:** Python 3.8+

```powershell
# Clone or navigate to the project directory
cd L-ZIP

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
**The fastest way:** Paste your prompt, press **Enter 2x fast**, get your compressed result auto-copied to clipboard!

```
lzip> (paste your text here)

(press Enter twice fast)

✓ L-ZIP result copied to clipboard!
```

---

## Usage Methods

### 1. **Interactive Mode (Default)**
Run the executable without arguments to enter interactive mode:

```powershell
.\lzip.exe
```

**How it works:**
- See the L-ZIP banner with available commands
- Type or paste your English prompt
- Press **Enter 2x fast** to submit (two blank lines trigger submission)
- Result is automatically copied to clipboard
- Ready to paste into any AI application (ChatGPT, Claude, etc.)

**Supported Commands in Interactive Mode:**
- `compress` (or just paste text) - Translate English → L-ZIP
- `expand <text>` - Translate L-ZIP → English
- `dict` - Show L-ZIP operator dictionary
- `templates` - Show example templates
- `batch` - Batch process multiple prompts
- `demo` - Run interactive demo
- `help` - Show help menu
- `version` - Show version info
- `exit` or `quit` - Exit program

**Example:**
```
lzip> Write a Python function that finds all prime numbers up to N

(press Enter twice)

═══════════════════════════════════════════════════════════════════════════
L-ZIP
═══════════════════════════════════════════════════════════════════════════

TRANSLATION RESULTS
───────────────────────────────────────────────────────────────────────────

Original Prompt:
Write a Python function that finds all prime numbers up to N

L-ZIP Translation:
WRITE:Python|FIND:Prime|TO:N

Compression Report:
  Original tokens: 14
  Compressed tokens: 5
  Token reduction: 64.29%
  Compression ratio: 2.80x

✓ L-ZIP result copied to clipboard! Ready to paste into any AI.
```

---

### 2. **Command-Line Arguments**
Pass your prompt directly as an argument:

```powershell
.\lzip.exe "Your prompt here"
```

**Examples:**
```powershell
# Single-line prompt
.\lzip.exe "Explain quantum computing"

# With pipes
Get-Content myfile.txt | lzip.exe

# Expand L-ZIP back to English
.\lzip.exe expand "EXPLAIN:Quantum|TYPE:Simple"
```

**Output:** Result is printed to console and copied to clipboard

---

### 3. **Piped Input**
Pipe text from files or other commands:

```powershell
# From a file
Get-Content prompt.txt | lzip.exe

# From clipboard
Get-Clipboard | lzip.exe

# Chain multiple operations
... | lzip.exe | Out-File result.txt
```

**Advantage:** No need for interactive Enter keypresses, works with large files

---

### 4. **Batch Processing**
Process multiple prompts from a file in one operation:

```
lzip> batch
```

Or use `batch` command with a file containing one prompt per line:

```powershell
.\lzip.exe batch < prompts.txt
```

---

## Output Format Control

### Format Instructions
The translator recognizes output format requests using L-ZIP operators:

| Format | Syntax | Example |
|--------|--------|---------|
| JSON | `OUT:JSON` | "Analyze data OUT:JSON" |
| Markdown | `OUT:Markdown` | "Create doc OUT:Markdown" |
| Table | `OUT:Table` | "Compare options OUT:Table" |
| Bullet List | `OUT:Bullets` | "List features OUT:Bullets" |
| Numbered List | `OUT:List` | "Steps to follow OUT:List" |

**Note:** Format instructions are automatically included in the L-ZIP translation but are **automatically removed when copied to clipboard** to keep your prompt clean!

**Example:**
```
Input: "Explain quantum computing OUT:JSON"
L-ZIP Translation: "EXPLAIN:Quantum|TYPE:Simple|OUT:JSON"
Clipboard Copy: "EXPLAIN:Quantum|TYPE:Simple"  (OUT:JSON stripped)
```

---

## Examples

### Example 1: Simple Compression
**Input:**
```
Write a detailed explanation of how machine learning works in simple terms for beginners.
```

**L-ZIP Output:**
```
WRITE:ML|EXPLAIN:Simple|AUDIENCE:Beginner
```

**Compression:** 20 tokens → 6 tokens (70% reduction)

---

### Example 2: Multi-Line Prompt with Structure
**Input:**
```
You are a Python expert.

Task: Create a function that:
1. Takes a list of numbers
2. Returns only even numbers
3. Preserves original order

Use type hints and add comments.
```

**L-ZIP Output:**
```
ROLE:Python|CREATE:Function|FILTER:Even|PRESERVE:Order|INCLUDE:TypeHints|INCLUDE:Comments
```

---

### Example 3: With Output Format
**Input:**
```
Compare Python, JavaScript, and Go. Focus on: performance, ease of learning, ecosystem. OUT:Table
```

**L-ZIP Output:**
```
COMPARE:Python|JS|Go|FOCUS:Performance|Learning|Ecosystem|OUT:Table
```

**Clipboard:** (auto-removes OUT:Table for clean paste)

---

## Tips & Tricks

### 💡 Fastest Workflow
1. **Copy** your English prompt to clipboard
2. **Run:** `.\lzip.exe`
3. **Paste** into the prompt (Ctrl+V)
4. **Press Enter 2x fast**
5. **Paste result** into your AI app (Ctrl+V) - already copied!

### 💡 Batch Compression
Compress multiple prompts at once:
```powershell
# Create prompts.txt with one prompt per line
Get-Content prompts.txt | foreach { ".\lzip.exe $_" }
```

### 💡 Integration with Scripts
Use in PowerShell scripts:
```powershell
$prompt = "Your prompt here"
$compressed = & .\lzip.exe $prompt
Write-Output $compressed
```

### 💡 Keyboard Shortcuts in Interactive Mode
- **Ctrl+C** - Cancel current input
- **Ctrl+D** (Unix) or **Ctrl+Z** (Windows) - Exit on piped input
- **Enter 2x** - Submit prompt (press Enter on blank line, then Enter again)

---

## Operators Reference

Common L-ZIP operators used in translations:

| Operator | Purpose | Example |
|----------|---------|---------|
| `WRITE:` | Create/generate content | `WRITE:Code`, `WRITE:Essay` |
| `EXPLAIN:` | Explain concepts | `EXPLAIN:Quantum` |
| `ANALYZE:` | Analyze/examine | `ANALYZE:Text` |
| `CREATE:` | Generate something new | `CREATE:Function` |
| `COMPARE:` | Compare items | `COMPARE:A|B|C` |
| `FIND:` | Search/locate | `FIND:Prime` |
| `FILTER:` | Filter results | `FILTER:Even` |
| `ROLE:` | Specify a role | `ROLE:Expert` |
| `TYPE:` | Specify type/style | `TYPE:Simple` |
| `OUT:` | Output format | `OUT:JSON`, `OUT:Table` |

Use `lzip.exe dict` in interactive mode to see the full dictionary.

---

## Compression Report

Each translation includes a compression report:

```
Compression Report:
  Original tokens: 25
  Compressed tokens: 8
  Token reduction: 68%
  Compression ratio: 3.1x
```

This helps you understand how much you're saving with L-ZIP compression!

---

## Troubleshooting

### "Out of memory" or crashes
- Close other applications
- The exe should work on any Windows machine with minimal resources
- If issues persist, check that you have at least 50MB free disk space

### Clipboard not working
- Ensure no other app has clipboard locked
- Try using piped output instead: `lzip.exe "prompt" | Set-Clipboard`

### Enter 2x not working in interactive mode
- Make sure you press Enter on a blank line, then Enter again
- File > Properties > Details to check exe version if updating
- Rebuild from source if persistent

### Unicode/emoji display issues
- Ensure your console supports UTF-8
- Update Windows Terminal or PowerShell to latest version
- Try running from newer Windows Terminal app (more stable)

---

## Advanced Usage

### Batch File Processing
Create a `compress-batch.ps1`:
```powershell
param([string]$inputFile, [string]$outputFile)

$results = @()
$prompts = Get-Content $inputFile

foreach ($prompt in $prompts) {
    $compressed = & .\lzip.exe $prompt
    $results += $compressed
}

$results | Out-File $outputFile
```

Run with:
```powershell
.\compress-batch.ps1 -inputFile prompts.txt -outputFile compressed.txt
```

### Integration with Python
```python
import subprocess

def compress_prompt(prompt):
    result = subprocess.run(['lzip.exe', prompt], capture_output=True, text=True)
    return result.stdout.strip()

compressed = compress_prompt("Your prompt here")
print(compressed)
```

### Integration with PowerShell Functions
```powershell
function Compress-Prompt {
    param([string]$Prompt)
    $result = & .\lzip.exe $Prompt
    return $result
}

$compressed = Compress-Prompt "Write a function"
```

---

## System Requirements

- **OS:** Windows 10 or later
- **Architecture:** x86-64 (64-bit)
- **RAM:** 50 MB minimum (typical usage: 100-200 MB)
- **Disk:** 200 MB for extraction + workspace
- **Dependencies:** None! Everything is bundled in the exe

---

## Performance

- **Single prompt:** < 100ms
- **Large prompt (1000+ tokens):** < 500ms
- **Clipboard operations:** < 50ms
- **Batch mode (100 prompts):** < 2 seconds

---

## Privacy & Security

- **No internet connection required** - everything runs locally
- **No telemetry** - your prompts never leave your machine
- **Clipboard access:** Only to copy results (same as Ctrl+C)
- **Source code:** Available on GitHub for audit

---

## Getting Help

- Run `lzip.exe help` for command list
- Run `lzip.exe demo` for interactive walkthrough
- Check this documentation for detailed usage
- See GitHub repository for source code and issues

---

## Version

Current version: See `lzip.exe version` in interactive mode

Last updated: February 2026
