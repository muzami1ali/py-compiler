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

def getVarVal(var, symT, addrT, builder):
    var_val = var[0]
    var_type = var[1] 
    if var_type == "Var":
        var_typ = symT[var_val]
        param  = len(re.findall("Arg",var_typ))
        if param:
            return addrT[var]
        else:
            addr = addrT[var_val]
            return builder.load(addr)
    return var_val


def getVar(var, typ, symT, addrT, builder):
    if typ == "Var":
        var_typ = symT[var]
        param  = len(re.findall("Arg",var_typ))
        if param:
            typ = re.sub("Arg", "Val", var_typ)
            var = addrT[var]
        else:
            typ = re.sub("Var", "Val", var_typ)
            addr = addrT[var]
            var = builder.load(addr)
    return (var,typ)



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
        self.address_table = dict()
        self.func_table = dict()
        self.args_table = dict()
        
        # set up main function
        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="main")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.num = 0
        self.if_else = -1
        self.stack=[]
        
        self.while_stmt = 0

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
        #    RULE_ret_smt = 3
        num = ctx.getChildCount()
        for i in range(num):
            self.visit(ctx.getChild(i))
        return 0


    # Visit a parse tree produced by LangParser#exp.
    def visitExp(self, ctx:LangParser.ExpContext):
        if self.builder.block.is_terminated:
            raise SystemExit("ERROR: Unreachable code")
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
        return (ir.Constant(ir.DoubleType(), float(ctx.getText())), "DoubleVal")


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
         

    # Visit a parse tree produced by LangParser#type.
    def visitType(self, ctx:LangParser.TypeContext):
        typ = ctx.getText()
        match typ:
            case 'int':
                return ('IntArg', ir.IntType(32))
            case 'float':
                return ('DoubleArg', ir.DoubleType())
            case 'bool':
                return ('BoolArg', ir.IntType(1))


    # Visit a parse tree produced by LangParser#ret_type.
    def visitRet_type(self, ctx:LangParser.Ret_typeContext):
        typ = ctx.getText()
        match typ:
            case 'int':
                return (ir.IntType(32), typ, 'IntVal')
            case 'float':
                return (ir.DoubleType(), typ, 'DoubleVal')
            case 'bool':
                return (ir.IntType(1), typ, 'BoolVal')
            case 'None':
                return (ir.VoidType(), typ, 'NoneVal')


    # Visit a parse tree produced by LangParser#arg.
    def visitArg(self, ctx:LangParser.ArgContext):
        arg = self.visit(ctx.getChild(0))
        arg_name = arg[0]
        typ = self.visit(ctx.getChild(2))
        self.symbol_table[arg_name] = typ[0]
        return (arg_name, typ[0], typ[1])


    # Visit a parse tree produced by LangParser#args.
    def visitArgs(self, ctx:LangParser.ArgsContext):
        size = ctx.getChildCount()
        if size == 2:
            return ([],[],[])
        else:
            names = []
            typs = []
            irtyps = []
            for i in range(1,size,2):
                arg = self.visit(ctx.getChild(i))
                names.append(arg[0])
                typs.append(arg[1])
                irtyps.append(arg[2])
                return (names, typs, irtyps)



    def visitParam(self, ctx:LangParser.ParamContext):
        child = self.visit(ctx.getChild(0))
        if child[1] == "Var":
        # if(ctx.getChild(0).getRuleIndex()==6): #Var rule index is 4
            param = child[0]
            typ = self.symbol_table[param]
            arg =  len(re.findall("Arg",typ)) 
            if arg:
                param_type = re.sub("Arg", "Val", typ)
                param_value = self.address_table[param]
                return (param_value,param_type)
            else:
                param_type = re.sub("Var", "Val", typ)
                param_address = self.address_table[param]
                param_value = self.builder.load(param_address)
                return (param_value,param_type)
        else:
            return child

    # Visit a parse tree produced by LangParser#params.
    def visitParams(self, ctx:LangParser.ParamsContext):
        size = ctx.getChildCount()
        if size == 2:
            return ([], [])
        else:
            vals = []
            typs = []
            for i in range(1,size,2):
                arg = self.visit(ctx.getChild(i))
                vals.append(arg[0])
                typs.append(arg[1])
            return (vals,typs)


    # Visit a parse tree produced by LangParser#func_call.
    def visitFunc_call(self, ctx:LangParser.Func_callContext):
        func_name  = self.visit(ctx.getChild(0))[0]
        vals, typs = self.visit(ctx.getChild(1))
        if (func_name == "print"):
            # self.num = print_func(self.builder,self.num,func_param)
            # print_func(self.builder,self.num,func_param, self.symbol_table, self.address_table)
            print_func(self.builder,self.num,(vals[0],typs[0]))
            self.num = self.num + 1
        else:
            try:
                """
                    Need to add error handling in parameters
                    error handling in return statements
                    Scoping 
                """
                func = self.func_table[func_name]
                arg_typs = self.args_table[func_name]
                # print(func_param)
                return (self.builder.call(func[0],vals), func[1])
            except KeyError:
                raise SystemExit(f"ERROR:{func_name} has not been declared")
        return 0

    def visitAop_var(self, ctx:LangParser.Aop_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        aop  = self.visit(ctx.getChild(2))
        # aop_val = aop[0]
        # aop_typ = aop[1]
        aop_val, aop_typ = getVar(aop[0],aop[1],self.symbol_table,self.address_table,self.builder)
        # if aop_typ == "Var":
        #     var_addr = self.address_table[aop_val]
        #     typ = self.symbol_table[aop_val]
        #     val = self.builder.load(var_addr)
        #     return (var_name, val, typ)
        typ = re.sub("Val","Var",aop_typ)
        return (var_name,aop_val, typ)



    # Visit a parse tree produced by LangParser#int_var.
    def visitInt_var(self, ctx:LangParser.Int_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "IntVar")


    # Visit a parse tree produced by LangParser#float_var.
    def visitFloat_var(self, ctx:LangParser.Float_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        val  = self.visit(ctx.getChild(2))[0]
        return (var_name, val, "DoubleVar")


    # Visit a parse tree produced by LangParser#bool_var.
    def visitBool_var(self, ctx:LangParser.Bool_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        var  = self.visit(ctx.getChild(2))
        var_val, var_typ = getVar(var[0],var[1],self.symbol_table,self.address_table,self.builder)
        # var_val = var[0]
        # var_typ = var[1]
        # if var_typ == "Var":
        #     var_addr = self.address_table[var_val]
        #     typ = self.symbol_table[var_val]
        #     val = self.builder.load(var_addr)
        #     return (var_name, val, typ)

        # print(var)
        typ = re.sub("Val","Var",var_typ)
        return (var_name, var_val, typ)


    # Visit a parse tree produced by LangParser#var_decl.
    def visitVar_decl(self, ctx:LangParser.Var_declContext):
        var_info = self.visit(ctx.getChild(0))
        var_name = var_info[0]
        var_val = var_info[1]
        var_type = var_info[2]
        try: 
            var_old_typ = self.symbol_table[var_name]
            if (var_old_typ==var_type):
                var_addr = self.address_table[var_name]
                self.builder.store(var_val, var_addr)
            else: 
                raise SystemExit(f"ERROR:{var_name} changed from {var_old_typ} to {var_type} \n Details: \n {var_info}")
                # var_addr = self.builder.alloca(checkType(var_type), name=var_name)
                # self.builder.store(var_val, var_addr)
                # self.address_table[var_name] = var_addr
                # self.symbol_table[var_name] = var_type
        except KeyError:
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
        # print(size)
        for i in range(1,size-1):
            self.visit(ctx.getChild(i))


    def visitIf(self, ctx:LangParser.IfContext):
        size = len(self.stack)
        num = self.stack[size-1]
        # pred = self.visit(ctx.getChild(1))[0]
        pred = getVarVal(self.visit(ctx.getChild(1)), self.symbol_table, self.address_table, self.builder)
        addr = self.address_table[f"ifvar{num}"]
        if_block = self.builder.append_basic_block(f"if_block_{num}")
        endif_block = self.builder.append_basic_block(f"endif_block_{num}")
        self.builder.cbranch(pred,if_block,endif_block)
        self.builder.position_at_start(if_block)
        self.builder.store(false, addr)
        self.visit(ctx.getChild(2))
        if(not self.builder.block.is_terminated):
            self.builder.branch(endif_block)
        self.builder.position_at_start(endif_block)


    def visitElif(self, ctx:LangParser.ElifContext):
        size = len(self.stack)
        num = self.stack[size-1]
        bool_val = getVarVal(self.visit(ctx.getChild(1)), self.symbol_table, self.address_table, self.builder)
        addr = self.address_table[f"ifvar{num}"]
        if_val = self.builder.load(addr)
        pred = self.builder.and_(bool_val,if_val)
        elif_block = self.builder.append_basic_block(f"elif_block_{num}")
        end_elif_block = self.builder.append_basic_block(f"end_elif_block_{num}")
        self.builder.cbranch(pred,elif_block,end_elif_block)
        self.builder.position_at_start(elif_block)
        self.builder.store(false, addr)
        self.visit(ctx.getChild(2))
        if(not self.builder.block.is_terminated):
            self.builder.branch(end_elif_block)
        self.builder.position_at_start(end_elif_block)
        


    def visitElse(self, ctx:LangParser.ElseContext):
        size = len(self.stack)
        num = self.stack[size-1]
        addr = self.address_table[f"ifvar{num}"]
        pred = self.builder.load(addr)
        else_block = self.builder.append_basic_block(f"else_block_{num}")
        end_else_block = self.builder.append_basic_block(f"end_else_block_{num}")
        self.builder.cbranch(pred,else_block,end_else_block)
        self.builder.position_at_start(else_block)
        self.visit(ctx.getChild(2))
        if(not self.builder.block.is_terminated):
            self.builder.branch(end_else_block)
        self.builder.position_at_start(end_else_block)

    
    def visitIf_statement(self, ctx:LangParser.If_statementContext):
        
        self.if_else += 1
        self.stack.append(self.if_else)
        var_name= f"ifvar{self.if_else}"
        var_addr = self.builder.alloca( ir.IntType(1), name=var_name)
        self.builder.store(true, var_addr)
        self.address_table[var_name] = var_addr
        size = ctx.getChildCount()
        for i in range(size):
            self.visit(ctx.getChild(i))
        self.stack.pop()


        return 0


    def visitWhile_statement(self, ctx:LangParser.While_statementContext):
        size = ctx.getChildCount()
        num = self.while_stmt
        pred = getVarVal(self.visit(ctx.getChild(1)), self.symbol_table, self.address_table, self.builder)
        # pred = self.visit(ctx.getChild(1))[0]
        while_block = self.builder.append_basic_block(f"while_block_{num}")
        end_while_block = self.builder.append_basic_block(f"end_while_block_{num}")
        if (size > 3):
            while_else_block = self.builder.append_basic_block(f"while_else_block_{num}")
            end_while_else_block = self.builder.append_basic_block(f"end_while_else_block_{num}")
        self.builder.cbranch(pred,while_block,end_while_block)
        self.builder.position_at_start(while_block)
        self.visit(ctx.getChild(2))
        if(not self.builder.block.is_terminated):
            pred = getVarVal(self.visit(ctx.getChild(1)), self.symbol_table, self.address_table, self.builder)
            # pred = self.visit(ctx.getChild(1))[0]
            self.builder.cbranch(pred,while_block,end_while_block)
        self.builder.position_at_start(end_while_block)
        if(size > 3):
            self.builder.branch(while_else_block)
            self.builder.position_at_start(while_else_block)
            self.visit(ctx.getChild(5))
            if (not self.builder.block.is_terminated):
                self.builder.branch(end_while_else_block)
            self.builder.position_at_start(end_while_else_block)

        return 0

    # Visit a parse tree produced by LangParser#function.
    def visitFunction(self, ctx:LangParser.FunctionContext):
        old_builder = self.builder
        # old_num = self.num
        # old_if_else = self.if_else
        # old_stack = self.stack
        # old_while_stmt = self.while_stmt
        # self.num = 0
        # self.if_else = -1
        # self.stack=[]
        # self.while_stmt = 0
        old_symbol_table = self.symbol_table
        old_address_table = self.address_table
        self.symbol_table = dict()
        self.address_table = dict()
        func_name = self.visit(ctx.getChild(1))[0]
        names, typs, args = self.visit(ctx.getChild(2))
        return_type = self.visit(ctx.getChild(4))
        # print(func_name)
        print(return_type)
        func_ty = ir.FunctionType(return_type[0], args)
        func = ir.Function(self.module, func_ty, name=func_name)
        args = func.args
        for i in range(len(names)):
            name = names[i]
            arg = args[i]
            self.address_table[name] = arg
            arg.name = name
        # func.args = args
        print(args)
        self.func_table[func_name] = (func, return_type[2])
        self.args_table[func_name] = typs
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        # visit body
        self.visit(ctx.getChild(6))
        if(not self.builder.block.is_terminated):
            match return_type[1]:
                case 'None':
                    self.builder.ret_void()
                case 'int':
                     self.builder.ret(ir.Constant(ir.IntType(32), 0))
                case 'float':
                     self.builder.ret(ir.Constant(ir.DoubleType(), 0.0))
                case 'bool':
                     self.builder.ret(ir.Constant(ir.IntType(1), 0))
        # self.builder.block
        self.builder = old_builder
        self.symbol_table = old_symbol_table
        self.address_table = old_address_table
        # self.num = old_num
        # self.if_else = old_if_else
        # self.stack = old_stack
        # self.while_stmt = old_while_stmt
        
        return 0

    
    # Visit a parse tree produced by LangParser#ret_smt.
    def visitRet_smt(self, ctx:LangParser.Ret_smtContext):
        func_name = self.builder.function.name
        if func_name == "main":
            raise SystemExit("ERROR: Return statement not allowed outside function")
        self.builder.ret(self.visit(ctx.getChild(1))[0])


    #
    #
    # # Visit a parse tree produced by LangParser#main_func.
    # def visitMain_func(self, ctx:LangParser.Main_funcContext):
    #     return self.visitChildren(ctx)
    #



