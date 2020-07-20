# parse.py
#
# Wabbit parser.  The parser needs to construct the data model or an
# abstract syntax tree from text input.  The grammar shown here represents
# WabbitScript--a subset of the full Wabbit language.  It's written as
# a EBNF.  You will need to expand the grammar to include later features.
#
# Reference: docs/WabbitScript.md
#
# The following conventions are used:
#
#       ALLCAPS       --> A token
#       { symbols }   --> Zero or more repetitions of symbols
#       [ symbols ]   --> Zero or one occurences of symbols (optional)
#       s | t         --> Either s or t (a choice)
#
#
# statements : { statement }
#
# statement : print_statement
#           | assignment_statement
#           | variable_definition
#           | const_definition
#           | if_statement
#           | while_statement
#           | break_statement
#           | continue_statement
#           | expr
#
# print_statement : PRINT expr SEMI
#
# assignment_statement : location ASSIGN expr SEMI
#
# variable_definition : VAR NAME [ type ] ASSIGN expr SEMI
#                     | VAR NAME type [ ASSIGN expr ] SEMI
#
# const_definition : CONST NAME [ type ] ASSIGN expr SEMI
#
# if_statement : IF expr LBRACE statements RBRACE [ ELSE LBRACE statements RBRACE ]
#
# while_statement : WHILE expr LBRACE statements RBRACE
#
# break_statement : BREAK SEMI
#
# continue_statement : CONTINUE SEMI
#
# expr : expr PLUS expr        (+)
#      | expr MINUS expr       (-)
#      | expr TIMES expr       (*)
#      | expr DIVIDE expr      (/)
#      | expr LT expr          (<)
#      | expr LE expr          (<=)
#      | expr GT expr          (>)
#      | expr GE expr          (>=)
#      | expr EQ expr          (==)
#      | expr NE expr          (!=)
#      | expr LAND expr        (&&)
#      | expr LOR expr         (||)
#      | PLUS expr
#      | MINUS expr
#      | LNOT expr              (!)
#      | LPAREN expr RPAREN
#      | location
#      | literal
#      | LBRACE statements RBRACE
#
# literal : INTEGER
#         | FLOAT
#         | CHAR
#         | TRUE
#         | FALSE
#         | LPAREN RPAREN
#
# location : NAME
#
# type      : NAME
#
# empty     :
# ======================================================================

# How to proceed:
#
# At first glance, writing a parser might look daunting. The key is to
# take it in tiny pieces.  Focus on one specific part of the language.
# For example, the print statement.  Start with something really basic
# like printing literals:
#
#     print 1;
#     print 2.5;
#
# From there, expand it to handle expressions:
#
#     print 2 + 3 * -4;
#
# Then, expand it to include variable names
#
#     var x = 3;
#     print 2 + x;
#
# Keep on expanding to more and more features of the language.  A good
# trajectory is to follow the programs found in the top level
# script_models.py file.  That is, write a parser that can recognize the
# source code for each part and build the corresponding model.  You
# will find yourself filling in pieces here throughout the project.
# It's ok to work piecemeal.
#
# Usage of tools:
#
# If you are highly motivated and want to know how a parser works at a
# low-level, you can write a hand-written recursive descent parser.
# It is also fine to use high-level tools such as
#
#    - SLY (https://github.com/dabeaz/sly),
#    - PLY (https://github.com/dabeaz/ply),
#    - ANTLR (https://www.antlr.org).

from sly import Parser
from .model import *
from .tokenize import *


class WabbitParser(Parser):
#    debugfile = 'parser.out'

    # Get list of tokens from tokenizer
    tokens = Tokenizer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('print_statement',
       'assignment_statement',
       'const_declare_statement',
       'var_declare_statement',
       'if_statement',
       'expr_statement')
    def statement(self, p):
        return p[0]

    @_('PRINT expr SEMI')
    def print_statement(self, p):
        return Print(p.expr)

    @_('expr SEMI')
    def expr_statement(self, p):
        return ExprAsStatement(p.expr)

    @_('location ASSIGN expr SEMI')
    def assignment_statement(self, p):
        return Assignment(p.location, p.expr)

    @_('VAR NAME ASSIGN expr SEMI')
    def var_declare_statement(self, p):
        return DeclareVar(p.NAME, None, p.expr)

    @_('VAR NAME typ SEMI')
    def var_declare_statement(self, p):
        return DeclareVar(p.NAME, p.typ.name, None)

    @_('VAR NAME typ ASSIGN expr SEMI')
    def var_declare_statement(self, p):
        type_name = p.typ.name
        return DeclareVar(p.NAME, type_name, p.expr)

    @_('CONST NAME ASSIGN expr SEMI')
    def const_declare_statement(self, p):
        return DeclareConst(p.NAME, None, p.expr)

    @_('CONST NAME typ ASSIGN expr SEMI')
    def const_declare_statement(self, p):
        return DeclareConst(p.NAME, p.typ.name, p.expr)

    @_('IF expr LBRACE statements RBRACE')
    def if_statement(self, p):
        return IfStatement(p[1], p.statements, None)

    @_('IF expr LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
    def if_statement(self, p):
        return IfStatement(p[1], p[3], p[7])

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr LT expr',
       'expr LE expr',
       'expr GT expr',
       'expr GE expr',
       'expr EQ expr',
       'expr NE expr',
       'expr LAND expr',
       'expr LOR expr')
    def expr(self, p):
        return BinOp(p[1], p.expr0, p.expr1)

    @_('MINUS expr',
       'PLUS expr')
    def expr(self, p):
        return UnaryOp(p[0], p.expr)

    @_('location')
    def expr(self, p):
        return p.location

    # !!! What is this ?
    # Required, otherwise above methods results in infinite recursion
    @_('literal')
    def expr(self, p):
        return p.literal

    @_('NAME')
    def literal(self, p):
        return Load(p.NAME)

    @_('INTEGER')
    def literal(self,p):
        # p have attributes from the names in the decorator
        # e.g.  'INTEGER in @_('INTEGER')
        return Integer(p.INTEGER)

    @_('FLOAT')
    def literal(self, p):
        return Float(p.FLOAT)

    @_('NAME')
    def location(self, p):
        return p.NAME

    @_('TYP')
    def typ(self, p):
        return Type(p[0])


# Top-level function that runs everything
def parse_source(text):
    tokens = tokenize(text)

    # !!! DEBUG (will consume generator and cause an error)
#    for tok in tokens:
#        print(tok)
    parser = WabbitParser()
    return parser.parse(tokens)

def parse_file(filename):
    with open(filename) as file:
        text = file.read()
    return parse_source(text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit('Usage: wabbit.parse filename')
    model = parse_file(sys.argv[1])
    print(model)


