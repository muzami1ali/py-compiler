import sys
from antlr4 import *
from LangParser import LangParser
from LangVisitor import LangVisitor
from llvmlite import ir
import llvmlite.binding as llvm
from util import printf
from arithmetic import *
import re
def checkType(ty): 
    match ty:
        case "Int":
            return ir.IntType(32)
        case "Float":
            return ir.FloatType()
        case _:
            return ir.IntType(1)

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

        self.symbol_table = dict()
        self.func_table = dict()
        self.address_table = dict()
        
        # set up main function
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="main")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.num = 0

        self.module.triple = "arm64-apple-macosx14.0.0"

    # Visit a parse tree produced by LangParser#prog.
    def visitProg(self, ctx:LangParser.ProgContext):
        self.visit(ctx.getChild(0))
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        f = open(f"{self.dir}.ll", "w")
        f.write(str(self.module))
        f.close()

        print(self.address_table)
        print(self.symbol_table)
        print(self.module.functions)
        print(str(self.module))
        return 0


    # Visit a parse tree produced by LangParser#file.
    def visitFile(self, ctx:LangParser.FileContext):
        num = ctx.getChildCount()
        for i in range(num):
            self.visit(ctx.getChild(i))
            
        return 0


    # Visit a parse tree produced by LangParser#exp.
    def visitExp(self, ctx:LangParser.ExpContext):
        self.visit(ctx.getChild(0)) 
        return 0


    # Visit a parse tree produced by LangParser#var.
    def visitVar(self, ctx:LangParser.VarContext):
        return (ctx.getText(), "Var")


    # Visit a parse tree produced by LangParser#int.
    def visitInt(self, ctx:LangParser.IntContext):
        return (ir.Constant(ir.IntType(32), int(ctx.getText())), "IntVal")


    # Visit a parse tree produced by LangParser#float.
    def visitFloat(self, ctx:LangParser.FloatContext):
        return (ir.Constant(ir.FloatType(), float(ctx.getText())), "FloatVal")


    # Visit a parse tree produced by LangParser#bool.
    def visitBool(self, ctx:LangParser.BoolContext):
        bool_val = ctx.getText()
        if (bool_val == "False"):   
            return ir.Constant(ir.IntType(1), 0)
        else:
            return ir.Constant(ir.IntType(1), 1)



    # Visit a parse tree produced by LangParser#a_op.
    def visitA_op(self, ctx:LangParser.A_opContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return aop(op,lhs,rhs,self.builder, self.symbol_table,self.address_table)


    # Visit a parse tree produced by LangParser#aop3.
    def visitAop3(self, ctx:LangParser.Aop3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))

            match op:
                case "/":
                    return self.builder.udiv(lhs,rhs)
                case "*":
                    return self.builder.mul(lhs,rhs)
                case "%":
                    return self.builder.urem(lhs,rhs)
                # case "//":
                #     return self.builder.mul(lhs,rhs)

    # Visit a parse tree produced by LangParser#aop2.
    def visitAop2(self, ctx:LangParser.Aop2Context):
        return self.visit(ctx.getChild(0))
        


    # Visit a parse tree produced by LangParser#aop1.
    def visitAop1(self, ctx:LangParser.Aop1Context):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by LangParser#b_op.
    def visitB_op(self, ctx:LangParser.B_opContext):
        return self.visitChildren(ctx)

    def visitParam(self, ctx:LangParser.ParamContext):
        if(ctx.getChild(0).getRuleIndex()==3):
            param = (self.visit(ctx.getChild(0)))[0]
            param_type = self.symbol_table[param]
            return (self.address_table[param],param_type)

        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by LangParser#params.
    def visitParams(self, ctx:LangParser.ParamsContext):
        size = ctx.getChildCount()
        if size == 2:
            return []
        else:
            lst = []
            for i in range(1,size,2):
                lst.append(self.visit(ctx.getChild(i)))
                return lst


    # Visit a parse tree produced by LangParser#func_call.
    def visitFunc_call(self, ctx:LangParser.Func_callContext):
        func_name  = self.visit(ctx.getChild(0))[0]
        func_param = self.visit(ctx.getChild(1))
        print(func_param[0])
        if (func_name == "print"):
            i = func_param[0]
            typ = i[1]
            if typ=="Int":
                res = self.builder.load(i[0])
                printf(self.builder, "%d\n", self.num, res)
                self.num += 1
            elif typ=="Float":
                res = self.builder.load(i[0])
                res1 = self.builder.fpext(res, ir.DoubleType())
                printf(self.builder, "%f\n", self.num, res1)
                self.num += 1
            elif typ=="IntVal":
                printf(self.builder, "%d\n", self.num, i[0])
                self.num += 1
            elif typ=="FloatVal":
                res = self.builder.fpext(i[0], ir.DoubleType())
                printf(self.builder, "%f\n", self.num, res)
                self.num += 1
        return 0


    # Visit a parse tree produced by LangParser#int_var.
    def visitInt_var(self, ctx:LangParser.Int_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "Int")


    # Visit a parse tree produced by LangParser#float_var.
    def visitFloat_var(self, ctx:LangParser.Float_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "Float")


    # Visit a parse tree produced by LangParser#bool_var.
    def visitBool_var(self, ctx:LangParser.Bool_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))
        return (var_name, val, "Bool")


    # Visit a parse tree produced by LangParser#var_decl.
    def visitVar_decl(self, ctx:LangParser.Var_declContext):
        var_info = self.visit(ctx.getChild(0))
        var_name = var_info[0]
        var_val = var_info[1]
        var_type = var_info[2]
        var_addr = self.builder.alloca(checkType(var_type), name=var_name)
        self.builder.store(var_val, var_addr)
        self.address_table[var_name] = var_addr
        self.symbol_table[var_name] = var_type
        return 0


    # Visit a parse tree produced by LangParser#function.
    def visitFunction(self, ctx:LangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#main_func.
    def visitMain_func(self, ctx:LangParser.Main_funcContext):
        return self.visitChildren(ctx)




