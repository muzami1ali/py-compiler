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
        4,1,5,18,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,2,3,14,0,6,1,0,0,0,2,9,1,0,0,
        0,4,15,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,0,0,
        10,11,3,4,2,0,11,12,5,4,0,0,12,13,3,4,2,0,13,14,5,5,0,0,14,3,1,0,
        0,0,15,16,7,0,0,0,16,5,1,0,0,0,0
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
    RULE_function = 1
    RULE_paren = 2

    ruleNames =  [ "prog", "function", "paren" ]

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
            self.state = 6
            self.function()
            self.state = 7
            self.match(ExprParser.EOF)
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

        def paren(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParenContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParenContext,i)


        def Number(self):
            return self.getToken(ExprParser.Number, 0)

        def Newline(self):
            return self.getToken(ExprParser.Newline, 0)

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
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(ExprParser.T__0)
            self.state = 10
            self.paren()
            self.state = 11
            self.match(ExprParser.Number)
            self.state = 12
            self.paren()
            self.state = 13
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
        self.enterRule(localctx, 4, self.RULE_paren)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
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





