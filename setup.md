# Setup Guide

This guide will help you set up the PyMADS development environment.

## Prerequisites

- Python 3.10 or higher
- Free Pascal Compiler (FPC) 3.2.2 or higher (for original MADS compilation)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pkali/pymads.git
cd pymads
```

### 2. Set Up Python Environment

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,docs]"
```

### 3. Set Up Pascal Environment

The original MADS Pascal code is needed for comparison and testing:

```bash
# Install Free Pascal Compiler
# On Ubuntu/Debian:
sudo apt-get update
sudo apt-get install -y fp-compiler

# On macOS (using Homebrew):
brew install fpc

# On Windows:
# Download and install from https://www.freepascal.org/download.html

# Compile the original MADS
cd pascal_env/Mad-Assembler
fpc -Mdelphi -vh -O3 mads.pas
```

## Project Structure

The PyMADS project is organized as follows:

```
pymads/
├── src/
│   └── pymads/       # Main package source code
├── tests/            # Test suite
├── docs/             # Documentation
├── examples/         # Example code and test cases
├── scripts/          # Utility scripts
└── pascal_env/       # Original Pascal environment for comparison
    └── Mad-Assembler/  # Original MADS source
```

## Development Workflow

1. Make sure all tests pass with the current code
2. Implement new features or fix bugs
3. Add tests for your changes
4. Run the binary comparison tool to ensure compatibility
5. Update documentation as needed
6. Submit a pull request

## Running Tests

```bash
# Run the test suite
pytest

# Run with coverage report
pytest --cov=pymads

# Test binary compatibility
python scripts/binary_compare.py test examples/hello_world.asm
```

## Building Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build static documentation site
mkdocs build
```

## IDE Setup

### VS Code

For VS Code users, here are recommended extensions and settings:

1. Install the Python extension
2. Set up linting and formatting:
   - Install Black formatter
   - Install Flake8 linter
   - Configure settings.json:

```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true
}
```
