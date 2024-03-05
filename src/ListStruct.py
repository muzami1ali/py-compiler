from llvmlite import ir
import llvmlite.binding as llvm
from util import printf

int0 = ir.Constant(ir.IntType(32), 0)
val_typ = ir.IntType(8)
int_typ = ir.IntType(32)
double_typ = ir.DoubleType()
list_struct = ir.LiteralStructType([
                                val_typ.as_pointer(), # pointer array element
                                ir.IntType(32), # length of the list
                                ir.IntType(32), # max length of the list
                                ir.IntType(32) #  Number of elements
                                ])


def create_list(module):
    try:
        func = module.get_global("create_list")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer()])
        func = ir.Function(module, func_typ, name="create_list")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg = func.args[0]
        # Initialize
        ptr1 = builder.gep(arg, [int0, int0])
        builder.store(ir.Constant(ir.IntType(8).as_pointer(), None), ptr1)

        ptr2 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 1)])
        builder.store(ir.Constant(ir.IntType(32), 0), ptr2)

        ptr3 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 2)])
        builder.store(ir.Constant(ir.IntType(32), 0), ptr3)

        ptr4 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 3)])
        builder.store(ir.Constant(ir.IntType(32), 0), ptr4)

        builder.ret_void()
    return func

def delete_list(module):
    func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer()])
    func = ir.Function(module, func_typ, name="delete_list")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg = func.args[0]
    # get the pointer to the array
    ptr = builder.load(builder.gep(arg, [int0, int0]))
    # free the array
    pred = builder.icmp_unsigned("!=", ptr, ir.Constant(val_typ.as_pointer(), None))
    free_begin = builder.append_basic_block("free_begin")
    free_end = builder.append_basic_block("free_end")
    builder.cbranch(pred, free_begin, free_end)

    builder.position_at_end(free_begin)
    builder.call(free, [ptr])
    builder.store(ir.Constant(ir.IntType(8).as_pointer(), None), builder.gep(arg, [int0, int0]))
    builder.branch(free_end)

    builder.position_at_end(free_end)
    builder.ret_void()

def resize_list(module):
    try:
        func = module.get_global("resize_list")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="resize_list")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]

        new_mem_block = builder.call(get_malloc(module), [arg2])

        ptr1 = builder.gep(arg1, [int0, int0])
        buffer = builder.load(ptr1)

        ptr2 = builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)])
        length = builder.load(ptr2)

        builder.call(get_memcpy(module), [new_mem_block, buffer, length])

        builder.call(get_free(module), [buffer])

        builder.store(new_mem_block, ptr1)

        ptr3 = builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 2)])
        builder.store(arg2, ptr3)
        
        builder.ret_void()
    return func

# def get_list_length(module):
#     func_typ = ir.FunctionType(ir.IntType(32), [list_struct.as_pointer()])
#     func = ir.Function(module, func_typ, name="get_list_length")
#     block = func.append_basic_block(name="entry")
#     builder = ir.IRBuilder(block)
#     arg = func.args[0]
#     ptr = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 3)])
#     length = builder.load(ptr)
#     builder.ret(length)





# def remove_list_element(module):
#     func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32)])
#     func = ir.Function(module, func_typ, name="remove_list_element")
#     block = func.append_basic_block(name="entry")
#     builder = ir.IRBuilder(block)
#     arg1 = func.args[0]
#     arg2 = func.args[1]
#     ptr1 = builder.gep(arg1, [int0, int0])
#     buffer = builder.load(ptr1)
#     ptr2 = builder.gep(buffer, [arg2])
#     builder.store(ir.Constant(val_typ, 0), ptr2)
#     builder.ret_void()

def append_char_list(module,):
    try:
        func = module.get_global("append_char_list")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(8)])
        func = ir.Function(module, func_typ, name="append_char_list")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        # get the length of the list
        length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))
        # get the max length of the list
        max_length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 2)]))

        grow_begin = builder.append_basic_block("grow_begin")
        grow_end = builder.append_basic_block("grow_end")
        pred = builder.icmp_unsigned("==", length, max_length)
        builder.cbranch(pred, grow_begin, grow_end)
        builder.position_at_end(grow_begin)
        # factor = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))
        factor = ir.Constant(ir.IntType(32), 1)
        sum = builder.add(factor, max_length)
        builder.call(resize_list(module), [arg1, sum])
        builder.branch(grow_end)
        builder.position_at_end(grow_end)
        buffer = builder.load(builder.gep(arg1, [int0, int0]))
        getLength = builder.load(builder.gep(buffer, [length]))
        builder.store(arg2, builder.gep(buffer, [getLength]))
        updateLength = builder.add(length, ir.Constant(ir.IntType(32), 1))
        builder.store(updateLength, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))
        builder.ret_void()
    return func

def get_malloc(module):
    try:
        malloc = module.get_global("malloc")
    except KeyError:
        fty1 = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(32)])
        malloc = ir.Function(module, fty1, name="malloc")
    return malloc

def get_exit(module):
    try:
        func = module.get_global("exit")
    except KeyError:
        fty1 = ir.FunctionType(ir.VoidType(), [ir.IntType(32)])
        func = ir.Function(module, fty1, name="exit")
    return func
    
def get_free(module):
    try:
        free = module.get_global("free")
    except KeyError:
        fty2 = ir.FunctionType(ir.VoidType(), [ir.IntType(8).as_pointer()])
        free = ir.Function(module, fty2, name="free")
    return free

def get_memcpy(module):
    try:
        memcpy = module.get_global("memcpy")
    except KeyError:
        fty3 = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(8).as_pointer(), ir.IntType(8).as_pointer(), ir.IntType(32)])
        memcpy = ir.Function(module, fty3, name="memcpy")
    return memcpy

def append_int_list(module):
    try:
        func = module.get_global("append_int_list")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="append_int_list")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        # get the length of the list
        length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))
        # get the max length of the list
        max_length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 2)]))

        grow_begin = builder.append_basic_block("grow_begin")
        grow_end = builder.append_basic_block("grow_end")
        pred = builder.icmp_unsigned("==", length, max_length)
        builder.cbranch(pred, grow_begin, grow_end)
        builder.position_at_end(grow_begin)
        # factor = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))
        factor = ir.Constant(ir.IntType(32), 4)
        sum = builder.add(factor, max_length)
        builder.call(resize_list(module), [arg1, sum])
        builder.branch(grow_end)

        builder.position_at_end(grow_end)

        buffer_i8 = builder.load(builder.gep(arg1, [int0, int0]))
        buffer_i32 = builder.bitcast(buffer_i8, ir.IntType(32).as_pointer())
        index =  builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))

        builder.store(arg2, builder.gep(buffer_i32, [index]))

        updateLength = builder.add(length, factor)
        builder.store(updateLength, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))

        new_index = builder.add(index, ir.Constant(ir.IntType(32),1))
        builder.store(new_index, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))
        builder.ret_void()
    return func

def append_double_list(module):
    try:
        func = module.get_global("append_double_list")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.DoubleType()])
        func = ir.Function(module, func_typ, name="append_double_list")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        # get the length of the list
        length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))
        # get the max length of the list
        max_length = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 2)]))

        grow_begin = builder.append_basic_block("grow_begin")
        grow_end = builder.append_basic_block("grow_end")
        pred = builder.icmp_unsigned("==", length, max_length)
        builder.cbranch(pred, grow_begin, grow_end)
        builder.position_at_end(grow_begin)
        # factor = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))
        factor = ir.Constant(ir.IntType(32), 8)
        sum = builder.add(factor, max_length)
        builder.call(resize_list(module), [arg1, sum])
        builder.branch(grow_end)

        builder.position_at_end(grow_end)
        index =  builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))

        buffer_i8 = builder.load(builder.gep(arg1, [int0, int0]))
        buffer_double = builder.bitcast(buffer_i8, ir.DoubleType().as_pointer())

        builder.store(arg2, builder.gep(buffer_double, [index]))
        # #
        updateLength = builder.add(length, factor)
        updateIndex = builder.add(index, ir.Constant(ir.IntType(32),1))
        builder.store(updateLength, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))
        builder.store(updateIndex, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))

        builder.ret_void()

    return func

"""Setter functions"""

def set_char_list_element(module):
    try:
        func = module.get_global("set_char_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32), ir.IntType(8)])
        func = ir.Function(module, func_typ, name="set_char_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1] #index
        arg3 = func.args[2] #val
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        ptr2 = builder.gep(buffer_i8, [arg2])
        builder.store(arg3, ptr2)
        builder.ret_void()
    return func

def set_int_list_element(module):
    try:
        func = module.get_global("set_int_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="set_int_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1] #index
        arg3 = func.args[2] #val
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        buffer_i32 = builder.bitcast(buffer_i8, ir.IntType(32).as_pointer())
        ptr2 = builder.gep(buffer_i32, [arg2])
        builder.store(arg3, ptr2)
        builder.ret_void()
    return func

def set_double_list_element(module):
    try:
        func = module.get_global("set_double_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32), ir.DoubleType()])
        func = ir.Function(module, func_typ, name="set_double_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1] #index
        arg3 = func.args[2] #val
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        buffer_double = builder.bitcast(buffer_i8, ir.DoubleType().as_pointer())
        ptr2 = builder.gep(buffer_double, [arg2])
        builder.store(arg3, ptr2)
        builder.ret_void()
    return func

def check_index_out_of_bound(module):
    try:
        func = module.get_global("check_index_out_of_bound")
    except KeyError:
        func_typ = ir.FunctionType(ir.VoidType(), [ir.IntType(32), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="check_index_out_of_bound")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        pred = builder.icmp_signed(">", arg1, arg2)
        with builder.if_then(pred):
            printf(builder, "Index out of bound\n", "index_error")
            builder.call(get_exit(module), [ir.Constant(ir.IntType(32), 1)])
            builder.ret_void()
        builder.ret_void()
    return func

def get_max_index(module):
    try:
        func = module.get_global("get_max_index")
    except KeyError:
        func_typ = ir.FunctionType(ir.IntType(32), [list_struct.as_pointer()])
        func = ir.Function(module, func_typ, name="get_max_index")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg = func.args[0]
        ptr = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 3)])
        length = builder.load(ptr)
        max_index = builder.sub(length, ir.Constant(ir.IntType(32), 1))
        builder.ret(max_index)
    return func


"""Getter functions"""

def get_char_list_element(module):
    try:
        func = module.get_global("get_char_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.IntType(8), [list_struct.as_pointer(), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="get_char_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        ptr2 = builder.gep(buffer_i8, [arg2])
        val = builder.load(ptr2)
        builder.ret(val)
    return func

def get_int_list_element(module):
    try:
        func = module.get_global("get_int_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.IntType(32), [list_struct.as_pointer(), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="get_int_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        buffer_i32 = builder.bitcast(buffer_i8, ir.IntType(32).as_pointer())
        ptr2 = builder.gep(buffer_i32, [arg2])
        val = builder.load(ptr2)
        builder.ret(val)
    return func

def get_double_list_element(module):
    try:
        func = module.get_global("get_double_list_element")
    except KeyError:
        func_typ = ir.FunctionType(ir.DoubleType(), [list_struct.as_pointer(), ir.IntType(32)])
        func = ir.Function(module, func_typ, name="get_double_list_element")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg1 = func.args[0]
        arg2 = func.args[1]
        max_index = builder.call(get_max_index(module), [arg1])
        builder.call(check_index_out_of_bound(module), [arg2, max_index])
        ptr1 = builder.gep(arg1, [int0, int0])
        buffer_i8 = builder.load(ptr1)
        buffer_double = builder.bitcast(buffer_i8, ir.DoubleType().as_pointer())
        ptr2 = builder.gep(buffer_double, [arg2])
        val = builder.load(ptr2)
        builder.ret(val)
    return func

def get_list_length(module):
    try:
        func = module.get_global("get_list_length")
    except KeyError:
        func_typ = ir.FunctionType(ir.IntType(32), [list_struct.as_pointer()])
        func = ir.Function(module, func_typ, name="get_list_length")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        arg = func.args[0]
        ptr = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 3)])
        length = builder.load(ptr)
        builder.ret(length)
    return func

# resize_func = None
# module = ir.Module()
# fty1 = ir.FunctionType(val_typ.as_pointer(), [ir.IntType(32)])
# malloc = ir.Function(module, fty1, name="malloc")
# add free function
# fty2 = ir.FunctionType(ir.VoidType(), [val_typ.as_pointer()])
# free = ir.Function(module, fty2, name="free")
# add memcopy function
# fty3 = ir.FunctionType(val_typ.as_pointer(), [val_typ.as_pointer(), val_typ.as_pointer(), ir.IntType(32)])
# memcpy = ir.Function(module, fty3, name="memcpy")
# create_list(module)
# delete_list(module)
# resize_list(module)
# append_list(module)
# get_list_length(module)
# get_list_element(module)
# set_list_element(module)
# fty2 = ir.FunctionType(ir.VoidType(), [ir.IntType(32).as_pointer()])
# free = ir.Function(module, fty2, name="free")
# print(module)

