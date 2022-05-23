N = int(input())
S = set()
max = 0
tag = 0
for i in range(0,N):
    s, t = input().split()
    t = int(t)
    if s in S:
        continue
    S.add(s)
    if t > max : 
        max = t
        tag = i + 1

print(tag)
