import os 
import sys
import re

name = (re.search("[a-zA-Z0-9]+", sys.argv[1])).group()
pwd = os.getcwd()
os.system(f"python ../Driver.py {pwd}/{sys.argv[1]} {pwd}/{name}")

os.system(f"clang {name}.ll -o {name}.o")