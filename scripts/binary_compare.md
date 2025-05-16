# Binary Comparison Tool for PyMADS

This module provides tools to compare binary outputs between the original MADS Pascal assembler and the Python port (PyMADS) to ensure compatibility.

```python
#!/usr/bin/env python3
"""
Binary Comparison Tool for PyMADS

This script compares binary outputs from the original MADS assembler and PyMADS
to verify compatibility and correctness of the Python implementation.

Usage:
    binary_compare.py compare <pascal_output> <python_output>
    binary_compare.py test <asm_file>
    binary_compare.py batch <test_dir>
    binary_compare.py (-h | --help)

Options:
    -h --help     Show this help message.
    
Commands:
    compare       Compare two binary files and report differences
    test          Assemble a file with both assemblers and compare results
    batch         Run tests on all .asm files in a directory
"""

import os
import sys
import subprocess
import difflib
import binascii
from docopt import docopt


def run_pascal_mads(asm_file, output_file=None):
    """
    Run the original Pascal MADS assembler on the given file.
    
    Args:
        asm_file (str): Path to the assembly file
        output_file (str, optional): Output binary file path
        
    Returns:
        str: Path to the generated binary file
    """
    if output_file is None:
        output_file = os.path.splitext(asm_file)[0] + '.bin'
    
    # Construct the command to run the Pascal MADS
    pascal_mads_path = os.path.join(os.path.dirname(__file__), 
                                   '../pascal_env/Mad-Assembler/mads')
    
    cmd = [pascal_mads_path, asm_file, '-o:' + output_file]
    
    # Run the command
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error running Pascal MADS: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        sys.exit(1)


def run_python_mads(asm_file, output_file=None):
    """
    Run the Python MADS (PyMADS) on the given file.
    
    Args:
        asm_file (str): Path to the assembly file
        output_file (str, optional): Output binary file path
        
    Returns:
        str: Path to the generated binary file
    """
    if output_file is None:
        output_file = os.path.splitext(asm_file)[0] + '_py.bin'
    
    # Construct the command to run PyMADS
    # This will need to be updated as PyMADS development progresses
    pymads_path = os.path.join(os.path.dirname(__file__), '../src/pymads/cli.py')
    
    cmd = [sys.executable, pymads_path, asm_file, '-o', output_file]
    
    # Run the command
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error running PyMADS: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        sys.exit(1)


def compare_binary_files(file1, file2, verbose=True):
    """
    Compare two binary files and report differences.
    
    Args:
        file1 (str): Path to first binary file
        file2 (str): Path to second binary file
        verbose (bool): Whether to print detailed differences
        
    Returns:
        bool: True if files are identical, False otherwise
    """
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
    
    if content1 == content2:
        if verbose:
            print(f"Files are identical: {file1} and {file2}")
            print(f"Size: {len(content1)} bytes")
        return True
    
    # Files differ
    if verbose:
        print(f"Files differ: {file1} and {file2}")
        print(f"Size of {file1}: {len(content1)} bytes")
        print(f"Size of {file2}: {len(content2)} bytes")
        
        # Find and display differences
        if len(content1) != len(content2):
            print(f"File sizes differ by {abs(len(content1) - len(content2))} bytes")
        
        # Compare byte by byte and report first differences
        min_len = min(len(content1), len(content2))
        diff_count = 0
        max_diffs = 10  # Maximum number of differences to show
        
        for i in range(min_len):
            if content1[i] != content2[i]:
                diff_count += 1
                if diff_count <= max_diffs:
                    print(f"Difference at byte {i}: "
                          f"{hex(content1[i])} vs {hex(content2[i])}")
        
        if diff_count > max_diffs:
            print(f"... and {diff_count - max_diffs} more differences")
    
    return False


def test_assembly_file(asm_file):
    """
    Test a single assembly file by assembling with both assemblers and comparing results.
    
    Args:
        asm_file (str): Path to the assembly file
        
    Returns:
        bool: True if outputs match, False otherwise
    """
    print(f"\nTesting file: {asm_file}")
    
    # Generate output filenames
    pascal_output = os.path.splitext(asm_file)[0] + '_pascal.bin'
    python_output = os.path.splitext(asm_file)[0] + '_python.bin'
    
    # Run both assemblers
    run_pascal_mads(asm_file, pascal_output)
    run_python_mads(asm_file, python_output)
    
    # Compare results
    return compare_binary_files(pascal_output, python_output)


def batch_test_directory(test_dir):
    """
    Test all .asm files in a directory.
    
    Args:
        test_dir (str): Directory containing assembly files
        
    Returns:
        tuple: (passed_count, total_count)
    """
    print(f"Batch testing files in: {test_dir}")
    
    passed = 0
    total = 0
    
    for filename in os.listdir(test_dir):
        if filename.endswith('.asm'):
            file_path = os.path.join(test_dir, filename)
            total += 1
            if test_assembly_file(file_path):
                passed += 1
    
    print(f"\nTest results: {passed}/{total} passed")
    return passed, total


def main():
    """Main entry point for the script."""
    args = docopt(__doc__)
    
    if args['compare']:
        pascal_output = args['<pascal_output>']
        python_output = args['<python_output>']
        result = compare_binary_files(pascal_output, python_output)
        sys.exit(0 if result else 1)
    
    elif args['test']:
        asm_file = args['<asm_file>']
        result = test_assembly_file(asm_file)
        sys.exit(0 if result else 1)
    
    elif args['batch']:
        test_dir = args['<test_dir>']
        passed, total = batch_test_directory(test_dir)
        sys.exit(0 if passed == total else 1)


if __name__ == '__main__':
    main()
```

## Usage Examples

### Compare Two Binary Files

```bash
python scripts/binary_compare.py compare output_pascal.bin output_python.bin
```

### Test a Single Assembly File

```bash
python scripts/binary_compare.py test examples/hello_world.asm
```

### Batch Test a Directory

```bash
python scripts/binary_compare.py batch examples/
```

## Integration with CI/CD

This tool can be integrated into CI/CD pipelines to automatically verify binary compatibility between the original MADS and PyMADS implementations. Example GitHub Actions workflow:

```yaml
name: Binary Compatibility Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    
    - name: Install Free Pascal Compiler
      run: |
        sudo apt-get update
        sudo apt-get install -y fp-compiler
    
    - name: Build original MADS
      run: |
        cd pascal_env/Mad-Assembler
        fpc -Mdelphi -vh -O3 mads.pas
    
    - name: Run binary compatibility tests
      run: |
        python scripts/binary_compare.py batch examples/
```

## Future Enhancements

1. Add detailed reporting of differences (e.g., HTML report with highlighted differences)
2. Add support for comparing assembly listings in addition to binary output
3. Implement performance benchmarking between the two implementations
4. Add support for testing specific assembler features or directives
