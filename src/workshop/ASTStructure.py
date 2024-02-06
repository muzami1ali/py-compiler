


class Expr:
    def accept(self):
        pass


class Int(Expr):
    def __init__(self, num:int):
        self.num = num 

    # def accept(self, visitor):
    #     visitor.visitInt(self)

class Float(Expr):
    def __init__(self, num:float):
        self.num = num 

class Var(Expr):
    def __init__(self, name:str):
        self.name = name

class Assign(Expr):
    def __init__(self, var:Var, val:Expr, typ:str):
        self.var = var
        self.val = val
        self.typ = typ

class Aop(Expr):
    def __init__(self, op:str, lhs:Expr, rhs:Expr, typ:str):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        self.typ = typ

class Bop(Expr):
    def __init__(self, op:str, lhs:Expr, rhs:Expr):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

class Call(Expr): 
    def __init__(self, fname:Var, params:list[Expr]):
        self.fname = fname
        self.params = params

