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
        self.dir = filePath
        first = re.search("[a-zA-Z0-9]+[.]py", fileName).group()
        self.moduleName = (re.search("[a-zA-Z0-9]+",first)).group()
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target = llvm.Target.from_default_triple()
        self.module = ir.Module(name=self.moduleName)
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="op")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.module.triple = target

        func3 = ir.Function(self.module, func_ty, name="main")
        block3 = func3.append_basic_block(name="entry")
        builder3 = ir.IRBuilder(block3)
        res = builder3.call(func,[],"result")
        #
        printf(builder3,"%d\n",res)
        #
        builder3.ret(ir.Constant(ir.IntType(32),0))

    def visitAtom(self, ctx: LangParser.AtomContext):
        return ir.Constant(ir.IntType(32), int(ctx.getText()))

    def visitFunc(self, ctx: LangParser.FuncContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))

            match op:
                case "+":
                    return self.builder.add(lhs,rhs)
                case "-":
                    return self.builder.sub(lhs,rhs)
                case "/":
                    return self.builder.udiv(lhs,rhs)
                case "*":
                    return self.builder.mul(lhs,rhs)
    
    def visitProg(self, ctx: LangParser.ProgContext):

        self.builder.ret(self.visit(ctx.getChild(0)))

        # f = open(f"src/lang_tests/{self.moduleName}.ll", "w")
        f = open(f"{self.dir}.ll", "w")
        f.write(str(self.module))
        f.close()

        # f = open(f"{self.moduleName}.ll", "r")
        # print(f.read())

        return 0


