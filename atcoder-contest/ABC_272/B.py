import itertools

n, m = map(int, input().split())

A = list(itertools.combinations(range(1, n+1), 2))

# print(A)

for i in range(m):
    T = list(map(int, input().split()))
    k = T[0]
    T = T[1:]
    X = list(itertools.combinations(T, 2))
    for x in X:
        if x in A:
            A.remove(x)

# print(A)

if len(A):
    print("No")
else: print("Yes")
