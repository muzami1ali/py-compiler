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
        4,1,19,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,1,2,3,2,34,8,2,1,3,1,3,1,3,1,3,3,3,40,8,3,1,4,1,
        4,1,4,1,4,3,4,46,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,
        1,10,10,0,2,4,6,8,10,12,14,16,18,0,0,108,0,20,1,0,0,0,2,26,1,0,0,
        0,4,33,1,0,0,0,6,35,1,0,0,0,8,41,1,0,0,0,10,49,1,0,0,0,12,94,1,0,
        0,0,14,96,1,0,0,0,16,98,1,0,0,0,18,100,1,0,0,0,20,21,3,2,1,0,21,
        22,5,0,0,1,22,1,1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,28,1,0,0,
        0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,0,29,34,3,
        6,3,0,30,34,3,10,5,0,31,34,3,12,6,0,32,34,3,8,4,0,33,29,1,0,0,0,
        33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,5,1,0,0,0,35,36,3,16,
        8,0,36,39,5,1,0,0,37,40,3,10,5,0,38,40,3,12,6,0,39,37,1,0,0,0,39,
        38,1,0,0,0,40,7,1,0,0,0,41,42,5,2,0,0,42,45,5,3,0,0,43,46,3,10,5,
        0,44,46,3,12,6,0,45,43,1,0,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,48,
        5,4,0,0,48,9,1,0,0,0,49,50,6,5,-1,0,50,51,3,14,7,0,51,66,1,0,0,0,
        52,53,10,4,0,0,53,54,5,5,0,0,54,65,3,10,5,5,55,56,10,3,0,0,56,57,
        5,6,0,0,57,65,3,10,5,4,58,59,10,2,0,0,59,60,5,7,0,0,60,65,3,10,5,
        3,61,62,10,1,0,0,62,63,5,8,0,0,63,65,3,10,5,2,64,52,1,0,0,0,64,55,
        1,0,0,0,64,58,1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,11,1,0,0,0,68,66,1,0,0,0,69,95,3,18,9,0,70,71,3,
        10,5,0,71,72,5,9,0,0,72,73,3,10,5,0,73,95,1,0,0,0,74,75,3,10,5,0,
        75,76,5,10,0,0,76,77,3,10,5,0,77,95,1,0,0,0,78,79,3,10,5,0,79,80,
        5,11,0,0,80,81,3,10,5,0,81,95,1,0,0,0,82,83,3,10,5,0,83,84,5,12,
        0,0,84,85,3,10,5,0,85,95,1,0,0,0,86,87,3,10,5,0,87,88,5,13,0,0,88,
        89,3,10,5,0,89,95,1,0,0,0,90,91,3,10,5,0,91,92,5,14,0,0,92,93,3,
        10,5,0,93,95,1,0,0,0,94,69,1,0,0,0,94,70,1,0,0,0,94,74,1,0,0,0,94,
        78,1,0,0,0,94,82,1,0,0,0,94,86,1,0,0,0,94,90,1,0,0,0,95,13,1,0,0,
        0,96,97,5,17,0,0,97,15,1,0,0,0,98,99,5,16,0,0,99,17,1,0,0,0,100,
        101,5,18,0,0,101,19,1,0,0,0,7,26,33,39,45,64,66,94
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'('", "')'", "'/'", 
                     "'*'", "'-'", "'+'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "ID", "NUM", "BOOL", "WS" ]

    RULE_prog = 0
    RULE_file = 1
    RULE_statement = 2
    RULE_assignment_stmt = 3
    RULE_print_stmt = 4
    RULE_arithmetic_stmt = 5
    RULE_boolean_stmt = 6
    RULE_num = 7
    RULE_id = 8
    RULE_bool = 9

    ruleNames =  [ "prog", "file", "statement", "assignment_stmt", "print_stmt", 
                   "arithmetic_stmt", "boolean_stmt", "num", "id", "bool" ]

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
    COMMENT=15
    ID=16
    NUM=17
    BOOL=18
    WS=19

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
            self.state = 20
            self.file_()
            self.state = 21
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)


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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 458756) != 0):
                self.state = 23
                self.statement()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(LangParser.Assignment_stmtContext,0)


        def arithmetic_stmt(self):
            return self.getTypedRuleContext(LangParser.Arithmetic_stmtContext,0)


        def boolean_stmt(self):
            return self.getTypedRuleContext(LangParser.Boolean_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(LangParser.Print_stmtContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.arithmetic_stmt(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.boolean_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.print_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(LangParser.IdContext,0)


        def arithmetic_stmt(self):
            return self.getTypedRuleContext(LangParser.Arithmetic_stmtContext,0)


        def boolean_stmt(self):
            return self.getTypedRuleContext(LangParser.Boolean_stmtContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = LangParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.id_()
            self.state = 36
            self.match(LangParser.T__0)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 37
                self.arithmetic_stmt(0)
                pass

            elif la_ == 2:
                self.state = 38
                self.boolean_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_stmt(self):
            return self.getTypedRuleContext(LangParser.Arithmetic_stmtContext,0)


        def boolean_stmt(self):
            return self.getTypedRuleContext(LangParser.Boolean_stmtContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = LangParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(LangParser.T__1)
            self.state = 42
            self.match(LangParser.T__2)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 43
                self.arithmetic_stmt(0)
                pass

            elif la_ == 2:
                self.state = 44
                self.boolean_stmt()
                pass


            self.state = 47
            self.match(LangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(LangParser.NumContext,0)


        def arithmetic_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Arithmetic_stmtContext)
            else:
                return self.getTypedRuleContext(LangParser.Arithmetic_stmtContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_arithmetic_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_stmt" ):
                listener.enterArithmetic_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_stmt" ):
                listener.exitArithmetic_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_stmt" ):
                return visitor.visitArithmetic_stmt(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_stmt(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.Arithmetic_stmtContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_arithmetic_stmt, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.num()
            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.Arithmetic_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_stmt)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        self.match(LangParser.T__4)
                        self.state = 54
                        self.arithmetic_stmt(5)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.Arithmetic_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_stmt)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        self.match(LangParser.T__5)
                        self.state = 57
                        self.arithmetic_stmt(4)
                        pass

                    elif la_ == 3:
                        localctx = LangParser.Arithmetic_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_stmt)
                        self.state = 58
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 59
                        self.match(LangParser.T__6)
                        self.state = 60
                        self.arithmetic_stmt(3)
                        pass

                    elif la_ == 4:
                        localctx = LangParser.Arithmetic_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_stmt)
                        self.state = 61
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 62
                        self.match(LangParser.T__7)
                        self.state = 63
                        self.arithmetic_stmt(2)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Boolean_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_(self):
            return self.getTypedRuleContext(LangParser.BoolContext,0)


        def arithmetic_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Arithmetic_stmtContext)
            else:
                return self.getTypedRuleContext(LangParser.Arithmetic_stmtContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_boolean_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_stmt" ):
                listener.enterBoolean_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_stmt" ):
                listener.exitBoolean_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_stmt" ):
                return visitor.visitBoolean_stmt(self)
            else:
                return visitor.visitChildren(self)




    def boolean_stmt(self):

        localctx = LangParser.Boolean_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolean_stmt)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.bool_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.arithmetic_stmt(0)
                self.state = 71
                self.match(LangParser.T__8)
                self.state = 72
                self.arithmetic_stmt(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.arithmetic_stmt(0)
                self.state = 75
                self.match(LangParser.T__9)
                self.state = 76
                self.arithmetic_stmt(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.arithmetic_stmt(0)
                self.state = 79
                self.match(LangParser.T__10)
                self.state = 80
                self.arithmetic_stmt(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.arithmetic_stmt(0)
                self.state = 83
                self.match(LangParser.T__11)
                self.state = 84
                self.arithmetic_stmt(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.arithmetic_stmt(0)
                self.state = 87
                self.match(LangParser.T__12)
                self.state = 88
                self.arithmetic_stmt(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.arithmetic_stmt(0)
                self.state = 91
                self.match(LangParser.T__13)
                self.state = 92
                self.arithmetic_stmt(0)
                pass


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

        def NUM(self):
            return self.getToken(LangParser.NUM, 0)

        def getRuleIndex(self):
            return LangParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = LangParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(LangParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def getRuleIndex(self):
            return LangParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = LangParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(LangParser.ID)
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
        self.enterRule(localctx, 18, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.arithmetic_stmt_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_stmt_sempred(self, localctx:Arithmetic_stmtContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




