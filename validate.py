#!/usr/bin/env python3
"""
Quick validation script for L-ZIP functionality
"""

import sys
sys.path.insert(0, r'D:\Dev\L-ZIP')

from lzip import LZIPTranslator, create_translator
from mcp_server import LZIPMCPServer, create_server


def test_basic_translation():
    """Test basic translation functionality"""
    print("=" * 70)
    print("TEST 1: Basic Translation")
    print("=" * 70)
    
    translator = create_translator()
    
    english = "Please write a Python script that reads a CSV file."
    lzip, metadata = translator.translate_to_lzip(english)
    
    print(f"\nEnglish:\n  {english}")
    print(f"\nL-ZIP:\n  {lzip}")
    print(f"\nCompression: {metadata['compression_ratio']}%")
    print(f"Original tokens: {metadata['original_tokens']}")
    print(f"Compressed tokens: {metadata['final_tokens']}")
    
    assert metadata['compression_ratio'] > 0
    print("\n✓ TEST PASSED\n")


def test_mcp_server():
    """Test MCP server functionality"""
    print("=" * 70)
    print("TEST 2: MCP Server")
    print("=" * 70)
    
    server = create_server()
    
    request = {
        'action': 'translate_to_lzip',
        'prompt': 'Act as a senior developer and write a Python function'
    }
    
    result = server.process_request(request)
    
    print(f"\nRequest: {request['action']}")
    print(f"Status: {result['status']}")
    print(f"L-ZIP: {result['lzip_prompt']}")
    print(f"Compression: {result['metadata']['compression_ratio']}%")
    
    assert result['status'] == 'success'
    print("\n✓ TEST PASSED\n")


def test_dictionary():
    """Test dictionary endpoint"""
    print("=" * 70)
    print("TEST 3: Dictionary")
    print("=" * 70)
    
    server = create_server()
    result = server.handle_get_dictionary()
    
    print(f"\nOperators found: {len(result['operators'])}")
    print(f"Examples provided: {len(result['examples'])}")
    
    all_ops = ['ACT', 'OBJ', 'LIM', 'CTX', 'OUT']
    for op in all_ops:
        assert op in result['operators'], f"Missing operator: {op}"
        print(f"  ✓ {op}: {result['operators'][op]}")
    
    print("\n✓ TEST PASSED\n")


def test_batch_translation():
    """Test batch translation"""
    print("=" * 70)
    print("TEST 4: Batch Translation")
    print("=" * 70)
    
    server = create_server()
    
    prompts = [
        "Write a Python script",
        "Create a database schema",
        "Design an API",
        "Review this code",
        "Summarize the report"
    ]
    
    result = server.handle_batch_translate(prompts)
    
    print(f"\nProcessed prompts: {result['count']}")
    
    for i, item in enumerate(result['results'], 1):
        compression = item['metadata']['compression_ratio']
        print(f"  Prompt {i}: {compression}% compression")
    
    aggregate = result['aggregate_compression']
    print(f"\nTotal compression: {aggregate['compression_ratio']}")
    
    assert result['status'] == 'success'
    print("\n✓ TEST PASSED\n")


def test_realworld_examples():
    """Test with real-world prompts"""
    print("=" * 70)
    print("TEST 5: Real-World Examples")
    print("=" * 70)
    
    translator = create_translator()
    
    examples = [
        (
            "code_review",
            "Act as a senior Python developer. Review this code for bugs, "
            "security vulnerabilities, performance issues, and best practice violations. "
            "Suggest improvements and provide a fixed version."
        ),
        (
            "content_writing",
            "Write a comprehensive blog post about artificial intelligence "
            "for business professionals. Target length: 1500 words. "
            "Include real statistics and actionable recommendations. "
            "Use markdown formatting with headers and links."
        ),
        (
            "data_analysis",
            "Analyze this dataset and identify patterns, anomalies, and trends. "
            "Provide statistical validation. Create visualizations to represent the findings. "
            "Summarize key insights and business implications."
        ),
    ]
    
    for name, prompt in examples:
        lzip, metadata = translator.translate_to_lzip(prompt)
        print(f"\n{name.upper()}:")
        print(f"  Compression: {metadata['compression_ratio']}%")
        print(f"  Original: {metadata['original_length']} words")
        print(f"  Compressed: {metadata['final_length']} words")
        assert metadata['compression_ratio'] > 30, f"Low compression for {name}"
        print(f"  ✓ PASSED")
    
    print("\n✓ ALL REAL-WORLD TESTS PASSED\n")


def test_roundtrip():
    """Test L-ZIP to English and back"""
    print("=" * 70)
    print("TEST 6: Round-Trip Translation")
    print("=" * 70)
    
    translator = create_translator()
    
    lzip = "ACT:Senior_Dev [Lang:Python] OBJ:Write_Function | Add_Tests GEN:Code | Tests OUT:Production_Ready"
    
    print(f"\nL-ZIP:\n  {lzip}")
    
    english = translator.translate_from_lzip(lzip)
    print(f"\nEnglish:\n  {english}")
    
    assert 'Dev' in english
    assert 'Python' in english
    assert 'Function' in english
    
    print("\n✓ TEST PASSED\n")


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("L-ZIP VALIDATION TEST SUITE")
    print("=" * 70 + "\n")
    
    try:
        test_basic_translation()
        test_mcp_server()
        test_dictionary()
        test_batch_translation()
        test_realworld_examples()
        test_roundtrip()
        
        print("=" * 70)
        print("✅ ALL TESTS PASSED!")
        print("=" * 70 + "\n")
        return 0
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
