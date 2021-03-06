# script_models.py
#
# Within the bowels of your compiler, you need to represent programs
# as data structures.   In this file, you will manually encode
# some simple Wabbit programs using the data model you're creating
# in the file wabbit/model.py
#
# The purpose of this exercise is two-fold:
#
#   1. Make sure you understand the data model of your compiler.
#   2. Have some program structures that you can use for later testing
#      and experimentation.
#
# This file is broken into sections. Follow the instructions for
# each part.  Parts of this file might be referenced in later
# parts of the project.  Plan to have a lot of discussion.
#
# Note: This file only includes examples for WabbitScript.  See
#
#     docs/WabbitScript.md


from wabbit.model import *
from wabbit.interp import *
from wabbit.parse import *
from wabbit.tokenize import *



# ----------------------------------------------------------------------
# Simple Expression
#
# This one is given to you as an example. You might need to adapt it
# according to the names/classes you defined in wabbit.model

expr_source = "2 + 3 * 4;"

expr_model  = BinOp('+', Integer("2"),
                         BinOp('*', Integer("3"), Integer("4")))

# ----------------------------------------------------------------------
# Program 1: Printing
#
# Encode the following program which tests printing and evaluates some
# simple expressions.
#
# How do you represent a list of statements? Is that a special kind of object? Or, can you just use a Python list?

source1 = """
    print 2 + 3 * -4;
    print 2.0 - 3.0 / -4.0;
    print -2 + 3;
    print 2 * 3 + -4;
"""

model1 = Statements([
    Print(BinOp('*', BinOp('+', Integer("2"), Integer("3")), UnaryOp('-', Integer("4")))),
    Print(BinOp('/', BinOp('-', Float("2.0"), Float("3.0")), UnaryOp('-', Float("4.0")))),
    Print(BinOp('+', UnaryOp('-', Integer("2")), Integer("3"))),
    Print(BinOp('+', BinOp('*', Integer("2"), Integer("3")), UnaryOp('-', Integer("4")))),
])


# ----------------------------------------------------------------------
# Program 2: Variable and constant declarations.
#            Expressions and assignment.
#
# Encode the following statements.

source2 = """
    const pi = 3.14159;
    var tau float;
    tau = 2.0 * pi;
    print tau;
"""

model2 = Statements([
    DeclareConst('pi', 'float', Float("3.14159")),
    DeclareVar('tau', 'float', None),
    Assignment('tau', BinOp('*', Float("2.0"), Load('pi'))),
    Print(Load('tau')),
])


# ----------------------------------------------------------------------
# Program 3: Conditionals.  This program prints out the minimum of
# two values.
#
source3 = '''
    var a int = 2;
    var b int = 3;
    if a < b {
        print a;
    } else {
        print b;
    }
'''

model3 = Statements([
    DeclareVar('a', 'int', Integer("2")),
    DeclareVar('b', 'int', Integer("3")),
    IfStatement(BinOp('<',
                      Load('a'),
                      Load('b')),
                [Print(Load('b'))],
                [Print(Load('a'))])
])


# ----------------------------------------------------------------------
# Program 4: Loops.  This program prints out the first 10 factorials.
#

source4 = '''
    const n = 10;
    var x int = 1;
    var fact int = 1;

    while x < n {
        print fact;
        x = x + 1;
    }
'''
model4 = Statements([
    DeclareConst('n', None, Integer("10")),
    DeclareVar('x', 'int', Integer("1")),
    DeclareVar('fact', 'int', Integer("1")),
    WhileLoop(BinOp('<', Load('x'), Load('n')),
              Statements([
                Assignment('fact', BinOp('*', Load('fact'), Load('x'))),
                Print(Load('fact')),
                Assignment('x', BinOp('+', Load('x'), Integer("1"))),
#                WhileLoop(BinOp('<', Load('x'), Load('n')),
#                          Statements([Assignment('fact', BinOp('*', Load('fact'), Load('x')))]))
              ])
    )
])


# ----------------------------------------------------------------------
# Program 5: Compound Expressions.  This program swaps the values of
# two variables using a single expression.
#

source5 = '''
    var x = 37;
    var y = 42;
    x = { var t = y; y = x; t; };     // Compound expression.
    print x;
    print y;
'''

model5 = Statements([
    DeclareVar('x', None, Integer("37")),
    DeclareVar('y', None, Integer("42")),
    Assignment('x',
               Compound(Statements([
                    DeclareVar('t', None, Load('y')),
                    Assignment('y', Load('x')),
                    ExprAsStatement(Load('t'))
               ]))
    ),
    Print(Load('x')),
    Print(Load('y'))
])



## Tests

def print_tokenz(text):
    for tok in tokenize(text):
        print(tok)

#source = "haha = 6;"
#source = "print 6.0;"
#source = "print 1+1;"
#source = "print haha;"
#source = "x = 4;"
#source = "var x int;"
#source = "const x int = 5; const x = 5;"

#print_tokenz(source)
#print(parse_source(source))

#print(source1)
#print(source2)
#print(source3)
#print(source4)
#print(source5)

#print(to_source(expr_model))
#print(to_source(model1))
#print(to_source(model2))
#print(to_source(model3))
#print(to_source(model4))
#print(to_source(model5))

#print(interpret_program(expr_model))
#print(interpret_program(model1))
#print(interpret_program(model2))
#print(interpret_program(model3))
#print(interpret_program(model4))
#print(interpret_program(model5))

#print_tokenz(source1)
#print_tokenz(source2)
#print_tokenz(source3)
#print_tokenz(source4)
#print_tokenz(source5)

print(parse_source(source1))
print(parse_source(source2))
print(parse_source(source3))
#print(parse_source(source4))  # TODO implement while
#print(parse_source(source5))  # TODO implement compound expression





# ----------------------------------------------------------------------
# What's next?  If you've made it here are are looking for more,
# proceed to the file "func_models.py" and continue.














