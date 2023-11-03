; ModuleID = "calc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"compute_expression"()
{
entry:
  %".2" = add i32 2, 3
  ret i32 %".2"
}
