; ModuleID = "bool"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  br i1 1, label %"entry.if", label %"entry.else"
entry.if:
  %".3" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3")
  br label %"entry.endif"
entry.else:
  %".6" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  br label %"entry.endif"
entry.endif:
  br i1 0, label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  %".10" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  br label %"entry.endif.endif"
entry.endif.else:
  %".13" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  br label %"entry.endif.endif"
entry.endif.endif:
  %".16" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 10)
  %".18" = sitofp i32 20 to double
  %".19" = sitofp i32 4 to double
  %".20" = call double @"pow"(double %".18", double %".19")
  %".21" = sitofp i32 5 to double
  %".22" = fdiv double %".20", %".21"
  %".23" = call double @"floor"(double %".22")
  %".24" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", double %".23")
  %".26" = icmp sgt i32 10, 5
  br i1 %".26", label %"entry.endif.endif.if", label %"entry.endif.endif.else"
entry.endif.endif.if:
  %".28" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28")
  br label %"entry.endif.endif.endif"
entry.endif.endif.else:
  %".31" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31")
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif:
  %".34" = sitofp i32 25 to double
  %".35" = sitofp i32 1 to double
  %".36" = call double @"pow"(double %".34", double %".35")
  %".37" = sitofp i32 5 to double
  %".38" = sitofp i32 2 to double
  %".39" = call double @"pow"(double %".37", double %".38")
  %".40" = fcmp oeq double %".36", %".39"
  br i1 %".40", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.else"
entry.endif.endif.endif.if:
  %".42" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42")
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.else:
  %".45" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45")
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  %".48" = sitofp i32 10 to float
  %".49" = fcmp oeq float %".48", 0x4024000000000000
  br i1 %".49", label %"entry.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.else"
entry.endif.endif.endif.endif.if:
  %".51" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51")
  br label %"entry.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.else:
  %".54" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54")
  br label %"entry.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif:
  %".57" = sitofp i32 10 to double
  %".58" = sitofp i32 1 to double
  %".59" = call double @"pow"(double %".57", double %".58")
  %".60" = sitofp i32 10 to double
  %".61" = fcmp oeq double %".60", %".59"
  br i1 %".61", label %"entry.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.else"
entry.endif.endif.endif.endif.endif.if:
  %".63" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63")
  br label %"entry.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.else:
  %".66" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66")
  br label %"entry.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif:
  %".69" = sitofp i32 10 to double
  %".70" = sitofp i32 1 to double
  %".71" = call double @"pow"(double %".69", double %".70")
  %".72" = fpext float 0x4024000000000000 to double
  %".73" = fcmp oeq double %".72", %".71"
  br i1 %".73", label %"entry.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.else"
entry.endif.endif.endif.endif.endif.endif.if:
  %".75" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".76" = call i32 (i8*, ...) @"printf"(i8* %".75")
  br label %"entry.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.else:
  %".78" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".79" = call i32 (i8*, ...) @"printf"(i8* %".78")
  br label %"entry.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.endif:
  %".81" = sub i32 10, 204
  %".82" = sitofp i32 5 to double
  %".83" = sitofp i32 2 to double
  %".84" = call double @"pow"(double %".82", double %".83")
  %".85" = sitofp i32 %".81" to double
  %".86" = fadd double %".85", %".84"
  %".87" = sitofp i32 10 to double
  %".88" = sitofp i32 3 to double
  %".89" = call double @"pow"(double %".87", double %".88")
  %".90" = fcmp ogt double %".86", %".89"
  %"foo" = alloca i1
  store i1 %".90", i1* %"foo"
  %".92" = load i1, i1* %"foo"
  br i1 %".92", label %"entry.endif.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.endif.else"
entry.endif.endif.endif.endif.endif.endif.endif.if:
  %".94" = bitcast [6 x i8]* @"printf_format_True" to i8*
  %".95" = call i32 (i8*, ...) @"printf"(i8* %".94")
  br label %"entry.endif.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.endif.else:
  %".97" = bitcast [7 x i8]* @"printf_format_False" to i8*
  %".98" = call i32 (i8*, ...) @"printf"(i8* %".97")
  br label %"entry.endif.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.endif.endif:
  ret i32 0
}

@"printf_format_True" = internal constant [6 x i8] c"True\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_False" = internal constant [7 x i8] c"False\0a\00"
@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare double @"pow"(double %".1", double %".2")

declare double @"floor"(double %".1")

@"printf_format_1" = internal constant [4 x i8] c"%f\0a\00"