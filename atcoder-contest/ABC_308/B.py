n, m = map(int, input().split())   

C = list(input().split())
D = list(input().split())

P = list(map(int, input().split()))

p0 = P[0]

P = P[1:]

dict = {}

for d, p in zip(D, P):
    dict[d] = p

ans = 0

for c in C:
    if c in dict:
        ans += dict[c]
    else:
        ans += p0

print(ans)