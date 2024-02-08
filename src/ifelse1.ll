; ModuleID = "ifelse1"
target triple = "arm64-apple-macosx14.0.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"foo" = alloca float
  store float 0x4008ccccc0000000, float* %"foo"
  %".3" = load float, float* %"foo"
  %".4" = sitofp i32 20 to float
  %".5" = fpext float %".4" to double
  %".6" = fpext float %".3" to double
  %".7" = call double @"pow"(double %".5", double %".6")
  %".8" = sitofp i32 20 to double
  %".9" = fdiv double %".7", %".8"
  %".10" = call double @"floor"(double %".9")
  %".11" = sitofp i32 10 to double
  %".12" = fadd double %".11", %".10"
  %"munch" = alloca double
  store double %".12", double* %"munch"
  %"munch.1" = alloca i32
  store i32 3, i32* %"munch.1"
  %".15" = load i32, i32* %"munch.1"
  %".16" = sitofp i32 %".15" to double
  %".17" = sitofp i32 3 to double
  %".18" = call double @"pow"(double %".16", double %".17")
  %"munch.2" = alloca double
  store double %".18", double* %"munch.2"
  %".20" = add i32 10, 20
  %".21" = add i32 10, 20
  %".22" = add i32 10, 20
  %".23" = add i32 10, 20
  %".24" = add i32 10, 20
  %".25" = add i32 10, 20
  %".26" = add i32 20, 30
  ret i32 0
}

declare double @"pow"(double %".1", double %".2")

declare double @"floor"(double %".1")
