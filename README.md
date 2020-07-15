# Write a Compiler : July 13-17, 2020

Hello! This is the course project repo for the "Write a Compiler"
course.  This project will serve as the central point of discussion, code
sharing, debugging, and other matters related to the compiler project.

Although each person will work on their own compiler, it is requested
that all participants work from this central project, but in a separate
branch.   You'll perform these setup steps:

    bash % git clone https://github.com/dabeaz-course/compilers_2020_07
    bash % cd compilers_2020_07
    bash % git checkout -b yourname
    bash % git push -u origin yourname

There are a couple of thought on this approach. First, it makes it
easier for me to look at your code and answer questions (you can 
point me at your code, raise an issue, etc.).   It also makes it easier
for everyone else to look at your code and to get ideas.  Writing a
compiler is difficult. Everyone is going to have different ideas about
the implementation, testing, and other matters.  By having all of the
code in one place and in different branches, it will be better.

I will also be using the repo to commit materials, solutions, and 
other things as the course nears and during the course.

Finally, the repo serves as a good historical record for everything
that happened during the course after the fact.

Best,
Dave

## Important Note

Everything in this repo is subject to change up until the course start date.
Free feel to look around now, but you may want to check back from time to
time to see what's new.

## Live Session 

The course is conducted live from 09:30 to 17:30 US Central Time on Zoom.
The meeting will be open about 30 minutes prior to the starttime. Meeting
details are as follows:

Topic: Write a Compiler, July 13-17, 2020.
Time: 09:30 - 17:30 US CDT (UTC-05:00). 

Join Zoom Meeting
https://us02web.zoom.us/j/89101593617?pwd=ejg5NmlHVlREbnh0Q0tscDBqZU51QT09

Meeting ID: 891 0159 3617
Password: 681844

## Chat

Discussion/Chat for the course can be found on [Gitter](https://gitter.im/dabeaz-course/compilers_2020_07).

## Course Requirements

Here are some of the basic software requirements:

* Python 3.6 or newer.
* llvmlite
* Clang C/C++ compiler.

One way to get llvmlite is to install the Anaconda Python
distribution.  If you intend to write a compiler in a different
language than Python, you will need to investigate the availability of
tools for generating LLVM. There is probably some library similar to
llvmlite.

## Warmup work

If you're looking to get started, there are some warmup exercises posted
on the wiki.   Reposted here.

* [Warmup Exercises](docs/Warmup-Exercises.md)
* [Recursion Exercises](docs/Recursion-Exercises.md)
* [Project 0 - The Metal](docs/Project0_The_Metal.md)
* [Project 0.25 - The Mental](docs/Project0_25_The_Mental.md)
* [Project 0.5 - SillyWabbit](docs/Project0_5_SillyWabbit.md)

## The Project

We are writing a compiler for the language [Wabbit](docs/Wabbit-Specification.md).
The following links provide more information on specific project stages.

* [Project 1 - The Model](docs/Project1_The_Model.md) ([video, 9 min](https://vimeo.com/437187898/2be4149e65))
* [Project 2 - The Interpreter](docs/Project2_The_Interpreter.md) ([video, 14 min](https://vimeo.com/437683254/2e02302bd4))
* [Project 3 - The Lexer](docs/Project3_Tokenizing.md) ([video, 10 min](https://vimeo.com/438048193/408c6cee16))
* [Project 4 - The Parser](docs/Project4_Parsing.md)([video, 31 min](https://vimeo.com/438047448/2900af0ab5))
* [Project 5 - Type Checking](docs/Project5_Type_Checking.md)([video, 12 min](https://vimeo.com/438496863/40d59a3fb0))
* [Project 6 - Compile to C](docs/Project6_Compile_to_C.md)
* [Project 7 - Transformation](docs/Project7_Transformation.md)
* [Project 8 - Compile to LLVM](docs/Project8_Generating_LLVM.md)
* [Project 9 - Compile to WebAssembly](docs/Project9_Generating_WebAssembly.md)
* [Project 10 - Functions](docs/Project10_Function_Calls.md)
* [Project 11 - Types! Types! Types!](docs/Project11_Types_Types_Types.md)

## Resources

* [Documents & Knowledge Base](docs/README.md)

## Videos

Short video lectures will introduce important parts of the project.
They will be posted here about a day in advance (an email notification
will also be sent).

* [Course Introduction](https://vimeo.com/437164645/de9053efbc) (20 min)
* [Part 0 - Preliminaries](https://vimeo.com/437166026/5a710f2e58) (7 min)
* [Part 1 - The Structure of Programs](https://vimeo.com/437187898/2be4149e65) (9 min)
* [Part 2 - The Evaluation of Programs](https://vimeo.com/437683254/2e02302bd4) (14 min)
* [Part 3 - Tokenizing](https://vimeo.com/438048193/408c6cee16) (10 min)
* [Part 4 - Parsing](https://vimeo.com/438047448/2900af0ab5) (31 min)

## Live Session Recordings

Video recordings of live sessions will be posted here.

**Day 1**

* [Course Intro/Project Demo](https://vimeo.com/437949039/17d0f4b52d) (27 min)
* [Warmup exercises, Project 1 start](https://vimeo.com/437949958/6c08b2b044) (35 min)
* [Project 1, model building](https://vimeo.com/438005734/3978c944d5) (8 min)
* [Project 1, practicalities](https://vimeo.com/438006039/b2c4453294) (35 min)
* [End of day](https://vimeo.com/438017483/bfc2d0bbe7) (7 min)

**Day 2**

* [Start of Day, Model, Pretty Printing](https://vimeo.com/438372824/cd34c3dee2) (20 min)
* [Pretty Printing, Project 2](https://vimeo.com/438373292/1f5a5544f4) (36 min)
* [Project 2, Interpreter](https://vimeo.com/438374155/79bd6e3b28) (20 min)
* [Project 3, Tokenizing](https://vimeo.com/438374640/9bad93ccac) (53 min)
* [Project 4, Parsing](https://vimeo.com/438379681/f366bb2cca) (76 min)

**Day 3**

* [Parsing, Expressions](https://vimeo.com/438721070/4256341742) (25 min)
* [Parser/Interpreter, Testing](https://vimeo.com/438721814/b260282922) (9 min)
* [Project 5, Type Checking](https://vimeo.com/438722105/a425d0ab2c) (30 min)
* [Type checking, end of day](https://vimeo.com/438723019/8db0ba43ca) (16 min)
