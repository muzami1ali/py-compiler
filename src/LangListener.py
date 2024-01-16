# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#prog.
    def enterProg(self, ctx:LangParser.ProgContext):
        pass

    # Exit a parse tree produced by LangParser#prog.
    def exitProg(self, ctx:LangParser.ProgContext):
        pass


    # Enter a parse tree produced by LangParser#file.
    def enterFile(self, ctx:LangParser.FileContext):
        pass

    # Exit a parse tree produced by LangParser#file.
    def exitFile(self, ctx:LangParser.FileContext):
        pass


    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx:LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx:LangParser.StatementContext):
        pass


    # Enter a parse tree produced by LangParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:LangParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:LangParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#print_stmt.
    def enterPrint_stmt(self, ctx:LangParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#print_stmt.
    def exitPrint_stmt(self, ctx:LangParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#arithmetic_stmt.
    def enterArithmetic_stmt(self, ctx:LangParser.Arithmetic_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#arithmetic_stmt.
    def exitArithmetic_stmt(self, ctx:LangParser.Arithmetic_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#boolean_stmt.
    def enterBoolean_stmt(self, ctx:LangParser.Boolean_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#boolean_stmt.
    def exitBoolean_stmt(self, ctx:LangParser.Boolean_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#num.
    def enterNum(self, ctx:LangParser.NumContext):
        pass

    # Exit a parse tree produced by LangParser#num.
    def exitNum(self, ctx:LangParser.NumContext):
        pass


    # Enter a parse tree produced by LangParser#id.
    def enterId(self, ctx:LangParser.IdContext):
        pass

    # Exit a parse tree produced by LangParser#id.
    def exitId(self, ctx:LangParser.IdContext):
        pass


    # Enter a parse tree produced by LangParser#bool.
    def enterBool(self, ctx:LangParser.BoolContext):
        pass

    # Exit a parse tree produced by LangParser#bool.
    def exitBool(self, ctx:LangParser.BoolContext):
        pass



del LangParser
