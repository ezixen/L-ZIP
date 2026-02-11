"""
L-ZIP MCP Server
Exposes L-ZIP translation capabilities via Model Context Protocol
"""

import json
from typing import Any, Optional
from lzip import LZIPTranslator, LZIPConfig


class LZIPMCPServer:
    """MCP Server for L-ZIP translation"""
    
    def __init__(self):
        self.translator = LZIPTranslator(config=LZIPConfig(aggressive_mode=False))
        self.version = "1.0.0"
        self.name = "L-ZIP MCP Server"
    
    def handle_translate_to_lzip(self, prompt: str, aggressive: bool = False) -> dict:
        """
        Translate English prompt to L-ZIP format
        
        Args:
            prompt: English language prompt
            aggressive: Whether to use aggressive compression mode
        
        Returns:
            Dictionary with lzip_prompt and metadata
        """
        translator = LZIPTranslator(config=LZIPConfig(aggressive_mode=aggressive))
        lzip_prompt, metadata = translator.translate_to_lzip(prompt)
        
        return {
            "status": "success",
            "lzip_prompt": lzip_prompt,
            "original_prompt": prompt,
            "metadata": metadata,
            "compression_report": translator.get_compression_report(prompt, lzip_prompt)
        }
    
    def handle_translate_from_lzip(self, lzip_prompt: str) -> dict:
        """
        Translate L-ZIP back to English
        
        Args:
            lzip_prompt: L-ZIP format prompt
        
        Returns:
            Dictionary with english_prompt
        """
        english_prompt = self.translator.translate_from_lzip(lzip_prompt)
        
        return {
            "status": "success",
            "english_prompt": english_prompt,
            "lzip_prompt": lzip_prompt
        }
    
    def handle_batch_translate(self, prompts: list, to_lzip: bool = True) -> dict:
        """
        Translate multiple prompts
        
        Args:
            prompts: List of prompts
            to_lzip: If True, translate to L-ZIP; if False, translate from L-ZIP
        
        Returns:
            Dictionary with results and aggregate stats
        """
        results = []
        total_original_tokens = 0
        total_compressed_tokens = 0
        
        for prompt in prompts:
            if to_lzip:
                lzip_prompt, metadata = self.translator.translate_to_lzip(prompt)
                results.append({
                    "original": prompt,
                    "translated": lzip_prompt,
                    "metadata": metadata
                })
                total_original_tokens += metadata['original_tokens']
                total_compressed_tokens += metadata['final_tokens']
            else:
                english = self.translator.translate_from_lzip(prompt)
                results.append({
                    "original": prompt,
                    "translated": english
                })
        
        return {
            "status": "success",
            "count": len(results),
            "results": results,
            "aggregate_compression": {
                "total_original_tokens": total_original_tokens,
                "total_compressed_tokens": total_compressed_tokens,
                "compression_ratio": f"{(1 - total_compressed_tokens/max(total_original_tokens, 1)) * 100:.1f}%"
            } if to_lzip else None
        }
    
    def handle_get_dictionary(self) -> dict:
        """Get L-ZIP operator dictionary"""
        return {
            "status": "success",
            "version": self.version,
            "operators": {
                "ACT": "Set role or persona",
                "OBJ": "Primary objective",
                "LIM": "Constraints and limits",
                "CTX": "Background context",
                "OUT": "Output format",
                "SUM": "Summarize or list top N",
                "GEN": "Generate content",
                "EVAL": "Evaluate or critique",
                "THINK": "Force step-by-step reasoning",
                "VIS": "Request visualization",
                "=>": "Leads to / results in",
                "|": "Sequential steps / pipe",
                "+": "And / also / addition",
                "@": "Time, level, audience, or condition",
                "LEN": "Length constraint"
            },
            "examples": {
                "simple": "ACT:Dev OBJ:Write_Python_Script OUT:Code",
                "moderate": "ACT:Senior_Dev [Lang:Python] OBJ:Debug OBJ:Refactor THINK:StepByStep OUT:Code+Explanation",
                "complex": "ACT:Consultant [Business:SaaS] OBJ:Revenue+Growth @6mo LIM:Budget<$50k CTX:[Market_Data] OUT:Strategy+Budget"
            }
        }
    
    def handle_get_templates(self) -> dict:
        """Get L-ZIP templates for common use cases"""
        return {
            "status": "success",
            "templates": {
                "code_review": "ACT:Senior_Dev [Lang:{LANG}] CTX:[Code_Block] OBJ:Review_Code | Find_Issues | Suggest_Improvements GEN:Fixed_Code THINK:StepByStep",
                "content_creation": "ACT:Writer OBJ:Create_{TYPE} [Topic:{TOPIC}] @{AUDIENCE} LIM:{STYLE} LEN:{LENGTH} OUT:Draft",
                "data_analysis": "ACT:DataScientist CTX:[Dataset] OBJ:Analyze_Data SUM:Top5_Insights EVAL:Statistical_Significance OUT:Report+Charts",
                "debugging": "ACT:DevOps [Service:{SERVICE}] CTX:[Error_Log] OBJ:Find_Root_Cause => Fix THINK:StepByStep OUT:Solution+Prevention",
                "meeting_summary": "ACT:Executive CTX:[Meeting_Transcript] OBJ:Summarize SUM:Key_Decisions+Action_Items OUT:Bullets",
                "strategy_planning": "ACT:Strategist OBJ:Create_Plan [Goal:{GOAL}] @{TIMEFRAME} LIM:{CONSTRAINTS} CTX:{CONTEXT} OUT:Timeline+Milestones+Budget"
            }
        }
    
    def process_request(self, request: dict) -> dict:
        """
        Main entry point for MCP requests
        
        Args:
            request: Dictionary with 'action' and corresponding parameters
        
        Returns:
            Response dictionary
        """
        action = request.get('action', '').lower()
        
        try:
            if action == 'translate_to_lzip':
                return self.handle_translate_to_lzip(
                    prompt=request.get('prompt', ''),
                    aggressive=request.get('aggressive', False)
                )
            elif action == 'translate_from_lzip':
                return self.handle_translate_from_lzip(
                    lzip_prompt=request.get('lzip_prompt', '')
                )
            elif action == 'batch_translate':
                return self.handle_batch_translate(
                    prompts=request.get('prompts', []),
                    to_lzip=request.get('to_lzip', True)
                )
            elif action == 'get_dictionary':
                return self.handle_get_dictionary()
            elif action == 'get_templates':
                return self.handle_get_templates()
            elif action == 'get_version':
                return {
                    "status": "success",
                    "name": self.name,
                    "version": self.version
                }
            else:
                return {
                    "status": "error",
                    "message": f"Unknown action: {action}",
                    "available_actions": [
                        "translate_to_lzip",
                        "translate_from_lzip",
                        "batch_translate",
                        "get_dictionary",
                        "get_templates",
                        "get_version"
                    ]
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "action": action
            }


def create_server() -> LZIPMCPServer:
    """Factory function to create the MCP server"""
    return LZIPMCPServer()
