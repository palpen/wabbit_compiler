# WabbitScript

WabbitScript is a subset of the Wabbit language that consists of mathematical expressions, variables, printing, relations, booleans, and control flow.   There are no functions or user-defined types... because of "reasons."

Here are the core features of WabbitScript shown in an example:

```
// Printing and math expressions involving ints and floats
print 3 + 4 * -5;             
print 3.4 - 5.6 / -7.8;

// Characters
print 'x';
print '\n';

// Constants
const pi = 3.14159;          
const tau = 2.0 * pi; 

// Variables
var r float;
var a float;

// Assignment and lookup of variables
r = 2.0;
a = pi*r*r;

// Relations, booleans, and boolean expressions
var c bool = true;
c = a < 100.0;
var d = (a > 0.0) && (a < 10.0);
print d;

// Conditionals
if a > 0.0 {
   print a;
} else {
   print -a;
}

// Loops
var n = 0;
while n < 10 {
    print n;
    n = n + 1;
}

// Loop control flow (break/continue)
n = 0;
while true {
    n = n + 1;
    if n > 10 {
         break;
    }
    if n == 5 {
         continue;
    }
    print n;
}
```

## Implementation Notes

* WabbitScript is strongly typed.  Mathematical expressions only work if all of the types match. So, `3 + 4` is fine. `3 + 4.0` is an error.

* Relations such as `a < b` produce a boolean.

* The test for control-flow features must evaluate to a bool.  It is illegal to write things like `if a { ... }` if `a` is some type like an `int` or `float`.

* Expressions in WabbitScript have the same precedence and associativity rules as math in other programming languages.   If you write `x + y * z`, it evaluates as `x + (y * z)` not as `(x + y) * z`.

    
## Test Programs

The `Scripts/` directory has a number of test programs that only make use of features of WabbitScript. Look at these programs for testing your compiler. 

