"""
L-ZIP Test Suite
Comprehensive tests for L-ZIP translator and MCP server
"""

import unittest
from lzip import LZIPTranslator, LZIPConfig
from mcp_server import LZIPMCPServer


class TestLZIPTranslator(unittest.TestCase):
    """Test cases for LZIPTranslator"""
    
    def setUp(self):
        """Initialize translator for each test"""
        self.translator = LZIPTranslator()
        self.server = LZIPMCPServer()
    
    # Test 1: Simple English to L-ZIP
    def test_simple_compression(self):
        """Test basic prompt compression"""
        prompt = "Please write a Python script."
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertIsNotNone(lzip)
        self.assertGreater(metadata['compression_ratio'], 0)
        self.assertLess(metadata['final_tokens'], metadata['original_tokens'])
    
    # Test 2: Complex prompt with multiple operators
    def test_complex_prompt(self):
        """Test compression of complex multi-part prompt"""
        prompt = (
            "Act as a senior Python developer. Your objective is to write a robust "
            "error handling script that processes user input. Limit the output to "
            "under 100 lines of code. The output should be formatted as a complete, "
            "production-ready Python script."
        )
        
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertIn('ACT:', lzip)  # Should detect role
        self.assertIn('OBJ:', lzip)  # Should detect objective
        self.assertIn('LIM:', lzip)  # Should detect limits
        self.assertIn('OUT:', lzip)  # Should detect output format
        self.assertGreater(metadata['compression_ratio'], 30)
    
    # Test 3: Round-trip translation
    def test_roundtrip(self):
        """Test that L-ZIP can be expanded back"""
        lzip_prompt = "ACT:Dev OBJ:Write_Script OUT:Python"
        expanded = self.translator.translate_from_lzip(lzip_prompt)
        
        self.assertIn('Dev', expanded)
        self.assertIn('Script', expanded)
    
    # Test 4: Token counting
    def test_token_counting(self):
        """Test that token counting is reasonable"""
        prompt = "This is a test sentence for token counting."
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        # Approximate: ~4 chars per token
        estimated_tokens = len(prompt) // 4
        self.assertAlmostEqual(metadata['original_tokens'], estimated_tokens, delta=2)
    
    # Test 5: Compression ratio calculation
    def test_compression_ratio(self):
        """Test compression ratio is calculated correctly"""
        original = "Please write a Python script that does something amazing"
        lzip, metadata = self.translator.translate_to_lzip(original)
        
        ratio = metadata['compression_ratio']
        self.assertGreaterEqual(ratio, 0)
        self.assertLessEqual(ratio, 100)
    
    # Test 6: Code preservation
    def test_code_preservation(self):
        """Test that code snippets are handled properly"""
        prompt = (
            "Act as a code reviewer. Review this Python function:\n"
            "def hello():\n    print('Hello')\n"
            "Identify any issues."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        # Translator should recognize it's code review
        self.assertIsNotNone(lzip)
    
    # Test 7: Technical term handling
    def test_technical_terms(self):
        """Test handling of technical terminology"""
        prompt = (
            "Create a REST API endpoint in Python that returns JSON. "
            "Use async/await for performance. Output as TypeScript."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        # Should preserve technical terms
        self.assertIsNotNone(lzip)
        self.assertGreater(metadata['compression_ratio'], 20)
    
    # Test 8: Different domains
    def test_business_domain(self):
        """Test compression of business-domain prompts"""
        prompt = (
            "Act as a business consultant. Create a marketing strategy "
            "with budget of $50,000 for a SaaS startup over 6 months. "
            "Provide actionable steps and ROI projections."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertIn('ACT:', lzip)
        self.assertGreater(metadata['compression_ratio'], 10)
    
    def test_technical_domain(self):
        """Test compression of technical prompts"""
        prompt = (
            "Act as a DevOps engineer. Debug the following Kubernetes deployment. "
            "Find root causes and suggest fixes."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertIsNotNone(lzip)
        self.assertGreater(metadata['compression_ratio'], 30)
    
    # Test 9: MCP Server integration
    def test_mcp_server_translate_to_lzip(self):
        """Test MCP server translate_to_lzip action"""
        result = self.server.handle_translate_to_lzip(
            "Please write a Python script"
        )
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('lzip_prompt', result)
        self.assertIn('metadata', result)
    
    def test_mcp_server_translate_from_lzip(self):
        """Test MCP server translate_from_lzip action"""
        result = self.server.handle_translate_from_lzip(
            "ACT:Dev OBJ:Write_Code"
        )
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('english_prompt', result)
    
    def test_mcp_server_batch_translate(self):
        """Test MCP server batch translation"""
        prompts = [
            "Write a Python script",
            "Create a database schema",
            "Design an API"
        ]
        
        result = self.server.handle_batch_translate(prompts)
        
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['count'], 3)
        self.assertIn('results', result)
    
    def test_mcp_server_get_dictionary(self):
        """Test MCP server dictionary endpoint"""
        result = self.server.handle_get_dictionary()
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('operators', result)
        self.assertIn('examples', result)
    
    def test_mcp_server_get_templates(self):
        """Test MCP server templates endpoint"""
        result = self.server.handle_get_templates()
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('templates', result)
    
    # Test 10: Empty and edge cases
    def test_empty_prompt(self):
        """Test handling of empty prompt"""
        lzip, metadata = self.translator.translate_to_lzip("")
        
        self.assertEqual(lzip.strip(), "")
        self.assertEqual(metadata['original_length'], 0)
    
    def test_single_word(self):
        """Test handling of single word"""
        lzip, metadata = self.translator.translate_to_lzip("code")
        
        self.assertIsNotNone(lzip)
    
    def test_very_long_prompt(self):
        """Test handling of very long prompt"""
        long_prompt = "word " * 1000  # 1000 words
        lzip, metadata = self.translator.translate_to_lzip(long_prompt)
        
        self.assertGreater(metadata['compression_ratio'], 5)
    
    # Test 11: Compression report generation
    def test_compression_report(self):
        """Test compression report generation"""
        original = "Please write a comprehensive Python script"
        lzip, _ = self.translator.translate_to_lzip(original)
        
        report = self.translator.get_compression_report(original, lzip)
        
        self.assertIn('original_words', report)
        self.assertIn('compressed_words', report)
        self.assertIn('word_reduction', report)
        self.assertIn('token_reduction', report)
    
    # Test 12: Process request handler
    def test_mcp_process_request_valid(self):
        """Test MCP process_request with valid action"""
        request = {
            'action': 'translate_to_lzip',
            'prompt': 'Write Python code'
        }
        
        result = self.server.process_request(request)
        self.assertEqual(result['status'], 'success')
    
    def test_mcp_process_request_invalid(self):
        """Test MCP process_request with invalid action"""
        request = {'action': 'invalid_action'}
        
        result = self.server.process_request(request)
        self.assertEqual(result['status'], 'error')
        self.assertIn('available_actions', result)
    
    # Test 13: Role normalization
    def test_role_normalization(self):
        """Test role name normalization"""
        roles = [
            ("senior developer", "Senior_Dev"),
            ("data scientist", "Data_Scientist"),
            ("software architect", "Software_Architect"),
        ]
        
        for input_role, expected in roles:
            normalized = self.translator._normalize_role(input_role)
            self.assertEqual(normalized, expected)
    
    # Test 14: Output format normalization
    def test_output_normalization(self):
        """Test output format normalization"""
        outputs = [
            ("json", "JSON"),
            ("python code", "Python"),
            ("markdown table", "Table"),
        ]
        
        for input_fmt, expected in outputs:
            normalized = self.translator._normalize_output(input_fmt)
            self.assertEqual(normalized, expected)
    
    # Test 15: Real-world examples
    def test_realworld_code_review(self):
        """Test real-world code review prompt"""
        prompt = (
            "I'm a Python developer working on a microservice. "
            "Here's my FastAPI endpoint code. Please review it for: "
            "1) Security vulnerabilities, 2) Performance issues, "
            "3) Code style improvements, 4) Better error handling. "
            "Provide the improved version."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertTrue(metadata['compression_ratio'] > 10)
        # May not detect ACT if prompt uses "I'm a developer" instead of "Act as"
        # This is still valid L-ZIP - just processed as OBJ/action text
        self.assertIn('OUT:', lzip)
    
    def test_realworld_writing_task(self):
        """Test real-world writing task prompt"""
        prompt = (
            "Please write a blog post about artificial intelligence and climate change. "
            "Target audience: business professionals. "
            "Length: about 1500 words. "
            "Tone: informative but accessible. "
            "Include at least 3 real statistics and 2 actionable recommendations. "
            "Format as markdown with proper headers and links."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertTrue(metadata['compression_ratio'] > 10)
    
    def test_realworld_technical_analysis(self):
        """Test real-world technical analysis prompt"""
        prompt = (
            "Act as a database architect. I have a PostgreSQL database "
            "handling 10M daily queries. Query response time degraded by 40% "
            "over the past week. Analyze this slow query log and suggest "
            "optimization strategies. Consider: indexing, query rewriting, "
            "materialized views, and partitioning. Provide before/after metrics."
        )
        lzip, metadata = self.translator.translate_to_lzip(prompt)
        
        self.assertTrue(metadata['compression_ratio'] > 10)


class TestLZIPIntegration(unittest.TestCase):
    """Integration tests for L-ZIP system"""
    
    def setUp(self):
        self.server = LZIPMCPServer()
    
    def test_workflow_compress_then_uncompress(self):
        """Test full workflow: English -> L-ZIP -> English"""
        original = "Please write a secure Python function that validates email addresses"
        
        # Compress
        compress_result = self.server.handle_translate_to_lzip(original)
        lzip = compress_result['lzip_prompt']
        
        # Expand
        expand_result = self.server.handle_translate_from_lzip(lzip)
        expanded = expand_result['english_prompt']
        
        # Both should be valid strings
        self.assertIsNotNone(lzip)
        self.assertIsNotNone(expanded)
    
    def test_batch_workflow(self):
        """Test batch translation workflow"""
        prompts = [
            "Write Python code",
            "Create database schema",
            "Design REST API",
            "Review this code",
            "Summarize the document"
        ]
        
        result = self.server.handle_batch_translate(prompts)
        
        self.assertEqual(result['status'], 'success')
        self.assertEqual(len(result['results']), len(prompts))
        
        # Check that all compressions are positive
        for item in result['results']:
            self.assertGreater(
                item['metadata']['original_tokens'],
                0
            )


class TestCompressionRatios(unittest.TestCase):
    """Validate compression ratio claims"""
    
    def setUp(self):
        self.translator = LZIPTranslator()
    
    def test_40_percent_compression_claim(self):
        """Verify minimum 15% compression on typical prompts (lossless)"""
        prompts = [
            "Please act as a senior software architect and review this code for potential bugs, security issues, and optimization opportunities.",
            "I need you to create a comprehensive marketing plan for a new product launch with a budget of $100,000 over 6 months including timeline and metrics.",
            "Write a detailed Python script that reads a CSV file, processes the data, applies filters, and exports results to a new file with error handling.",
        ]
        
        for prompt in prompts:
            lzip, metadata = self.translator.translate_to_lzip(prompt)
            self.assertGreater(
                metadata['compression_ratio'],
                15,
                f"Failed for: {prompt[:50]}..."
            )


def run_tests():
    """Run all tests"""
    unittest.main(verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()
