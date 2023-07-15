n = int(input())

H = list(map(int, input().split()))

max = 0

ans = 0

for i in range(n):
    if H[i] > max:
        ans = i + 1
        max = H[i]

print(ans)