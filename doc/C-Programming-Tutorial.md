Parts of the compiler project involve writing code in C.  This tutorial presents the absolute basics you need to know about C for the purposes of this class--which turns out to not be too much.

## Hello World

Here is a basic "Hello World" program in C:

```
/* hello.c */
#include <stdio.h>

int main() {
    printf("Hello World\n");
    return 0;
}
```

All C programs start in a function called `main()`.  The `printf()` function is how you make output.  The `#include <stdio.h>` is like an import statement that declares `printf()` as well as a variety of other functions.

To compile and run it, you'll probably need to invoke C from the command line:

```
bash $ cc hello.c -o out.exe
bash $ ./out.exe
Hello World
bash $
```

## Variables and Types

C has a few core datatypes such as `int`, `double`, and `char` for representing data of different types. Here is a sample program that declares some variables and prints them out:

```
/* example.c */
#include <stdio.h>

int main() {
    int x = 42;
    double y = 3.14159;
    char c = 'z';

    printf("%i\n", x);
    printf("%lf\n", y);
    printf("%c\n", c);
    return 0;
}
```

Try compiling and running the above program. You should get this output:

```
bash $ cc example.c -o out.exe
bash $ ./out.exe
42
3.141590
z
bash $
```

## Math Expressions

C understands the usual math operators of `+`, `-`, `*`, `/` and follows the same order of evaluation rules as most other programming languages.  The result type is always the same type as the input operands. Try performing some math operations and printing the result.

```
/* example.c */
#include <stdio.h>

int main() {
  int x = 42;
  double y = 3.14159;
  char c = 'z';

  printf("%i\n", x + 10);
  printf("%i\n", x / 10);
  printf("%lf\n", y + 10.0);
  printf("%lf\n", y / 10.0);
  return 0;
}
```

Compile and run:

```
bash $ cc example.c -o out.exe
bash $ ./out.exe
52
4
13.141590
0.314159
bash $
```

## Conditionals and Looping

C support both the `if`-statement and `while`-loops.   Here are some samples:

```
/* example.c */
#include <stdio.h>

int main() {
  int n = 0;
  int sum = 0;
  while (n < 10) {
    sum = sum + n;
    n = n + 1;
  }
  printf("%i\n", sum);
  if (sum > 100) {
    printf("Seems kind of big\n");
  } else {
    printf("Yawn.\n");
  }
  return 0;
}
```

The test used for `if` and `while` needs to be enclosed in parentheses.  C uses `<`, `>`, `<=`, `>=`, `==`, and `!=` for comparisons.   The operators `&&`, `||`, and `!` are used for logical-and, logical-or, and logical-not.

Compile and run:

```
bash $ cc example.c -o out.exe
bash $ ./out.exe
45
Yawn
bash $
```

## Goto

Suppose you think that structured control flow is harmful. You can always use `goto` statements instead. Here's
a different version of the above program:

```
/* example.c */
#include <stdio.h>

int main() {
  int n = 0;
  int sum = 0;

 test:
  if (n >= 10) goto end;
  sum = sum + n;
  n = n + 1;
  goto test;

 end:
  printf("%i\n", sum);
  if (sum > 100) goto big; else goto small;

 big:
    printf("Seems kind of big\n");
    goto exit;
 small:
    printf("Yawn.\n");
    goto exit;
 exit:
  return 0;
}
```

Why for all that is good in computing would `goto` be introduced here?  Reasons. Reasons related to compiler writing.

## Functions

Here's an example of defining and calling a new function:

```
/* squares.c */

#include <stdio.h>

/* User-defined function */
int square(int x) {
   return x * x;
}

int main() {
   int n = 0;
   while (n < 10) {
       printf("%i\n", square(n));
       n = n + 1;
   }
   return 0;
}
```

Compile and run the above code to see what it does.

## Structures

C allows you to define new data types.  Here's an example of making a structure:

```
/* fraction.c */

#include <stdio.h>

struct Fraction {
  int numer;
  int denom;
};

struct Fraction mul_frac(struct Fraction a, struct Fraction b) {
  struct Fraction result;
  result.numer = a.numer * b.numer;
  result.denom = a.denom * b.denom;
  return result;
}

int main() {
  struct Fraction a = { 2, 3};
  struct Fraction b = { 4, 5};
  struct Fraction c = mul_frac(a, b);
  printf("%i %i\n", c.numer, c.denom);
  return 0;
}
```

Compile and run the above code to see what it does.

## More?!?

There is a lot more to C that could be covered here. However, for the purposes of writing our compiler, you're not going to need to know much more than what's covered above.  The basic checklist:

* Make sure you include `#include <stdio.h>`
* Make sure there is a `main()` function.
* All variables have types and must be declared before use.
* Expressions, conditionals, and loops work about the same as they do in Python.
* Use `printf()` for printing. 
* You can write spaghetti code with `goto` if you want.
* `struct` can be used to define new data structures.


