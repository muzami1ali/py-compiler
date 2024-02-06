; ModuleID = "test"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"barc" = alloca i32
  store i32 102, i32* %"barc"
  %"marc" = alloca float
  store float 0x405a23d700000000, float* %"marc"
  %"larc" = alloca i1
  store i1 0, i1* %"larc"
  %".5" = load i32, i32* %"barc"
  %".6" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  %".8" = load float, float* %"marc"
  %".9" = fpext float %".8" to double
  %".10" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", double %".9")
  %".12" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 10)
  %".14" = fpext float 0x405edd2f20000000 to double
  %".15" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", double %".14")
  %".17" = add i32 10, 20
  %".18" = add i32 %".17", 50
  %".19" = sub i32 %".18", 60
  %".20" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  %".22" = fadd float 0x4034800000000000, 0x4023000000000000
  %".23" = fsub float %".22", 0x3fc3333340000000
  %".24" = fpext float %".23" to double
  %".25" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", double %".24")
  %".27" = sitofp i32 15 to float
  %".28" = fadd float %".27", 0x4012000000000000
  %".29" = fpext float %".28" to double
  %".30" = bitcast [4 x i8]* @"printf_format_6" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", double %".29")
  %".32" = sitofp i32 15 to float
  %".33" = fsub float %".32", 0x4012000000000000
  %".34" = fpext float %".33" to double
  %".35" = bitcast [4 x i8]* @"printf_format_7" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", double %".34")
  %".37" = sitofp i32 4 to float
  %".38" = fadd float 0x402f000000000000, %".37"
  %".39" = fpext float %".38" to double
  %".40" = bitcast [4 x i8]* @"printf_format_8" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", double %".39")
  %".42" = sitofp i32 4 to float
  %".43" = fsub float 0x402f000000000000, %".42"
  %".44" = fpext float %".43" to double
  %".45" = bitcast [4 x i8]* @"printf_format_9" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", double %".44")
  %".47" = fadd float 0x402f1eb860000000, 0x40401999a0000000
  %".48" = fadd float %".47", 0x4030b33340000000
  %".49" = sitofp i32 15 to float
  %".50" = fadd float %".48", %".49"
  %".51" = sitofp i32 24 to float
  %".52" = fadd float %".50", %".51"
  %".53" = sitofp i32 35 to float
  %".54" = fadd float %".52", %".53"
  %".55" = fpext float %".54" to double
  %".56" = bitcast [4 x i8]* @"printf_format_10" to i8*
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".56", double %".55")
  %".58" = fadd float 0x402f1eb860000000, 0x40401999a0000000
  %".59" = fsub float %".58", 0x4030b33340000000
  %".60" = sitofp i32 15 to float
  %".61" = fadd float %".59", %".60"
  %".62" = sitofp i32 24 to float
  %".63" = fadd float %".61", %".62"
  %".64" = sitofp i32 35 to float
  %".65" = fadd float %".63", %".64"
  %".66" = fpext float %".65" to double
  %".67" = bitcast [4 x i8]* @"printf_format_11" to i8*
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", double %".66")
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_3" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_4" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_5" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_6" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_7" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_8" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_9" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_10" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_11" = internal constant [4 x i8] c"%f\0a\00"