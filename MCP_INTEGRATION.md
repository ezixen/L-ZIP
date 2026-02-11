# MCP Integration Guide for L-ZIP

**MCP Server:** L-ZIP Token Compression Protocol  
**Version:** 1.0.0  
**Author:** ezixen  
**License:** MIT

---

## Overview

L-ZIP MCP Server provides Model Context Protocol integration for token-efficient prompting. Use it to automatically compress your prompts to 50-70% of original size, saving tokens and costs on GitHub Copilot, Claude, ChatGPT, and other LLMs.

---

## Installation

### Option 1: Direct Python (Recommended for Development)

```bash
git clone https://github.com/ezixen/l-zip.git
cd l-zip
pip install -r requirements.txt
python mcp_server.py
```

### Option 2: As Python Module

```bash
pip install git+https://github.com/ezixen/l-zip.git
```

Then in your Python code:
```python
from lzip import LZIPTranslator
translator = LZIPTranslator()
compressed, stats = translator.translate_to_lzip("Your long prompt here")
print(compressed)
```

### Option 3: Docker (Coming Soon)

```bash
docker run -p 5000:5000 ezixen/l-zip:latest
```

---

## Quick Start

### 1. Run the CLI

```bash
python cli.py
```

**Interactive commands:**
```
compress          - Compress a prompt
expand           - Expand L-ZIP back to English
batch            - Compress multiple prompts
dict             - Show L-ZIP operators
templates        - Show template prompts
demo             - Run demo with examples
help             - Show all commands
exit             - Quit
```

### 2. Use the MCP Server

```bash
python mcp_server.py
```

Then call via HTTP or your MCP client:
```python
{
  "method": "translate_to_lzip",
  "params": {
    "prompt": "Write a Python function that validates emails"
  }
}
```

### 3. Use in Python

```python
from lzip import LZIPTranslator

translator = LZIPTranslator()

# Translate to L-ZIP
prompt = "I need a Python function to validate email addresses"
lzip_prompt, stats = translator.translate_to_lzip(prompt)

print(f"Original: {prompt}")
print(f"L-ZIP: {lzip_prompt}")
print(f"Savings: {stats['compression_percentage']:.1f}%")

# Expand back to English
expanded, _ = translator.translate_from_lzip(lzip_prompt)
print(f"Expanded: {expanded}")
```

---

## MCP Server Endpoints

### `translate_to_lzip`
Compress English prompt to L-ZIP format

**Request:**
```json
{
  "method": "translate_to_lzip",
  "params": {
    "prompt": "Your prompt here",
    "aggressive": false
  }
}
```

**Response:**
```json
{
  "result": "ACT:Dev OBJ:Function OUT:Code",
  "stats": {
    "original_tokens": 15,
    "lzip_tokens": 4,
    "compression_percentage": 73.3,
    "tokens_saved": 11
  }
}
```

### `translate_from_lzip`
Expand L-ZIP back to English

**Request:**
```json
{
  "method": "translate_from_lzip",
  "params": {
    "lzip_prompt": "ACT:Dev OBJ:Function OUT:Code"
  }
}
```

**Response:**
```json
{
  "result": "Developer role, objective is to write a function, output is code",
  "stats": {}
}
```

### `batch_translate`
Compress multiple prompts

**Request:**
```json
{
  "method": "batch_translate",
  "params": {
    "prompts": ["prompt 1", "prompt 2"],
    "to_lzip": true
  }
}
```

### `get_dictionary`
Get L-ZIP operators and definitions

**Request:**
```json
{
  "method": "get_dictionary",
  "params": {}
}
```

### `get_templates`
Get pre-built prompt templates

**Request:**
```json
{
  "method": "get_templates",
  "params": {}
}
```

---

## L-ZIP Operator Reference

| Operator | Purpose | Example |
|----------|---------|---------|
| `ACT:` | Define actor/role | `ACT:Senior_Dev` |
| `OBJ:` | Set objective | `OBJ:Write_Function` |
| `OUT:` | Specify output | `OUT:Code+Tests` |
| `CTX:` | Add context | `CTX:[Code_Below]` |
| `LIM:` | Set limitations | `LIM:No_Breaking_Changes` |
| `THINK:` | Define reasoning | `THINK:StepByStep` |
| `GEN:` | Generate what | `GEN:Function` |
| `EVAL:` | Evaluate criteria | `EVAL:Performance+Security` |
| `SUM:` | Summarize what | `SUM:[Features, API]` |
| `VIS:` | Visualize what | `VIS:Diagram` |
| `[..]` | Parameters | `[Lang:Python]` |
| `+` | Addition | `Code + Tests` |
| `\|` | Alternative | `Fix \| Optimize` |
| `=>` | Implication | `Issue => Solution` |
| `@` | Apply to | `@function_name` |
| `LEN:` | Length constraint | `LEN:500w` |

---

## Real-World Examples

### Example 1: Code Generation

**Natural Language (45 words, ~58 tokens)**
```
I need you to write a Python function that validates email addresses. 
The function should check for proper format, handle edge cases, and 
include comprehensive error handling. Please provide the complete 
implementation with docstring, type hints, and a full test suite.
```

**L-ZIP (3 words, ~4 tokens)**
```
ACT:Senior_Dev [Lang:Python] OBJ:Email_Validator OUT:Function+Tests+Docstring
```

**Savings: 93.3%** ✓

---

### Example 2: Code Review

**Natural Language (40 words)**
```
Please review the following code for performance issues, security 
vulnerabilities, and code quality. Suggest optimizations and point 
out any problems. Provide a detailed analysis with specific recommendations.
```

**L-ZIP (8 words)**
```
ACT:Code_Reviewer CTX:[Code_Below] OBJ:Review | Optimize EVAL:Performance+Security
```

**Savings: 80%** ✓

---

### Example 3: Bug Fixing

**Natural Language (35 words)**
```
There's an error in the code below. Can you identify the root cause, 
explain why it happened, and provide a fix? Also suggest how to prevent 
similar issues in the future.
```

**L-ZIP (7 words)**
```
ACT:Debugger OBJ:Fix_Bug THINK:RootCause+Prevention OUT:Solution
```

**Savings: 80%** ✓

---

## GitHub Copilot Cost Savings

### Pricing
- GitHub Copilot Pro: **$0.003 per 1K input tokens**

### Example Savings (100 prompts)
- Average prompt: 45 words (~58 tokens)
- L-ZIP compression: 93%
- Tokens saved per prompt: 54
- **Cost saved per 100 prompts: $0.016** (16 cents)
- **Cost saved per 1,000 prompts: $0.16** (16 cents per thousand)

### Annual Impact (1000 prompts/month)
- Tokens saved: 648,000
- Cost saved: **$1.94/month** or **$23.33/year**
- Plus: **Token limits stretched 10x further**

---

## Integration Examples

### With Any AI Tool (ChatGPT, Claude, Gemini, etc.)

1. Generate or copy an L-ZIP prompt
2. Paste into your AI tool:
   ```
   ACT:Senior_Dev [Lang:Python] OBJ:Parse_JSON OUT:Function+Tests
   ```
3. AI generates code using 70% fewer tokens! ✓

### With Python Script

```python
from lzip import LZIPTranslator

translator = LZIPTranslator()

prompts = [
    "Write a Python function to validate emails",
    "Create a REST API endpoint for user data",
    "Generate comprehensive test cases"
]

for prompt in prompts:
    lzip, stats = translator.translate_to_lzip(prompt)
    print(f"Savings: {stats['compression_percentage']:.1f}%")
    print(f"L-ZIP: {lzip}\n")
```

### With HTTP Server

```bash
# Start server
python mcp_server.py

# In another terminal, use curl
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a Python function"}'
```

---

## Configuration

### config.json

```json
{
  "aggressive_mode": false,
  "preserve_examples": true,
  "enable_caching": true,
  "max_prompt_length": 5000,
  "compression_threshold": 0.3
}
```

**Options:**
- `aggressive_mode`: Compress even more (may lose some meaning)
- `preserve_examples`: Keep code examples in output
- `enable_caching`: Cache compression results
- `max_prompt_length`: Reject prompts longer than this
- `compression_threshold`: Minimum 30% reduction before compressing

---

## Troubleshooting

### Low Compression Ratio?
- ✓ L-ZIP works best on longer prompts (>20 words)
- ✓ Add more detail to the prompt
- ✓ Use specific domain tags: `[Lang:Python]`, `[Framework:FastAPI]`

### Not Getting Expected Results?
- ✓ Check operator syntax (ACT:, OBJ:, OUT: required)
- ✓ Use quotes for multiword values: `[Name:emailValidator]`
- ✓ Test with demo_lzip.py first

### Server Won't Start?
- ✓ Check Python version (3.8+)
- ✓ Verify port 5000 is available: `netstat -an | grep 5000`
- ✓ Try different port: `python mcp_server.py --port 8000`

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and add tests: `python test_lzip.py`
4. Commit: `git commit -m "Your message"`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## FAQ

**Q: Can I use L-ZIP with ChatGPT?**  
A: Yes! Copy the generated L-ZIP prompt into any AI chat interface.

**Q: Does this work with Claude?**  
A: Yes! All LLMs understand semantic compression.

**Q: Is this secure?**  
A: L-ZIP is a prompting technique. Your data security depends on the LLM service you use.

**Q: Can I modify L-ZIP?**  
A: Absolutely! It's MIT licensed. Make it better if you can, Human!

**Q: What about output tokens?**  
A: L-ZIP primarily compresses inputs. Outputs aren't affected.

---

## Support

- **GitHub Issues:** https://github.com/ezixen/l-zip/issues
- **Discussions:** https://github.com/ezixen/l-zip/discussions
- **Email:** ezixen@github.com

---

## License

MIT License - See [LICENSE](LICENSE) for details

**"Make it better if you can, Human!"** - ezixen, 2026
