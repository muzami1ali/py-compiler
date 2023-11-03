# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,23,8,4,11,4,12,4,24,1,5,4,
        5,28,8,5,11,5,12,5,29,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,
        2,1,0,48,57,3,0,9,10,13,13,32,32,34,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,15,1,
        0,0,0,5,17,1,0,0,0,7,19,1,0,0,0,9,22,1,0,0,0,11,27,1,0,0,0,13,14,
        5,43,0,0,14,2,1,0,0,0,15,16,5,45,0,0,16,4,1,0,0,0,17,18,5,47,0,0,
        18,6,1,0,0,0,19,20,5,42,0,0,20,8,1,0,0,0,21,23,7,0,0,0,22,21,1,0,
        0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,10,1,0,0,0,26,28,
        7,1,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,31,1,0,0,0,31,32,6,5,0,0,32,12,1,0,0,0,3,0,24,29,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'/'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INT", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


