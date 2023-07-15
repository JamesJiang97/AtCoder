n, d = map(int, input().split())


import math
from collections import deque

def reachable_points(start, points, d):
    reachable = [points.index(start)]
    visited = set(reachable)
    queue = deque(reachable)
    
    while queue:
        current_index = queue.popleft()
        for index, point in enumerate(points):
            if index not in visited and math.sqrt((point[0] - points[current_index][0])**2 + (point[1] - points[current_index][1])**2) <= d:
                queue.append(index)
                reachable.append(index)
                visited.add(index)
    
    return reachable


points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

start = points[0]

li = reachable_points(start, points, d)

for i in range(n):
    if i in li:
        print("Yes")
        
    else:
        print("No")
        