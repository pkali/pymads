#!/usr/bin/env python3
"""
PyMADS CLI - Command-line interface for the Python Mad-Assembler

Usage:
    pymads <source_file> [-o <output_file>] [options]
    pymads (-h | --help)
    pymads --version

Options:
    -h --help           Show this help message and exit
    --version           Show version and exit
    -o <output_file>    Output file [default: <source_file_base>.bin]
    -v --verbose        Enable verbose output
    --list              Generate listing file
    --symbols           Generate symbols file
"""

from docopt import docopt
import os
import sys

__version__ = '0.1.0'


def main():
    """Main entry point for the PyMADS CLI."""
    args = docopt(__doc__, version=f'PyMADS v{__version__}')
    
    # This is a placeholder implementation
    # In the future, this will call the actual assembler
    source_file = args['<source_file>']
    output_file = args['-o']
    
    if output_file is None:
        base_name = os.path.splitext(source_file)[0]
        output_file = f"{base_name}.bin"
    
    print(f"PyMADS v{__version__}")
    print(f"Source file: {source_file}")
    print(f"Output file: {output_file}")
    print("Note: This is a placeholder. The actual assembler is not yet implemented.")
    
    # Return with error code since we're not actually assembling anything yet
    return 1


if __name__ == '__main__':
    sys.exit(main())
