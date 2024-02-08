# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#newl_ignore.
    def enterNewl_ignore(self, ctx:LangParser.Newl_ignoreContext):
        pass

    # Exit a parse tree produced by LangParser#newl_ignore.
    def exitNewl_ignore(self, ctx:LangParser.Newl_ignoreContext):
        pass


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


    # Enter a parse tree produced by LangParser#exp.
    def enterExp(self, ctx:LangParser.ExpContext):
        pass

    # Exit a parse tree produced by LangParser#exp.
    def exitExp(self, ctx:LangParser.ExpContext):
        pass


    # Enter a parse tree produced by LangParser#var.
    def enterVar(self, ctx:LangParser.VarContext):
        pass

    # Exit a parse tree produced by LangParser#var.
    def exitVar(self, ctx:LangParser.VarContext):
        pass


    # Enter a parse tree produced by LangParser#int.
    def enterInt(self, ctx:LangParser.IntContext):
        pass

    # Exit a parse tree produced by LangParser#int.
    def exitInt(self, ctx:LangParser.IntContext):
        pass


    # Enter a parse tree produced by LangParser#float.
    def enterFloat(self, ctx:LangParser.FloatContext):
        pass

    # Exit a parse tree produced by LangParser#float.
    def exitFloat(self, ctx:LangParser.FloatContext):
        pass


    # Enter a parse tree produced by LangParser#bool.
    def enterBool(self, ctx:LangParser.BoolContext):
        pass

    # Exit a parse tree produced by LangParser#bool.
    def exitBool(self, ctx:LangParser.BoolContext):
        pass


    # Enter a parse tree produced by LangParser#a_op.
    def enterA_op(self, ctx:LangParser.A_opContext):
        pass

    # Exit a parse tree produced by LangParser#a_op.
    def exitA_op(self, ctx:LangParser.A_opContext):
        pass


    # Enter a parse tree produced by LangParser#aop3.
    def enterAop3(self, ctx:LangParser.Aop3Context):
        pass

    # Exit a parse tree produced by LangParser#aop3.
    def exitAop3(self, ctx:LangParser.Aop3Context):
        pass


    # Enter a parse tree produced by LangParser#aop2.
    def enterAop2(self, ctx:LangParser.Aop2Context):
        pass

    # Exit a parse tree produced by LangParser#aop2.
    def exitAop2(self, ctx:LangParser.Aop2Context):
        pass


    # Enter a parse tree produced by LangParser#aop1.
    def enterAop1(self, ctx:LangParser.Aop1Context):
        pass

    # Exit a parse tree produced by LangParser#aop1.
    def exitAop1(self, ctx:LangParser.Aop1Context):
        pass


    # Enter a parse tree produced by LangParser#b_op.
    def enterB_op(self, ctx:LangParser.B_opContext):
        pass

    # Exit a parse tree produced by LangParser#b_op.
    def exitB_op(self, ctx:LangParser.B_opContext):
        pass


    # Enter a parse tree produced by LangParser#param.
    def enterParam(self, ctx:LangParser.ParamContext):
        pass

    # Exit a parse tree produced by LangParser#param.
    def exitParam(self, ctx:LangParser.ParamContext):
        pass


    # Enter a parse tree produced by LangParser#params.
    def enterParams(self, ctx:LangParser.ParamsContext):
        pass

    # Exit a parse tree produced by LangParser#params.
    def exitParams(self, ctx:LangParser.ParamsContext):
        pass


    # Enter a parse tree produced by LangParser#func_call.
    def enterFunc_call(self, ctx:LangParser.Func_callContext):
        pass

    # Exit a parse tree produced by LangParser#func_call.
    def exitFunc_call(self, ctx:LangParser.Func_callContext):
        pass


    # Enter a parse tree produced by LangParser#aop_var.
    def enterAop_var(self, ctx:LangParser.Aop_varContext):
        pass

    # Exit a parse tree produced by LangParser#aop_var.
    def exitAop_var(self, ctx:LangParser.Aop_varContext):
        pass


    # Enter a parse tree produced by LangParser#int_var.
    def enterInt_var(self, ctx:LangParser.Int_varContext):
        pass

    # Exit a parse tree produced by LangParser#int_var.
    def exitInt_var(self, ctx:LangParser.Int_varContext):
        pass


    # Enter a parse tree produced by LangParser#float_var.
    def enterFloat_var(self, ctx:LangParser.Float_varContext):
        pass

    # Exit a parse tree produced by LangParser#float_var.
    def exitFloat_var(self, ctx:LangParser.Float_varContext):
        pass


    # Enter a parse tree produced by LangParser#bool_var.
    def enterBool_var(self, ctx:LangParser.Bool_varContext):
        pass

    # Exit a parse tree produced by LangParser#bool_var.
    def exitBool_var(self, ctx:LangParser.Bool_varContext):
        pass


    # Enter a parse tree produced by LangParser#var_decl.
    def enterVar_decl(self, ctx:LangParser.Var_declContext):
        pass

    # Exit a parse tree produced by LangParser#var_decl.
    def exitVar_decl(self, ctx:LangParser.Var_declContext):
        pass


    # Enter a parse tree produced by LangParser#function.
    def enterFunction(self, ctx:LangParser.FunctionContext):
        pass

    # Exit a parse tree produced by LangParser#function.
    def exitFunction(self, ctx:LangParser.FunctionContext):
        pass


    # Enter a parse tree produced by LangParser#main_func.
    def enterMain_func(self, ctx:LangParser.Main_funcContext):
        pass

    # Exit a parse tree produced by LangParser#main_func.
    def exitMain_func(self, ctx:LangParser.Main_funcContext):
        pass


    # Enter a parse tree produced by LangParser#indent.
    def enterIndent(self, ctx:LangParser.IndentContext):
        pass

    # Exit a parse tree produced by LangParser#indent.
    def exitIndent(self, ctx:LangParser.IndentContext):
        pass


    # Enter a parse tree produced by LangParser#block_end.
    def enterBlock_end(self, ctx:LangParser.Block_endContext):
        pass

    # Exit a parse tree produced by LangParser#block_end.
    def exitBlock_end(self, ctx:LangParser.Block_endContext):
        pass


    # Enter a parse tree produced by LangParser#block_stmt.
    def enterBlock_stmt(self, ctx:LangParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#block_stmt.
    def exitBlock_stmt(self, ctx:LangParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#block_middle.
    def enterBlock_middle(self, ctx:LangParser.Block_middleContext):
        pass

    # Exit a parse tree produced by LangParser#block_middle.
    def exitBlock_middle(self, ctx:LangParser.Block_middleContext):
        pass


    # Enter a parse tree produced by LangParser#exp_block.
    def enterExp_block(self, ctx:LangParser.Exp_blockContext):
        pass

    # Exit a parse tree produced by LangParser#exp_block.
    def exitExp_block(self, ctx:LangParser.Exp_blockContext):
        pass


    # Enter a parse tree produced by LangParser#if_param.
    def enterIf_param(self, ctx:LangParser.If_paramContext):
        pass

    # Exit a parse tree produced by LangParser#if_param.
    def exitIf_param(self, ctx:LangParser.If_paramContext):
        pass


    # Enter a parse tree produced by LangParser#if.
    def enterIf(self, ctx:LangParser.IfContext):
        pass

    # Exit a parse tree produced by LangParser#if.
    def exitIf(self, ctx:LangParser.IfContext):
        pass


    # Enter a parse tree produced by LangParser#elif.
    def enterElif(self, ctx:LangParser.ElifContext):
        pass

    # Exit a parse tree produced by LangParser#elif.
    def exitElif(self, ctx:LangParser.ElifContext):
        pass


    # Enter a parse tree produced by LangParser#else.
    def enterElse(self, ctx:LangParser.ElseContext):
        pass

    # Exit a parse tree produced by LangParser#else.
    def exitElse(self, ctx:LangParser.ElseContext):
        pass


    # Enter a parse tree produced by LangParser#if_statement.
    def enterIf_statement(self, ctx:LangParser.If_statementContext):
        pass

    # Exit a parse tree produced by LangParser#if_statement.
    def exitIf_statement(self, ctx:LangParser.If_statementContext):
        pass



del LangParser