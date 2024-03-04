
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

double_list = [1.0,0.5]
double_list.append(10.0)
double_list.append(20.0)
print(double_list[0] + 5.0)
print(double_list[1] + 5)
