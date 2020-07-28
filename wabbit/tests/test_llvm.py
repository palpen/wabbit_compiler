import warnings

from wabbit.interp import *
from wabbit.model import *
from wabbit.parse import *
from wabbit.typecheck import *
from wabbit.llvm import *

def run(source):

    # Parse wabbit soure code to convert to data model
    print(">>>> Model being run:")
    model = parse_source(source)
    print(model)

    # Run data model through type checker
    check_program(model)

    # Generate LLVM code
    llvm_code = generate_program(model, write_out=True)

    # Run data model through interpreter to compare with LLVM output
    print(">>> Output of interpreter:")
    print(interpret_program(model))

def test_simple_print():
    source = """
        print 60;
        print 50;
    """
    run(source)

def test_intfloat_arithmetic():
    source = """
        print 1 + 3;
        print 2 * 3;
        print 4 / 2;
        print 4 - 2;
        print 4 - 5;
        print -3 + 10;
        print -3.0 + 10.1;
    """
    run(source)

def test_vardeclaration():
    source = """
        var x int = 4;
        var y int = 5;
        print x + y;
    """
    run(source)

def test_vardeclaration2():
    source = """
        var x int = 4.;
        var y int = 5.;
        print x + y;
    """
    # run(source)
