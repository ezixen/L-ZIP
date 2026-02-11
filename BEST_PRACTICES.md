# Best Practices for L-ZIP

## Prompt Compression Best Practices

### 1. Structure Your Prompts Consistently

**Good:**
```
ACT:Senior_Dev CTX:[Codebase] OBJ:Debug_Issue THINK:StepByStep OUT:Solution+Prevention
```

**Avoid:**
```
ACT:Senior_Dev debug this thing with step by step output
```

### 2. Use Clear Operator Order

Standard order for maximum readability:
1. `ACT:` (Set persona first)
2. `CTX:` (Provide context)
3. `OBJ:` (State objective)
4. `LIM:` (Add constraints)
5. `THINK:` (Reasoning mode if needed)
6. `OUT:` (Output format)

### 3. Parameter Grouping with Brackets

Use `[]` to group related parameters:

```
ACT:Developer [Lang:Python, Framework:Django] OBJ:Build_API LIM:RESTful+Async OUT:Code+Tests
```

### 4. Pipe vs Plus

- Use `|` for sequential steps: `Step1 | Step2 | Step3`
- Use `+` for combined aspects: `Code + Tests + Docs`

### 5. When to Add Plain English

For complex or creative tasks, add a brief clarification:

```
ACT:Writer OBJ:Blog_Post [Topic:AI] LEN:1500w OUT:Markdown
// "Make it engaging for business professionals, include 3 statistics"
```

### 6. Batching Requests

For multiple similar prompts, create a template:

```
Template: ACT:Analyst [Dataset:$DATASET] OBJ:Find_Insights => Recommendations

Instance 1: ACT:Analyst [Dataset:Q4_Sales] OBJ:Find_Insights => Recommendations
Instance 2: ACT:Analyst [Dataset:Q4_Traffic] OBJ:Find_Insights => Recommendations
```

## Domain-Specific Tips

### Code Development
- Always specify language: `[Lang:Python]`
- Include framework if applicable: `[Framework:FastAPI]`
- Use THINK:StepByStep for complex logic
- Save output as Code/Script

### Content Creation
- Specify audience: `@Beginner` or `@Expert`
- Include style/tone in LIM
- Set LEN for length constraints
- Request Markdown for formatting

### Data Analysis
- Reference data source in CTX
- Use EVAL for statistical validation
- Request visualizations with VIS
- Combine with SUM for key findings

### Debugging
- Put error logs in CTX
- Use THINK:StepByStep
- Request both immediate fix and prevention
- Output as solution documentation

## Common Mistakes to Avoid

### ❌ Over-abbreviation
```
ACT:Dev OBJ:Cod OUT:Py
// Too vague - what kind of code?
```

### ✅ Clear abbreviation
```
ACT:Senior_Dev OBJ:Python_REST_API OUT:Production_Code
// Clear purpose
```

---

### ❌ Missing context
```
ACT:Debugger OBJ:Fix_Error
// What error? What system?
```

### ✅ Provide context
```
ACT:Debugger CTX:[Error_Log] [Service:Payment_API] OBJ:Fix_Error
// Full context provided
```

---

### ❌ Ambiguous objectives
```
OBJ:Improve_Code
// How should it be improved?
```

### ✅ Specific objectives
```
OBJ:Improve_Code [Performance, Readability, Security]
// Clear improvement areas
```

## Testing Your L-ZIP

Before sending to production:

1. **Expansion Test**: Expand it back to English - does it make sense?
2. **Compression Test**: Did you save > 30% tokens?
3. **Clarity Test**: Would someone understand your intent?
4. **Domain Test**: Is it appropriate for your specific use case?

Use the CLI:
```bash
python cli.py
lzip> compress
[Your English prompt]
# Check the compression report

lzip> expand
# Paste your L-ZIP
# Verify it expands correctly
```

## Iteration Strategy

1. Start with basic operators (ACT + OBJ + OUT)
2. Test with your model
3. Add LIM and CTX only if needed
4. Use THINK for complex reasoning
5. Refine based on model feedback

## Token Counting

Estimate compression before and after:
- English prompts: ~4 chars per token
- L-ZIP prompts: ~1.5-3 chars per token

Use an API tokenizer or IDE extension for accurate counts.

## Integration with Version Control

```bash
# Version your L-ZIP templates
git add l-zip-templates/
git commit -m "Add L-ZIP templates for code review: 55% compression achieved"
```

## Troubleshooting

### Model returns format errors
- **Solution**: Add a clarifying comment in English after the L-ZIP
- Example: `ACT:Dev OBJ:Code // "Write production Python code"`

### Low compression on short prompts
- **Expected**: Very short prompts don't compress much
- Try batching multiple related prompts

### Ambiguous interpretation
- **Solution**: Use more specific operator values
- Instead of `OBJ:Improve`, use `OBJ:Improve_Performance | Readability | Security`

---

**Remember:** L-ZIP is a tool for precision and efficiency. Start simple, test often, iterate based on results.
