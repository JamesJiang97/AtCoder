import heapq
import math


n, m = map(int, input().split())

G = [[] for i in range(n+1)]

ans = [-1] * (n+1)

dist = [math.inf] * (n+1)


for i in range(m) : 
    a, b, c = map(int, input().split())
    G[a].append([b, c, i + 1])

cur = 1
dist[1] = 0
pq = []
heapq.heappush(pq, (0,1))

while pq :
    d, cur = heapq.heappop(pq)
    if(dist[cur] != d) : continue
    for j in G[cur] :
        if dist[j[0]] > dist[cur] + j[1] :
            dist[j[0]] = int(dist[cur] + j[1])
            heapq.heappush(pq, (dist[j[0]], j[0]))
            ans[j[0]] = j[2]

for i in ans :
    if i != -1 :
        print(i, end = " ")