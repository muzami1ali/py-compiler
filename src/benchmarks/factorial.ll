; ModuleID = "factorial"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"factorial"(i32 5)
  %".3" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

define i32 @"factorial"(i32 %"n")
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".4" = icmp eq i32 %"n", 0
  br i1 %".4", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  ret i32 1
endif_block_0:
  %".8" = load i1, i1* %"ifvar0"
  br i1 %".8", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".10" = sub i32 %"n", 1
  %".11" = call i32 @"factorial"(i32 %".10")
  %".12" = mul i32 %"n", %".11"
  ret i32 %".12"
end_else_block_0:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
