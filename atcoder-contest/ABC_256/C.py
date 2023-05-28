I = list(map(int, input().split()))
H = I[0:3]
W = I[3:6]

ans = 0

for a in range(1, 31) : 
    for b in range(1, 31) : 
        for d in range(1, 31) : 
            for e in range(1, 31) : 
                c = H[0] - a - b
                f = H[1] - d - e
                g = W[0] - a - d
                h = W[1] - b - e 
                i = W[2] - c - f
                if min(c, f, g, h, i) > 0 and i == H[2] - g - h : 
                    ans += 1

print(ans)