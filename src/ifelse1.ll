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
  br i1 1, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".6" = add i32 10, 20
  %".7" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  %"ifvar1" = alloca i1
  store i1 1, i1* %"ifvar1"
  br i1 0, label %"if_block_1", label %"endif_block_1"
endif_block_0:
  %".43" = load i1, i1* %"ifvar0"
  %".44" = and i1 0, %".43"
  br i1 %".44", label %"elif_block_0", label %"end_elif_block_0"
if_block_1:
  store i1 0, i1* %"ifvar1"
  %".12" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 5000)
  br label %"endif_block_1"
endif_block_1:
  %".15" = load i1, i1* %"ifvar1"
  %".16" = and i1 1, %".15"
  br i1 %".16", label %"elif_block_1", label %"end_elif_block_1"
elif_block_1:
  store i1 0, i1* %"ifvar1"
  %".19" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 100)
  %"ifvar2" = alloca i1
  store i1 1, i1* %"ifvar2"
  br i1 1, label %"if_block_2", label %"endif_block_2"
end_elif_block_1:
  %".27" = load i1, i1* %"ifvar1"
  br i1 %".27", label %"else_block_1", label %"end_else_block_1"
if_block_2:
  store i1 0, i1* %"ifvar2"
  %".24" = call i32 @"print_bool"(i1 0)
  br label %"endif_block_2"
endif_block_2:
  br label %"end_elif_block_1"
else_block_1:
  %".29" = sitofp i32 5 to double
  %".30" = sitofp i32 20 to double
  %".31" = call double @"pow"(double %".29", double %".30")
  %".32" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", double %".31")
  %"ifvar3" = alloca i1
  store i1 1, i1* %"ifvar3"
  br i1 1, label %"if_block_3", label %"endif_block_3"
end_else_block_1:
  br label %"endif_block_0"
if_block_3:
  store i1 0, i1* %"ifvar3"
  %".37" = sdiv i32 1024, 5
  %".38" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".38", i32 %".37")
  br label %"endif_block_3"
endif_block_3:
  br label %"end_else_block_1"
elif_block_0:
  store i1 0, i1* %"ifvar0"
  %".47" = bitcast [4 x i8]* @"printf_format_6" to i8*
  %".48" = call i32 (i8*, ...) @"printf"(i8* %".47", i32 0)
  br label %"end_elif_block_0"
end_elif_block_0:
  %".50" = load i1, i1* %"ifvar0"
  %".51" = and i1 1, %".50"
  br i1 %".51", label %"elif_block_0.1", label %"end_elif_block_0.1"
elif_block_0.1:
  store i1 0, i1* %"ifvar0"
  %".54" = call i32 @"print_bool"(i1 1)
  br label %"end_elif_block_0.1"
end_elif_block_0.1:
  %".56" = load i1, i1* %"ifvar0"
  br i1 %".56", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".58" = add i32 20, 20
  %".59" = bitcast [4 x i8]* @"printf_format_8" to i8*
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59", i32 %".58")
  br label %"end_else_block_0"
end_else_block_0:
  %"ifvar4" = alloca i1
  store i1 1, i1* %"ifvar4"
  br i1 1, label %"if_block_4", label %"endif_block_4"
if_block_4:
  store i1 0, i1* %"ifvar4"
  %".65" = add i32 10, 20
  br label %"endif_block_4"
endif_block_4:
  %".67" = load i1, i1* %"ifvar4"
  br i1 %".67", label %"else_block_4", label %"end_else_block_4"
else_block_4:
  %".69" = add i32 20, 30
  br label %"end_else_block_4"
end_else_block_4:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
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
declare double @"pow"(double %".1", double %".2")

@"printf_format_4" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_5" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_6" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_8" = internal constant [4 x i8] c"%d\0a\00"