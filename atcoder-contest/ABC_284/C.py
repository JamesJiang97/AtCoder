def dfs(v, G, seen):
    seen[v] = True
    for v2 in G[v]:

        if seen[v2]: continue

        dfs(v2, G, seen)
    return


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())

    G[a-1].append(b-1)

    G[b-1].append(a-1)

seen = [False for _ in range(N)] 
ans = 0 

for v in range(N):

    if seen[v]: continue

    dfs(v, G, seen)
    ans += 1

print(ans)