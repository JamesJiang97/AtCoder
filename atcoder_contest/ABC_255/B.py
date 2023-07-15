import math


n, k = map(int, input().split())

A = list(map(int, input().split()))

P = []

L = []

for i in range(n) : 
    P.append(list(map(int, input().split())))

for n in A :
    L.append(P[n-1])

maxvalue = []

for i in range(n) :
    minvalue = math.sqrt(2000000)
    #if A.count(i+1) == 0 :
    x1 = float(P[i][0])
    y1 = float(P[i][1])
    for j in  range(k) :
        x2 = float(L[j][0])
        y2 = float(L[j][1])
        dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if dis < minvalue : minvalue = dis
        maxvalue.append(minvalue)

print(max(maxvalue))
