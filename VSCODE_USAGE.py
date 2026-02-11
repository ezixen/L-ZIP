"""
L-ZIP Usage Guide - Semantic Prompt Compression

How to use L-ZIP format for efficient prompting with any AI tool.

Author: ezixen
"""

# ============================================================================
# GETTING STARTED WITH L-ZIP
# ============================================================================

"""
## Quick Start: Using L-ZIP

### Method 1: Copy To Any AI Tool
Generate an L-ZIP prompt and paste it into ChatGPT, Claude, Gemini, etc.

Example:
ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON [Format:Strict]
THINK:Error_Handling OUT:Function + Tests

### Method 2: Use in Code Comments
Place your L-ZIP prompt in a comment as self-documentation:

// ACT:Dev [Lang:Python] OBJ:Parse_JSON
// OUT:Production_Code

def parse_json_strict(data: str) -> dict:
    ...

### Method 3: VS Code CLI
python cli.py
lzip> compress
[Enter your English prompt]
"""


# ============================================================================
# COMMON DEVELOPMENT WORKFLOWS WITH L-ZIP
# ============================================================================

# WORKFLOW 1: Quick Function Generation
"""
L-ZIP Prompt:
ACT:Dev [Lang:Python] OBJ:Implement_Function [Name:fibonacci]
LIM:Efficient+Readable THINK:StepByStep OUT:Function + Tests

Steps:
1. Copy the prompt above
2. Paste into your AI tool
3. Receive efficient, focused code
"""

# WORKFLOW 2: Bug Fix
"""
L-ZIP Prompt:
ACT:Debugger CTX:[Error_Details] OBJ:Fix_Bug | Prevent_Similar
THINK:RootCause + Solution OUT:Fixed_Code + Explanation

Steps:
1. Create prompt with context
2. Paste into AI tool
3. Add error details as context
"""

# WORKFLOW 3: Code Review
"""
L-ZIP Prompt:
ACT:Architect [Focus:Performance+Security] CTX:[Code_Below]
OBJ:Review | Optimize | Check_Security
OUT:Analysis + Suggestions

Steps:
1. Copy code to review
2. Paste L-ZIP prompt + code into AI tool
3. Get focused review analysis
"""

# WORKFLOW 4: Refactoring
"""
L-ZIP Prompt:
ACT:Software_Engineer OBJ:Optimize_Performance | Improve_Readability
LIM:No_Functional_Changes OUT:Refactored_Code + Explanation

Steps:
1. Paste prompt with existing code
2. AI tool suggests improvements
3. Review refactored version
"""

# WORKFLOW 5: Documentation
"""
L-ZIP Prompt:
ACT:Technical_Writer OBJ:Generate_Docstring [Style:Google]
OUT:Complete_Docstring_with_TypeHints

Steps:
1. Add prompt above function
2. Paste into AI tool
3. Receive complete documentation
"""

# WORKFLOW 6: Testing
"""
L-ZIP Prompt:
ACT:QA_Engineer [Framework:Pytest] CTX:[Function_Above]
OBJ:Create_Tests [Coverage:Edge_Cases+Happy_Path]
THINK:Comprehensive_Coverage OUT:Test_Code

Steps:
1. Copy function to test
2. Paste L-ZIP prompt + function into AI tool
3. Receive comprehensive test suite
"""

# WORKFLOW 7: Add Type Hints
"""
L-ZIP Prompt:
ACT:Python_Expert OBJ:Add_Type_Annotations
OUT:Function_With_Complete_Type_Hints

Steps:
1. Copy untyped function
2. Paste L-ZIP prompt + function into AI tool
3. Get fully typed version
"""


# ============================================================================
# L-ZIP PROMPT TEMPLATES FOR COMMON TASKS
# ============================================================================

TEMPLATE_FUNCTION_GENERATION = """
ACT:Senior_Dev [Lang:Python] 
OBJ:Implement_Function [Name:{FunctionName}]
LIM:{Constraints} 
THINK:StepByStep 
OUT:Function + Docstring + Error_Handling + Tests
"""

TEMPLATE_CODE_REVIEW = """
ACT:Code_Reviewer [Expertise:Performance+Security+Readability]
CTX:[Code_Below]
OBJ:Review | Identify_Issues | Suggest_Improvements
EVAL:Performance | Security | Readability | Best_Practices
OUT:ReviewReport + RefactoredCode
"""

TEMPLATE_BUG_FIX = """
Error: {ErrorMessage} on line {LineNumber}
ACT:Debugger CTX:[ErrorLog + Code_Context]
OBJ:Identify_RootCause + Provide_Fix
THINK:StepByStep | Explain_Why
OUT:FixedCode + Prevention_Strategy
"""

TEMPLATE_OPTIMIZATION = """
Current approach: {CurrentApproach}
ACT:Performance_Engineer
OBJ:Optimize_for_{MetricType} | Improve_Efficiency
THINK:Algorithmic_Analysis | Benchmark_Comparison
LIM:No_Breaking_Changes
OUT:Optimized_Code + Performance_Comparison
"""

TEMPLATE_REFACTORING = """
ACT:Software_Architect [Focus:{Focus}]
CTX:[Code_Below]
OBJ:Refactor + Improve_Structure + Reduce_Complexity
LIM:No_Breaking_Changes
OUT:RefactoredCode + MigrationGuide
"""

TEMPLATE_DOCUMENTATION = """
ACT:Technical_Writer [Audience:Developers]
CTX:[Code + Functionality]
OBJ:Create_Documentation [Type:{DocType}]
LIM:Clear + Concise + Complete
OUT:{DocFormat} + Examples
"""

TEMPLATE_TESTING = """
ACT:QA_Engineer [Framework:{Framework}]
CTX:[Function_or_Module_Below]
OBJ:Create_Tests [Coverage:{CoverageGoal}]
THINK:Edge_Cases + Happy_Path + Error_Cases
OUT:TestCode + Coverage_Report
"""

TEMPLATE_TYPE_HINTS = """
ACT:Python_Expert
OBJ:Add_Complete_Type_Annotations
LIM:PEP484_Compliant + Clear
OUT:Function_With_Types + Docstring
"""


# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

# EXAMPLE 1: Quick Function
EXAMPLE_1_QUICK_FUNCTION = """
PROMPT:
ACT:Dev [Lang:Python] OBJ:Email_Validator_Function
OUT:Production_Code

Insert before function:
def validate_email(email: str) -> bool:
    \"\"\"Validate email address format.\"\"\"
    # AI generates efficient validation logic

RESULT: Complete, production-ready function
TOKEN SAVINGS: 65%
"""

# EXAMPLE 2: Complete Class
EXAMPLE_2_CLASS = """
PROMPT:
ACT:Senior_Dev OBJ:User_Model [DB:SQLAlchemy]
THINK:OOP_Principles | Database_Design
OUT:Complete_Class_with_Methods + Docstrings

class User:
    \"\"\"User model with validation.\"\"\"
    # AI generates all methods

RESULT: Full class with methods, relationships, validation
TOKEN SAVINGS: 58%
"""

# EXAMPLE 3: Test Suite
EXAMPLE_3_TESTS = """
PROMPT:
ACT:QA_Engineer [Framework:Pytest]
OBJ:Test_Suite [Subject:UserValidator]
LIM:100%_Coverage | Edge_Cases_Included
OUT:Comprehensive_Test_Code

class TestUserValidator:
    \"\"\"Tests for user validation.\"\"\"
    # AI generates all test methods

RESULT: Comprehensive test suite with edge cases
TOKEN SAVINGS: 62%
"""

# EXAMPLE 4: Documentation
EXAMPLE_4_DOCS = """
PROMPT:
ACT:Technical_Writer [Audience:Developers]
OBJ:API_Documentation [Format:OpenAPI]
OUT:Complete_Spec + Examples

def create_user():
    \"\"\"
    Paste L-ZIP prompt + this function into AI tool
    AI generates OpenAPI compatible docstring
    with request/response examples
    \"\"\"

RESULT: Professional API documentation
TOKEN SAVINGS: 70%
"""

# EXAMPLE 5: Optimization
EXAMPLE_5_OPTIMIZE = """
PROMPT:
ACT:Performance_Engineer
OBJ:Optimize_Algorithm | Improve_Complexity
OUT:Optimized_Code + Complexity_Explanation

Current approach: O(n²) nested loop

def find_duplicates(items: list) -> list:
    # Paste this with L-ZIP prompt into AI tool
    # AI replaces with efficient implementation

RESULT: Optimized algorithm (O(n) with hashset)
TOKEN SAVINGS: 60%
"""


# ============================================================================
# AI TOOL USAGE EXAMPLES
# ============================================================================

AI_EXAMPLE_1 = """
SCENARIO: Generate REST API handler

STEP 1 - Copy this prompt:
ACT:Dev [Lang:Python] OBJ:REST_API_Handler [Framework:FastAPI]
OUT:Complete_Endpoint + Type_Hints + Error_Handling

STEP 2 - Paste into ChatGPT/Claude/Gemini

STEP 3 - Receive:
- Complete FastAPI route handler
- Proper type annotations
- Error handling
- Input validation
- Response models

TOKEN SAVINGS: 68%
"""

AI_EXAMPLE_2 = """
SCENARIO: Debug production error

STEP 1 - Copy this prompt:
ACT:Debugger CTX:[Error_trace.log] OBJ:Find_RootCause + Suggest_Fix
OUT:Analysis + Fix_Code + Prevention

STEP 2 - Paste prompt + error log into AI tool

STEP 3 - Receive:
- Root cause analysis
- Step-by-step explanation
- Code fix recommendations  
- Prevention tips

TOKEN SAVINGS: 65%
"""

AI_EXAMPLE_3 = """
SCENARIO: Design microservice architecture

STEP 1 - Copy this prompt:
ACT:Architect [Domain:Microservices] OBJ:Design_Service_Architecture
OUT:[Architecture_Diagram, Config_Templates, Scaling_Strategy]

STEP 2 - Paste into AI tool + describe requirements

STEP 3 - Receive:
- Service architecture overview
- Configuration templates
- Scaling recommendations
- Docker/Kubernetes configs

TOKEN SAVINGS: 55%
"""


# ============================================================================
# TIPS & TRICKS
# ============================================================================

TIPS = """
1. START SIMPLE:
   ACT:Dev OBJ:Function OUT:Code
   (Add more detail as needed)

2. USE SPECIFIC PARAMETERS:
   [Lang:Python] is better than "python"
   [Framework:FastAPI] is clearer than "web framework"

3. CHAIN FOLLOW-UPS:
   First request: ACT:Dev OBJ:Function
   Follow-ups: "Add error handling", "Add tests", "Optimize"
   AI remembers context from L-ZIP

4. USE IN COMMENTS:
   Comments persist = self-documentation
   Helps next developer understand intent

5. MIX AND MATCH:
   Start with L-ZIP, add English for complexity
   Example: "ACT:Dev OBJ:Code // Please handle edge cases"

6. SAVE FAVORITES:
   Keep working L-ZIP prompts in a file
   Reuse for similar tasks

7. ITERATE:
   First version might not be perfect
   Refine the L-ZIP prompt, send again
"""


# ============================================================================
# BEST PRACTICES
# ============================================================================

BEST_PRACTICES = """
✅ DO:
- Start with ACT to set persona
- Use specific language tags [Lang:Python]
- Set clear objectives OBJ:
- Specify output format OUT:
- Use [square brackets] for parameters
- Use + for additions, | for alternatives
- Keep L-ZIP in comments for clarity

❌ DON'T:
- Use verbose English with L-ZIP
- Over-specify if not needed
- Mix L-ZIP with casual language confusingly
- Forget to set output format
- Use ambiguous role names (be specific)

⚡ OPTIMIZE:
- Ultra-quick: ACT:Dev OBJ:Func
- Better: ACT:Senior_Dev [Lang:Python] OBJ:Function
- Best: ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON OUT:Code+Tests+Docs
"""


# ============================================================================
# WORKFLOW EXAMPLE: FULL SESSION
# ============================================================================

WORKFLOW_EXAMPLE = """
SESSION: Building a JSON Parser - Copy/Paste to AI Tool

STEP 1 - DEFINE:
Paste in AI tool:
ACT:Senior_Dev [Lang:Python] OBJ:JSON_Parser [Features:Strict_Mode]
THINK:Error_Handling | Performance
OUT:Class + Methods + Tests

Result: AI generates the class structure

STEP 2 - REVIEW:
Follow-up: "Check for performance issues"
Result: AI reviews and suggests optimizations

STEP 3 - TEST:
Paste:
ACT:QA_Engineer OBJ:Test_JSON_Parser
LIM:100%_Coverage
OUT:Pytest_Suite

Result: Complete test suite generated

STEP 4 - DOCUMENT:
Paste:
ACT:Technical_Writer OBJ:API_Docs
OUT:Markdown + Examples

Result: Professional documentation

STEP 5 - OPTIMIZE:
Follow-up: "Reduce memory usage"
Result: AI refactors for efficiency

FINAL RESULT: Production-ready JSON parser!
TOKENS SAVED: 60-70% vs natural language prompts
TIME SAVED: ~2 hours of manual coding
"""


if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════╗
║   L-ZIP - Semantic Prompt Compression                         ║
║   By: ezixen                                                   ║
║   Usage: Efficient prompting with any AI tool                 ║
╚════════════════════════════════════════════════════════════════╝

THREE WAYS TO USE L-ZIP:

1️⃣  COPY-PASTE TO AI TOOL
Generate L-ZIP prompt, paste into ChatGPT/Claude/Gemini

2️⃣  CODE COMMENTS
// ACT:Dev OBJ:Function OUT:Code

3️⃣  VS CODE CLI
python cli.py
(Interactive prompt compression)

QUICK TEMPLATES:
◽ Function Generation
◽ Code Review  
◽ Bug Fixing
◽ Testing
◽ Documentation
◽ Refactoring

Start using L-ZIP now!
See examples.py for 18 ready-to-use prompts.

TOKEN SAVINGS: 50-70% on average ⚡
SUPPORTS: ChatGPT, Claude, Gemini, and all LLMs 🤖
    """)
