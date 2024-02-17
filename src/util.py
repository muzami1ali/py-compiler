# Ref:Numba
from llvmlite import ir

int1_t = ir.IntType(1)
int8_t = ir.IntType(8)
int32_t = ir.IntType(32)
voidptr_t = int8_t.as_pointer()
true = ir.Constant(ir.IntType(1), 1)
false = ir.Constant(ir.IntType(1), 0)


def make_bytearray(buf):
    """
    Make a byte array constant from *buf*.
    """
    b = bytearray(buf)
    n = len(b)
    return ir.Constant(ir.ArrayType(ir.IntType(8), n), b)


def global_constant(builder_or_module, name, value, linkage='internal'):
    """
    Get or create a (LLVM module-)global constant with *name* or *value*.
    """
    if isinstance(builder_or_module, ir.Module):
        module = builder_or_module
    else:
        module = builder_or_module.module
    data = ir.GlobalVariable(module=module,typ=value.type,name=name)
    data.linkage = linkage
    data.global_constant = True
    data.initializer = value
    return data


def printf(builder, format, num, *args):
    """
    Calls printf().
    Argument `format` is expected to be a Python string.
    Values to be printed are listed in `args`.

    Note: There is no checking to ensure there is correct number of values
    in `args` and there type matches the declaration in the format string.
    """
    assert isinstance(format, str)
    mod = builder.module
    # Make global constant for format string
    cstring = voidptr_t
    fmt_bytes = make_bytearray((format + '\00').encode('ascii'))
    global_fmt = global_constant(mod, f"printf_format_{num}", fmt_bytes)
    fnty = ir.FunctionType(int32_t, [cstring], var_arg=True)
    # Insert printf()
    try:
        fn = mod.get_global("printf")
    except KeyError:
        fn = ir.Function(mod, fnty, name="printf")
    # Call
    ptr_fmt = builder.bitcast(global_fmt, cstring)
    return builder.call(fn, [ptr_fmt] + list(args))


def print_func(builder, num, func_param, address_table):
    i = func_param[0]
    typ = i[1]
    if typ=="IntVal":
        printf(builder, "%d\n", num, i[0])
    elif typ=="FloatVal":
        res = builder.fpext(i[0], ir.DoubleType())
        printf(builder, "%f\n", num, res)
    elif typ=="DoubleVal":
        printf(builder, "%f\n", num, i[0])
    elif typ=="BoolVal":
        print_bool(builder, i[0])
    elif typ=="Var":
        printVar(builder, num, i[0], address_table)
        
typ_lst = ["IntVar", "FloatVar", "DoubleVar", "BoolVar"]
def printVar(builder, num, var, address_table):
        size = len(typ_lst)
        typ_var = f"{var}-type"
        for i in range(size):
            typ = typ_lst[i]
            try:
                var_addr = address_table[(var,typ)]
                typ_var_addr = address_table[(typ_var,"TypeVar")]
                check_typ_block = builder.append_basic_block(name=f"check_typ_block_{var}_{typ}")
                end_check_typ_block = builder.append_basic_block(name=f"end_check_typ_block_{var}_{typ}")
                typ_var_val = builder.load(typ_var_addr)
                comp = ir.Constant(ir.IntType(2), i)
                pred = builder.icmp_unsigned("==",comp,typ_var_val)
                builder.cbranch(pred,check_typ_block,end_check_typ_block)
                builder.position_at_start(check_typ_block)
                if typ=="IntVar":
                    res = builder.load(var_addr)
                    printf(builder, "%d\n", int(f"{i}{num}"), res)
                elif typ=="FloatVar":
                    res = builder.load(var_addr)
                    res1 = builder.fpext(res, ir.DoubleType())
                    printf(builder, "%f\n",  int(f"{i}{num}"), res1)
                elif typ=="DoubleVar":
                    res = builder.load(var_addr)
                    printf(builder, "%f\n",  int(f"{i}{num}"), res)
                elif typ=="BoolVar":
                    res = builder.load(var_addr)
                    print_bool(builder, res)
                builder.branch(end_check_typ_block)
                builder.position_at_start(end_check_typ_block)
            except KeyError:
                pass

                


def printb(builder, format):
    assert isinstance(format, str)
    mod = builder.module
    # Make global constant for format string
    cstring = voidptr_t
    try:
        global_fmt = mod.get_global(f"printf_format_{format}")
    except KeyError:
        fmt_bytes = make_bytearray((format + '\n\00').encode('ascii'))
        global_fmt = global_constant(mod, f"printf_format_{format}", fmt_bytes)
    fnty = ir.FunctionType(int32_t, [cstring], var_arg=True)
    # Insert printf()
    try:
        fn = mod.get_global("printf")
    except KeyError:
        fn = ir.Function(mod, fnty, name="printf")
    # Call
    ptr_fmt = builder.bitcast(global_fmt, cstring)
    return builder.call(fn, [ptr_fmt])

def print_bool(sbuilder, res):
    mod = sbuilder.module
  
    func_typ = ir.FunctionType(int32_t, [int1_t])

    try:
        func = mod.get_global("print_bool")
    except KeyError:
        func = ir.Function(mod, func_typ, name="print_bool")
        val = func.args
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        true_block = func.append_basic_block(f"print_bool_if")
        false_block = func.append_basic_block(f"print_bool_else")
        end_block = func.append_basic_block(f"print_bool_endif")
        builder.cbranch(val[0],true_block,false_block)
        builder.position_at_start(true_block)
        printb(builder, "True")
        builder.branch(end_block)
        builder.position_at_start(false_block)
        printb(builder, "False")
        builder.branch(end_block)
        builder.position_at_start(end_block)
        builder.ret(ir.Constant(int32_t, 0))

    return sbuilder.call(func,[res])



    



