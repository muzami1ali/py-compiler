
def twoSum(target:int)->int:
    lst = [2,7,11,15]
    size  = len(lst)
    x = 0
    y = 0
    while x < size:
        while y < size:
            first = lst[x]
            scnd = lst[y]
            sum = first + scnd
            if sum == target:
                print("The indices are: [{},{}]".format(x,y))
                return 0
            y = y + 1
        y = 0
        x = x + 1
    return 0

twoSum(9)

