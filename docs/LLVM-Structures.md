# Generation of Structures in LLVM

Wabbit allows data structures to be defined like this:

```
struct Complex {
    real float;
    imag float;
}
```

One issue concerns the mechanism for handling this in LLVM.  Here are some of the steps involved.

## Definining an LLVM Type

You can define a LLVM structure type using `ir.LiteralStructType` like this:

```
>>> from llvmlite import ir
>>> float_type = ir.DoubleType()
>>> Complex_type = ir.LiteralStructType([float_type, float_type])
>>> Complex_type
<<class 'llvmlite.ir.types.LiteralStructType'> {double, double}>
>>>
```

All types need to have an initializer defined.  This is the value that represents the contents of an uninitialized variable. For numbers, it's usually just a zero constant.  For a structure type, you'll want to make one yourself:

```
>>> Complex_initializer = ir.Constant(Complex_type, (ir.Constant(float_type, 0.0), ir.Constant(float_type, 0.0)))
>>> Complex_initializer
<ir.Constant type='{double, double}' value=[<ir.Constant type='double' value=0.0>, <ir.Constant type='double' value=0.0>]>
>>> 
```

You're going to use `Complex_type` and `Complex_initializer` in further code generation steps.

## Declaring a Global Variable

To declare a global variable for this:

```
var a Complex;
```

Take these steps:

```
>>> mod = ir.Module()
>>> a_var = ir.GlobalVariable(mod, Complex_type, "a")
>>> a_var.initializer = Complex_initializer
>>> print(mod)
; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"a" = global {double, double} {double              0x0, double              0x0}
>>>
```

Notice that the process is basically identical to how you create global variables for `int`, `float`, and other primitive types.  The key step is that you have to make sure you have the right initializer value.  Your code generator needs to create this along with the LLVM type itself.

## Declaring Local Variables

Declaring a local variable works the same way as with primitive types.  For example, if you had this:

```
func f() float {
    var x Complex;
    ...
}
```

You will take steps like this:

```
>>> f = ir.Function(mod, ir.FunctionType(float_type, []), name='f')
>>> block = f.append_basic_block('entry')
>>> builder = ir.IRBuilder(block)
>>> x_var = builder.alloca(Complex_type, name="x")
>>> x_var
<ir.AllocaInstr 'x' of type '{double, double}*', opname 'alloca', operands ()>
>>> 
```

## Changing a Structure Field

Suppose you want to change the value of a structure field.  Consider this code:

```
func f() float {
   var x Complex;
   x.imag = 2.5;
   ...
}
```

To do that, use `builder.insert_value()` using the numeric index of the field you want to change.
You also need to perform a few additional load/store steps to account for your local variable.
For this example, the numeric index of `x.imag` is 1.

```
>>> x_value = builder.load(x_var)
>>> new_x_value = builder.insert_value(x_value, ir.Constant(float_type, 2.5), 1)
>>> builder.store(new_x_value, x_var)
>>> print(mod)
...
define double @"f"() 
{
entry:
  %"x" = alloca {double, double}
  %".2" = load {double, double}, {double, double}* %"x"
  %".3" = insertvalue {double, double} %".2", double 0x4004000000000000, 1
  store {double, double} %".3", {double, double}* %"x"
}
```

One very subtle facet of `builder.insert_value()` is that it does not perform an "in-place" modification. Instead, it returns an entirely new structure object where the given field has been updated.  In order for the change to take effect, you need to save the result of `builder.insert_value()` back into the place where you got it.  In this example, that means using `builder.store()` to put the updated value back into the `x` variable.  If you forget this step, you'll be left scratching your head wondering why data structures can't be modified.

## Loading from Structure Fields

Suppose you have code that loads from a structure field like this:

```
func f() float {
    var x Complex;
    ...
    return x.imag;
}
```

For this, use `builder.load()` and `builder.extract_value()` like this:

```
>>> x_value = builder.load(x_var)
>>> x_imag = builder.extract_value(x_value, 1)
>>> builder.ret(x_imag)
>>>
```

Here is the final output of the function you just created:

```
func f() float {
    var x Complex;
    x.imag = 2.5;
    return x.imag;
}

>>> print(mod)
define double @"f"() 
{
entry:
  %"x" = alloca {double, double}
  %".2" = load {double, double}, {double, double}* %"x"
  %".3" = insertvalue {double, double} %".2", double 0x4004000000000000, 1
  store {double, double} %".3", {double, double}* %"x"
  %".5" = load {double, double}, {double, double}* %"x"
  %".6" = extractvalue {double, double} %".5", 1
  ret double %".6"
}
>>>
```

## Creating Structures

A final problem with structures concerns their creation. Wabbit allows the type name to be used as a constructor.  For example:

```
var a = Complex(2.5, 4.7);
```

For this, you can use a bit of so-called "syntactic sugar."  That is, you can solve the problem at a high-level by translating the operation into something else. Instead of figuring out how to directly create LLVM code for this, create a hidden function:

```
func _create_Complex(real float, imag float) Complex {
    var self Complex;
    self.real = real;
    self.imag = imag;
    return self;
}
```

Now, translated `Complex(2.5, 4.7)` into a function call to `_create_Complex(2.5, 4.7)`.  If you have all of the steps above working (declaration of variables, setting attributes, etc.), it will just "work."  You're done.

## Words of Advice

Implementing structures requires you to introduce new kinds of LLVM types as you generate code. Basically, each structure definition introduces a new type.  For each type, you need to use `ir.LiteralStructType()` to bring the type into existence.  You're going to need an initializer value so you can create variables. You're going to need to make a type-constructor function.    There are some messy tricky bits with the process of updating structure attribute values (e.g., the fact that you need to save the new structure value back to the variable where it came from). 

The hardest part of putting all of this together is the book-keeping.  You'll need to figure out where to put all of the extra parts and how to pass the necessary type data around so you can actually make code.



