import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprListener import ExprListener

class ListenerInterp(ExprListener):
    def __init__(self):
        self.result = {}

    def exitNewl(self, ctx: ExprParser.NewlContext):
        self.result[ctx] = ctx.getText()

    def exitNum(self, ctx: ExprParser.NumContext):
        self.result[ctx] = ctx.getText()
    
    def exitParen(self, ctx: ExprParser.ParenContext):
        self.result[ctx] = ctx.getText()

    def exitPrint(self, ctx: ExprParser.PrintContext):
        self.result[ctx] = ctx.getText()

    def exitFunction(self, ctx: ExprParser.FunctionContext):
        # children = ctx.getChildCount()
        # for x in range(5):
        #     print("individual: {0}".format(ctx.getChild(x).getText()))
        for x in range(4):
            self.result[ctx] = ctx.getChild(x).getText()
            # print(ctx.getChild(x))
            print(self.result[ctx.getChild(x)])

        # if ctx.getChildCount() == 5: 
        #     if ctx.getChild(0).getText() == "print": 
        #         self.result[ctx] = "print"
                # print(ctx.getChild(1).getText())

    # def exitProg(self, ctx: ExprParser.ProgContext):
        # print(ctx.getChildCount())
    #     for i in range(ctx.getChildCount()):
        # print(self.result[ctx.getChild(0)])
