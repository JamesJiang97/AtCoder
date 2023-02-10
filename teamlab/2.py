i = 0
ans = 0
while i < 9999:
    t = (i+1)*(i+2)/(i+3)
    ans += t
    i += 3

print(ans)
