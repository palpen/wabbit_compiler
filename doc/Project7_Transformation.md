# Project 7 : Transformation

One of the most critical parts of the whole compiler is the data model that you use to represent programs.  For example, to represent an expression such as `2 + 3 * 4`, you might have a data structure like this:

```
BinOp('+', Integer(2), BinOp('*', Integer(3), Integer(4)))
```

When generating the low-level code, your compiler might emit instructions roughly like this:

```
t1 = 3 * 4;
t2 = 2 + t1;
```

However, a lot of this seems like unnecessary work.  For example, couldn't the compiler just figure out the value in advance and emit this instead?   

```
t2 = 14;
```

In short, the answer is yes.  One way to do this is to recognize patterns in the data model and to simplify the model.  As an example, if you had a node like this:

```
BinOp('*', Integer(3), Integer(4))
```

It could be replaced by a new node:

```
Integer(12)
```

Your task in this project is to see if you can apply transformations to the model that result in more efficient and/or simplified code generation.    The above example is known as "constant folding."  However, there are other kinds of transformations that could be applied.  For example, perhaps you could implement short-circuit evaluation of boolean expressions this way.   See the file `tests/Script/short.wb` for an example of such a program.

More instructions can be found in the file `wabbit/transform.py`.


