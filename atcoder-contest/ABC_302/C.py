import itertools


n, m = map(int, input().split())

S = [input() for _ in range(n)]

for l in itertools.permutations(S):
    ans = [0] * (n-1)
    for i in range(n - 1):
        for a, b in zip(l[i], l[i + 1]):
            if a == b:
                continue
            else:
                ans[i] += 1
    flag = True
    # print(ans)
    for a in ans:
        if a == 1:
            continue
        else:
            flag = False
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")


