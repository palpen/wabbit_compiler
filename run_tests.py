
from wabbit.tests.test_typecheck import *


def run_test_typecheck():
    test_binop()
    test_unaryop()
    test_declare_constvar()
    test_load()
    test_assignment()
    test_ifstatement()

if __name__ == '__main__':
    run_test_typecheck()

