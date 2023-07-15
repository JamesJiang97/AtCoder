from collections import defaultdict, deque


def bfs(graph, start, h, visited, pairs):
    queue = deque([(start, h)])

    while queue:
        node, h = queue.popleft()
        if node in pairs:
            h = max(h, pairs[node])
        if h < 0:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, h - 1))

def radiated_vertices(edges, pairs):

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)


    pairsS = dict(sorted(pairs.items(), key=lambda x: x[1], reverse=True))



    visited = set()
    for p, h in pairsS.items():
        if p not in visited:
            bfs(graph, p, h, visited, pairsS)
    
    visited = sorted(list(visited))
    return len(visited), ' '.join(map(str, visited))


n, m, k = map(int, input().split())



edges = [tuple(map(int, input().split())) for _ in range(m)]
pairs = {}
for _ in range(k):
    v, p = map(int, input().split())
    pairs[v] = p

l, ans = radiated_vertices(edges, pairs)

print(l)

print(ans)
