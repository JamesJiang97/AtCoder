import itertools


n, m = map(int, input().split())

S = [input() for _ in range(n)]

for l in itertools.permutations(S):
    ans = [0] * 3
    for i in range(n - 1):
        for a, b in zip(l[i], l[i + 1]):
            if a == b:
                continue
            else:
                ans[i] += 1
    if ans[0] == ans[1] == ans[2] == 1:
        print('Yes')
        exit()

print('No')