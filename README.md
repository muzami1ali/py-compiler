# py-compiler
This project builds an ahead-of-time compiler for Python

Thsi was built on macos so should also work on linux.1

## Requirments
Before running this compiler you will need to install some packages
Firstly make sure that you have python 3 installed.
Secondly clang shoudld also be installed.
For the final step navigate to py-compiler/ and run
the following command
pip install -r requirements.txt

## Running code
To compile the code simply navigate to py-compiler/src. The file you want to compile should
also be present here. Then run the following command
python compile.py filname.py
This will produce the executable.
If you want to directly run the program you can use the following command:
python run.py filname.py


## Testing
Before running tests ensure that you have rust and cargo installed. 
Then navigate to py-compiler/src/tests/py-tests and run the following command
cargo test. Altenratively if you want to look at the output of running the tests
you could use the follwoing command cargo test --test lang_tests -- --nocapture

## Becnchmark
Before running benchmarks you will need to download PyPy from https://www.pypy.org/
Then navigate to the py-compiler/src/benchmarks directory and run the follwing command:
python benchmark.py

## Resetting FrontEnd
The compiler should work with current frontend code but if there are some 
issue you could reset the frontend. first navigate to py-compiler/src
and run the following command antlr4 -v 4.13.0 -Dlanguage=Python3 Lang.g4 -visitor
