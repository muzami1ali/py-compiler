; ModuleID = "calc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = mul i32 3, 4
  %".3" = add i32 2, %".2"
  ret i32 %".3"
}
