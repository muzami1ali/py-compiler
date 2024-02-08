; ModuleID = "bool3"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"print_bool"(i1 1)
  %".3" = call i32 @"print_bool"(i1 0)
  %"foo" = alloca i1
  store i1 1, i1* %"foo"
  %"baz" = alloca i1
  store i1 0, i1* %"baz"
  %".6" = load i1, i1* %"foo"
  %".7" = load i1, i1* %"baz"
  %".8" = and i1 %".6", %".7"
  %".9" = call i32 @"print_bool"(i1 %".8")
  %".10" = sitofp i32 10 to double
  %".11" = sitofp i32 2 to double
  %".12" = call double @"pow"(double %".10", double %".11")
  %".13" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", double %".12")
  ret i32 0
}

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
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_False" = internal constant [7 x i8] c"False\0a\00"
declare double @"pow"(double %".1", double %".2")

@"printf_format_3" = internal constant [4 x i8] c"%f\0a\00"