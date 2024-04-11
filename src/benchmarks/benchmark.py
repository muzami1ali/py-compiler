import os 
import sys
import re
import timeit

compilerTimeFactorial = 0
programTimeFactorial = 0
cpythonTimeFactorial = 0
pypyTimeFactorial = 0

compilerTimeFibonacci = 0
programTimeFibonacci = 0
cpythonTimeFibonacci = 0
pypyTimeFibonacci = 0

compilerTimeTowers = 0
programTimeTowers = 0
cpythonTimeTowers = 0
pypyTimeTowers = 0


for i in range(20):

    ## Benchmark factorial 

    ## This compiler compile + run the program
    start = timeit.default_timer()
    os.system(f"python run.py factorial.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    compilerTimeFactorial += timeTaken
    print(f"Time taken by this compiler: {stop-start}")

    ## This compiler execute the program
    start = timeit.default_timer()
    os.system(f"./factorial")
    stop = timeit.default_timer()
    timeTaken = stop-start
    programTimeFactorial += timeTaken
    print(f"Time taken by this compiled program: {stop-start}")

    ## Cpython
    start = timeit.default_timer()
    os.system(f"python factorial.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    cpythonTimeFactorial += timeTaken
    print(f"Time taken by cpython: {stop-start}")

    # pypy
    start = timeit.default_timer()
    os.system(f"pypy factorialPypy.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    pypyTimeFactorial += timeTaken
    print(f"Time taken by pypy: {stop-start}")

    # ## Benchmark fibonacci

    ## This compiler compile + run the program
    start = timeit.default_timer()
    os.system(f"python run.py fibonacci.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    compilerTimeFibonacci += timeTaken
    print(f"Time taken by this compiler: {stop-start}")

    ## This compiler execute the program
    start = timeit.default_timer()
    os.system(f"./fibonacci")
    stop = timeit.default_timer()
    timeTaken = stop-start
    programTimeFibonacci += timeTaken
    print(f"Time taken by this compiled program: {stop-start}")

    ## Cpython
    start = timeit.default_timer()
    os.system(f"python fibonacci.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    cpythonTimeFibonacci += timeTaken
    print(f"Time taken by cpython: {stop-start}")

    # pypy
    start = timeit.default_timer()
    os.system(f"pypy fibonacciPypy.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    pypyTimeFibonacci += timeTaken
    print(f"Time taken by pypy: {stop-start}")

    ## Benchmark towers of hanoi
    start = timeit.default_timer()
    os.system(f"python run.py towerOfHanoi.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    compilerTimeTowers += timeTaken
    print(f"Time taken by this compiler: {stop-start}")

    ## This compiler execute the program
    start = timeit.default_timer()
    os.system(f"./towerOfHanoi")
    stop = timeit.default_timer()
    timeTaken = stop-start
    programTimeTowers += timeTaken
    print(f"Time taken by this compiled program: {stop-start}")

    ## Cpython
    start = timeit.default_timer()
    os.system(f"python towerOfHanoi.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    cpythonTimeTowers += timeTaken
    print(f"Time taken by cpython: {stop-start}")

    # pypy
    start = timeit.default_timer()
    os.system(f"pypy towerOfHanoiPypy.py")
    stop = timeit.default_timer()
    timeTaken = stop-start
    pypyTimeTowers += timeTaken
    print(f"Time taken by pypy: {stop-start}")




averageCompilerTimeFactorial = compilerTimeFactorial/20
averageProgramTimeFactorial = programTimeFactorial/20
averageCpythonTimeFactorial = cpythonTimeFactorial/20
averagePypyTimeFactorial = pypyTimeFactorial/20

averageCompilerTimeFibonacci = compilerTimeFibonacci/20
averageProgramTimeFibonacci = programTimeFibonacci/20
averageCpythonTimeFibonacci = cpythonTimeFibonacci/20
averagePypyTimeFibonacci = pypyTimeFibonacci/20

averageCompilerTimeTowers = compilerTimeTowers/20
averageProgramTimeTowers = programTimeTowers/20
averageCpythonTimeTowers = cpythonTimeTowers/20
averagePypyTimeTowers = pypyTimeTowers/20

print("#######################################################################")
print("####################### Factorial RESULTS #############################")
print("#######################################################################")
print(f"Average time taken by this compiler for factorial: {averageCompilerTimeFactorial}")
print(f"Average time taken by this compiled program for factorial: {averageProgramTimeFactorial}")
print(f"Average time taken by cpython for factorial: {averageCpythonTimeFactorial}")
print(f"Average time taken by pypy for factorial: {averagePypyTimeFactorial}")

print("#######################################################################")
print("####################### Fibonacci RESULTS #############################")
print("#######################################################################")
print(f"Average time taken by this compiler for fibonacci: {averageCompilerTimeFibonacci}")
print(f"Average time taken by this compiled program for fibonacci: {averageProgramTimeFibonacci}")
print(f"Average time taken by cpython for fibonacci: {averageCpythonTimeFibonacci}")
print(f"Average time taken by pypy for fibonacci: {averagePypyTimeFibonacci}")

print("#######################################################################")
print("####################### Towers of Hanoi RESULTS #############################")
print("#######################################################################")
print(f"Average time taken by this compiler for towers of hanoi: {averageCompilerTimeTowers}")
print(f"Average time taken by this compiled program for towers of hanoi: {averageProgramTimeTowers}")
print(f"Average time taken by cpython for towers of hanoi: {averageCpythonTimeTowers}")
print(f"Average time taken by pypy for towers of hanoi: {averagePypyTimeTowers}")

