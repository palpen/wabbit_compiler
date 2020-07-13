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

class Integer(Expression):
    '''
    Example: 42
    '''
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Integer({self.value})'

class Float(Expression):
    '''
    Example: 1.0
    '''
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Float({self.value})'

class UnaryOp(Expression):
    '''
    Example: -4.0
    '''
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def __repr__(self):
        return f'UnaryOp({self.op}, {self.operand})'

class DeclareConst(Declaration):
    '''
    Example: const pi = 3.14159
    '''
    def __init__(self, name, vartype, value):
        assert isinstance(name, str)
        assert vartype is None or isinstance(vartype, str)
        assert isinstance(value, Expression)
        self.name = name
        self.value = value

    def __repr__(self):
        return f'DeclareConst({self.name}, {self.value})'

class DeclareVar(Declaration):
    '''
    Example: var name vartype
    '''
    def __init__(self, name, vartype, value):
        assert isinstance(name, str)
        assert vartype is None or isinstance(vartype, str)
        assert value is None or isinstance(value, Expression)
        self.name = name
        self.vartype = vartype
        self.value = value

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

class Load(Expression):
    '''
    Retrieves the value assigned to a variable
    '''
    def __init__(self, location):
        self.location = location
    def __repr__(self):
        return f'Load({self.location})'

class BinOp(Expression):
    '''
    Example: left + right
    '''
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f'BinOp({self.op}, {self.left}, {self.right})'

class Print(Statement):
    '''
    Example: print 1.0
    '''
    def __init__(self, expression):
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
        self.statements = statements

    def __repr__(self):
        return f'Statements({self.statements})'


# ------ Debugging function to convert a model into source code (for easier viewing)

def to_source(node):
    if isinstance(node, Integer):
        return node.value
    elif isinstance(node, Float):
        return node.value
    elif isinstance(node, UnaryOp):
        return f'{node.op}{to_source(node.operand)}'
    elif isinstance(node, DeclareConst):
        return f'const {node.name} = {to_source(node.value)};\n'
    elif isinstance(node, DeclareVar):
        return (f'var {node.name}' + \
            (f' {node.vartype}' if node.vartype else '') + \
            ((" = " + to_source(node.value)) if node.value else '') + \
            ";\n")
    elif isinstance(node, Assignment):
        return f'{node.location} = {to_source(node.value)};\n'
    elif isinstance(node, Load):
        return f'{node.location}'


    elif isinstance(node, BinOp):
        return f'{to_source(node.left)} {node.op} {to_source(node.right)}'
    elif isinstance(node, Print):
        return f'print {to_source(node.expression)};\n'
    elif isinstance(node, Statements):
        return ''.join([to_source(s) for s in node.statements])
    else:
        raise RuntimeError(f"Can't convert {node} to source")




