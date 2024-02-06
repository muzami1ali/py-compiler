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
  %"munch.1" = alloca i32
  store i32 3, i32* %"munch.1"
  %".18" = load i32, i32* %"munch.1"
  %".19" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".18")
  %".21" = load i32, i32* %"munch.1"
  %".22" = sitofp i32 %".21" to double
  %".23" = sitofp i32 3 to double
  %".24" = call double @"pow"(double %".22", double %".23")
  %"munch.2" = alloca double
  store double %".24", double* %"munch.2"
  %".26" = load double, double* %"munch.2"
  %".27" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", double %".26")
  ret i32 0
}

declare double @"pow"(double %".1", double %".2")

declare double @"floor"(double %".1")

@"printf_format_0" = internal constant [4 x i8] c"%f\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%f\0a\00"