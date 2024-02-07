# Ref:Numba
from llvmlite import ir


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


def print_func(builder, num, func_param):
    i = func_param[0]
    typ = i[1]
    if typ=="IntVar":
        res = builder.load(i[0])
        printf(builder, "%d\n", num, res)
    elif typ=="FloatVar":
        res = builder.load(i[0])
        res1 = builder.fpext(res, ir.DoubleType())
        printf(builder, "%f\n", num, res1)
    elif typ=="DoubleVar":
        res = builder.load(i[0])
        printf(builder, "%f\n", num, res)
    elif typ=="BoolVar":
        res = builder.load(i[0])
        print_bool(builder, num, res)
        # return num
    elif typ=="IntVal":
        printf(builder, "%d\n", num, i[0])
    elif typ=="FloatVal":
        res = builder.fpext(i[0], ir.DoubleType())
        printf(builder, "%f\n", num, res)
    elif typ=="DoubleVal":
        printf(builder, "%f\n", num, i[0])
    elif typ=="BoolVal":
        print_bool(builder, num, i[0])
        # return num
    # return (num + 1)


def print_bool(builder, num, val):
    true_block = builder.append_basic_block(f"print_bool_if_{num}")
    false_block = builder.append_basic_block(f"print_bool_else_{num}")
    end_block = builder.append_basic_block(f"print_bool_endif_{num}")
    builder.cbranch(val,true_block,false_block)
    builder.position_at_start(true_block)
    printb(builder, "True")
    builder.branch(end_block)
    builder.position_at_start(false_block)
    printb(builder, "False")
    builder.branch(end_block)
    builder.position_at_start(end_block)


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


