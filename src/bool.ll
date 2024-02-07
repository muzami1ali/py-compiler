; ModuleID = "bool"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = icmp eq i1 1, 1
  br i1 %".2", label %"entry.if", label %"entry.else"
entry.if:
  %".4" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  br label %"entry.endif"
entry.else:
  %".7" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  br label %"entry.endif"
entry.endif:
  %".10" = icmp eq i1 0, 1
  br i1 %".10", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  %".12" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  br label %"entry.endif.endif"
entry.endif.else:
  %".15" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15")
  br label %"entry.endif.endif"
entry.endif.endif:
  %".18" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 10)
  %".20" = sitofp i32 20 to double
  %".21" = sitofp i32 4 to double
  %".22" = call double @"pow"(double %".20", double %".21")
  %".23" = sitofp i32 5 to double
  %".24" = fdiv double %".22", %".23"
  %".25" = call double @"floor"(double %".24")
  %".26" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", double %".25")
  ret i32 0
}

@"printf_format_True" = internal constant [6 x i8] c"True\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_False" = internal constant [7 x i8] c"False\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
declare double @"pow"(double %".1", double %".2")

declare double @"floor"(double %".1")

@"printf_format_3" = internal constant [4 x i8] c"%f\0a\00"