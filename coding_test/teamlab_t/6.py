ans = 1

track = 0

for i in reversed(range(501)):
    track += i
    
    if track > 5000:
        track = i
        ans += 1

print(ans)