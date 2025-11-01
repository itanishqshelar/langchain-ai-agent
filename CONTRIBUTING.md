# Contributing to LangChain AI Agent

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository**

   - Click the "Fork" button on GitHub
   - Clone your fork locally

2. **Set up development environment**

   ```bash
   git clone https://github.com/YOUR_USERNAME/langchain-ai-agent.git
   cd langchain-ai-agent
   python -m venv venv
   source venv/bin/activate  # or `.\venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Example:

```python
def my_function(param: str) -> str:
    """
    Brief description of what the function does.

    Args:
        param: Description of the parameter

    Returns:
        Description of the return value
    """
    # Implementation
    return result
```

### Adding New Tools

To add a new tool:

1. **Create the tool function** in `tools.py`:

   ```python
   def my_tool_function(input: str) -> str:
       """
       Description of what the tool does.

       Args:
           input: Description of expected input

       Returns:
           Description of output
       """
       # Your implementation
       return result
   ```

2. **Wrap it as a LangChain Tool**:

   ```python
   my_tool = Tool(
       name="MyTool",
       func=my_tool_function,
       description="Clear description for the AI agent to understand when to use this tool"
   )
   ```

3. **Add to the tools list**:

   ```python
   all_tools = [...existing_tools..., my_tool]
   ```

4. **Document it** in README.md

### Testing

- Write tests for new features in `test_chatbot.py`
- Run tests before submitting:
  ```bash
  pytest test_chatbot.py -v
  ```

### Commit Messages

Use clear, descriptive commit messages:

- `feat: Add new calculator tool`
- `fix: Resolve chat history overflow issue`
- `docs: Update installation instructions`
- `refactor: Improve error handling in main.py`
- `test: Add tests for new tools`

## 🔧 Areas for Contribution

### High Priority

- [ ] Additional tool integrations (weather, calculator, etc.)
- [ ] Streaming responses support
- [ ] Memory persistence (save/load conversations)
- [ ] Multi-language support
- [ ] Web UI frontend

### Medium Priority

- [ ] Additional LLM provider support
- [ ] Custom prompt templates
- [ ] Rate limiting for API
- [ ] Docker support
- [ ] Advanced error recovery

### Documentation

- [ ] Video tutorials
- [ ] More usage examples
- [ ] API documentation
- [ ] Architecture diagrams

## 📤 Submitting Changes

1. **Ensure code quality**

   - Run tests: `pytest test_chatbot.py -v`
   - Check for errors in your code
   - Update documentation if needed

2. **Commit your changes**

   ```bash
   git add .
   git commit -m "feat: Brief description of changes"
   ```

3. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of changes
   - Reference any related issues

## 🐛 Reporting Bugs

When reporting bugs, include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: Exact steps to reproduce the behavior
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: OS, Python version, package versions
- **Error messages**: Full error traceback if applicable

## 💡 Feature Requests

For feature requests:

- Describe the feature clearly
- Explain the use case
- Provide examples if possible
- Discuss potential implementation approaches

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files are included
- [ ] `.env` files are not committed

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards others

## ❓ Questions?

If you have questions:

- Check existing issues and discussions
- Open a new issue with the "question" label
- Be specific and provide context

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
