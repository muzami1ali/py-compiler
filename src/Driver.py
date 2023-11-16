import sys
from antlr4 import *
from LangLexer import LangLexer
from LangParser import LangParser
from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
