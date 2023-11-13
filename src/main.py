# import sys
# from llvmlite import binding

# def main(argv):
#     binding.initialize_all_targets()
#     binding.initialize_native_target()
#     binding.initialize_native_asmparser()
#     binding.initialize_native_asmprinter()

#     targetTriple = binding.get_default_triple()
#     target =

# if __name__ == '__main__':
#     main(sys.argv)


import llvmlite.binding as llvm

def main():
  llvm.initialize()
  llvm.initialize_native_target()
  llvm.initialize_native_asmprinter()

  llvm_ir = """
    ; ModuleID = "examples/ir_fpadd.py"
    target triple = "unknown-unknown-unknown"
    target datalayout = ""

    define double @"fpadd"(double %".1", double %".2")
    {
    entry:
      %"res" = fadd double %".1", %".2"
      ret double %"res"
    }
    """
  target = llvm.Target.from_default_triple()
  target_machine = target.create_target_machine()

if __name__ == '__main__':
  main()