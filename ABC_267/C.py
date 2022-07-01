n = int(input())
s = str(input())
W = list(map(int, input().split()))

P = []

for i in range(n) : 
    P.append([W[i],s[i]])

P = sorted(P, key = lambda x : x[0])

x = s.count('1')

ans = 0

for i in range(n) :
    if P[i][1] == '1' : x -= 1
    else : x += 1
    if i < (n-1) : 
        if P[i][0] != P[i+1][0] : ans = max(ans, x)
    else : ans = max(ans, x)

print(ans)

