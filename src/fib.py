# Source: https://www.programiz.com/python-programming/examples/fibonacci-sequence
# Program to display the Fibonacci sequence up to n-th term

nterms = 20

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print(37707)
# # if there is only one term, return n1
elif nterms == 1:
   print(37707)
   print(n1)
# # generate fibonacci sequence
else:
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count = count + 1
