import warnings

from wabbit.model import *
from wabbit.parse import *
from wabbit.typecheck import *
from wabbit.llvm import *

def run(source, out):
    model = parse_source(source)
    print(model)
    check_program(model)
    llvm_code = generate_program(model, write_out=True)
    print(llvm_code)
    # TODO: Compare output with out

def test_example0():
    source = """
        print 60;
        print 50;
    """
    out = """
    """
    print(">>>>> LLVM code:")
    run(source, out)

def test_example1():
    source = """
        var x int = 4;
        var y int = 5;
        print x + y;
    """
    out = """
    ; ModuleID = "wabbit"
    target triple = "unknown-unknown-unknown"
    target datalayout = ""

    define i32 @"main"()
    {
    entry:
      %"x" = alloca i32
      %"y" = alloca i32
      store i32 4, i32* %"x"
      store i32 5, i32* %"y"
      %".4" = load i32, i32* %"x"
      %".5" = load i32, i32* %"y"
      %".6" = add i32 %".4", %".5"
      %"d" = alloca i32
      store i32 %".6", i32* %"d"
      %".8" = load i32, i32* %"d"
      ret i32 %".8"
    }
    """
    run(source, out)

