; ModuleID = "test"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"barc" = alloca i32
  store i32 102, i32* %"barc"
  %"marc" = alloca float
  store float 0x405a23d700000000, float* %"marc"
  %"larc" = alloca i1
  store i1 0, i1* %"larc"
  %".5" = load i32, i32* %"barc"
  %".6" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  %".8" = load float, float* %"marc"
  %".9" = fpext float %".8" to double
  %".10" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", double %".9")
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%f\0a\00"