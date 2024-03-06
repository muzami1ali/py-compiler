; ModuleID = "forLoopBench"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"i" = alloca double
  store double              0x0, double* %"i"
  %".3" = load double, double* %"i"
  %".4" = fcmp olt double %".3", 0x412e848000000000
  br i1 %".4", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".6" = load double, double* %"i"
  %".7" = sitofp i32 1 to double
  %".8" = fadd double %".6", %".7"
  store double %".8", double* %"i"
  %".10" = load double, double* %"i"
  %".11" = fcmp olt double %".10", 0x412e848000000000
  br i1 %".11", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  %".13" = bitcast [21 x i8]* @"printf_format_0" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  ret i32 0
}

@"printf_format_0" = internal constant [21 x i8] c"Execution completed\0a\00"
declare i32 @"printf"(i8* %".1", ...)
