; ModuleID = "while1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  store i32 1, i32* %"i"
  %".3" = load i32, i32* %"i"
  %".4" = icmp slt i32 %".3", 6
  br i1 %".4", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".6" = load i32, i32* %"i"
  %".7" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  %".9" = load i32, i32* %"i"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"i"
  %".12" = load i32, i32* %"i"
  %".13" = icmp slt i32 %".12", 6
  br i1 %".13", label %"while_block_0", label %"end_while_block_0"
end_while_block_0:
  store i32 1, i32* %"i"
  %".16" = load i32, i32* %"i"
  %".17" = icmp slt i32 %".16", 6
  br i1 %".17", label %"while_block_0.1", label %"end_while_block_0.1"
while_block_0.1:
  %".19" = load i32, i32* %"i"
  %".20" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  %".22" = load i32, i32* %"i"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"i"
  %".25" = load i32, i32* %"i"
  %".26" = icmp slt i32 %".25", 6
  br i1 %".26", label %"while_block_0.1", label %"end_while_block_0.1"
end_while_block_0.1:
  br label %"while_else_block_0"
while_else_block_0:
  %".29" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 123456789)
  br label %"end_while_else_block_0"
end_while_else_block_0:
  store i32 1, i32* %"i"
  %".33" = load i32, i32* %"i"
  %".34" = icmp slt i32 %".33", 6
  br i1 %".34", label %"while_block_0.2", label %"end_while_block_0.2"
while_block_0.2:
  %".36" = load i32, i32* %"i"
  %".37" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i32 %".36")
  %".39" = load i32, i32* %"i"
  %".40" = add i32 %".39", 1
  store i32 %".40", i32* %"i"
  %".42" = load i32, i32* %"i"
  %".43" = icmp slt i32 %".42", 6
  br i1 %".43", label %"while_block_0.2", label %"end_while_block_0.2"
end_while_block_0.2:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 1, label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".48" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 20)
  br label %"endif_block_0"
endif_block_0:
  %"foo" = alloca i1
  store i1 1, i1* %"foo"
  %"ifvar1" = alloca i1
  store i1 1, i1* %"ifvar1"
  %".53" = load i1, i1* %"foo"
  br i1 %".53", label %"if_block_1", label %"endif_block_1"
if_block_1:
  store i1 0, i1* %"ifvar1"
  %".56" = bitcast [4 x i8]* @"printf_format_5" to i8*
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".56", i32 0)
  br label %"endif_block_1"
endif_block_1:
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_3" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_4" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_5" = internal constant [4 x i8] c"%d\0a\00"