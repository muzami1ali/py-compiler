; ModuleID = "ifelse1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 1, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".5" = add i32 10, 20
  %".6" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  %"ifvar1" = alloca i1
  store i1 1, i1* %"ifvar1"
  br i1 0, label %"if_block_1", label %"endif_block_1"
endif_block_0:
  %".42" = load i1, i1* %"ifvar0"
  %".43" = and i1 0, %".42"
  br i1 %".43", label %"elif_block_0", label %"end_elif_block_0"
if_block_1:
  store i1 0, i1* %"ifvar1"
  %".11" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 5000)
  br label %"endif_block_1"
endif_block_1:
  %".14" = load i1, i1* %"ifvar1"
  %".15" = and i1 1, %".14"
  br i1 %".15", label %"elif_block_1", label %"end_elif_block_1"
elif_block_1:
  store i1 0, i1* %"ifvar1"
  %".18" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 100)
  %"ifvar2" = alloca i1
  store i1 1, i1* %"ifvar2"
  br i1 1, label %"if_block_2", label %"endif_block_2"
end_elif_block_1:
  %".26" = load i1, i1* %"ifvar1"
  br i1 %".26", label %"else_block_1", label %"end_else_block_1"
if_block_2:
  store i1 0, i1* %"ifvar2"
  %".23" = call i32 @"print_bool"(i1 0)
  br label %"endif_block_2"
endif_block_2:
  br label %"end_elif_block_1"
else_block_1:
  %".28" = sitofp i32 5 to double
  %".29" = sitofp i32 20 to double
  %".30" = call double @"pow"(double %".28", double %".29")
  %".31" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", double %".30")
  %"ifvar3" = alloca i1
  store i1 1, i1* %"ifvar3"
  br i1 1, label %"if_block_3", label %"endif_block_3"
end_else_block_1:
  br label %"endif_block_0"
if_block_3:
  store i1 0, i1* %"ifvar3"
  %".36" = sdiv i32 1024, 5
  %".37" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i32 %".36")
  br label %"endif_block_3"
endif_block_3:
  br label %"end_else_block_1"
elif_block_0:
  store i1 0, i1* %"ifvar0"
  %".46" = bitcast [4 x i8]* @"printf_format_6" to i8*
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i32 0)
  br label %"end_elif_block_0"
end_elif_block_0:
  %".49" = load i1, i1* %"ifvar0"
  %".50" = and i1 1, %".49"
  br i1 %".50", label %"elif_block_0.1", label %"end_elif_block_0.1"
elif_block_0.1:
  store i1 0, i1* %"ifvar0"
  %".53" = call i32 @"print_bool"(i1 1)
  br label %"end_elif_block_0.1"
end_elif_block_0.1:
  %".55" = load i1, i1* %"ifvar0"
  br i1 %".55", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".57" = add i32 20, 20
  %".58" = bitcast [4 x i8]* @"printf_format_8" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %".57")
  br label %"end_else_block_0"
end_else_block_0:
  %"ifvar4" = alloca i1
  store i1 1, i1* %"ifvar4"
  br i1 1, label %"if_block_4", label %"endif_block_4"
if_block_4:
  store i1 0, i1* %"ifvar4"
  %".64" = add i32 10, 20
  br label %"endif_block_4"
endif_block_4:
  %".66" = load i1, i1* %"ifvar4"
  br i1 %".66", label %"else_block_4", label %"end_else_block_4"
else_block_4:
  %".68" = add i32 20, 30
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