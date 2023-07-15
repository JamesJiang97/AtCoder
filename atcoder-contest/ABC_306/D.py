n = int(input())

dp = [[0,0] for i in range(n+1)]



for i in range(1, n+1):
    x,y = map(int,input().split())
    if x == 1:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + y)
    else:
        dp[i][0] = max(dp[i-1][0] + y, dp[i-1][1] + y, dp[i-1][0])
        dp[i][1] = dp[i-1][1]

print(max(dp[n][0], dp[n][1]))