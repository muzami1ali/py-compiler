import sys
from antlr4 import *
from LangParser import LangParser
from LangVisitor import LangVisitor
from llvmlite import ir
import llvmlite.binding as llvm
from util import printf, print_func
from arithmetic import *
from boolean import *
import re

true = ir.Constant(ir.IntType(1), 1)
false = ir.Constant(ir.IntType(1), 0)

def checkType(ty): 
    match ty:
        case "IntVar":
            return ir.IntType(32)
        case "FloatVar":
            return ir.FloatType()
        case "DoubleVar":
            return ir.DoubleType()
        case "BoolVar":
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
        self.if_else = 0
        self.elif_num = 0

        self.module.triple = "arm64-apple-macosx14.0.0"

    # Visit a parse tree produced by LangParser#prog.
    def visitProg(self, ctx:LangParser.ProgContext):
        self.visit(ctx.getChild(1))
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        f = open(f"{self.dir}.ll", "w")
        f.write(str(self.module))
        f.close()

        # print(self.address_table)
        # print(self.symbol_table)
        # print(self.module.functions)
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
            return (false, "BoolVal")
        else:
            return (true, "BoolVal")



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
            return aop(op,lhs,rhs,self.builder, self.symbol_table,self.address_table)


    # Visit a parse tree produced by LangParser#aop2.
    def visitAop2(self, ctx:LangParser.Aop2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return aop(op,lhs,rhs,self.builder, self.symbol_table,self.address_table)



    # Visit a parse tree produced by LangParser#aop1.
    def visitAop1(self, ctx:LangParser.Aop1Context):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by LangParser#b_op.
    def visitB_op(self, ctx:LangParser.B_opContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 2:
            # Satisfying the not condition
            res = self.visit(ctx.getChild(1))
            return bop_not(self.builder,res,self.symbol_table,self.address_table)
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return bop(op,lhs,rhs,self.builder, self.symbol_table,self.address_table)
         

    def visitParam(self, ctx:LangParser.ParamContext):
        if(ctx.getChild(0).getRuleIndex()==4): #Var rule index is 4
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
        if (func_name == "print"):
            # self.num = print_func(self.builder,self.num,func_param)
            print_func(self.builder,self.num,func_param)
            self.num = self.num + 1
        return 0

    def visitAop_var(self, ctx:LangParser.Aop_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        aop  = self.visit(ctx.getChild(2))
        aop_val = aop[0]
        aop_typ = aop[1]
        typ = re.sub("Val","Var",aop_typ)
        return (var_name,aop_val,typ)



    # Visit a parse tree produced by LangParser#int_var.
    def visitInt_var(self, ctx:LangParser.Int_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "IntVar")


    # Visit a parse tree produced by LangParser#float_var.
    def visitFloat_var(self, ctx:LangParser.Float_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "FloatVar")


    # Visit a parse tree produced by LangParser#bool_var.
    def visitBool_var(self, ctx:LangParser.Bool_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "BoolVar")


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


    def visitIf_param(self, ctx:LangParser.If_paramContext):
        size = ctx.getChildCount()
        if (size==2):
            return self.visit(ctx.getChild(0))
        elif (size==4):
            return self.visit(ctx.getChild(1))


    def visitExp_block(self, ctx:LangParser.Exp_blockContext):
        size = ctx.getChildCount()
        for i in range(1,size-1):
            self.visit(ctx.getChild(i))


    def visitIf(self, ctx:LangParser.IfContext):
        num = self.if_else
        pred = self.visit(ctx.getChild(1))[0]
        addr = self.address_table[f"ifvar{num}"]
        if_block = self.builder.append_basic_block(f"if_block_{num}")
        endif_block = self.builder.append_basic_block(f"endif_block_{num}")
        self.builder.cbranch(pred,if_block,endif_block)
        self.builder.position_at_start(if_block)
        self.visit(ctx.getChild(2))
        self.builder.store(false, addr)
        self.builder.branch(endif_block)
        self.builder.position_at_start(endif_block)


    def visitElif(self, ctx:LangParser.ElifContext):
        num = f"{self.if_else}{self.elif_num}"
        pred = self.visit(ctx.getChild(1))[0]
        addr = self.address_table[f"ifvar{self.if_else}"]
        elif_block = self.builder.append_basic_block(f"elif_block_{num}")
        end_elif_block = self.builder.append_basic_block(f"end_elif_block_{num}")
        self.builder.cbranch(pred,elif_block,end_elif_block)
        self.builder.position_at_start(elif_block)
        self.visit(ctx.getChild(2))
        self.builder.store(false, addr)
        self.builder.branch(end_elif_block)
        self.builder.position_at_start(end_elif_block)
        
        self.elif_num += 1



    def visitElse(self, ctx:LangParser.ElseContext):
        num = self.if_else
        addr = self.address_table[f"ifvar{num}"]
        pred = self.builder.load(addr)
        else_block = self.builder.append_basic_block(f"else_block_{num}")
        end_else_block = self.builder.append_basic_block(f"end_else_block_{num}")
        self.builder.cbranch(pred,else_block,end_else_block)
        self.builder.position_at_start(else_block)
        self.visit(ctx.getChild(2))
        self.builder.branch(end_else_block)
        self.builder.position_at_start(end_else_block)

    
    def visitIf_statement(self, ctx:LangParser.If_statementContext):
        
        var_name= f"ifvar{self.if_else}"
        var_addr = self.builder.alloca( ir.IntType(1), name=var_name)
        self.builder.store(true, var_addr)
        self.address_table[var_name] = var_addr
        size = ctx.getChildCount()
        for i in range(size):
            self.visit(ctx.getChild(i))
        self.elif_num = 0
        self.if_else += 1

            

        return 0

    # # Visit a parse tree produced by LangParser#function.
    # def visitFunction(self, ctx:LangParser.FunctionContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by LangParser#main_func.
    # def visitMain_func(self, ctx:LangParser.Main_funcContext):
    #     return self.visitChildren(ctx)
    #



