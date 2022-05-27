S = input()

n = len(S) - 1

ans = int(S)

for bit in range(1, 1<<(n)):
    sta = 0
    end = n + 1
    for i in range(n) :
        if bit & (1<<i) :
            ans += int(S[sta:i+1])
            sta = i+1
    
    ans += int(S[sta:end])

print(ans)