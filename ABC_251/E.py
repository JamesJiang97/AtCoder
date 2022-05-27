import math


N = int(input())
A = list(map(int, input().split()))

dp = [[0,0] for i in range (300005)]

ans = math.inf

for t in range(2) :
    dp[1][t] = A[0] * t
    dp[1][1-t] = math.inf
    for i in range(2, N+1) :
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + A[i-1]
    if t == 0 : ans = min(ans, dp[N][1])
    if t == 1 : ans = min(ans, min(dp[N][0], dp[N][1]))

print(ans)