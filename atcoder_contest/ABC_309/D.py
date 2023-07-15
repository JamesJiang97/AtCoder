from collections import deque

n1, n2, m = map(int, input().split())

graph = [[] for _ in range(n1+n2)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def BFS(graph, start):
    distance = [-1] * (n1+n2)

    distance[start] = 0

    # print(visited)
    # print(distance)

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            y = neighbor
            if distance[y] == -1:
                queue.append(y)
                distance[y] = distance[node] + 1

    return max(distance)

# print(BFS(graph1, 1))
# print(BFS(graph2, n1+n2))
a1 = BFS(graph, 0)
a2 = BFS(graph, n1+n2-1)

ans = a1 + a2 + 1

print(ans)