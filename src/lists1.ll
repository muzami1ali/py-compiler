; ModuleID = "lists1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca i32
  %"var" = alloca {i8*, i32, i32, i32}
  store i32 200, i32* %"foo"
  %".3" = load i32, i32* %"foo"
  %".4" = call i32 @"test"()
  call void @"create_list"({i8*, i32, i32, i32}* %"var")
  ret i32 0
}

define i32 @"test"()
{
entry:
  ret i32 100
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
  store i32 %".20", i32* %".24"
}
