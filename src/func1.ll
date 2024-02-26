; ModuleID = "func1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca float
  store float 0x4024000000000000, float* %"foo"
  %".3" = load float, float* %"foo"
  %".4" = fpext float %".3" to double
  %".5" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", double %".4")
  call void @"test"()
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%f\0a\00"
declare i32 @"printf"(i8* %".1", ...)

define void @"test"()
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".3" = load i32, i32* %"i"
  %".4" = icmp slt i32 %".3", 10
  br i1 %".4", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".6" = load i32, i32* %"i"
  %".7" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  %".9" = load i32, i32* %"i"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"i"
  %".12" = load i32, i32* %"i"
  %".13" = icmp slt i32 %".12", 10
  br i1 %".13", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  %".15" = call i32 @"print_bool"(i1 1)
  ret void
}

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