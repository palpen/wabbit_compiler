#!/bin/bash

set -e

python3 run_llvm_tests.py
echo "LLVM program"
cat ./out.ll
clang ./wabbit/main.c ./wabbit/runtime.c ./out.ll
./a.out

