; ModuleID = "bool2"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca i1
  store i1 1, i1* %"foo"
  %".3" = load i1, i1* %"foo"
  %".4" = xor i1 %".3", -1
  br i1 %".4", label %"print_bool_if_0", label %"print_bool_else_0"
print_bool_if_0:
  %".6" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  br label %"print_bool_endif_0"
print_bool_else_0:
  %".9" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  br label %"print_bool_endif_0"
print_bool_endif_0:
  %".12" = icmp sgt i32 10, 2
  %".13" = xor i1 %".12", -1
  br i1 %".13", label %"print_bool_if_1", label %"print_bool_else_1"
print_bool_if_1:
  %".15" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15")
  br label %"print_bool_endif_1"
print_bool_else_1:
  %".18" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18")
  br label %"print_bool_endif_1"
print_bool_endif_1:
  %".21" = and i1 1, 1
  br i1 %".21", label %"print_bool_if_2", label %"print_bool_else_2"
print_bool_if_2:
  %".23" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23")
  br label %"print_bool_endif_2"
print_bool_else_2:
  %".26" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26")
  br label %"print_bool_endif_2"
print_bool_endif_2:
  %".29" = and i1 0, 0
  br i1 %".29", label %"print_bool_if_3", label %"print_bool_else_3"
print_bool_if_3:
  %".31" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31")
  br label %"print_bool_endif_3"
print_bool_else_3:
  %".34" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34")
  br label %"print_bool_endif_3"
print_bool_endif_3:
  %".37" = and i1 1, 0
  br i1 %".37", label %"print_bool_if_4", label %"print_bool_else_4"
print_bool_if_4:
  %".39" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".39")
  br label %"print_bool_endif_4"
print_bool_else_4:
  %".42" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42")
  br label %"print_bool_endif_4"
print_bool_endif_4:
  %".45" = or i1 1, 1
  br i1 %".45", label %"print_bool_if_5", label %"print_bool_else_5"
print_bool_if_5:
  %".47" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".48" = call i32 (i8*, ...) @"printf"(i8* %".47")
  br label %"print_bool_endif_5"
print_bool_else_5:
  %".50" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".50")
  br label %"print_bool_endif_5"
print_bool_endif_5:
  %".53" = or i1 0, 1
  br i1 %".53", label %"print_bool_if_6", label %"print_bool_else_6"
print_bool_if_6:
  %".55" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55")
  br label %"print_bool_endif_6"
print_bool_else_6:
  %".58" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58")
  br label %"print_bool_endif_6"
print_bool_endif_6:
  %".61" = or i1 0, 0
  br i1 %".61", label %"print_bool_if_7", label %"print_bool_else_7"
print_bool_if_7:
  %".63" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63")
  br label %"print_bool_endif_7"
print_bool_else_7:
  %".66" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66")
  br label %"print_bool_endif_7"
print_bool_endif_7:
  ret i32 0
}

@"printf_format_True" = internal constant [6 x i8] c"True\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_False" = internal constant [7 x i8] c"False\0a\00"