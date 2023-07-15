from decimal import Decimal
import math

INF = 10**18

n, m = map(int, input().split())

sm = math.ceil(math.sqrt(m))

ans = INF

for a in range(1, sm+10):
    b = math.ceil(m/a)
    # print(a, b)
    # print(a*b)
    if a > b:
        break
    if b <= n:
        ans = min(ans, a*b)


if ans == INF:
    print(-1)
else:
    print(ans)
