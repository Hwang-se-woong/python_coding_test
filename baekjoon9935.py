import sys

s = input()
boomS = input()

tmp = True

while tmp:
    if boomS in s:
        s = s.replace(boomS, "")
    else:
        tmp = False

if s == "":
    print("FRULA")
else:
    print(s)
