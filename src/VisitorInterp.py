import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from llvmlite import ir
import llvmlite.binding as llvm
from util import printf

class VisitorInterp(ExprVisitor):
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target = llvm.Target.from_default_triple()
        self.module = ir.Module(name="calc")
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="op")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.symbol_table = {}
        self.func = None
        self.module.triple = target

        func3 = ir.Function(self.module,ir.FunctionType(ir.IntType(32), []),name="main")
        block3 = func3.append_basic_block(name="entry")
        builder3 = ir.IRBuilder(block3)
        res = builder3.call(func,[],"result")
        printf(builder3,"%d",res)
        builder3.ret(ir.Constant(ir.IntType(32),0))

    def visitAtom(self, ctx: ExprParser.AtomContext):
        return ir.Constant(ir.IntType(32), int(ctx.getText()))

    def visitFunc(self, ctx: ExprParser.FuncContext):
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
    
    def visitProg(self, ctx: ExprParser.ProgContext):

        # print(ctx.getChild(0).getText())
        # print(self.visit(ctx.getChild(0)))

        self.builder.ret(self.visit(ctx.getChild(0)))

        f = open("calc.ll", "w")
        f.write(str(self.module))
        f.close()

        f = open("calc.ll", "r")
        print(f.read())

        return 0
        return super().visitProg(ctx)


