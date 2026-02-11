# Security Policy

## Reporting Security Issues

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please email: **security@github.com** and mention this is for **ezixen/l-zip**

Include:
- Description of vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Security Disclaimer

### What L-ZIP Does NOT Do

- ❌ Does NOT encrypt data
- ❌ Does NOT hide data from the LLM service
- ❌ Does NOT provide cryptographic security
- ❌ Does NOT guarantee privacy

### What L-ZIP DOES Do

- ✓ Compresses prompts semantically
- ✓ Reduces token usage
- ✓ Maintains prompt meaning
- ✓ Works with any LLM API

## Data Security

**Your data security depends on:**

1. **LLM Service Provider** (OpenAI, Anthropic, etc.)
   - Follow their security policies
   - Review their privacy terms
   - Use official APIs only

2. **Your System**
   - Keep Python updated
   - Use secure network (HTTPS)
   - Protect API keys

3. **Network Security**
   - Don't send prompts over insecure networks
   - Use VPN if needed
   - Encrypt sensitive data before prompting

## What You Should Know

- L-ZIP is a **prompting technique**, not a security tool
- The compressed format still contains all original information
- An LLM with access to your L-ZIP prompt can decompress it
- **Do NOT use L-ZIP to hide sensitive information from LLMs**

## Best Practices

✅ **DO:**
- Review what you send to LLMs
- Use API keys securely (environment variables)
- Keep dependencies updated
- Follow LLM provider security guidelines

❌ **DON'T:**
- Send PII (personal info) unless necessary
- Hardcode API keys in code
- Use L-ZIP to "hide" data
- Trust compression for security

## Responsible Disclosure

If you discover a vulnerability:

1. **Do NOT** publish it publicly
2. **DO** report it to security channels
3. **DO** give maintainers time to respond (30 days)
4. **DO** work with maintainers on fixes

## Dependencies Security

L-ZIP has **zero external dependencies** for core functionality.

All included packages are:
- Minimal
- Well-maintained
- From official sources

Check [requirements.txt](requirements.txt) for the full list.

## Regular Updates

- Subscribe to GitHub Security Advisories
- Check [CHANGELOG.md](CHANGELOG.md) for updates
- Use `git pull` to get latest version

## License

This security policy is part of the MIT License.
See [LICENSE](LICENSE) for full details.

---

**Remember: The MIT License includes a clause absolving the author of liability.**

Review your own security practices and consult professionals for sensitive applications.

- ezixen, 2026
