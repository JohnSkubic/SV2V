# SV2V
Converter of Synthesizable SystemVerilog to Verilog code

## Motivation

Some open source SystemVerilog projects would benefit from a large amount of users being able to run the designs.  Many free tools (Icarus Verilog) don't support many of the SytemVerilog constructs.  SV2V aims to convert synthesizable SystemVerilog code into vanilla Verilog so designers can use fully free tools to contribute to open SystemVerilog projects.

## Directory Structure and Code Organization

TODO

## SystemVerilog Improvements and Implementation Status for SVD (SystemVerilog for Design)

This section shows what SystemVerilog features need to be implemented in the converter.  Only SystemVerilog constructs that affect synthesizable code are listed.

Completed features will be highlighted in green.
In progress features will be highlighted in yellow.
Not started features will not be highlighted.

### High Importance

- Logic datatype
- Port definitions are now expanded to support a wider variety of datatypes: struct, enum, real, multi-dimensional types
- Interfaces 
  - modports
- Multidimensional packed arrays
- Enumerated data types
- Structures 
- Unions
- Procedural blocks
  - always_comb
  - always_ff
  - always_latch


### Medium Importance

- Procedural assignment operators can now operate directly on arrays
- For-loop construct now allows automatic variable declaration inside the for statement.  Loop control improved by continue and break statements
- SystemVerilog adds a do-while construct
- Parameters can be declared any type, includeing user-defined typedefs

### Low Importance

- Constant variables (use of const)
- Variable initializations can now operate on arrays
- Preprocessor has improved `define macro-substitutions capabilities, specifically substitution within literal-strings
- New integer types (byte 8, shortint 16, int 32, longint 64)

## License

Refer to the "LICENSE" file for licensing information.  All files in this repository are distributed under this license.
