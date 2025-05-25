# Contributing to Modal Deployments

Thank you for your interest in contributing to Modal Deployments! This document provides guidelines and information for contributors.

## 🤝 Ways to Contribute

### 1. Reporting Issues

- Use the GitHub issue tracker
- Provide detailed descriptions and reproduction steps
- Include system information and error logs

### 2. Feature Requests

- Describe the feature and its use case
- Explain how it fits with the project goals
- Consider implementation complexity

### 3. Code Contributions

- Bug fixes
- New features
- Documentation improvements
- Test coverage improvements

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- Git
- Poetry (recommended) or pip

### Setup Steps

1. **Fork the repository**

   ```bash
   git clone https://github.com/yourusername/modal-deployments.git
   cd modal-deployments
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   # Using poetry (recommended)
   poetry install --with dev

   # Using pip
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**

   ```bash
   pre-commit install
   ```

5. **Run tests to verify setup**
   ```bash
   python -m pytest
   ```

## 📝 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes

- Follow the coding standards (see below)
- Write tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run all tests
python -m pytest

# Run specific test categories
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest tests/e2e/

# Check code coverage
python -m pytest --cov=src --cov-report=html
```

### 4. Code Quality Checks

```bash
# Format code
black .
isort .

# Lint code
flake8 src/ tests/

# Type checking
mypy src/

# Security check
bandit -r src/

# Run all pre-commit hooks
pre-commit run --all-files
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: resolve issue description"
```

Use conventional commit messages:

- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `test:` test additions/modifications
- `refactor:` code refactoring
- `style:` formatting changes
- `chore:` maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin your-branch-name
```

Then create a pull request on GitHub with:

- Clear description of changes
- Reference to related issues
- Test results and coverage information

## 🎯 Coding Standards

### Python Style

- Follow PEP 8
- Use Black for formatting (line length: 88)
- Use type hints for function signatures
- Write docstrings for all public functions/classes

### Code Organization

- Keep functions focused and small
- Use meaningful variable and function names
- Add comments for complex logic
- Organize imports: standard library, third-party, local

### Testing

- Write unit tests for all new functions
- Include integration tests for workflows
- Aim for high test coverage (>80%)
- Use descriptive test names

### Documentation

- Update README.md for new features
- Add docstrings to all public APIs
- Include usage examples
- Update configuration documentation

## 🔍 Code Review Process

1. **Automated Checks**

   - All tests must pass
   - Code coverage must not decrease
   - Pre-commit hooks must pass
   - No security vulnerabilities

2. **Manual Review**

   - Code quality and maintainability
   - Test adequacy
   - Documentation completeness
   - Architectural consistency

3. **Approval and Merge**
   - At least one approved review required
   - Squash and merge preferred for features
   - Merge commit for releases

## 📚 Project Structure Guidelines

### Directory Organization

```text
src/
├── core/           # Core business logic
├── deployment/     # Deployment scripts and configs
├── models/         # Model definitions and utilities
└── utils/          # Helper functions and utilities

tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
└── e2e/            # End-to-end tests

config/             # Configuration files
docs/               # Documentation
examples/           # Usage examples
```

### File Naming

- Use snake_case for Python files
- Use descriptive names
- Group related functionality

### Import Guidelines

- Use absolute imports
- Group imports by category
- Sort imports alphabetically

## 🐛 Debugging Guidelines

### Common Issues

1. **Modal Authentication**

   - Ensure `modal token new` was run
   - Check token expiration

2. **Python Environment**

   - Verify Python version compatibility
   - Check virtual environment activation

3. **Dependency Conflicts**
   - Use `poetry show --tree` to check dependencies
   - Consider using `poetry update`

### Debug Tools

- Use `loguru` for logging
- Set log level to DEBUG for detailed output
- Use pytest fixtures for test data
- Use `pdb` or `ipdb` for interactive debugging

## 📖 Documentation Guidelines

### README Updates

- Keep the main README concise
- Link to detailed documentation
- Update feature lists

### Code Documentation

- Use Google-style docstrings
- Include parameter types and return values
- Add usage examples for complex functions

### API Documentation

- Document all public APIs
- Include request/response examples
- Explain error conditions

## 🚀 Release Process

### Version Numbering

- Follow Semantic Versioning (SemVer)
- Format: MAJOR.MINOR.PATCH
- Pre-release: MAJOR.MINOR.PATCH-alpha/beta.N

### Release Steps

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create release tag
4. Update documentation
5. Deploy to production

## 📞 Getting Help

### Community

- GitHub Discussions for questions
- GitHub Issues for bugs
- Email maintainers for private concerns

### Resources

- [Modal Labs Documentation](https://modal.com/docs)
- [Ollama Documentation](https://ollama.ai/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 🙏 Recognition

Contributors will be recognized in:

- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to Modal Deployments! 🎉
