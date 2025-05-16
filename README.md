# PyMADS Project

PyMADS is a Python port of the Mad-Assembler (MADS), a 6502/65816 cross-assembler originally written in Pascal.

## Project Overview

This project aims to convert the Mad-Assembler from Pascal to Python while:
- Maintaining compatibility with existing MADS projects
- Improving code readability and maintainability
- Enabling easier future feature additions

## Development Environment

### Python Environment
- Python 3.10+ (targeting 3.13 where available)
- VS Code as the primary IDE
- Google-style docstrings
- docopt for command-line arguments
- pytest for testing
- MkDocs for documentation

### Pascal Environment
- Free Pascal Compiler (FPC) 3.2.2
- Original MADS source code

## Project Structure

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

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/pkali/pymads.git
cd pymads

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,docs]"
```

### Building Documentation

```bash
mkdocs serve  # For local preview
mkdocs build  # To build static site
```

### Running Tests

```bash
pytest
pytest --cov=pymads  # With coverage
```

## Development Workflow

1. Analyze original Pascal code
2. Translate function by function
3. Write tests to verify binary compatibility
4. Document the translated code

## License

MIT License
