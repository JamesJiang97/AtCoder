import itertools

n, m = map(int, input().split())

N = [i for i in range(1, n+1)]

li = list(itertools.combinations(N, 2))

for p in range(m):
    A = list(map(int, input().split()))
    for i in range(len(A)-1):
        # print(i)
        pair = (A[i], A[i+1])
        pair2 = (A[i+1], A[i])
        if pair in li:
            li.remove(pair)
        elif pair2 in li:
            li.remove(pair2)

print(len(li))