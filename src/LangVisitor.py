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


    # Visit a parse tree produced by LangParser#file.
    def visitFile(self, ctx:LangParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx:LangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:LangParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#print_stmt.
    def visitPrint_stmt(self, ctx:LangParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arithmetic_stmt.
    def visitArithmetic_stmt(self, ctx:LangParser.Arithmetic_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#boolean_stmt.
    def visitBoolean_stmt(self, ctx:LangParser.Boolean_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#num.
    def visitNum(self, ctx:LangParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#id.
    def visitId(self, ctx:LangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bool.
    def visitBool(self, ctx:LangParser.BoolContext):
        return self.visitChildren(ctx)



del LangParser