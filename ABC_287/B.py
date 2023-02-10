n, m = map(int,input().split())

dict = {}

for i in range(n):
    s = input()
    s = s[3:]
    if s in dict: dict[s] +=1
    else: dict.update({s:1})

ans = 0
set = set()

for i in range(m):
    t = input()
    if t not in set: set.add(t)

for t in set:
    if t in dict: ans += dict[t]
    

print(ans)
