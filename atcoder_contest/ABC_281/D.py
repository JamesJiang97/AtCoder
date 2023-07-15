import itertools


n, k, d = map(int, input().split())
A = list(map(int, input().split()))

S = []

s = itertools.permutations(A, k)

max = -1

for i in s :
    res = sum(i)
    if res % d == 0 and res > max : max = res

print(max)

