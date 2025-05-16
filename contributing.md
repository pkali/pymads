# Contributing to PyMADS

Thank you for your interest in contributing to PyMADS! This document provides guidelines and information for contributors.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:

- A clear title and description
- Steps to reproduce the issue
- Expected and actual behavior
- Any relevant logs or screenshots

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:

- A clear title and description
- Detailed explanation of the proposed functionality
- Any relevant examples or references

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass
6. Update documentation if necessary
7. Submit a pull request

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use Google-style docstrings
- Run Black formatter before committing

### Testing

- Write tests for all new functionality
- Ensure binary compatibility with the original MADS
- Run the full test suite before submitting a PR

### Documentation

- Update documentation for any changed functionality
- Add docstrings to all public functions, classes, and methods
- Follow Google-style docstring format

## Translation Guidelines

When translating Pascal code to Python:

1. **Understand Before Translating**: Make sure you understand what the Pascal code does before attempting to translate it.

2. **Function by Function**: Translate one function at a time, ensuring each works correctly before moving on.

3. **Test Thoroughly**: Write tests for each translated function to verify it behaves the same as the original.

4. **Maintain Compatibility**: The primary goal is binary compatibility with the original MADS.

5. **Improve Readability**: Use Python's features to make the code more readable and maintainable.

6. **Document Everything**: Add clear documentation, especially for complex algorithms or non-obvious behavior.

7. **Handle Polish Comments**: Translate Polish comments to English or document their meaning.

## Project Structure

When adding new files, follow the existing project structure:

- `src/pymads/`: Main package source code
  - `core/`: Core functionality
  - `parser/`: Parsing and tokenization
  - `assembler/`: Assembly code generation
  - `utils/`: Utility functions
- `tests/`: Test suite
- `docs/`: Documentation
- `examples/`: Example code and test cases

## Release Process

1. Update version number in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a new GitHub release with release notes
4. Publish to PyPI (if applicable)

## Questions?

If you have any questions or need help, please create an issue on GitHub or reach out to the project maintainers.
