N, M = map(int,input().split())

root = [i for i in range(N+1)] 


rank = [0]*(N+1)


def find(x):

    if root[x] == x:
        return x
    else:
        root[x] = find(root[x]) 
        return root[x]
        

def same(x,y):
    return find(x) == find(y)


def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0

    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

ans = 0

for i in range(M):
    a, b = map(int,input().split())
    if same(a,b): ans += 1
    else: unite(a,b)



print(ans)
