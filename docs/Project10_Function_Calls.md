# Project 10 - Function Calls

Project 10 is about turning WabbitScript into [WabbitFunc](WabbitFunc.md).   You're going to have to make changes to virtually every part of your compiler to make this work.

The key is to take it in small steps.  Start with the model.  Think about what's required to represent a function definition and a function call.  Think about the return statement.   Then move on to the parser and modify it read source code with functions.  From there, you work on type checking and code generation.

There are going to be a lot of small details. And in some sense, this part of the project serves as a good review of everything.

## Testing

The directory `tests/Func/` has test programs involving Wabbit functions.  If your compiler can compile and run these, you're well on your way to having a new language.   Try compiling `tests/Func/mandel.wb` to see the Mandelbrot set.
