import math


n, x = map(int, input().split())

ans = math.ceil(x/n) 

ans = chr(64 + ans)

print(ans)