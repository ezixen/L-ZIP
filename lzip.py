"""
L-ZIP (Logic-based Zero-redundancy Information Prompting) Translator
Converts verbose English prompts into compact L-ZIP format to reduce token usage by 40-70%
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class LZIPConfig:
    """Configuration for L-ZIP translation"""
    aggressive_mode: bool = False  # More aggressive compression
    preserve_examples: bool = True  # Keep code examples untouched
    include_annotations: bool = False  # Add // explanations
    min_phrase_length: int = 3  # Min words before converting


class LZIPTranslator:
    """Translates verbose English prompts to L-ZIP compact format"""
    
    # Core L-ZIP operators
    OPERATORS = {
        'ACT': 'Act as|role|persona|assume the role',
        'OBJ': 'objective|goal|task|create|write|develop|generate|produce',
        'LIM': 'limit|constraint|restrict|without|no |only|maximum|minimum|under |less than|more than',
        'CTX': 'context|background|given|based on|considering|with the following|assume|given that',
        'OUT': 'output|format|return|provide as|in the form of|as a|structure should be',
        'SUM': 'summarize|summary|list|top|key|main points|highlight',
        'GEN': 'generate|write|create|produce|make|build|code|script|function',
        'EVAL': 'evaluate|assess|analyze|critique|review|examine|check for',
        'THINK': 'think|reason|step by step|explain|breakdown|detail|walk through',
        'VIS': 'visualize|diagram|chart|graph|flowchart|draw|image|illustration',
    }
    
    # Phrase mappings for common expressions
    PHRASE_MAP = {
        # Imperatives & requests
        r'\bplease\b': '',
        r'\byou should\b': '',
        r'\bi want you to\b': '',
        r'\bcan you\b': '',
        r'\bcould you\b': '',
        r'\byou must\b': '',
        r'\bmake sure you\b': '',
        
        # Verbose connectors
        r'\band then\b': '|',
        r'\bfollowed by\b': '|',
        r'\bas well as\b': '+',
        r'\balso\b': '+',
        r'\bincluding\b': '+',
        r'\bwith the addition of\b': '+',
        r'\badditionally\b': '+',
        
        # Results & implications
        r'\bresult in\b': '=>',
        r'\bleading to\b': '=>',
        r'\bwhich leads to\b': '=>',
        r'\bthus\b': '=>',
        r'\ntherefore\b': '=>',
        r'\bconsequently\b': '=>',
        
        # Comparisons
        r'\bor\b': '|',
        r'\beither\s+(.+?)\s+or\b': r'\1/',
        
        # Temporal
        r'\bwithin\s+(\d+)\s+(days|hours|weeks|months|years)\b': r'@\1\2_abbr',
        r'\bby\s+(\w+)\b': r'@\1',
        r'\tat\s+(\w+)\b': r'@\1',
        
        # Filler words
        r'\breally\b': '',
        r'\bvery\b': '',
        r'\bactually\b': '',
        r'\bjust\b': '',
        r'\bbasically\b': '',
        r'\bassentially\b': '',
    }
    
    # Phrase abbreviations
    PHRASE_ABBREV = {
        'and': '+',
        'or': '|',
        'then': '|',
        'follows': '|',
        'leading': '=>',
        'results': '=>',
        'implies': '=>',
        'therefore': '=>',
        'thus': '=>',
        'consequently': '=>',
        'but': '~',  # with caveat
        'except': '~',
        'unless': '~',
    }
    
    # Technique detections
    TECHNIQUE_KEYWORDS = {
        'step by step': 'THINK:StepByStep',
        'chain of thought': 'THINK:ChainOfThought',
        'json': 'OUT:JSON',
        'table': 'OUT:Table',
        'markdown': 'OUT:Markdown',
        'code': 'GEN:Code',
        'script': 'GEN:Script',
        'function': 'GEN:Function',
        'bullet points': 'OUT:Bullets',
        'list': 'OUT:List',
        'concise': 'LIM:Concise',
        'detailed': 'LIM:Detailed',
        'brief': 'LIM:Brief',
        'example': 'CTX:Example',
        'bug': 'EVAL:Bugs',
        'security': 'EVAL:Security',
        'performance': 'EVAL:Performance',
    }
    
    def __init__(self, config: LZIPConfig = None):
        self.config = config or LZIPConfig()
    
    def translate_to_lzip(self, english_prompt: str) -> Tuple[str, Dict[str, str]]:
        """
        Translate English prompt to L-ZIP format
        Returns: (lzip_prompt, metadata)
        """
        metadata = {
            'original_length': len(english_prompt.split()),
            'original_tokens': len(english_prompt) // 4,  # Rough estimate
        }
        
        # Step 1: Pre-process text
        processed = english_prompt.lower()
        processed = self._clean_text(processed)
        
        # Step 2: Compress common phrases early
        processed = self._compress_phrases(processed)
        
        # Step 3: Extract structured information
        lzip_parts = []
        remaining_text = processed
        
        # Step 4: Detect and extract operators
        lzip_parts, remaining_text = self._extract_operators(remaining_text)
        
        # Step 5: Final cleanup
        remaining_text = self._clean_text(remaining_text)
        remaining_text = re.sub(r'\s+', ' ', remaining_text).strip()
        
        # Step 6: Build final L-ZIP
        if lzip_parts:
            final_lzip = ' '.join(lzip_parts)
        else:
            final_lzip = remaining_text[:100] if remaining_text else "UNCLASSIFIED"
        
        # Calculate compression stats
        metadata['final_length'] = len(final_lzip.split())
        metadata['final_tokens'] = len(final_lzip) // 4
        metadata['compression_ratio'] = round(
            (1 - metadata['final_tokens'] / max(metadata['original_tokens'], 1)) * 100, 1
        )
        
        return final_lzip, metadata
    
    def _extract_operators(self, text: str) -> Tuple[List[str], str]:
        """Extract L-ZIP operators from text"""
        operators = []
        remaining = text
        
        # Look for ACT (persona detection)
        act_patterns = [
            (r'(?:act as|role|persona|assume|be a?)\s+([a-z\s]{2,30}?)(?:[.,;]|and|then|who|that)', 1),
            (r'\b(senior|expert|professional|experienced)\s+([a-z]+)(?:\s+(developer|engineer|architect|analyst))?', 2),
        ]
        
        for pattern, group in act_patterns:
            try:
                match = re.search(pattern, remaining, re.IGNORECASE)
                if match:
                    role = match.group(group).strip()[:40]
                    if len(role) > 1:
                        role = self._normalize_role(role)
                        operators.append(f'ACT:{role}')
                        remaining = remaining[:match.start()] + ' ' + remaining[match.end():]
                        break
            except:
                pass
        
        # Look for OBJ (objective detection)  
        obj_patterns = [
            (r'(?:write|create|generate|produce|develop|design)\s+([a-z\s]{2,50}?)(?:[.,;]|and|for|to)', 1),
            (r'(?:objective|goal)\s+(?:is\s+to\s+)?(?:write|create)?\s+([a-z\s]{2,50}?)(?:[.,;])',  1),
        ]
        
        for pattern, group in obj_patterns:
            try:
                match = re.search(pattern, remaining, re.IGNORECASE)
                if match:
                    objective = match.group(group).strip()[:50]
                    objective = self._shorten_term(objective)
                    if len(objective) > 1:
                        operators.append(f'OBJ:{objective}')
                        remaining = remaining[:match.start()] + ' ' + remaining[match.end():]
                        break
            except:
                pass
        
        # Look for LIM (constraints)
        lim_patterns = [
            (r'(?:without|no|only|limit|restrict|maximum)\s+([a-z\s]{2,40}?)(?:[.,;]|and)', 1),
        ]
        
        for pattern, group in lim_patterns:
            try:
                match = re.search(pattern, remaining, re.IGNORECASE)
                if match:
                    constraint = match.group(group).strip()[:40]
                    if len(constraint) > 1:
                        operators.append(f'LIM:{constraint}')
                        remaining = remaining[:match.start()] + ' ' + remaining[match.end():]
                        break
            except:
                pass
        
        # Look for OUT (output format)
        out_patterns = [
            (r'(?:output|format|return|provide)\s+(?:as\s+)?(?:a\s+)?([a-z\s]{2,40}?)(?:[.,;]|$)', 1),
        ]
        
        for pattern, group in out_patterns:
            try:
                match = re.search(pattern, remaining, re.IGNORECASE)
                if match:
                    output_format = match.group(group).strip()[:40]
                    if len(output_format) > 1:
                        output_format = self._normalize_output(output_format)
                        operators.append(f'OUT:{output_format}')
                        remaining = remaining[:match.start()] + ' ' + remaining[match.end():]
                        break
            except:
                pass
        
        # Look for technique keywords
        for keyword, operator in self.TECHNIQUE_KEYWORDS.items():
            if keyword.lower() in remaining.lower():
                operators.append(operator)
                remaining = remaining.replace(keyword, '', count=1)
        
        # Remove extra spaces
        remaining = re.sub(r'\s+', ' ', remaining).strip()
        
        return operators, remaining
    
    def _clean_text(self, text: str) -> str:
        """Clean up and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove quoted text (assume these are preserved)
        # Keep code blocks and examples
        
        return text.strip()
    
    def _compress_phrases(self, text: str) -> str:
        """Compress common phrases and filler words"""
        # Apply phrase replacements
        for pattern, replacement in self.PHRASE_MAP.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Remove common filler words more aggressively
        fillers = [
            r'\b(please|kindly|would you|can you|could you|would|could|should|may|might)\b',
            r'\b(very|really|actually|basically|essentially|obviously|certainly|just|simply|only)\b',
            r'\b(that|this|this is|that is)\b\s*',
            r'\b(a\s+|an\s+|the\s+)(?=[a-z])',  # Remove articles before nouns
            r'\s*\b(for me|to me|to us|from me)\b',
        ]
        
        for filler in fillers:
            text = re.sub(filler, '', text, flags=re.IGNORECASE, count=5)
        
        # Remove double spaces created by replacements
        text = re.sub(r'\s+', ' ', text)
        
        # Remove redundant punctuation
        text = re.sub(r'[,;:]+\s*$', '', text)
        text = re.sub(r'[,;:]+', ',', text)  # Consolidate multiple punctuation
        
        return text.strip()
    
    def _normalize_role(self, role: str) -> str:
        """Normalize role names"""
        role = role.lower().strip()
        role_map = {
            'expert': 'Expert',
            'senior developer': 'Senior_Dev',
            'architect': 'Architect',
            'analyst': 'Analyst',
            'consultant': 'Consultant',
            'teacher': 'Teacher',
            'writer': 'Writer',
            'designer': 'Designer',
            'engineer': 'Engineer',
            'scientist': 'Scientist',
            'researcher': 'Researcher',
            'doctor': 'Doctor',
            'lawyer': 'Lawyer',
        }
        
        for key, val in role_map.items():
            if key in role:
                return val
        
        return role.replace(' ', '_').title()
    
    def _shorten_term(self, term: str) -> str:
        """Shorten long terms"""
        term = term.strip()
        
        # Remove articles and small words
        term = re.sub(r'\b(a|an|the|for|to|and|or)\b\s*', '', term, flags=re.IGNORECASE)
        
        # Convert to underscore format
        term = term.replace(' ', '_')
        
        return term
    
    def _normalize_output(self, output: str) -> str:
        """Normalize output format names"""
        output = output.lower().strip()
        output_map = {
            'json': 'JSON',
            'csv': 'CSV',
            'table': 'Table',
            'markdown': 'Markdown',
            'html': 'HTML',
            'xml': 'XML',
            'yaml': 'YAML',
            'python': 'Python',
            'javascript': 'JavaScript',
            'code': 'Code',
            'list': 'List',
            'bullet': 'Bullets',
            'paragraph': 'Paragraph',
        }
        
        for key, val in output_map.items():
            if key in output:
                return val
        
        return '+'.join(output.split())
    
    def translate_from_lzip(self, lzip_prompt: str) -> str:
        """Translate L-ZIP back to readable English"""
        english = lzip_prompt
        
        # Replace operators with English
        english = re.sub(r'ACT:(\w+)', r'Act as \1', english)
        english = re.sub(r'OBJ:(\w+)', r'Objective: \1', english)
        english = re.sub(r'LIM:(\w+)', r'Limit: \1', english)
        english = re.sub(r'CTX:(\w+)', r'Context: \1', english)
        english = re.sub(r'OUT:(\w+)', r'Output format: \1', english)
        english = re.sub(r'=>', 'leading to', english)
        english = re.sub(r'\|', 'and then', english)
        english = re.sub(r'@(\w+)', r'at \1', english)
        
        return english
    
    def get_compression_report(self, original: str, compressed: str) -> Dict:
        """Generate a detailed compression report"""
        original_words = len(original.split())
        compressed_words = len(compressed.split())
        original_tokens = len(original) // 4  # Rough estimate
        compressed_tokens = len(compressed) // 4
        
        return {
            'original_words': original_words,
            'compressed_words': compressed_words,
            'word_reduction': f"{(1 - compressed_words/max(original_words, 1)) * 100:.1f}%",
            'original_tokens': original_tokens,
            'compressed_tokens': compressed_tokens,
            'token_reduction': f"{(1 - compressed_tokens/max(original_tokens, 1)) * 100:.1f}%",
            'efficiency_gain': f"{(1 - compressed_tokens/max(original_tokens, 1)) * 100:.1f}%",
        }


def create_translator(aggressive: bool = False) -> LZIPTranslator:
    """Factory function to create a translator instance"""
    config = LZIPConfig(aggressive_mode=aggressive)
    return LZIPTranslator(config)
