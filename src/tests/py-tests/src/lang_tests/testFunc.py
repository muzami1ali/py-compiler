# Run-time:
#    stdout:
#      10.000000
#      420.250000
#      20
#      100000000
#      10
#      0
#      1
#      2
#      3
#      4
#      5
#      6
#      7
#      8
#      9
#      True
#      30
#      20
#      0
#      1
#      2
#      3
#      4
#      5
#      6
#      7
#      8
#      9
#      True
#      0
#      1
#      2
#      3
#      4
#      5
#      6
#      7
#      8
#      9
#      False
#      11
#      1


foo = 10.0
print(foo)
print(20.5**2)

def test(wow:int)->None:
    i = 0
    baz = wow + 10
    print(baz)
    if wow == 10:
        print(100000000)
    print(wow)
    while i < 10 :
        print(i)
        i = i + 1
    print(True)

test(10)
test(20)


def recur(n:int)->None:
    if n < 10:
        print(n)
        recur(n+1)
    else:
        print(False)

recur(0)

def test1()->int:
    if (True):
        return 1
    else:
        return 0

print(10+test1())
print(test1())