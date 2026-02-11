"""
L-ZIP in VS Code - Developer Guide

How to use L-ZIP format for efficient prompting in VS Code and GitHub Copilot.

Author: ezixen
"""

# ============================================================================
# USING L-ZIP WITH GITHUB COPILOT IN VS CODE
# ============================================================================

"""
## Quick Start: Using L-ZIP in VS Code

### Method 1: In Code Comments
Place your L-ZIP prompt in a comment and let Copilot generate code:

// ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON [Format:Strict]
// THINK:Error_Handling OUT:Function + Tests
def parse_json_strict(data: str) -> dict:
    ...

### Method 2: Inline Prompts
Ask Copilot with L-ZIP format:

# ACT:Dev OBJ:Generate_Test [Coverage:Unit] OUT:Pytest

### Method 3: Chat with Copilot
Use L-ZIP in Copilot Chat:
- Select code or open chat
- Type: "ACT:Reviewer [Lang:Python] OBJ:Optimize OUT:Refactored_Code"
- Press Enter
"""


# ============================================================================
# COMMON DEVELOPMENT WORKFLOWS WITH L-ZIP
# ============================================================================

# WORKFLOW 1: Quick Function Generation
"""
// ACT:Dev [Lang:Python] OBJ:Implement_Function [Name:fibonacci]
// LIM:Efficient+Readable THINK:StepByStep OUT:Function + Tests
def fibonacci(n: int) -> int:
    ...
"""

# WORKFLOW 2: Bug Fix
"""
# Error: IndexError on line 45
# ACT:Debugger CTX:[Error_Details] OBJ:Fix_Bug | Prevent_Similar
# THINK:RootCause + Solution OUT:Fixed_Code + Explanation
"""

# WORKFLOW 3: Code Review
"""
# ACT:Architect [Focus:Performance+Security] CTX:[Code_Below]
# OBJ:Review | Optimize | Check_Security
# OUT:Analysis + Suggestions
def expensive_operation():
    ...
"""

# WORKFLOW 4: Refactoring
"""
# Current code below uses nested loops - inefficient
# ACT:Software_Engineer OBJ:Optimize_Performance | Improve_Readability
# LIM:No_Functional_Changes OUT:Refactored_Code + Explanation
"""

# WORKFLOW 5: Documentation
"""
// ACT:Technical_Writer OBJ:Generate_Docstring [Style:Google]
// OUT:Complete_Docstring_with_TypeHints
def complex_function(param1, param2, param3):
    ...
"""

# WORKFLOW 6: Testing
"""
# ACT:QA_Engineer [Framework:Pytest] CTX:[Function_Above]
# OBJ:Create_Tests [Coverage:Edge_Cases+Happy_Path]
# THINK:Comprehensive_Coverage OUT:Test_Code
"""

# WORKFLOW 7: Add Type Hints
"""
# ACT:Python_Expert OBJ:Add_Type_Annotations
# OUT:Function_With_Complete_Type_Hints
def process_data(data, filter_func, transform_func):
    ...
"""


# ============================================================================
# L-ZIP PROMPT TEMPLATES FOR COMMON TASKS
# ============================================================================

TEMPLATE_FUNCTION_GENERATION = """
// ACT:Senior_Dev [Lang:Python] 
// OBJ:Implement_Function [Name:{FunctionName}]
// LIM:{Constraints} 
// THINK:StepByStep 
// OUT:Function + Docstring + Error_Handling + Tests
"""

TEMPLATE_CODE_REVIEW = """
// ACT:Code_Reviewer [Expertise:Performance+Security+Readability]
// CTX:[Code_Below]
// OBJ:Review | Identify_Issues | Suggest_Improvements
// EVAL:Performance | Security | Readability | Best_Practices
// OUT:ReviewReport + RefactoredCode
"""

TEMPLATE_BUG_FIX = """
// Error: {ErrorMessage} on line {LineNumber}
// ACT:Debugger CTX:[ErrorLog + Code_Context]
// OBJ:Identify_RootCause + Provide_Fix
// THINK:StepByStep | Explain_Why
// OUT:FixedCode + Prevention_Strategy
"""

TEMPLATE_OPTIMIZATION = """
// Current approach: {CurrentApproach}
// ACT:Performance_Engineer
// OBJ:Optimize_for_{MetricType} | Improve_Efficiency
// THINK:Algorithmic_Analysis | Benchmark_Comparison
// LIM:No_Breaking_Changes
// OUT:Optimized_Code + Performance_Comparison
"""

TEMPLATE_REFACTORING = """
// ACT:Software_Architect [Focus:{Focus}]
// CTX:[Code_Below]
// OBJ:Refactor + Improve_Structure + Reduce_Complexity
// LIM:No_Breaking_Changes
// OUT:RefactoredCode + MigrationGuide
"""

TEMPLATE_DOCUMENTATION = """
// ACT:Technical_Writer [Audience:Developers]
// CTX:[Code + Functionality]
// OBJ:Create_Documentation [Type:{DocType}]
// LIM:Clear + Concise + Complete
// OUT:{DocFormat} + Examples
"""

TEMPLATE_TESTING = """
// ACT:QA_Engineer [Framework:{Framework}]
// CTX:[Function_or_Module_Above]
// OBJ:Create_Tests [Coverage:{CoverageGoal}]
// THINK:Edge_Cases + Happy_Path + Error_Cases
// OUT:TestCode + Coverage_Report
"""

TEMPLATE_TYPE_HINTS = """
// ACT:Python_Expert
// OBJ:Add_Complete_Type_Annotations
// LIM:PEP484_Compliant + Clear
// OUT:Function_With_Types + Docstring
"""


# ============================================================================
# HOW TO USE WITH GITHUB COPILOT CHAT
# ============================================================================

"""
STEPS TO USE L-ZIP WITH COPILOT CHAT:

1. Open Copilot Chat (Ctrl+Shift+I or Cmd+Shift+I)

2. Type your L-ZIP prompt:
   "ACT:Senior_Dev [Lang:Python] OBJ:Write_API_Handler THINK:DDD OUT:FastAPI_Code"

3. To make it context-aware, mention:
   - @workspace for workspace files
   - @terminal for terminal context
   - Select code snippet first

4. Examples:

   Example A (Simple):
   ACT:Dev OBJ:Python_Code OUT:Quick_Function

   Example B (Complex):
   ACT:Architect [Expertise:Web_Dev] CTX:[Current_Project]
   OBJ:Design_API_Structure | Build_Endpoints
   OUT:[Architecture_Diagram, Code_Skeleton, Database_Schema]

   Example C (With Selection):
   [Select some buggy code]
   ACT:Debugger OBJ:Fix_Bug | Explain_Why OUT:Fixed_Code

5. Use follow-ups:
   "More detailed"
   "Add error handling"
   "Include tests"
   "Optimize performance"
"""


# ============================================================================
# REAL-WORLD EXAMPLES IN VS CODE
# ============================================================================

# EXAMPLE 1: Quick Function
PREFIX_1_QUICK_FUNCTION = """
// ACT:Dev [Lang:Python] OBJ:Email_Validator_Function
// OUT:Production_Code

def validate_email(email: str) -> bool:
    """Validate email address format."""
    # Copilot will generate efficient validation logic
"""

# EXAMPLE 2: Complete Class
PREFIX_2_CLASS = """
// ACT:Senior_Dev OBJ:User_Model [DB:SQLAlchemy]
// THINK:OOP_Principles | Database_Design
// OUT:Complete_Class_with_Methods + Docstrings

class User:
    """User model with validation."""
    # Copilot generates all methods
"""

# EXAMPLE 3: Test Suite
PREFIX_3_TESTS = """
# ACT:QA_Engineer [Framework:Pytest]
# OBJ:Test_Suite [Subject:UserValidator]
# LIM:100%_Coverage | Edge_Cases_Included
# OUT:Comprehensive_Test_Code

class TestUserValidator:
    """Tests for user validation."""
    # Copilot generates all test methods
"""

# EXAMPLE 4: Documentation
PREFIX_4_DOCS = """
// ACT:Technical_Writer [Audience:Developers]
// OBJ:API_Documentation [Format:OpenAPI]
// OUT:Complete_Spec + Examples

def create_user():
    \"\"\"
    Copilot generates OpenAPI compatible docstring
    with request/response examples
    \"\"\"
"""

# EXAMPLE 5: Optimization
PREFIX_5_OPTIMIZE = """
# Current approach: O(n²) nested loop
# ACT:Performance_Engineer
# OBJ:Optimize_Algorithm | Improve_Complexity
# OUT:Optimized_Code + Complexity_Explanation

def find_duplicates(items: list) -> list:
    # Copilot replaces with efficient algo (hashset, etc)
"""


# ============================================================================
# COPILOT CHAT EXAMPLES
# ============================================================================

CHAT_EXAMPLE_1 = """
USER INPUT (in Copilot Chat):
ACT:Dev [Lang:Python] OBJ:REST_API_Handler [Framework:FastAPI]
OUT:Complete_Endpoint + Type_Hints + Error_Handling

EXPECTED OUTPUT:
Copilot generates a complete FastAPI route handler with:
- Proper type annotations
- Error handling
- Input validation
- Response models
"""

CHAT_EXAMPLE_2 = """
USER INPUT (in Copilot Chat):
ACT:Debugger CTX:[Error_trace.log] OBJ:Find_RootCause OBJ:Suggest_Fix

EXPECTED OUTPUT:
Copilot analyzes error trace andProvides:
- Root cause analysis
- Step-by-step explanation
- Code fix recommendations
- Prevention tips
"""

CHAT_EXAMPLE_3 = """
USER INPUT (in Copilot Chat):
ACT:Architect [Domain:Microservices] OBJ:Design_Service_Architecture
OUT:[Architecture_Diagram, Config_Files, Scaling_Strategy]

EXPECTED OUTPUT:
Copilot generates:
- Service architecture overview
- Configuration templates
- Scaling recommendations
- Docker/Kubernetes configs
"""


# ============================================================================
# TIPS & TRICKS FOR VS CODE
# ============================================================================

TIPS = """
1. USE KEYBOARD SHORTCUTS:
   - Ctrl+I: Copilot inline suggestions
   - Ctrl+Shift+I: Copilot chat
   - Ctrl+Shift+A: Accept suggestion

2. LEVERAGE CONTEXT:
   - Select code before asking
   - Mention files with @filename
   - Use @workspace for project context

3. CHAIN PROMPTS:
   First:  "ACT:Dev OBJ:Write_Function"
   Then:   "Add error handling"
   Then:   "Add type hints"
   Then:   "Generate tests"

4. USE L-ZIP IN COMMENTS:
   They persist in code = self-documenting
   Copilot understands context better

5. COMBINE WITH EXTENSIONS:
   - GitLens for blame/history
   - Error Lens for inline errors
   - Thunder Client for API testing

6. SAVE TEMPLATES:
   Create .vscode/snippets.json with L-ZIP templates
   Triggers: "lzip-func", "lzip-test", "lzip-review"

7. FOLLOW-UP NATURALLY:
   L-ZIP: "ACT:Dev OBJ:Function"
   Then just say: "Add docstring", "Optimize it", "Test edge cases"
   Copilot remembers the L-ZIP context
"""


# ============================================================================
# BEST PRACTICES IN VS CODE
# ============================================================================

BEST_PRACTICES = """
✅ DO:
- Start with ACT to set persona
- Use specific language tags
- Set clear objectives
- Specify output format
- Use [square brackets] for params
- Use + for additions, | for alternatives
- Keep L-ZIP in comments for clarity

❌ DON'T:
- Use verbose English with L-ZIP
- Over-specify if not needed
- Mix L-ZIP with natural language
- Forget to set output format
- Use ambiguous role names

⚡ OPTIMIZE:
- Ultra-quick: ACT:Dev OBJ:Func
- Better: ACT:Senior_Dev [Lang:Python] OBJ:Function
- Best: ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON OUT:Code+Tests
"""


# ============================================================================
# WORKFLOW EXAMPLE: FULL SESSION
# ============================================================================

WORKFLOW_EXAMPLE = """
SESSION: Building a JSON Parser

Step 1 - DEFINE:
Comment:
// ACT:Senior_Dev [Lang:Python] OBJ:JSON_Parser [Features:Strict_Mode]
// THINK:Error_Handling | Performance
// OUT:Class + Methods + Tests

Copilot generates the class structure

Step 2 - REVIEW:
You: "Check for performance issues"
Copilot: Reviews and suggests optimizations

Step 3 - TEST:
Comment:
// ACT:QA_Engineer OBJ:Test_JSON_Parser
// LIM:100%_Coverage
// OUT:Pytest_Suite

Step 4 - DOCUMENT:
Comment:
// ACT:Technical_Writer OBJ:API_Docs
// OUT:Markdown + Examples

Step 5 - OPTIMIZE:
You: "Reduce memory usage"
Copilot: Refactors for efficiency

Result: Production-ready JSON parser, all generated and tested!
Tokens saved: 60-70% vs natural language
"""


if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════╗
║   L-ZIP IN VS CODE - Developer Quick Reference                ║
║   By: ezixen                                                   ║
║   Usage: Efficient prompting with semantic compression         ║
╚════════════════════════════════════════════════════════════════╝

THREE WAYS TO USE L-ZIP:

1️⃣  CODE COMMENTS
// ACT:Dev OBJ:Function OUT:Code

2️⃣  COPILOT CHAT
Copy/paste L-ZIP prompt directly

3️⃣  INLINE SUGGESTIONS
Type L-ZIP comment and trigger Copilot

QUICK TEMPLATES:
◽ lzip-gen:  Generate code
◽ lzip-fix:  Debug and fix bugs
◽ lzip-test: Create test suite
◽ lzip-docs: Write documentation
◽ lzip-review: Code review

Start using L-ZIP now in VS Code!
See examples.py for 18 ready-to-use prompts.
    """)
