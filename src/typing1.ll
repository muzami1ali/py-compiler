; ModuleID = "typing1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
var_block:
  %".15" = sitofp i32 20 to double
  %".16" = sitofp i32 2 to double
  %".17" = call double @"pow"(double %".15", double %".16")
  %".39" = add i32 20, 5
  br label %"entry"
entry:
  %"boo" = alloca i1
  store i1 1, i1* %"boo"
  %"boo-type" = alloca i2
  store i2 3, i2* %"boo-type"
  %"foo" = alloca i32
  store i32 20, i32* %"foo"
  %"foo-type" = alloca i2
  store i2 0, i2* %"foo-type"
  %".6" = load i2, i2* %"foo-type"
  %".7" = icmp eq i2 0, %".6"
  br i1 %".7", label %"check_typ_block_foo_IntVar", label %"end_check_typ_block_foo_IntVar"
check_typ_block_foo_IntVar:
  %".9" = load i32, i32* %"foo"
  %".10" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  br label %"end_check_typ_block_foo_IntVar"
end_check_typ_block_foo_IntVar:
  %"baz" = alloca float
  store float 0x4034000000000000, float* %"baz"
  %"baz-type" = alloca i2
  store i2 1, i2* %"baz-type"
  %"foo.1" = alloca double
  store double %".17", double* %"foo.1"
  store i2 2, i2* %"foo-type"
  %".20" = load i2, i2* %"foo-type"
  %".21" = icmp eq i2 0, %".20"
  br i1 %".21", label %"check_typ_block_foo_IntVar.1", label %"end_check_typ_block_foo_IntVar.1"
check_typ_block_foo_IntVar.1:
  %".23" = load i32, i32* %"foo"
  %".24" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".23")
  br label %"end_check_typ_block_foo_IntVar.1"
end_check_typ_block_foo_IntVar.1:
  %".27" = load i2, i2* %"foo-type"
  %".28" = icmp eq i2 2, %".27"
  br i1 %".28", label %"check_typ_block_foo_DoubleVar", label %"end_check_typ_block_foo_DoubleVar"
check_typ_block_foo_DoubleVar:
  %".30" = load double, double* %"foo.1"
  %".31" = bitcast [4 x i8]* @"printf_format_21" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", double %".30")
  br label %"end_check_typ_block_foo_DoubleVar"
end_check_typ_block_foo_DoubleVar:
  %"test" = alloca i32
  store i32 10, i32* %"test"
  %"test-type" = alloca i2
  store i2 0, i2* %"test-type"
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 0, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  store i32 %".39", i32* %"test"
  br label %"endif_block_0"
endif_block_0:
  %".42" = load i1, i1* %"ifvar0"
  br i1 %".42", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %"zoom" = alloca i1
  store i1 0, i1* %"zoom"
  %"zoom-type" = alloca i2
  store i2 3, i2* %"zoom-type"
  br label %"end_else_block_0"
end_else_block_0:
  %".47" = load i2, i2* %"test-type"
  %".48" = icmp eq i2 0, %".47"
  br i1 %".48", label %"check_typ_block_test_IntVar", label %"end_check_typ_block_test_IntVar"
check_typ_block_test_IntVar:
  %".50" = load i32, i32* %"test"
  %".51" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".50")
  br label %"end_check_typ_block_test_IntVar"
end_check_typ_block_test_IntVar:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

declare double @"pow"(double %".1", double %".2")

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_21" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"