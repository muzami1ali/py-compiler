; ModuleID = "calc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"compute_expression"()
{
entry:
  %".2" = add i32 2, 3
  %".3" = mul i32 %".2", 4
  %".4" = udiv i32 %".3", 2
  ret i32 %".4"
}
