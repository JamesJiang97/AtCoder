import itertools


n, m = map(int,input().split())

S = []

for i in range(n):
    S.append(input())

C = itertools.combinations(S, 2)

ans = 0

for c in C:
    c1 = c[0]
    c2 = c[1]
    flag = 1
    for i in range(m):
        if c1[i] != 'o' and c2[i] != 'o':
            flag = 0
            break
    if flag: ans+=1

print(ans)
