#!/usr/bin/env python3
"""
L-ZIP MCP Server - Model Context Protocol Implementation
Provides L-ZIP compression as an MCP tool for VS Code and GitHub Copilot
"""

import sys
import json
from typing import Any, Dict
from lzip import LZIPTranslator


class LZIPMCPStdioServer:
    """MCP Server using stdio for communication with VS Code"""
    
    def __init__(self):
        self.translator = LZIPTranslator()
        self.tools = {
            "compress_prompt": {
                "description": "Compress an English prompt to L-ZIP format to save tokens",
                "parameters": {
                    "prompt": {"type": "string", "description": "The prompt to compress"}
                }
            },
            "expand_lzip": {
                "description": "Expand L-ZIP format back to English",
                "parameters": {
                    "lzip": {"type": "string", "description": "The L-ZIP prompt to expand"}
                }
            }
        }
    
    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP request"""
        method = request.get("method", "")
        params = request.get("params", {})
        
        if method == "tools/list":
            return {
                "tools": [
                    {
                        "name": "compress_prompt",
                        "description": "Compress English prompt to L-ZIP (saves 50-70% tokens)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "prompt": {
                                    "type": "string",
                                    "description": "English prompt to compress"
                                }
                            },
                            "required": ["prompt"]
                        }
                    },
                    {
                        "name": "expand_lzip",
                        "description": "Expand L-ZIP back to English",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "lzip": {
                                    "type": "string",
                                    "description": "L-ZIP prompt to expand"
                                }
                            },
                            "required": ["lzip"]
                        }
                    }
                ]
            }
        
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            
            if tool_name == "compress_prompt":
                prompt = arguments.get("prompt", "")
                lzip, metadata = self.translator.translate_to_lzip(prompt)
                
                orig_tokens = metadata.get('original_tokens', 0)
                final_tokens = metadata.get('final_tokens', 0)
                tokens_saved = max(0, orig_tokens - final_tokens)
                compression_pct = metadata.get('compression_ratio', 0)
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"L-ZIP Compressed Prompt:\n{lzip}\n\n"
                                   f"Original: {metadata.get('original_length', 0)} words ({orig_tokens} tokens)\n"
                                   f"Compressed: {metadata.get('final_length', 0)} words ({final_tokens} tokens)\n"
                                   f"Tokens saved: {tokens_saved} ({compression_pct}% compression)"
                        }
                    ]
                }
            
            elif tool_name == "expand_lzip":
                lzip = arguments.get("lzip", "")
                expanded, _ = self.translator.translate_from_lzip(lzip)
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Expanded Prompt:\n{expanded}"
                        }
                    ]
                }
        
        elif method == "initialize":
            return {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "l-zip",
                    "version": "1.0.0"
                }
            }
        
        return {"error": f"Unknown method: {method}"}
    
    def run(self):
        """Run the MCP server via stdio"""
        for line in sys.stdin:
            try:
                request = json.loads(line.strip())
                response = self.handle_request(request)
                print(json.dumps(response), flush=True)
            except Exception as e:
                error_response = {"error": str(e)}
                print(json.dumps(error_response), flush=True)


if __name__ == "__main__":
    server = LZIPMCPStdioServer()
    server.run()
