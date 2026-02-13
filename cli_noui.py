#!/usr/bin/env python3
"""
L-ZIP Command Line Interface (CLI-only, no GUI)
Standalone entry point with full feature set and original design
"""

import sys
import json
import platform
import os
import re
from typing import Optional
from lzip import LZIPTranslator, LZIPConfig
from mcp_server import LZIPMCPServer


class ClipboardManager:
    """Cross-platform clipboard management"""
    
    @staticmethod
    def copy_to_clipboard(text: str) -> bool:
        """Copy text to clipboard (Windows-optimized)"""
        try:
            if platform.system() == 'Windows':
                import ctypes
                cf_unicode_text = 13
                
                kernel32 = ctypes.windll.kernel32
                kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
                kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
                kernel32.GlobalAlloc.restype = ctypes.c_void_p
                kernel32.GlobalLock.restype = ctypes.c_void_p
                
                user32 = ctypes.windll.user32
                user32.OpenClipboard.argtypes = [ctypes.c_void_p]
                user32.SetClipboardData.argtypes = [ctypes.c_int, ctypes.c_void_p]
                
                if not ctypes.windll.user32.OpenClipboard(None):
                    return False
                
                ctypes.windll.user32.EmptyClipboard()
                
                hCd = ctypes.windll.kernel32.GlobalAlloc(0x0002, len(text.encode('utf-16-le')) + 2)
                if not hCd:
                    ctypes.windll.user32.CloseClipboard()
                    return False
                
                pch_data = ctypes.windll.kernel32.GlobalLock(hCd)
                if not pch_data:
                    ctypes.windll.user32.CloseClipboard()
                    return False
                
                try:
                    ctypes.memmove(pch_data, text.encode('utf-16-le'), len(text.encode('utf-16-le')))
                    ctypes.windll.kernel32.GlobalUnlock(hCd)
                    ctypes.windll.user32.SetClipboardData(cf_unicode_text, hCd)
                    return True
                finally:
                    ctypes.windll.user32.CloseClipboard()
            else:
                import subprocess
                try:
                    if platform.system() == 'Darwin':
                        subprocess.run(['pbcopy'], input=text.encode(), check=True)
                    else:
                        subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode(), check=True)
                    return True
                except:
                    return False
        except Exception:
            return False


class LZIPCLI:
    """Command-line interface for L-ZIP - full feature CLI"""
    
    def __init__(self):
        self.server = LZIPMCPServer()
        self.translator = LZIPTranslator()
        self.clipboard = ClipboardManager()
        self.running = True
    
    def display_logo(self, size: str = "512") -> None:
        """Display logo as text art in console"""
        if size == "512":
            width = 70
            print("\n" + "█"*72)
            print("█" + " "*width + "█")
            
            line1 = "❤  L-ZIP - EZIXEN  ❤"
            padding1 = (width - len(line1)) // 2
            print("█" + " "*padding1 + line1 + " "*(width - len(line1) - padding1) + "█")
            
            print("█" + " "*width + "█")
            
            line2 = "Logic-based Zero-redundancy Information Prompting"
            padding2 = (width - len(line2)) // 2
            print("█" + " "*padding2 + line2 + " "*(width - len(line2) - padding2) + "█")
            
            print("█" + " "*width + "█")
            
            line3 = "Compress Your Prompts • Save Tokens • Accelerate AI"
            padding3 = (width - len(line3)) // 2
            print("█" + " "*padding3 + line3 + " "*(width - len(line3) - padding3) + "█")
            
            print("█" + " "*width + "█")
            print("█"*72 + "\n")
        else:
            border = "═" * 66
            text = "L-ZIP"
            padding = (66 - len(text)) // 2
            left_pad = " " * padding
            right_pad = " " * (66 - len(text) - padding)
            
            print("\n" + "╔" + border + "╗")
            print("║" + left_pad + text + right_pad + "║")
            print("╚" + border + "╝" + "\n")
    
    def print_header(self):
        """Print application header"""
        self.display_logo("512")
        
        print()
        print("✨ DEFAULT MODE: Paste English prompt → Press Enter 2x → L-ZIP → Auto-copy")
        print()
    
    def print_help(self):
        """Print available commands"""
        commands = {
            "compress (c)": "Convert English prompt to L-ZIP format",
            "expand (e)": "Convert L-ZIP back to English",
            "batch (b)": "Batch translate multiple prompts",
            "dict (d)": "Show L-ZIP operator dictionary",
            "templates (t)": "Show example templates",
            "version (v)": "Show version info",
            "help (h)": "Show this help message",
            "exit/quit (q)": "Exit the program",
        }
        
        print("\nAvailable Commands:")
        print("-" * 70)
        for cmd, desc in commands.items():
            print(f"  {cmd:20} - {desc}")
        print("-" * 70)
    
    def cmd_compress(self, args: list):
        """Translate English to L-ZIP"""
        self.display_logo("128")
        
        if not args or (isinstance(args, list) and not args[0]):
            prompt = input("\nEnter English prompt (or 'cancel' to abort):\n> ")
            if prompt.lower() == 'cancel':
                return
        else:
            prompt = args[0] if isinstance(args, list) and args else ' '.join(args)
        
        result = self.server.handle_translate_to_lzip(prompt)
        lzip_for_clipboard = re.sub(r'\s*OUT:\w+', '', result['lzip_prompt']).strip()
        
        print("\n" + "-" * 70)
        print("TRANSLATION RESULTS")
        print("-" * 70)
        print(f"\nOriginal Prompt:\n{result['original_prompt']}")
        print(f"\nL-ZIP Translation:\n{result['lzip_prompt']}")
        print("\nCompression Report:")
        for key, value in result['compression_report'].items():
            print(f"  {key}: {value}")
        
        if self.clipboard.copy_to_clipboard(lzip_for_clipboard):
            print("\n✓ L-ZIP result copied to clipboard! Ready to paste into any AI.")
        else:
            print("\n⚠ Could not copy to clipboard, but here's your result above.")
        print()
    
    def cmd_expand(self, args: list):
        """Translate L-ZIP to English"""
        self.display_logo("128")
        
        if not args or (isinstance(args, list) and not args[0]):
            lzip = input("\nEnter L-ZIP prompt (or 'cancel' to abort):\n> ")
            if lzip.lower() == 'cancel':
                return
        else:
            lzip = args[0] if isinstance(args, list) and args else ' '.join(args)
        
        result = self.server.handle_translate_from_lzip(lzip)
        
        print("\n" + "-" * 70)
        print("EXPANSION RESULTS")
        print("-" * 70)
        print(f"\nL-ZIP Prompt:\n{result['lzip_prompt']}")
        print(f"\nEnglish Translation:\n{result['english_prompt']}")
        
        if self.clipboard.copy_to_clipboard(result['english_prompt']):
            print("\n✓ English result copied to clipboard!")
        else:
            print("\n⚠ Could not copy to clipboard, but here's your result above.")
        print()
    
    def cmd_dict(self, args: list):
        """Show L-ZIP dictionary"""
        result = self.server.handle_get_dictionary()
        
        print("\n" + "-" * 70)
        print("L-ZIP OPERATOR DICTIONARY")
        print("-" * 70)
        
        for op, desc in result['operators'].items():
            print(f"  {op:10} - {desc}")
        
        print("\n" + "-" * 70)
        print("EXAMPLES")
        print("-" * 70)
        for name, example in result['examples'].items():
            print(f"\n{name.upper()}:")
            print(f"  {example}")
        print()
    
    def cmd_templates(self, args: list):
        """Show L-ZIP templates"""
        result = self.server.handle_get_templates()
        
        print("\n" + "-" * 70)
        print("L-ZIP TEMPLATES")
        print("-" * 70)
        
        for name, template in result['templates'].items():
            print(f"\n{name.upper()}:")
            print(f"  {template}")
        print()
    
    def cmd_batch(self, args: list):
        """Batch translate prompts"""
        print("\nBatch Mode - Enter prompts (one per line, empty line to finish):")
        prompts = []
        while True:
            p = input(f"Prompt {len(prompts)+1} (or press Enter to finish): ").strip()
            if not p:
                break
            prompts.append(p)
        
        if not prompts:
            print("No prompts entered.")
            return
        
        result = self.server.handle_batch_translate(prompts, to_lzip=True)
        
        print("\n" + "-" * 70)
        print(f"BATCH RESULTS ({result['count']} prompts)")
        print("-" * 70)
        
        for i, item in enumerate(result['results'], 1):
            print(f"\n[Prompt {i}]")
            print(f"Original: {item['original']}")
            print(f"L-ZIP:    {item['translated']}")
            if 'metadata' in item:
                print(f"Compression: {item['metadata'].get('compression_ratio', 'N/A')}")
        
        if result['aggregate_compression']:
            print("\n" + "-" * 70)
            print("AGGREGATE STATISTICS")
            print("-" * 70)
            for key, value in result['aggregate_compression'].items():
                print(f"  {key}: {value}")
        print()
    
    def cmd_version(self, args: list):
        """Show version info"""
        result = self.server.handle_get_version()
        print(f"\n{result['name']} v{result['version']}\n")
    
    def process_command(self, cmd: str):
        """Process a CLI command or default to compress"""
        parts = cmd.strip().split(maxsplit=1)
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else None
        
        if command in ['compress', 'c', 'to-lzip']:
            self.cmd_compress([args] if args else [])
        elif command in ['expand', 'e', 'from-lzip']:
            self.cmd_expand([args] if args else [])
        elif command in ['dict', 'd', 'dictionary']:
            self.cmd_dict([])
        elif command in ['templates', 't', 'template']:
            self.cmd_templates([])
        elif command in ['batch', 'b']:
            self.cmd_batch([])
        elif command in ['help', 'h', '?']:
            self.print_help()
        elif command in ['version', 'v']:
            self.cmd_version([])
        elif command in ['exit', 'quit', 'q']:
            self._exit()
        else:
            self.cmd_compress([cmd])
    
    def _exit(self):
        """Exit the program"""
        print("\nGoodbye!\n")
        self.running = False
    
    def sanitize_text(self, text: str) -> str:
        """
        Sanitize pasted text to remove hidden characters.
        Preserves: visible text, numbers, punctuation, spaces, line breaks, capitalization
        Removes: control characters, special unicode, zero-width chars, etc.
        """
        # Remove control characters except newline (\n) and tab (\t)
        sanitized = "".join(
            ch for ch in text
            if ch == "\n" or ch == "\t" or ord(ch) >= 32
        )
        return sanitized
    
    def read_multiline_input(self, prompt_text: str = "") -> str:
        """Read multi-line input (Enter twice to submit, Ctrl+C to cancel)"""
        if prompt_text:
            print(prompt_text, end="")
        
        lines = []
        consecutive_empty = 0
        
        try:
            while True:
                try:
                    # Read input and sanitize to remove hidden characters
                    user_input = input()
                    user_input = self.sanitize_text(user_input)
                    
                    if user_input.strip() == "":
                        consecutive_empty += 1
                        lines.append(user_input)
                        if consecutive_empty >= 2:
                            lines = lines[:-2]
                            break
                    else:
                        consecutive_empty = 0
                        lines.append(user_input)
                except EOFError:
                    break
        except KeyboardInterrupt:
            raise
        
        return "\n".join(lines).strip()
    
    def run_interactive(self):
        """Run interactive REPL"""
        self.print_header()
        self.print_help()
        
        print("\n💡 TIP: Paste text, press Enter twice to submit, Ctrl+C to cancel.")
        
        while self.running:
            try:
                cmd = self.read_multiline_input("\nlzip> ")
                if cmd:
                    self.process_command(cmd)
            except EOFError:
                print("\n\nEnd of input reached. Goodbye!\n")
                self.running = False
            except KeyboardInterrupt:
                print("\n\nInterrupted. Type 'exit' to quit.\n")
            except Exception as e:
                print(f"\nError: {e}\n")
    
    def run_single_command(self, cmd: str):
        """Run a single command and exit"""
        self.process_command(cmd)


def main():
    """Main entry point - CLI only"""
    cli = LZIPCLI()
    
    if len(sys.argv) > 1:
        cmd = ' '.join(sys.argv[1:])
        cli.run_single_command(cmd)
    elif not sys.stdin.isatty():
        try:
            piped_input = sys.stdin.read().strip()
            if piped_input:
                cli.run_single_command(piped_input)
            else:
                cli.run_interactive()
        except Exception as e:
            print(f"Error reading piped input: {e}")
            cli.run_interactive()
    else:
        cli.run_interactive()


if __name__ == '__main__':
    main()
