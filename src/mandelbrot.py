def z(n:float,ci:float)->float:
    if n==0.0:
        return 0.0
    else:
        return z(n - 1.0, ci) ** 2.0 + ci

i = 0.0
while i < 10.0:
    print("z({}) = {}".format(i,z(i,1.0)))
    i = i + 1.0

