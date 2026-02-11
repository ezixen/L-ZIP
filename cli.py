#!/usr/bin/env python3
"""
L-ZIP Command Line Interface
Interactive tool for translating prompts to/from L-ZIP format
"""

import sys
import json
from typing import Optional
from lzip import LZIPTranslator, LZIPConfig
from mcp_server import LZIPMCPServer


class LZIPCLI:
    """Command-line interface for L-ZIP"""
    
    def __init__(self):
        self.server = LZIPMCPServer()
        self.translator = LZIPTranslator()
        self.running = True
    
    def print_header(self):
        """Print application header"""
        print("\n" + "="*70)
        print("L-ZIP MCP Server - CLI Interface")
        print("Logic-based Zero-redundancy Information Prompting")
        print("="*70)
        print()
    
    def print_help(self):
        """Print available commands"""
        commands = {
            "compress": "Translate English prompt to L-ZIP format",
            "expand": "Translate L-ZIP back to English",
            "batch": "Batch translate multiple prompts",
            "dict": "Show L-ZIP operator dictionary",
            "templates": "Show example templates",
            "version": "Show version info",
            "help": "Show this help message",
            "demo": "Run interactive demo",
            "exit/quit": "Exit the program",
        }
        
        print("\nAvailable Commands:")
        print("-" * 70)
        for cmd, desc in commands.items():
            print(f"  {cmd:15} - {desc}")
        print("-" * 70)
    
    def cmd_compress(self, args: list):
        """Translate English to L-ZIP"""
        if not args:
            prompt = input("\nEnter English prompt (or 'cancel' to abort):\n> ")
            if prompt.lower() == 'cancel':
                return
        else:
            prompt = ' '.join(args)
        
        result = self.server.handle_translate_to_lzip(prompt)
        
        print("\n" + "-" * 70)
        print("TRANSLATION RESULTS")
        print("-" * 70)
        print(f"\nOriginal Prompt:\n{result['original_prompt']}")
        print(f"\nL-ZIP Translation:\n{result['lzip_prompt']}")
        print("\nCompression Report:")
        for key, value in result['compression_report'].items():
            print(f"  {key}: {value}")
        print()
    
    def cmd_expand(self, args: list):
        """Translate L-ZIP to English"""
        if not args:
            lzip = input("\nEnter L-ZIP prompt (or 'cancel' to abort):\n> ")
            if lzip.lower() == 'cancel':
                return
        else:
            lzip = ' '.join(args)
        
        result = self.server.handle_translate_from_lzip(lzip)
        
        print("\n" + "-" * 70)
        print("EXPANSION RESULTS")
        print("-" * 70)
        print(f"\nL-ZIP Prompt:\n{result['lzip_prompt']}")
        print(f"\nEnglish Translation:\n{result['english_prompt']}")
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
    
    def cmd_demo(self, args: list):
        """Run interactive demo with sample prompts"""
        demo_prompts = [
            "Please write a Python script that reads a CSV file, filters for rows where the age is over 30, and saves the results to a new CSV file.",
            "Act as a senior software architect. Review the following code for bugs, security vulnerabilities, performance issues, and suggest refactoring for readability and maintainability.",
            "Create a comprehensive marketing strategy for a SaaS startup with a budget of $50,000 over 6 months, considering current market conditions.",
            "Summarize the key points from this research paper and identify the top 3 limitations.",
            "Design a database schema for an e-commerce application that handles products, users, orders, and reviews with proper relationships.",
        ]
        
        print("\n" + "="*70)
        print("INTERACTIVE DEMO")
        print("="*70)
        print("\nDemonstrating L-ZIP translation with sample prompts...\n")
        
        for i, prompt in enumerate(demo_prompts, 1):
            print(f"\n{'='*70}")
            print(f"DEMO {i}")
            print(f"{'='*70}")
            
            # Show original
            print(f"\nOriginal Prompt (English):")
            print(f"{prompt[:100]}..." if len(prompt) > 100 else prompt)
            
            # Translate
            result = self.server.handle_translate_to_lzip(prompt)
            
            print(f"\nL-ZIP Translation:")
            print(f"{result['lzip_prompt']}")
            
            print(f"\nCompression: {result['compression_report']['token_reduction']}")
            
            input("\nPress Enter to continue to next example...")
        
        print("\n" + "="*70)
        print("Demo Complete!")
        print("="*70 + "\n")
    
    def cmd_version(self, args: list):
        """Show version info"""
        result = self.server.handle_get_version()
        print(f"\n{result['name']} v{result['version']}\n")
    
    def process_command(self, cmd: str):
        """Process a CLI command"""
        parts = cmd.strip().split(maxsplit=1)
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []
        
        if command in ['compress', 'c', 'to-lzip']:
            self.cmd_compress(args)
        elif command in ['expand', 'e', 'from-lzip']:
            self.cmd_expand(args)
        elif command in ['dict', 'd', 'dictionary']:
            self.cmd_dict(args)
        elif command in ['templates', 't', 'template']:
            self.cmd_templates(args)
        elif command in ['batch', 'b']:
            self.cmd_batch(args)
        elif command in ['demo']:
            self.cmd_demo(args)
        elif command in ['help', 'h', '?']:
            self.print_help()
        elif command in ['version', 'v']:
            self.cmd_version(args)
        elif command in ['exit', 'quit', 'q']:
            print("\nGoodbye!\n")
            self.running = False
        else:
            print(f"\nUnknown command: {command}")
            print("Type 'help' for available commands.\n")
    
    def run_interactive(self):
        """Run interactive REPL"""
        self.print_header()
        self.print_help()
        
        while self.running:
            try:
                cmd = input("\nlzip> ").strip()
                if cmd:
                    self.process_command(cmd)
            except KeyboardInterrupt:
                print("\n\nInterrupted. Type 'exit' to quit.\n")
            except Exception as e:
                print(f"\nError: {e}\n")
    
    def run_single_command(self, cmd: str):
        """Run a single command and exit"""
        self.process_command(cmd)


def main():
    """Main entry point"""
    cli = LZIPCLI()
    
    if len(sys.argv) > 1:
        # Run with arguments
        cmd = ' '.join(sys.argv[1:])
        cli.run_single_command(cmd)
    else:
        # Run interactive mode
        cli.run_interactive()


if __name__ == '__main__':
    main()
