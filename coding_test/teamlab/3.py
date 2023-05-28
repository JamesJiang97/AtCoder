S = list('ABCDEFGJKQTVWXYZ')

import itertools

A = itertools.product(S, repeat=5)

ans = 0

T1 = []

for a in A:
    if 'A' in a and a[1] != 'A' :
        T1.append(a)
        # print(a)
T2 = []
for a in T1:
    if 'E' in a and a[3]!= 'E' :
        T2.append(a)
        # print(a)
T3 = []
for a in T2:
    if 'T' in a and a[1]!= 'T' :
        T3.append(a)
        print(a)


# and 'E' in a and a[3]!= 'E' and 'T' in a and a[1]!= 'T' 

print(len(T3))