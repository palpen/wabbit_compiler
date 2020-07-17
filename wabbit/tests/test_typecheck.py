'''
To run test, execute run_test.py from top level dir of repo
'''

import warnings

from wabbit.model import *
from wabbit.parse import *
from wabbit.typecheck import *

def has_error(source, err_msg=None, pe=False):
    # Check if there's an error (borrowed from @dcrosta)

    model = parse_source(source)
    print(model)
    errors = check_program(model)

    errors_list = errors._errors

    if pe:
        print(f"Errors returned: {errors_list}\n")

    if errors_list:
        if err_msg:
            for err in errors_list:
                if err_msg == err:
                    return err
            else:
                warnings.warn(f"Error did not match: {errors}")
                return None
            return True
        else:
            return f"No errors expected but found {errors_list}"
    else:
        return None

#def get_type(source):
#    model = parse_source(source)
#    errors = check_program(model)


def test_binop():
    assert not has_error("1 + 1;")

    assert has_error("1 + 1; 2+3.;", "Type error (int + float)")
    assert has_error("1. + 1 - 2.;", "Type error (float + int)")

def test_unaryop():
    assert not has_error("-1;")
    assert not has_error("-1.;")
    assert not has_error("+4.234234;")
    assert not has_error("-----1;")
    assert not has_error("--+-1;")

    # TODO Write test for following
    # has_error("-a;")
    # has_error("-(1);")

def test_declare_constvar():
    assert not has_error("var x int;", pe=True)
    assert not has_error("var x int = 5;", pe=True)
    assert has_error("var x int; var x int;", "Duplicate definition of x")

    assert not has_error("const x int = 1;", pe=True)
    assert not has_error("const x = 1;", pe=True)


    # TODO: Test this in the assignment; should fail if x hasn't been declared
    has_error("x = 3;", pe=True)
    # TODO
    # has_error("var x;", pe=True)

def test_declare_const():
    ...

def test_load():
    ...
