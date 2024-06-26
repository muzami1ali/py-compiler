# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#prog.
    def visitProg(self, ctx:LangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#file.
    def visitFile(self, ctx:LangParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#function.
    def visitFunction(self, ctx:LangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ret_smt.
    def visitRet_smt(self, ctx:LangParser.Ret_smtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#exp_block.
    def visitExp_block(self, ctx:LangParser.Exp_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#exp.
    def visitExp(self, ctx:LangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#exp_stmt.
    def visitExp_stmt(self, ctx:LangParser.Exp_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#stmt.
    def visitStmt(self, ctx:LangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#len_func.
    def visitLen_func(self, ctx:LangParser.Len_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#list.
    def visitList(self, ctx:LangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#type.
    def visitType(self, ctx:LangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ret_type.
    def visitRet_type(self, ctx:LangParser.Ret_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#format.
    def visitFormat(self, ctx:LangParser.FormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#str_literal.
    def visitStr_literal(self, ctx:LangParser.Str_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#str.
    def visitStr(self, ctx:LangParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#var.
    def visitVar(self, ctx:LangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#int.
    def visitInt(self, ctx:LangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#float.
    def visitFloat(self, ctx:LangParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bool.
    def visitBool(self, ctx:LangParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#list_get.
    def visitList_get(self, ctx:LangParser.List_getContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#list_set.
    def visitList_set(self, ctx:LangParser.List_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#list_append.
    def visitList_append(self, ctx:LangParser.List_appendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#a_op.
    def visitA_op(self, ctx:LangParser.A_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#aop3.
    def visitAop3(self, ctx:LangParser.Aop3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#aop2.
    def visitAop2(self, ctx:LangParser.Aop2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#aop1.
    def visitAop1(self, ctx:LangParser.Aop1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#b_op.
    def visitB_op(self, ctx:LangParser.B_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#func_call.
    def visitFunc_call(self, ctx:LangParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arg.
    def visitArg(self, ctx:LangParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#args.
    def visitArgs(self, ctx:LangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#param.
    def visitParam(self, ctx:LangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#params.
    def visitParams(self, ctx:LangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#list_var.
    def visitList_var(self, ctx:LangParser.List_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#aop_var.
    def visitAop_var(self, ctx:LangParser.Aop_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#int_var.
    def visitInt_var(self, ctx:LangParser.Int_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#float_var.
    def visitFloat_var(self, ctx:LangParser.Float_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bool_var.
    def visitBool_var(self, ctx:LangParser.Bool_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#var_decl.
    def visitVar_decl(self, ctx:LangParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#if_param.
    def visitIf_param(self, ctx:LangParser.If_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#if.
    def visitIf(self, ctx:LangParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#elif.
    def visitElif(self, ctx:LangParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#else.
    def visitElse(self, ctx:LangParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#if_statement.
    def visitIf_statement(self, ctx:LangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#while_statement.
    def visitWhile_statement(self, ctx:LangParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#newl_ignore.
    def visitNewl_ignore(self, ctx:LangParser.Newl_ignoreContext):
        return self.visitChildren(ctx)



del LangParser