from numba import jit

@jit
def my_function():
    lst = []
    lst.append(1)
    lst.append(2)
    lst.append(3)
    # return x * 2

# Compile the function
# my_function(10)
my_function()

# Get LLVM IR
llvm_ir = my_function.inspect_llvm()
print(llvm_ir)

