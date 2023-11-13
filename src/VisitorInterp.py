import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from llvmlite import ir

class VisitorInterp(ExprVisitor):
    def __init__(self):
        self.module = ir.Module(name="calc")
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="main")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.symbol_table = {}
        self.func = None

    def visitAtom(self, ctx: ExprParser.AtomContext):
        return ir.Constant(ir.IntType(32), int(ctx.getText()))

    def visitOp(self, ctx: ExprParser.OpContext):
        return ctx.getText()
    
    def visitFunc(self, ctx: ExprParser.FuncContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            op = self.visit(ctx.getChild(1))
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


