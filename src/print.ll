; ModuleID = "print"
target triple = "<Target aarch64 (AArch64 (little endian))>"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = bitcast [3 x i8]* @"printf_format" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 25)
  ret i32 0
}

@"printf_format" = internal constant [3 x i8] c"%d\00"
declare i32 @"printf"(i8* %".1", ...)
