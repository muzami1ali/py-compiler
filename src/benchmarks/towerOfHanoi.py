# This is a recursive function that solves the Tower of Hanoi problem
# This code was taken from https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# This was slightly modified to work with this compiler



def towerOfHanoi(n:int, start:int, middle:int, end:int)->None:
    if n == 1:
        print("Move disk 1 from source {} to target {}".format(start, end))
    else: 
        towerOfHanoi(n-1, start, middle, end)
        print("Move disk {} from source {} to target {}".format(n, start, end))      
        towerOfHanoi(n-1, middle, start, end)

towerOfHanoi(3, 0, 2, 1)