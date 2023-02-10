ans = 0

for i in range(1, 5000001):
    s = list(str(i))
    t = 0
    for x in s:
        t += int(x)
    if i%t == 0 : ans += 1

print(ans)
