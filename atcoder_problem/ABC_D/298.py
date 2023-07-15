from collections import deque

Mod=998244353

q = int(input())

power=[1]*(q+1)

for i in range(1,q+1):
    power[i]=(10*power[i-1])%Mod

S = deque([1])

ans = 1

Ans = []

for _ in range(q):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        ans = (ans*10+Q[1])%Mod
        S.append(Q[1])
    elif Q[0] == 2:
        a = S.popleft()
        l = len(S)
        ans = (ans-a*power[l])%Mod
    else:
        Ans.append(ans)

import sys

write=sys.stdout.write

write("\n".join(map(str,Ans)))