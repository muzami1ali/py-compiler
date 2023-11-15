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

declare i32 @"put"(i8* nocapture %".1") nounwind

define i32 @"main"()
{
entry:
  %"result" = call i32 @"op"()
  %".2" = bitcast i32 %"result" to i8*
  %".3" = call i32 @"put"(i8* %".2")
  ret i32 0
}
