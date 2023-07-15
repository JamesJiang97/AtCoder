
L = {}
A = [1]

def dfs(s, f):
    for i in L[s]:
        if A.count(i) == 0:
            A.append(i)
            dfs(i, s)
        else :continue


n = int(input())



for i in range(n) :
    a, b = map(int, input().split())
    if a in L :
        L[a].append(b)
    else:
        L.update({a:[b]})
    if b in L :
        L[b].append(a)
    else:
        L.update({b:[a]})


tag = 1

if 1 not in L :
    print(1)
    tag = 0
else:
    dfs(1, -1)
if tag : print(max(A))
