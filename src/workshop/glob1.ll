; ModuleID = "glob1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"ifvar0" = alloca i1
  %"foo" = alloca i32
  store i1 1, i1* %"ifvar0"
  br i1 1, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  store i32 42, i32* %"foo"
  br label %"endif_block_0"
endif_block_0:
  %".7" = load i1, i1* %"ifvar0"
  br i1 %".7", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  store i32 0, i32* %"foo"
  br label %"end_else_block_0"
end_else_block_0:
  %".11" = load i32, i32* %"foo"
  %".12" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".11")
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
