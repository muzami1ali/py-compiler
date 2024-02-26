from llvmlite import ir
import re


def getVarVal(var, typ, symT, addrT, builder):
    if typ == "Var":
        var_typ = symT[var]
        param  = len(re.findall("Arg",var_typ))
        if param:
            typ = re.sub("Arg", "Val", var_typ)
            var = addrT[var]
        else:
            typ = re.sub("Var", "Val", var_typ)
            addr = addrT[var]
            var = builder.load(addr)
    return (var,typ)


def bop(op,lhs,rhs,builder,symT,addrT):
    lhs_val, lhs_typ = getVarVal(lhs[0],lhs[1],symT,addrT,builder)
    rhs_val, rhs_typ = getVarVal(rhs[0],rhs[1],symT,addrT,builder)
    # lhs_val = lhs[0]
    # lhs_typ = lhs[1]
    # if lhs_typ == "Var":
    #     lhs_typ = re.sub("Var", "Val", symT[lhs_val])
    #     addr = addrT[lhs_val]
    #     lhs_val = builder.load(addr)
    # rhs_val = rhs[0]
    # rhs_typ = rhs[1]
    # if rhs_typ == "Var":
    #     rhs_typ = re.sub("Var", "Val", symT[rhs_val])
    #     addr = addrT[rhs_val]
    #     rhs_val = builder.load(addr)

    if rhs_typ == lhs_typ:
        if lhs_typ == "IntVal":
            return (builder.icmp_signed(op,lhs_val,rhs_val), "BoolVal")
        elif lhs_typ == "BoolVal":
            return bop_condition(builder, op, lhs_val, rhs_val)
        else:
            return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")
    else:
        if lhs_typ == "IntVal":
            if rhs_typ == "FloatVal":
                lhs_val = builder.sitofp(lhs_val, ir.FloatType())
                return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")
            elif rhs_typ == "DoubleVal":
                lhs_val = builder.sitofp(lhs_val, ir.DoubleType())
                return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")

        elif rhs_typ == "IntVal":
            if lhs_typ == "FloatVal":
                rhs_val = builder.sitofp(rhs_val, ir.FloatType())
                return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")
            elif lhs_typ == "DoubleVal":
                rhs_val = builder.sitofp(rhs_val, ir.DoubleType())
                return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")
        elif lhs_typ == "FloatVal":
            lhs_val = builder.fpext(lhs_val, ir.DoubleType())
            return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")
        elif rhs_typ == "FloatVal":
            rhs_val = builder.fpext(rhs_val, ir.DoubleType())
            return (builder.fcmp_ordered(op,lhs_val,rhs_val), "BoolVal")


def bop_condition(builder,op,lhs,rhs):
    match op:
        case 'and':
            return (builder.and_(lhs,rhs), "BoolVal")
        case 'or':
            return (builder.or_(lhs,rhs), "BoolVal")

def bop_not(builder, res, symT, addrT):
    res_val = res[0]
    res_typ = res[1]
    if res_typ == "Var":
        res_typ = re.sub("Var", "Val", symT[res_val])
        addr = addrT[res_val]
        res_val = builder.load(addr)
    return (builder.not_(res_val), res_typ)

