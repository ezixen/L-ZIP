# L-ZIP Specification

## Purpose
L-ZIP is a compact symbolic prompt protocol for reducing prompt verbosity while preserving intent.

## Core Syntax
- Operator form: KEY:Value
- Grouping: [Key:Value, Key:Value]
- Combine: A + B
- Sequence: A | B
- Mapping: A => B
- Scope/time/audience: @Value
- Length constraint: LEN:<Nw

## Operator Set
- ACT: Role/persona
- OBJ: Objective
- CTX: Context
- LIM: Constraints
- OUT: Output format
- THINK: Reasoning mode
- GEN: Generation type
- EVAL: Evaluation criteria
- SUM: Summary target
- VIS: Visualization request

## Recommended Prompt Order
1. ACT
2. CTX
3. OBJ
4. LIM
5. THINK (optional)
6. OUT

## Translation Behavior
- English input is translated into compact symbolic form.
- Hidden/control characters are sanitized while preserving visible content and line structure.
- Output formatting hints may be included in translation and cleaned for clipboard export where configured.

## Compatibility
- Works with modern LLM families (GPT, Claude, Gemini, Grok, Copilot-integrated workflows).
- Protocol is model-agnostic and transport-agnostic.

## Example
English:
"Act as a senior Python developer. Analyze this code for security issues and output a markdown report."

L-ZIP:
ACT:Senior_Dev [Lang:Python] CTX:[Code_Block] OBJ:Security_Analysis EVAL:Vulnerabilities OUT:Markdown_Report

## Related Documents
- ../BEST_PRACTICES.md
- ../MCP_INTEGRATION.md
- ../COMMAND_LINE_PARAMETERS.md
