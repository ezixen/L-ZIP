#!/usr/bin/env python3
"""
L-ZIP Extended - Comprehensive Operators for All Tasks
Supports: Code, Images, Videos, Audio, Writing, Analysis, and more
"""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ExtendedLZIPOperators:
    """Comprehensive L-ZIP operator library for all task types"""
    
    # UNIVERSAL OPERATORS (Work for all tasks)
    UNIVERSAL = {
        'ACT': 'Define role/persona/expertise level',
        'OBJ': 'Define objective/goal/task',
        'OUT': 'Specify output format/structure',
        'CTX': 'Provide context/background information',
        'LIM': 'Set constraints/limitations/rules',
        'THINK': 'Specify reasoning mode/approach',
        'SUM': 'Request summary/key points/highlights',
        'EVAL': 'Request evaluation/analysis criteria',
        'GEN': 'Specify generation type (Code/Text/Image)',
        'VIS': 'Request visualization/diagram/chart',
        'LEN': 'Set length constraints (word/token count)',
        'LANG': '[Language specification]',
        'FMT': 'Specify exact format requirements',
        'QUAL': '[Quality level: draft/normal/high/best]',
        'STYLE': '[Style/tone/mood specification]',
    }
    
    # CODE GENERATION OPERATORS
    CODE = {
        'LANG': '[Python|JavaScript|Java|C++|Go|Rust|TypeScript|SQL]',
        'FRAMEWORK': '[Django|FastAPI|React|Vue|SpringBoot|Flask]',
        'PATTERN': '[MVC|OOP|FP|Async|Event-Driven|Microservices]',
        'TYPE': '[Function|Class|Module|API|CLI|Library|Script]',
        'FEATURE': '[Authentication|Caching|Logging|Error-Handling|Testing]',
        'PERF': '[Optimize for: Speed|Memory|Readability|Security]',
        'DOC': '[Include: Docstring|TypeHints|Comments|Examples]',
        'TEST': '[Unit|Integration|E2E|Load|Security tests]',
        'ERR': '[Error handling strategy: Try/Catch|Validation|Assert]',
        'ARCH': '[Architecture: Monolithic|Microservices|Serverless|Distributed]',
    }
    
    # IMAGE/VISUAL GENERATION OPERATORS
    IMAGE = {
        'SUBJECT': '[Main subject description]',
        'BODY': '[Full-body|Bust|Headshot|Environmental|Landscape]',
        'STYLE': '[Photorealistic|Anime|Oil-Painting|Sketch|3D|Realistic|Cartoon]',
        'POSE': '[Standing|Sitting|Running|Flying|Dynamic|Profile|Frontal]',
        'MOOD': '[Cheerful|Dark|Romantic|Dramatic|Mysterious|Serene]',
        'LIGHTING': '[Soft|Hard|Dramatic|Backlit|Rim-Light|Golden-Hour]',
        'BG': '[Background: None|Blurred|Detailed|Pattern|Natural|Urban]',
        'COLORS': '[Color-Scheme: Warm|Cool|Muted|Vibrant|B&W|Sunset]',
        'COMPOSITION': '[Rule-of-Thirds|Centered|Leading-Lines|Symmetrical]',
        'QUALITY': '[Resolution: 512|768|1024|1440|2K|4K]',
        'RATIO': '[Aspect-Ratio: 1:1|16:9|9:16|2:3|3:2]',
        'FILTER': '[Vintage|Noir|HDR|Film|Cinematic|Toy|Watercolor]',
        'DETAIL': '[Level: Low|Medium|High|Ultra-Detailed|Balanced]',
    }
    
    # VIDEO GENERATION OPERATORS  
    VIDEO = {
        'DURATION': '[Length in seconds: 5|10|15|30|60]',
        'FPS': '[Frame-rate: 24|30|60]',
        'MOTION': '[Motion-type: Pan|Zoom|Rotate|Track|Static|Dynamic]',
        'TRANSITION': '[Transition: Cut|Fade|Dissolve|Slide|Wipe|Morph]',
        'EFFECT': '[Effects: Blur|Glow|Particle|Distortion|Wave|Tremor]',
        'MUSIC': '[Music: Upbeat|Calm|Epic|Ambient|Jazz|Classical|Custom]',
        'NARRATION': '[Voice: Male|Female|Neutral|Age|Accent|Tone]',
        'SCENE': '[Number of scenes/cuts required]',
        'SPEED': '[Playback-speed: Slow-Mo|Normal|Time-Lapse|Hyper-Speed]',
        'BEHAVIOR': '[Character/Object behavior: Idle|Walking|Talking|Interacting]',
    }
    
    # AUDIO/MUSIC GENERATION OPERATORS
    AUDIO = {
        'GENRE': '[Genre: Pop|Rock|Jazz|Classical|Electronic|Hip-Hop|Ambient]',
        'MOOD': '[Mood: Happy|Sad|Energetic|Calming|Dramatic|Mysterious]',
        'TEMPO': '[BPM: Slow(60-90)|Medium(90-120)|Fast(120-180)|Extreme(180+)]',
        'INSTRUMENT': '[Instruments: Piano|Guitar|Violin|Drums|Synth|Orchestra]',
        'DURATION': '[Length: 15s|30s|1m|3m|5m|Full-Track]',
        'VOICE': '[Voice-Type: Male|Female|Chorus|Narrator|Singer]',
        'ACCENT': '[Accent/Language: American|British|Neutral|Other]',
        'QUALITY': '[Audio-Quality: 128kbps|192kbps|320kbps|Lossless|Studio]',
        'EFFECT': '[Effects: Echo|Reverb|Compression|EQ|Distortion|Chorus]',
        'PRODUCTION': '[Style: Raw|Produced|Mixed|Mastered|Engineered]',
    }
    
    # WRITING/CONTENT OPERATORS
    WRITING = {
        'GENRE': '[Fiction|Non-Fiction|Poetry|Blog|Article|Script|Report]',
        'TONE': '[Formal|Casual|Academic|Creative|Journalistic|Technical]',
        'AUDIENCE': '[Audience: Children|Teens|Adults|Experts|General-Public]',
        'POV': '[Point-of-View: First|Second|Third|Omniscient|Limited]',
        'TENSE': '[Tense: Past|Present|Future|Mixed]',
        'VOICE': '[Voice: Active|Passive|Conversational|Authoritative]',
        'STRUCTURE': '[Structure: Linear|Non-Linear|Chronological|Thematic]',
        'EMOTION': '[Emotional-Tone: Humorous|Serious|Inspiring|Tragic|Dark]',
        'DIALECT': '[Dialect/Language-Style: Standard|Colloquial|Formal|Regional]',
        'LENGTH': '[Word-count: 100|500|1000|5000|10000]',
    }
    
    # ANALYSIS/RESEARCH OPERATORS
    ANALYSIS = {
        'METHOD': '[Analysis-Method: Statistical|Comparative|Causal|Trend|Predictive]',
        'DATA': '[Data-Type: Quantitative|Qualitative|Mixed|Time-Series|Cross-Sectional]',
        'SCOPE': '[Scope: Micro|Macro|Local|Global|Industry|Market]',
        'DEPTH': '[Depth: Surface|Moderate|Deep|Comprehensive|Expert-Level]',
        'FOCUS': '[Focus-Area: Market|Technology|Finance|Social|Environmental]',
        'BIAS': '[Bias-Awareness: Neutral|Pro|Critical|Devil-Advocate]',
        'EVIDENCE': '[Evidence-Required: High|Medium|Cited-Sources|Expert-Opinion]',
        'FRAMEWORK': '[Framework: SWOT|Porter|BCG|McKinsey|Custom]',
        'TIMELINE': '[Timeline: Historical|Current|Projected|Comparative]',
    }
    
    # SYMBOLS & CONNECTORS
    SYMBOLS = {
        '|': 'OR / Alternative / Either-Or',
        '+': 'AND / Addition / Both',
        '=>': 'IMPLIES / Leads-to / Therefore',
        '@': 'Apply-to / At / Location / Time-marker',
        '~': 'But / Except / With-caveat / Negation',
        '//': 'Or-else / Fallback / Alternative',
        '->': 'Results-in / Transforms-to / Becomes',
        '<>': 'Replace-with / Substitute / Swap',
        '[]': 'Parameter / Option / Specification',
        '{}': 'Variable / Placeholder / Dynamic-value',
        ':': 'Is / Defined-as / Specification-marker',
    }
    
    @classmethod
    def print_dictionary(cls):
        """Print complete L-ZIP operator dictionary"""
        print("\n" + "="*80)
        print("L-ZIP EXTENDED OPERATOR DICTIONARY")
        print("Complete Reference for All Tasks")
        print("="*80 + "\n")
        
        # Print each category
        categories = [
            ("UNIVERSAL OPERATORS", cls.UNIVERSAL),
            ("CODE GENERATION", cls.CODE),
            ("IMAGE/VISUAL GENERATION", cls.IMAGE),
            ("VIDEO GENERATION", cls.VIDEO),
            ("AUDIO/MUSIC GENERATION", cls.AUDIO),
            ("WRITING/CONTENT", cls.WRITING),
            ("ANALYSIS/RESEARCH", cls.ANALYSIS),
        ]
        
        for category_name, operators in categories:
            print(f"\n{category_name}")
            print("-" * 80)
            max_len = max(len(k) for k in operators.keys())
            
            for operator, description in operators.items():
                print(f"  {operator:<{max_len}}  →  {description}")
        
        # Print symbols
        print(f"\nSYMBOLS & CONNECTORS")
        print("-" * 80)
        max_len = max(len(k) for k in cls.SYMBOLS.keys())
        for symbol, meaning in cls.SYMBOLS.items():
            print(f"  {symbol:<{max_len}}  →  {meaning}")
        
        print("\n" + "="*80)


# EXAMPLE TRANSFORMATIONS FOR DIFFERENT TASK TYPES
EXAMPLES = {
    'CODE': {
        'original': 'Write me a Python function that takes a list of numbers and returns the sum of all even numbers. Include error handling and docstring.',
        'lzip': 'ACT:Senior_Dev [LANG:Python] OBJ:Sum_Even_Numbers OUT:Function+Docstring+ErrorHandling',
        'savings': '73%'
    },
    'IMAGE': {
        'original': 'Create a picture tall, slim male magician in his 30s, his full body is on the picture, no backfround, warm smile, charismatic, and has big, kind eyes. Elegantly dressed in a 3 piece black suite with red lining, top hat, and fitting elegant shoes. Generate it in best quality you can.',
        'lzip_v1': 'VIS:[Magician_Male_30s] [BODY:Tall+Slim+Full-Body] [STYLE:Elegant+Professional] [POSE:Standing] [BG:None] [MOOD:Charismatic+Warm] [DETAIL:High] QUAL:Best',
        'lzip_v2': 'GEN:Portrait [SUBJECT:Male_Magician_30s_Tall_Slim] [OUTFIT:Black_3Piece_Suit+Red_Lining+Top_Hat] [EXPRESSION:Warm_Smile+Kind_Eyes] [BODY:Full-Body] [POSE:Frontal] [BG:None] [LIGHTING:Professional] OUT:HQ_Image',
        'savings': '75%'
    },
    'VIDEO': {
        'original': 'Create a 30 second video of a magician performing a card trick. Include dramatic lighting and smooth camera movements. Add upbeat music and show his reactions.',
        'lzip': 'GEN:Video [DURATION:30s] [SUBJECT:Magician_Card_Trick] [MOTION:Smooth_Pan+Dynamic] [LIGHTING:Dramatic] [MUSIC:Upbeat] [BEHAVIOR:Performing+Reacting] [EFFECT:Cinematic]',
        'savings': '68%'
    },
    'AUDIO': {
        'original': 'Generate a 1-minute ambient music track with calm, peaceful vibes. Use piano and light string instruments. Include subtle sound effects like rain or wind.',
        'lzip': 'GEN:Audio [GENRE:Ambient] [MOOD:Peaceful+Calm] [INSTRUMENT:Piano|Strings] [DURATION:1m] [EFFECT:Rain+Wind] [QUALITY:Studio]',
        'savings': '71%'
    },
    'WRITING': {
        'original': 'Write a short blog post (500 words) about the benefits of meditation for beginners. Use a casual, friendly tone and include practical tips.',
        'lzip': 'ACT:Wellness_Blogger OBJ:Benefits_Meditation_Beginners OUT:Blog_Post [LEN:500w] [TONE:Casual+Friendly] CTX:[Practical_Tips]',
        'savings': '64%'
    },
    'ANALYSIS': {
        'original': 'Analyze the impact of artificial intelligence on job market trends over the last 5 years. Compare different industries and provide predictions for the next 3 years.',
        'lzip': 'ACT:Market_Analyst OBJ:AI_Job_Market_Impact [TIMELINE:Historical_5yr+Predictive_3yr] [SCOPE:Industry+Comparative] [METHOD:Trend+Predictive] OUT:Analysis_Report',
        'savings': '67%'
    },
}


def main():
    """Display operator dictionary and examples"""
    
    # Print operator dictionary
    ExtendedLZIPOperators.print_dictionary()
    
    # Print examples
    print("\n" + "="*80)
    print("COMPREHENSIVE EXAMPLES BY TASK TYPE")
    print("="*80)
    
    for task_type, example in EXAMPLES.items():
        print(f"\n\n{task_type} GENERATION EXAMPLE")
        print("-" * 80)
        print(f"\n📝 ORIGINAL ({len(example['original'].split())} words):")
        print(f"  {example['original']}")
        
        if task_type == 'IMAGE':
            print(f"\n✓ L-ZIP VERSION 1 (Detailed):")
            print(f"  {example['lzip_v1']}")
            print(f"\n✓ L-ZIP VERSION 2 (Comprehensive):")
            print(f"  {example['lzip_v2']}")
        else:
            print(f"\n✓ L-ZIP VERSION:")
            print(f"  {example['lzip']}")
        
        print(f"\n💾 Token Savings: {example['savings']}")
    
    print("\n" + "="*80)
    print("END OF REFERENCE GUIDE")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
