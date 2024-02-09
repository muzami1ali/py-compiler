; ModuleID = "ifelse1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca float
  store float 0x4008ccccc0000000, float* %"foo"
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 0, label %"if_block_0", label %"endif_block_0"
if_block_0:
  %".5" = add i32 10, 20
  %".6" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  store i1 0, i1* %"ifvar0"
  br label %"endif_block_0"
endif_block_0:
  br i1 0, label %"elif_block_00", label %"end_elif_block_00"
elif_block_00:
  %".11" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 0)
  store i1 0, i1* %"ifvar0"
  br label %"end_elif_block_00"
end_elif_block_00:
  br i1 1, label %"elif_block_01", label %"end_elif_block_01"
elif_block_01:
  %".16" = call i32 @"print_bool"(i1 1)
  store i1 0, i1* %"ifvar0"
  br label %"end_elif_block_01"
end_elif_block_01:
  %".19" = load i1, i1* %"ifvar0"
  br i1 %".19", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".21" = add i32 20, 20
  %".22" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".21")
  br label %"end_else_block_0"
end_else_block_0:
  %"ifvar1" = alloca i1
  store i1 1, i1* %"ifvar1"
  br i1 1, label %"if_block_1", label %"endif_block_1"
if_block_1:
  %".27" = add i32 10, 20
  store i1 0, i1* %"ifvar1"
  br label %"endif_block_1"
endif_block_1:
  %".30" = load i1, i1* %"ifvar1"
  br i1 %".30", label %"else_block_1", label %"end_else_block_1"
else_block_1:
  %".32" = add i32 20, 30
  br label %"end_else_block_1"
end_else_block_1:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
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
@"printf_format_3" = internal constant [4 x i8] c"%d\0a\00"