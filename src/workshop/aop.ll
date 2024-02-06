; ModuleID = "aop"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 10)
  %".4" = fpext float 0x405edd2f20000000 to double
  %".5" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", double %".4")
  %".7" = add i32 10, 20
  %".8" = add i32 %".7", 50
  %".9" = sub i32 %".8", 60
  %".10" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  %".12" = fadd float 0x4034800000000000, 0x4023000000000000
  %".13" = fsub float %".12", 0x3fc3333340000000
  %".14" = fpext float %".13" to double
  %".15" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", double %".14")
  %".17" = sitofp i32 15 to float
  %".18" = fadd float %".17", 0x4012000000000000
  %".19" = fpext float %".18" to double
  %".20" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", double %".19")
  %".22" = sitofp i32 15 to float
  %".23" = fsub float %".22", 0x4012000000000000
  %".24" = fpext float %".23" to double
  %".25" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", double %".24")
  %".27" = sitofp i32 4 to float
  %".28" = fadd float 0x402f000000000000, %".27"
  %".29" = fpext float %".28" to double
  %".30" = bitcast [4 x i8]* @"printf_format_6" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", double %".29")
  %".32" = sitofp i32 4 to float
  %".33" = fsub float 0x402f000000000000, %".32"
  %".34" = fpext float %".33" to double
  %".35" = bitcast [4 x i8]* @"printf_format_7" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", double %".34")
  %".37" = fadd float 0x402f1eb860000000, 0x40401999a0000000
  %".38" = fadd float %".37", 0x4030b33340000000
  %".39" = sitofp i32 15 to float
  %".40" = fadd float %".38", %".39"
  %".41" = sitofp i32 24 to float
  %".42" = fadd float %".40", %".41"
  %".43" = sitofp i32 35 to float
  %".44" = fadd float %".42", %".43"
  %".45" = fpext float %".44" to double
  %".46" = bitcast [4 x i8]* @"printf_format_8" to i8*
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", double %".45")
  %".48" = fadd float 0x402f1eb860000000, 0x40401999a0000000
  %".49" = fsub float %".48", 0x4030b33340000000
  %".50" = sitofp i32 15 to float
  %".51" = fadd float %".49", %".50"
  %".52" = sitofp i32 24 to float
  %".53" = fadd float %".51", %".52"
  %".54" = sitofp i32 35 to float
  %".55" = fadd float %".53", %".54"
  %".56" = fpext float %".55" to double
  %".57" = bitcast [4 x i8]* @"printf_format_9" to i8*
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57", double %".56")
  %"foo" = alloca i32
  store i32 20, i32* %"foo"
  %"bar" = alloca i32
  store i32 12, i32* %"bar"
  %".61" = load i32, i32* %"foo"
  %".62" = load i32, i32* %"bar"
  %".63" = add i32 %".61", %".62"
  %".64" = bitcast [4 x i8]* @"printf_format_10" to i8*
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", i32 %".63")
  %"foo1" = alloca float
  store float 0x4034666660000000, float* %"foo1"
  %"bar1" = alloca float
  store float 0x4028000000000000, float* %"bar1"
  %".68" = load float, float* %"foo1"
  %".69" = load float, float* %"bar1"
  %".70" = fadd float %".68", %".69"
  %".71" = fpext float %".70" to double
  %".72" = bitcast [4 x i8]* @"printf_format_11" to i8*
  %".73" = call i32 (i8*, ...) @"printf"(i8* %".72", double %".71")
  %".74" = load i32, i32* %"foo"
  %".75" = load float, float* %"bar1"
  %".76" = sitofp i32 %".74" to float
  %".77" = fsub float %".76", %".75"
  %".78" = load float, float* %"foo1"
  %".79" = fadd float %".77", %".78"
  %".80" = fpext float %".79" to double
  %".81" = bitcast [4 x i8]* @"printf_format_12" to i8*
  %".82" = call i32 (i8*, ...) @"printf"(i8* %".81", double %".80")
  %".83" = load i32, i32* %"foo"
  %".84" = load float, float* %"bar1"
  %".85" = sitofp i32 %".83" to float
  %".86" = fsub float %".85", %".84"
  %".87" = load float, float* %"foo1"
  %".88" = fadd float %".86", %".87"
  %".89" = sitofp i32 200 to float
  %".90" = fadd float %".88", %".89"
  %".91" = fpext float %".90" to double
  %".92" = bitcast [4 x i8]* @"printf_format_13" to i8*
  %".93" = call i32 (i8*, ...) @"printf"(i8* %".92", double %".91")
  %".94" = load i32, i32* %"foo"
  %".95" = load i32, i32* %"foo"
  %".96" = add i32 %".94", %".95"
  %".97" = load i32, i32* %"foo"
  %".98" = sub i32 %".96", %".97"
  %".99" = bitcast [4 x i8]* @"printf_format_14" to i8*
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99", i32 %".98")
  %".101" = sdiv i32 7, 3
  %".102" = bitcast [4 x i8]* @"printf_format_15" to i8*
  %".103" = call i32 (i8*, ...) @"printf"(i8* %".102", i32 %".101")
  %".104" = sitofp i32 7 to float
  %".105" = sitofp i32 3 to float
  %".106" = fdiv float %".104", %".105"
  %".107" = fpext float %".106" to double
  %".108" = bitcast [4 x i8]* @"printf_format_16" to i8*
  %".109" = call i32 (i8*, ...) @"printf"(i8* %".108", double %".107")
  %".110" = fdiv float 0x401e000000000000, 0x4004ccccc0000000
  %".111" = fpext float %".110" to double
  %".112" = call double @"floor"(double %".111")
  %".113" = bitcast [4 x i8]* @"printf_format_17" to i8*
  %".114" = call i32 (i8*, ...) @"printf"(i8* %".113", double %".112")
  %".115" = sitofp i32 2 to double
  %".116" = sitofp i32 6 to double
  %".117" = call double @"pow"(double %".115", double %".116")
  %".118" = bitcast [4 x i8]* @"printf_format_18" to i8*
  %".119" = call i32 (i8*, ...) @"printf"(i8* %".118", double %".117")
  %".120" = sitofp i32 2 to float
  %".121" = fpext float 0x4034666660000000 to double
  %".122" = fpext float %".120" to double
  %".123" = call double @"pow"(double %".121", double %".122")
  %".124" = bitcast [4 x i8]* @"printf_format_19" to i8*
  %".125" = call i32 (i8*, ...) @"printf"(i8* %".124", double %".123")
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_3" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_4" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_5" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_6" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_7" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_8" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_9" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_10" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_11" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_12" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_13" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_14" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_15" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_16" = internal constant [4 x i8] c"%f\0a\00"
declare double @"floor"(double %".1")

@"printf_format_17" = internal constant [4 x i8] c"%f\0a\00"
declare double @"pow"(double %".1", double %".2")

@"printf_format_18" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_19" = internal constant [4 x i8] c"%f\0a\00"