# WabbitFunc

WabbitFunc is an extension of [WabbitScript](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitScript) that adds the
ability to define functions.  In a nutshell, you can now write code like this:

```
func square(x int) int {
    return x * x;
}

func abs(x float) float {
    if x > 0.0 {
        return x;
    } else {
        return -x;
    }
}

const TOLERANCE = 0.000000001;

func sqrt(x float) float {
    var guess = 1.0;
    var nextguess = 0.0;
    while true {
        nextguess = (guess + (x / guess)) / 2.0;
        if (abs(nextguess-guess)/guess) < TOLERANCE {
            break;
        }
        guess = nextguess;
    }
    return guess;
}

// Example
func main() void {
    var n = 0;
    // Print the first 10 squares
    while n < 10 {
        print square(n);
        n = n + 1;
    }
    // Print the sqrt of the first 10 integers
    var f = 0.0;
    while f < 10.0 {
        print sqrt(f);
        f = f + 1.0;
    }
}
```

## Implementation Hints

To implement WabbitFunc, you'll need to add the following core features to your compiler:

* Function definitions using the `func` keyword.  A function definition creates a function object. A function object has parameters, a return type, and a list of statements that form the function body.

* Function call expression.  Code such as `func(arg1, arg2, ...)` should execute a function and return a result. A function call is sometimes called a "function application." 

* Return statement.  `return expr;` returns a value from a function.

* Scoping. Functions have local variables. You will need to make a distinction between global variables and local variables. 

* Type checking.  You'll need to check the number of arguments, the types of all arguments, and the return type of all function calls. 

Implementing functions will touch all parts of your compiler. It's a good idea to make sure that WabbitScript is working first. 