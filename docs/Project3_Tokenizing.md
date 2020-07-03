# Project 3 - Tokenizing

This project starts the process of building a parser that can take
[WabbitScript](WabbitScript.md) source text and turn it into the data
model you created in Project 1.

Go to the file `wabbit/tokenize.py` and follow the instructions inside.

## Testing

Once you have written a tokenizer, you should be able to test it on
some sample input programs in the `tests/Script/` directory.  For
example:

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

bash $ python3 -m wabbit.tokenize tests/Script/fact.wb
Token(type='VAR', value='var', lineno=3, index=34)
Token(type='NAME', value='n', lineno=3, index=38)
Token(type='NAME', value='int', lineno=3, index=40)
Token(type='ASSIGN', value='=', lineno=3, index=44)
Token(type='INTEGER', value='1', lineno=3, index=46)
Token(type='SEMI', value=';', lineno=3, index=47)
Token(type='VAR', value='var', lineno=4, index=49)
Token(type='NAME', value='value', lineno=4, index=53)
Token(type='NAME', value='int', lineno=4, index=59)
Token(type='ASSIGN', value='=', lineno=4, index=63)
Token(type='INTEGER', value='1', lineno=4, index=65)
Token(type='SEMI', value=';', lineno=4, index=66)
Token(type='WHILE', value='while', lineno=6, index=69)
Token(type='NAME', value='n', lineno=6, index=75)
Token(type='LT', value='<', lineno=6, index=77)
Token(type='INTEGER', value='10', lineno=6, index=79)
Token(type='LBRACE', value='{', lineno=6, index=82)
Token(type='NAME', value='value', lineno=7, index=88)
Token(type='ASSIGN', value='=', lineno=7, index=94)
Token(type='NAME', value='value', lineno=7, index=96)
Token(type='TIMES', value='*', lineno=7, index=102)
Token(type='NAME', value='n', lineno=7, index=104)
Token(type='SEMI', value=';', lineno=7, index=105)
Token(type='PRINT', value='print', lineno=8, index=111)
Token(type='NAME', value='value', lineno=8, index=117)
Token(type='SEMI', value=';', lineno=8, index=123)
Token(type='NAME', value='n', lineno=9, index=129)
Token(type='ASSIGN', value='=', lineno=9, index=131)
Token(type='NAME', value='n', lineno=9, index=133)
Token(type='PLUS', value='+', lineno=9, index=135)
Token(type='INTEGER', value='1', lineno=9, index=137)
Token(type='SEMI', value=';', lineno=9, index=138)
Token(type='RBRACE', value='}', lineno=10, index=140)
```

Your output might vary slight depending on how you implement things, but it should roughly look like that--a stream of tokens representing the input program.


