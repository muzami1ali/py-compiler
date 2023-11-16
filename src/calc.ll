; ModuleID = "calc"
target triple = "<Target aarch64 (AArch64 (little endian))>"
target datalayout = ""

define i32 @"op"()
{
entry:
  %".2" = mul i32 4, 6
  %".3" = mul i32 %".2", 8
  %".4" = add i32 2, %".3"
  ret i32 %".4"
}

define i32 @"main"()
{
entry:
  %"result" = call i32 @"op"()
  %".2" = bitcast [3 x i8]* @"printf_format" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"result")
  ret i32 0
}

@"printf_format" = internal constant [3 x i8] c"%d\00"
declare i32 @"printf"(i8* %".1", ...)
