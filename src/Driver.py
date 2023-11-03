import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ListenerInterp import ListenerInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
    #    print(tree.toStringTree(recog=parser)) 
        linterp = ListenerInterp()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)

if __name__ == '__main__':
    main(sys.argv)

# import sys
# from antlr4 import *
# from ExprLexer import ExprLexer
# from ExprParser import ExprParser
# from ListenerInterp import ListenerInterp

# def main(argv):
#     input_stream = FileStream(argv[1])
#     lexer = ExprLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = ExprParser(stream)
#     tree = parser.start_()
#     if parser.getNumberOfSyntaxErrors() > 0:
#         print("syntax errors")
#     else:
#         linterp = ListenerInterp()
#         walker = ParseTreeWalker()
#         walker.walk(linterp, tree)

# if __name__ == '__main__':
#     main(sys.argv)