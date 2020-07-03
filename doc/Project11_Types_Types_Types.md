# Project 11 - Types! Types! Types!

In this project, you extend WabbitFunc to [WabbitType](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitType-Specification).  This is the full Wabbit Language.

In a nutshell, you are extending Wabbit to have user-defined structure and enum types.  Virtually every part of the compiler will need to be modified.  The type-checker is going to become a lot more complicated. You are going to face a lot of challenges in code generation related to mapping user-defined types to structures in LLVM and WebAssembly.  You will definitely want to consult the knowledge base.  For example:

* [Generating Structures in LLVM](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitType-Specification)
* [Generating Code for Enums](https://github.com/dabeaz/compilers_2020_05/wiki/Generating-Code-for-Enums)

## Testing

The `tests/Type/` directory contains test programs related to WabbitType.  If you want the ultimate challenge, try to compile `tests/Type/mandel_struct.wb`.

## Commentary

Completing this part of the project is likely to be extremely difficult.  Is it doable? Yes.  However, there are a lot of fine details and a lot of things that can go wrong.   To make it work, I'd focus heavily on getting data structures to work under the interpreter and transpiler first.  Only when you get that fully working would I move on to something like LLVM or WebAssembly. 
