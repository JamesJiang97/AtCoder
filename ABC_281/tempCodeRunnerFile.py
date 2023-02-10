import itertools


n, k, d = map(int, input().split())
A = list(map(int, input().split()))

S = []

s = itertools.combinations(A, k)

flag = True

for i in s :
    S.append(sum(i))

list.sort(S, reverse=True)


for i in S:
    if i % d == 0:
        print(i)
        flag = False
        break

if flag:    
    print(-1)

