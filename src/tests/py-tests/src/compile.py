import os 
import sys
import re

first = re.search("[a-zA-Z0-9]+[.]py", sys.argv[1]).group()
name = (re.search("[a-zA-Z0-9]+", first)).group()
pwd = os.getcwd()
os.system(f"python3 ~/Work/PRJ/py-compiler/src/Driver.py {sys.argv[1]} {sys.argv[2]}")

# os.system(f"clang src/lang_tests/{name}.ll -o src/lang_tests/{name}.o")
os.system(f"clang {sys.argv[2]}.ll -o {sys.argv[2]}")
