; ModuleID = "mandelbrot"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"i" = alloca double
  store double              0x0, double* %"i"
  %".3" = load double, double* %"i"
  %".4" = fcmp olt double %".3", 0x4024000000000000
  br i1 %".4", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".6" = load double, double* %"i"
  %".7" = load double, double* %"i"
  %".8" = call double @"z"(double %".7", double 0x3ff0000000000000)
  %".9" = bitcast [12 x i8]* @"printf_format_0" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", double %".6", double %".8")
  %".11" = load double, double* %"i"
  %".12" = fadd double %".11", 0x3ff0000000000000
  store double %".12", double* %"i"
  %".14" = load double, double* %"i"
  %".15" = fcmp olt double %".14", 0x4024000000000000
  br i1 %".15", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  ret i32 0
}

define double @"z"(double %"n", double %"ci")
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".5" = fcmp oeq double %"n",              0x0
  br i1 %".5", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  ret double              0x0
endif_block_0:
  %".9" = load i1, i1* %"ifvar0"
  br i1 %".9", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".11" = fsub double %"n", 0x3ff0000000000000
  %".12" = call double @"z"(double %".11", double %"ci")
  %".13" = call double @"pow"(double %".12", double 0x4000000000000000)
  %".14" = fadd double %".13", %"ci"
  ret double %".14"
end_else_block_0:
  ret double              0x0
}

declare double @"pow"(double %".1", double %".2")

@"printf_format_0" = internal constant [12 x i8] c"z(%f) = %f\0a\00"
declare i32 @"printf"(i8* %".1", ...)
