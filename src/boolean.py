from llvmlite import ir


def bop(op,lhs,rhs,builder,symT,addrT):
    lhs_val = lhs[0]
    lhs_typ = lhs[1]
    if lhs_typ == "Var":
        lhs_typ = re.sub("Var", "Val", symT[lhs_val])
        addr = addrT[lhs_val]
        lhs_val = builder.load(addr)
    rhs_val = rhs[0]
    rhs_typ = rhs[1]
    if rhs_typ == "Var":
        rhs_typ = re.sub("Var", "Val", symT[rhs_val])
        addr = addrT[rhs_val]
        rhs_val = builder.load(addr)

    if rhs_typ == lhs_typ:
        if lhs_typ == "IntVal":
            return (builder.icmp_signed(op,lhs_val,rhs_val), "BoolVal")
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


