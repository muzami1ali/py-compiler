
# foo = 200
# def test()->int:
#     return 100
# var = [32,58,60,foo, test()]
var = [32,58,60]
# var[0] = 10
var.append(100)
var.append(200)
var.append(300)
print(var[0] + 50)
print(var[1] + 50)
print(var[2] + 50)
print(len(var))
print("we are done with the first list")
print('We are done with the first list')
print(var[0])
print("testing f-string {}".format(var[0]))
# print("""I am done with the first list""")

double_list = [1.0,0.5]
double_list.append(10.0)
double_list.append(20.0)
print(double_list[0] + 5.0)
print(double_list[1] + 5)
print(len(double_list))
print("The first element of the  first list is: {var}. The first element of the second list: {double}".format(var[0],double_list[0]))
