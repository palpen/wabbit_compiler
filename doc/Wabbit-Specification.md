# Introducing Wabbit

You are going to be implementing a programming language called
"Wabbit."  Wabbit is statically typed (like C, Java, Rust, etc.). The syntax is
roughly similar to Go, but some of the features are inspired by Rust.   Ultimately, you'll be able to
compile Wabbit programs that execute as stand-alone executables or as
programs that execute under WebAssembly in the browser.

Most parts of Wabbit are straightforward--being identical to features of programming languages that you already know.  However, some parts of Wabbit are significantly more challenging to understand and implement.  For example, short-circuit evaluation or pattern matching on enums.  Expect to be pushed to the limit on the project. 

## 0. A Taste of Wabbit

Here is a sample Wabbit program that computes the first 30 ever-so-useful
Fibonacci numbers:

```
/* fib.wb -  Compute fibonacci numbers */

const LAST = 30;            // A constant declaration

// A function declaration
func fibonacci(n int) int {
    if n > 1 {              // Conditionals
        return fibonacci(n-1) + fibonacci(n-2);
    } else {
        return 1;
    }
}

func main() int {
    var n int = 0;            // Variable declaration
    while n < LAST {          // Looping (while)
        print fibonacci(n);   // Printing
        n = n + 1;            // Assignment
    }
    return 0;
}
```

This program, although small, illustrates most of Wabbit's basic features
including variables, functions, conditionals, looping, and printing.  

## 1. Syntax

Wabbit programs consist of statements, expressions, and definitions.  Each of these is normally terminated
by a semicolon.  For example:

```
print 3;
var a int = 4;
```

A single-line comment is denoted by `//`.  For example:

```
var a int = 4;    // This is a comment
```

Multiline comments can be written using `/* ... */`. For example:

```
/* 
 This is a multiline
 comment.
*/
```

An identifier is a name used to identify variables, constants, types, and
functions.  Identifiers can include letters, numbers, and the
underscore (_), but must always start with a non-numeric character 
(Wabbit follows the same rules as Python).  The following reserved words
may not be used as an identifier:

```
break const continue else enum import false func if let match 
print return struct true while var
```

A numeric literal such as `12345` is intepreted as an integer.  A
numeric literal involving a decimal point such as `1.2345` is
interpreted as a floating point number.  The literals `true` and
`false` are interpreted as booleans.  

A character literal such as `'h'` is interpreted as a single
text character. Escape codes such as `\'`, `\n`, `\\`, and `\xhh`
are to be interpreted in the same way they are in Python.  Wabbit does
not have multi-character text strings (although it could if you made it). 

The literal `()` is interpreted as the instance of the `unit` type.  See the section on types.

Curly braces are used to enclose blocks of statements or expressions for the purpose of
expressing control flow or defining compound expressions. For example:

```
if a < b {
   statement1;
   statement2;
} else {
   statement3;
   statement4;
}
```

## 2. Types

Wabbit implements a static type system similar to C or Java.

### 2.1 Built-in types

There are four built-in datatypes; `int`, `float`, `char`, and `bool`.

`int` is a signed 32-bit integer.  `float` is a 64-bit double precision
floating point number.  `char` is a single character, represented
as a byte. `bool` represents the boolean values `true` and `false`.

### 2.2 Defining Variables

Variables are declared using a `var` declaration.  They must also have a type and
optional initializer.  For example:

```
var a int;
var b float = 3.14159;
var c bool;  
var d char = 'h';
```

When given an initializer, the type may be omitted--in which case
the type is inferred from the initial value.  For example, these
declarations are legal:

```
var b = 3.14159;    // type float (inferred)
var d = b * 2.0;    // type float (inferred in expression)
```

Immutable variables may be declared using `const`.  `const`
declarations must include an initializer.  For example:

```
const e = 4;        // Integer constant
const f = 2.71828;  // Float constant
const g = true;     // Bool constant
const h = 'h';      // Char constant
```

A `const` declaration may include a type even though it is
redundant.  For example:

```
const e int = 4;    // Integer constant
```

### 2.3 Structures

A data structure can be defined using the `struct` declaration:

```
struct Point {
    x int;
    y int;
}
```

A structure value is created using the type name as a function. The arguments
correspond to the values of the structure fields and must match their type.

```
var p = Point(2, 3);
```

Members of a structure are accessed via dot (.).  For example:

```
print p.x;
var s = p.x + p.y;
p.x = p.x + 10;
```

Structures may be nested:

```
struct Rectangle {
    Point p1;
    Point p2;
}

var r = Rectangle(Point(2, 3), Point(4, 5));
print r.p1.x;
print r.p1.y;
```

Structures may NOT be recursive:

```
struct Spam {
     x int;
     y Spam;      // ERROR. No recursive strutures!
}
```

### 2.4 Enumerations

An enumeration represents a single choice between several options.  Here are a few examples:

```
enum Color {
    Red;
    Green;
    Yellow;
}

enum MaybeNumber {
    No;
    Integer(int);
    Real(float);
}
```

The choices defined within an enum can be simple names such as `Green` or `No`.  A name can also be parameterized with a single typed value such as `Integer(int)`.    

An instance of an enumeration is constructed using the name of the `enum` along
with one of the choices.  For example::

```
var a = MaybeNumber::No;
var b = MaybeNumber::Integer(42);
var c = Color::Red;
```

If you've never encountered enums before, they might look rather exotic.  However, the best way to think of them is as named values.  For example, an instance of `MaybeNumber` could be expressed in Python using tuples like this::

```
a = ('No', )           # a = MaybeNumber::No
b = ('Integer', 42)    # b = MaybeNumber::Integer(42)
```

### 2.4 Unit

The built in datatype `unit` represents a singleton object that's used to represent the result of operations that produce no interesting value at all. The `unit` object itself is written using `()`.   For example:

```
var a = ();                  // a has type "unit"

func print_point(Point p) {  // No return type. Assume "unit"
    print p.x;
    print p.y;
}
```

The best analogy for `unit` is Python's `None` object.  In Python `None` is a special singleton object.  It's used as the return value of functions that don't return any other kind of result.  `unit` is the same concept.  A common confusion with `unit` is that it's not simply "nothing."  It has a value (albeit, an uninteresting one). There is a unit object you can refer to by writing `()`.  Likewise, in Python `None`, is an object as well.  You can pass `None` around, store it in variables, and so forth.  Wabbit has similar behavior. 

C programmers might look at `unit` and wonder if it's the same as the C `void` type.  In short, no.  `void` serves a somewhat similar purpose, but `void` represents nothing at all.  It's not an object.  You can't instantiate a value of type `void` whereas `unit` actually has a value.  

## 3. Operators and Expressions

An expression represents something that evaluates to a value (i.e., an integer, float, structure, etc.). Think of it as code that could legally go on the right-hand-side of an assignment:

```
x = expression;
```

### 3.1 Numeric operators

Numeric types support the binary operators `+`, `-`, `*`, and
`/` with their standard mathematical meaning.  Operators require
both operands to be of the same type.  For example, `x / y` is only
legal if `x` and `y` are the same type.  The result type is always
the same type as the operands.   Note: for integer division, the result
is an integer and is truncated.

Numeric types also support the unary operators of `+` and `-`. For
example:

```
z = -y;
z = x * -y;
```

No automatic type coercion is performed.  Thus, integers and floats
can not be mixed together in an operation.  If this is desired, 
one of the values may be converted to the other using an 
explicit type cast.  For example:

```
var a = 2;
var b = 2.5;
var c float = float(a) + b;  // Explicit cast (a->float)
var d int = a + int(b);      // Explicit cast (b->int)  
```

Numbers can be compared using `<`, `<=`, `>`, `>=`, `==`,
and `!=` with their usual meaning.  The result of any comparison is of type `bool`.

### 3.2 Character operations

Character literals support no mathematical operations whatever. A character is simply
a "character" and that's it.  However, characters can be compared using
`<`, `<=`, `>`, `>=`, `==`, and `!=`.  The result of a comparison is based on
the character's numeric representation (i.e., ASCII code).

### 3.3 Boolean operators

The `bool` type only supports the operators `==`, `!=`, `&&` (logical-and),
`||` (logical-or), and `!` (logical-not).  Boolean values are not equivalent
to integers and can not be used in mathematical operators involving
numbers.

Expressions such as the following are illegal unless `a` and `b` are
of type `bool`:

```
a && b;     // Illegal unless a,b are bools
```

Unlike Python, Wabbit is precise with booleans. If a `bool` is expected, you must provide a `bool` and not a "truthy" value like an `int`.

### 3.4 Associativity and precedence rules

All operators are left-associative.   The following chart shows the
precedence rules from highest to lowest precedence:

```
+, -, ! (unary)          // Highest precedence
*, /
+, -
<, <=, >, >=, ==, !=
&&
||                       // Lowest precedence
```

Relational operators may NOT be chained or associate together. For example:

```
a < b && b < c        // OK
a < b < c             // Illegal
```

### 3.5 Short-circuit evaluation

The logical operators `&&` and `||` should implement short-circuit behavior
in evaluation.   That is, in the expression `a && b`, if `a` evaluates
to `false`, then `b` is not evaluated.  Similarly, if `a` evaluates
to `true`, then `a || b` does not evaluate `b`.

As an example, an expression such as this should not cause a crash:

```
const x = 0;
const y = 1;

if (x == 0 or (y / x > 0)) {  /* y/x does not evaluate */
    print 0;
} else {
    print 1;
}
```

### 3.6 Compound Expressions

Normally, an expression is defined by a single operation.  However, arbitrary blocks of statements enclosed
by `{` and `}` can also be used as an expression.  For example:

```
var a = { 1 + 2; 3 + 4; 5 + 6; };
```

For such expressions, the value is the result of the last operation performed. All other results are computed, but discarded. So, in the above example, the value of `a` is set to `11`.  If the last operation produces no value, then the result of a statement block is the unit object `()`.   For example:

```
var b = 2;
var c = { b = b + 1; print b; };    // Result is ()
```

Statement blocks also define a scope in which temporary variables can be assigned. For example,
you could swap the value of two variables by writing code like this:

```
var a = 2;
var b = 3;

a = { var temp = b; b = a; temp; };
// temp variable is no longer defined here (out of scope)
```

This might look rather strange, but having compound expressions can be useful in situations where calculations both produce values and involve side effects such as assignments or I/O. It can also be a useful trick for debugging.  If you wanted to inject a `print` statement somewhere, you can do it with a compound expression. 
For example::

```
func factorial(n int) int {
    if n == 0 {
        return 1;
    } else {
        return n * factorial({print n; n-1;});
    }
}
```

### 3.7 Pattern Matching

A common problem with `enum` types is that of case-analysis (i.e., figuring out which choice is represented by a value).  This is done using the `match` operator as follows:

```
enum MaybeInt {
    No;
    Some(int);
}

a = MaybeInt::Some(42);

var x = match a {
           No => 0;
           Some(val) => val * 10;
        };
```

This matches the value of `a` according to a series of pattern matching clauses. 
Each clause consists of a specific enum choice on the left and an expression on the right, separated by `=>`.
The expression on the right represents the value that's returned by the match.

For choices that include a value, a variable name can be introduced
and used in the resulting expression.  For example, the `val` variable
in the line `Some(val) => val * 10;` above.   In that example, `val` is bound to the
42 in the expression on the right hand side. 

In matching, it's not necessary to fully quality the choice names
such as `MaybeInt::No` or `MaybeInt::Some`.  It's already known what type `a` is so 
you can use the simple names such as `No` and `Some`.  It is an error
to write a `match` expression that doesn't account for all possibilities:

```
var x = match a {                   
           Some(val) => val * 10; 
          // ERROR: No match for No case
        };
```

The underscore can be used as a default to match all remaining cases:

```
var x = match a {
           Some(val) => val * 10;
           _ => 0;             // Default
        };
```

The result value of a `match` expression must be of the same type for
all choices.   This is an error:

```
var x = match a {
            No => 0.0;          // float
            Some(val) => 1;     // int     (TYPE ERROR)
        };
```

Although `match` returns a value, you can also use it to perform printing and other
actions by using compound expressions.   For example:

```
match a {
    No => {
        print 0;
    };
    Some(val) => {
        print val;
    };
};
```

In this example, the result type of `match` is `unit`--indicating the fact that the `print` statement
doesn't actually return an interesting value.

If you're only interested in one of the choices, it is easier to use `if let` as described in the next section.

## 4. Control Flow

Wabbit has basic control-flow features in the form of `if`-statements and `while`-loops.

### 4.1. Conditionals

The `if` statement is used for a basic conditional. For example:

```
if (a < b) {
   statements;
   ...
} else {
   statements;
   ...
}
```

The conditional expression used for the test must evaluate to a `bool`.
Code such as the following is an error unless `a` has type `bool`:

```
if (a) {     // Illegal unless a is type bool
   ...
}
```

The `else` clause in a conditional is optional.

### 4.2 Looping

The `while` statement can be used to execute a loop.  For example:

```
while (n < 10) {
    statements;
    ...
}
```

This executes the enclosed statements as long as the associated
condition is `true`.   Again, the conditional expression must
evaluate to type `bool`.

The `break` statement can be used to break out of a loop early.  For example, this
code only prints the numbers 0, 1, ..., 4:

```
var n int = 0;
while n < 10 {
    statements;
    if (n == 5) {
        break;
    }
    print n;
    n = n + 1;
}
```

The `continue` statement can be used to jump back to the top of a loop, ignoring
the remainder of the loop body.

```
var n int = 0;
while n < 10 {
    statements;
    if n == 5 {
       continue;   // Skip to next iteration
    }
    print n;
    n = n + 1;
}
```

### 4.3 Conditional Pattern Matching

The `if let` construct can be used to match a specific choice in an `enum` type.  For example:

```
enum MaybeInt {
    No;
    Some(int);
}

var a = MaybeInt::No;
var b = MaybeInt::Some(42);

if let No = a {
    // Executes if a has the value MaybeInt::No
} else {
    // Executes if a has some other value.
}

if let Some(x) = b {
    // Executes if b has the value MaybeInt::Some(x)
    print x;   // Variable "x" is bound to the value.  In this case, 42.
}
```

As with the normal `if`-statement, the `else` clause is optional.   There is also a corresponding `while let` statement.  Here is an example:

```
var n = MaybeInt::Some(42);

while let Some(x) = n {
    print x;
    if x > 0 {
        n = MaybeInt::Some(x-1);
    } else {
        n = MaybeInt::No;
    }
}
```

## 5. Functions

Functions can be defined using the `func` keyword as follows:

```
func fib(n int) int {
    if (n <= 2) {
       return 1;
    } else {
       return fib(n-1) + fib(n-2);
    }
}
```

Functions must supply types for the input parameters and return value as shown.  A function can 
have multiple input parameters. For example:

```
func add(x int, y int) int {
    return x + y;
}
```

A function can elect to return no value. For example:

```
func spam(x int) {
    print x*42;
}
```

The return type of such a function is `unit`.   

When calling a function, all function arguments are fully evaluated, left-to-right
prior to making the associated function call.   That is, in a 
call such as `foo(a, b, c)`, the arguments `a`, `b`, and `c`
are fully evaluated to a value first. This is known as "applicative
evaluation order" or "eager evaluation."

All arguments are passed to a function by value--meaning that they are
effectively copies of the input.  This includes structures and enums.  Thus,
you should see this behavior:

```
struct Point {
   x int;
   y int;
}

func f(p Point) {
   p.x = p.x + 10;    // Mutates local p only
}

var q = Point(2, 3);
f(q);         
print q.x;     // prints --> 2
```

Functions may return structures and enums. Again, this is effective a
copy of the data.

## 6.  Scoping rules

Wabbit uses lexical scoping to manage names. Declarations defined
outside of a function are globally visible to the entire
program. Declarations inside a function are local and not visible to
any other part of a program except for code in the same function.  For
example:

```
var a int;     // Global variable

func foo(b int) int {
    var c int;          // Local variable
    ...
}
```

Wabbit also makes use of so-called "block-scope" where variables declared
inside any block of code enclosed by curly braces (`{` ... `}`) are only
visible inside that block.  For example:

```
func bar(a int, b int) int {
    if a > b {
        var t int = b;   // Block scope variable
        b = a;
        a = t;
    }
    print t;             // Error: t not defined (not in scope)
    return a;   
}
```

Nested function definitions are not supported.  For 
example:

```
func foo(b int) int {
     func bar(c int) int {   // Illegal. Nested functions not allowed
         ...
     }
     ...
}
```

## 7.  Main entry point and initialization

Programs always begin execution in a function `main()` which takes
no arguments and returns an integer result.  For example:

```
func main() int {
    var i int = 0;
    while (i < N) {
       print fib(i);
       i = i + 1;
    }
    return 0;
}
```

Any initialization steps related to global variables must execute
prior to the invocation of `main()`.   For example:

```
var a int = 4;
var b int = 5;
var c int = a + b;     // Evaluates prior to main()
...
func main() int {
   ...
}
```

Your compiler should put initialization steps in a special function called `_init()`.   Your compiler 
should then have the `main()` function call `_init()` prior to any other statements.

If there is no `main()` function, any kind of "scripting" statements
will still execute as part of the initialization step.  Your compiler
should emit a dummy main() function that calls `_init()` in this case.

## 8. Printing

The built-in `print value` operation can be used for debugging
output.  It prints the value of any type given to it.  Values are
normally printed on separate lines.  However, if you print a single
character value, it is printed with no line break.

`print` is an example of a polymorphic operation in that it 
works on any kind of data.  This is different than how functions
work--where a matching datatype must be given.

## 9. Formal Grammar

The following grammar is a formal description of Wabbit syntax. Tokens
are specified in ALLCAPS and are assumed to be returned by the tokenizer.
In this specification, the following syntax is used:

```
{ symbols }   --> Zero or more repetitions of symbols
[ symbols ]   --> Zero or one occurences of symbols (optional)
sym1 | sym2   --> Either sym1 or sym2 (a choice)
```

A program consists of zero or more statements followed by the end-of-file (EOF).
Here is the grammar:

```
program : statements EOF

statements : { statement }

statement : print_statement
          | assignment_statement
          | variable_definition
          | const_definition
          | func_definition
          | struct_definition
          | enum_definition
          | if_statement
          | if_let_statement
          | while_statement
          | while_let_statement
          | break_statement
          | continue_statement
          | return_statement
          | expression SEMI

print_statement : PRINT expression SEMI

assignment_statement : location ASSIGN expression SEMI

variable_definition : VAR NAME [ type ] ASSIGN expression SEMI
                    | VAR NAME type [ ASSIGN expression ] SEMI

const_definition : CONST NAME [ type ] ASSIGN expression SEMI

func_definition : FUNC NAME LPAREN [ parameters ] RPAREN type LBRACE statements RBRACE

parameters : parameter { COMMA parameter }
           | empty

parameter  : NAME type 

struct_definition : STRUCT NAME LBRACE { struct_field } RBRACE

struct_field : NAME type SEMI

enum_definition : ENUM NAME LBRACE { enum_choice } RBRACE

enum_choice : NAME SEMI
            | NAME LPAREN type RPAREN
      
if_statement : IF expr LBRACE statements RBRACE [ ELSE LBRACE statements RBRACE ]

if_let_statement : IF LET pattern ASSIGN expression LBRACE statements RBRACE [ ELSE LBRACE statements RBRACE ]

while_statement : WHILE expr LBRACE statements RBRACE

while_let_statement : WHILE LET pattern ASSIGN expression LBRACE statements RBRACE

break_statement : BREAK SEMI

continue_statement : CONTINUE SEMI

return_statement : RETURN expression SEMI

expression : orterm { LOR ortem }

orterm : andterm { LAND andterm }

andterm : sumterm { LT|LE|GT|GE|EQ|NE sumterm }

sumterm : multerm { PLUS|MINUS multerm }

multerm : factor { TIMES|DIVIDE factor }

factor : literal
       | location
       | enum_value
       | match
       | LPAREN expression RPAREN
       | PLUS expression
       | MINUS expression
       | LNOT expression
       | NAME LPAREN exprlist RPAREN
       | LBRACE statements RBRACE
       
literal : INTEGER
        | FLOAT
        | CHAR
        | TRUE
        | FALSE
        | LPAREN RPAREN
 
exprlist : expression { COMMA expression }
         | empty
 
location : NAME
         | expression DOT NAME

enum_value : NAME DCOLON NAME
           | NAME DCOLON NAME LPAREN expression RPAREN

match : MATCH expression LBRACE { matchcase } RBRACE
 
matchcase : pattern ARROW expression SEMI

pattern   : NAME
          | NAME LPAREN NAME RPAREN

type      : NAME

empty     :
```

