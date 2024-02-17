; ModuleID = "while1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  store i32 1, i32* %"i"
  %"foo" = alloca i1
  store i1 0, i1* %"foo"
  %".4" = load i32, i32* %"i"
  %".5" = icmp slt i32 %".4", 6
  br i1 %".5", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".7" = load i32, i32* %"i"
  %".8" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  %"ifvar0" = alloca i1
  store i1 1, i1* %"ifvar0"
  br i1 0, label %"if_block_0", label %"endif_block_0"
end_while_block_0:
  ret i32 0
if_block_0:
  store i1 0, i1* %"ifvar0"
  %"pos" = alloca i32
  store i32 1, i32* %"pos"
  br label %"endif_block_0"
endif_block_0:
  %".15" = load i1, i1* %"ifvar0"
  br i1 %".15", label %"else_block_0", label %"end_else_block_0"
else_block_0:
  %"pos.1" = alloca float
  store float 0x4000000000000000, float* %"pos.1"
  br label %"end_else_block_0"
end_else_block_0:
  %".19" = load float, float* %"pos.1"
  %".20" = load i32, i32* %"i"
  %".21" = sitofp i32 %".20" to float
  %".22" = fadd float %".19", %".21"
  %"i.1" = alloca float
  store float %".22", float* %"i.1"
  %".24" = load float, float* %"i.1"
  %".25" = sitofp i32 6 to float
  %".26" = fcmp olt float %".24", %".25"
  br i1 %".26", label %"while_block_0", label %"end_while_block_0"
}

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...)
