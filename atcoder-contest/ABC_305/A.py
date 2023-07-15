n = int(input())

u = n % 5

ans = n // 5

if u > 2:
    ans += 1

print(ans*5)