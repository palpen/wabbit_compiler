# tokenizer.py
#
# The role of a tokenizer is to turn raw text into recognized symbols
# known as tokens.
#
# The following set of tokens are defined for "WabbitScript".  Later
# parts of the project require you to add more tokens.  The suggested
# name of the token is on the left. The matching text is on the right.
#
# Reserved Keywords:
#x     CONST   : 'const'
#x     VAR     : 'var'
#x     PRINT   : 'print'
#x     BREAK   : 'break'
#x     CONTINUE: 'continue'
#x     IF      : 'if'
#x     ELSE    : 'else'
#x     WHILE   : 'while'
#x     TRUE    : 'true'
#x     FALSE   : 'false'
#
# Identifiers/Names
#     NAME    : Text starting with a letter or '_', followed by any number
#               number of letters, digits, or underscores.
#               Examples:  'abc' 'ABC' 'abc123' '_abc' 'a_b_c'
#
# Literals:
#x     INTEGER :  123   (decimal)
#
#x     FLOAT   : 1.234
#               .1234
#               1234.
#
#     CHAR    : 'a'     (a single character - byte)
#               '\xhh'  (byte value)
#               '\n'    (newline)
#               '\''    (literal single quote)
#
# Operators:
#x     PLUS     : '+'
#x     MINUS    : '-'
#x     TIMES    : '*'
#x     DIVIDE   : '/'
#x     LT       : '<'
#x     LE       : '<='
#x     GT       : '>'
#x     GE       : '>='
#x     EQ       : '=='
#x     NE       : '!='
#x     LAND     : '&&'
#x     LOR      : '||'
#x     LNOT     : '!'
#
# Miscellaneous Symbols
#x     ASSIGN   : '='
#x     SEMI     : ';'
#x     LPAREN   : '('
#x     RPAREN   : ')'
#x     LBRACE   : '{'
#x     RBRACE   : '}'
#
# Comments:  To be ignored
#      //             Skips the rest of the line
#      /* ... */      Skips a block (no nesting allowed)
#
# Errors: Your lexer may optionally recognize and report the following
# error messages:
#
#      lineno: Illegal char 'c'
#      lineno: Unterminated character constant
#      lineno: Unterminated comment
#
# ----------------------------------------------------------------------

from sly import Lexer

# High level function that takes input source text and turns it into tokens.
# This is a natural place to use some kind of generator function.


class Tokenizer(Lexer):
    tokens = {
        PLUS, MINUS, TIMES, DIVIDE, LT, LE, GT, GE, EQ, NE,
        LAND, LOR, LNOT, ASSIGN, SEMI, LPAREN, RPAREN, LBRACE, RBRACE,
        NAME, CONST, VAR, PRINT, BREAK, CONTINUE, TRUE, FALSE, IF, ELSE,
        WHILE, FLOAT, INTEGER, NEWLINE
    }
    ignore = ' \t'

    # tokens as regex
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LT = r'<'
    LE = r'<='
    GT = r'>'
    GE = r'>='
    EQ = r'='
    NE = r'!='
    LAND = r'&&'
    LOR = r'\|\|'
    LNOT = r'!'
    ASSIGN = r'='
    SEMI   = r';'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'{'
    RBRACE = r'}'
    NAME = r'[a-zA-Z][a-zA-Z0-9]*'
    NAME['const'] = CONST
    NAME['var'] = VAR
    NAME['print'] = PRINT
    NAME['break'] = BREAK
    NAME['continue'] = CONTINUE
    NAME['true'] = TRUE
    NAME['false'] = FALSE
    NAME['if'] = IF  # special cases of NAME
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    FLOAT = r'\d+\.\d*'
    INTEGER = r'\d+'
    NEWLINE = r'\n'


def tokenize(text):
    lexer = Tokenizer()
    for tok in lexer.tokenize(text):
        yield tok

# Main program to test on input files
def main(filename):
    with open(filename) as file:
        text = file.read()

    for tok in tokenize(text):
        print(tok)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])







