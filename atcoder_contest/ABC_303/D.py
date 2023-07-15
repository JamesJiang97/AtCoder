
# DP
#

x, y, z = map(int, input().split())
S = input()

inf = 10**9+7

dp = [[inf,inf] for _ in range(len(S)+1)]

dp[0][0] = 0

for i in range(len(S)):
    s = S[i]
    if s == 'A': cur = 1
    else: cur = 0
    if cur ==0 :
        dp[i+1][0] = min(dp[i][0]+x, dp[i][1]+z+x)
        dp[i+1][1] = min(dp[i][0]+z+y, dp[i][1]+y)
    else:
        dp[i+1][1] = min(dp[i][1]+x, dp[i][0]+z+x)
        dp[i+1][0] = min(dp[i][0]+y, dp[i][1]+z+y)
print(min(dp[-1][0], dp[-1][1]))