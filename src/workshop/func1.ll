; ModuleID = "func1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca double
  store double 0x4024000000000000, double* %"foo"
  %".3" = load double, double* %"foo"
  %".4" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", double %".3")
  %".6" = sitofp i32 2 to double
  %".7" = call double @"pow"(double 0x4034800000000000, double %".6")
  %".8" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", double %".7")
  call void @"test"(i32 10)
  call void @"test"(i32 20)
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%f\0a\00"
declare i32 @"printf"(i8* %".1", ...)

declare double @"pow"(double %".1", double %".2")

@"printf_format_1" = internal constant [4 x i8] c"%f\0a\00"
define void @"test"(i32 %"wow")
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".4" = add i32 %"wow", 10
  %"baz" = alloca i32
  store i32 %".4", i32* %"baz"
  %".6" = load i32, i32* %"baz"
  %".7" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".10" = icmp eq i32 %"wow", 10
  br i1 %".10", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".13" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 100000000)
  br label %"endif_block_0"
endif_block_0:
  %".16" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %"wow")
  %".18" = load i32, i32* %"i"
  %".19" = icmp slt i32 %".18", 10
  br i1 %".19", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".21" = load i32, i32* %"i"
  %".22" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".21")
  %".24" = load i32, i32* %"i"
  %".25" = add i32 %".24", 1
  store i32 %".25", i32* %"i"
  %".27" = load i32, i32* %"i"
  %".28" = icmp slt i32 %".27", 10
  br i1 %".28", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  %".30" = call i32 @"print_bool"(i1 1)
  ret void
}

@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_3" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_4" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_5" = internal constant [4 x i8] c"%d\0a\00"
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