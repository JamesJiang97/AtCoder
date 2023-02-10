ans = 0

for i in range(58):
    if i % 2 == 1:
        ans += i*i*i

print(ans)