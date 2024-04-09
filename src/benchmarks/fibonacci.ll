; ModuleID = "fibonacci"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"fibonacci"(i32 10)
  %".3" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

define i32 @"fibonacci"(i32 %"n")
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".4" = icmp eq i32 %"n", 0
  br i1 %".4", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  ret i32 0
endif_block_0:
  %".8" = icmp eq i32 %"n", 1
  %".9" = load i1, i1* %"ifvar0"
  %".10" = and i1 %".8", %".9"
  br i1 %".10", label %"elif_block_0", label %"end_elif_block_0"
elif_block_0:
  store i1 0, i1* %"ifvar0"
  ret i32 1
end_elif_block_0:
  %".14" = load i1, i1* %"ifvar0"
  br i1 %".14", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".16" = sub i32 %"n", 1
  %".17" = call i32 @"fibonacci"(i32 %".16")
  %".18" = sub i32 %"n", 2
  %".19" = call i32 @"fibonacci"(i32 %".18")
  %".20" = add i32 %".17", %".19"
  ret i32 %".20"
end_else_block_0:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
