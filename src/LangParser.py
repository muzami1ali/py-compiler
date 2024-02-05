# Generated from Lang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,3,2,54,8,
        2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,73,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,92,8,8,1,9,1,9,1,9,1,9,1,9,3,9,99,8,9,1,
        10,1,10,1,10,3,10,104,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,130,8,11,1,12,1,12,1,12,1,12,5,12,136,8,12,
        10,12,12,12,139,9,12,5,12,141,8,12,10,12,12,12,144,9,12,1,12,1,12,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,3,17,166,8,17,1,18,1,18,1,18,1,18,1,18,
        4,18,173,8,18,11,18,12,18,174,1,19,1,19,4,19,179,8,19,11,19,12,19,
        180,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,0,0,186,0,40,1,0,0,0,2,46,1,0,0,0,4,53,1,0,0,0,6,55,1,0,0,
        0,8,57,1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,72,1,0,0,0,16,91,1,
        0,0,0,18,98,1,0,0,0,20,103,1,0,0,0,22,129,1,0,0,0,24,131,1,0,0,0,
        26,147,1,0,0,0,28,150,1,0,0,0,30,154,1,0,0,0,32,158,1,0,0,0,34,165,
        1,0,0,0,36,167,1,0,0,0,38,176,1,0,0,0,40,41,3,2,1,0,41,42,5,0,0,
        1,42,1,1,0,0,0,43,45,3,4,2,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,
        0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,54,3,34,17,0,50,
        54,3,14,7,0,51,54,3,22,11,0,52,54,3,26,13,0,53,49,1,0,0,0,53,50,
        1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,5,1,0,0,0,55,56,5,23,0,0,
        56,7,1,0,0,0,57,58,5,25,0,0,58,9,1,0,0,0,59,60,5,26,0,0,60,11,1,
        0,0,0,61,62,5,22,0,0,62,13,1,0,0,0,63,64,3,16,8,0,64,65,5,1,0,0,
        65,66,3,14,7,0,66,73,1,0,0,0,67,68,3,16,8,0,68,69,5,2,0,0,69,70,
        3,14,7,0,70,73,1,0,0,0,71,73,3,16,8,0,72,63,1,0,0,0,72,67,1,0,0,
        0,72,71,1,0,0,0,73,15,1,0,0,0,74,75,3,18,9,0,75,76,5,3,0,0,76,77,
        3,16,8,0,77,92,1,0,0,0,78,79,3,18,9,0,79,80,5,4,0,0,80,81,3,16,8,
        0,81,92,1,0,0,0,82,83,3,18,9,0,83,84,5,5,0,0,84,85,3,16,8,0,85,92,
        1,0,0,0,86,87,3,18,9,0,87,88,5,6,0,0,88,89,3,16,8,0,89,92,1,0,0,
        0,90,92,3,18,9,0,91,74,1,0,0,0,91,78,1,0,0,0,91,82,1,0,0,0,91,86,
        1,0,0,0,91,90,1,0,0,0,92,17,1,0,0,0,93,94,3,20,10,0,94,95,5,7,0,
        0,95,96,3,18,9,0,96,99,1,0,0,0,97,99,3,20,10,0,98,93,1,0,0,0,98,
        97,1,0,0,0,99,19,1,0,0,0,100,104,3,8,4,0,101,104,3,6,3,0,102,104,
        3,10,5,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,21,
        1,0,0,0,105,106,3,14,7,0,106,107,5,8,0,0,107,108,3,14,7,0,108,130,
        1,0,0,0,109,110,3,14,7,0,110,111,5,9,0,0,111,112,3,14,7,0,112,130,
        1,0,0,0,113,114,3,14,7,0,114,115,5,10,0,0,115,116,3,14,7,0,116,130,
        1,0,0,0,117,118,3,14,7,0,118,119,5,11,0,0,119,120,3,14,7,0,120,130,
        1,0,0,0,121,122,3,14,7,0,122,123,5,12,0,0,123,124,3,14,7,0,124,130,
        1,0,0,0,125,126,3,14,7,0,126,127,5,13,0,0,127,128,3,14,7,0,128,130,
        1,0,0,0,129,105,1,0,0,0,129,109,1,0,0,0,129,113,1,0,0,0,129,117,
        1,0,0,0,129,121,1,0,0,0,129,125,1,0,0,0,130,23,1,0,0,0,131,142,5,
        14,0,0,132,137,3,6,3,0,133,134,5,15,0,0,134,136,3,6,3,0,135,133,
        1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,141,
        1,0,0,0,139,137,1,0,0,0,140,132,1,0,0,0,141,144,1,0,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,142,1,0,0,0,145,146,
        5,16,0,0,146,25,1,0,0,0,147,148,3,6,3,0,148,149,3,24,12,0,149,27,
        1,0,0,0,150,151,3,6,3,0,151,152,5,17,0,0,152,153,3,8,4,0,153,29,
        1,0,0,0,154,155,3,6,3,0,155,156,5,17,0,0,156,157,3,10,5,0,157,31,
        1,0,0,0,158,159,3,6,3,0,159,160,5,17,0,0,160,161,3,12,6,0,161,33,
        1,0,0,0,162,166,3,28,14,0,163,166,3,30,15,0,164,166,3,32,16,0,165,
        162,1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,35,1,0,0,0,167,168,
        5,18,0,0,168,169,3,6,3,0,169,170,3,24,12,0,170,172,5,19,0,0,171,
        173,3,4,2,0,172,171,1,0,0,0,173,174,1,0,0,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,37,1,0,0,0,176,178,5,20,0,0,177,179,3,4,2,0,178,
        177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        39,1,0,0,0,12,46,53,72,91,98,103,129,137,142,165,174,180
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'/'", "'*'", "'%'", "'//'", 
                     "'**'", "'>'", "'<'", "'<='", "'>='", "'=='", "'!='", 
                     "'('", "','", "')'", "'='", "'def'", "':'", "'if __name__ == \"__main__\" :'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "BOOL", "ID", "HID", "INT", 
                      "FLOAT", "KWD", "SYM", "PAREN", "WS" ]

    RULE_prog = 0
    RULE_file = 1
    RULE_exp = 2
    RULE_var = 3
    RULE_int = 4
    RULE_float = 5
    RULE_bool = 6
    RULE_a_op = 7
    RULE_aop3 = 8
    RULE_aop2 = 9
    RULE_aop1 = 10
    RULE_b_op = 11
    RULE_params = 12
    RULE_func_call = 13
    RULE_int_var = 14
    RULE_float_var = 15
    RULE_bool_var = 16
    RULE_var_decl = 17
    RULE_function = 18
    RULE_main_func = 19

    ruleNames =  [ "prog", "file", "exp", "var", "int", "float", "bool", 
                   "a_op", "aop3", "aop2", "aop1", "b_op", "params", "func_call", 
                   "int_var", "float_var", "bool_var", "var_decl", "function", 
                   "main_func" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    COMMENT=21
    BOOL=22
    ID=23
    HID=24
    INT=25
    FLOAT=26
    KWD=27
    SYM=28
    PAREN=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_(self):
            return self.getTypedRuleContext(LangParser.FileContext,0)


        def EOF(self):
            return self.getToken(LangParser.EOF, 0)

        def getRuleIndex(self):
            return LangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.file_()
            self.state = 41
            self.match(LangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = LangParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 109051904) != 0):
                self.state = 43
                self.exp()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(LangParser.Var_declContext,0)


        def a_op(self):
            return self.getTypedRuleContext(LangParser.A_opContext,0)


        def b_op(self):
            return self.getTypedRuleContext(LangParser.B_opContext,0)


        def func_call(self):
            return self.getTypedRuleContext(LangParser.Func_callContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = LangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.a_op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.b_op()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def getRuleIndex(self):
            return LangParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(LangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangParser.INT, 0)

        def getRuleIndex(self):
            return LangParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = LangParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(LangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(LangParser.FLOAT, 0)

        def getRuleIndex(self):
            return LangParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = LangParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(LangParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(LangParser.BOOL, 0)

        def getRuleIndex(self):
            return LangParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = LangParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aop3(self):
            return self.getTypedRuleContext(LangParser.Aop3Context,0)


        def a_op(self):
            return self.getTypedRuleContext(LangParser.A_opContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_a_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_op" ):
                listener.enterA_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_op" ):
                listener.exitA_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_op" ):
                return visitor.visitA_op(self)
            else:
                return visitor.visitChildren(self)




    def a_op(self):

        localctx = LangParser.A_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_a_op)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.aop3()
                self.state = 64
                self.match(LangParser.T__0)
                self.state = 65
                self.a_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.aop3()
                self.state = 68
                self.match(LangParser.T__1)
                self.state = 69
                self.a_op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.aop3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aop3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aop2(self):
            return self.getTypedRuleContext(LangParser.Aop2Context,0)


        def aop3(self):
            return self.getTypedRuleContext(LangParser.Aop3Context,0)


        def getRuleIndex(self):
            return LangParser.RULE_aop3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAop3" ):
                listener.enterAop3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAop3" ):
                listener.exitAop3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAop3" ):
                return visitor.visitAop3(self)
            else:
                return visitor.visitChildren(self)




    def aop3(self):

        localctx = LangParser.Aop3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_aop3)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.aop2()
                self.state = 75
                self.match(LangParser.T__2)
                self.state = 76
                self.aop3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.aop2()
                self.state = 79
                self.match(LangParser.T__3)
                self.state = 80
                self.aop3()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.aop2()
                self.state = 83
                self.match(LangParser.T__4)
                self.state = 84
                self.aop3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.aop2()
                self.state = 87
                self.match(LangParser.T__5)
                self.state = 88
                self.aop3()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.aop2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aop2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aop1(self):
            return self.getTypedRuleContext(LangParser.Aop1Context,0)


        def aop2(self):
            return self.getTypedRuleContext(LangParser.Aop2Context,0)


        def getRuleIndex(self):
            return LangParser.RULE_aop2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAop2" ):
                listener.enterAop2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAop2" ):
                listener.exitAop2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAop2" ):
                return visitor.visitAop2(self)
            else:
                return visitor.visitChildren(self)




    def aop2(self):

        localctx = LangParser.Aop2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_aop2)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.aop1()
                self.state = 94
                self.match(LangParser.T__6)
                self.state = 95
                self.aop2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.aop1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aop1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(LangParser.IntContext,0)


        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def float_(self):
            return self.getTypedRuleContext(LangParser.FloatContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_aop1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAop1" ):
                listener.enterAop1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAop1" ):
                listener.exitAop1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAop1" ):
                return visitor.visitAop1(self)
            else:
                return visitor.visitChildren(self)




    def aop1(self):

        localctx = LangParser.Aop1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_aop1)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.int_()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.var()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.float_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class B_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.A_opContext)
            else:
                return self.getTypedRuleContext(LangParser.A_opContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_b_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB_op" ):
                listener.enterB_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB_op" ):
                listener.exitB_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_op" ):
                return visitor.visitB_op(self)
            else:
                return visitor.visitChildren(self)




    def b_op(self):

        localctx = LangParser.B_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_b_op)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.a_op()
                self.state = 106
                self.match(LangParser.T__7)
                self.state = 107
                self.a_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.a_op()
                self.state = 110
                self.match(LangParser.T__8)
                self.state = 111
                self.a_op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.a_op()
                self.state = 114
                self.match(LangParser.T__9)
                self.state = 115
                self.a_op()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.a_op()
                self.state = 118
                self.match(LangParser.T__10)
                self.state = 119
                self.a_op()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.a_op()
                self.state = 122
                self.match(LangParser.T__11)
                self.state = 123
                self.a_op()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.a_op()
                self.state = 126
                self.match(LangParser.T__12)
                self.state = 127
                self.a_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.VarContext)
            else:
                return self.getTypedRuleContext(LangParser.VarContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = LangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LangParser.T__13)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 132
                self.var()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 133
                    self.match(LangParser.T__14)
                    self.state = 134
                    self.var()
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(LangParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def params(self):
            return self.getTypedRuleContext(LangParser.ParamsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = LangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.var()
            self.state = 148
            self.params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def int_(self):
            return self.getTypedRuleContext(LangParser.IntContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_int_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_var" ):
                listener.enterInt_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_var" ):
                listener.exitInt_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_var" ):
                return visitor.visitInt_var(self)
            else:
                return visitor.visitChildren(self)




    def int_var(self):

        localctx = LangParser.Int_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_int_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.var()
            self.state = 151
            self.match(LangParser.T__16)
            self.state = 152
            self.int_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def float_(self):
            return self.getTypedRuleContext(LangParser.FloatContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_float_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_var" ):
                listener.enterFloat_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_var" ):
                listener.exitFloat_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_var" ):
                return visitor.visitFloat_var(self)
            else:
                return visitor.visitChildren(self)




    def float_var(self):

        localctx = LangParser.Float_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_float_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.var()
            self.state = 155
            self.match(LangParser.T__16)
            self.state = 156
            self.float_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def bool_(self):
            return self.getTypedRuleContext(LangParser.BoolContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_bool_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_var" ):
                listener.enterBool_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_var" ):
                listener.exitBool_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_var" ):
                return visitor.visitBool_var(self)
            else:
                return visitor.visitChildren(self)




    def bool_var(self):

        localctx = LangParser.Bool_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_bool_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.var()
            self.state = 159
            self.match(LangParser.T__16)
            self.state = 160
            self.bool_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_var(self):
            return self.getTypedRuleContext(LangParser.Int_varContext,0)


        def float_var(self):
            return self.getTypedRuleContext(LangParser.Float_varContext,0)


        def bool_var(self):
            return self.getTypedRuleContext(LangParser.Bool_varContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = LangParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_decl)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.int_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.float_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.bool_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def params(self):
            return self.getTypedRuleContext(LangParser.ParamsContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = LangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(LangParser.T__17)
            self.state = 168
            self.var()
            self.state = 169
            self.params()
            self.state = 170
            self.match(LangParser.T__18)
            self.state = 172 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 171
                self.exp()
                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 109051904) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_main_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_func" ):
                listener.enterMain_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_func" ):
                listener.exitMain_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




    def main_func(self):

        localctx = LangParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_main_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(LangParser.T__19)
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.exp()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 109051904) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





