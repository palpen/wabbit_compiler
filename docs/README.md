# Write a Compiler

Various course materials, specifications, and other documents are
found here.  (Note: Until the course starts, all of this material is
subject to frequent change). Submit questions as issues. Feel free to
fix small typos.

* [Project Overview](Compiler-Project-Overview.md)
* The [Wabbit Specification](Wabbit-Specification.md)

## Preparation Exercises (Coding Practice)

* [Warmup Exercises](Warmup-Exercises.md)
* [Recursion Exercises](Recursion-Exercises.md)

## Project Milestones

### Preliminaries

* [Project 0 - The Metal](Project0_The_Metal.md)
* [Project 0.5 - SillyWabbit](Project0_5_SillyWabbit.md)

### WabbitScript

Our first task is to implement a compiler for [WabbitScript](WabbitScript.md), a subset of the Wabbit language that only supports scripting statements.

* [Project 1 - The Model](Project1_The_Model.md)
* [Project 2 - The Interpreter](Project2_The_Interpreter.md) 
* [Project 3 - The Lexer](Project3_Tokenizing.md)
* [Project 4 - The Parser](Project4_Parsing.md)
* [Project 5 - Type Checking](Project5_Type_Checking.md)
* [Project 6 - Compile to C](Project6_Compile_to_C.md)
* [Project 7 - Transformation](Project7_Transformation.md)
* [Project 8 - Compile to LLVM](Project8_Generating_LLVM.md)
* [Project 9 - Compile to WebAssembly](Project9_Generating_WebAssembly.md)

### WabbitFunc

Once you have WabbitScript working, you will add support for user-defined functions.  See [WabbitFunc](WabbitFunc.md).

* [Project 10 - Functions](Project10_FunctionCalls.md)

### WabbitType

Where do you go once you've made it all the way to Project 10 and functions are working?  Project 11 obviously! The final stage of the project is to add support for user-defined types. See [WabbitType](WabbitType.md).

* [Project 11 - Types! Types! Types!](Project11_Types_Types_Types.md)

## Knowledge Base

* [C Tutorial](C-Programming-Tutorial.md)
* [LLVM Tutorial](LLVM-Tutorial.md)
* [WebAssembly Tutorial](WebAssembly-Tutorial.md)
* [Implementing Control Flow](Control-Flow.md)
* [Implementing Functions](Function-Implementation-Notes.md)

## Tools and Specifications

* [SLY](https://github.com/dabeaz/sly)
* [Wasm Specification](https://webassembly.github.io/spec/core/index.html)

