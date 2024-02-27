import llvmlite.ir as ir
import llvmlite.binding as llvm

# Initialize LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Create a module
module = ir.Module(name="test_module")
module.triple = llvm.get_default_triple()

# Define the function type: no arguments and returns an integer
func_ty = ir.FunctionType(ir.IntType(32), [])

# Create the function
func = ir.Function(module, func_ty, name="test")

# Create basic blocks
entry_block = func.append_basic_block('entry')
true_block = func.append_basic_block('true')
false_block = func.append_basic_block('false')

# Create a builder and position at the end of entry block
builder = ir.IRBuilder(entry_block)

# Compare (this is trivial as the condition is always True)
cond = ir.Constant(ir.IntType(1), 1) # True
builder.cbranch(cond, true_block, false_block)

# True block
builder.position_at_end(true_block)
builder.ret(ir.Constant(ir.IntType(32), 0))

# False block
builder.position_at_end(false_block)
builder.ret(ir.Constant(ir.IntType(32), 1))

# Print the module
print(module)

