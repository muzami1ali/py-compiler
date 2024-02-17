; ModuleID = "typing1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
var_block:
  %"boo" = alloca i1
  store i1 1, i1* %"boo"
  %"boo-type" = alloca i2
  store i2 3, i2* %"boo-type"
  %"foo" = alloca i32
  store i32 20, i32* %"foo"
  %"foo-type" = alloca i2
  store i2 0, i2* %"foo-type"
  %"baz" = alloca float
  store float 0x4034000000000000, float* %"baz"
  %"baz-type" = alloca i2
  store i2 1, i2* %"baz-type"
  %".8" = sitofp i32 20 to double
  %".9" = sitofp i32 2 to double
  %".10" = call double @"pow"(double %".8", double %".9")
  %"foo.1" = alloca double
  store double %".10", double* %"foo.1"
  %"test" = alloca float
  store float 0x4024000000000000, float* %"test"
  %"test-type" = alloca i2
  store i2 1, i2* %"test-type"
  %"test.1" = alloca i32
  store i32 10, i32* %"test.1"
  %"test.2" = alloca i1
  store i1 0, i1* %"test.2"
  br label %"entry"
entry:
  store i2 2, i2* %"foo-type"
  %".13" = load i2, i2* %"foo-type"
  %".14" = icmp eq i2 0, %".13"
  br i1 %".14", label %"check_typ_block_foo_IntVar", label %"end_check_typ_block_foo_IntVar"
check_typ_block_foo_IntVar:
  %".16" = load i32, i32* %"foo"
  %".17" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".16")
  br label %"end_check_typ_block_foo_IntVar"
end_check_typ_block_foo_IntVar:
  %".20" = load i2, i2* %"foo-type"
  %".21" = icmp eq i2 2, %".20"
  br i1 %".21", label %"check_typ_block_foo_DoubleVar", label %"end_check_typ_block_foo_DoubleVar"
check_typ_block_foo_DoubleVar:
  %".23" = load double, double* %"foo.1"
  %".24" = bitcast [4 x i8]* @"printf_format_20" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", double %".23")
  br label %"end_check_typ_block_foo_DoubleVar"
end_check_typ_block_foo_DoubleVar:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 0, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  store i2 0, i2* %"test-type"
  br label %"endif_block_0"
endif_block_0:
  %".35" = load i1, i1* %"ifvar0"
  br i1 %".35", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  store i2 3, i2* %"test-type"
  br label %"end_else_block_0"
end_else_block_0:
  %".40" = load i2, i2* %"test-type"
  %".41" = icmp eq i2 0, %".40"
  br i1 %".41", label %"check_typ_block_test_IntVar", label %"end_check_typ_block_test_IntVar"
check_typ_block_test_IntVar:
  %".43" = load i32, i32* %"test.1"
  %".44" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i32 %".43")
  br label %"end_check_typ_block_test_IntVar"
end_check_typ_block_test_IntVar:
  %".47" = load i2, i2* %"test-type"
  %".48" = icmp eq i2 1, %".47"
  br i1 %".48", label %"check_typ_block_test_FloatVar", label %"end_check_typ_block_test_FloatVar"
check_typ_block_test_FloatVar:
  %".50" = load float, float* %"test"
  %".51" = fpext float %".50" to double
  %".52" = bitcast [4 x i8]* @"printf_format_11" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", double %".51")
  br label %"end_check_typ_block_test_FloatVar"
end_check_typ_block_test_FloatVar:
  %".55" = load i2, i2* %"test-type"
  %".56" = icmp eq i2 3, %".55"
  br i1 %".56", label %"check_typ_block_test_BoolVar", label %"end_check_typ_block_test_BoolVar"
check_typ_block_test_BoolVar:
  %".58" = load i1, i1* %"test.2"
  %".59" = call i32 @"print_bool"(i1 %".58")
  br label %"end_check_typ_block_test_BoolVar"
end_check_typ_block_test_BoolVar:
  ret i32 0
}

declare double @"pow"(double %".1", double %".2")

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_20" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_11" = internal constant [4 x i8] c"%f\0a\00"
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