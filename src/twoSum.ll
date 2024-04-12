; ModuleID = "twoSum"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"twoSum"(i32 9)
  ret i32 0
}

define i32 @"twoSum"(i32 %"target")
{
entry:
  %"lst" = alloca {i8*, i32, i32, i32}
  %"size" = alloca i32
  %"x" = alloca i32
  %"y" = alloca i32
  %"ifvar0" = alloca i1
  %"first" = alloca i32
  %"scnd" = alloca i32
  %"sum" = alloca i32
  %"ifvar1" = alloca i1
  call void @"create_list"({i8*, i32, i32, i32}* %"lst")
  call void @"append_int_list"({i8*, i32, i32, i32}* %"lst", i32 2)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"lst", i32 7)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"lst", i32 11)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"lst", i32 15)
  %".8" = call i32 @"get_list_length"({i8*, i32, i32, i32}* %"lst")
  store i32 %".8", i32* %"size"
  store i32 0, i32* %"x"
  store i32 0, i32* %"y"
  %".12" = load i32, i32* %"x"
  %".13" = load i32, i32* %"size"
  %".14" = icmp slt i32 %".12", %".13"
  br i1 %".14", label %"while_block_0", label %"end_while_block_0"
while_block_0:
  %".16" = load i32, i32* %"y"
  %".17" = load i32, i32* %"size"
  %".18" = icmp slt i32 %".16", %".17"
  br i1 %".18", label %"while_block_0.1", label %"end_while_block_0.1"
end_while_block_0:
  call void @"delete_list"({i8*, i32, i32, i32}* %"lst")
  ret i32 0
while_block_0.1:
  store i1 1, i1* %"ifvar0"
  %".21" = load i32, i32* %"x"
  %".22" = load i32, i32* %"y"
  %".23" = icmp ne i32 %".21", %".22"
  br i1 %".23", label %"if_block_0", label %"endif_block_0"
end_while_block_0.1:
  store i32 0, i32* %"y"
  %".56" = load i32, i32* %"x"
  %".57" = add i32 %".56", 1
  store i32 %".57", i32* %"x"
  %".59" = load i32, i32* %"x"
  %".60" = load i32, i32* %"size"
  %".61" = icmp slt i32 %".59", %".60"
  br i1 %".61", label %"while_block_0", label %"end_while_block_0"
if_block_0:
  store i1 0, i1* %"ifvar0"
  %".26" = load i32, i32* %"x"
  %".27" = call i32 @"get_int_list_element"({i8*, i32, i32, i32}* %"lst", i32 %".26")
  store i32 %".27", i32* %"first"
  %".29" = load i32, i32* %"y"
  %".30" = call i32 @"get_int_list_element"({i8*, i32, i32, i32}* %"lst", i32 %".29")
  store i32 %".30", i32* %"scnd"
  %".32" = load i32, i32* %"first"
  %".33" = load i32, i32* %"scnd"
  %".34" = add i32 %".32", %".33"
  store i32 %".34", i32* %"sum"
  store i1 1, i1* %"ifvar1"
  %".37" = load i32, i32* %"sum"
  %".38" = icmp eq i32 %".37", %"target"
  br i1 %".38", label %"if_block_1", label %"endif_block_1"
endif_block_0:
  %".48" = load i32, i32* %"y"
  %".49" = add i32 %".48", 1
  store i32 %".49", i32* %"y"
  %".51" = load i32, i32* %"y"
  %".52" = load i32, i32* %"size"
  %".53" = icmp slt i32 %".51", %".52"
  br i1 %".53", label %"while_block_0.1", label %"end_while_block_0.1"
if_block_1:
  store i1 0, i1* %"ifvar1"
  %".41" = load i32, i32* %"x"
  %".42" = load i32, i32* %"y"
  %".43" = bitcast [26 x i8]* @"printf_format_0" to i8*
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i32 %".41", i32 %".42")
  call void @"delete_list"({i8*, i32, i32, i32}* %"lst")
  ret i32 0
endif_block_1:
  br label %"endif_block_0"
}

define void @"create_list"({i8*, i32, i32, i32}* %".1")
{
entry:
  %".3" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  store i8* null, i8** %".3"
  %".5" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  store i32 0, i32* %".5"
  %".7" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 2
  store i32 0, i32* %".7"
  %".9" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  store i32 0, i32* %".9"
  ret void
}

define void @"append_int_list"({i8*, i32, i32, i32}* %".1", i32 %".2")
{
entry:
  %".4" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  %".6" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 2
  %".7" = load i32, i32* %".6"
  %".8" = icmp eq i32 %".5", %".7"
  br i1 %".8", label %"grow_begin", label %"grow_end"
grow_begin:
  %".10" = add i32 4, %".7"
  call void @"resize_list"({i8*, i32, i32, i32}* %".1", i32 %".10")
  br label %"grow_end"
grow_end:
  %".13" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".14" = load i8*, i8** %".13"
  %".15" = bitcast i8* %".14" to i32*
  %".16" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  %".17" = load i32, i32* %".16"
  %".18" = getelementptr i32, i32* %".15", i32 %".17"
  store i32 %".2", i32* %".18"
  %".20" = add i32 %".5", 4
  %".21" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  store i32 %".20", i32* %".21"
  %".23" = add i32 %".17", 1
  %".24" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  store i32 %".23", i32* %".24"
  ret void
}

define void @"resize_list"({i8*, i32, i32, i32}* %".1", i32 %".2")
{
entry:
  %".4" = call i8* @"malloc"(i32 %".2")
  %".5" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".6" = load i8*, i8** %".5"
  %".7" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  %".8" = load i32, i32* %".7"
  %".9" = call i8* @"memcpy"(i8* %".4", i8* %".6", i32 %".8")
  call void @"free"(i8* %".6")
  store i8* %".4", i8** %".5"
  %".12" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 2
  store i32 %".2", i32* %".12"
  ret void
}

declare i8* @"malloc"(i32 %".1")

declare i8* @"memcpy"(i8* %".1", i8* %".2", i32 %".3")

declare void @"free"(i8* %".1")

define i32 @"get_list_length"({i8*, i32, i32, i32}* %".1")
{
entry:
  %".3" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i32 @"get_int_list_element"({i8*, i32, i32, i32}* %".1", i32 %".2")
{
entry:
  %".4" = call i32 @"get_max_index"({i8*, i32, i32, i32}* %".1")
  call void @"check_index_out_of_bound"(i32 %".2", i32 %".4")
  %".6" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".7" = load i8*, i8** %".6"
  %".8" = bitcast i8* %".7" to i32*
  %".9" = getelementptr i32, i32* %".8", i32 %".2"
  %".10" = load i32, i32* %".9"
  ret i32 %".10"
}

define i32 @"get_max_index"({i8*, i32, i32, i32}* %".1")
{
entry:
  %".3" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  %".4" = load i32, i32* %".3"
  %".5" = sub i32 %".4", 1
  ret i32 %".5"
}

define void @"check_index_out_of_bound"(i32 %".1", i32 %".2")
{
entry:
  %".4" = icmp sgt i32 %".1", %".2"
  br i1 %".4", label %"entry.if", label %"entry.endif"
entry.if:
  %".6" = bitcast [20 x i8]* @"printf_format_index_error" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  call void @"exit"(i32 1)
  ret void
entry.endif:
  ret void
}

@"printf_format_index_error" = internal constant [20 x i8] c"Index out of bound\0a\00"
declare i32 @"printf"(i8* %".1", ...)

declare void @"exit"(i32 %".1")

@"printf_format_0" = internal constant [26 x i8] c"The indices are: [%d,%d]\0a\00"
define void @"delete_list"({i8*, i32, i32, i32}* %".1")
{
entry:
  %".3" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".4" = load i8*, i8** %".3"
  %".5" = icmp ne i8* %".4", null
  br i1 %".5", label %"free_begin", label %"free_end"
free_begin:
  call void @"free"(i8* %".4")
  %".8" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  store i8* null, i8** %".8"
  br label %"free_end"
free_end:
  ret void
}
