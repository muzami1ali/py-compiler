; ModuleID = "calc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = mul i32 4, 6
  %".3" = mul i32 %".2", 8
  %".4" = add i32 2, %".3"
  ret i32 %".4"
}
