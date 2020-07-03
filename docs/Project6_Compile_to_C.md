# Project 6 - Compile to C

A common approach in creating a new language is compiling the language to a different high-level language. One common target is C programming.  In this project, you'll write a compiler that takes [WabbitScript](https://github.com/dabeaz/compilers_2020_05/wiki/WabbitScript) code and turns it into C code.

See the file `wabbit/c.py` for further instructions.

## Testing

For this part of the project, you should be able to take scripts in `tests/Script/` and turn them into C programs. For example:

```
bash $ python3 -m wabbit.c tests/Script/fact.wb
Wrote out.c
bash $ cc out.c
bash $ ./a.out
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

These programs should run significantly faster than the interpreted version.  Try it with the `tests/Script/mandel_loop.wb` program and perform a comparison.

