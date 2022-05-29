n, a, b = map(int, input().split())

SUM = (n*(n+1)) // 2

aa = n // a
bb = n // b

ab = n // (a*b)

saa = (aa*(aa+1))//2
sbb = (bb*(bb+1))//2
sab = (ab*(ab+1))//2

SUM -= a*saa
SUM -= b*sbb
SUM += ab*sab

print(SUM)
