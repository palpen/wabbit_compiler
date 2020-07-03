# WabbitType Specification

WabbitType is a full implementation of the Wabbit language.  It has
all of the features of
[WabbitFunc](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitFunc)
plus the ability to define user-defined types.  Type-casts and
conversions are also added.

Here are the main features added in WabbitType:

```
// Type conversions
var x int = 2;
var y float = 2.5;

print x + int(y);       // float -> int conversion
print float(x) + y;     // int -> float conversion

// Structure definitions
struct Fraction {
    numer int;
    denom int;
}

func mul(a Fraction, b Fraction Fraction {
    return Fraction(a.numer * b.numer, a.denom * b.denom);
}

var s = Fraction(2, 3);
var t = Fraction(4, 5);
var r = mul(s, t);

// Enum definitions
enum MaybePositive {
     No;
     Yes(float);
}

func f(x float) MaybePositive {
    if x >= 0.0 {
        return MaybePositive::Yes(x);
    } else {
        return MaybePositive::No;
    }
}

var a = f(3.0);
var b = f(-4.0);

// match expressions
var c = match a {
           No => 0.0;
           Yes(x) => 100.0 * x;
        };
print c;     // Prints 300.0
var d = match b {
           No => 0.0;
           Yes(x) => 100.0 * x;
       };
print d;     // Prints 0.0

// if let
if let Yes(x) = a {
   print x;
}

// while let
while let Yes(x) = a {
   print x;
   a = f(x - 1.0);
}

```

## Implementation Notes

Implementing user-defined types is difficult.  Don't even attempt it unless you have WabbitFunc working first.  You will need to modify almost every part of the compiler.  Here are some critical components:

* You need to define `struct` and `enum` objects that represent these definitions.  These objects are containers for other objects that represent structure fields and enum choices.

* You need to support type-conversions and type construction.  This looks (syntactically) the same as a function call.  For example, to create a `Fraction` above, you write `Fraction(2, 3)`.  Or, to convert a value to a `float`, you write `float(x)`.   So, somehow you need to know that these operations are related to type construction as opposed to calling an ordinary function (although there are still many similarities).

* You'll have to extend the concept of a "location" to cover structure attributes.  For example, if `f` is a `Fraction`, then you can write `f.numer` and `f.denom` on both sides of an assignment.  That is, either as a location where you're storing a value or as a location where you're reading a value in an expression.

* You'll need to extend expressions to allow the construction of enum choices.

* Type checking now has a lot of moving parts.  You need to check struct and enum fields. You'll need to track the types of these fields. A lot of checks must show up elsewhere. For example, if using dotted attributes, you need to make sure the dotted attribute name corresponds to a valid structure field.

* Code generation is complicated.  You'll need to figure out how to map type definitions to LLVM and WebAssembly.  WebAssembly has no user-defined structures for instance.

A critical step in implementing types is to implement it in the interpreter first. Make sure you fully understand the semantics of what's happening first.  Get it to work under interpretation.  Then focus on making it work in LLVM or something lower-level.
