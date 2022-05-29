import heapq
import math


n, m = map(int, input().split())

A = list(map(int, input().split()))

for i in range(n):
    A[i] = -A[i]

heapq.heapify(A)


for i in range(m):
    A[0] = A[0]/2
    a = heapq.heappop(A)
    a = math.ceil(a)
    heapq.heappush(A, a)

A[0] = math.ceil(A[0])

ans = -sum(A)

print(ans)