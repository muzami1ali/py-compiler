# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx:ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx:ExprParser.PrintContext):
        pass


    # Enter a parse tree produced by ExprParser#function.
    def enterFunction(self, ctx:ExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#function.
    def exitFunction(self, ctx:ExprParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#num.
    def enterNum(self, ctx:ExprParser.NumContext):
        pass

    # Exit a parse tree produced by ExprParser#num.
    def exitNum(self, ctx:ExprParser.NumContext):
        pass


    # Enter a parse tree produced by ExprParser#newl.
    def enterNewl(self, ctx:ExprParser.NewlContext):
        pass

    # Exit a parse tree produced by ExprParser#newl.
    def exitNewl(self, ctx:ExprParser.NewlContext):
        pass


    # Enter a parse tree produced by ExprParser#paren.
    def enterParen(self, ctx:ExprParser.ParenContext):
        pass

    # Exit a parse tree produced by ExprParser#paren.
    def exitParen(self, ctx:ExprParser.ParenContext):
        pass



del ExprParser