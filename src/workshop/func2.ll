; ModuleID = "func2"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  call void @"recur"(i32 0)
  ret i32 0
}

define void @"recur"(i32 %"n")
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".4" = icmp slt i32 %"n", 10
  br i1 %".4", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".7" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"n")
  %".9" = add i32 %"n", 1
  call void @"recur"(i32 %".9")
  br label %"endif_block_0"
endif_block_0:
  %".12" = load i1, i1* %"ifvar0"
  br i1 %".12", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".14" = call i32 @"print_bool"(i1 0)
  br label %"end_else_block_0"
end_else_block_0:
  ret void
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

define i32 @"print_bool"(i1 %".1")
{
entry:
  br i1 %".1", label %"print_bool_if", label %"print_bool_else"
print_bool_if:
  %".4" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  br label %"print_bool_endif"
print_bool_else:
  %".7" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  br label %"print_bool_endif"
print_bool_endif:
  ret i32 0
}

@"printf_format_True" = internal constant [6 x i8] c"True\0a\00"
@"printf_format_False" = internal constant [7 x i8] c"False\0a\00"