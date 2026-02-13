# L-ZIP Command Line Parameters

## Overview
L-ZIP provides two executables: a GUI+CLI hybrid (`lzip.exe`) and a CLI-only version (`lzip-cli.exe`).

## lzip.exe (GUI + CLI Mode)

### Default Mode - GUI
```bash
lzip.exe
```
Launches the CustomTkinter GUI interface for interactive prompt compression.

### CLI Mode
```bash
lzip.exe --cli
```
Runs in command-line mode. Paste or input English prompts and press Enter twice to compress.

**Features:**
- Interactive prompt compression
- Auto-copy to clipboard
- Batch processing
- Expand L-ZIP back to English
- View operator dictionary
- Show example templates

## lzip-cli.exe (CLI Only)

### Basic Usage
```bash
lzip-cli.exe "Your English prompt here"
```
Compresses the provided text and copies the result to clipboard.

**Example:**
```bash
lzip-cli.exe "You are a helpful AI assistant that provides detailed answers"
```

**Output:**
```
Original: 12 words, 10 tokens
Compressed: 6 words, 8 tokens
Savings: 20% token reduction
```

## Environment Variables

- `LZIP_MODE`: Set to `cli` to force CLI mode (for GUI executable)
- `LZIP_AUTO_COPY`: Set to `1` to auto-copy results to clipboard (default: enabled)

## Exit Codes

- `0` - Success
- `1` - Error (invalid input, clipboard error, etc.)

## Features

### Text Sanitization
- Removes hidden/control characters
- Preserves visible text, paragraphs, and capitalization
- Handles multi-line input with proper line breaks

### Clipboard Handling
- **Read**: Uses tkinter's clipboard_get() for safe cross-platform reading
- **Write**: Supports auto-copy of results to clipboard
- **Clipboard Empty Check**: Returns error if clipboard is empty

### Supported Platforms
- Windows (primary)
- macOS (with xclip/pbcopy)
- Linux (with xclip/xsel)

## Building from Source

### Requirements
```
Python 3.13+
customtkinter
Pillow
PyInstaller 6.18.0+
```

### Build GUI+CLI Executable
```bash
pyinstaller build_exe.spec
```

### Build CLI-Only Executable
```bash
pyinstaller build_cli_standalone.spec
```

## Command Reference (GUI/Interactive Mode)

### Available Commands
- `compress (c)` - Convert English to L-ZIP
- `expand (e)` - Convert L-ZIP to English
- `batch (b)` - Process multiple prompts
- `dict (d)` - Show L-ZIP operator dictionary
- `templates (t)` - Show example templates
- `version (v)` - Show version info
- `help (h)` - Show help message
- `exit/quit (q)` - Exit program

## Version Information
- **Latest Build**: 2026-02-13
- **Python**: 3.13.11
- **GUI**: CustomTkinter
- **Build Tool**: PyInstaller 6.18.0
