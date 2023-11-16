# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#prog.
    def visitProg(self, ctx:LangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#func.
    def visitFunc(self, ctx:LangParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#atom.
    def visitAtom(self, ctx:LangParser.AtomContext):
        return self.visitChildren(ctx)



del LangParser