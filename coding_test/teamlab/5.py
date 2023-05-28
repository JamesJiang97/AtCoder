ans = 0

t =0

for i in reversed(range(1, 778)):
    t += i
    if t > 5000:
        ans += 1
        t = i
print(ans)