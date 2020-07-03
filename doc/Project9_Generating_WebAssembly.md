# Project 9 - Generating WebAssembly

As an alternative to LLVM, you can compile WabbitScript to WebAssembly.  Before going any further, complete the [WebAssembly Tutorial](https://github.com/dabeaz/compilers_2020_05/wiki/WebAssembly-Tutorial).

Once you have completed the tutorial, go to the file `wabbit/wasm.py` and follow the instructions inside.

## Testing

If this part of the project is working, you should be able to take any program in `tests/Script/` and compile it to a WebAssembly file.  For example:

```
bash $ python3 -m wabbit.wasm tests/Script/fact.wb
Wrote out.wasm
bash $ 
```

To test the program, there is an HTML page `test.html`.  Copy it out of the `html/` directory into your directory.  Take a look at what it does.  Now, to see the WebAssembly run in the browser, run a small web server:

```
bash $ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Now, click on [http://localhost:8000/test.html](http://localhost:8000/test.html).  If it's working, you should see the program output in the browser.

## Hints

There are a lot of fiddly bits that can go wrong here. Debugging is often difficult.  If you get no output at all, turn on the debugging features of your browser. WebAssembly related errors are often reported on the JavaScript console. 

Absolutely make sure you go through the WebAssembly tutorial first.  If you can't get that to work, you won't get Wabbit to work either.
