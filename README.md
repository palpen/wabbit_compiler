# Wabbit Compiler

A simple compiler I'm writing in Python for David Beazely's "Write a Compiler" course. The compiler compiles a simple programming language called Wabbit into LLVM. The compiler at present can only do simple arithmetic.

Features that need to be implemented

- [] Variable declaration
- [] Control flow
- [] Loops
- [] Boolean and character types
- [] Compound statements

The goal is to be able to plot the Mandelbrot set by compiling the Wabbit code [here](https://github.com/dabeaz-course/compilers_2020_07/blob/dabeaz/tests/Script/mandel_loop.wb) in LLVM.

### Testing the compiler

To test the compiler, do `./compile_tests.sh`

### Adding new features

To add a new feature
    * Add the data model for the feature in `wabbit/model.py`
    * Add support for the feature in
        * `wabbit/interp.py`
        * `wabbit/tokenize.py`
        * `wabbit/parse.py`
        * `wabbit/typecheck.py`
        * `wabbit/llvm.py`

