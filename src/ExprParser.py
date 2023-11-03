# Generated from Expr.g4 by ANTLR 4.13.0
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
        4,1,5,30,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,
        0,0,6,0,2,4,6,8,10,0,1,1,0,2,3,23,0,12,1,0,0,0,2,15,1,0,0,0,4,17,
        1,0,0,0,6,23,1,0,0,0,8,25,1,0,0,0,10,27,1,0,0,0,12,13,3,4,2,0,13,
        14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,0,0,16,3,1,0,0,0,17,18,3,2,1,0,
        18,19,3,10,5,0,19,20,3,6,3,0,20,21,3,10,5,0,21,22,3,8,4,0,22,5,1,
        0,0,0,23,24,5,4,0,0,24,7,1,0,0,0,25,26,5,5,0,0,26,9,1,0,0,0,27,28,
        7,0,0,0,28,11,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Number", "Newline" ]

    RULE_prog = 0
    RULE_print = 1
    RULE_function = 2
    RULE_num = 3
    RULE_newl = 4
    RULE_paren = 5

    ruleNames =  [ "prog", "print", "function", "num", "newl", "paren" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Number=4
    Newline=5

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

        def function(self):
            return self.getTypedRuleContext(ExprParser.FunctionContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.function()
            self.state = 13
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = ExprParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(ExprParser.T__0)
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

        def print_(self):
            return self.getTypedRuleContext(ExprParser.PrintContext,0)


        def paren(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParenContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParenContext,i)


        def num(self):
            return self.getTypedRuleContext(ExprParser.NumContext,0)


        def newl(self):
            return self.getTypedRuleContext(ExprParser.NewlContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = ExprParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.print_()
            self.state = 18
            self.paren()
            self.state = 19
            self.num()
            self.state = 20
            self.paren()
            self.state = 21
            self.newl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(ExprParser.Number, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = ExprParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ExprParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Newline(self):
            return self.getToken(ExprParser.Newline, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_newl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewl" ):
                listener.enterNewl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewl" ):
                listener.exitNewl(self)




    def newl(self):

        localctx = ExprParser.NewlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_newl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ExprParser.Newline)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_paren

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)




    def paren(self):

        localctx = ExprParser.ParenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paren)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





