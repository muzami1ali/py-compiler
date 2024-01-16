import sys
from antlr4 import *
from LangParser import LangParser
from LangVisitor import LangVisitor
from llvmlite import ir
import llvmlite.binding as llvm
from util import printf
import re

class IRGenerator(LangVisitor):
    def __init__(self, fileName, filePath):
        # Set up module
        self.dir = filePath
        first = re.search("[a-zA-Z0-9]+[.]py", fileName).group()
        self.moduleName = (re.search("[a-zA-Z0-9]+",first)).group()
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target = llvm.Target.from_default_triple()
        self.module = ir.Module(name=self.moduleName)

        # set up main function
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="op")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.module.triple = target

        # func2 = ir.Function(self.module, func_ty, name="main")
        # block2 = func2.append_basic_block(name="entry")
        # builder2 = ir.IRBuilder(block2)
        # res = builder2.call(func,[],"result")
        # #
        # printf(builder2,"%d\n",res)
        # #
        # builder2.ret(ir.Constant(ir.IntType(32),0))

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
        try:
            return ir.Constant(ir.IntType(32), int(ctx.getText()))
        except:
            return ir.Constant(ir.FloatType(32), float(ctx.getText()))


    # Visit a parse tree produced by LangParser#id.
    def visitId(self, ctx:LangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bool.
    def visitBool(self, ctx:LangParser.BoolContext):
        return self.visitChildren(ctx)

