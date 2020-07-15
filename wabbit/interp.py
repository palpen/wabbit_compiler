# interp.py
#
# In order to write a compiler for a programming language, it helps to
# have some kind of specification of how programs written in the
# programming language are actually supposed to work. A language is
# more than just "syntax" or a data model.  There has to be some kind
# of operational semantics that describe what happens when a program
# runs.
#
# One way to specify the operational semantics is to write a so-called
# "definitional interpreter" that directly executes the data
# model. This might seem like cheating--after all, our final goal is
# not to write an interpreter, but a compiler. However, if you can't
# write an interpreter, chances are you can't write a compiler either.
# So, the purpose of doing this is to pin down fine details as well as
# our overall understanding of what needs to happen when programs run.
#
# We'll write our interpreter in Python.  The idea is relatively
# straightforward.  For each class in the model.py file, you're
# going to write a function similar to this:
#
#    def interpret_node_name(node, env):
#        # Execute "node" in the environment "env"
#        ...
#        return result
#
# The input to the function will be an object from model.py (node)
# along with an object respresenting the execution environment (env).
# The function will then execute the node in the environment and return
# a result.  It might also modify the environment (for example,
# when executing assignment statements, variable definitions, etc.).
#
# For the purposes of this projrect, assume that all programs provided
# as input are "sound"--meaning that there are no programming errors
# in the input.  Our purpose is not to create a "production grade"
# interpreter.  We're just trying to understand how things actually
# work when a program runs.
#
# For testing, try running your interpreter on the models you
# created in the example_models.py file.
#

from collections import ChainMap
from .model import *

# Top level function that interprets an entire program. It creates the
# initial environment that's used for storing variables.

def interpret_program(model):
    # Make the initial environment (a dict)
    env = ChainMap()
    out = interp(model, env)
    print("env content:", env)
    return out

# Internal function to interpret a node in the environment
def interp(node, env):

    # Expand to check for different node types
    if isinstance(node, Integer):
        return int(node.value)

    elif isinstance(node, Float):
        return float(node.value)

    elif isinstance(node, UnaryOp):
        operand = interp(node.operand, env)
        if node.op == '-':
            return -operand
        elif node.op == '+':
            return +operand
        else:
            raise RuntimeError(f'Bad operator {op}')

    elif isinstance(node, (DeclareConst, DeclareVar)):
        # !!! Where to include node.vartype?
        if node.value:
            value = interp(node.value, env)
        else:
            value = None
        env[node.name] = value

    elif isinstance(node, Assignment):
        if node.value:
            value = interp(node.value, env)
        else:
            raise RuntimeError(f'Must assign a value to {name.location}')
        for scope in env.maps:

            # Check that variables has been declared
            # before doing assignment
            if node.location in scope:
                scope[node.location] = value
                break
        else:
            raise NameError(f"{node.location} needs to be declared")

    elif isinstance(node, Load):
        value = env[node.location]
        return value

    elif isinstance(node, IfStatement):
        if interp(node.condition, env):
            return interp(node.consequence, env.new_child())
        else:
            return interp(node.alternative, env.new_child())

    elif isinstance(node, WhileLoop):
        while interp(node.condition, env):
            new_scope = env.new_child()
            interp(node.body, new_scope)

    elif isinstance(node, Compound):
        return interp(node.statements, env.new_child())

    elif isinstance(node, ExprAsStatement):
       return interp(node.expression, env)

    elif isinstance(node, BinOp):
        leftval = interp(node.left, env)
        rightval = interp(node.right, env)
        if node.op == '+':
            return leftval + rightval
        elif node.op == '-':
            return leftval - rightval
        elif node.op == '*':
            return leftval * rightval
        elif node.op == '/':
            # Follow python behaviour with division
            return leftval / rightval
        elif node.op == '<':
            return leftval < rightval
        elif node.op == '>':
            return leftval > rightval
        elif node.op == '<=':
            return leftval <= rightval
        elif node.op == '>=':
            return leftval >= rightval
        elif node.op == '==':
            return leftval == rightval
        elif node.op == '!=':
            return leftval != rightval

    elif isinstance(node, Print):
        print(interp(node.expression, env))
        return None

    elif isinstance(node, Statements):
        value = None
        for s in node.statements:
            value = interp(s, env)
        return value

    else:
        raise RuntimeError(f"Can't interpret {node}")

# Techniques:
# collections.ChainMap for maintaining scopes for the variables
# chainmaps maybe easier that list???
#


