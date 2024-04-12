# Run-time:
#   stdout:
#      82
#      108
#      110
#      6
#      We are done with the first list
#      32
#      testing f-string 32
#      6.000000
#      5.500000
#      4
#      The first element of the first list is: 32. The first element of the second list: 1.000000

var = [32,58,60]
var.append(100)
var.append(200)
var.append(300)
print(var[0] + 50)
print(var[1] + 50)
print(var[2] + 50)
print(len(var))
print('We are done with the first list')
print(var[0])
print("testing f-string {}".format(var[0]))

double_list = [1.0,0.5]
double_list.append(10.0)
double_list.append(20.0)
print(double_list[0] + 5.0)
print(double_list[1] + 5)
print(len(double_list))
print("The first element of the first list is: {}. The first element of the second list: {}".format(var[0],double_list[0]))
