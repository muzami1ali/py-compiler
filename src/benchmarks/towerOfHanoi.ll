; ModuleID = "towerOfHanoi"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  call void @"towerOfHanoi"(i32 3, i32 0, i32 2, i32 1)
  ret i32 0
}

define void @"towerOfHanoi"(i32 %"n", i32 %"start", i32 %"middle", i32 %"end")
{
entry:
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  %".7" = icmp eq i32 %"n", 1
  br i1 %".7", label %"if_block_0", label %"endif_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".10" = bitcast [41 x i8]* @"printf_format_0" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %"start", i32 %"end")
  br label %"endif_block_0"
endif_block_0:
  %".13" = load i1, i1* %"ifvar0"
  br i1 %".13", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %".15" = sub i32 %"n", 1
  call void @"towerOfHanoi"(i32 %".15", i32 %"start", i32 %"middle", i32 %"end")
  %".17" = bitcast [42 x i8]* @"printf_format_1" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %"n", i32 %"start", i32 %"end")
  %".19" = sub i32 %"n", 1
  call void @"towerOfHanoi"(i32 %".19", i32 %"middle", i32 %"start", i32 %"end")
  br label %"end_else_block_0"
end_else_block_0:
  ret void
}

@"printf_format_0" = internal constant [41 x i8] c"Move disk 1 from source %d to target %d\0a\00"
declare i32 @"printf"(i8* %".1", ...)

@"printf_format_1" = internal constant [42 x i8] c"Move disk %d from source %d to target %d\0a\00"