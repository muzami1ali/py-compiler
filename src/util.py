# Ref:Numba
from llvmlite import ir
import llvmlite.binding as llvm

int8_t = ir.IntType(8)
int32 = ir.IntType(32)
int32_t = ir.IntType(32)

voidptr_t = int8_t.as_pointer()

# def main():
#     llvm.initialize()
#     llvm.initialize_native_target()
#     llvm.initialize_native_asmprinter()
#     target = llvm.Target.from_default_triple()
#     module = ir.Module(name="print")
#     module.triple = target
#     func_type = ir.FunctionType(int32,[])
#     func = ir.Function(module,func_type,name="main")
#     block = func.append_basic_block(name="entry")
#     builder = ir.IRBuilder(block)
#     printf(builder,"%d", ir.Constant(ir.IntType(32),int(25)))
#     builder.ret(ir.Constant(ir.IntType(32),int(0)))
#     f = open("print.ll", "w")
#     f.write(str(module))
#     f.close()
#     print(module)

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
    # module.add_global(data)
    # print(module.global_values)
    # data = module.add_global_variable(value.type, name=name)
    data.linkage = linkage
    data.global_constant = True
    data.initializer = value
    return data

def printf(builder, format, *args):
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
    global_fmt = global_constant(mod, "printf_format", fmt_bytes)
    fnty = ir.FunctionType(int32_t, [cstring], var_arg=True)
    # Insert printf()
    # try:
    #     fn = mod.get_global('printf')
    # except KeyError:
    fn = ir.Function(mod, fnty, name="printf")
    # Call
    ptr_fmt = builder.bitcast(global_fmt, cstring)
    return builder.call(fn, [ptr_fmt] + list(args))

# if __name__=="__main__": 
#     main() 