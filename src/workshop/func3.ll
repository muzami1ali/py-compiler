; ModuleID = "func3"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"test"()
  %".3" = add i32 10, %".2"
  %".4" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  %".6" = call i32 @"test"()
  %".7" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  ret i32 0
}

define i32 @"test"()
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 1, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  ret i32 1
endif_block_0:
  %".6" = load i1, i1* %"ifvar0"
  br i1 %".6", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  ret i32 0
end_else_block_0:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"