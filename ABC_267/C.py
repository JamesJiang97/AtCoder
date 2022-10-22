n, m = map(int, input().split())

A = list(map(int, input().split()))



cur = 0

sum = 0


for i in range(m):
    sum = sum + A[i]

for i in range(m):
    cur = cur + (i+1)*A[i]


best = cur

for i in range(m, n):
    cur = cur - sum + m*A[i]
    sum = sum - A[i-m] + A[i]
    best = max(cur,best)
    #print(best)

print(best)