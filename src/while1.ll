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
  ret i32 0
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
