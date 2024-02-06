from llvmlite import ir

def int_op(op,lhs,rhs,builder):
     match op:
        case "+":
            return (builder.add(lhs,rhs), "IntVal")
        case "-":
            return (builder.sub(lhs,rhs), "IntVal")

def float_op(op,lhs,rhs,builder):
     match op:
        case "+":
            return (builder.fadd(lhs,rhs), "FloatVal")
        case "-":
            return (builder.fsub(lhs,rhs), "FloatVal")



def aop(op,lhs,rhs,builder,symT,addrT):
    print(lhs)
    lhs_val = lhs[0]
    lhs_typ = lhs[1]
    if lhs_typ == "Var":
        lhs_typ = f"{symT[lhs_val]}Val"
        addr = addrT[lhs_val]
        lhs_val = builder.load(addr)
    rhs_val = rhs[0]
    rhs_typ = rhs[1]
    if rhs_typ == "Var":
        rhs_typ = f"{symT[rhs_val]}Val"
        addr = addrT[rhs_val]
        rhs_val = builder.load(addr)

    if rhs_typ == lhs_typ:
        if lhs_typ == "IntVal":
            return int_op(op,lhs_val,rhs_val,builder)
        elif lhs_typ == "FloatVal":
            return float_op(op,lhs_val,rhs_val,builder)
    else:
        if lhs_typ == "IntVal":
            lhs_val = builder.sitofp(lhs_val, ir.FloatType())
            return float_op(op,lhs_val,rhs_val,builder)
        elif rhs_typ == "IntVal":
            rhs_val = builder.sitofp(rhs_val, ir.FloatType())
            return float_op(op,lhs_val,rhs_val,builder)


