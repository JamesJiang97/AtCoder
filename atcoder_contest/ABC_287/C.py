def fun(v,G,seen):
    # print(seen[v])
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]: continue
        fun(v2,G, seen)
    return


N, M = map(int, input().split())

if N-M !=1: print('No')
else:
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())

        G[a-1].append(b-1)

        G[b-1].append(a-1)
    
    flag = False

    v = 0

    for i in range(len(G)):
        if len(G[i]) > 2 : flag = True
        if len(G[i]) == 1: v = i

    if flag : print('No')
    else:
        seen = [False for _ in range(N)] 

        # fun(s, G, seen)

        for i in range(N):
            # print(v)
            seen[v] = True
            for v2 in G[v]:
                if seen[v2]: continue
                v = v2
        # print(seen)

        if False in seen: print('No')
        else: print('Yes')



