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
    enable_symbols: bool = True  # Enable symbol replacements like => | +
    enable_extended_ops: bool = True  # Enable IMAGE, VIDEO, AUDIO operators


class LZIPTranslator:
    """Translates verbose English prompts to L-ZIP compact format"""
    
    # Core L-ZIP operators
    OPERATORS = {
        'ACT': 'Act as|role|persona|assume the role',
        'OBJ': 'objective|goal|task|create|write|develop|generate|produce',
        'LIM': 'limit|constraint|restrict|without|no |only|maximum|minimum|under |less than|more than',
        'CTX': 'context|background|given|based on|considering|with the following|assume|given that',
        'OUT': 'output|format|return|provide as|in the form of|as a|structure should be',
        'SUM': 'summarize|summary|top|key|main points|highlight',
        'GEN': 'generate|write|create|produce|make|build',
        'EVAL': 'evaluate|assess|analyze|critique|review|examine|check for',
        'THINK': 'think|reason|step by step|explain|breakdown|detail|walk through',
        'VIS': 'visualize|diagram|chart|graph|flowchart|draw|image|illustration|picture',
    }
    
    # Extended operators for specific domains
    EXTENDED_OPERATORS = {
        # Image/Visual generation
        'STYLE': 'style|artistic style|art style|look like|appearance',
        'MOOD': 'mood|feeling|atmosphere|vibe|emotion',
        'LIGHTING': 'lighting|light|illumination|shadows',
        'COLORS': 'colors|color scheme|palette|hues',
        'QUALITY': 'quality|resolution|detailed|detail level',
        'RATIO': 'aspect ratio|dimensions|size',
        'POSE': 'pose|position|posture|stance',
        'BG': 'background|backdrop|setting',
        'SUBJECT': 'subject|main subject|focus on',
        
        # Code/Technical
        'LANG': 'language|programming language|in language',
        'FRAMEWORK': 'framework|using framework|library',
        'PATTERN': 'pattern|design pattern|architecture',
        'PERF': 'performance|optimize|efficiency',
        'TEST': 'test|testing|unit test|integration test',
        
        # Content/Writing
        'TONE': 'tone|writing tone|voice',
        'AUDIENCE': 'audience|for audience|target',
        'LEN': 'length|word count|character count|long|short',
    }
    
    # Symbol replacements with word boundaries (SAFE - won't corrupt words)
    SYMBOL_MAP = {
        r'\b(and then|followed by|after that|next step)\b': '|',
        r'\b(and also|as well as|along with|combined with)\b': '+',
        r'\b(leads to|results in|implies|therefore|thus|consequently)\b': '=>',
        r'\b(becomes|transforms to|converts to|changes to)\b': '->',
        r'\b(or alternatively|or else)\b': '//',
        # Removed overly ambiguous: "for", "above", "except", "but not"
        # These have too many contextual meanings
    }
    
    # Common abbreviations (telegraphic compression - safe substitutions)
    ABBREVIATIONS = {
        # Scale/quantity
        r'\b(\d+),?000,?000\b': r'\1M',  # 5,000,000 -> 5M
        r'\b(\d+),?000\b': r'\1k',  # 5,000 -> 5k
        r'\bthousand\b': 'k',
        r'\bmillion\b': 'M',
        r'\bbillion\b': 'B',
        
        # Time
        r'\bseconds?\b': 's',
        r'\bminutes?\b': 'm',
        r'\bhours?\b': 'h',
        r'\bdays?\b': 'd',
        r'\bweeks?\b': 'w',
        r'\bmonths?\b': 'mo',
        r'\byears?\b': 'y',
        
        # Common tech terms (word boundaries - safe)
        r'\bimage\b': 'img',
        r'\bvideo\b': 'vid',
        r'\bdocument\b': 'doc',
        r'\bapplication\b': 'app',
        r'\bdatabase\b': 'db',
        r'\brepository\b': 'repo',
        r'\bconfiguration\b': 'config',
        r'\bauthentication\b': 'auth',
        r'\badministrator\b': 'admin',
        r'\benvironment\b': 'env',
        
        # Additional tech terms for better compression
        r'\bpython\b': 'Py',
        r'\btypescript\b': 'TS',
        r'\bjavascript\b': 'JS',
        r'\bkubernetes\b': 'K8s',
        r'\bdocker\b': 'DCK',
        r'\bapi\b': 'API',
        r'\bjson\b': 'JSON',
        r'\bxml\b': 'XML',
        r'\bhtml\b': 'HTML',
        r'\bcss\b': 'CSS',
        r'\brest\b': 'REST',
        r'\bhttp\b': 'HTTP',
        r'\bsql\b': 'SQL',
        r'\bnosql\b': 'NoSQL',
        r'\bgraphql\b': 'GQL',
        r'\bdevops\b': 'DevOps',
        r'\bcicd\b': 'CI/CD',
        r'\btesting\b': 'Test',
        r'\boptimiz\w*\b': 'Opt',
        r'\bperformance\b': 'Perf',
        r'\befficiency\b': 'Eff',
        r'\bsecurity\b': 'Sec',
        r'\breliability\b': 'Rel',
        r'\bscalability\b': 'Scale',
        r'\bmaintainability\b': 'Maint',
        r'\baccessibility\b': 'A11y',
    }
    
    # Technique detections - only specific multi-word phrases to avoid false matches
    TECHNIQUE_KEYWORDS = {
        'step by step': 'THINK:StepByStep',
        'chain of thought': 'THINK:ChainOfThought',
        'output as json': 'OUT:JSON',
        'return json': 'OUT:JSON',
        'as a table': 'OUT:Table',
        'in markdown': 'OUT:Markdown',
        'write code': 'GEN:Code',
        'generate script': 'GEN:Script',
        'bullet points': 'OUT:Bullets',
        'as a list': 'OUT:List',
        'provide list': 'OUT:List',
    }
    
    def __init__(self, config: LZIPConfig = None):
        self.config = config or LZIPConfig()
    
    def translate_to_lzip(self, english_prompt: str) -> Tuple[str, Dict[str, str]]:
        """
        Translate English prompt to L-ZIP format
        Returns: (lzip_prompt, metadata)
        """
        # Handle empty input
        if not english_prompt or not english_prompt.strip():
            metadata = {
                'original_length': 0,
                'original_tokens': 0,
                'original_text': english_prompt,
                'final_length': 0,
                'final_tokens': 0,
                'compression_ratio': 100.0,
            }
            return "", metadata
        
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
        
        # Step 6: Build final L-ZIP - ALWAYS include remaining text with operators
        if lzip_parts and remaining_text:
            final_lzip = ' '.join(lzip_parts) + ' ' + remaining_text
        elif lzip_parts:
            final_lzip = ' '.join(lzip_parts)
        elif remaining_text:
            final_lzip = remaining_text
        else:
            final_lzip = "UNCLASSIFIED"
        
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
            # "your objective is to write..." or "goal is to create..." 
            (r'(?:your\s+)?(?:objective|goal)\s+(?:is\s+)?(?:to\s+)?([a-z0-9_\s]{2,50}?)(?:\.|,|;|and|$)', 1),
            # Imperative commands at start: "Write X", "Create X" (excluding "provide" which is for OUT)
            (r'(?:^|\.\s+)(?:write|create|generate|produce|develop|design|analyze|summarize)\s+(?:a\s+)?([a-z0-9_\s]{2,45}?)(?:\.|,|;|for|with|about)', 1),
            # Direct action detection (fallback, more conservative)
            (r'(?<!to\s)(?:write|create|generate|produce|develop|design)\s+([a-z0-9_\s]{2,40}?)(?:\s+(?:about|for|with)|\.|\.|,|;|and)', 1),
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
            (r'(?:limit|restrict|maximum|under|no|without|only)\s+(?:the\s+)?(?:output\s+)?(?:to\s+)?([a-z0-9\s]{2,40}?)(?:[.,;]|and)', 1),
            (r'(?:under|less than|maximum of)\s+([0-9a-z\s]{2,40}?)(?:[.,;])', 1),
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
            # "output/format/provide as X" or "Use X formatting"
            (r'(?:output|format|return|provide|should be)\s+(?:as\s+)?(?:a\s+)?([a-z\s]{2,40}?)(?:[.,;]|$)', 1),
            # "Use X formatting/format/markup" pattern
            (r'use\s+([a-z]+)\s+(?:formatting|format|markup|style|structure)\b', 1),
            # "formatted as X" pattern
            (r'formatted?\s+as\s+(?:a\s+)?([a-z\s]{2,40}?)(?:[.,;]|$)', 1),
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
        
        # Look for technique keywords with word boundaries
        for keyword, operator in self.TECHNIQUE_KEYWORDS.items():
            # Use word boundary regex to avoid matching within words
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, remaining, re.IGNORECASE):
                operators.append(operator)
                # Use regex replacement with word boundaries
                remaining = re.sub(pattern, '', remaining, count=1, flags=re.IGNORECASE)
        
        # Look for extended operators if enabled (IMAGE, VIDEO, AUDIO specific)
        if self.config.enable_extended_ops:
            self._detect_extended_operators(operators, remaining)
        
        # Remove extra spaces
        remaining = re.sub(r'\s+', ' ', remaining).strip()
        
        return operators, remaining
    
    def _detect_extended_operators(self, operators: List[str], text: str) -> None:
        """Detect extended operators for specialized tasks (image, video, etc.)"""
        text_lower = text.lower()
        
        # Detect image-specific operators by keywords
        image_keywords = {
            'STYLE': ['realistic', 'anime', 'oil painting', 'sketch', '3d', 'cartoon', 'photorealistic'],
            'MOOD': ['happy', 'dark', 'cheerful', 'friendly', 'dramatic', 'mysterious', 'serene'],
            'LIGHTING': ['sunny', 'noon', 'golden hour', 'backlit', 'dramatic lighting', 'soft light'],
            'QUALITY': ['high quality', 'best quality', '4k', '8k', 'detailed', 'ultra detailed'],
            'RATIO': ['16:9', '9:16', '1:1', '4:3', '3:2', 'aspect ratio'],
        }
        
        for op, keywords in image_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    # Extract the specific value found
                    if keyword in ['16:9', '9:16', '1:1', '4:3', '3:2']:
                        operators.append(f'{op}:{keyword}')
                    elif keyword in ['4k', '8k']:
                        operators.append(f'QUALITY:{keyword.upper()}')
                    else:
                        value = keyword.replace(' ', '_').title()
                        operators.append(f'{op}:{value}')
                    break  # Only add each operator type once
    
    def _clean_text(self, text: str) -> str:
        """Clean up and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove quoted text (assume these are preserved)
        # Keep code blocks and examples
        
        return text.strip()
    
    def _compress_phrases(self, text: str) -> str:
        """Compress common phrases and filler words - CONSERVATIVE mode"""
        # Only remove truly redundant filler words, preserve content
        
        # Step 1: Apply abbreviations if enabled (telegraphic compression)
        if self.config.enable_symbols:
            # Apply number abbreviations first (5000 -> 5k, etc.)
            for pattern, replacement in self.ABBREVIATIONS.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Step 2: Apply symbol replacements if enabled (with word boundaries - SAFE)
        if self.config.enable_symbols:
            for pattern, replacement in self.SYMBOL_MAP.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Step 3: Remove only the most obvious filler words with strict word boundaries
        fillers = [
            r'\bplease\b',
            r'\bkindly\b',
            r'\bfor me\b',
            r'\bto me\b',
            r'\bthank you\b',
            r'\bi would like\b',
            r'\bif you could\b',
            r'\bif you can\b',
            r'\byou can\b',
            r'\bcan you\b',
            r'\bcould you\b',
        ]
        
        for filler in fillers:
            text = re.sub(filler, '', text, flags=re.IGNORECASE)
        
        # Step 4: Remove double spaces created by replacements
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def _normalize_role(self, role: str) -> str:
        """Normalize role names"""
        role = role.lower().strip()
        role_map = {
            # Compound roles (check first - longest match first)
            'senior developer': 'Senior_Dev',
            'data scientist': 'Data_Scientist',
            'software architect': 'Software_Architect',
            'machine learning': 'ML',
            'devops engineer': 'DevOps_Eng',
            # Single word roles
            'expert': 'Expert',
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
            'developer': 'Dev',
        }
        
        # Sort by length (longest first) to match compound roles before single words
        sorted_roles = sorted(role_map.items(), key=lambda x: len(x[0]), reverse=True)
        
        for key, val in sorted_roles:
            if key in role:
                return val
        
        return role.replace(' ', '_').title()
    
    def _shorten_term(self, term: str) -> str:
        """Shorten long terms into compact identifiers"""
        term = term.strip()
        
        # Remove only truly redundant articles and prepositions
        term = re.sub(r'\b(a|an|the)\b\s+', '', term, flags=re.IGNORECASE)
        
        # Convert to underscore format and title case for readability
        words = term.split()
        # Keep important words, capitalize them
        important_words = [w for w in words if len(w) > 2 or w.lower() in ['ai', 'ui', 'ux', 'db', 'id', 'io']]
        
        # Join with underscores and capitalize
        result = '_'.join(important_words)
        # Title case each word
        result = '_'.join(word.capitalize() for word in result.split('_'))
        
        return result if result else term.replace(' ', '_')
    
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
