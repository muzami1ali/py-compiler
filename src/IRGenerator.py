import sys
from antlr4 import *
from LangParser import LangParser
from LangVisitor import LangVisitor
from llvmlite import ir
import llvmlite.binding as llvm
from util import printf, print_func
from ListStruct import *
from arithmetic import *
from boolean import *
import re

true = ir.Constant(ir.IntType(1), 1)
false = ir.Constant(ir.IntType(1), 0)

# Check the type of the variable and return the corresponding ir type
def checkType(ty): 
    match ty:
        case "IntVar":
            return ir.IntType(32)
        # case "FloatVar":
        #     return ir.FloatType()
        case "DoubleVar":
            return ir.DoubleType()
        case "BoolVar":
            return ir.IntType(1)
        case "ListVar":
            return list_struct

# If typ is Var, get the value of the variable or argument and return var_val
# else just return var_val
def getVarVal(var, symT, addrT, builder):
    var_val = var[0]
    var_type = var[1] 
    if var_type == "Var":
        try: 
            var_typ = symT[var_val]
        except KeyError:
            raise SystemExit(f"GetVarVAl-->ERROR:{var_val} has not been declared")
        param  = len(re.findall("Arg",var_typ))
        if param:
            return addrT[var]
        else:
            addr = addrT[var_val]
            return builder.load(addr)
    return var_val

# Similar to getVarVal, but returns the variable value and its type
def getVar(var, typ, symT, addrT, builder):
    if typ == "Var":
        try: 
            var_typ = symT[var]
        except KeyError:
            raise SystemExit(f"GetVar-->ERROR:{var} has not been declared")
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
        first = re.search("[a-zA-Z0-9_-]+[.]py", fileName).group()
        self.moduleName = (re.search("[a-zA-Z0-9_-]+",first)).group()
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

        self.entry_block = block 
        self.instr = None # instr is used to keep track of the last allocate instruction
        self.num = 0 # num is used to keep track of print statements
        self.if_else = -1 # if_else is used to keep track of if-else blocks
        self.stack=[] # stack is used to keep track of if statements as they are nested
        
        self.while_stmt = 0 # while_stmt is used to keep track of while statements

        # self.module.triple = "arm64-apple-macosx14.0.0"


    # Visit a parse tree produced by LangParser#prog.
    # This is the starting point of the program
    # Writes the generated IR to a file
    def visitProg(self, ctx:LangParser.ProgContext):
        self.visit(ctx.getChild(1))
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        f = open(f"{self.dir}.ll", "w")
        f.write(str(self.module))
        f.close()

        # print(str(self.module))
        # return 0


    # Visit all the children of the file
    def visitFile(self, ctx:LangParser.FileContext):
        #    RULE_ret_smt = 3
        num = ctx.getChildCount()
        for i in range(num):
            self.visit(ctx.getChild(i))
        # return 0


    # Visit a parse tree produced by LangParser#exp.
    # Visit the first child of the expression
    def visitExp(self, ctx:LangParser.ExpContext):
        if self.builder.block.is_terminated:
            raise SystemExit("ERROR: Unreachable code")
        self.visit(ctx.getChild(0)) 
        # return 0


    # Visit a parse tree produced by LangParser#var.
    # Get the variable name and return it
    def visitVar(self, ctx:LangParser.VarContext):
        return (ctx.getText(), "Var")


    # Visit a parse tree produced by LangParser#int.
    # Get the integer value and return it as a 32 bit integer constant
    def visitInt(self, ctx:LangParser.IntContext):
        return (ir.Constant(ir.IntType(32), int(ctx.getText())), "IntVal")


    # Visit a parse tree produced by LangParser#float.
    # Get the float value and return it as a double constant
    def visitFloat(self, ctx:LangParser.FloatContext):
        return (ir.Constant(ir.DoubleType(), float(ctx.getText())), "DoubleVal")


    # Visit a parse tree produced by LangParser#bool.
    # Get the boolean value and return it as a 1 bit integer constant
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
        val = self.visit(ctx.getChild(0))
        return getVar(val[0],val[1],self.symbol_table,self.address_table,self.builder)
        # return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by LangParser#b_op.
    def visitB_op(self, ctx:LangParser.B_opContext):
        if ctx.getChildCount() == 1:
            val = self.visit(ctx.getChild(0))
            return getVar(val[0],val[1],self.symbol_table,self.address_table,self.builder)
            # return self.visit(ctx.getChild(0))
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
    # Get the tyoe of an argument and return the corresponding ir type
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
    # Get the return type of a function and return the corresponding ir type
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
    # Get the argument name and type and store it in the symbol table
    # Return the argument name , type and ir type
    def visitArg(self, ctx:LangParser.ArgContext):
        arg = self.visit(ctx.getChild(0))
        arg_name = arg[0]
        typ = self.visit(ctx.getChild(2))
        self.symbol_table[arg_name] = typ[0]
        return (arg_name, typ[0], typ[1])


    # Visit a parse tree produced by LangParser#args.
    # Get the arguments of a function and return their names, types and ir types
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



    # Visit a parse tree produced by LangParser#param.
    # Get the parameter value and type and return it
    def visitParam(self, ctx:LangParser.ParamContext):
        child = self.visit(ctx.getChild(0))
        if child[1] == "Var":
        # if(ctx.getChild(0).getRuleIndex()==6): #Var rule index is 4
            param = child[0]
            try:
                typ = self.symbol_table[param]
            except KeyError:
                raise SystemExit(f"Param-->ERROR:{param} has not been declared")
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
    # Get the parameters of a function call and return their values and types
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
    # Get the function name and parameters of a function call
    # If the function is print, call the print function
    # Else, call the function and return the value
    def visitFunc_call(self, ctx:LangParser.Func_callContext):
        func_name  = self.visit(ctx.getChild(0))[0]
        vals, typs = self.visit(ctx.getChild(1))
        if (func_name == "print"):
            if re.search("List",typs[0]):
                raise SystemExit(f"PrintFunc-->ERROR: No List support currently")
            elif typs[0] == "StrVal":
                printf(self.builder,vals[0] + '\n',self.num)
            elif typs[0] == "FstrVal":
                val = vals[0]
                str_literal = val[0]
                args_val = val[1]
                args_typ = val[2]
                matches = re.findall(r"\{\w*\}",str_literal)
                # print(matches)
                # match_len = len(matches)
                # args_len = len(args_val)
                if (len(matches) != len(args_val)):
                    raise SystemExit(f"PrintFunc-->ERROR: Number of arguments in string does not match number of arguments passed")
                if len(matches) == 0:
                    raise SystemExit(f"PrintFunc-->ERROR: No arguments found in string")
                else:
                    for t in args_typ:
                        match t:
                            case "IntVal":
                                str_literal = re.sub("\{\w*\}", "%d",str_literal,1)
                            case "DoubleVal":
                                str_literal = re.sub("\{\w*\}", "%f",str_literal,1)
                            case "BoolVal":
                                raise SystemExit(f"PrintFunc-->ERROR: No support for bool in string format")
                    printf(self.builder,str_literal + '\n',self.num,*args_val)

            else: 
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
                return (self.builder.call(func[0],vals), func[1])
            except KeyError:
                raise SystemExit(f"FuncCall-->ERROR:{func_name} has not been declared")
        return 0

    def visitAop_var(self, ctx:LangParser.Aop_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        aop  = self.visit(ctx.getChild(2))
        aop_val, typ = getVar(aop[0],aop[1],self.symbol_table,self.address_table,self.builder)
        # typ = re.sub("Val","Var",typ)
        return (var_name,aop_val, typ)


    # Visit a parse tree produced by LangParser#list_var.
    def visitList_var(self, ctx:LangParser.List_varContext):
        var_name = self.visit(ctx.getChild(0))[0]
        # val  = self.visit(ctx.getChild(2))[0]
        val = self.visit(ctx.getChild(2))
        return (var_name, val, "ListVar")

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
        var_val, typ = getVar(var[0],var[1],self.symbol_table,self.address_table,self.builder)
        # typ = re.sub("Val","Var",typ)
        return (var_name, var_val, typ)


    # Visit a parse tree produced by LangParser#var_decl.
    def visitVar_decl(self, ctx:LangParser.Var_declContext):
        var_info = self.visit(ctx.getChild(0))
        var_name = var_info[0]
        var_val = var_info[1]
        var_type = var_info[2]
        var_typ = re.sub("Val","Var",var_type)
        try: 
            var_old_typ = self.symbol_table[var_name]
            if var_typ == "ListVar":
                raise SystemExit(f"VarDecl-->ERROR: No List support currently")
            if (var_old_typ==var_typ):
                var_addr = self.address_table[var_name]
                self.builder.store(var_val, var_addr)
            else: 
                raise SystemExit(f"VarDecl-->ERROR:{var_name} changed from {var_old_typ} to {var_typ} \n Details: \n {var_info}")
                # var_addr = self.builder.alloca(checkType(var_type), name=var_name)
                # self.builder.store(var_val, var_addr)
                # self.address_table[var_name] = var_addr
                # self.symbol_table[var_name] = var_type
        except KeyError:
            """
                Variable are allocated in the entry block
                in order that they are ready to be used
                when the program starts, the value is stored
                by moving to current block and storing the value
            """
            current_block = self.builder.block
            if self.instr == None:
                self.builder.position_at_start(self.entry_block)
            else:
                self.builder.position_after(self.instr)
            var_addr = self.builder.alloca(checkType(var_typ), name=var_name)
            self.instr = var_addr
            self.builder.position_at_end(current_block)
            if var_typ == "ListVar":
                self.builder.call(create_list(self.module), [var_addr])
                match var_val[1]:
                    case "IntList":
                        self.symbol_table[var_name] = "IntList"
                        func = append_int_list(self.module)
                        int_lst = var_val[0]
                        for val in int_lst:
                            self.builder.call(func, [var_addr, val[0]])
                    case "DoubleList":
                        self.symbol_table[var_name] = "DoubleList"
                        func = append_double_list(self.module)
                        double_lst = var_val[0]
                        for val in double_lst:
                            self.builder.call(func, [var_addr, val[0]])
                    case "ListVar":
                        self.symbol_table[var_name] = "ListVar"

            else:
                self.builder.store(var_val, var_addr)
                self.symbol_table[var_name] = var_typ
            self.address_table[var_name] = var_addr
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
        current_block = self.builder.block
        if self.instr == None:
            self.builder.position_at_start(self.entry_block)
        else:
            self.builder.position_after(self.instr)
        var_addr = self.builder.alloca( ir.IntType(1), name=var_name)
        self.instr = var_addr
        self.builder.position_at_end(current_block)
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
        old_entry_block = self.entry_block
        old_instr = self.instr
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
        func_ty = ir.FunctionType(return_type[0], args)
        func = ir.Function(self.module, func_ty, name=func_name)
        args = func.args
        for i in range(len(names)):
            name = names[i]
            arg = args[i]
            self.address_table[name] = arg
            arg.name = name
        self.func_table[func_name] = (func, return_type[2])
        self.args_table[func_name] = typs
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.entry_block = block
        self.instr = None
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
        self.entry_block = old_entry_block
        self.instr = old_instr
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
        func_return_type = self.func_table[func_name][1]
        if func_name == "main":
            raise SystemExit("RetStmt-->ERROR: Return statement not allowed outside function")
        ret = self.visit(ctx.getChild(1))
        ret_val, ret_typ = getVar(ret[0],ret[1],self.symbol_table,self.address_table,self.builder)
        if ret_typ != func_return_type:
            raise SystemExit(f"RetStmt-->ERROR: Return type {ret_typ} does not match function return type {func_return_type}")
        self.builder.ret(ret_val)


    # Visit a parse tree produced by LangParser#list.
    def visitList(self, ctx:LangParser.ListContext):
        size  = ctx.getChildCount()
        if size == 2:
            return ([], "ListVar")
        else:
            vals = []
            for i in range(1,size,2):
                val = self.visit(ctx.getChild(i))
                if i==1:
                    lst_typ = val[1]
                else:
                    if val[1] != lst_typ:
                        raise SystemExit(f"visitList-->ERROR: List elements must be of same type")
                vals.append(val)
            return (vals, re.sub("Val","List",lst_typ))


    # Visit a parse tree produced by LangParser#list_get.
    def visitList_get(self, ctx:LangParser.List_getContext):
        lst_name = self.visit(ctx.getChild(0))[0]
        val = self.visit(ctx.getChild(2))
        if val[1] != "IntVal":
            raise SystemExit(f"visitListGet-->ERROR: List index must be an integer")
        try:
            lst_addr = self.address_table[lst_name]
            lst_typ = self.symbol_table[lst_name]
            if lst_typ == "ListVar":
                raise SystemExit(f"visitListGet-->ERROR: {lst_name} is empty")
            match lst_typ:
                case "IntList":
                    get_func =  get_int_list_element(self.module)
                case "DoubleList":
                    get_func = get_double_list_element(self.module)
            val_typ =re.sub("List","Val",lst_typ)
            return (self.builder.call(get_func, [lst_addr, val[0]]), val_typ)
        except KeyError:
            raise SystemExit(f"visitListGet-->ERROR:{lst_name} has not been declared")



    # Visit a parse tree produced by LangParser#list_set.
    def visitList_set(self, ctx:LangParser.List_setContext):
        lst_name = self.visit(ctx.getChild(0))[0]
        index = self.visit(ctx.getChild(2))
        val = self.visit(ctx.getChild(5))
        if index[1] != "IntVal":
            raise SystemExit(f"visitListSet-->ERROR: List index must be an integer")
        try:
            lst_addr = self.address_table[lst_name]
            lst_typ = self.symbol_table[lst_name]
            if lst_typ == "ListVar":
                raise SystemExit(f"visitListSet-->ERROR: {lst_name} is empty")
            match lst_typ:
                case "IntList":
                    if val[1] != "IntVal":
                        raise SystemExit(f"visitListSet-->ERROR: List elements must be of same type")
                    set_func = set_int_list_element(self.module)
                case "DoubleList":
                    if val[1] != "DoubleVal":
                        raise SystemExit(f"visitListSet-->ERROR: List elements must be of same type")
                    set_func = set_double_list_element(self.module)
            self.builder.call(set_func, [lst_addr, index[0], val[0]])
        except KeyError:
            raise SystemExit(f"visitListSet-->ERROR:{lst_name} has not been declared")


    # Visit a parse tree produced by LangParser#list_append.
    def visitList_append(self, ctx:LangParser.List_appendContext):
        lst_name = self.visit(ctx.getChild(0))[0]
        val = self.visit(ctx.getChild(3))
        try:
            lst_addr = self.address_table[lst_name]
            lst_typ = self.symbol_table[lst_name]
            val_typ = val[1]
            if lst_typ == "ListVar":
                match val_typ:
                    case "IntVal":
                        self.symbol_table[lst_name] = "IntList"
                        append_func = append_int_list(self.module)
                    case "DoubleVal":
                        self.symbol_table[lst_name] = "DoubleList"
                        append_func = append_double_list(self.module)
            else:
                match lst_typ:
                    case "IntList":
                        if val_typ != "IntVal":
                            raise SystemExit(f"visitListAppend-->ERROR: List elements must be of same type")
                        append_func = append_int_list(self.module)
                    case "DoubleList":
                        if val_typ != "DoubleVal":
                            raise SystemExit(f"visitListAppend-->ERROR: List elements must be of same type")
                        append_func = append_double_list(self.module)
            self.builder.call(append_func, [lst_addr, val[0]])
        except KeyError:
            raise SystemExit(f"visitListAppend-->ERROR :{lst_name} has not been declared")
        
    # Visit a parse tree produced by LangParser#len_func.
    def visitLen_func(self, ctx:LangParser.Len_funcContext):
        list_name = self.visit(ctx.getChild(2))[0]
        try:
            lst_addr = self.address_table[list_name]
            lst_typ = self.symbol_table[list_name]
            if lst_typ == "ListVar":
                raise SystemExit(f"LenFunc-->ERROR: {list_name} is empty")
            # lst_typm must contain List
            if re.search("List",lst_typ):
                func = get_list_length(self.module)
                return (self.builder.call(func, [lst_addr]), "IntVal")
            else:
                raise SystemExit(f"LenFunc-->ERROR: {list_name} is not a list")

        except KeyError:
            raise SystemExit(f"LenFunc-->ERROR:{list_name} has not been declared")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#str_literal.
    def visitStr_literal(self, ctx:LangParser.Str_literalContext):
        str_val = ctx.getText()
        str_typ = "StrVal"
        str_val = str_val[1:]
        str_val = str_val[:-1]
        return (str_val, str_typ)

    # Visit a parse tree produced by LangParser#str.
    def visitStr(self, ctx:LangParser.StrContext):
        str_literal = self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 1:
            return (str_literal[0], "StrVal")
        else :
            args = self.visit(ctx.getChild(1))
            return ((str_literal[0], args[0], args[1]), "FstrVal")
        


    # Visit a parse tree produced by LangParser#format.
    def visitFormat(self, ctx:LangParser.FormatContext):
        if ctx.getChildCount() == 4:
            child = self.visit(ctx.getChild(3))
            val = child[0]
            typ = child[1]
            return ([val], [typ])
        else:
            size  = ctx.getChildCount()
            val_lst = []
            typ_lst = []
            for i in range(3,size,2):
                child = self.visit(ctx.getChild(i))
                val = child[0]
                typ = child[1]
                val_lst.append(val)
                typ_lst.append(typ)
            return (val_lst, typ_lst)



    #
    #
    # # Visit a parse tree produced by LangParser#main_func.
    # def visitMain_func(self, ctx:LangParser.Main_funcContext):
    #     return self.visitChildren(ctx)
    #



