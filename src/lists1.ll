; ModuleID = "lists1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"var" = alloca {i8*, i32, i32, i32}
  %"double_list" = alloca {i8*, i32, i32, i32}
  call void @"create_list"({i8*, i32, i32, i32}* %"var")
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 32)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 58)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 60)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 100)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 200)
  call void @"append_int_list"({i8*, i32, i32, i32}* %"var", i32 300)
  %".9" = call i32 @"get_int_list_element"({i8*, i32, i32, i32}* %"var", i32 0)
  %".10" = add i32 %".9", 50
  %".11" = bitcast [4 x i8]* @"printf_format_0" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  %".13" = call i32 @"get_int_list_element"({i8*, i32, i32, i32}* %"var", i32 1)
  %".14" = add i32 %".13", 50
  %".15" = bitcast [4 x i8]* @"printf_format_1" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".14")
  %".17" = call i32 @"get_int_list_element"({i8*, i32, i32, i32}* %"var", i32 2)
  %".18" = add i32 %".17", 50
  %".19" = bitcast [4 x i8]* @"printf_format_2" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".18")
  call void @"create_list"({i8*, i32, i32, i32}* %"double_list")
  call void @"append_double_list"({i8*, i32, i32, i32}* %"double_list", double 0x3ff0000000000000)
  call void @"append_double_list"({i8*, i32, i32, i32}* %"double_list", double 0x3fe0000000000000)
  call void @"append_double_list"({i8*, i32, i32, i32}* %"double_list", double 0x4024000000000000)
  call void @"append_double_list"({i8*, i32, i32, i32}* %"double_list", double 0x4034000000000000)
  %".26" = call double @"get_double_list_element"({i8*, i32, i32, i32}* %"double_list", i32 0)
  %".27" = fadd double %".26", 0x4014000000000000
  %".28" = bitcast [4 x i8]* @"printf_format_3" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28", double %".27")
  %".30" = call double @"get_double_list_element"({i8*, i32, i32, i32}* %"double_list", i32 1)
  %".31" = sitofp i32 5 to double
  %".32" = fadd double %".30", %".31"
  %".33" = bitcast [4 x i8]* @"printf_format_4" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", double %".32")
  ret i32 0
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

@"printf_format_0" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_1" = internal constant [4 x i8] c"%d\0a\00"
@"printf_format_2" = internal constant [4 x i8] c"%d\0a\00"
define void @"append_double_list"({i8*, i32, i32, i32}* %".1", double %".2")
{
entry:
  %".4" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  %".6" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 2
  %".7" = load i32, i32* %".6"
  %".8" = icmp eq i32 %".5", %".7"
  br i1 %".8", label %"grow_begin", label %"grow_end"
grow_begin:
  %".10" = add i32 8, %".7"
  call void @"resize_list"({i8*, i32, i32, i32}* %".1", i32 %".10")
  br label %"grow_end"
grow_end:
  %".13" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  %".14" = load i32, i32* %".13"
  %".15" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".16" = load i8*, i8** %".15"
  %".17" = bitcast i8* %".16" to double*
  %".18" = getelementptr double, double* %".17", i32 %".14"
  store double %".2", double* %".18"
  %".20" = add i32 %".5", 8
  %".21" = add i32 %".14", 1
  %".22" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 1
  store i32 %".20", i32* %".22"
  %".24" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 3
  store i32 %".21", i32* %".24"
  ret void
}

define double @"get_double_list_element"({i8*, i32, i32, i32}* %".1", i32 %".2")
{
entry:
  %".4" = call i32 @"get_max_index"({i8*, i32, i32, i32}* %".1")
  call void @"check_index_out_of_bound"(i32 %".2", i32 %".4")
  %".6" = getelementptr {i8*, i32, i32, i32}, {i8*, i32, i32, i32}* %".1", i32 0, i32 0
  %".7" = load i8*, i8** %".6"
  %".8" = bitcast i8* %".7" to double*
  %".9" = getelementptr double, double* %".8", i32 %".2"
  %".10" = load double, double* %".9"
  ret double %".10"
}

@"printf_format_3" = internal constant [4 x i8] c"%f\0a\00"
@"printf_format_4" = internal constant [4 x i8] c"%f\0a\00"