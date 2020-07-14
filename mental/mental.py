# mental.py
#
# In the Metal project, you wrote small machine language programs
# to carry out simple calculations.  You had to convert the
# calculations to operations on hardware such as "ADD", "SUB", and
# so forth.  These hardware operations involved registers.
#
# This exercise puts a slightly different spin on the whole affair.
# We'll start by abstracting the idea of a "hardware operation".
# Define these two functions:

def ADD(x, y, resultfunc):
    resultfunc(x+y)

def SUB(x, y, resultfunc):
    resultfunc(x-y)

# These functions carry out a calculation and send the result to
# another function.   For example:

ADD(2, 3, print)        # --> Prints 5

# -----------------------------------------------------------------------------
# Exercise 1:
#
# Show how you would calculate and print the final value of the following
# math expression using only the above functions and print.
#
#    2 + 3 - 4 - 5
#
# Hint: It's also ok to use lambda.

ADD(2, 3, lambda x: SUB(x, 4, lambda x: SUB(x, 5, print)))

# -----------------------------------------------------------------------------
# Exercise 2:
#
# Suppose the following function has been written to perform a comparison.

def CMP(x, y, resultfunc):
    resultfunc(x==y)

# Show how you could use ADD, SUB, CMP to implement
# multiplication.  You may additionally use lambda functions and
# conditional expressions (i.e., "val1 if test else val2").
# You may not use other Python features.

def MUL(x, y, resultfunc):
    ...
    # You implement using ADD, SUB, CMP only
    ...

MUL(3, 7, print)     # --> Should print 21

# -----------------------------------------------------------------------------
# Exercise 3
#
# Show how you can implement a factorial function.

def FACT(n, resultfunc):
    ...
    # Implement only using ADD, SUB, CMP, and MUL
    ...

FACT(5, print)       # --> Should print 120

