; ModuleID = "aop2"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca float
  store float 0x4008ccccc0000000, float* %"foo"
  %".3" = load float, float* %"foo"
  %".4" = sitofp i32 20 to float
  %".5" = fpext float %".4" to double
  %".6" = fpext float %".3" to double
  %".7" = call double @"pow"(double %".5", double %".6")
  %".8" = sitofp i32 20 to double
  %".9" = fdiv double %".7", %".8"
  %".10" = call double @"floor"(double %".9")
  %".11" = sitofp i32 10 to double
  %".12" = fadd double %".11", %".10"
  %"munch" = alloca double
  store double %".12", double* %"munch"
  %".14" = load double, double* %"munch"
  %".15" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", double %".14")
  ret i32 0
}

declare double @"pow"(double %".1", double %".2")

declare double @"floor"(double %".1")

@"printf_format_0" = internal constant [4 x i8] c"%f\0a\00"
declare i32 @"printf"(i8* %".1", ...)
