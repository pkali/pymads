# MADS Core Functions Analysis

This document analyzes the core functions and procedures in the MADS assembler, focusing on their purpose, inputs, outputs, and relationships to guide the Python translation process.

## Function Categories

Based on the function and procedure signatures, we can categorize the MADS codebase into several functional groups:

### Text Processing and Parsing
- `omin_spacje` - Skip spaces in input
- `Tab2Space` - Convert tabs to spaces
- `__inc` - Increment position in string
- `AnsiUpperCase` - Convert string to uppercase
- `UpCas_` - Convert character to uppercase
- `search_comment_block` - Process comment blocks

### Value Calculation and Conversion
- `oblicz_wartosc` - Calculate value (likely expression evaluation)
- `oblicz_wartosc_noSPC` - Calculate value without spaces
- `ata2int` - Convert (likely ASCII to integer)
- `IntToStr` - Convert integer to string
- `StrToInt` - Convert string to integer
- `Hex` - Convert to hexadecimal representation

### File and Path Handling
- `GetFilePath` - Extract path from filename
- `GetFileName` - Extract filename from path
- `NormalizePath` - Normalize file path
- `GetFile` - Get file content
- `TestFile` - Test if file exists/is valid
- `WriteAccessFile` - Write to file with access check

### Assembly Processing
- `oblicz_mnemonik` - Process mnemonics
- `analizuj_mem` - Analyze memory
- `analizuj_plik` - Analyze file
- `oblicz_dane` - Process data

### Output Generation
- `flush_dst` - Flush destination buffer
- `put_dst` - Put byte to destination
- `save_dst` - Save byte to destination
- `save_dstW` - Save word to destination
- `save_dstS` - Save string to destination
- `save_nul` - Save null bytes
- `justuj` - Justify/align output

### Symbol Table Management
- `l_lab` - Likely label length or lookup
- `load_lab` - Load label
- `zapisz_etykiete` - Save label/symbol
- `obetnij_kropke` - Remove dot from label

### Error Handling and Messaging
- `warning` - Generate warning
- `new_message` - Create new message
- `blad` - Generate error
- `blad_und` - Generate undefined error
- `koniec` - End processing (likely with error)
- `load_mes` - Load message

## Key Data Flows

The main data flows appear to be:

1. **Input Processing**:
   - File loading → Text normalization → Tokenization → Parsing

2. **Symbol Resolution**:
   - Symbol table management → Value calculation → Address resolution

3. **Code Generation**:
   - Mnemonic processing → Operand evaluation → Binary output generation

4. **Error Handling**:
   - Error detection → Message generation → Output formatting

## Function Dependencies

Based on the forward declarations and function signatures, we can identify these key dependencies:

- `oblicz_wartosc` likely depends on `omin_spacje`, `__inc`, and other text processing functions
- `analizuj_plik` likely depends on `analizuj_mem` and `search_comment_block`
- `oblicz_mnemonik` likely depends on value calculation functions

## Translation Priority

For the Python translation, we should prioritize functions in this order:

1. Utility functions (text processing, file handling)
2. Value calculation and conversion
3. Symbol table management
4. Assembly processing
5. Output generation
6. Error handling and messaging

This approach will allow us to build a foundation of well-tested utility functions before tackling the more complex assembly logic.

## Next Steps

1. Analyze the implementation of each core function
2. Document the parameters and return values in detail
3. Create Python equivalents with comprehensive tests
4. Verify binary compatibility with test cases
