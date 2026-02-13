#!/usr/bin/env python3
"""L-ZIP GUI (CustomTkinter)"""

import tkinter as tk
from tkinter import filedialog
import os
import sys
import threading
import logging
import traceback
from datetime import datetime

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    import customtkinter as ctk
except Exception as exc:
    raise SystemExit("CustomTkinter is required. Install: pip install customtkinter") from exc

from lzip import LZIPTranslator
from cli import ClipboardManager

def debug_print(msg: str) -> None:
    """Print debug messages - disabled to avoid encoding issues"""
    pass  # Silently skip debug output to avoid encoding errors

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), "lzip_gui_debug.log")
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("LZIP_GUI")
logger.info("=" * 60)
logger.info("L-ZIP GUI Starting")
logger.info(f"Log file: {log_file}")
logger.info("=" * 60)


class LZIPGuiApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("L-ZIP GUI")
        self.geometry("980x680")
        self.minsize(860, 560)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.translator = LZIPTranslator()

        self.auto_copy_var = tk.BooleanVar(value=True)
        self.copy_status_var = tk.StringVar(value="")
        self.input_chars_var = tk.StringVar(value="Input: 0 chars")
        self.output_chars_var = tk.StringVar(value="Output: 0 chars")
        self._pending_text = ""
        self._insert_index = 0
        self._chunk_size = 2000

        self._build_ui()

    def _build_ui(self) -> None:
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=12, pady=(12, 6))

        # Load and display logo
        if Image:
            try:
                logo_path = os.path.join(os.path.dirname(__file__), "images", "L-ZIP-logo-transparent.png")
                if not os.path.exists(logo_path):
                    logo_path = "images/L-ZIP-logo-transparent.png"
                if os.path.exists(logo_path):
                    logo_image = Image.open(logo_path)
                    logo_photo = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(32, 32))
                    logo_label = ctk.CTkLabel(header, image=logo_photo, text="")
                    logo_label.image = logo_photo  # Keep reference
                    logo_label.pack(side="left", padx=(12, 6), pady=10)
            except Exception:
                pass  # Skip logo if not available

        title = ctk.CTkLabel(header, text="L-ZIP Translator", font=("Segoe UI", 20, "bold"))
        title.pack(side="left", padx=(0, 12), pady=10)

        options = ctk.CTkFrame(header, fg_color="transparent")
        options.pack(side="right", padx=12)

        self.copy_status_label = ctk.CTkLabel(options, textvariable=self.copy_status_var, font=("Segoe UI", 11), text_color="green")
        self.copy_status_label.pack(side="left", padx=(0, 12))
        ctk.CTkCheckBox(options, text="Auto-copy", variable=self.auto_copy_var).pack(side="left", padx=8)

        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=12, pady=6)

        left = ctk.CTkFrame(body)
        left.pack(side="left", fill="both", expand=True, padx=(0, 6), pady=6)

        right = ctk.CTkFrame(body)
        right.pack(side="right", fill="both", expand=True, padx=(6, 0), pady=6)

        input_header = ctk.CTkFrame(left, fg_color="transparent")
        input_header.pack(fill="x", padx=10, pady=(10, 4))
        ctk.CTkLabel(input_header, text="Input", font=("Segoe UI", 14, "bold")).pack(side="left")
        ctk.CTkLabel(input_header, textvariable=self.input_chars_var, font=("Segoe UI", 10)).pack(side="right")
        
        self.input_box = ctk.CTkTextbox(left, wrap="word")
        self.input_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.input_box.bind("<<Paste>>", self._on_paste)
        self.input_box.bind("<Return>", self._on_enter)
        self.input_box.bind("<Shift-Return>", self._on_shift_enter)
        self.input_box.bind("<KeyRelease>", self._update_input_chars)

        output_header = ctk.CTkFrame(right, fg_color="transparent")
        output_header.pack(fill="x", padx=10, pady=(10, 4))
        ctk.CTkLabel(output_header, text="Output", font=("Segoe UI", 14, "bold")).pack(side="left")
        ctk.CTkLabel(output_header, textvariable=self.output_chars_var, font=("Segoe UI", 10)).pack(side="right")
        
        self.output_box = ctk.CTkTextbox(right, wrap="word")
        self.output_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        controls = ctk.CTkFrame(self)
        controls.pack(fill="x", padx=12, pady=(6, 12))

        ctk.CTkButton(controls, text="Clear", command=self._clear).pack(side="left", padx=8, pady=8)
        ctk.CTkButton(controls, text="Open File", command=self._open_file).pack(side="left", padx=8, pady=8)
        ctk.CTkButton(controls, text="Paste", command=self._paste).pack(side="left", padx=8, pady=8)
        ctk.CTkButton(controls, text="Translate", command=self._translate).pack(side="left", padx=8, pady=8)

        self.stats_label = ctk.CTkLabel(controls, text="Tokens: -", font=("Segoe UI", 11))
        self.stats_label.pack(side="right", padx=20, fill="x", expand=True)

    def _update_input_chars(self, _event=None) -> None:
        try:
            text = self.input_box.get("1.0", "end-1c")
            char_count = len(text)
            self.input_chars_var.set(f"Input: {char_count} chars")
        except Exception as e:
            debug_print(f"Error updating input chars: {str(e)}")
    
    def _translate(self) -> None:
        debug_print("_translate() called")
        try:
            text = self.input_box.get("1.0", "end").strip()
            debug_print(f"Input text length: {len(text)}")
            if not text:
                self.copy_status_var.set("⚠ No input")
                return

            lzip, metadata = self.translator.translate_to_lzip(text)
            debug_print(f"Translation completed: {len(lzip)} chars output")
            output = lzip.replace("OUT:", "")

            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", output)
            self.output_chars_var.set(f"Output: {len(output)} chars")

            original_tokens = metadata.get("original_tokens", 0)
            final_tokens = metadata.get("final_tokens", 0)
            original_words = metadata.get("original_length", 0)
            final_words = metadata.get("final_length", 0)
            savings = 0.0
            if original_tokens:
                savings = (1 - (final_tokens / max(original_tokens, 1))) * 100
            self.stats_label.configure(
                text=f"Tokens: {original_tokens}->{final_tokens} | Save: {savings:.1f}% | Words: {original_words}->{final_words}"
            )

            if self.auto_copy_var.get():
                copied = ClipboardManager.copy_to_clipboard(output)
                self.copy_status_var.set("✓ Copied" if copied else "⚠ Copy failed")
                self.after(3000, lambda: self.copy_status_var.set(""))
            debug_print("_translate() completed")
        except Exception as e:
            debug_print(f"Error in _translate: {str(e)}")
            import traceback
            debug_print(traceback.format_exc())

    def _paste(self) -> None:
        debug_print("_paste() called")
        try:
            text = ClipboardManager.get_from_clipboard()
            if text is None:
                debug_print("Clipboard is empty")
                self.copy_status_var.set("⚠ Clipboard empty")
                self.after(3000, lambda: self.copy_status_var.set(""))
                return
            debug_print(f"Got clipboard text: {len(text)} chars")
            self._start_paste(text)
        except Exception as e:
            debug_print(f"Error in _paste: {str(e)}")
            import traceback
            debug_print(traceback.format_exc())
            self.copy_status_var.set("⚠ Paste failed")
            self.after(3000, lambda: self.copy_status_var.set(""))

    def _on_paste(self, _event) -> str:
        debug_print("_on_paste() called (Ctrl+V)")
        try:
            text = ClipboardManager.get_from_clipboard()
            if text is None:
                debug_print("Clipboard is empty")
                self.copy_status_var.set("⚠ Clipboard empty")
                self.after(3000, lambda: self.copy_status_var.set(""))
                return "break"
            debug_print(f"Got clipboard text: {len(text)} chars")
            self._start_paste(text)
        except Exception as e:
            debug_print(f"Error in _on_paste: {str(e)}")
            import traceback
            debug_print(traceback.format_exc())
            self.copy_status_var.set("⚠ Paste failed")
            self.after(3000, lambda: self.copy_status_var.set(""))
        return "break"

    def _on_enter(self, _event) -> str:
        self._translate()
        return "break"

    def _on_shift_enter(self, _event) -> str:
        self.input_box.insert("insert", "\n")
        return "break"

    def _start_paste(self, text: str) -> None:
        debug_print(f"_start_paste() called with {len(text)} characters")
        try:
            sanitized = "".join(
                ch for ch in text
                if ch == "\n" or ch == "\t" or ord(ch) >= 32
            )
            debug_print(f"After sanitization: {len(sanitized)} characters")
            
            self.input_box.delete("1.0", "end")
            debug_print("Input box cleared")
            
            self.input_box.insert("1.0", sanitized)
            debug_print("Text inserted successfully")
            
            self.after(100, self._update_input_chars)
            debug_print("_start_paste() completed")
        except Exception as e:
            debug_print(f"Error in _start_paste: {str(e)}")
            import traceback
            debug_print(traceback.format_exc())
            self.copy_status_var.set("⚠ Paste error")
            self.after(3000, lambda: self.copy_status_var.set(""))

    def _insert_next_chunk(self) -> None:
        # Method kept for compatibility but unused now
        pass

    def _clear(self) -> None:
        self.input_box.delete("1.0", "end")
        self.output_box.delete("1.0", "end")
        self.copy_status_var.set("")
        self.input_chars_var.set("Input: 0 chars")
        self.output_chars_var.set("Output: 0 chars")
        self.stats_label.configure(text="Tokens: -")

    def _open_file(self) -> None:
        path = filedialog.askopenfilename(
            title="Open Prompt File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                content = handle.read()
            self._start_paste(content)
        except Exception as exc:
            self.copy_status_var.set(f"⚠ Error: {str(exc)[:30]}")
            self.after(5000, lambda: self.copy_status_var.set(""))


def main() -> None:
    debug_print("Creating GUI app...")
    try:
        app = LZIPGuiApp()
        debug_print("App created, starting mainloop...")
        app.mainloop()
        debug_print("App closed")
    except Exception as e:
        debug_print(f"Fatal error: {str(e)}")
        import traceback
        debug_print(traceback.format_exc())
        raise


if __name__ == "__main__":
    main()
