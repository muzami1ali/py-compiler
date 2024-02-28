from llvmlite import ir
import llvmlite.binding as llvm

int0 = ir.Constant(ir.IntType(32), 0)
val_typ = ir.IntType(8)
int_typ = ir.IntType(32)
double_typ = ir.DoubleType()
list_struct = ir.LiteralStructType([
                                val_typ.as_pointer(), # pointer array element
                                ir.IntType(32), # length of the list
                                ir.IntType(32), # max length of the list
                                ir.IntType(32) #  factor type of the list
                                ])


def create_list(module):
    # add malloc function
    # fty1 = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(32)])
    # malloc = ir.Function(module, fty1, name="malloc")
    # # add free function
    # fty2 = ir.FunctionType(ir.VoidType(), [ir.IntType(8).as_pointer()])
    # free = ir.Function(module, fty2, name="free")
    # # add memcopy function
    # fty3 = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(8).as_pointer(), ir.IntType(8).as_pointer(), ir.IntType(32)])
    # memcpy = ir.Function(module, fty3, name="memcpy")


    func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer()])
    func = ir.Function(module, func_typ, name="create_list")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg = func.args[0]
    # Initialize
    ptr1 = builder.gep(arg, [int0, int0])
    builder.store(ir.Constant(val_typ.as_pointer(), None), ptr1)

    ptr2 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 1)])
    builder.store(ir.Constant(ir.IntType(32), 0), ptr2)

    ptr3 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 2)])
    builder.store(ir.Constant(ir.IntType(32), 0), ptr3)

    ptr4 = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 3)])
    builder.store(ir.Constant(ir.IntType(32), 0), ptr4)

    builder.ret_void()

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
    builder.store(ir.Constant(val_typ.as_pointer(), None), builder.gep(arg, [int0, int0]))
    builder.branch(free_end)

    builder.position_at_end(free_end)
    builder.ret_void()

def resize_list(module):
    func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32)])
    func = ir.Function(module, func_typ, name="resize_list")
    global resize_func
    resize_func = func
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg1 = func.args[0]
    arg2 = func.args[1]
    # get the length of the list
    output = builder.call(malloc, [arg2])

    ptr1 = builder.gep(arg1, [int0, int0])
    buffer = builder.load(ptr1)

    ptr2 = builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)])
    length = builder.load(ptr2)

    builder.call(memcpy, [output, buffer, length])

    builder.call(free, [buffer])

    builder.store(output, ptr1)

    ptr3 = builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 2)])
    builder.store(arg2, ptr3)
    
    builder.ret_void()

def get_list_length(module):
    func_typ = ir.FunctionType(ir.IntType(32), [list_struct.as_pointer()])
    func = ir.Function(module, func_typ, name="get_list_length")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg = func.args[0]
    ptr = builder.gep(arg, [int0, ir.Constant(ir.IntType(32), 1)])
    length = builder.load(ptr)
    builder.ret(length)

def get_list_element(module):
    func_typ = ir.FunctionType(val_typ, [list_struct.as_pointer(), ir.IntType(32)])
    func = ir.Function(module, func_typ, name="get_list_element")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg1 = func.args[0]
    arg2 = func.args[1]
    ptr1 = builder.gep(arg1, [int0, int0])
    buffer = builder.load(ptr1)
    ptr2 = builder.gep(buffer, [arg2])
    element = builder.load(ptr2)
    builder.ret(element)

def set_list_element(module):
    func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), ir.IntType(32), val_typ])
    func = ir.Function(module, func_typ, name="set_list_element")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    arg1 = func.args[0]
    arg2 = func.args[1]
    arg3 = func.args[2]
    ptr1 = builder.gep(arg1, [int0, int0])
    buffer = builder.load(ptr1)
    ptr2 = builder.gep(buffer, [arg2])
    builder.store(arg3, ptr2)
    builder.ret_void()

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

def append_list(module):
    func_typ = ir.FunctionType(ir.VoidType(), [list_struct.as_pointer(), val_typ])
    func = ir.Function(module, func_typ, name="append_list")
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
    factor = builder.load(builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 3)]))
    sum = builder.add(factor, max_length)
    builder.call(resize_func, [arg1, sum])
    builder.branch(grow_end)
    builder.position_at_end(grow_end)
    buffer = builder.load(builder.gep(arg1, [int0, int0]))
    getLength = builder.load(builder.gep(buffer, [length]))
    builder.store(arg2, builder.gep(buffer, [getLength]))
    updateLength = builder.add(length, ir.Constant(ir.IntType(32), 1))
    builder.store(updateLength, builder.gep(arg1, [int0, ir.Constant(ir.IntType(32), 1)]))



# resize_func = None
module = ir.Module()
fty1 = ir.FunctionType(val_typ.as_pointer(), [ir.IntType(32)])
malloc = ir.Function(module, fty1, name="malloc")
# add free function
fty2 = ir.FunctionType(ir.VoidType(), [val_typ.as_pointer()])
free = ir.Function(module, fty2, name="free")
# add memcopy function
fty3 = ir.FunctionType(val_typ.as_pointer(), [val_typ.as_pointer(), val_typ.as_pointer(), ir.IntType(32)])
memcpy = ir.Function(module, fty3, name="memcpy")
create_list(module)
delete_list(module)
resize_list(module)
append_list(module)
get_list_length(module)
get_list_element(module)
set_list_element(module)
# fty2 = ir.FunctionType(ir.VoidType(), [ir.IntType(32).as_pointer()])
# free = ir.Function(module, fty2, name="free")
print(module)

#
# def create_list():
#     return ir.Constant(list_struct, [ir.Constant(ir.IntType(32).as_pointer(), None), ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
#
# print(create_list())
#
# def append_list(listS, value):
#     # get the length of the list
#     length = listS.elements[1]
#     # get the max length of the list
#     max_length = listS.operands[2]
#     # get the pointer to the array
#     ptr = listS.operands[0]
#     # create a new array with length + 1
#     new_array = ir.Constant(ir.ArrayType(ir.IntType(32), length + 1), [ptr, value])
#     # update the list with the new array
#     listS.operands[0] = new_array
#     # update the length of the list
#     listS.operands[1] = length + 1
#     # update the max length of the list
#     listS.operands[2] = max_length + 1
#     return listS
# print(append_list(create_list(), ir.Constant(ir.IntType(32), 10)))
#
# def append_list(listS, value):

    # # get the length of the list
    # length = list.operands[1]
    # # get the max length of the list
    # max_length = list.operands[2]
    # # get the pointer to the array
    # ptr = list.operands[0]
    # # create a new array with length + 1
    # new_array = ir.Constant(ir.ArrayType(ir.IntType(32), length + 1), [ptr, value])
    # # update the list with the new array
    # list.operands[0] = new_array
    # # update the length of the list
    # list.operands[1] = length + 1
    # # update the max length of the list
    # list.operands[2] = max_length + 1
    # return list


