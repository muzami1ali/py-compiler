import sys
from antlr4 import *
from LangLexer import LangLexer
from LangParser import LangParser
from IRGenerator import IRGenerator
import re

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        print(tree.toStringTree(recog=parser))
        if len(argv) != 2: # Calling Compile.py
            irGen = IRGenerator(argv[1], argv[2])
            irGen.visit(tree)
        else: # Directly calling driver.py
            moduleName = (re.search("[a-zA-Z0-9]+",argv[1])).group()
            irGen = IRGenerator(argv[1], moduleName)
            irGen.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
