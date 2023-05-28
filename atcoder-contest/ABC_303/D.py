import re
x, y, z = map(int, input().split())
S = input()

all = re.findall(r'[A-Z]+|[a-z]+', S)

CapsLock = False

time = 0


for a in all:
    # print(CapsLock)
    if a[0] == 'A' and CapsLock == True:
        time += len(a)*x
    elif a[0] == 'a' and CapsLock == False:
        time += len(a)*x
    elif a[0] == 'A' and CapsLock == False:
        if len(a)*y >= z+len(a)*x:
            CapsLock = True
            time += z+len(a)*x
        else:
            time += len(a)*y
    else:
        if len(a)*y >= z+len(a)*x:
            CapsLock = False
            time += z+len(a)*x
        else:
            time += len(a)*y

print(time)
