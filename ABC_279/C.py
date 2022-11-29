from operator import *

h, w = map(int, input().split())

S = []
T = []
flag = 1

for i in range(h):
    s = input()
    temp = [0,0]
    for a in s :
        if a == '#': temp[0] += 1
        else : temp[1] += 1
    S.append(temp)

for i in range(h):
    s = input()
    temp = [0,0]
    for a in s :
        if a == '#': temp[0] += 1
        else : temp[1] += 1 
    res = eq(temp, S[i])
    if res == False :
         print('No')
         flag = 0
         break

if flag :
    print('Yes')