import math

input_value = input()
my_list = []
maxNum = -1

for i in range(10):
    num = input_value.count(str(i))
    if i == 9:
        my_list[6] += num
        my_list[6] /= 2
        my_list[6] = math.ceil(my_list[6])
    else:
        my_list.append(num)

for i in range(len(my_list)):
    if(my_list[i] > maxNum):
        maxNum = my_list[i]

print(maxNum)
