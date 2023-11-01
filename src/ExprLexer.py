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
        4,0,5,28,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,23,8,3,11,3,12,3,24,1,4,1,
        4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,2,1,0,48,57,1,0,10,10,28,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,
        3,17,1,0,0,0,5,19,1,0,0,0,7,22,1,0,0,0,9,26,1,0,0,0,11,12,5,112,
        0,0,12,13,5,114,0,0,13,14,5,105,0,0,14,15,5,110,0,0,15,16,5,116,
        0,0,16,2,1,0,0,0,17,18,5,40,0,0,18,4,1,0,0,0,19,20,5,41,0,0,20,6,
        1,0,0,0,21,23,7,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,
        24,25,1,0,0,0,25,8,1,0,0,0,26,27,7,1,0,0,27,10,1,0,0,0,2,0,24,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    Number = 4
    Newline = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Number", "Newline" ]

    ruleNames = [ "T__0", "T__1", "T__2", "Number", "Newline" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


