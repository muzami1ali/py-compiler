from llvmlite import ir
import re

# This function is used to get the result of a power operation
def pow(builder, lhs, rhs):
    double = ir.DoubleType()
    mod = builder.module
    func_ty = ir.FunctionType(double,[double,double])

    # If the function is not already defined, define it
    try:
        func = mod.get_global("pow")
    except KeyError:
        func = ir.Function(mod, func_ty, name="pow")

    return builder.call(func, [lhs,rhs])

# This function is used to get the floor of a double value
def floor(builder, val):
    double = ir.DoubleType()
    mod = builder.module
    func_ty = ir.FunctionType(double,[double])

    # If the function is not already defined, define it
    try:
        func = mod.get_global("floor")
    except KeyError:
        func = ir.Function(mod, func_ty, name="floor")

    return builder.call(func,[val])

# Integer operations
def int_op(op,lhs,rhs,builder):
     match op:
        case "+":
            return (builder.add(lhs,rhs), "IntVal")
        case "-":
            return (builder.sub(lhs,rhs), "IntVal")
        case "/":
            lhs = builder.sitofp(lhs, ir.DoubleType())
            rhs = builder.sitofp(rhs, ir.DoubleType())
            return (builder.fdiv(lhs,rhs),"DoubleVal")
        case "*":
            return (builder.mul(lhs,rhs), "IntVal")
        case "%":
            return (builder.srem(lhs,rhs), "IntVal")
        case "//":
            return (builder.sdiv(lhs,rhs), "IntVal")
        case "**":
            lhs = builder.sitofp(lhs, ir.DoubleType())
            rhs = builder.sitofp(rhs, ir.DoubleType())
            return (pow(builder,lhs,rhs), "DoubleVal")


# Double operations
def double_op(op,lhs,rhs,builder):
     match op:
        case "+":
            return (builder.fadd(lhs,rhs), "DoubleVal")
        case "-":
            return (builder.fsub(lhs,rhs), "DoubleVal")
        case "/":
            return (builder.fdiv(lhs,rhs), "DoubleVal")
        case "*":
            return (builder.fmul(lhs,rhs), "DoubleVal")
        case "%":
            return (builder.frem(lhs,rhs), "DoubleVal")
        case "//":
            res = builder.fdiv(lhs,rhs)
            return (floor(builder,res), "DoubleVal" )
        case "**":
            return (pow(builder,lhs,rhs), "DoubleVal")

# If typ is Var, get the value of the variable or argument
# else just return var(This here is the actual value) and typ
def getVarVal(var, typ, symT, addrT, builder):
    if typ == "Var":
        try:
            var_typ = symT[var]
        except KeyError:
            raise SystemExit(f"Variable {var} not declared")
        param  = len(re.findall("Arg",var_typ))
        if param:
            typ = re.sub("Arg", "Val", var_typ)
            var = addrT[var]
        else:
            typ = re.sub("Var", "Val", var_typ)
            addr = addrT[var]
            var = builder.load(addr)
    return (var,typ)

# This function is used to perform arithmetic operations
def aop(op,lhs,rhs,builder,symT,addrT):
    lhs_val, lhs_typ = getVarVal(lhs[0],lhs[1],symT,addrT,builder)
    rhs_val, rhs_typ = getVarVal(rhs[0],rhs[1],symT,addrT,builder)

    if rhs_typ == lhs_typ:
        if lhs_typ == "IntVal":
            return int_op(op,lhs_val,rhs_val,builder)
        elif lhs_typ == "DoubleVal":
            return double_op(op,lhs_val,rhs_val,builder)
    else:
        if lhs_typ == "IntVal":
            if rhs_typ == "DoubleVal":
                lhs_val = builder.sitofp(lhs_val, ir.DoubleType())
                return double_op(op,lhs_val,rhs_val,builder)
            else:
                raise SystemExit(f"Invalid operation between {lhs_typ} and {rhs_typ}")
        elif rhs_typ == "IntVal":
            if lhs_typ == "DoubleVal":
                rhs_val = builder.sitofp(rhs_val, ir.DoubleType())
                return double_op(op,lhs_val,rhs_val,builder)
            else:
                raise SystemExit(f"Invalid operation between {lhs_typ} and {rhs_typ}")


