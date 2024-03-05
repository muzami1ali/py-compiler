import os 
import sys
import re

name = (re.search("[a-zA-Z0-9]+", sys.argv[1])).group()
pwd = os.getcwd()
os.system(f"python ~/Work/PRJ/py-compiler/src/Driver.py {pwd}/{sys.argv[1]} {pwd}/{name}")

print("-----Runtime Output-----")
os.system(f"lli {name}.ll")
