#!/usr/bin/env python3
"""
L-ZIP Demonstration Script
Shows real-world compression and token savings
"""

from lzip import LZIPTranslator

def main():
    translator = LZIPTranslator()
    
    # Test prompt
    test_prompt = """I need you to write a Python function that validates email addresses. 
The function should check for proper format, handle edge cases, and include comprehensive 
error handling. Please provide the complete implementation with docstring, type hints, 
and a full test suite covering all edge cases."""
    
    print('=' * 80)
    print('ORIGINAL PROMPT (Natural Language)')
    print('=' * 80)
    print(test_prompt)
    print()
    
    # Translate to L-ZIP
    lzip_version, stats = translator.translate_to_lzip(test_prompt)
    
    print('=' * 80)
    print('L-ZIP TRANSLATED VERSION')
    print('=' * 80)
    print(lzip_version)
    print()
    
    # Get metrics
    original_words = len(test_prompt.split())
    lzip_words = len(lzip_version.split())
    original_tokens = original_words * 1.3
    lzip_tokens = lzip_words * 1.3
    savings_pct = ((original_tokens - lzip_tokens) / original_tokens) * 100
    tokens_saved = int(original_tokens - lzip_tokens)
    
    print('=' * 80)
    print('TOKEN ANALYSIS & GITHUB COPILOT SAVINGS')
    print('=' * 80)
    print(f'Original prompt words: {original_words}')
    print(f'L-ZIP prompt words: {lzip_words}')
    print(f'Compression ratio: {(lzip_words/original_words)*100:.1f}%')
    print()
    print(f'Est. original tokens: {int(original_tokens)}')
    print(f'Est. L-ZIP tokens: {int(lzip_tokens)}')
    print(f'Token savings per prompt: {savings_pct:.1f}%')
    print()
    print('GITHUB COPILOT PRICING (Pro Plan):')
    print(f'  Rate: $0.003 per 1K input tokens')
    print(f'  Tokens saved per prompt: {tokens_saved}')
    print(f'  Cost saved per prompt: ${(tokens_saved * 0.003 / 1000):.5f}')
    print(f'  Cost saved per 100 prompts: ${((tokens_saved / 1000) * 0.003 * 100):.2f}')
    print(f'  Cost saved per 1000 prompts: ${((tokens_saved / 1000) * 0.003 * 1000):.2f}')
    print()
    print('EXAMPLE USAGE IN COPILOT CHAT:')
    print('-' * 80)
    print('Copy and paste this L-ZIP prompt into GitHub Copilot Chat:')
    print()
    print(lzip_version)
    print()
    print('-' * 80)
    

if __name__ == '__main__':
    main()
