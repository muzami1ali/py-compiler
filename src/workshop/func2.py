
def recur(n:int)->None:
    if n < 10:
        print(n)
        recur(n+1)
    else:
        print(False)

recur(0)
