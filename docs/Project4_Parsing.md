# Project 4 - Parsing

In this project, we write a proper parser for [WabbitScript](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitScript).   This will allow us to build data models directly from source code as opposed to having to build them by hand as we did in `script_models.py`.

Go to the file `wabbit/parse.py` and follow the instructions inside.

## Testing 

When you are done with this project, you should be able to run the parser on programs in `tests/Script/` and see the resulting data model.  Here is an example:

```
bash $ cat tests/Script/fact.wb
/* print values of factorials */

var n int = 1;
var value int = 1;

while n < 10 {
    value = value * n;
    print value ;
    n = n + 1;
}

bash $ python3 -m wabbit.parse tests/Script/fact.wb
[Variable(n, int, Integer(1)), Variable(value, int, Integer(1)), While(BinOp(<, Load(NamedLocation(n)),
 Integer(10)), [Assignment(NamedLocation(value), BinOp(*, Load(NamedLocation(value)), Load(NamedLocation(n)))), 
Print(Load(NamedLocation(value))), Assignment(NamedLocation(n), BinOp(+, Load(NamedLocation(n)), Integer(1)))])]
```

Again, your output might vary depending on how you defined your data model.  Reading that is not always so easy. You might want to add some debugging functions to make it easier to view.  For example, the `to_source()` function in the `wabbit/model.py` file. 

## Interpretation

If you are feeling lucky, you might modify the `wabbit/interp.py` file to run programs.  Have it read source code, parse it into a model, and run it.  For example:

```
bash $ python3 -m wabbit.interp tests/Script/fact.wb
1
2
6
24
120
720
5040
40320
362880
bash $
```

If that works, congratulations! You just wrote a scripting language--albeit a really slow one. 