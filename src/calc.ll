; ModuleID = "calc"
target triple = "<Target aarch64 (AArch64 (little endian))>"
target datalayout = ""

define i32 @"op"()
{
entry:
  %".2" = sub i32 50, 34
  %".3" = mul i32 60, 2
  %".4" = sub i32 %".3", 34
  %".5" = add i32 %".2", %".4"
  %".6" = sub i32 70, 5
  %".7" = add i32 %".5", %".6"
  %".8" = add i32 %".7", 1
  ret i32 %".8"
}

define i32 @"main"()
{
entry:
  %"result" = call i32 @"op"()
  %".2" = bitcast [4 x i8]* @"printf_format" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"result")
  ret i32 0
}

@"printf_format" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
