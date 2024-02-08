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
        4,1,40,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,4,2,80,8,
        2,11,2,12,2,81,5,2,84,8,2,10,2,12,2,87,9,2,1,3,1,3,1,3,1,3,1,3,3,
        3,94,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,5,8,113,8,8,10,8,12,8,116,9,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,
        10,1,10,1,10,1,10,3,10,142,8,10,1,11,1,11,1,11,3,11,147,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,178,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,186,8,
        12,10,12,12,12,189,9,12,1,13,1,13,1,13,3,13,194,8,13,1,14,1,14,1,
        14,1,14,5,14,200,8,14,10,14,12,14,203,9,14,5,14,205,8,14,10,14,12,
        14,208,9,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,3,20,235,8,20,1,21,1,21,1,21,1,21,1,21,4,21,242,8,21,11,
        21,12,21,243,1,22,1,22,4,22,248,8,22,11,22,12,22,249,1,23,1,23,1,
        24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,5,26,262,8,26,10,26,12,26,
        265,9,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,273,8,27,1,28,1,28,1,
        28,1,28,1,28,3,28,280,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,
        30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,5,32,301,
        8,32,10,32,12,32,304,9,32,1,32,3,32,307,8,32,1,32,0,2,16,24,33,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,0,0,315,0,69,1,0,0,0,2,72,1,0,0,0,4,85,
        1,0,0,0,6,93,1,0,0,0,8,95,1,0,0,0,10,97,1,0,0,0,12,99,1,0,0,0,14,
        101,1,0,0,0,16,103,1,0,0,0,18,134,1,0,0,0,20,141,1,0,0,0,22,146,
        1,0,0,0,24,177,1,0,0,0,26,193,1,0,0,0,28,195,1,0,0,0,30,211,1,0,
        0,0,32,214,1,0,0,0,34,218,1,0,0,0,36,222,1,0,0,0,38,226,1,0,0,0,
        40,234,1,0,0,0,42,236,1,0,0,0,44,245,1,0,0,0,46,251,1,0,0,0,48,253,
        1,0,0,0,50,256,1,0,0,0,52,263,1,0,0,0,54,272,1,0,0,0,56,279,1,0,
        0,0,58,283,1,0,0,0,60,288,1,0,0,0,62,293,1,0,0,0,64,298,1,0,0,0,
        66,68,5,37,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,
        0,0,0,70,1,1,0,0,0,71,69,1,0,0,0,72,73,3,0,0,0,73,74,3,4,2,0,74,
        75,3,0,0,0,75,76,5,0,0,1,76,3,1,0,0,0,77,79,3,6,3,0,78,80,5,37,0,
        0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,
        1,0,0,0,83,77,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,5,1,0,0,0,87,85,1,0,0,0,88,94,3,40,20,0,89,94,3,16,8,0,90,94,
        3,24,12,0,91,94,3,30,15,0,92,94,3,64,32,0,93,88,1,0,0,0,93,89,1,
        0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,7,1,0,0,0,95,
        96,5,27,0,0,96,9,1,0,0,0,97,98,5,29,0,0,98,11,1,0,0,0,99,100,5,30,
        0,0,100,13,1,0,0,0,101,102,5,26,0,0,102,15,1,0,0,0,103,104,6,8,-1,
        0,104,105,3,18,9,0,105,114,1,0,0,0,106,107,10,3,0,0,107,108,5,1,
        0,0,108,113,3,18,9,0,109,110,10,2,0,0,110,111,5,2,0,0,111,113,3,
        18,9,0,112,106,1,0,0,0,112,109,1,0,0,0,113,116,1,0,0,0,114,112,1,
        0,0,0,114,115,1,0,0,0,115,17,1,0,0,0,116,114,1,0,0,0,117,118,3,20,
        10,0,118,119,5,3,0,0,119,120,3,18,9,0,120,135,1,0,0,0,121,122,3,
        20,10,0,122,123,5,4,0,0,123,124,3,18,9,0,124,135,1,0,0,0,125,126,
        3,20,10,0,126,127,5,5,0,0,127,128,3,18,9,0,128,135,1,0,0,0,129,130,
        3,20,10,0,130,131,5,6,0,0,131,132,3,18,9,0,132,135,1,0,0,0,133,135,
        3,20,10,0,134,117,1,0,0,0,134,121,1,0,0,0,134,125,1,0,0,0,134,129,
        1,0,0,0,134,133,1,0,0,0,135,19,1,0,0,0,136,137,3,22,11,0,137,138,
        5,7,0,0,138,139,3,20,10,0,139,142,1,0,0,0,140,142,3,22,11,0,141,
        136,1,0,0,0,141,140,1,0,0,0,142,21,1,0,0,0,143,147,3,10,5,0,144,
        147,3,8,4,0,145,147,3,12,6,0,146,143,1,0,0,0,146,144,1,0,0,0,146,
        145,1,0,0,0,147,23,1,0,0,0,148,149,6,12,-1,0,149,150,3,16,8,0,150,
        151,5,8,0,0,151,152,3,16,8,0,152,178,1,0,0,0,153,154,3,16,8,0,154,
        155,5,9,0,0,155,156,3,16,8,0,156,178,1,0,0,0,157,158,3,16,8,0,158,
        159,5,10,0,0,159,160,3,16,8,0,160,178,1,0,0,0,161,162,3,16,8,0,162,
        163,5,11,0,0,163,164,3,16,8,0,164,178,1,0,0,0,165,166,3,16,8,0,166,
        167,5,12,0,0,167,168,3,16,8,0,168,178,1,0,0,0,169,170,3,16,8,0,170,
        171,5,13,0,0,171,172,3,16,8,0,172,178,1,0,0,0,173,174,5,16,0,0,174,
        178,3,24,12,3,175,178,3,14,7,0,176,178,3,8,4,0,177,148,1,0,0,0,177,
        153,1,0,0,0,177,157,1,0,0,0,177,161,1,0,0,0,177,165,1,0,0,0,177,
        169,1,0,0,0,177,173,1,0,0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,
        187,1,0,0,0,179,180,10,5,0,0,180,181,5,14,0,0,181,186,3,24,12,6,
        182,183,10,4,0,0,183,184,5,15,0,0,184,186,3,24,12,5,185,179,1,0,
        0,0,185,182,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,
        0,0,188,25,1,0,0,0,189,187,1,0,0,0,190,194,3,8,4,0,191,194,3,16,
        8,0,192,194,3,24,12,0,193,190,1,0,0,0,193,191,1,0,0,0,193,192,1,
        0,0,0,194,27,1,0,0,0,195,206,5,33,0,0,196,201,3,26,13,0,197,198,
        5,17,0,0,198,200,3,26,13,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,
        1,0,0,0,201,202,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,204,196,
        1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,
        1,0,0,0,208,206,1,0,0,0,209,210,5,34,0,0,210,29,1,0,0,0,211,212,
        3,8,4,0,212,213,3,28,14,0,213,31,1,0,0,0,214,215,3,8,4,0,215,216,
        5,18,0,0,216,217,3,16,8,0,217,33,1,0,0,0,218,219,3,8,4,0,219,220,
        5,18,0,0,220,221,3,10,5,0,221,35,1,0,0,0,222,223,3,8,4,0,223,224,
        5,18,0,0,224,225,3,12,6,0,225,37,1,0,0,0,226,227,3,8,4,0,227,228,
        5,18,0,0,228,229,3,24,12,0,229,39,1,0,0,0,230,235,3,34,17,0,231,
        235,3,36,18,0,232,235,3,38,19,0,233,235,3,32,16,0,234,230,1,0,0,
        0,234,231,1,0,0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,41,1,0,0,0,
        236,237,5,19,0,0,237,238,3,8,4,0,238,239,3,28,14,0,239,241,5,20,
        0,0,240,242,3,6,3,0,241,240,1,0,0,0,242,243,1,0,0,0,243,241,1,0,
        0,0,243,244,1,0,0,0,244,43,1,0,0,0,245,247,5,21,0,0,246,248,3,6,
        3,0,247,246,1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,250,1,0,
        0,0,250,45,1,0,0,0,251,252,5,38,0,0,252,47,1,0,0,0,253,254,3,46,
        23,0,254,255,3,6,3,0,255,49,1,0,0,0,256,257,3,46,23,0,257,258,3,
        6,3,0,258,259,5,37,0,0,259,51,1,0,0,0,260,262,3,50,25,0,261,260,
        1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,53,1,
        0,0,0,265,263,1,0,0,0,266,267,3,52,26,0,267,268,3,50,25,0,268,273,
        1,0,0,0,269,270,3,52,26,0,270,271,3,48,24,0,271,273,1,0,0,0,272,
        266,1,0,0,0,272,269,1,0,0,0,273,55,1,0,0,0,274,275,5,33,0,0,275,
        276,3,24,12,0,276,277,5,34,0,0,277,280,1,0,0,0,278,280,3,24,12,0,
        279,274,1,0,0,0,279,278,1,0,0,0,280,281,1,0,0,0,281,282,5,20,0,0,
        282,57,1,0,0,0,283,284,5,22,0,0,284,285,3,56,28,0,285,286,5,37,0,
        0,286,287,3,54,27,0,287,59,1,0,0,0,288,289,5,23,0,0,289,290,3,56,
        28,0,290,291,5,37,0,0,291,292,3,54,27,0,292,61,1,0,0,0,293,294,5,
        24,0,0,294,295,5,20,0,0,295,296,5,37,0,0,296,297,3,54,27,0,297,63,
        1,0,0,0,298,302,3,58,29,0,299,301,3,60,30,0,300,299,1,0,0,0,301,
        304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,306,1,0,0,0,304,
        302,1,0,0,0,305,307,3,62,31,0,306,305,1,0,0,0,306,307,1,0,0,0,307,
        65,1,0,0,0,23,69,81,85,93,112,114,134,141,146,177,185,187,193,201,
        206,234,243,249,263,272,279,302,306
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'/'", "'*'", "'%'", "'//'", 
                     "'**'", "'>'", "'<'", "'<='", "'>='", "'=='", "'!='", 
                     "'and'", "'or'", "'not'", "','", "'='", "'def'", "':'", 
                     "'if __name__ == \"__main__\" :'", "'if'", "'elif'", 
                     "'else'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "BOOL", "ID", "HID", "INT", 
                      "FLOAT", "KWD", "SYM", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "NEWLINE", "INDENT", "WS", "LINE_ESCAPE" ]

    RULE_newl_ignore = 0
    RULE_prog = 1
    RULE_file = 2
    RULE_exp = 3
    RULE_var = 4
    RULE_int = 5
    RULE_float = 6
    RULE_bool = 7
    RULE_a_op = 8
    RULE_aop3 = 9
    RULE_aop2 = 10
    RULE_aop1 = 11
    RULE_b_op = 12
    RULE_param = 13
    RULE_params = 14
    RULE_func_call = 15
    RULE_aop_var = 16
    RULE_int_var = 17
    RULE_float_var = 18
    RULE_bool_var = 19
    RULE_var_decl = 20
    RULE_function = 21
    RULE_main_func = 22
    RULE_indent = 23
    RULE_block_end = 24
    RULE_block_stmt = 25
    RULE_block_middle = 26
    RULE_exp_block = 27
    RULE_if_param = 28
    RULE_if = 29
    RULE_elif = 30
    RULE_else = 31
    RULE_if_statement = 32

    ruleNames =  [ "newl_ignore", "prog", "file", "exp", "var", "int", "float", 
                   "bool", "a_op", "aop3", "aop2", "aop1", "b_op", "param", 
                   "params", "func_call", "aop_var", "int_var", "float_var", 
                   "bool_var", "var_decl", "function", "main_func", "indent", 
                   "block_end", "block_stmt", "block_middle", "exp_block", 
                   "if_param", "if", "elif", "else", "if_statement" ]

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
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    COMMENT=25
    BOOL=26
    ID=27
    HID=28
    INT=29
    FLOAT=30
    KWD=31
    SYM=32
    LPAREN=33
    RPAREN=34
    LBRACK=35
    RBRACK=36
    NEWLINE=37
    INDENT=38
    WS=39
    LINE_ESCAPE=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Newl_ignoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.NEWLINE)
            else:
                return self.getToken(LangParser.NEWLINE, i)

        def getRuleIndex(self):
            return LangParser.RULE_newl_ignore

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewl_ignore" ):
                listener.enterNewl_ignore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewl_ignore" ):
                listener.exitNewl_ignore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewl_ignore" ):
                return visitor.visitNewl_ignore(self)
            else:
                return visitor.visitChildren(self)




    def newl_ignore(self):

        localctx = LangParser.Newl_ignoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_newl_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(LangParser.NEWLINE) 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newl_ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Newl_ignoreContext)
            else:
                return self.getTypedRuleContext(LangParser.Newl_ignoreContext,i)


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
        self.enterRule(localctx, 2, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.newl_ignore()
            self.state = 73
            self.file_()
            self.state = 74
            self.newl_ignore()
            self.state = 75
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.NEWLINE)
            else:
                return self.getToken(LangParser.NEWLINE, i)

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
        self.enterRule(localctx, 4, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1816199168) != 0):
                self.state = 77
                self.exp()
                self.state = 79 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 78
                        self.match(LangParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 81 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 87
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


        def if_statement(self):
            return self.getTypedRuleContext(LangParser.If_statementContext,0)


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
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.a_op(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.b_op(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.if_statement()
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
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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
        self.enterRule(localctx, 10, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
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
        self.enterRule(localctx, 12, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
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
        self.enterRule(localctx, 14, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
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



    def a_op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.A_opContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_a_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.aop3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 112
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.A_opContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_op)
                        self.state = 106
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 107
                        self.match(LangParser.T__0)
                        self.state = 108
                        self.aop3()
                        pass

                    elif la_ == 2:
                        localctx = LangParser.A_opContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_op)
                        self.state = 109
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 110
                        self.match(LangParser.T__1)
                        self.state = 111
                        self.aop3()
                        pass

             
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 18, self.RULE_aop3)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.aop2()
                self.state = 118
                self.match(LangParser.T__2)
                self.state = 119
                self.aop3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.aop2()
                self.state = 122
                self.match(LangParser.T__3)
                self.state = 123
                self.aop3()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.aop2()
                self.state = 126
                self.match(LangParser.T__4)
                self.state = 127
                self.aop3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.aop2()
                self.state = 130
                self.match(LangParser.T__5)
                self.state = 131
                self.aop3()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
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
        self.enterRule(localctx, 20, self.RULE_aop2)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.aop1()
                self.state = 137
                self.match(LangParser.T__6)
                self.state = 138
                self.aop2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
        self.enterRule(localctx, 22, self.RULE_aop1)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.int_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.var()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
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


        def b_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.B_opContext)
            else:
                return self.getTypedRuleContext(LangParser.B_opContext,i)


        def bool_(self):
            return self.getTypedRuleContext(LangParser.BoolContext,0)


        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


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



    def b_op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.B_opContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_b_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 149
                self.a_op(0)
                self.state = 150
                self.match(LangParser.T__7)
                self.state = 151
                self.a_op(0)
                pass

            elif la_ == 2:
                self.state = 153
                self.a_op(0)
                self.state = 154
                self.match(LangParser.T__8)
                self.state = 155
                self.a_op(0)
                pass

            elif la_ == 3:
                self.state = 157
                self.a_op(0)
                self.state = 158
                self.match(LangParser.T__9)
                self.state = 159
                self.a_op(0)
                pass

            elif la_ == 4:
                self.state = 161
                self.a_op(0)
                self.state = 162
                self.match(LangParser.T__10)
                self.state = 163
                self.a_op(0)
                pass

            elif la_ == 5:
                self.state = 165
                self.a_op(0)
                self.state = 166
                self.match(LangParser.T__11)
                self.state = 167
                self.a_op(0)
                pass

            elif la_ == 6:
                self.state = 169
                self.a_op(0)
                self.state = 170
                self.match(LangParser.T__12)
                self.state = 171
                self.a_op(0)
                pass

            elif la_ == 7:
                self.state = 173
                self.match(LangParser.T__15)
                self.state = 174
                self.b_op(3)
                pass

            elif la_ == 8:
                self.state = 175
                self.bool_()
                pass

            elif la_ == 9:
                self.state = 176
                self.var()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.B_opContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_b_op)
                        self.state = 179
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 180
                        self.match(LangParser.T__13)
                        self.state = 181
                        self.b_op(6)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.B_opContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_b_op)
                        self.state = 182
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 183
                        self.match(LangParser.T__14)
                        self.state = 184
                        self.b_op(5)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def a_op(self):
            return self.getTypedRuleContext(LangParser.A_opContext,0)


        def b_op(self):
            return self.getTypedRuleContext(LangParser.B_opContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = LangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.a_op(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.b_op(0)
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

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ParamContext)
            else:
                return self.getTypedRuleContext(LangParser.ParamContext,i)


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
        self.enterRule(localctx, 28, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(LangParser.LPAREN)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1812004864) != 0):
                self.state = 196
                self.param()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 197
                    self.match(LangParser.T__16)
                    self.state = 198
                    self.param()
                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(LangParser.RPAREN)
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
        self.enterRule(localctx, 30, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.var()
            self.state = 212
            self.params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aop_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangParser.VarContext,0)


        def a_op(self):
            return self.getTypedRuleContext(LangParser.A_opContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_aop_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAop_var" ):
                listener.enterAop_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAop_var" ):
                listener.exitAop_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAop_var" ):
                return visitor.visitAop_var(self)
            else:
                return visitor.visitChildren(self)




    def aop_var(self):

        localctx = LangParser.Aop_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_aop_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.var()
            self.state = 215
            self.match(LangParser.T__17)
            self.state = 216
            self.a_op(0)
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
        self.enterRule(localctx, 34, self.RULE_int_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.var()
            self.state = 219
            self.match(LangParser.T__17)
            self.state = 220
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
        self.enterRule(localctx, 36, self.RULE_float_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.var()
            self.state = 223
            self.match(LangParser.T__17)
            self.state = 224
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


        def b_op(self):
            return self.getTypedRuleContext(LangParser.B_opContext,0)


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
        self.enterRule(localctx, 38, self.RULE_bool_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.var()
            self.state = 227
            self.match(LangParser.T__17)
            self.state = 228
            self.b_op(0)
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


        def aop_var(self):
            return self.getTypedRuleContext(LangParser.Aop_varContext,0)


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
        self.enterRule(localctx, 40, self.RULE_var_decl)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.int_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.float_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.bool_var()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.aop_var()
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
        self.enterRule(localctx, 42, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(LangParser.T__18)
            self.state = 237
            self.var()
            self.state = 238
            self.params()
            self.state = 239
            self.match(LangParser.T__19)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.exp()
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1816199168) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_main_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(LangParser.T__20)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.exp()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1816199168) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(LangParser.INDENT, 0)

        def getRuleIndex(self):
            return LangParser.RULE_indent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndent" ):
                listener.enterIndent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndent" ):
                listener.exitIndent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndent" ):
                return visitor.visitIndent(self)
            else:
                return visitor.visitChildren(self)




    def indent(self):

        localctx = LangParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_indent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(LangParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indent(self):
            return self.getTypedRuleContext(LangParser.IndentContext,0)


        def exp(self):
            return self.getTypedRuleContext(LangParser.ExpContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_block_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_end" ):
                listener.enterBlock_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_end" ):
                listener.exitBlock_end(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_end" ):
                return visitor.visitBlock_end(self)
            else:
                return visitor.visitChildren(self)




    def block_end(self):

        localctx = LangParser.Block_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.indent()
            self.state = 254
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indent(self):
            return self.getTypedRuleContext(LangParser.IndentContext,0)


        def exp(self):
            return self.getTypedRuleContext(LangParser.ExpContext,0)


        def NEWLINE(self):
            return self.getToken(LangParser.NEWLINE, 0)

        def getRuleIndex(self):
            return LangParser.RULE_block_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stmt" ):
                listener.enterBlock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stmt" ):
                listener.exitBlock_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = LangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.indent()
            self.state = 257
            self.exp()
            self.state = 258
            self.match(LangParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_middleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(LangParser.Block_stmtContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_block_middle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_middle" ):
                listener.enterBlock_middle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_middle" ):
                listener.exitBlock_middle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_middle" ):
                return visitor.visitBlock_middle(self)
            else:
                return visitor.visitChildren(self)




    def block_middle(self):

        localctx = LangParser.Block_middleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_block_middle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.block_stmt() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_middle(self):
            return self.getTypedRuleContext(LangParser.Block_middleContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(LangParser.Block_stmtContext,0)


        def block_end(self):
            return self.getTypedRuleContext(LangParser.Block_endContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_exp_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_block" ):
                listener.enterExp_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_block" ):
                listener.exitExp_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_block" ):
                return visitor.visitExp_block(self)
            else:
                return visitor.visitChildren(self)




    def exp_block(self):

        localctx = LangParser.Exp_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp_block)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.block_middle()
                self.state = 267
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.block_middle()
                self.state = 270
                self.block_end()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b_op(self):
            return self.getTypedRuleContext(LangParser.B_opContext,0)


        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def getRuleIndex(self):
            return LangParser.RULE_if_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_param" ):
                listener.enterIf_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_param" ):
                listener.exitIf_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_param" ):
                return visitor.visitIf_param(self)
            else:
                return visitor.visitChildren(self)




    def if_param(self):

        localctx = LangParser.If_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 274
                self.match(LangParser.LPAREN)
                self.state = 275
                self.b_op(0)
                self.state = 276
                self.match(LangParser.RPAREN)
                pass
            elif token in [16, 26, 27, 29, 30]:
                self.state = 278
                self.b_op(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 281
            self.match(LangParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_param(self):
            return self.getTypedRuleContext(LangParser.If_paramContext,0)


        def NEWLINE(self):
            return self.getToken(LangParser.NEWLINE, 0)

        def exp_block(self):
            return self.getTypedRuleContext(LangParser.Exp_blockContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = LangParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(LangParser.T__21)
            self.state = 284
            self.if_param()
            self.state = 285
            self.match(LangParser.NEWLINE)
            self.state = 286
            self.exp_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_param(self):
            return self.getTypedRuleContext(LangParser.If_paramContext,0)


        def NEWLINE(self):
            return self.getToken(LangParser.NEWLINE, 0)

        def exp_block(self):
            return self.getTypedRuleContext(LangParser.Exp_blockContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = LangParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(LangParser.T__22)
            self.state = 289
            self.if_param()
            self.state = 290
            self.match(LangParser.NEWLINE)
            self.state = 291
            self.exp_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(LangParser.NEWLINE, 0)

        def exp_block(self):
            return self.getTypedRuleContext(LangParser.Exp_blockContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = LangParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(LangParser.T__23)
            self.state = 294
            self.match(LangParser.T__19)
            self.state = 295
            self.match(LangParser.NEWLINE)
            self.state = 296
            self.exp_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(LangParser.IfContext,0)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ElifContext)
            else:
                return self.getTypedRuleContext(LangParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(LangParser.ElseContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = LangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.if_()
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 299
                    self.elif_() 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 305
                self.else_()


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
        self._predicates[8] = self.a_op_sempred
        self._predicates[12] = self.b_op_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_op_sempred(self, localctx:A_opContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def b_op_sempred(self, localctx:B_opContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




