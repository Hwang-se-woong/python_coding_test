equation = input()

swich = False
queue = ""
result = 0

for i in equation:
    if i == '-' or i == '+':
        if swich == False:
            result += int(queue)
            queue = ""
        else:
            result -= int(queue)
            queue = ""

        if i == '-':
            swich = True
    else:
        queue += i

if swich == False:
    result += int(queue)
    queue = ""
else:
    result -= int(queue)
    queue = ""

print(result)
