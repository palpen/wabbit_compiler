# wabbit/llvm.py
#
# In this file you will have your compiler generate LLVM output.  Don't
# start this unless you have first worked through the LLVM Tutorial in
#
#     docs/LLVM-Tutorial.md
#
# Once you have done that, come back here.
#
# The overall strategy here is going to be very similar to how type
# checking works. Recall, in type checking, there was an environment
# and functions like this:
#
#    def check_expression(node, env):
#        ...
#
# It's going to be almost exactly the same idea here. Instead of an
# environment, define a class that represents an LLVM Module:
#
#    class LLVMModule:
#        ...
#
# This module will contain everything that's needed to output LLVM
# code. Build it from what you learned in the LLVM tutorial (i.e.,
# you'll have a function, an IRBuilder, a basic block, etc.).
#
# Write functions that accept the LLVM module as an argument.  For
# example:
#
#    def generate_expression(node, mod):
#       ...
#
# In these functions, you will produce code by interacting with the
# module in some way.
#
# One somewhat messy bit concerns the mapping of Wabbit types to
# LLVM types. You'll probably want to make some type objects to help.
# (see below)

from collections import ChainMap

from llvmlite import ir

from .model import *

# Define LLVM types corresponding to Wabbit types
int_type = ir.IntType(32)
float_type = ir.DoubleType()
void_type = ir.VoidType()

# The LLVM world that Wabbit is populating
class WabbitLLVMModule:
    def __init__(self):

        # Boilerplate code to setup llvlite to write LLVM code
        self.module = ir.Module("wabbit")
        self.function = ir.Function(self.module,
                                    ir.FunctionType(void_type, []),
                                    name='main_block')
        self.block = self.function.append_basic_block('entry')
        self.builder = ir.IRBuilder(self.block)

        # Runtime functions for printing. See wabbit/runtime.c.
        self._printi = ir.Function(
            self.module,
            ir.FunctionType(void_type, [int_type]),
            name='_printi')

        self._printf = ir.Function(
            self.module,
            ir.FunctionType(void_type, [float_type]),
            name='_printf')

        # Environment
        self.env = ChainMap()

    def gettype(self, node):
        return node.type

# Top-level function
def generate_program(model, write_out=False):
    mod = WabbitLLVMModule()
    code = g(model, mod)
    mod.builder.ret_void()  # closes the block in LLVM

    if write_out:
        with open('out.ll', 'w') as file:
            file.write(str(mod.module))
        print('Wrote out.ll')
    return mod.module

# Internal function to to generate code for each node type
def g(node, mod):
    if isinstance(node, list):
        for stmt in node:
            code = g(stmt, mod)
        return None

    elif isinstance(node, Integer):
        return ir.Constant(int_type, int(node.value))





    elif isinstance(node, UnaryOp):
#        node.op
#        node.operand
#        if node.type
#        if node.op == '-':






    elif isinstance(node, Print):
        node_type = mod.gettype(node.expression)
        value = g(node.expression, mod)
        if node_type == 'int':
            return mod.builder.call(mod._printi, [value])

    elif isinstance(node, BinOp):
        leftval = g(node.left, mod)
        rightval = g(node.right, mod)

        lefttype = mod.gettype(node.left)
        if lefttype in {'int'}:
            if node.op == '+':
                return mod.builder.add(leftval, rightval)
            if node.op == '-':
                return mod.builder.sub(leftval, rightval)
            if node.op == '*':
                return mod.builder.mul(leftval, rightval)
            if node.op == '/':
                return mod.builder.sdiv(leftval, rightval)


    else:
        raise RuntimeError(f"Can't generate code for {node}")

# Sample main program that runs the compiler
def main(filename):
    from .parse import parse_file
    from .typecheck import check_program

    model = parse_file(filename)
    check_program(model)
    mod = generate_program(model)
    with open('out.ll', 'w') as file:
        file.write(str(mod))
    print('Wrote out.ll')

if __name__ == '__main__':
    import sys
    main(sys.argv[1])

