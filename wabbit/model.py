# model.py
#
# This file defines the data model for Wabbit programs.  The data
# model is a data structure that represents the contents of a program
# as objects, not text.  Sometimes this structure is known as an
# "abstract syntax tree" or AST.  However, the model is not
# necessarily directly tied to the actual syntax of the language.  So,
# we'll prefer to think of it as a more generic data model instead.
#
# To do this, you need to identify the different "elements" that make
# up a program and encode them into classes.  To do this, it may be
# useful to slightly "underthink" the problem. To illustrate, suppose
# you wanted to encode the idea of "assigning a value."  Assignment
# involves a location (the left hand side) and a value like this:
#
#         location = expression;
#
# To represent this idea, make a class with just those parts:
#
#     class Assignment:
#         def __init__(self, location, expression):
#             self.location = location
#             self.expression = expression
#
# What are "location" and "expression"?  Does it matter? Maybe
# not. All you know is that an assignment operator definitely requires
# both of those parts.  DON'T OVERTHINK IT.  Further details will be
# filled in as the project evolves.
#
# Work on this file in conjunction with the top-level
# "script_models.py" file.  Go look at that file and see what program
# samples are provided.  Then, figure out what those programs look like
# in terms of data structures.
#
# There is no "right" solution to this part of the project other than
# the fact that a program has to be represented as some kind of data
# structure that's not "text."   You could use classes. You could use
# tuples. You could make a bunch of nested dictionaries like JSON.
# The key point: it must be a data structure.
#
# Starting out, I'd advise against making this file too fancy. Just
# use basic data structures. You can add usability enhancements later.
# -----------------------------------------------------------------------------

# The following classes are used for the expression example in script_models.py.
# Feel free to modify as appropriate.  You don't even have to use classes
# if you want to go in a different direction with it.

from typing import List

VALID_TYPES = {
    'int',
    'float',
    'char',
    'bool',
    'unit'
}

class Statement:
    '''
    Any syntactic entity that may be evaluated to determine its value
    Example:
        3 + 2
        4.0
    '''
    pass

class Expression:
    '''
    Any syntactic entity with no value
    Example:
        print "hello"
        x = 1
        var myint int
    '''
    pass

class Declaration(Statement):
    '''
    Used to define new names, e.g const pi = 3.14159
    '''
    pass

class BinOp(Expression):
    '''
    Example: left + right
    '''
    def __init__(self, op, left, right):
        assert isinstance(op, str)
        assert isinstance(left, Expression)
        assert isinstance(right, Expression)
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f'BinOp({self.op}, {self.left}, {self.right})'

class Integer(Expression):
    '''
    Example: 42
    '''
    def __init__(self, value):
        assert isinstance(value, str)
        self.value = value
        self.type = 'int'

    def __repr__(self):
        return f'Integer({self.value})'

class Float(Expression):
    '''
    Example: 1.0
    '''
    def __init__(self, value):
        assert isinstance(value, str)
        self.value = value
        self.type = 'float'

    def __repr__(self):
        return f'Float({self.value})'

class UnaryOp(Expression):
    '''
    Example: -4.0
    '''
    def __init__(self, op, operand):
        assert isinstance(op, str)
        assert isinstance(operand, Expression)
        self.op = op
        self.operand = operand

    def __repr__(self):
        return f'UnaryOp({self.op}, {self.operand})'

class DeclareConst(Declaration):
    '''
    Example: const pi = 3.14159
    '''
    def __init__(self, name, type, value):
        assert isinstance(name, str)
        assert type is None or isinstance(type, str)
        assert isinstance(value, Expression)
        self.name = name
        self.type = type
        self.value = value

    def __repr__(self):
        if self.type and self.value:
            return f'DeclareConst({self.name}, {self.type}, {self.value})'
        elif not self.type:
            return f'DeclareConst({self.name}, {self.value})'

class DeclareVar(Declaration):
    '''
    Example: var name type
    '''
    def __init__(self, name, type, value):
        assert isinstance(name, str)
        assert type is None or isinstance(type, str)
        assert value is None or isinstance(value, Expression)
        self.name = name
        self.type = type
        self.value = value

    def __repr__(self):
        if self.type and self.value:
            return f'DeclareVar({self.name}, {self.type}, {self.value})'
        elif not self.type:
            return f'DeclareVar({self.name}, {self.value})'
        elif not self.value:
            return f'DeclareVar({self.name}, {self.type})'

class Assignment(Statement):
    '''
    Example:
        tau = 2.0 * pi
    '''
    def __init__(self, location, value):
        assert isinstance(location, str)
        assert isinstance(value, Expression)
        self.location = location
        self.value = value
    def __repr__(self):
        return f'Assignment({self.location},{self.value})'

class Type:
    def __init__(self, name):
        assert isinstance(name, str)
        assert name in VALID_TYPES
        self.name = name
    def __repr__(self):
        return f'Type({self.name})'

class Load(Expression):
    '''
    Retrieves the value assigned to a variable
    '''
    def __init__(self, location):
        assert isinstance(location, str)
        self.location = location
    def __repr__(self):
        return f'Load({self.location})'

class IfStatement(Statement):
    '''
    Example:
        if condition {
            consequence
        } else {
            alternative
        }
    '''
    def __init__(self, condition, consequence, alternative):
        assert isinstance(condition, Expression)
        assert isinstance(consequence, List)
        assert alternative is None or isinstance(alternative, List)
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __repr__(self):
        return f'IfStatement({self.condition},{self.consequence},{self.alternative})'

class WhileLoop(Statement):
    '''
    Example:
        while condition {
            body
        }
    '''
    def __init__(self, condition, body):
        assert isinstance(condition, Expression)
        assert isinstance(body, Statement) or isinstance(body, Statements)
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f'WhileLoop({self.condition},{self.body})'

class Compound(Expression):
    '''
    Example:
        x = {var t = y; y = x; t; };
    '''
    def __init__(self, statements):
        assert isinstance(statements, Statements)
        self.statements = statements
    def __repr__(self):
        return f'Compound({self.statements})'

class ExprAsStatement(Statement):
    '''
    Used to deal with cases where an expression
    is used as a statement

    Example:
        # The t in the compound expression in
        x = {var t = y; y = x; t; };
    '''
    def __init__(self, expression):
        assert isinstance(expression, Expression)
        self.expression = expression
    def __repr__(self):
        return f'ExprAsStatement({self.expression})'

class Print(Statement):
    '''
    Example: print 1.0
    '''
    def __init__(self, expression):
        assert isinstance(expression, Expression)
        self.expression = expression
    def __repr__(self):
        return f'Print({self.expression})'

class Statements:
    '''
    Example:
        print 1;
        print "hello";
    '''
    def __init__(self, statements):
        assert all(isinstance(s, Statement) for s in statements)
        self.statements = statements
    def __repr__(self):
        return f'Statements({self.statements})'


# ------ Debugging function to convert a model into source code (for easier viewing)

def to_source(node, num_indent=0, curr_indent=0):

    # !!! BUG
    indent_sz = curr_indent*num_indent*'____'

    if isinstance(node, BinOp):
        return indent_sz + \
               f'{to_source(node.left)} {node.op} {to_source(node.right)}'

    elif isinstance(node, Integer):
        return node.value

    elif isinstance(node, Float):
        return node.value

    elif isinstance(node, UnaryOp):
        return f'{node.op}{to_source(node.operand)}'

    elif isinstance(node, DeclareConst):
        return indent_sz + \
               f'const {node.name} = {to_source(node.value)};\n'

    elif isinstance(node, DeclareVar):
        return indent_sz + (f'var {node.name}' + \
            (f' {node.type}' if node.type else '') + \
            ((" = " + to_source(node.value)) if node.value else '') + \
            ";\n")

    elif isinstance(node, Assignment):
        return indent_sz + \
               f'{node.location} = {to_source(node.value)};\n'

    elif isinstance(node, Load):
        return f'{node.location}'

    elif isinstance(node, IfStatement):
        return f'if {to_source(node.condition)}' + ' {\n' + \
               f'    {to_source(node.consequence)}' + \
               '} else {\n' + \
               f'    {to_source(node.alternative)}' + \
               '}'



    elif isinstance(node, WhileLoop):
        return indent_sz + \
               f'while {to_source(node.condition)}' + ' {\n' + \
               f'{to_source(node.body, num_indent=1, curr_indent=1)}' + \
               '}'



    elif isinstance(node, Compound):
        return '{ ' + \
               ''.join([to_source(s).rstrip() for s in node.statements.statements])  + ' }'

    elif isinstance(node, ExprAsStatement):
        return f'{to_source(node.expression)};'

    elif isinstance(node, Print):
        return indent_sz + \
               f'print {to_source(node.expression)};\n'

    elif isinstance(node, Statements):
        return ''.join([to_source(s, num_indent=num_indent, curr_indent=curr_indent) for s in node.statements])

    elif isinstance(node, List):
        # This is for cases where the node is a list of statements
        # !!! FIX Super hacky bandaid solution
        return ''.join([to_source(s, num_indent=num_indent, curr_indent=curr_indent) for s in node])

    else:
        raise RuntimeError(f"Can't convert {node} to source")

