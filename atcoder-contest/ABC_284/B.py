t = int(input())

for q in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for a in A:
        if a % 2 == 0:
            continue
        else: ans += 1
    print(ans)