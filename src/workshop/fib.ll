; ModuleID = "fib"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"nterms" = alloca i32
  store i32 20, i32* %"nterms"
  %"n1" = alloca i32
  store i32 0, i32* %"n1"
  %"n2" = alloca i32
  store i32 1, i32* %"n2"
  %"count" = alloca i32
  store i32 0, i32* %"count"
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".7" = load i32, i32* %"nterms"
  %".8" = icmp sle i32 %".7", 0
  br i1 %".8", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".11" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 37707)
  br label %"endif_block_0"
endif_block_0:
  %".14" = load i32, i32* %"nterms"
  %".15" = icmp eq i32 %".14", 1
  %".16" = load i1, i1* %"ifvar0"
  %".17" = and i1 %".15", %".16"
  br i1 %".17", label %"elif_block_0", label %"end_elif_block_0"
elif_block_0:
  store i1 0, i1* %"ifvar0"
  %".20" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 37707)
  %".22" = load i32, i32* %"n1"
  %".23" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".22")
  br label %"end_elif_block_0"
end_elif_block_0:
  %".26" = load i1, i1* %"ifvar0"
  br i1 %".26", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".28" = load i32, i32* %"count"
  %".29" = load i32, i32* %"nterms"
  %".30" = icmp slt i32 %".28", %".29"
  br i1 %".30", label %"while_block_0", label %"end_while_block_0"
end_else_block_0:
  ret i32 0
while_block_0:
  %".32" = load i32, i32* %"n1"
  %".33" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".32")
  %".35" = load i32, i32* %"n1"
  %".36" = load i32, i32* %"n2"
  %".37" = add i32 %".35", %".36"
  %"nth" = alloca i32
  store i32 %".37", i32* %"nth"
  %".39" = load i32, i32* %"n2"
  store i32 %".39", i32* %"n1"
  %".41" = load i32, i32* %"nth"
  store i32 %".41", i32* %"n2"
  %".43" = load i32, i32* %"count"
  %".44" = add i32 %".43", 1
  store i32 %".44", i32* %"count"
  %".46" = load i32, i32* %"count"
  %".47" = load i32, i32* %"nterms"
  %".48" = icmp slt i32 %".46", %".47"
  br i1 %".48", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  br label %"end_else_block_0"
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_3" = internal constant [4 x i8] c"%d\0a\00"