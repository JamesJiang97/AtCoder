a, b, c, d, e, f = map(int, input().split())

X = 998244353

a = a % X
b = b % X
c = c % X
d = d % X
e = e % X
f = f % X

ab = (a*b)%X
abc = (ab*c)%X
de = (d*e)%X
dex = (de*f)%X

ans = abc-dex
print(ans)