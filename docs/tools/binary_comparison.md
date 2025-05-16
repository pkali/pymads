# Binary Comparison Tool

This document describes the binary comparison tool for PyMADS, which is used to verify that the Python implementation produces identical binary output to the original Pascal MADS assembler.

## Overview

The binary comparison tool provides three main functions:

1. **Compare two binary files** - Directly compare binary outputs from both assemblers
2. **Test a single assembly file** - Assemble with both assemblers and compare results
3. **Batch test a directory** - Run tests on all assembly files in a directory

## Usage

### Compare Two Binary Files

```bash
python scripts/binary_compare.py compare output_pascal.bin output_python.bin
```

This command compares two binary files and reports any differences in detail.

### Test a Single Assembly File

```bash
python scripts/binary_compare.py test examples/hello_world.asm
```

This command:
1. Assembles the file with the original Pascal MADS
2. Assembles the file with PyMADS
3. Compares the resulting binary files
4. Reports whether they match

### Batch Test a Directory

```bash
python scripts/binary_compare.py batch examples/
```

This command runs the test on all `.asm` files in the specified directory and provides a summary of results.

## Integration with CI/CD

The binary comparison tool is designed to be integrated into CI/CD pipelines to automatically verify compatibility between implementations. See the GitHub Actions workflow example in the script documentation.

## Implementation Details

The tool is implemented in Python and uses the `subprocess` module to run both assemblers. It then performs a byte-by-byte comparison of the output files and reports any differences.

Key features:
- Detailed reporting of differences
- Support for batch testing
- Integration with CI/CD pipelines
- Exit codes for automated testing (0 for success, 1 for failure)

## Future Enhancements

Planned enhancements for the binary comparison tool include:

1. HTML reports with highlighted differences
2. Assembly listing comparison
3. Performance benchmarking
4. Feature-specific testing
