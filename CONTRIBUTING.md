# CONTRIBUTING TO L-ZIP

**Project Created By:** [ezixen](https://github.com/ezixen)

Thank you for your interest in contributing to L-ZIP! 

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- A GitHub account

### Setup Development Environment

```bash
git clone https://github.com/yourusername/l-zip.git
cd l-zip

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt
```

## Development Workflow

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes** and test thoroughly
5. **Commit with clear messages**: `git commit -m "Add feature X with Y benefit"`
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Create a Pull Request** with detailed description

## Code Style

- Follow PEP 8 conventions
- Use type hints where possible
- Add docstrings to all functions
- Keep functions focused and modular
- Maximum line length: 100 characters

Example:
```python
def translate_to_lzip(self, prompt: str) -> Tuple[str, Dict[str, Any]]:
    """
    Translate English prompt to L-ZIP format.
    
    Args:
        prompt: English language prompt
        
    Returns:
        Tuple of (lzip_prompt, metadata with compression ratios)
    """
```

## Testing Requirements

All contributions must include tests:

```bash
# Run existing tests
python test_lzip.py

# Add tests for your feature in test_lzip.py
# Example:
def test_your_new_feature(self):
    """Test description"""
    result = your_function("input")
    self.assertEqual(result, expected_output)
```

### Test Coverage Areas
- **Unit tests**: Individual functions in isolation
- **Integration tests**: Multiple components together
- **Domain tests**: Different use cases (code, content, data)
- **Edge cases**: Empty inputs, very long inputs, special characters

## Documentation

Update relevant documentation for your changes:

1. **Code comments**: Explain the "why", not the "what"
2. **Docstrings**: Use Google style docstrings
3. **README.md**: Update if adding user-facing features
4. **BEST_PRACTICES.md**: Add new best practices
5. **CHANGELOG.md**: Note breaking changes

## Types of Contributions We Welcome

### New Features
- New operators or operator variants
- Better compression algorithms
- Domain-specific enhancements
- Integration with new LLM APIs

### Bug Fixes
- Incorrect translation results
- Crashes or hangs
- Unexpected behavior
- Documentation issues

### Improvements
- Performance optimizations
- Better error messages
- Code refactoring
- Test coverage

## Pull Request Process

1. **Title**: Clear, descriptive title
   - ✓ "Add support for domain-specific operators"
   - ✗ "Fix stuff"

2. **Description**: Include
   - What problem does this solve?
   - How does it work?
   - Any breaking changes?
   - Test results

3. **Tests**: All tests must pass
   ```bash
   python test_lzip.py
   ```
## Communication

- **Issues**: For bugs and features
- **Discussions**: For questions and ideas
- **Pull Requests**: For code changes
- **Slack**: (if available) For real-time discussion

## Becoming a Maintainer

Active contributors with quality PRs can be invited to become maintainers. This includes:
- Commit access to main repository
- Permission to review and merge PRs
- Responsibility for code quality
- Time commitment (typically 5-10 hours/week)

## Code of Conduct

Please be respectful and professional:
- No harassment or discrimination
- Constructive criticism only
- Assume good intent
- Help others learn

## Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- GitHub contributor list
- Release notes for significant contributions

## Questions?

- Check existing issues and discussions
- Read the documentation thoroughly
- Ask in a new discussion
- Join our community channels
- DM ezixen somewhere :)
---

Thank you for contributing to making L-ZIP better! 🚀
