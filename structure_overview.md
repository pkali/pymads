# MADS Codebase Structure Analysis

This document provides an analysis of the Mad-Assembler (MADS) Pascal codebase structure, focusing on key components, functions, and data flows to guide the Python translation process.

## Overview

The MADS assembler is primarily contained in a single large Pascal file (`mads.pas`, ~16,300 lines) with the following key components:

- Type definitions
- Global variables
- Utility functions
- Parsing and processing functions
- Assembly code generation
- Main program logic

## Key Data Structures

Based on initial analysis of the code, the following data structures appear to be central to MADS:

```pascal
type
    t_Dirop  = (_unknown, _r=1, _or, _lo, _hi, _get, _wget, _lget, _dget, _and, _xor, _not,
		_len, _adr, _def, _filesize, _sizeof, _zpvar, _rnd, _asize, _isize,
		_fileexists, _array);
    t_Mads   = (__STACK_POINTER, __STACK_ADDRESS, __PROC_VARS_ADR);
    t_MXinst =  (REP = $c2, SEP = $e2);
    t_Attrib = (__U, __R, __W, __RW);
    _typStrREG = string [4];
    _typStrSMB = string [8];
    _typStrINT = string [32];
    _strArray  = array of string;
    _intArray  = array of integer;
    _bolArray  = array of Boolean;
    _bckAdr    = array [0..1] of integer;
```

These types suggest the assembler handles various operations, register types, and memory attributes, with specialized string and array types for different purposes.

## Core Functions

The following functions appear to be central to the assembler's operation:

```pascal
function oblicz_wartosc(var a:string; var old:string): Int64; forward;
function oblicz_wartosc_noSPC(var zm,old:string; var i:integer; const sep,typ:Char): Int64; forward;
function oblicz_mnemonik(var i:integer; var a,old:string): int5; forward;

procedure search_comment_block(var i:integer; var zm,txt:string); forward;
procedure analizuj_mem(const start,koniec:integer; var old,a,old_str:string; licz:integer; const p_max:integer; const rp:Boolean); forward;
procedure analizuj_plik(var a:string; var old_str: string); forward;
procedure oblicz_dane(var i:integer; var a,old:string; const typ: byte); forward;
```

These function declarations suggest a structure where:
- `oblicz_*` functions handle value calculations and mnemonics
- `analizuj_*` procedures analyze memory and files
- `search_*` procedures handle parsing and text processing

## Main Program Flow

The main program flow appears to involve:

1. Initialization and command-line parsing
2. File loading and preprocessing
3. Multi-pass assembly process
4. Symbol resolution and address calculation
5. Code generation and output

A more detailed analysis of the control flow will be developed as we examine the code more thoroughly.

## Polish Language Elements

The codebase contains Polish language comments and some variable/function names. Examples include:

```pascal
// czy etykieta jest używana
// czy symbol jest słaby (Weak Symbol)
// wstrzymaj się z alokacją zmiennych .VAR
// globalna tablica dla parametrów przekazywanych do .REPT
// 256 znaczników dla zmiennych odkladanych na stronie zerowej
```

These will need careful translation or documentation during the Python conversion process.

## Next Steps

1. Perform a more detailed analysis of each core function
2. Map data dependencies between functions
3. Identify the assembly process flow in detail
4. Document the binary output generation process
5. Create a translation priority list based on dependencies
