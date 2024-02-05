# from ASTStructure import *
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitInt(self):
        pass

    @abstractmethod
    def visitFloat(self):
        pass

    @abstractmethod
    def visitVar(self):
        pass

    @abstractmethod
    def visitAssign(self):
        pass

    @abstractmethod
    def visitAop(self):
        pass

    @abstractmethod
    def visitBop(self):
        pass

    @abstractmethod
    def visitCall(self):
        pass

