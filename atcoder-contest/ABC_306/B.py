A = list(map(int, input().split()))

ans = 0

for i in range(64):
    ans += A[i]*(1<<i)

print(ans)