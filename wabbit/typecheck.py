# typecheck.py
#
# Type Checking
# =============
# This file implements type checking. Wabbit uses what's known as
# "nomimal typing."  That means that types are given unique
# names such as "int", "float", "bool", etc. Two types are the same
# if they have exactly the same name.  That's it.
#
# In implementing the type checker, the best strategy might be to
# not overthink the problem at hand. Basically, you have type names.
# You can represent these names using Python strings and compare them
# using string comparison. This gives you most of what you need.
#
# In some cases, you might need to check combinations of types against a
# large number of cases (such as when implementing the math operators).
# For that, it helps to make lookup tables.  For example, you can use
# Python dictionaries to build lookup tables that encode valid
# combinations of binary operators.  For example:
#
# _binops = {
#     # ('lefttype', 'op', 'righttype') : 'resulttype'
#     ('int', '+', 'int') : 'int',
#     ('int', '-', 'int') : 'int',
#     ...
# }
#
# The directory tests/Errors has Wabbit programs with various errors.

from collections import ChainMap
from .model import *


class CheckContext:
    '''
    Context tracker that managers environment variables
    and errors captured by the type checker
    '''

    def __init__(self, env=None):
        self.env = ChainMap() if env is None else env
        self._errors = []

    def new_child(self):
        ctx = CheckContext(self.env.new_child())
        ctx._errors = self._errors
        return ctx

    def error(self, msg):
        self._errors.append(msg)

    def have_errors(self):
        return bool(self._errors)


# Top-level function used to check programs
def check_program(model):
    ctx = CheckContext()
    check(model, ctx)
    # print("Returned context:", ctx.env)
    return ctx
    # Maybe return True/False if there are errors

# In the dict below,
# key: types of input operation
# value: type of output
_binops = {
    ('int', '+', 'int'): 'int',
    ('int', '-', 'int'): 'int',
    ('int', '*', 'int'): 'int',
    ('int', '/', 'int'): 'int',
    ('int', '<', 'int'): 'bool',
    ('int', '>', 'int'): 'bool',
    ('int', '<=', 'int'): 'bool',
    ('int', '>=', 'int'): 'bool',
    ('int', '==', 'int'): 'bool',
    ('int', '!=', 'int'): 'bool',

    ('float', '+', 'float'): 'float',
    ('float', '-', 'float'): 'float',
    ('float', '*', 'float'): 'float',
    ('float', '/', 'float'): 'float',
    ('float', '<', 'float'): 'bool',
    ('float', '>', 'float'): 'bool',
    ('float', '<=','float'): 'bool',
    ('float', '>=','float'): 'bool',
    ('float', '==','float'): 'bool',
    ('float', '!=','float'): 'bool',

    ('bool', '==', 'bool') : 'bool',
    ('bool', '!=', 'bool') : 'bool',
    ('bool', '&&', 'bool') : 'bool',
    ('bool', '||', 'bool') : 'bool',
}

_unaryops = {
    ('-', 'int'): 'int',
    ('+', 'int'): 'int',
    ('-', 'float'): 'float',
    ('+', 'float'): 'float',
}

# Borrowing from @dabeaze's implementation here
def check(node, ctx):

    # TODO !!! Need to create a data model for Programs! (which is a list of statements)
    if isinstance(node, list):
        for stmt in node:
            value_type = check(stmt, ctx)
        return value_type

    # Expression must return a type
    if isinstance(node, ExprAsStatement):
        return check(node.expression, ctx)

    # Expression must return a type
    elif isinstance(node, Integer):
        # ??? Why do we want to attach the expression type to the node ???
        # ANS: To fill in missing type information
        # e.g. var x = 42 where the type of x shold be an int
        typ = 'int'
        node.type = typ
        return typ

    # Expression must return a type
    elif isinstance(node, Float):
        typ = 'float'
        node.type = typ
        return typ

    # Expression must return a type
    elif isinstance(node, UnaryOp):
        operand_type = check(node.operand, ctx)
        result_type = _unaryops.get((node.op, operand_type))
        node.type = result_type

        if not result_type:
            ctx.error(f'Type error {node.op}{operand_type}')
        return result_type

    # Expression must return a type
    elif isinstance(node, BinOp):
        left_type = check(node.left, ctx)
        right_type = check(node.right, ctx)

        # Use `get` method to return None if key is not in table
        result_type = _binops.get((left_type, node.op, right_type))

        # Attach the resulting type to the BinOp object
        node.type = result_type

        if not result_type:
            ctx.error(f"Type error ({left_type} {node.op} {right_type})")
        return result_type

    # Statements does not need to return anything...generally???
    elif isinstance(node, (DeclareConst, DeclareVar)):
        if node.value:
            value_type = check(node.value, ctx)

            if node.type is None:
                node.type = value_type
            if node.type != value_type:
                # Type clash
                ctx.error(f"Type mismatch in initialization")

        current_scope = ctx.env.maps[0]  # current scope is the 1st element
        # print("DeclareVar current_scope",current_scope)
        if node.name in current_scope:
            ctx.error(f"Duplicate definition of {node.name}")
        else:
            ctx.env[node.name] = node

    elif isinstance(node, Print):
        # print doesnt need to return anything because it is a statement
        check(node.expression, ctx)

    elif isinstance(node, Load):
        # Returns the type of the variable to be loaded

        # checks every scope in ctx.env
        if node.location not in ctx.env:
            ctx.error(f"Bad assignment (undefined name)")

        if node.location in ctx.env:
            declared_node = ctx.env[node.location]
            node.type = declared_node.type  # For use later in assignment
            return declared_node.type

    elif isinstance(node, Assignment):

        if node.location not in ctx.env:
            ctx.error("Bad assignment (undefined name)")

        # We do a loop because we want to use the variables
        # in the most current scope first before using variables
        # from a higher scope
        for scope in ctx.env.maps:
            if node.location in scope:
                declared_node = scope[node.location]  # get node from scope
                value_type = check(node.value, ctx)  # get type of value being asgn

                if declared_node.type != value_type:
                    ctx.error("Bad assignment (type error)")

                if isinstance(declared_node, DeclareConst):
                    ctx.error("Can't assign to const")

    elif isinstance(node, IfStatement):
        cond_val_type = check(node.condition, ctx)  # type (bec. expression)
        # TODO Need to implement Bools to check cond_val_type is a bool
        check(node.consequence, ctx)
        check(node.alternative, ctx)

    else:
        raise RuntimeError(f"Cannot type check node {node}")


# Sample main program
def main(filename):
    from .parse import parse_file
    model = parse_file(filename)
    check_program(model)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])







