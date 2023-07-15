h, w = map(int, input().split())

C = []

for i in range(h):
    C.append(list(input()))


for i in range(w):
    ans = 0
    for j in range(h):
        if C[j][i] =="#" : ans += 1
    if i == w-1: print(ans, end ="")
    else: print(ans, end=" ")